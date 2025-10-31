+++
date = '2025-10-31T00:00:00+08:00'
draft = false
title = 'IntelliJ IDEA Community Edition使用教學'
tags = ['教學', '工具']
categories = ['教學']
+++
# IntelliJ IDEA Community Edition 使用教學手冊

## 文件資訊
- **版本**: 1.0
- **建立日期**: 2025年8月29日
- **適用對象**: Java 後端開發新進人員
- **IDE 版本**: IntelliJ IDEA Community Edition 2023.3+

---

## 目錄

1. [IntelliJ IDEA CE 下載與安裝](#1-intellij-idea-ce-下載與安裝)
   - [1.1 下載 IntelliJ IDEA Community Edition](#11-下載-intellij-idea-community-edition)
   - [1.2 安裝步驟](#12-安裝步驟)
   - [1.3 首次啟動設定](#13-首次啟動設定)
   - [1.4 授權與隱私設定](#14-授權與隱私設定)

2. [開發環境基本設定](#2-開發環境基本設定)
   - [2.1 JDK 設定](#21-jdk-設定)
   - [2.2 Maven 整合設定](#22-maven-整合設定)
   - [2.3 編碼設定](#23-編碼設定)
   - [2.4 Code Style 設定](#24-code-style-設定)
   - [2.5 檢查器設定](#25-檢查器設定)

3. [匯入專案與建立新專案](#3-匯入專案與建立新專案)
   - [3.1 匯入現有專案](#31-匯入現有專案)
   - [3.2 建立新專案](#32-建立新專案)
   - [3.3 專案設定優化](#33-專案設定優化)

4. [與 Git/GitHub/GitLab 的整合](#4-與-gitgithubgitlab-的整合)
   - [4.1 Git 基本設定](#41-git-基本設定)
   - [4.2 本地版本控制操作](#42-本地版本控制操作)
   - [4.3 遠端儲存庫整合](#43-遠端儲存庫整合)
   - [4.4 分支管理](#44-分支管理)
   - [4.5 處理合併衝突](#45-處理合併衝突)
   - [4.6 Pull Request / Merge Request 管理](#46-pull-request--merge-request-管理)

5. [專案編譯與執行](#5-專案編譯與執行)
   - [5.1 Maven 專案編譯](#51-maven-專案編譯)
   - [5.2 執行 Java 應用程式](#52-執行-java-應用程式)
   - [5.3 Spring Boot 專案執行](#53-spring-boot-專案執行)
   - [5.4 建立和管理執行配置](#54-建立和管理執行配置)
   - [5.5 建置和部署](#55-建置和部署)

6. [Debug 與單元測試](#6-debug-與單元測試)
   - [6.1 Debug 基本操作](#61-debug-基本操作)
   - [6.2 Debug 視窗操作](#62-debug-視窗操作)
   - [6.3 進階 Debug 技巧](#63-進階-debug-技巧)
   - [6.4 單元測試](#64-單元測試)
   - [6.5 測試執行和管理](#65-測試執行和管理)
   - [6.6 Mock 測試](#66-mock-測試)

7. [常用快捷鍵與開發小技巧](#7-常用快捷鍵與開發小技巧)
   - [7.1 基本快捷鍵](#71-基本快捷鍵)
   - [7.2 導航快捷鍵](#72-導航快捷鍵)
   - [7.3 程式碼產生快捷鍵](#73-程式碼產生快捷鍵)
   - [7.4 重構快捷鍵](#74-重構快捷鍵)
   - [7.5 執行和除錯快捷鍵](#75-執行和除錯快捷鍵)
   - [7.6 開發小技巧](#76-開發小技巧)

8. [插件管理與擴展功能](#8-插件管理與擴展功能)
   - [8.1 插件安裝與管理](#81-插件安裝與管理)
   - [8.2 開發效率插件](#82-開發效率插件)
   - [8.3 程式碼品質插件](#83-程式碼品質插件)
   - [8.4 資料庫相關插件](#84-資料庫相關插件)
   - [8.5 測試輔助插件](#85-測試輔助插件)
   - [8.6 主題和外觀插件](#86-主題和外觀插件)
   - [8.7 團隊協作插件](#87-團隊協作插件)
   - [8.8 插件開發基礎](#88-插件開發基礎)

9. [資料庫整合與工具](#9-資料庫整合與工具)
   - [9.1 Database Tool Window](#91-database-tool-window)
   - [9.2 SQL 查詢和管理](#92-sql-查詢和管理)
   - [9.3 資料庫結構管理](#93-資料庫結構管理)
   - [9.4 與 JPA/Hibernate 整合](#94-與-jpahibernate-整合)
   - [9.5 資料庫效能分析](#95-資料庫效能分析)
   - [9.6 資料庫測試環境](#96-資料庫測試環境)

10. [效能調校與疑難排解](#10-效能調校與疑難排解)
    - [10.1 IDE 效能優化](#101-ide-效能優化)
    - [10.2 專案載入優化](#102-專案載入優化)
    - [10.3 常見效能問題](#103-常見效能問題)
    - [10.4 效能監控工具](#104-效能監控工具)
    - [10.5 疑難排解指南](#105-疑難排解指南)
    - [10.6 系統整合問題](#106-系統整合問題)

11. [專案最佳實務](#11-專案最佳實務)
    - [11.1 程式碼格式化和風格](#111-程式碼格式化和風格)
    - [11.2 註解和文件](#112-註解和文件)
    - [11.3 套件管理和依賴](#113-套件管理和依賴)
    - [11.4 設定檔管理](#114-設定檔管理)
    - [11.5 例外處理和日誌](#115-例外處理和日誌)
    - [11.6 測試策略](#116-測試策略)
    - [11.7 效能最佳化](#117-效能最佳化)
    - [11.8 安全性考量](#118-安全性考量)

12. [常見問題與解決方案](#12-常見問題與解決方案)
    - [12.1 安裝和設定問題](#121-安裝和設定問題)
    - [12.2 專案匯入問題](#122-專案匯入問題)
    - [12.3 編譯和執行問題](#123-編譯和執行問題)
    - [12.4 Git 整合問題](#124-git-整合問題)
    - [12.5 效能相關問題](#125-效能相關問題)
    - [12.6 插件相關問題](#126-插件相關問題)
    - [12.7 除錯問題](#127-除錯問題)
    - [12.8 快速診斷檢查清單](#128-快速診斷檢查清單)

13. [檢查清單](#13-檢查清單)
    - [13.1 安裝和設定檢查清單](#131-安裝和設定檢查清單)
    - [13.2 專案開發檢查清單](#132-專案開發檢查清單)
    - [13.3 資料庫整合檢查清單](#133-資料庫整合檢查清單)
    - [13.4 團隊協作檢查清單](#134-團隊協作檢查清單)
    - [13.5 效能和安全檢查清單](#135-效能和安全檢查清單)
    - [13.6 日常開發檢查清單](#136-日常開發檢查清單)
    - [13.7 問題排除檢查清單](#137-問題排除檢查清單)

---

## 1. IntelliJ IDEA CE 下載與安裝

### 1.1 下載 IntelliJ IDEA Community Edition

#### 步驟說明
1. 前往 JetBrains 官方網站：[https://www.jetbrains.com/idea/](https://www.jetbrains.com/idea/)
2. 點選「Download」按鈕
3. 選擇「Community Edition」（免費版本）
4. 根據作業系統選擇對應版本：
   - Windows: `.exe` 安裝檔
   - macOS: `.dmg` 安裝檔
   - Linux: `.tar.gz` 壓縮檔

#### 系統需求
- **記憶體**: 最少 2GB RAM，建議 8GB 以上
- **磁碟空間**: 至少 3.5GB 可用空間
- **解析度**: 1024x768 以上
- **作業系統**: 
  - Windows 10/11 (64-bit)
  - macOS 10.14+
  - Linux (64-bit)

### 1.2 安裝步驟

#### Windows 安裝
1. 執行下載的 `.exe` 檔案
2. 點選「Next」進入安裝精靈
3. 選擇安裝路徑（建議使用預設路徑）
4. 選擇安裝選項：
   - ✅ 建立桌面捷徑
   - ✅ 更新系統 PATH 變數
   - ✅ 關聯 .java 檔案
   - ✅ 下載並安裝 32-bit JetBrains Runtime
5. 點選「Install」開始安裝
6. 安裝完成後選擇「Finish」

#### macOS 安裝
1. 開啟下載的 `.dmg` 檔案
2. 將 IntelliJ IDEA CE 拖曳到 Applications 資料夾
3. 從 Applications 資料夾執行 IntelliJ IDEA

#### Linux 安裝
```bash
# 解壓縮檔案
tar -xzf ideaIC-*.tar.gz

# 移動到 opt 目錄
sudo mv idea-IC-* /opt/intellij-idea-community

# 建立執行檔連結
sudo ln -s /opt/intellij-idea-community/bin/idea.sh /usr/local/bin/idea

# 執行 IDEA
idea
```

### 1.3 首次啟動設定

#### 初始設定精靈
1. **匯入設定**: 如果是首次安裝，選擇「Do not import settings」
2. **選擇 UI 主題**: 
   - Light（淺色主題）
   - Dark（深色主題，建議）
   - High contrast（高對比）
3. **選擇鍵盤對應**: 
   - IntelliJ IDEA Classic
   - Eclipse
   - Visual Studio
   - Emacs
4. **安裝插件**: 可以跳過，稍後再安裝

#### 注意事項
- 首次啟動可能需要較長時間進行索引
- 建議在安裝完成後重新啟動電腦
- 確保系統已安裝 Java 8 或更高版本

### 1.4 授權與隱私設定

#### 同意使用條款
1. 閱讀並同意 JetBrains 使用者協議
2. 選擇是否傳送匿名使用統計資料（建議不傳送）
3. 設定自動更新偏好（建議開啟）

#### 實務建議
- 定期檢查更新以獲得最新功能和安全修補
- 關閉不必要的資料收集功能以保護隱私
- 備份 IDE 設定檔以便在重新安裝時快速復原

---

## 2. 開發環境基本設定

### 2.1 JDK 設定

#### 檢查並設定 Project SDK
1. 開啟 IntelliJ IDEA
2. 前往 `File` → `Project Structure` (Ctrl+Alt+Shift+S)
3. 在左側選單點選「Project」
4. 設定 Project SDK：
   - 如果已安裝 JDK，從下拉選單選擇
   - 如果未安裝，點選「Add SDK」→「Download JDK」

#### 推薦 JDK 版本
```
優先順序：
1. OpenJDK 17 (LTS) - 推薦用於新專案
2. OpenJDK 11 (LTS) - 適合維護既有專案
3. Oracle JDK 8 (LTS) - 適合舊版專案

下載來源：
- Adoptium (Eclipse Temurin)
- Amazon Corretto
- Oracle OpenJDK
```

#### 設定 JAVA_HOME 環境變數
**Windows:**
```powershell
# 設定 JAVA_HOME
[Environment]::SetEnvironmentVariable("JAVA_HOME", "C:\Program Files\Java\jdk-17", "Machine")

# 更新 PATH
$path = [Environment]::GetEnvironmentVariable("PATH", "Machine")
[Environment]::SetEnvironmentVariable("PATH", "$path;%JAVA_HOME%\bin", "Machine")
```

**macOS/Linux:**
```bash
# 編輯 ~/.bashrc 或 ~/.zshrc
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
export PATH=$JAVA_HOME/bin:$PATH

# 重新載入設定
source ~/.bashrc
```

### 2.2 Maven 整合設定

#### 設定 Maven 路徑
1. 前往 `File` → `Settings` (Ctrl+Alt+S)
2. 展開「Build, Execution, Deployment」→「Build Tools」→「Maven」
3. 設定 Maven 相關路徑：
   - **Maven home path**: Maven 安裝目錄
   - **User settings file**: `~/.m2/settings.xml`
   - **Local repository**: `~/.m2/repository`

#### Maven 配置檔案範例
```xml
<!-- ~/.m2/settings.xml -->
<?xml version="1.0" encoding="UTF-8"?>
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0">
  <localRepository>${user.home}/.m2/repository</localRepository>
  
  <mirrors>
    <mirror>
      <id>central</id>
      <mirrorOf>central</mirrorOf>
      <name>Central Repository</name>
      <url>https://repo1.maven.org/maven2</url>
    </mirror>
  </mirrors>
  
  <profiles>
    <profile>
      <id>jdk-17</id>
      <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
      </properties>
    </profile>
  </profiles>
  
  <activeProfiles>
    <activeProfile>jdk-17</activeProfile>
  </activeProfiles>
</settings>
```

#### Maven 匯入設定
1. 在 Settings 中前往「Build Tools」→「Maven」→「Importing」
2. 建議設定：
   - ✅ Import Maven projects automatically
   - ✅ Automatically download sources
   - ✅ Automatically download documentation
   - VM options for importer: `-Xmx1024m`

### 2.3 編碼設定

#### 檔案編碼設定
1. 前往 `File` → `Settings` → `Editor` → `File Encodings`
2. 設定所有編碼為 **UTF-8**：
   - Global Encoding: UTF-8
   - Project Encoding: UTF-8
   - Default encoding for properties files: UTF-8
   - ✅ Transparent native-to-ascii conversion

#### IDE 編碼設定
1. 在 IDE 啟動參數中加入：
```
-Dfile.encoding=UTF-8
-Dconsole.encoding=UTF-8
```

2. 編輯 `idea64.exe.vmoptions` 檔案（Windows）：
```
-Dfile.encoding=UTF-8
-Dconsole.encoding=UTF-8
-Dsun.jnu.encoding=UTF-8
```

### 2.4 Code Style 設定

#### Java 程式碼風格
1. 前往 `File` → `Settings` → `Editor` → `Code Style` → `Java`
2. 建議設定：

**縮排設定:**
```
Tab size: 4
Indent: 4
Continuation indent: 8
☑ Use tab character: 取消勾選（使用空格）
```

**換行設定:**
```
Right margin: 120
☑ Wrap on typing: 勾選
```

**匯入設定:**
```
Class count to use import with '*': 10
Names count to use static import with '*': 5
☑ Use single class import: 勾選
Import layout:
- import static all other imports
- <blank line>
- import java.*
- import javax.*
- <blank line>
- import all other imports
```

#### 匯入程式碼風格設定檔
```xml
<!-- Java-Code-Style.xml -->
<code_scheme name="Company Standard">
  <option name="RIGHT_MARGIN" value="120" />
  <JavaCodeStyleSettings>
    <option name="CLASS_COUNT_TO_USE_IMPORT_ON_DEMAND" value="10" />
    <option name="NAMES_COUNT_TO_USE_IMPORT_ON_DEMAND" value="5" />
    <option name="IMPORT_LAYOUT_TABLE">
      <value>
        <package name="" withSubpackages="true" static="true" />
        <emptyLine />
        <package name="java" withSubpackages="true" static="false" />
        <package name="javax" withSubpackages="true" static="false" />
        <emptyLine />
        <package name="" withSubpackages="true" static="false" />
      </value>
    </option>
  </JavaCodeStyleSettings>
</code_scheme>
```

### 2.5 檢查器設定

#### 啟用程式碼檢查
1. 前往 `File` → `Settings` → `Editor` → `Inspections`
2. 建議啟用的檢查項目：
   - ✅ Java → Code style issues
   - ✅ Java → Probable bugs
   - ✅ Java → Performance issues
   - ✅ Java → Security issues
   - ✅ Spelling

#### 自訂檢查規則
```xml
<!-- 常用檢查規則設定 -->
<inspections>
  <inspection class="JavaDoc" enabled="true" level="WARNING" />
  <inspection class="UnusedImport" enabled="true" level="WARNING" />
  <inspection class="MissingOverrideAnnotation" enabled="true" level="WARNING" />
  <inspection class="UnnecessaryLocalVariable" enabled="true" level="INFO" />
</inspections>
```

#### 實務注意事項
- 定期匯出 IDE 設定進行備份
- 團隊成員應使用相同的程式碼風格設定
- 設定完成後重新啟動 IDE 確保設定生效
- 建議建立團隊專用的設定檔案範本

---

## 3. 匯入專案與建立新專案

### 3.1 匯入現有專案

#### 匯入 Maven 專案
1. 啟動 IntelliJ IDEA
2. 選擇「Open」或「Import Project」
3. 選擇專案根目錄（包含 `pom.xml` 的目錄）
4. 選擇「Import project from external model」→「Maven」
5. 設定匯入選項：
   - ✅ Import Maven projects automatically
   - ✅ Automatically download sources and documentation
   - ✅ Search for projects recursively
6. 點選「Next」並完成匯入

#### 匯入 Gradle 專案
1. 選擇「Open」
2. 選擇包含 `build.gradle` 的專案目錄
3. 選擇「Import Gradle project」
4. 設定 Gradle 相關選項：
   - Use default gradle wrapper
   - Build and run using: Gradle
   - Run tests using: Gradle

#### 從版本控制匯入
1. 選擇「Get from VCS」
2. 輸入 Git 儲存庫 URL
3. 選擇本地目錄位置
4. 點選「Clone」
5. IntelliJ 會自動偵測專案類型並匯入

### 3.2 建立新專案

#### 建立 Maven 專案
1. 選擇「New Project」
2. 選擇「Maven」
3. 選擇 Project SDK
4. 勾選「Create from archetype」（可選）
   - `maven-archetype-quickstart`: 基本 Java 專案
   - `maven-archetype-webapp`: Web 應用程式專案
5. 設定專案資訊：
   ```
   GroupId: com.company.projectname
   ArtifactId: project-name
   Version: 1.0.0-SNAPSHOT
   ```
6. 選擇專案位置並建立

#### Maven 專案結構範例
```
project-name/
├── pom.xml
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/company/projectname/
│   │   │       └── App.java
│   │   └── resources/
│   └── test/
│       ├── java/
│       │   └── com/company/projectname/
│       │       └── AppTest.java
│       └── resources/
└── target/
```

#### Spring Boot 專案建立
1. 前往 [Spring Initializr](https://start.spring.io/)
2. 設定專案參數：
   - Project: Maven
   - Language: Java
   - Spring Boot: 3.x.x (最新穩定版)
   - Java: 17
3. 添加依賴項目：
   - Spring Web
   - Spring Data JPA
   - H2 Database（開發用）
   - Spring Boot DevTools
4. 下載並匯入到 IntelliJ IDEA

### 3.3 專案設定優化

#### 模組設定
1. 前往 `File` → `Project Structure` → `Modules`
2. 檢查模組設定：
   - Sources: `src/main/java`
   - Test Sources: `src/test/java`
   - Resources: `src/main/resources`
   - Test Resources: `src/test/resources`

#### 編譯輸出設定
1. 在 Project Structure 中設定：
   - Project compiler output: `專案目錄/target/classes`
   - Module compile output path: Use module compile output path

#### 實務建議
- 建立專案範本以統一團隊專案結構
- 使用版本控制忽略檔案（`.gitignore`）排除編譯產物
- 設定適當的專案編碼和 JDK 版本

---

## 4. 與 Git/GitHub/GitLab 的整合

### 4.1 Git 基本設定

#### 設定 Git 路徑
1. 前往 `File` → `Settings` → `Version Control` → `Git`
2. 設定 Git 執行檔路徑：
   - Windows: `C:\Program Files\Git\bin\git.exe`
   - macOS: `/usr/bin/git`
   - Linux: `/usr/bin/git`

#### 設定 Git 使用者資訊
```bash
# 在終端機執行
git config --global user.name "Your Name"
git config --global user.email "your.email@company.com"
git config --global init.defaultBranch main
```

#### IntelliJ 中的 Git 設定
1. 在 Settings → Version Control → Git 中設定：
   - ✅ Use credential helper
   - ✅ Update branches automatically
   - ✅ Auto-update if push of the current branch was rejected

### 4.2 本地版本控制操作

#### 初始化 Git 儲存庫
1. 右鍵點選專案根目錄
2. 選擇「Git」→「Initialize Repository」
3. 或使用選單：`VCS` → `Import into Version Control` → `Create Git Repository`

#### 基本 Git 操作
**新增檔案到暫存區:**
1. 在 Project 視窗中選擇檔案
2. 右鍵選擇「Git」→「Add」
3. 或使用快捷鍵 `Ctrl+Alt+A`

**提交變更:**
1. 使用快捷鍵 `Ctrl+K` 開啟 Commit 視窗
2. 選擇要提交的檔案
3. 撰寫提交訊息
4. 點選「Commit」或「Commit and Push」

**檢視變更歷史:**
1. 使用快捷鍵 `Alt+9` 開啟 Version Control 視窗
2. 點選「Log」頁籤檢視提交歷史
3. 雙擊提交記錄檢視詳細變更

### 4.3 遠端儲存庫整合

#### 添加遠端儲存庫
1. 前往 `VCS` → `Git` → `Remotes`
2. 點選「+」新增遠端儲存庫
3. 設定名稱（通常是 `origin`）和 URL

#### GitHub 整合
1. 安裝 GitHub 插件（通常已預裝）
2. 前往 `File` → `Settings` → `Version Control` → `GitHub`
3. 點選「Add account」
4. 選擇認證方式：
   - **Token**: 建議使用 Personal Access Token
   - **Log in via GitHub**: 使用瀏覽器登入

#### 建立 GitHub Personal Access Token
1. 前往 GitHub → Settings → Developer settings → Personal access tokens
2. 點選「Generate new token (classic)」
3. 設定權限：
   - ✅ repo
   - ✅ workflow
   - ✅ read:org
4. 複製 token 並在 IntelliJ 中使用

#### GitLab 整合
1. 前往 `File` → `Settings` → `Version Control` → `GitLab`
2. 新增 GitLab 伺服器設定
3. 輸入 GitLab URL 和 Access Token

### 4.4 分支管理

#### 建立和切換分支
1. 點選右下角的分支名稱
2. 選擇「New Branch」建立新分支
3. 選擇「Checkout」切換到其他分支

#### 分支操作指南
```bash
# 常用分支操作命令
git branch                    # 檢視所有分支
git branch feature/new-api   # 建立新分支
git checkout feature/new-api # 切換分支
git checkout -b hotfix/bug   # 建立並切換分支
git branch -d feature/old    # 刪除已合併分支
```

#### 合併分支
1. 切換到目標分支（通常是 `main` 或 `develop`）
2. 選擇要合併的分支 → 右鍵 → 「Merge into Current」
3. 解決衝突（如果有）
4. 提交合併結果

### 4.5 處理合併衝突

#### 識別衝突
1. IntelliJ 會自動標示有衝突的檔案
2. 衝突檔案會顯示紅色驚嘆號標記
3. 在 Version Control 視窗中檢視衝突清單

#### 解決衝突
1. 雙擊衝突檔案開啟合併工具
2. 三欄視圖顯示：
   - 左欄：目前分支版本
   - 中欄：合併結果
   - 右欄：要合併的分支版本
3. 選擇要保留的變更或手動編輯
4. 點選「Apply」完成解決

#### 衝突解決最佳實務
- 仔細檢視每個衝突的上下文
- 與相關開發人員討論複雜的衝突
- 測試合併後的程式碼
- 撰寫清楚的合併提交訊息

### 4.6 Pull Request / Merge Request 管理

#### 在 IntelliJ 中建立 Pull Request
1. 確保分支已推送到遠端
2. 前往 `VCS` → `Git` → `Create Pull Request`
3. 填寫 PR 標題和描述
4. 選擇 reviewer 和 assignee
5. 建立 Pull Request

#### 檢視和管理 PR
1. 在 Version Control 視窗中點選「Pull Requests」
2. 檢視 PR 清單和狀態
3. 點選 PR 查看詳細資訊和變更
4. 在 IDE 中直接進行 code review

---

## 5. 專案編譯與執行

### 5.1 Maven 專案編譯

#### 使用 Maven Tool Window
1. 開啟 Maven Tool Window：`View` → `Tool Windows` → `Maven`
2. 展開專案節點查看 Maven 生命週期
3. 常用編譯命令：
   - **clean**: 清理編譯產物
   - **compile**: 編譯主程式碼
   - **test-compile**: 編譯測試程式碼
   - **package**: 打包成 JAR/WAR

#### Maven 生命週期詳解
```xml
<!-- 標準 Maven 生命週期 -->
validate → compile → test → package → verify → install → deploy
```

**各階段說明:**
- `validate`: 驗證專案正確性
- `compile`: 編譯 `src/main/java` 下的程式碼
- `test`: 執行單元測試
- `package`: 將編譯後的程式碼打包成 JAR/WAR
- `install`: 安裝到本地儲存庫
- `deploy`: 部署到遠端儲存庫

#### 自訂編譯設定
1. 編輯 `pom.xml` 設定編譯選項：
```xml
<properties>
    <maven.compiler.source>17</maven.compiler.source>
    <maven.compiler.target>17</maven.compiler.target>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
</properties>

<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.11.0</version>
            <configuration>
                <source>17</source>
                <target>17</target>
                <encoding>UTF-8</encoding>
                <compilerArgs>
                    <arg>-Xlint:unchecked</arg>
                    <arg>-Xlint:deprecation</arg>
                </compilerArgs>
            </configuration>
        </plugin>
    </plugins>
</build>
```

### 5.2 執行 Java 應用程式

#### 執行主程式
1. 找到包含 `main` 方法的類別
2. 右鍵點選類別檔案 → 「Run 'ClassName.main()'」
3. 或使用快捷鍵 `Ctrl+Shift+F10`

#### 設定執行配置
1. 前往 `Run` → `Edit Configurations`
2. 點選「+」→「Application」
3. 設定執行參數：
   - **Main class**: 指定主類別
   - **Program arguments**: 程式參數
   - **VM options**: JVM 參數
   - **Working directory**: 工作目錄
   - **Environment variables**: 環境變數

#### 常用 JVM 參數範例
```bash
# 記憶體設定
-Xms512m -Xmx2g

# 垃圾回收設定
-XX:+UseG1GC -XX:MaxGCPauseMillis=200

# 系統屬性
-Dspring.profiles.active=dev
-Dfile.encoding=UTF-8

# 偵錯模式
-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005
```

### 5.3 Spring Boot 專案執行

#### 執行 Spring Boot 應用程式
1. 找到標註 `@SpringBootApplication` 的主類別
2. 右鍵執行或使用 Maven 命令：`mvn spring-boot:run`

#### Spring Boot 執行配置
```xml
<!-- pom.xml 中的 Spring Boot 插件 -->
<plugin>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-maven-plugin</artifactId>
    <version>3.1.0</version>
    <configuration>
        <mainClass>com.company.Application</mainClass>
        <jvmArguments>
            -Dspring.profiles.active=dev
            -Xms256m -Xmx1g
        </jvmArguments>
    </configuration>
</plugin>
```

#### Spring Boot 設定檔管理
```yaml
# application.yml
spring:
  profiles:
    active: dev
  datasource:
    url: jdbc:h2:mem:testdb
    driver-class-name: org.h2.Driver

server:
  port: 8080

logging:
  level:
    com.company: DEBUG
```

### 5.4 建立和管理執行配置

#### 應用程式執行配置
1. 建立新的 Application 配置
2. 設定必要參數：
```
Name: MyApp (Local)
Main class: com.company.myapp.Application
VM options: -Dspring.profiles.active=local -Xms512m
Program arguments: --debug
Working directory: $MODULE_WORKING_DIR$
```

#### Maven 執行配置
1. 建立 Maven 配置
2. 設定 Maven 目標：
```
Name: Clean Install
Command line: clean install -DskipTests
Working directory: $PROJECT_DIR$
```

#### 執行配置範本
建立團隊共用的執行配置範本：
```xml
<!-- .idea/runConfigurations/Application.xml -->
<component name="ProjectRunConfigurationManager">
  <configuration default="false" name="Application" type="Application">
    <option name="MAIN_CLASS_NAME" value="com.company.Application" />
    <option name="VM_PARAMETERS" value="-Dspring.profiles.active=dev" />
    <option name="PROGRAM_PARAMETERS" value="" />
    <option name="WORKING_DIRECTORY" value="$PROJECT_DIR$" />
    <module name="project-name" />
  </configuration>
</component>
```

### 5.5 建置和部署

#### Maven 打包
1. 執行 `mvn clean package` 
2. 檢查 `target` 目錄中的 JAR 檔案
3. 針對可執行 JAR，使用：
```xml
<plugin>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-maven-plugin</artifactId>
    <executions>
        <execution>
            <goals>
                <goal>repackage</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

#### WAR 檔案部署
1. 修改 `pom.xml` 包裝類型：
```xml
<packaging>war</packaging>
```

2. 添加 Tomcat 依賴：
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-tomcat</artifactId>
    <scope>provided</scope>
</dependency>
```

#### Docker 化部署
```dockerfile
# Dockerfile
FROM openjdk:17-jre-slim

COPY target/myapp-1.0.0.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "/app.jar"]
```

#### 實務建議
- 使用 Maven profiles 管理不同環境的設定
- 設定自動化建置流程
- 建立標準化的部署腳本
- 定期清理 target 目錄避免空間浪費

---

## 6. Debug 與單元測試

### 6.1 Debug 基本操作

#### 設定中斷點
1. 在程式碼行號左側點擊設定中斷點
2. 右鍵中斷點可設定條件：
   - **Condition**: 條件中斷點
   - **Log message**: 記錄訊息而不停止
   - **Evaluate and log**: 評估表達式並記錄

#### 中斷點類型
- **Line breakpoint**: 一般行中斷點
- **Method breakpoint**: 方法進入/退出中斷點
- **Exception breakpoint**: 例外中斷點
- **Field watchpoint**: 欄位變更監控點

#### 啟動 Debug 模式
1. 右鍵點選類別 → 「Debug 'ClassName.main()'」
2. 使用快捷鍵 `Ctrl+Shift+F9`
3. 或點選工具列的 Debug 按鈕

### 6.2 Debug 視窗操作

#### Debug 工具視窗介紹
- **Frames**: 呼叫堆疊
- **Variables**: 變數檢視器
- **Watches**: 監控表達式
- **Console**: 程式輸出

#### 程式執行控制
- **Step Over** (F8): 逐行執行
- **Step Into** (F7): 進入方法內部
- **Step Out** (Shift+F8): 跳出目前方法
- **Resume Program** (F9): 繼續執行
- **Stop** (Ctrl+F2): 停止執行

#### 變數檢視和修改
1. 在 Variables 視窗中檢視變數值
2. 右鍵變數可以：
   - Set Value: 修改變數值
   - Mark Object: 標記物件
   - Copy Value: 複製變數值
   - View as Array: 以陣列形式檢視

### 6.3 進階 Debug 技巧

#### 條件中斷點
```java
// 範例：只在特定條件下中斷
for (int i = 0; i < 100; i++) {
    processItem(i);  // 中斷點條件：i > 50
}
```

#### 例外中斷點設定
1. 前往 `Run` → `View Breakpoints` (Ctrl+Shift+F8)
2. 點選「+」→「Java Exception Breakpoints」
3. 選擇例外類型（如 `NullPointerException`）
4. 設定中斷條件：
   - Caught exceptions: 被處理的例外
   - Uncaught exceptions: 未處理的例外

#### 遠端 Debug
1. 在遠端應用程式啟動時加入 JVM 參數：
```bash
-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005
```

2. 在 IntelliJ 中建立 Remote 配置：
   - Host: 遠端主機 IP
   - Port: 5005
   - Debugger mode: Attach to remote JVM

### 6.4 單元測試

#### JUnit 5 設定
```xml
<!-- pom.xml 中添加 JUnit 5 依賴 -->
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.9.2</version>
    <scope>test</scope>
</dependency>
```

#### 建立測試類別
1. 右鍵點選要測試的類別
2. 選擇「Go To」→「Test」(Ctrl+Shift+T)
3. 點選「Create New Test」
4. 選擇測試框架和要測試的方法

#### 測試類別範例
```java
@DisplayName("Calculator 測試類別")
class CalculatorTest {
    
    private Calculator calculator;
    
    @BeforeEach
    void setUp() {
        calculator = new Calculator();
    }
    
    @Test
    @DisplayName("加法測試")
    void testAdd() {
        // Given
        int a = 5;
        int b = 3;
        
        // When
        int result = calculator.add(a, b);
        
        // Then
        assertEquals(8, result, "5 + 3 應該等於 8");
    }
    
    @ParameterizedTest
    @DisplayName("參數化除法測試")
    @CsvSource({
        "10, 2, 5",
        "15, 3, 5",
        "20, 4, 5"
    })
    void testDivide(int dividend, int divisor, int expected) {
        int result = calculator.divide(dividend, divisor);
        assertEquals(expected, result);
    }
    
    @Test
    @DisplayName("除零例外測試")
    void testDivideByZero() {
        assertThrows(ArithmeticException.class, () -> {
            calculator.divide(10, 0);
        }, "除以零應該拋出 ArithmeticException");
    }
}
```

### 6.5 測試執行和管理

#### 執行測試
1. 執行單一測試方法：右鍵 → 「Run 'testMethodName()'」
2. 執行整個測試類別：右鍵類別 → 「Run 'ClassName'」
3. 執行所有測試：`Ctrl+Shift+F10` 或 Maven 視窗中的 test

#### 測試結果分析
- **綠色**: 測試通過
- **紅色**: 測試失敗
- **黃色**: 測試被忽略

#### 測試覆蓋率
1. 右鍵選擇「Run 'Tests' with Coverage」
2. 檢視 Coverage 視窗的結果：
   - Line coverage: 行覆蓋率
   - Branch coverage: 分支覆蓋率
   - Method coverage: 方法覆蓋率

### 6.6 Mock 測試

#### Mockito 設定
```xml
<dependency>
    <groupId>org.mockito</groupId>
    <artifactId>mockito-core</artifactId>
    <version>5.1.1</version>
    <scope>test</scope>
</dependency>
```

#### Mock 測試範例
```java
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    
    @Mock
    private UserRepository userRepository;
    
    @InjectMocks
    private UserService userService;
    
    @Test
    void testFindUserById() {
        // Given
        Long userId = 1L;
        User mockUser = new User(userId, "John Doe");
        when(userRepository.findById(userId)).thenReturn(Optional.of(mockUser));
        
        // When
        User result = userService.findById(userId);
        
        // Then
        assertThat(result.getName()).isEqualTo("John Doe");
        verify(userRepository).findById(userId);
    }
}
```

#### 實務測試建議
- 遵循 AAA 模式（Arrange, Act, Assert）
- 使用有意義的測試名稱和 @DisplayName
- 每個測試方法只測試一個功能點
- 使用參數化測試減少重複程式碼
- 維持測試的獨立性，避免測試間相互依賴

---

## 7. 常用快捷鍵與開發小技巧

### 7.1 基本快捷鍵

#### 檔案和專案操作
| 功能 | Windows/Linux | macOS | 說明 |
|------|---------------|-------|------|
| 新建檔案 | `Ctrl+Alt+Insert` | `Cmd+N` | 在目前目錄建立新檔案 |
| 開啟檔案 | `Ctrl+Shift+N` | `Cmd+Shift+O` | 快速開啟專案中的檔案 |
| 最近檔案 | `Ctrl+E` | `Cmd+E` | 顯示最近開啟的檔案 |
| 關閉檔案 | `Ctrl+F4` | `Cmd+W` | 關閉目前檔案 |
| 儲存所有檔案 | `Ctrl+S` | `Cmd+S` | 儲存所有修改 |
| 專案視窗 | `Alt+1` | `Cmd+1` | 顯示/隱藏專案視窗 |

#### 編輯操作
| 功能 | Windows/Linux | macOS | 說明 |
|------|---------------|-------|------|
| 複製行 | `Ctrl+D` | `Cmd+D` | 複製目前行到下一行 |
| 刪除行 | `Ctrl+Y` | `Cmd+Backspace` | 刪除目前行 |
| 移動行 | `Ctrl+Shift+↑/↓` | `Option+Shift+↑/↓` | 上下移動行 |
| 註解/取消註解 | `Ctrl+/` | `Cmd+/` | 單行註解切換 |
| 區塊註解 | `Ctrl+Shift+/` | `Cmd+Option+/` | 多行註解切換 |
| 格式化程式碼 | `Ctrl+Alt+L` | `Cmd+Option+L` | 自動格式化程式碼 |

### 7.2 導航快捷鍵

#### 程式碼導航
| 功能 | Windows/Linux | macOS | 說明 |
|------|---------------|-------|------|
| 前往定義 | `Ctrl+B` | `Cmd+B` | 跳轉到變數/方法定義 |
| 前往實作 | `Ctrl+Alt+B` | `Cmd+Option+B` | 跳轉到介面實作 |
| 前往使用處 | `Alt+F7` | `Option+F7` | 查找使用此變數/方法的地方 |
| 前往行號 | `Ctrl+G` | `Cmd+L` | 跳轉到指定行號 |
| 前往符號 | `Ctrl+Alt+Shift+N` | `Cmd+Option+O` | 搜尋類別、方法、變數 |
| 後退/前進 | `Ctrl+Alt+←/→` | `Cmd+Option+←/→` | 瀏覽歷史前進後退 |

#### 搜尋和取代
| 功能 | Windows/Linux | macOS | 說明 |
|------|---------------|-------|------|
| 檔案內搜尋 | `Ctrl+F` | `Cmd+F` | 在目前檔案中搜尋 |
| 檔案內取代 | `Ctrl+R` | `Cmd+R` | 在目前檔案中取代 |
| 全域搜尋 | `Ctrl+Shift+F` | `Cmd+Shift+F` | 在整個專案中搜尋 |
| 全域取代 | `Ctrl+Shift+R` | `Cmd+Shift+R` | 在整個專案中取代 |
| 搜尋所有地方 | `Double Shift` | `Double Shift` | 全域搜尋（檔案、類別、動作） |

### 7.3 程式碼產生快捷鍵

#### 自動完成和產生
| 功能 | Windows/Linux | macOS | 說明 |
|------|---------------|-------|------|
| 基本自動完成 | `Ctrl+Space` | `Ctrl+Space` | 顯示程式碼補全建議 |
| 智慧自動完成 | `Ctrl+Shift+Space` | `Ctrl+Shift+Space` | 智慧型程式碼補全 |
| 產生程式碼 | `Alt+Insert` | `Cmd+N` | 產生 getter/setter、建構子等 |
| 覆寫方法 | `Ctrl+O` | `Ctrl+O` | 覆寫父類別方法 |
| 實作方法 | `Ctrl+I` | `Ctrl+I` | 實作介面方法 |
| 圍繞程式碼 | `Ctrl+Alt+T` | `Cmd+Option+T` | 用 if/try/for 等包圍程式碼 |

#### Live Templates（程式碼範本）
| 範本 | 說明 | 展開結果 |
|------|------|----------|
| `sout` | System.out.println | `System.out.println();` |
| `psvm` | main 方法 | `public static void main(String[] args) {}` |
| `fori` | for 迴圈 | `for (int i = 0; i < ; i++) {}` |
| `iter` | foreach 迴圈 | `for (Type item : collection) {}` |
| `ifn` | if null 判斷 | `if (var == null) {}` |
| `inn` | if not null 判斷 | `if (var != null) {}` |

### 7.4 重構快捷鍵

#### 重構操作
| 功能 | Windows/Linux | macOS | 說明 |
|------|---------------|-------|------|
| 重新命名 | `Shift+F6` | `Shift+F6` | 重新命名變數、方法、類別 |
| 擷取變數 | `Ctrl+Alt+V` | `Cmd+Option+V` | 將表達式擷取為變數 |
| 擷取方法 | `Ctrl+Alt+M` | `Cmd+Option+M` | 將程式碼區塊擷取為方法 |
| 擷取常數 | `Ctrl+Alt+C` | `Cmd+Option+C` | 將值擷取為常數 |
| 內聯 | `Ctrl+Alt+N` | `Cmd+Option+N` | 內聯變數或方法 |
| 移動 | `F6` | `F6` | 移動類別、方法到其他位置 |

### 7.5 執行和除錯快捷鍵

#### 執行除錯
| 功能 | Windows/Linux | macOS | 說明 |
|------|---------------|-------|------|
| 執行 | `Shift+F10` | `Ctrl+R` | 執行目前配置 |
| 除錯 | `Shift+F9` | `Ctrl+D` | 除錯模式執行 |
| 執行目前檔案 | `Ctrl+Shift+F10` | `Ctrl+Shift+R` | 執行目前檔案 |
| 停止 | `Ctrl+F2` | `Cmd+F2` | 停止執行 |
| 設定中斷點 | `Ctrl+F8` | `Cmd+F8` | 切換中斷點 |
| 逐步執行 | `F8` | `F8` | Step Over |
| 進入方法 | `F7` | `F7` | Step Into |
| 跳出方法 | `Shift+F8` | `Shift+F8` | Step Out |
| 繼續執行 | `F9` | `F9` | Resume Program |

### 7.6 開發小技巧

#### 程式碼檢視技巧
1. **Quick Definition** (`Ctrl+Shift+I`): 快速檢視定義而不離開目前檔案
2. **Parameter Info** (`Ctrl+P`): 顯示方法參數資訊
3. **Quick Documentation** (`Ctrl+Q`): 快速檢視文件
4. **Type Info** (`Ctrl+Shift+P`): 顯示變數類型資訊

#### 多重選取和編輯
1. **Column Selection**: `Alt+Shift+Insert` 切換為欄位選取模式
2. **Multiple Cursors**: `Alt+J` 選取相同的下一個單字
3. **Select All Occurrences**: `Ctrl+Alt+Shift+J` 選取所有相同單字

#### 書籤管理
1. **設定書籤**: `F11` 切換匿名書籤
2. **設定數字書籤**: `Ctrl+F11` 設定編號書籤
3. **前往書籤**: `Shift+F11` 顯示書籤清單

#### 分割視窗
1. **水平分割**: 右鍵標籤 → "Split Right"
2. **垂直分割**: 右鍵標籤 → "Split Down"
3. **取消分割**: 右鍵 → "Unsplit"

#### 自訂快捷鍵
1. 前往 `File` → `Settings` → `Keymap`
2. 搜尋要修改的動作
3. 右鍵選擇 "Add Keyboard Shortcut"
4. 設定新的快捷鍵組合

#### 實用插件推薦
- **String Manipulation**: 字串處理工具
- **Rainbow Brackets**: 彩色括弧配對
- **GitToolBox**: Git 增強工具
- **SonarLint**: 程式碼品質檢查
- **JPA Buddy**: JPA 開發工具

---

## 8. 插件管理與擴展功能

### 8.1 插件安裝與管理

#### 安裝插件
1. 前往 `File` → `Settings` → `Plugins`
2. 在 Marketplace 標籤中搜尋插件
3. 點選「Install」安裝插件
4. 重新啟動 IDE 啟用插件

#### 插件管理最佳實務
- 只安裝必要的插件，避免影響效能
- 定期檢查並更新插件版本
- 移除不再使用的插件
- 備份插件清單以便團隊同步

### 8.2 開發效率插件

#### Essential Plugins for Java Development

**1. Lombok Plugin**
```java
// 使用 Lombok 減少樣板程式碼
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class User {
    private Long id;
    private String name;
    private String email;
}
```

**2. String Manipulation**
- 格式化 JSON、XML
- 編碼/解碼（Base64、URL）
- 大小寫轉換
- 排序和去重

**3. Rainbow Brackets**
- 彩色括弧配對
- 提高程式碼可讀性
- 支援多種程式語言

**4. GitToolBox**
- 顯示 Git blame 資訊
- 分支狀態指示器
- 提交歷史快速檢視

### 8.3 程式碼品質插件

#### SonarLint
```xml
<!-- 在 pom.xml 中配置 -->
<plugin>
    <groupId>org.sonarsource.scanner.maven</groupId>
    <artifactId>sonar-maven-plugin</artifactId>
    <version>3.9.1.2184</version>
</plugin>
```

**SonarLint 功能:**
- 即時程式碼分析
- 安全漏洞檢測
- 程式碼異味識別
- 修復建議

#### CheckStyle-IDEA
- 程式碼風格檢查
- 自訂檢查規則
- 與 Maven CheckStyle 插件整合

### 8.4 資料庫相關插件

#### JPA Buddy
- Entity 類別生成
- 資料庫視覺化工具
- JPA Query 輔助
- 遷移腳本生成

```java
// JPA Buddy 輔助生成的 Entity
@Entity
@Table(name = "users")
@Getter
@Setter
@ToString
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(nullable = false, unique = true)
    private String email;
    
    @OneToMany(mappedBy = "user", cascade = CascadeType.ALL)
    private Set<Order> orders = new HashSet<>();
}
```

### 8.5 測試輔助插件

#### JUnit Generator V2.0
- 自動生成測試類別
- 測試方法範本
- Mock 物件產生

#### TestMe
- 智慧型測試生成
- 支援多種測試框架
- 參數化測試支援

### 8.6 主題和外觀插件

#### 推薦主題
- **Material Theme UI**: 現代化材質設計
- **One Dark theme**: 類似 VS Code 的深色主題
- **Solarized Theme**: 經典的護眼主題

#### 自訂主題設定
1. 安裝主題插件
2. 前往 `File` → `Settings` → `Appearance & Behavior` → `Appearance`
3. 選擇主題並調整字體和顏色

### 8.7 團隊協作插件

#### Code With Me
- 即時協作編輯
- 螢幕分享
- 語音通話整合

#### GitLive
- 即時 Git 協作
- 分支狀態共享
- 衝突預警

### 8.8 插件開發基礎

#### 建立簡單插件
```xml
<!-- plugin.xml -->
<idea-plugin>
    <id>com.company.my-plugin</id>
    <name>My Plugin</name>
    <version>1.0</version>
    <vendor>Company</vendor>
    
    <depends>com.intellij.modules.platform</depends>
    
    <extensions defaultExtensionNs="com.intellij">
        <applicationService serviceImplementation="com.company.MyService"/>
    </extensions>
    
    <actions>
        <action id="MyAction" class="com.company.MyAction" text="My Action">
            <add-to-group group-id="ToolsMenu" anchor="first"/>
        </action>
    </actions>
</idea-plugin>
```

---

## 9. 資料庫整合與工具

### 9.1 Database Tool Window

#### 連接資料庫
1. 開啟 Database Tool Window：`View` → `Tool Windows` → `Database`
2. 點選「+」新增資料來源
3. 選擇資料庫類型（MySQL、PostgreSQL、H2 等）
4. 輸入連線資訊：
   ```
   Host: localhost
   Port: 3306
   Database: myapp
   User: root
   Password: ****
   ```

#### 支援的資料庫
- **關聯式資料庫**: MySQL, PostgreSQL, Oracle, SQL Server, H2
- **NoSQL**: MongoDB, Redis, Cassandra
- **雲端資料庫**: AWS RDS, Google Cloud SQL, Azure SQL

### 9.2 SQL 查詢和管理

#### SQL 控制台
1. 右鍵資料庫連線 → 「Open Console」
2. 撰寫 SQL 查詢：
```sql
-- 查詢使用者資料
SELECT u.id, u.name, u.email, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at >= '2023-01-01'
GROUP BY u.id, u.name, u.email
ORDER BY order_count DESC;
```

#### 查詢結果處理
- 匯出為 CSV、JSON、XML
- 複製為 INSERT 語句
- 比較查詢結果
- 查詢歷史記錄

### 9.3 資料庫結構管理

#### 表格設計工具
1. 右鍵資料庫 → 「New」→ 「Table」
2. 使用視覺化編輯器設計表格：
```sql
CREATE TABLE users (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    INDEX idx_email (email),
    INDEX idx_created_at (created_at)
);
```

#### 資料庫遷移
- 生成 DDL 腳本
- 比較資料庫結構
- 同步結構差異

### 9.4 與 JPA/Hibernate 整合

#### Entity 自動生成
1. 右鍵資料表 → 「Generate POJOs.kt」
2. 選擇生成選項：
   - JPA annotations
   - Lombok annotations
   - Builder pattern

```java
// 自動生成的 Entity
@Entity
@Table(name = "users")
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(nullable = false, unique = true)
    private String email;
    
    @Column(nullable = false)
    private String password;
    
    @Column(nullable = false, length = 100)
    private String name;
    
    @CreationTimestamp
    @Column(name = "created_at")
    private LocalDateTime createdAt;
    
    @UpdateTimestamp
    @Column(name = "updated_at")
    private LocalDateTime updatedAt;
}
```

### 9.5 資料庫效能分析

#### 查詢執行計畫
1. 撰寫 SQL 查詢
2. 點選「Explain Plan」按鈕
3. 分析執行計畫：
   - Index usage
   - Join 策略
   - 成本估算

#### 慢查詢優化
```sql
-- 優化前
SELECT * FROM users u, orders o 
WHERE u.id = o.user_id 
AND u.created_at > '2023-01-01';

-- 優化後
SELECT u.id, u.name, o.total_amount
FROM users u
INNER JOIN orders o ON u.id = o.user_id
WHERE u.created_at > '2023-01-01'
AND u.status = 'ACTIVE'
ORDER BY o.created_at DESC
LIMIT 100;
```

### 9.6 資料庫測試環境

#### H2 內存資料庫設定
```yaml
# application-test.yml
spring:
  datasource:
    url: jdbc:h2:mem:testdb;DB_CLOSE_DELAY=-1;DB_CLOSE_ON_EXIT=FALSE
    driver-class-name: org.h2.Driver
    username: sa
    password: password
  h2:
    console:
      enabled: true
      path: /h2-console
  jpa:
    hibernate:
      ddl-auto: create-drop
    show-sql: true
```

#### TestContainers 整合
```java
@Testcontainers
@SpringBootTest
class UserRepositoryTest {
    
    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:14")
            .withDatabaseName("testdb")
            .withUsername("test")
            .withPassword("test");
    
    @DynamicPropertySource
    static void configureProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", postgres::getJdbcUrl);
        registry.add("spring.datasource.username", postgres::getUsername);
        registry.add("spring.datasource.password", postgres::getPassword);
    }
    
    @Test
    void shouldSaveAndFindUser() {
        // 測試程式碼
    }
}
```

---

## 10. 效能調校與疑難排解

### 10.1 IDE 效能優化

#### JVM 記憶體調整
編輯 `idea64.exe.vmoptions` 檔案：
```
-Xms2048m
-Xmx8192m
-XX:ReservedCodeCacheSize=512m
-XX:+UseConcMarkSweepGC
-XX:SoftRefLRUPolicyMSPerMB=50
-ea
-XX:CICompilerCount=2
-Dsun.io.useCanonPrefixCache=false
-Djdk.http.auth.tunneling.disabledSchemes=""
-XX:+HeapDumpOnOutOfMemoryError
-XX:-OmitStackTraceInFastThrow
-Djb.vmOptionsFile=%APPDATA%\JetBrains\IntelliJIdea2023.3\idea64.exe.vmoptions
```

#### 索引優化
1. **排除不必要的檔案**：
   - 前往 `File` → `Settings` → `Build, Execution, Deployment` → `Compiler`
   - 在「Excludes」中添加：
     ```
     target/**
     node_modules/**
     *.log
     ```

2. **暫停索引**：
   - `File` → `Pause Indexing` 在大量檔案操作時

### 10.2 專案載入優化

#### Maven 匯入優化
```xml
<!-- .mvn/maven.config -->
-Dorg.slf4j.simpleLogger.log.org.apache.maven.cli.transfer.Slf4jMavenTransferListener=warn
-Dmaven.repo.local=D:\maven-repository
-Xmx2g
```

#### Gradle 優化
```properties
# gradle.properties
org.gradle.daemon=true
org.gradle.parallel=true
org.gradle.caching=true
org.gradle.jvmargs=-Xmx4g -XX:+HeapDumpOnOutOfMemoryError
```

### 10.3 常見效能問題

#### 問題：IDE 啟動緩慢
**解決方案：**
1. 減少啟動時載入的插件
2. 關閉不必要的工具視窗
3. 清理快取：`File` → `Invalidate Caches and Restart`

#### 問題：程式碼補全延遲
**解決方案：**
1. 調整補全設定：
   ```
   Settings → Editor → General → Code Completion
   - Show suggestions as you type: 關閉
   - Case sensitive completion: First letter
   ```

#### 問題：記憶體不足
**診斷步驟：**
1. 檢查記憶體使用：`Help` → `Memory Indicator`
2. 生成記憶體轉儲：`Help` → `Diagnostic Tools` → `Capture Memory Snapshot`
3. 分析記憶體使用模式

### 10.4 效能監控工具

#### 內建效能分析器
1. 啟用 CPU 使用監控：
   ```
   Help → Diagnostic Tools → CPU Usage Profiling
   ```

2. 檢查 UI 回應性：
   ```
   Help → Diagnostic Tools → UI Response Time
   ```

#### 自訂效能監控
```java
// 加入應用程式中的效能監控
@Component
public class PerformanceMonitor {
    
    private final MeterRegistry meterRegistry;
    
    @EventListener
    public void handleMethodExecution(MethodExecutionEvent event) {
        Timer.Sample sample = Timer.start(meterRegistry);
        try {
            // 方法執行
        } finally {
            sample.stop(Timer.builder("method.execution")
                         .tag("class", event.getClassName())
                         .tag("method", event.getMethodName())
                         .register(meterRegistry));
        }
    }
}
```

### 10.5 疑難排解指南

#### 常見錯誤及解決方案

**1. OutOfMemoryError**
```bash
# 錯誤訊息
java.lang.OutOfMemoryError: Java heap space

# 解決方案
- 增加 heap 大小：-Xmx8g
- 檢查記憶體洩漏
- 使用更高效的 GC：-XX:+UseG1GC
```

**2. 插件衝突**
```
# 排查步驟
1. 安全模式啟動：Help → Diagnostic Tools → Start IDE in Safe Mode
2. 逐步啟用插件確認問題插件
3. 檢查插件版本相容性
```

**3. 專案索引問題**
```
# 解決步驟
1. File → Invalidate Caches and Restart
2. 檢查專案 SDK 設定
3. 重新匯入 Maven/Gradle 專案
```

#### 日誌檢查
1. **IDE 日誌位置**：
   - Windows: `%APPDATA%\JetBrains\IntelliJIdea2023.3\log`
   - macOS: `~/Library/Logs/JetBrains/IntelliJIdea2023.3`
   - Linux: `~/.cache/JetBrains/IntelliJIdea2023.3/log`

2. **重要日誌檔案**：
   - `idea.log`: 主要的 IDE 日誌
   - `gc.log`: 垃圾回收日誌
   - `threadDumps-*`: 執行緒轉儲

### 10.6 系統整合問題

#### 防毒軟體干擾
**症狀**：檔案存取緩慢、編譯失敗
**解決方案**：
1. 將專案目錄加入防毒軟體排除清單
2. 排除 IDE 安裝目錄
3. 排除 JDK 目錄

#### 網路連線問題
```xml
<!-- Maven 代理設定 -->
<proxies>
    <proxy>
        <id>company-proxy</id>
        <active>true</active>
        <protocol>http</protocol>
        <host>proxy.company.com</host>
        <port>8080</port>
        <username>user</username>
        <password>password</password>
    </proxy>
</proxies>
```

---

## 11. 專案最佳實務

### 11.1 程式碼格式化和風格

#### 自動格式化設定
1. 啟用儲存時自動格式化：
   - 前往 `File` → `Settings` → `Tools` → `Actions on Save`
   - ✅ Reformat code
   - ✅ Optimize imports
   - ✅ Rearrange code

#### 團隊程式碼風格統一
```xml
<!-- .editorconfig 檔案 -->
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true

[*.java]
indent_style = space
indent_size = 4
max_line_length = 120

[*.{xml,yml,yaml}]
indent_style = space
indent_size = 2
```

#### CheckStyle 整合
```xml
<!-- pom.xml 中添加 CheckStyle 插件 -->
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-checkstyle-plugin</artifactId>
    <version>3.2.0</version>
    <configuration>
        <configLocation>checkstyle.xml</configLocation>
        <encoding>UTF-8</encoding>
        <consoleOutput>true</consoleOutput>
        <failsOnError>true</failsOnError>
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
</plugin>
```

### 11.2 註解和文件

#### JavaDoc 撰寫規範
```java
/**
 * 使用者服務類別，提供使用者相關的業務邏輯處理。
 * 
 * <p>此類別負責處理使用者的 CRUD 操作，包括：
 * <ul>
 *   <li>使用者註冊和登入驗證</li>
 *   <li>使用者資料查詢和更新</li>
 *   <li>使用者權限管理</li>
 * </ul>
 * 
 * @author John Doe
 * @version 1.0
 * @since 2023-01-01
 */
@Service
public class UserService {
    
    /**
     * 根據使用者 ID 查詢使用者資訊。
     * 
     * @param userId 使用者唯一識別碼，不可為 null
     * @return 使用者資訊物件，如果找不到則拋出例外
     * @throws UserNotFoundException 當指定 ID 的使用者不存在時
     * @throws IllegalArgumentException 當 userId 為 null 時
     * @see User
     * @since 1.0
     */
    public User findById(@NonNull Long userId) {
        if (userId == null) {
            throw new IllegalArgumentException("User ID cannot be null");
        }
        
        return userRepository.findById(userId)
            .orElseThrow(() -> new UserNotFoundException("User not found: " + userId));
    }
}
```

#### 方法註解最佳實務
```java
// ✅ 好的註解：說明為什麼，而不是做什麼
/**
 * 使用 BCrypt 演算法加密密碼，提供安全的密碼儲存。
 * 使用 salt round 為 12，在安全性和效能間取得平衡。
 */
public String encryptPassword(String plainPassword) {
    return BCrypt.hashpw(plainPassword, BCrypt.gensalt(12));
}

// ❌ 不好的註解：只是重複程式碼
/**
 * 加密密碼
 */
public String encryptPassword(String plainPassword) {
    return BCrypt.hashpw(plainPassword, BCrypt.gensalt(12));
}
```

### 11.3 套件管理和依賴

#### Maven 依賴管理最佳實務
```xml
<properties>
    <!-- 統一管理版本號 -->
    <spring.boot.version>3.1.0</spring.boot.version>
    <junit.version>5.9.2</junit.version>
    <mockito.version>5.1.1</mockito.version>
</properties>

<dependencyManagement>
    <dependencies>
        <!-- 使用 BOM 管理版本 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-dependencies</artifactId>
            <version>${spring.boot.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>

<dependencies>
    <!-- 生產依賴 -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    
    <!-- 測試依賴 -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
</dependencies>
```

#### 依賴安全性檢查
```xml
<!-- OWASP Dependency Check 插件 -->
<plugin>
    <groupId>org.owasp</groupId>
    <artifactId>dependency-check-maven</artifactId>
    <version>8.2.1</version>
    <executions>
        <execution>
            <goals>
                <goal>check</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

### 11.4 設定檔管理

#### 多環境設定管理
```yaml
# application.yml (基本設定)
spring:
  application:
    name: myapp
  profiles:
    active: @spring.profiles.active@

server:
  servlet:
    context-path: /api

logging:
  pattern:
    console: "%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n"

---
# application-dev.yml (開發環境)
spring:
  config:
    activate:
      on-profile: dev
  datasource:
    url: jdbc:h2:mem:devdb
    username: sa
    password: password
  jpa:
    show-sql: true

---
# application-prod.yml (生產環境)
spring:
  config:
    activate:
      on-profile: prod
  datasource:
    url: jdbc:postgresql://prod-db:5432/myapp
    username: ${DB_USERNAME}
    password: ${DB_PASSWORD}
  jpa:
    show-sql: false
```

#### 敏感資訊管理
```properties
# 使用環境變數
database.password=${DB_PASSWORD:defaultPassword}
jwt.secret=${JWT_SECRET:defaultSecret}
api.key=${EXTERNAL_API_KEY:}

# 使用 Spring Boot 的配置處理器
@ConfigurationProperties(prefix = "app.security")
@Configuration
public class SecurityProperties {
    private String jwtSecret;
    private Duration jwtExpiration = Duration.ofHours(24);
    
    // getters and setters
}
```

### 11.5 例外處理和日誌

#### 統一例外處理
```java
@RestControllerAdvice
public class GlobalExceptionHandler {
    
    private static final Logger logger = LoggerFactory.getLogger(GlobalExceptionHandler.class);
    
    @ExceptionHandler(UserNotFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public ErrorResponse handleUserNotFound(UserNotFoundException ex) {
        logger.warn("User not found: {}", ex.getMessage());
        return new ErrorResponse("USER_NOT_FOUND", ex.getMessage());
    }
    
    @ExceptionHandler(IllegalArgumentException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public ErrorResponse handleIllegalArgument(IllegalArgumentException ex) {
        logger.warn("Invalid argument: {}", ex.getMessage());
        return new ErrorResponse("INVALID_ARGUMENT", ex.getMessage());
    }
    
    @ExceptionHandler(Exception.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public ErrorResponse handleGeneral(Exception ex) {
        logger.error("Unexpected error", ex);
        return new ErrorResponse("INTERNAL_ERROR", "An unexpected error occurred");
    }
}
```

#### 結構化日誌
```java
@Service
public class UserService {
    
    private static final Logger logger = LoggerFactory.getLogger(UserService.class);
    
    public User createUser(CreateUserRequest request) {
        logger.info("Creating user with email: {}", request.getEmail());
        
        try {
            User user = userMapper.toEntity(request);
            User savedUser = userRepository.save(user);
            
            logger.info("User created successfully with ID: {}", savedUser.getId());
            return savedUser;
            
        } catch (DataIntegrityViolationException ex) {
            logger.error("Failed to create user due to data integrity violation: {}", 
                         ex.getMessage());
            throw new UserAlreadyExistsException("User with this email already exists");
        }
    }
}
```

### 11.6 測試策略

#### 測試金字塔實施
```java
// 單元測試 (70%)
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    @Mock private UserRepository userRepository;
    @InjectMocks private UserService userService;
    
    @Test
    void shouldCreateUserSuccessfully() {
        // 測試業務邏輯
    }
}

// 整合測試 (20%)
@SpringBootTest
@Testcontainers
class UserRepositoryTest {
    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:14");
    
    @Test
    void shouldPersistUserCorrectly() {
        // 測試資料層整合
    }
}

// 端到端測試 (10%)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class UserControllerE2ETest {
    @Autowired private TestRestTemplate restTemplate;
    
    @Test
    void shouldCreateUserViaAPI() {
        // 測試完整 API 流程
    }
}
```

#### 測試資料管理
```java
@TestConfiguration
public class TestDataConfig {
    
    @Bean
    @Primary
    public UserRepository testUserRepository() {
        return new InMemoryUserRepository();
    }
    
    @EventListener
    public void resetTestData(TestExecutionEvent event) {
        if (event.getTestContext().getTestMethod().isAnnotationPresent(ResetData.class)) {
            // 重置測試資料
        }
    }
}
```

### 11.7 效能最佳化

#### 啟動時間優化
```properties
# application.yml
spring:
  jpa:
    hibernate:
      ddl-auto: none  # 生產環境不自動建立表格
  main:
    lazy-initialization: true  # 延遲初始化
  datasource:
    hikari:
      maximum-pool-size: 10
      minimum-idle: 5
```

#### 記憶體使用監控
```java
@Component
public class MemoryMonitor {
    
    private static final Logger logger = LoggerFactory.getLogger(MemoryMonitor.class);
    
    @Scheduled(fixedRate = 60000)  // 每分鐘檢查一次
    public void logMemoryUsage() {
        Runtime runtime = Runtime.getRuntime();
        long totalMemory = runtime.totalMemory();
        long freeMemory = runtime.freeMemory();
        long usedMemory = totalMemory - freeMemory;
        
        logger.info("Memory usage - Used: {} MB, Free: {} MB, Total: {} MB",
                   usedMemory / (1024 * 1024),
                   freeMemory / (1024 * 1024),
                   totalMemory / (1024 * 1024));
    }
}
```

### 11.8 安全性考量

#### 安全配置檢查清單
- ✅ 使用 HTTPS 傳輸敏感資料
- ✅ 實施適當的驗證和授權機制
- ✅ 定期更新依賴套件
- ✅ 使用環境變數管理敏感設定
- ✅ 實施適當的輸入驗證
- ✅ 記錄安全相關事件

#### 輸入驗證
```java
@RestController
public class UserController {
    
    @PostMapping("/users")
    public ResponseEntity<User> createUser(@Valid @RequestBody CreateUserRequest request) {
        // Spring Validation 自動驗證
        User user = userService.createUser(request);
        return ResponseEntity.status(HttpStatus.CREATED).body(user);
    }
}

// DTO 驗證
public class CreateUserRequest {
    
    @NotBlank(message = "Email is required")
    @Email(message = "Invalid email format")
    private String email;
    
    @NotBlank(message = "Password is required")
    @Size(min = 8, message = "Password must be at least 8 characters")
    @Pattern(regexp = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d).*$", 
             message = "Password must contain uppercase, lowercase and digit")
    private String password;
    
    // getters and setters
}
```

---

## 12. 常見問題與解決方案

### 12.1 安裝和設定問題

#### 問題：無法啟動 IntelliJ IDEA
**可能原因：**
- JVM 記憶體設定不當
- 插件衝突
- 權限不足

**解決步驟：**
1. 檢查系統需求是否符合
2. 使用安全模式啟動：
   ```bash
   # Windows
   idea.exe /safe
   
   # macOS/Linux
   idea.sh safe
   ```
3. 重置 IDE 設定：刪除配置目錄並重新啟動

#### 問題：JDK 無法正確識別
**解決方案：**
1. 確認 JAVA_HOME 環境變數設定
2. 在 Project Structure 中手動添加 JDK
3. 檢查 JDK 版本相容性

```bash
# 檢查 JAVA_HOME 設定
echo $JAVA_HOME  # macOS/Linux
echo %JAVA_HOME% # Windows

# 檢查 Java 版本
java -version
javac -version
```

### 12.2 專案匯入問題

#### 問題：Maven 專案無法正確匯入
**症狀：**
- 依賴項目無法解析
- 原始碼目錄未正確識別
- 編譯錯誤

**解決步驟：**
1. 檢查 Maven 設定：
   ```bash
   mvn --version
   mvn dependency:tree
   ```

2. 重新匯入專案：
   - Maven Tool Window → Refresh
   - 或執行：`mvn clean install`

3. 檢查 `pom.xml` 語法：
   ```xml
   <!-- 確保基本結構正確 -->
   <project xmlns="http://maven.apache.org/POM/4.0.0">
       <modelVersion>4.0.0</modelVersion>
       <groupId>com.example</groupId>
       <artifactId>my-app</artifactId>
       <version>1.0-SNAPSHOT</version>
       <packaging>jar</packaging>
   </project>
   ```

#### 問題：Gradle 專案建置失敗
**解決方案：**
1. 檢查 Gradle Wrapper：
   ```bash
   ./gradlew --version
   ./gradlew clean build
   ```

2. 清理 Gradle 快取：
   ```bash
   ./gradlew clean
   rm -rf ~/.gradle/caches/
   ```

### 12.3 編譯和執行問題

#### 問題：編譯錯誤「找不到符號」
**常見原因：**
- 類別路徑不正確
- 依賴項目遺失
- 套件匯入錯誤

**診斷步驟：**
1. 檢查 Module 設定：
   ```
   File → Project Structure → Modules
   檢查 Sources、Dependencies 設定
   ```

2. 重新建置專案：
   ```
   Build → Rebuild Project
   ```

3. 檢查依賴項目：
   ```bash
   mvn dependency:resolve
   ```

#### 問題：「Could not find or load main class」
**解決方案：**
1. 確認主類別路徑正確
2. 檢查執行配置：
   ```
   Run → Edit Configurations
   Main class: com.example.MainClass
   Module: 選擇正確的模組
   ```

3. 清理並重新編譯：
   ```bash
   mvn clean compile
   ```

### 12.4 Git 整合問題

#### 問題：Git 操作失敗
**症狀：**
- Push/Pull 失敗
- 認證問題
- 分支操作錯誤

**解決步驟：**
1. 檢查 Git 設定：
   ```bash
   git config --global --list
   git remote -v
   ```

2. 更新認證資訊：
   ```bash
   # 清除快取的認證
   git config --global --unset credential.helper
   
   # 重新設定認證
   git config --global credential.helper store
   ```

3. 檢查 SSH 金鑰（如果使用 SSH）：
   ```bash
   ssh -T git@github.com
   ```

#### 問題：合併衝突無法解決
**解決策略：**
1. 使用 IntelliJ 的合併工具：
   ```
   VCS → Git → Resolve Conflicts
   ```

2. 手動解決衝突：
   ```bash
   # 查看衝突檔案
   git status
   
   # 編輯衝突檔案後
   git add <檔案名稱>
   git commit -m "Resolve merge conflict"
   ```

### 12.5 效能相關問題

#### 問題：IDE 回應緩慢
**優化措施：**
1. 增加記憶體配置：
   ```
   # idea64.exe.vmoptions
   -Xms2048m
   -Xmx8192m
   ```

2. 停用不必要的插件：
   ```
   File → Settings → Plugins
   停用未使用的插件
   ```

3. 清理快取：
   ```
   File → Invalidate Caches and Restart
   ```

#### 問題：大型專案載入緩慢
**解決方案：**
1. 排除大型目錄：
   ```
   File → Settings → Build, Execution, Deployment → Compiler
   Excludes: target/, node_modules/, .git/
   ```

2. 使用部分檢索：
   ```
   File → Power Save Mode
   暫時停用背景任務
   ```

### 12.6 插件相關問題

#### 問題：插件無法正常運作
**排查步驟：**
1. 檢查插件版本相容性
2. 停用其他插件測試
3. 查看 IDE 日誌：
   ```
   Help → Show Log in Explorer
   檢查 idea.log 中的錯誤訊息
   ```

#### 問題：自訂設定遺失
**預防措施：**
1. 定期匯出設定：
   ```
   File → Export Settings
   ```

2. 使用版本控制管理設定：
   ```bash
   # 備份 IDE 設定目錄
   cp -r ~/.IntelliJIdea2023.3/ ~/backup/
   ```

### 12.7 除錯問題

#### 問題：無法設定中斷點
**可能原因：**
- 程式碼未編譯
- 除錯符號遺失
- 執行配置錯誤

**解決方法：**
1. 重新編譯專案
2. 檢查除錯配置：
   ```
   Run → Edit Configurations
   確認 Debug 模式設定正確
   ```

3. 驗證 JVM 參數：
   ```
   -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005
   ```

#### 問題：變數值無法檢視
**解決方案：**
1. 確認變數在作用域內
2. 檢查編譯最佳化設定
3. 使用 Evaluate Expression 功能

### 12.8 快速診斷檢查清單

#### 遇到問題時的標準流程
1. **檢查基本環境**
   - [ ] JDK 版本和設定
   - [ ] IDE 版本和插件狀態
   - [ ] 專案設定正確性

2. **嘗試基本修復**
   - [ ] 重新啟動 IDE
   - [ ] 清理並重新建置專案
   - [ ] 清除快取和索引

3. **檢查日誌和錯誤訊息**
   - [ ] 查看 IDE 日誌
   - [ ] 檢查控制台輸出
   - [ ] 分析錯誤堆疊追蹤

4. **尋求幫助**
   - [ ] 查閱官方文件
   - [ ] 搜尋社群論壇
   - [ ] 聯繫團隊成員

---

## 13. 檢查清單

### 13.1 安裝和設定檢查清單

#### 初始安裝 ✓
- [ ] 下載並安裝 IntelliJ IDEA Community Edition
- [ ] 設定 JDK 路徑和版本（推薦 Java 17）
- [ ] 配置 Maven 路徑和設定檔
- [ ] 設定檔案編碼為 UTF-8
- [ ] 配置程式碼風格和格式化規則
- [ ] 啟用必要的程式碼檢查規則
- [ ] 安裝推薦插件（SonarLint、GitToolBox 等）
- [ ] 設定 UI 主題和字體大小

#### Git 整合設定 ✓
- [ ] 設定 Git 執行檔路徑
- [ ] 配置 Git 使用者資訊（name、email）
- [ ] 添加 GitHub/GitLab 帳戶和 Token
- [ ] 測試版本控制功能（clone、commit、push）
- [ ] 設定 .gitignore 檔案
- [ ] 配置 SSH 金鑰（如需要）

### 13.2 專案開發檢查清單

#### 專案建立和匯入 ✓
- [ ] 建立或匯入專案成功
- [ ] 驗證專案結構正確（src/main/java、src/test/java）
- [ ] 確認 Maven/Gradle 配置正確
- [ ] 設定適當的 JDK 版本
- [ ] 建立和測試執行配置
- [ ] 驗證依賴項目正確載入
- [ ] 設定模組和輸出目錄

#### 程式碼品質控制 ✓
- [ ] 啟用儲存時自動格式化
- [ ] 設定 CheckStyle 或 SonarLint 規則
- [ ] 配置程式碼檢查和警告
- [ ] 實施統一的命名慣例
- [ ] 撰寫適當的 JavaDoc 註解
- [ ] 設定匯入排序和清理規則
- [ ] 配置行長度和縮排規範

#### 測試和除錯設定 ✓
- [ ] 建立測試類別和方法範本
- [ ] 設定測試執行配置
- [ ] 配置測試覆蓋率檢查
- [ ] 建立和測試除錯配置
- [ ] 驗證中斷點和變數檢視功能
- [ ] 設定 Mock 框架（Mockito）
- [ ] 配置測試資料庫（H2、TestContainers）

### 13.3 資料庫整合檢查清單

#### 資料庫連線設定 ✓
- [ ] 設定開發環境資料庫連線
- [ ] 測試 SQL 查詢執行
- [ ] 配置 JPA/Hibernate 整合
- [ ] 設定資料庫遷移工具
- [ ] 建立測試資料庫環境
- [ ] 驗證 Entity 類別自動生成

#### 資料庫開發工具 ✓
- [ ] 安裝 JPA Buddy 插件
- [ ] 設定資料庫結構同步
- [ ] 配置查詢執行計畫分析
- [ ] 建立 DDL 腳本範本
- [ ] 設定資料庫備份策略

### 13.4 團隊協作檢查清單

#### 設定標準化 ✓
- [ ] 匯出並共享 IDE 設定檔
- [ ] 建立團隊程式碼風格範本
- [ ] 設定統一的執行配置
- [ ] 建立專案特定的 Live Templates
- [ ] 配置共同的檢查規則
- [ ] 建立插件安裝清單
- [ ] 設定團隊 Git 工作流程

#### 版本控制協作 ✓
- [ ] 設定適當的 .gitignore 規則
- [ ] 建立分支管理策略
- [ ] 配置 Pull Request 範本
- [ ] 設定程式碼審查流程
- [ ] 建立部署和發布流程
- [ ] 配置 CI/CD 整合
- [ ] 設定衝突解決策略

### 13.5 效能和安全檢查清單

#### 效能優化 ✓
- [ ] 配置適當的 JVM 記憶體參數
- [ ] 設定記憶體使用監控
- [ ] 優化編譯和索引設定
- [ ] 配置適當的快取策略
- [ ] 監控應用程式啟動時間
- [ ] 排除大型目錄的索引
- [ ] 定期清理快取和日誌

#### 安全性設定 ✓
- [ ] 使用環境變數管理敏感資訊
- [ ] 實施適當的輸入驗證
- [ ] 配置安全的傳輸協定（HTTPS）
- [ ] 定期更新依賴套件
- [ ] 實施適當的錯誤處理
- [ ] 設定安全掃描工具
- [ ] 配置認證和授權機制

### 13.6 日常開發檢查清單

#### 每日工作流程 ✓
- [ ] 同步最新程式碼（git pull）
- [ ] 檢查並解決合併衝突
- [ ] 執行完整測試套件
- [ ] 檢查程式碼品質報告
- [ ] 提交程式碼變更（附完整註解）
- [ ] 推送變更到遠端儲存庫
- [ ] 更新任務狀態

#### 週期性維護 ✓
- [ ] 清理 target/build 目錄
- [ ] 更新 IDE 和插件版本
- [ ] 檢查安全性警告和漏洞
- [ ] 備份 IDE 設定和專案配置
- [ ] 更新文件和程式碼註解
- [ ] 檢討和優化開發流程
- [ ] 更新依賴項目版本

### 13.7 問題排除檢查清單

#### 遇到問題時的標準流程 ✓
- [ ] 檢查錯誤訊息和日誌
- [ ] 驗證基本環境設定
- [ ] 嘗試重新啟動 IDE
- [ ] 清理快取和重新建置
- [ ] 檢查插件相容性
- [ ] 查閱相關文件
- [ ] 尋求團隊協助

#### 效能問題診斷 ✓
- [ ] 檢查記憶體使用狀況
- [ ] 分析 CPU 使用率
- [ ] 檢查磁碟空間
- [ ] 驗證網路連線
- [ ] 檢查防毒軟體干擾
- [ ] 分析啟動時間
- [ ] 優化 JVM 參數

---

## 總結

這份 IntelliJ IDEA Community Edition 使用教學手冊提供了完整且深入的 IDE 使用指南，涵蓋從基本安裝到進階開發技巧的各個面向。建議新進開發人員按照以下時程學習：

### 📅 學習時程建議

**第一週：基礎建立**
- 完成安裝和基本設定（第1-2章）
- 熟悉專案建立和匯入（第3章）
- 掌握基本的編輯和導航功能

**第二週：版本控制整合**
- 學習 Git 整合和協作（第4章）
- 熟悉專案編譯和執行（第5章）
- 開始使用基本的除錯功能

**第三週：進階開發技能**
- 掌握除錯技巧和測試方法（第6章）
- 學習常用快捷鍵和開發技巧（第7章）
- 安裝和配置必要插件（第8章）

**第四週：專業化設定**
- 設定資料庫整合工具（第9章）
- 進行效能調校和疑難排解（第10章）
- 實施專案最佳實務（第11章）

### 🎯 持續改進

1. **定期檢視**：每月回顧檢查清單，確保開發流程的一致性
2. **工具更新**：定期更新 IDE、插件和相關工具
3. **知識分享**：與團隊分享有用的技巧和最佳實務
4. **流程優化**：根據專案需求調整和優化開發流程

### 📚 延伸學習資源

- **官方文件**：[IntelliJ IDEA 官方文件](https://www.jetbrains.com/help/idea/)
- **社群論壇**：[JetBrains Community](https://intellij-support.jetbrains.com/)
- **影片教學**：[JetBrains YouTube 頻道](https://www.youtube.com/user/JetBrainsTV)
- **最佳實務**：定期關注 Java 社群的開發實務分享

### 🔄 文件維護

**版本控制**：此文件應納入版本控制，定期更新以反映：
- 最新的 IDE 版本功能
- 團隊開發實務的變化
- 新工具和插件的整合
- 常見問題的解決方案

**回饋機制**：建立回饋渠道，讓團隊成員可以：
- 回報文件中的錯誤或不足
- 建議新增內容或改進
- 分享實用的技巧和經驗

---

**文件資訊更新**
- **最後更新**：2025年8月29日
- **版本**：2.0
- **維護者**：開發團隊
- **下次檢討**：2025年11月29日

如有任何問題或建議，請聯繫開發團隊進行討論和改進。
