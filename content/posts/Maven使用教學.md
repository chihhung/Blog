+++
date = '2025-10-21T17:48:56+08:00'
draft = true
title = 'Maven使用教學'
tags = ['教學','工具' ,'Maven']
categories = ['技術']
author = 'Eric Cheng'
summary = 'Maven使用教學，作為新進開發人員的建構管理學習指引'
+++

# Maven 使用教學手冊

## 文件資訊

- **版本**: 1.0.0
- **建立日期**: 2025年8月29日
- **適用對象**: 新進開發同仁
- **目的**: 協助快速熟悉並在專案中正確使用 Maven

---

## 目錄

1. [Maven 基本介紹](#1-maven-基本介紹)
   - 1.1 [什麼是 Maven？](#11-什麼是-maven)
   - 1.2 [Maven 的用途與優勢](#12-maven-的用途與優勢)
   - 1.3 [在專案中的角色](#13-在專案中的角色)
2. [環境建置](#2-環境建置)
   - 2.1 [前置條件](#21-前置條件)
   - 2.2 [Maven 安裝](#22-maven-安裝)
   - 2.3 [驗證安裝成功](#23-驗證安裝成功)
   - 2.4 [IDE 整合](#24-ide-整合)
   - 2.5 [設定檔配置](#25-設定檔配置)
3. [Maven 專案結構](#3-maven-專案結構)
   - 3.1 [標準目錄結構](#31-標準目錄結構)
   - 3.2 [目錄結構詳細說明](#32-目錄結構詳細說明)
   - 3.3 [在專案中的實際應用](#33-在專案中的實際應用)
   - 3.4 [自訂目錄結構](#34-自訂目錄結構)
4. [pom.xml 說明](#4-pomxml-說明)
   - 4.1 [什麼是 POM？](#41-什麼是-pom)
   - 4.2 [基本結構](#42-基本結構)
   - 4.3 [常用標籤詳細說明](#43-常用標籤詳細說明)
   - 4.4 [如何新增與管理依賴](#44-如何新增與管理依賴)
   - 4.5 [建置配置](#45-建置配置)
   - 4.6 [我們專案的完整 pom.xml 分析](#46-我們專案的完整-pomxml-分析)
5. [常用指令](#5-常用指令)
   - 5.1 [Maven 生命週期](#51-maven-生命週期)
   - 5.2 [基本指令詳解](#52-基本指令詳解)
   - 5.3 [依賴管理指令](#53-依賴管理指令)
   - 5.4 [執行指令](#54-執行指令)
   - 5.5 [資訊查詢指令](#55-資訊查詢指令)
   - 5.6 [進階指令](#56-進階指令)
   - 5.7 [我們專案中的常用工作流程](#57-我們專案中的常用工作流程)
   - 5.8 [VS Code 中的 Maven 整合](#58-vs-code-中的-maven-整合)
   - 5.9 [Maven Wrapper 使用](#59-maven-wrapper-使用)
   - 5.10 [與 CI/CD 整合](#510-與-cicd-整合)
6. [專案最佳實務](#6-專案最佳實務)
   - 6.1 [依賴管理建議](#61-依賴管理建議)
   - 6.2 [Docker 整合](#62-docker-整合)
   - 6.3 [安全性管理](#63-安全性管理)
   - 6.4 [效能監控](#64-效能監控)
   - 6.5 [現代化開發實務](#65-現代化開發實務)
   - 6.6 [效能優化策略](#66-效能優化策略)
   - 6.7 [微服務架構支援](#67-微服務架構支援)
7. [常見問題排解 FAQ](#7-常見問題排解-faq)
   - 7.1 [編譯相關問題](#71-編譯相關問題)
   - 7.2 [依賴相關問題](#72-依賴相關問題)
   - 7.3 [測試相關問題](#73-測試相關問題)
   - 7.4 [IDE 整合問題](#74-ide-整合問題)
   - 7.5 [效能相關問題](#75-效能相關問題)
   - 7.6 [網路相關問題](#76-網路相關問題)
   - 7.7 [專案中注意事項](#77-專案中注意事項)
8. [附錄](#8-附錄)
   - 8.1 [官方文件與教學資源連結](#81-官方文件與教學資源連結)
   - 8.2 [常用插件參考](#82-常用插件參考)
   - 8.3 [Maven 生命週期詳細說明](#83-maven-生命週期詳細說明)
   - 8.4 [常用 Maven 屬性](#84-常用-maven-屬性)
   - 8.5 [範例設定檔](#85-範例設定檔)
   - 8.6 [團隊協作指南](#86-團隊協作指南)
9. [檢查清單 Checklist](#9-檢查清單-checklist)
   - 9.1 [環境設定檢查清單](#91-環境設定檢查清單)
   - 9.2 [日常開發檢查清單](#92-日常開發檢查清單)
   - 9.3 [問題排解檢查清單](#93-問題排解檢查清單)
   - 9.4 [發布準備檢查清單](#94-發布準備檢查清單)
   - 9.5 [新人上手檢查清單](#95-新人上手檢查清單)
   - 9.6 [定期維護檢查清單](#96-定期維護檢查清單)
10. [快速參考手冊](#10-快速參考手冊)
    - 10.1 [常用指令速查表](#101-常用指令速查表)
    - 10.2 [常用參數速查表](#102-常用參數速查表)
    - 10.3 [POM 檔案基本結構速查](#103-pom-檔案基本結構速查)
    - 10.4 [常見問題快速解決](#104-常見問題快速解決)
    - 10.5 [開發工作流程檢查清單](#105-開發工作流程檢查清單)
    - 10.6 [實用技巧](#106-實用技巧)
11. [進階主題](#11-進階主題)
    - 11.1 [自定義 Maven Archetype](#111-自定義-maven-archetype)
    - 11.2 [Maven 插件開發](#112-maven-插件開發)
    - 11.3 [Maven 與 Spring Boot 整合](#113-maven-與-spring-boot-整合)
    - 11.4 [Maven 與容器化部署](#114-maven-與容器化部署)
    - 11.5 [企業級 Maven 倉庫管理](#115-企業級-maven-倉庫管理)
12. [團隊協作與規範](#12-團隊協作與規範)
    - 12.1 [程式碼審查規範](#121-程式碼審查規範)
    - 12.2 [版本管理策略](#122-版本管理策略)
    - 12.3 [分支管理與 Maven](#123-分支管理與-maven)
    - 12.4 [自動化測試策略](#124-自動化測試策略)
13. [Maven 與現代 Java 開發](#13-maven-與現代-java-開發)
    - 13.1 [Java 模組系統（JPMS）與 Maven](#131-java-模組系統jpms與-maven)
    - 13.2 [Maven 與 JDK 版本管理](#132-maven-與-jdk-版本管理)
    - 13.3 [Maven 與記錄（Records）和文字區塊](#133-maven-與記錄records和文字區塊)
    - 13.4 [Maven 與虛擬執行緒](#134-maven-與虛擬執行緒)
14. [效能調校與監控](#14-效能調校與監控)
    - 14.1 [Maven 建置效能優化](#141-maven-建置效能優化)
    - 14.2 [依賴解析效能調校](#142-依賴解析效能調校)
    - 14.3 [建置時間監控與分析](#143-建置時間監控與分析)
    - 14.4 [記憶體使用最佳化](#144-記憶體使用最佳化)
15. [錯誤處理與除錯技巧](#15-錯誤處理與除錯技巧)
    - 15.1 [常見錯誤診斷流程](#151-常見錯誤診斷流程)
    - 15.2 [除錯工具與技巧](#152-除錯工具與技巧)
    - 15.3 [日誌分析與解讀](#153-日誌分析與解讀)
    - 15.4 [遠端除錯設定](#154-遠端除錯設定)
16. [實戰專案範例](#16-實戰專案範例)
    - 16.1 [簡單控制台應用程式](#161-簡單控制台應用程式)
    - 16.2 [Spring Boot Web 應用程式](#162-spring-boot-web-應用程式)
    - 16.3 [多模組企業級專案](#163-多模組企業級專案)
    - 16.4 [微服務架構專案](#164-微服務架構專案)

---

## 1. Maven 基本介紹

### 1.1 什麼是 Maven？

Apache Maven 是一個專案管理和建置自動化工具，主要用於 Java 專案（也支援其他語言如 C#、Ruby、Scala 等）。Maven 使用專案物件模型（Project Object Model, POM）來管理專案的建置、報告和文件。

### 1.2 Maven 的用途與優勢

#### 主要用途

- **依賴管理**：自動下載和管理專案所需的第三方 JAR 檔案
- **專案建置**：提供標準化的專案建置流程
- **測試執行**：整合單元測試和整合測試
- **報告生成**：產生專案報告、測試報告、程式碼覆蓋率等
- **部署管理**：自動化部署到不同環境

#### 主要優勢

- **標準化專案結構**：統一的目錄佈局，降低學習成本
- **簡化依賴管理**：自動解決依賴關係和版本衝突
- **豐富的插件生態**：支援各種建置、測試、部署需求
- **跨平台相容**：在不同作業系統間保持一致性
- **IDE 整合**：主流 IDE 都有良好的 Maven 支援

### 1.3 在專案中的角色

在我們的 Java 教學專案中，Maven 扮演以下角色：

1. **專案架構標準化**：確保所有開發人員使用相同的專案結構
2. **依賴版本統一**：避免「在我的電腦上可以執行」的問題
3. **建置流程自動化**：從編譯到測試到打包的完整流程
4. **團隊協作支援**：新人可以快速上手，減少環境配置問題

#### 實務案例

在我們的專案中，當新同事加入團隊時，只需要：
```bash
git clone <repository-url>
cd java_tutorial
mvn clean install
```
就能完成整個專案的建置和依賴下載。

#### 注意事項

- Maven 需要網路連接來下載依賴
- 首次建置可能需要較長時間下載依賴
- 建議使用公司內部的 Maven 倉庫以提高下載速度

---

## 2. 環境建置

### 2.1 前置條件

在安裝 Maven 之前，請確保已安裝：
- **JDK 8 或更高版本**（建議使用 JDK 17，與專案保持一致）
- **JAVA_HOME 環境變數**已正確設定

#### 驗證 JDK 安裝

```bash
java -version
javac -version
echo $JAVA_HOME  # Linux/Mac
echo %JAVA_HOME%  # Windows
```

### 2.2 Maven 安裝

#### 2.2.1 Windows 安裝方式

**方法一：使用 Chocolatey（推薦）**

```powershell
# 安裝 Chocolatey（如果尚未安裝）
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# 安裝 Maven
choco install maven
```

**方法二：手動安裝**

1. 下載 Maven：前往 [Maven 官網](https://maven.apache.org/download.cgi)
2. 下載 Binary zip archive（如：apache-maven-3.9.4-bin.zip）
3. 解壓縮到適當目錄（如：C:\Program Files\Apache\Maven）
4. 設定環境變數：
   - 新增 `MAVEN_HOME` = `C:\Program Files\Apache\Maven\apache-maven-3.9.4`
   - 將 `%MAVEN_HOME%\bin` 加入 `PATH`

#### 2.2.2 macOS 安裝方式

**使用 Homebrew（推薦）**

```bash
# 安裝 Homebrew（如果尚未安裝）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 安裝 Maven
brew install maven
```

#### 2.2.3 Linux 安裝方式

**Ubuntu/Debian：**

```bash
sudo apt update
sudo apt install maven
```

**CentOS/RHEL：**

```bash
sudo yum install maven
# 或使用 dnf（較新版本）
sudo dnf install maven
```

### 2.3 驗證安裝成功

安裝完成後，開啟新的終端機視窗並執行：

```bash
mvn -version
```

應該會看到類似以下的輸出：

```
Apache Maven 3.9.4 (d86a17ee24cd95b4b6dc57e87667d4e2de6ab7a)
Maven home: C:\Program Files\Apache\Maven\apache-maven-3.9.4
Java version: 17.0.7, vendor: Eclipse Adoptium
Java home: C:\Program Files\Eclipse Adoptium\jdk-17.0.7.10-hotspot
Default locale: zh_TW, platform encoding: UTF-8
OS name: "windows 10", version: "10.0", arch: "amd64", family: "windows"
```

### 2.4 IDE 整合

#### 2.4.1 VS Code 整合

1. **安裝必要擴充功能：**
   - Extension Pack for Java
   - Maven for Java

2. **VS Code 設定：**
   在 `settings.json` 中加入：
   
   ```json
   {
     "java.configuration.maven.userSettings": "C:\\Users\\<username>\\.m2\\settings.xml",
     "maven.executable.path": "C:\\Program Files\\Apache\\Maven\\apache-maven-3.9.4\\bin\\mvn.cmd"
   }
   ```

3. **驗證整合：**
   - 打開 Java 專案
   - 在 Explorer 中應該能看到 "JAVA PROJECTS" 區段
   - 右鍵點擊 `pom.xml` 應該能看到 Maven 相關選項

#### 2.4.2 IntelliJ IDEA 整合

IntelliJ IDEA 內建 Maven 支援：

1. **檢查 Maven 設定：**
   - File → Settings → Build, Execution, Deployment → Build Tools → Maven
   - 確認 Maven home path 正確
   - 確認 User settings file 路徑正確

2. **匯入 Maven 專案：**
   - File → Open → 選擇包含 `pom.xml` 的資料夾
   - IntelliJ 會自動識別為 Maven 專案

#### 2.4.3 Eclipse 整合

Eclipse 也內建 Maven 支援（m2e 插件）：

1. **匯入 Maven 專案：**
   - File → Import → Maven → Existing Maven Projects
   - 選擇包含 `pom.xml` 的資料夾

2. **檢查 Maven 設定：**
   - Window → Preferences → Maven
   - 確認設定正確

### 2.5 設定檔配置

#### 2.5.1 Maven 設定檔位置

Maven 有兩個主要設定檔：
- **全域設定**：`${MAVEN_HOME}/conf/settings.xml`
- **使用者設定**：`${user.home}/.m2/settings.xml`（優先級較高）

#### 2.5.2 基本設定檔範例

在 `~/.m2/settings.xml` 中：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0 
          http://maven.apache.org/xsd/settings-1.0.0.xsd">
    
    <!-- 本地倉庫位置 -->
    <localRepository>C:/Users/${user.name}/.m2/repository</localRepository>
    
    <!-- 伺服器設定（如需要認證） -->
    <servers>
        <!-- 如果公司有私有倉庫需要認證 -->
        <!--
        <server>
            <id>company-nexus</id>
            <username>your-username</username>
            <password>your-password</password>
        </server>
        -->
    </servers>
    
    <!-- 鏡像設定（加速下載） -->
    <mirrors>
        <!-- 使用阿里雲鏡像加速（中國地區） -->
        <mirror>
            <id>aliyun-maven</id>
            <name>Aliyun Maven Mirror</name>
            <url>https://maven.aliyun.com/repository/central</url>
            <mirrorOf>central</mirrorOf>
        </mirror>
    </mirrors>
    
    <!-- 預設設定檔 -->
    <profiles>
        <profile>
            <id>development</id>
            <activation>
                <activeByDefault>true</activeByDefault>
            </activation>
            <properties>
                <maven.compiler.source>17</maven.compiler.source>
                <maven.compiler.target>17</maven.compiler.target>
                <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
            </properties>
        </profile>
    </profiles>
</settings>
```

#### 實務案例

在我們的專案中，建議所有開發人員使用相同的 Maven 設定，以確保：
- 相同的 JDK 版本（Java 17）
- 相同的編碼格式（UTF-8）
- 統一的倉庫來源

#### 注意事項

- 設定檔修改後需要重新啟動 IDE
- 密碼建議使用加密方式儲存
- 公司內部倉庫設定請詢問系統管理員

---

## 3. Maven 專案結構

### 3.1 標準目錄結構

Maven 遵循「慣例優於配置」（Convention over Configuration）的原則，定義了標準的專案目錄結構：

```
java_tutorial/
├── pom.xml                    # 專案物件模型檔案
├── src/                       # 原始碼目錄
│   ├── main/                  # 主要程式碼
│   │   ├── java/              # Java 原始碼
│   │   │   └── com/
│   │   │       └── tutorial/
│   │   │           └── java/
│   │   └── resources/         # 資源檔案
│   │       └── log4j2.xml     # 日誌設定檔
│   └── test/                  # 測試程式碼
│       ├── java/              # 測試原始碼
│       │   └── com/
│       │       └── tutorial/
│       │           └── java/
│       └── resources/         # 測試資源檔案
├── target/                    # 建置輸出目錄（自動生成）
│   ├── classes/               # 編譯後的 class 檔案
│   ├── test-classes/          # 編譯後的測試 class 檔案
│   └── *.jar                  # 打包後的 JAR 檔案
└── docs/                      # 文件目錄（非標準，專案特有）
```

### 3.2 目錄結構詳細說明

#### 3.2.1 `src/main/java/`

- **用途**：存放專案的主要 Java 原始碼
- **套件結構**：遵循 Java 套件命名慣例
- **範例**：`com.tutorial.java.Student.java`

#### 3.2.2 `src/main/resources/`

- **用途**：存放應用程式的資源檔案
- **常見檔案**：
  - 設定檔（properties、xml、yaml）
  - 靜態資源（圖片、文字檔案）
  - 模板檔案

#### 3.2.3 `src/test/java/`

- **用途**：存放單元測試和整合測試程式碼
- **命名慣例**：測試類別名稱通常以 `Test` 結尾
- **範例**：`StudentTest.java`

#### 3.2.4 `src/test/resources/`

- **用途**：存放測試專用的資源檔案
- **常見用途**：測試資料、模擬設定檔

#### 3.2.5 `target/`

- **用途**：Maven 建置過程的輸出目錄
- **自動生成**：執行 Maven 指令時自動建立
- **內容**：
  - `classes/`：編譯後的主程式 class 檔案
  - `test-classes/`：編譯後的測試 class 檔案
  - JAR/WAR 檔案：打包後的執行檔

### 3.3 在專案中的實際應用

讓我們看看我們教學專案的實際結構：

```bash
# 查看專案結構
tree /f java_tutorial
# 或在 Linux/Mac 使用
find java_tutorial -type f -name "*.java" | head -10
```

#### 3.3.1 主要程式碼範例

在 `src/main/java/com/tutorial/java/` 目錄下：

```java
// Student.java - 學生類別
package com.tutorial.java;

/**
 * 學生類別範例
 * 
 * @author Tutorial Team
 * @version 1.0.0
 */
public class Student {
    private String name;
    private int age;
    private String studentId;
    
    // 建構子、getter、setter 方法...
}
```

#### 3.3.2 測試程式碼範例

在 `src/test/java/com/tutorial/java/` 目錄下：

```java
// StudentTest.java - 學生類別測試
package com.tutorial.java;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Student 類別的單元測試
 */
public class StudentTest {
    
    @Test
    public void testStudentCreation() {
        Student student = new Student("張三", 20, "S001");
        assertEquals("張三", student.getName());
        assertEquals(20, student.getAge());
    }
}
```

#### 3.3.3 資源檔案範例

在 `src/main/resources/` 目錄下的 `log4j2.xml`：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN">
    <Appenders>
        <Console name="Console" target="SYSTEM_OUT">
            <PatternLayout pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} - %msg%n"/>
        </Console>
        <File name="File" fileName="logs/application.log">
            <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss.SSS} [%t] %-5level %logger{36} - %msg%n"/>
        </File>
    </Appenders>
    <Loggers>
        <Root level="info">
            <AppenderRef ref="Console"/>
            <AppenderRef ref="File"/>
        </Root>
    </Loggers>
</Configuration>
```

### 3.4 自訂目錄結構

雖然建議遵循 Maven 標準結構，但有時需要自訂。在 `pom.xml` 中可以指定：

```xml
<build>
    <sourceDirectory>src/main/java</sourceDirectory>
    <testSourceDirectory>src/test/java</testSourceDirectory>
    <resources>
        <resource>
            <directory>src/main/resources</directory>
        </resource>
    </resources>
    <testResources>
        <testResource>
            <directory>src/test/resources</directory>
        </testResource>
    </testResources>
</build>
```

#### 實務案例

在我們的專案中，除了標準結構外，還增加了：
- `docs/` 目錄：存放專案文件和教學資料
- `.github/` 目錄：存放 GitHub 相關設定和模板
- `logs/` 目錄：存放應用程式執行時產生的日誌檔案

#### 注意事項

- 遵循標準結構可提高專案的可讀性和可維護性
- IDE 通常能自動識別標準 Maven 結構
- 團隊成員更容易快速理解專案架構
- 第三方工具和插件通常基於標準結構設計

---

## 4. pom.xml 說明

### 4.1 什麼是 POM？

POM（Project Object Model）是 Maven 的核心概念，`pom.xml` 檔案包含了專案的所有重要資訊：

- 專案基本資訊（名稱、版本、描述）
- 依賴管理（第三方函式庫）
- 建置設定（編譯、測試、打包）
- 插件配置（額外功能）

### 4.2 基本結構

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    
    <!-- POM 模型版本 -->
    <modelVersion>4.0.0</modelVersion>
    
    <!-- 專案座標 -->
    <groupId>com.tutorial.java</groupId>
    <artifactId>java-vscode-tutorial</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>
    
    <!-- 專案資訊 -->
    <name>Java VS Code Tutorial</name>
    <description>一個教學專案，幫助成員學習如何使用 VS Code 撰寫 Java 程式</description>
    
    <!-- 屬性設定 -->
    <properties>
        <!-- 更多設定... -->
    </properties>
    
    <!-- 依賴管理 -->
    <dependencies>
        <!-- 依賴清單... -->
    </dependencies>
    
    <!-- 建置設定 -->
    <build>
        <!-- 插件設定... -->
    </build>
</project>
```

### 4.3 常用標籤詳細說明

#### 4.3.1 專案座標（Project Coordinates）

```xml
<!-- 組織或公司的唯一識別 -->
<groupId>com.tutorial.java</groupId>

<!-- 專案的唯一識別 -->
<artifactId>java-vscode-tutorial</artifactId>

<!-- 專案版本 -->
<version>1.0.0</version>

<!-- 打包類型 -->
<packaging>jar</packaging>  <!-- jar, war, pom, maven-plugin 等 -->
```

**命名慣例：**
- `groupId`：通常使用反向網域名稱，如 `com.company.department`
- `artifactId`：專案名稱，使用小寫加連字號，如 `my-project`
- `version`：建議使用語意化版本，如 `1.0.0`、`2.1.3-SNAPSHOT`

#### 4.3.2 屬性設定（Properties）

```xml
<properties>
    <!-- Java 版本設定 -->
    <maven.compiler.source>17</maven.compiler.source>
    <maven.compiler.target>17</maven.compiler.target>
    
    <!-- 編碼設定 -->
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
    
    <!-- 依賴版本管理 -->
    <junit.version>5.9.2</junit.version>
    <log4j.version>2.20.0</log4j.version>
    <maven.compiler.plugin.version>3.11.0</maven.compiler.plugin.version>
</properties>
```

#### 4.3.3 依賴管理（Dependencies）

```xml
<dependencies>
    <!-- JUnit 5 測試框架 -->
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter</artifactId>
        <version>${junit.version}</version>
        <scope>test</scope>  <!-- 只在測試時使用 -->
    </dependency>
    
    <!-- Log4j 2 日誌框架 -->
    <dependency>
        <groupId>org.apache.logging.log4j</groupId>
        <artifactId>log4j-core</artifactId>
        <version>${log4j.version}</version>
    </dependency>
    
    <!-- 可選依賴 -->
    <dependency>
        <groupId>com.fasterxml.jackson.core</groupId>
        <artifactId>jackson-core</artifactId>
        <version>2.15.2</version>
        <optional>true</optional>
    </dependency>
</dependencies>
```

**依賴範圍（Scope）：**
- `compile`（預設）：編譯和執行時都需要
- `test`：只在測試時需要
- `provided`：編譯時需要，但執行時由容器提供
- `runtime`：執行時需要，編譯時不需要
- `system`：類似 provided，但需要明確指定 JAR 路徑

### 4.4 如何新增與管理依賴

#### 4.4.1 手動新增依賴

1. **前往 Maven Central Repository**：https://mvnrepository.com/
2. **搜尋需要的函式庫**，如 "jackson-core"
3. **複製 Maven 依賴資訊**：
   ```xml
   <dependency>
       <groupId>com.fasterxml.jackson.core</groupId>
       <artifactId>jackson-core</artifactId>
       <version>2.15.2</version>
   </dependency>
   ```
4. **貼到 pom.xml 的 `<dependencies>` 區段**

#### 4.4.2 使用 IDE 新增依賴

**VS Code：**
1. 打開 `pom.xml`
2. 在 `<dependencies>` 標籤內按 `Ctrl+Space`
3. 輸入依賴名稱，IDE 會提供自動完成

**IntelliJ IDEA：**
1. 右鍵點擊專案 → Add Framework Support → Maven
2. 或使用 Generate → Dependency

#### 4.4.3 版本管理最佳實務

```xml
<!-- 方法一：使用 properties 統一管理版本 -->
<properties>
    <spring.version>5.3.21</spring.version>
</properties>

<dependencies>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-core</artifactId>
        <version>${spring.version}</version>
    </dependency>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>${spring.version}</version>
    </dependency>
</dependencies>

<!-- 方法二：使用 dependencyManagement 管理版本 -->
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-framework-bom</artifactId>
            <version>5.3.21</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

### 4.5 建置配置（Build Configuration）

```xml
<build>
    <!-- 專案名稱（打包後的檔案名稱） -->
    <finalName>java-tutorial</finalName>
    
    <!-- 插件配置 -->
    <plugins>
        <!-- Maven Compiler Plugin -->
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>${maven.compiler.plugin.version}</version>
            <configuration>
                <source>17</source>
                <target>17</target>
                <encoding>UTF-8</encoding>
                <compilerArgs>
                    <arg>-parameters</arg>  <!-- 保留參數名稱 -->
                </compilerArgs>
            </configuration>
        </plugin>
        
        <!-- Maven Surefire Plugin（測試） -->
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>3.1.2</version>
            <configuration>
                <includes>
                    <include>**/*Test.java</include>
                    <include>**/*Tests.java</include>
                </includes>
            </configuration>
        </plugin>
        
        <!-- Maven JAR Plugin -->
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-jar-plugin</artifactId>
            <version>3.3.0</version>
            <configuration>
                <archive>
                    <manifest>
                        <mainClass>com.tutorial.java.Main</mainClass>
                        <addClasspath>true</addClasspath>
                    </manifest>
                </archive>
            </configuration>
        </plugin>
    </plugins>
</build>
```

### 4.6 我們專案的完整 pom.xml 分析

讓我們分析我們教學專案的 `pom.xml`：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <!-- 專案座標：清楚識別這是教學專案 -->
    <groupId>com.tutorial.java</groupId>
    <artifactId>java-vscode-tutorial</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>

    <!-- 專案描述：說明專案目的 -->
    <name>Java VS Code Tutorial</name>
    <description>一個教學專案，幫助成員學習如何使用 VS Code 撰寫 Java 程式</description>

    <!-- 統一設定：確保所有開發人員使用相同版本 -->
    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <junit.version>5.9.2</junit.version>
    </properties>

    <dependencies>
        <!-- 測試框架：使用最新的 JUnit 5 -->
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>${junit.version}</version>
            <scope>test</scope>
        </dependency>
        
        <!-- 日誌框架：企業級日誌管理 -->
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-core</artifactId>
            <version>2.20.0</version>
        </dependency>
    </dependencies>
</project>
```

#### 實務案例

這個 `pom.xml` 的設計考量：

1. **教學導向**：依賴精簡，容易理解
2. **現代化**：使用 Java 17 和 JUnit 5
3. **標準化**：遵循企業開發慣例
4. **可擴充**：容易新增更多依賴

#### 注意事項

- 版本號建議使用 properties 管理，便於統一升級
- 依賴的 scope 要正確設定，避免不必要的依賴
- 定期檢查依賴是否有安全性更新
- 避免使用 SNAPSHOT 版本在正式環境

---

## 5. 常用指令

### 5.1 Maven 生命週期

Maven 有三個內建的建置生命週期：

1. **default**：處理專案的部署
2. **clean**：清理專案建置產生的檔案
3. **site**：建立專案的網站文件

每個生命週期包含多個階段（phase），執行某個階段會自動執行之前的所有階段。

#### Default 生命週期的主要階段

```
validate → compile → test → package → verify → install → deploy
```

### 5.2 基本指令詳解

#### 5.2.1 清理指令

```bash
# 清理 target 目錄
mvn clean

# 清理並顯示詳細輸出
mvn clean -X

# 只清理不編譯
mvn clean -Dmaven.test.skip=true
```

**用途：**
- 刪除 `target/` 目錄及其內容
- 清除之前建置的 class 檔案和 JAR 檔案
- 解決某些建置快取問題

#### 5.2.2 編譯指令

```bash
# 編譯主要原始碼（到 target/classes/）
mvn compile

# 編譯測試程式碼（到 target/test-classes/）
mvn test-compile

# 清理後編譯
mvn clean compile
```

**VS Code 中的使用：**
- 打開命令面板（Ctrl+Shift+P）
- 輸入 "Java: Clean Workspace"
- 或使用我們專案中的任務：編譯專案

#### 5.2.3 測試指令

```bash
# 執行所有測試
mvn test

# 跳過測試
mvn compile -Dmaven.test.skip=true

# 只編譯不執行測試
mvn compile -DskipTests

# 執行特定測試類別
mvn test -Dtest=StudentTest

# 執行特定測試方法
mvn test -Dtest=StudentTest#testStudentCreation

# 並行執行測試
mvn test -T 4  # 使用 4 個執行緒
```

**測試報告：**
- 測試結果存放在 `target/surefire-reports/`
- 包含 TXT 和 XML 格式的報告

#### 5.2.4 打包指令

```bash
# 打包成 JAR 檔案
mvn package

# 清理後打包
mvn clean package

# 跳過測試打包
mvn package -DskipTests

# 打包並安裝到本地倉庫
mvn clean package install
```

**打包結果：**
- JAR 檔案位於 `target/` 目錄
- 檔案名稱格式：`{artifactId}-{version}.jar`
- 我們專案會產生：`java-vscode-tutorial-1.0.0.jar`

#### 5.2.5 安裝與部署指令

```bash
# 安裝到本地倉庫（~/.m2/repository/）
mvn install

# 完整建置並安裝
mvn clean install

# 部署到遠端倉庫（需要配置）
mvn deploy

# 只安裝不執行測試
mvn install -DskipTests
```

### 5.3 依賴管理指令

#### 5.3.1 查看依賴樹

```bash
# 顯示完整依賴樹
mvn dependency:tree

# 顯示特定依賴的路徑
mvn dependency:tree -Dincludes=org.junit.jupiter:junit-jupiter

# 顯示依賴衝突
mvn dependency:tree -Dverbose

# 輸出到檔案
mvn dependency:tree -DoutputFile=dependencies.txt
```

**範例輸出：**
```
[INFO] com.tutorial.java:java-vscode-tutorial:jar:1.0.0
[INFO] +- org.junit.jupiter:junit-jupiter:jar:5.9.2:test
[INFO] |  +- org.junit.jupiter:junit-jupiter-api:jar:5.9.2:test
[INFO] |  +- org.junit.jupiter:junit-jupiter-params:jar:5.9.2:test
[INFO] |  \- org.junit.jupiter:junit-jupiter-engine:jar:5.9.2:test
[INFO] +- org.apache.logging.log4j:log4j-core:jar:2.20.0:compile
[INFO] \- org.apache.logging.log4j:log4j-api:jar:2.20.0:compile
```

#### 5.3.2 分析依賴

```bash
# 分析已使用和未使用的依賴
mvn dependency:analyze

# 複製所有依賴到指定目錄
mvn dependency:copy-dependencies -DoutputDirectory=lib

# 下載原始碼
mvn dependency:sources

# 下載 JavaDoc
mvn dependency:resolve -Dclassifier=javadoc
```

#### 5.3.3 解決依賴問題

```bash
# 清理本地倉庫的損壞檔案
mvn dependency:purge-local-repository

# 強制更新依賴
mvn clean install -U

# 檢查依賴更新
mvn versions:display-dependency-updates
```

### 5.4 執行指令

#### 5.4.1 執行主類別

```bash
# 使用 exec plugin 執行主類別
mvn exec:java -Dexec.mainClass="com.tutorial.java.Main"

# 傳遞參數
mvn exec:java -Dexec.mainClass="com.tutorial.java.Main" -Dexec.args="arg1 arg2"

# 使用專案設定的主類別（在 pom.xml 中已配置）
mvn exec:java
```

**在我們的專案中：**
- 使用任務："執行主程式"
- 或直接執行：`mvn exec:java`

#### 5.4.2 執行編譯後的 JAR

```bash
# 先打包
mvn clean package

# 執行 JAR 檔案
java -jar target/java-vscode-tutorial-1.0.0.jar

# 或使用 Maven 執行
mvn exec:exec -Dexec.executable=java -Dexec.args="-jar target/java-vscode-tutorial-1.0.0.jar"
```

### 5.5 資訊查詢指令

#### 5.5.1 專案資訊

```bash
# 顯示專案有效的 POM
mvn help:effective-pom

# 顯示專案設定
mvn help:effective-settings

# 顯示系統屬性
mvn help:system

# 顯示 Maven 版本
mvn --version
```

#### 5.5.2 插件資訊

```bash
# 列出所有可用的 goals
mvn help:describe -Dplugin=compiler

# 描述特定插件
mvn help:describe -Dplugin=org.apache.maven.plugins:maven-compiler-plugin -Ddetail

# 列出專案中使用的插件
mvn help:describe -Dcmd=compile
```

### 5.6 進階指令

#### 5.6.1 多模組專案

```bash
# 在根目錄建置所有模組
mvn clean install

# 只建置特定模組
mvn clean install -pl module-name

# 建置特定模組及其依賴
mvn clean install -pl module-name -am

# 建置依賴特定模組的所有模組
mvn clean install -pl module-name -amd
```

#### 5.6.2 性能優化

```bash
# 平行建置（使用多個執行緒）
mvn clean install -T 4

# 離線模式（不檢查遠端更新）
mvn clean install -o

# 靜默模式（減少輸出）
mvn clean install -q

# 批次模式（非互動模式）
mvn clean install -B
```

#### 5.6.3 設定檔（Profile）

```bash
# 使用特定設定檔
mvn clean install -P production

# 使用多個設定檔
mvn clean install -P prod,security

# 列出可用的設定檔
mvn help:active-profiles
```

### 5.7 我們專案中的常用工作流程

#### 5.7.1 日常開發工作流程

```bash
# 1. 獲取最新程式碼
git pull

# 2. 清理並編譯
mvn clean compile

# 3. 執行測試
mvn test

# 4. 打包（如果需要）
mvn package
```

#### 5.7.2 新功能開發工作流程

```bash
# 1. 建立新分支
git checkout -b feature/new-feature

# 2. 開發過程中頻繁測試
mvn test -Dtest=NewFeatureTest

# 3. 完成後完整測試
mvn clean test

# 4. 確認可以正常打包
mvn clean package

# 5. 提交程式碼
git add .
git commit -m "Add new feature"
git push origin feature/new-feature
```

#### 5.7.3 發布準備工作流程

```bash
# 1. 完整建置和測試
mvn clean install

# 2. 檢查依賴安全性
mvn dependency:analyze

# 3. 產生報告
mvn site

# 4. 打包發布版本
mvn clean package -Prelease
```

### 5.8 VS Code 中的 Maven 整合

#### 5.8.1 使用 VS Code 任務

我們專案中預設的任務：

```json
{
    "label": "編譯專案",
    "type": "shell",
    "command": "mvn",
    "args": ["compile"],
    "group": "build"
}
```

**執行方式：**
- 按 `Ctrl+Shift+P` 開啟命令面板
- 輸入 "Tasks: Run Task"
- 選擇相應的任務

#### 5.8.2 Java Extension Pack 功能

- **自動建置**：儲存檔案時自動編譯
- **測試執行**：點擊測試方法上的 "Run Test" 按鈕
- **依賴管理**：在 Java Projects 視圖中管理依賴

#### 實務案例

在我們的專案中，常用的指令組合：

1. **開始工作時**：`mvn clean compile`
2. **開發測試時**：`mvn test -Dtest=StudentTest`
3. **提交前檢查**：`mvn clean test`
4. **準備部署時**：`mvn clean package`

#### 注意事項

- 在 Windows PowerShell 中，某些特殊字元需要轉義
- 大型專案建議使用 `-T` 參數進行平行建置
- 網路較慢時可以使用 `-o` 離線模式
- 定期使用 `mvn clean` 清理建置快取

### 5.9 Maven Wrapper 使用

#### 5.9.1 什麼是 Maven Wrapper？

Maven Wrapper（mvnw）是一個確保團隊成員使用相同 Maven 版本的工具，無需預先安裝 Maven。

#### 5.9.2 設定 Maven Wrapper

```bash
# 在專案根目錄執行
mvn wrapper:wrapper

# 指定特定 Maven 版本
mvn wrapper:wrapper -Dmaven=3.9.4
```

生成的檔案：
```
.mvn/
├── wrapper/
│   ├── maven-wrapper.jar
│   └── maven-wrapper.properties
├── mvnw         # Linux/Mac 執行檔
└── mvnw.cmd     # Windows 執行檔
```

#### 5.9.3 使用 Maven Wrapper

```bash
# Linux/Mac
./mvnw clean install

# Windows
mvnw.cmd clean install
```

#### 5.9.4 優點

- **版本一致性**：確保所有開發人員使用相同的 Maven 版本
- **無需預裝**：新人無需事先安裝 Maven
- **CI/CD 友善**：在持續整合環境中更容易使用

### 5.10 與 CI/CD 整合

#### 5.10.1 GitHub Actions 範例

在 `.github/workflows/ci.yml`：

```yaml
name: CI

on:
  push:
    branches: [ master, develop ]
  pull_request:
    branches: [ master ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up JDK 17
      uses: actions/setup-java@v4
      with:
        java-version: '17'
        distribution: 'temurin'
        
    - name: Cache Maven packages
      uses: actions/cache@v3
      with:
        path: ~/.m2
        key: ${{ runner.os }}-m2-${{ hashFiles('**/pom.xml') }}
        restore-keys: ${{ runner.os }}-m2
        
    - name: Run tests
      run: ./mvnw clean test
      
    - name: Generate test report
      uses: dorny/test-reporter@v1
      if: success() || failure()
      with:
        name: Maven Tests
        path: target/surefire-reports/*.xml
        reporter: java-junit
```

#### 5.10.2 GitLab CI 範例

在 `.gitlab-ci.yml`：

```yaml
image: maven:3.9.4-openjdk-17

variables:
  MAVEN_OPTS: "-Dmaven.repo.local=$CI_PROJECT_DIR/.m2/repository"

cache:
  paths:
    - .m2/repository/

stages:
  - test
  - build
  - deploy

test:
  stage: test
  script:
    - mvn clean test
  artifacts:
    reports:
      junit: target/surefire-reports/TEST-*.xml

build:
  stage: build
  script:
    - mvn clean package
  artifacts:
    paths:
      - target/*.jar
```

---

## 6. 專案最佳實務

### 6.1 依賴管理建議

#### 6.1.1 版本管理策略

**使用 BOM（Bill of Materials）管理相關依賴版本：**

```xml
<dependencyManagement>
    <dependencies>
        <!-- Spring Boot BOM -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-dependencies</artifactId>
            <version>2.7.14</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

**在 properties 中統一管理版本：**

```xml
<properties>
    <!-- Java 相關 -->
    <java.version>17</java.version>
    <maven.compiler.source>${java.version}</maven.compiler.source>
    <maven.compiler.target>${java.version}</maven.compiler.target>
    
    <!-- 測試框架 -->
    <junit.version>5.9.2</junit.version>
    <mockito.version>4.11.0</mockito.version>
    
    <!-- 日誌框架 -->
    <log4j.version>2.20.0</log4j.version>
    
    <!-- 工具類庫 -->
    <jackson.version>2.15.2</jackson.version>
    <apache.commons.version>3.12.0</apache.commons.version>
</properties>
```

### 6.2 Docker 整合

#### 6.2.1 Dockerfile 範例

```dockerfile
# 多階段建置
FROM maven:3.9.4-openjdk-17-slim AS build
WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN mvn clean package -DskipTests

FROM openjdk:17-jre-slim
WORKDIR /app
COPY --from=build /app/target/java-vscode-tutorial-1.0.0.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

#### 6.2.2 使用 Jib Plugin 建置 Docker 映像

```xml
<plugin>
    <groupId>com.google.cloud.tools</groupId>
    <artifactId>jib-maven-plugin</artifactId>
    <version>3.3.2</version>
    <configuration>
        <from>
            <image>openjdk:17-jre-slim</image>
        </from>
        <to>
            <image>java-tutorial</image>
            <tags>
                <tag>latest</tag>
                <tag>${project.version}</tag>
            </tags>
        </to>
    </configuration>
</plugin>
```

建置指令：
```bash
# 建置到本地 Docker
mvn jib:dockerBuild

# 建置並推送到 Registry
mvn jib:build
```

### 6.3 安全性管理

#### 6.3.1 OWASP Dependency Check

```xml
<plugin>
    <groupId>org.owasp</groupId>
    <artifactId>dependency-check-maven</artifactId>
    <version>8.3.1</version>
    <configuration>
        <format>ALL</format>
        <outputDirectory>target/dependency-check</outputDirectory>
        <suppressionFile>dependency-check-suppressions.xml</suppressionFile>
    </configuration>
    <executions>
        <execution>
            <goals>
                <goal>check</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

執行安全性檢查：
```bash
mvn dependency-check:check
```

#### 6.3.2 密碼加密

加密 settings.xml 中的密碼：

```bash
# 建立主密碼
mvn --encrypt-master-password <password>

# 加密伺服器密碼
mvn --encrypt-password <password>
```

### 6.4 效能監控

#### 6.4.1 Maven 建置時間分析

```xml
<plugin>
    <groupId>co.leantechniques</groupId>
    <artifactId>maven-buildtime-extension</artifactId>
    <version>3.0.1</version>
    <extensions>true</extensions>
</plugin>
```

#### 6.4.2 記憶體使用優化

設定 Maven 環境變數：
```bash
# 增加堆記憶體
export MAVEN_OPTS="-Xmx2g -Xms512m -XX:ReservedCodeCacheSize=512m"

# 啟用 G1GC
export MAVEN_OPTS="$MAVEN_OPTS -XX:+UseG1GC"
```

### 6.5 現代化開發實務

#### 6.5.1 使用 Maven Profiles 進行環境管理

```xml
<profiles>
    <!-- 開發環境 -->
    <profile>
        <id>dev</id>
        <activation>
            <activeByDefault>true</activeByDefault>
        </activation>
        <properties>
            <spring.profiles.active>dev</spring.profiles.active>
            <log.level>DEBUG</log.level>
            <database.url>jdbc:h2:mem:testdb</database.url>
        </properties>
    </profile>
    
    <!-- 測試環境 -->
    <profile>
        <id>test</id>
        <properties>
            <spring.profiles.active>test</spring.profiles.active>
            <log.level>INFO</log.level>
            <database.url>jdbc:mysql://test-db:3306/testdb</database.url>
        </properties>
        <build>
            <plugins>
                <plugin>
                    <groupId>org.jacoco</groupId>
                    <artifactId>jacoco-maven-plugin</artifactId>
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
        </build>
    </profile>
    
    <!-- 生產環境 -->
    <profile>
        <id>prod</id>
        <properties>
            <spring.profiles.active>prod</spring.profiles.active>
            <log.level>WARN</log.level>
            <maven.test.skip>true</maven.test.skip>
        </properties>
        <build>
            <plugins>
                <!-- 安全性掃描 -->
                <plugin>
                    <groupId>org.owasp</groupId>
                    <artifactId>dependency-check-maven</artifactId>
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
    </profile>
</profiles>
```

使用指令：
```bash
# 使用測試環境設定
mvn clean package -Ptest

# 使用生產環境設定
mvn clean package -Pprod
```

#### 6.5.2 整合 SonarQube 程式碼品質檢查

```xml
<plugin>
    <groupId>org.sonarsource.scanner.maven</groupId>
    <artifactId>sonar-maven-plugin</artifactId>
    <version>3.9.1.2184</version>
</plugin>
```

執行程式碼分析：
```bash
mvn sonar:sonar \
  -Dsonar.projectKey=java-tutorial \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=your-token
```

#### 6.5.3 使用 Testcontainers 進行整合測試

```xml
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>1.18.3</version>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>mysql</artifactId>
    <version>1.18.3</version>
    <scope>test</scope>
</dependency>
```

測試範例：
```java
@Testcontainers
class DatabaseIntegrationTest {
    
    @Container
    static MySQLContainer<?> mysql = new MySQLContainer<>("mysql:8.0")
            .withDatabaseName("testdb")
            .withUsername("test")
            .withPassword("test");
    
    @Test
    void testDatabaseConnection() {
        String jdbcUrl = mysql.getJdbcUrl();
        // 測試邏輯...
    }
}
```

### 6.6 效能優化策略

#### 6.6.1 Maven Daemon 使用

安裝 Maven Daemon：
```bash
# 使用 SDKMAN
sdk install mvnd

# 或下載並設定
curl -s "https://get.sdkman.io" | bash
sdk install mvnd
```

使用 mvnd 替代 mvn：
```bash
mvnd clean install  # 更快的建置速度
```

#### 6.6.2 平行建置優化

```xml
<!-- 在 pom.xml 中設定平行建置 -->
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <configuration>
        <parallel>methods</parallel>
        <threadCount>4</threadCount>
        <forkCount>2C</forkCount>
        <reuseForks>true</reuseForks>
    </configuration>
</plugin>
```

指令層級的平行建置：
```bash
# 使用所有 CPU 核心
mvn clean install -T 1C

# 使用 4 個執行緒
mvn clean install -T 4
```

### 6.7 微服務架構支援

#### 6.7.1 多模組專案結構

```
microservices-project/
├── pom.xml                 # 父 POM
├── common/                 # 共用模組
│   └── pom.xml
├── user-service/           # 使用者服務
│   └── pom.xml
├── order-service/          # 訂單服務
│   └── pom.xml
└── gateway/                # API 閘道
    └── pom.xml
```

父 POM 設定：
```xml
<packaging>pom</packaging>

<modules>
    <module>common</module>
    <module>user-service</module>
    <module>order-service</module>
    <module>gateway</module>
</modules>

<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-dependencies</artifactId>
            <version>2.7.14</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

#### 6.7.2 服務獨立部署

每個服務的 Dockerfile：
```dockerfile
FROM openjdk:17-jre-slim
COPY target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app.jar"]
```

Docker Compose 範例：
```yaml
version: '3.8'
services:
  user-service:
    build: ./user-service
    ports:
      - "8081:8080"
    environment:
      - SPRING_PROFILES_ACTIVE=docker
      
  order-service:
    build: ./order-service
    ports:
      - "8082:8080"
    environment:
      - SPRING_PROFILES_ACTIVE=docker
```

#### 依賴管理建議

**使用 BOM（Bill of Materials）管理相關依賴版本：**

```xml
<dependencyManagement>
    <dependencies>
        <!-- Spring Boot BOM -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-dependencies</artifactId>
            <version>2.7.14</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

**在 properties 中統一管理版本：**

```xml
<properties>
    <!-- Java 相關 -->
    <java.version>17</java.version>
    <maven.compiler.source>${java.version}</maven.compiler.source>
    <maven.compiler.target>${java.version}</maven.compiler.target>
    
    <!-- 測試框架 -->
    <junit.version>5.9.2</junit.version>
    <mockito.version>4.11.0</mockito.version>
    
    <!-- 日誌框架 -->
    <log4j.version>2.20.0</log4j.version>
    
    <!-- 工具類庫 -->
    <jackson.version>2.15.2</jackson.version>
    <apache.commons.version>3.12.0</apache.commons.version>
</properties>
```

#### 6.1.2 依賴範圍最佳實務

```xml
<dependencies>
    <!-- 主要功能：使用 compile scope -->
    <dependency>
        <groupId>org.apache.commons</groupId>
        <artifactId>commons-lang3</artifactId>
        <version>${apache.commons.version}</version>
    </dependency>
    
    <!-- 測試專用：使用 test scope -->
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter</artifactId>
        <version>${junit.version}</version>
        <scope>test</scope>
    </dependency>
    
    <!-- 運行時需要：使用 runtime scope -->
    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <version>8.0.33</version>
        <scope>runtime</scope>
    </dependency>
    
    <!-- 容器提供：使用 provided scope -->
    <dependency>
        <groupId>javax.servlet</groupId>
        <artifactId>javax.servlet-api</artifactId>
        <version>4.0.1</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
```

#### 6.1.3 排除不需要的依賴

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-core</artifactId>
    <version>5.3.21</version>
    <exclusions>
        <!-- 排除內建的 commons-logging，使用 slf4j -->
        <exclusion>
            <groupId>commons-logging</groupId>
            <artifactId>commons-logging</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

### 6.2 避免版本衝突的方法

#### 6.2.1 檢測依賴衝突

```bash
# 檢視完整依賴樹
mvn dependency:tree -Dverbose

# 分析依賴衝突
mvn dependency:tree -Dincludes=*:*:*:*:compile | grep "conflict"

# 檢查重複依賴
mvn dependency:analyze-duplicate
```

#### 6.2.2 解決版本衝突

**方法一：使用 dependencyManagement 強制指定版本**

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-core</artifactId>
            <version>2.15.2</version>
        </dependency>
    </dependencies>
</dependencyManagement>
```

**方法二：排除衝突的傳遞依賴**

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-web</artifactId>
    <version>5.3.21</version>
    <exclusions>
        <exclusion>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-core</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

#### 6.2.3 依賴收斂策略

```xml
<!-- 使用 Maven Enforcer Plugin 確保依賴收斂 -->
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-enforcer-plugin</artifactId>
    <version>3.3.0</version>
    <executions>
        <execution>
            <id>enforce-dependency-convergence</id>
            <goals>
                <goal>enforce</goal>
            </goals>
            <configuration>
                <rules>
                    <dependencyConvergence/>
                    <requireMavenVersion>
                        <version>3.6.0</version>
                    </requireMavenVersion>
                    <requireJavaVersion>
                        <version>17</version>
                    </requireJavaVersion>
                </rules>
            </configuration>
        </execution>
    </executions>
</plugin>
```

### 6.3 建置優化策略

#### 6.3.1 編譯器優化

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>3.11.0</version>
    <configuration>
        <source>17</source>
        <target>17</target>
        <encoding>UTF-8</encoding>
        <compilerArgs>
            <!-- 啟用所有建議的警告 -->
            <arg>-Xlint:all</arg>
            <!-- 將警告視為錯誤 -->
            <arg>-Werror</arg>
            <!-- 保留參數名稱 -->
            <arg>-parameters</arg>
        </compilerArgs>
    </configuration>
</plugin>
```

#### 6.3.2 測試優化

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.1.2</version>
    <configuration>
        <!-- 平行執行測試 -->
        <parallel>methods</parallel>
        <threadCount>4</threadCount>
        
        <!-- 測試失敗時繼續執行 -->
        <testFailureIgnore>false</testFailureIgnore>
        
        <!-- 包含/排除測試 -->
        <includes>
            <include>**/*Test.java</include>
            <include>**/*Tests.java</include>
        </includes>
        
        <!-- 產生測試報告 -->
        <reportFormat>xml</reportFormat>
        <reportFormat>plain</reportFormat>
    </configuration>
</plugin>
```

#### 6.3.3 JAR 打包優化

```xml
<!-- 建立可執行 JAR -->
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-shade-plugin</artifactId>
    <version>3.5.0</version>
    <executions>
        <execution>
            <phase>package</phase>
            <goals>
                <goal>shade</goal>
            </goals>
            <configuration>
                <transformers>
                    <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                        <mainClass>com.tutorial.java.Main</mainClass>
                    </transformer>
                </transformers>
                <!-- 縮小 JAR 檔案大小 -->
                <minimizeJar>true</minimizeJar>
            </configuration>
        </execution>
    </executions>
</plugin>
```

### 6.4 程式碼品質管理

#### 6.4.1 程式碼檢查（Checkstyle）

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-checkstyle-plugin</artifactId>
    <version>3.3.0</version>
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

#### 6.4.2 程式碼覆蓋率（JaCoCo）

```xml
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.10</version>
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
        <execution>
            <id>check</id>
            <goals>
                <goal>check</goal>
            </goals>
            <configuration>
                <rules>
                    <rule>
                        <element>PACKAGE</element>
                        <limits>
                            <limit>
                                <counter>LINE</counter>
                                <value>COVEREDRATIO</value>
                                <minimum>0.80</minimum>
                            </limit>
                        </limits>
                    </rule>
                </rules>
            </configuration>
        </execution>
    </executions>
</plugin>
```

### 6.5 使用公司內部 Nexus/Artifactory

#### 6.5.1 設定私有倉庫

在 `~/.m2/settings.xml` 中：

```xml
<settings>
    <!-- 伺服器認證 -->
    <servers>
        <server>
            <id>company-nexus</id>
            <username>${env.NEXUS_USERNAME}</username>
            <password>${env.NEXUS_PASSWORD}</password>
        </server>
    </servers>
    
    <!-- 鏡像設定 -->
    <mirrors>
        <mirror>
            <id>company-nexus</id>
            <name>Company Nexus Repository</name>
            <url>http://nexus.company.com/repository/maven-public/</url>
            <mirrorOf>central</mirrorOf>
        </mirror>
    </mirrors>
    
    <!-- 設定檔 -->
    <profiles>
        <profile>
            <id>company</id>
            <repositories>
                <repository>
                    <id>company-releases</id>
                    <url>http://nexus.company.com/repository/maven-releases/</url>
                    <releases><enabled>true</enabled></releases>
                    <snapshots><enabled>false</enabled></snapshots>
                </repository>
                <repository>
                    <id>company-snapshots</id>
                    <url>http://nexus.company.com/repository/maven-snapshots/</url>
                    <releases><enabled>false</enabled></releases>
                    <snapshots><enabled>true</enabled></snapshots>
                </repository>
            </repositories>
        </profile>
    </profiles>
    
    <activeProfiles>
        <activeProfile>company</activeProfile>
    </activeProfiles>
</settings>
```

#### 6.5.2 部署到私有倉庫

在 `pom.xml` 中：

```xml
<distributionManagement>
    <repository>
        <id>company-nexus</id>
        <name>Company Releases</name>
        <url>http://nexus.company.com/repository/maven-releases/</url>
    </repository>
    <snapshotRepository>
        <id>company-nexus</id>
        <name>Company Snapshots</name>
        <url>http://nexus.company.com/repository/maven-snapshots/</url>
    </snapshotRepository>
</distributionManagement>
```

### 6.6 環境特定設定

#### 6.6.1 使用 Profile 管理不同環境

```xml
<profiles>
    <!-- 開發環境 -->
    <profile>
        <id>development</id>
        <activation>
            <activeByDefault>true</activeByDefault>
        </activation>
        <properties>
            <spring.profiles.active>dev</spring.profiles.active>
            <log.level>DEBUG</log.level>
        </properties>
    </profile>
    
    <!-- 測試環境 -->
    <profile>
        <id>test</id>
        <properties>
            <spring.profiles.active>test</spring.profiles.active>
            <log.level>INFO</log.level>
        </properties>
    </profile>
    
    <!-- 生產環境 -->
    <profile>
        <id>production</id>
        <properties>
            <spring.profiles.active>prod</spring.profiles.active>
            <log.level>WARN</log.level>
        </properties>
        <build>
            <plugins>
                <!-- 生產環境額外的安全檢查 -->
                <plugin>
                    <groupId>org.owasp</groupId>
                    <artifactId>dependency-check-maven</artifactId>
                    <version>8.3.1</version>
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
    </profile>
</profiles>
```

#### 實務案例

在我們的教學專案中，建議的最佳實務：

1. **統一 Java 版本**：所有開發人員使用 JDK 17
2. **版本號管理**：在 properties 中統一管理第三方庫版本
3. **測試覆蓋率**：維持至少 80% 的測試覆蓋率
4. **程式碼檢查**：使用 Checkstyle 確保程式碼風格一致
5. **定期更新**：每月檢查並更新依賴版本

#### 注意事項

- 避免在 pom.xml 中硬編碼敏感資訊
- 定期檢查依賴的安全性漏洞
- 使用語意化版本號管理
- 保持 pom.xml 的簡潔和可讀性

---

## 7. 常見問題排解 FAQ

### 7.1 編譯相關問題

#### 7.1.1 Java 版本不匹配

**錯誤訊息：**
```
[ERROR] Source option 17 is no longer supported. Use 8 or later.
[ERROR] Target option 17 is no longer supported. Use 8 or later.
```

**原因：** 系統安裝的 JDK 版本與專案設定不匹配。

**解決方式：**

1. **檢查系統 JDK 版本：**
   ```bash
   java -version
   javac -version
   ```

2. **檢查 JAVA_HOME 設定：**
   ```bash
   echo $JAVA_HOME    # Linux/Mac
   echo %JAVA_HOME%   # Windows
   ```

3. **更新 JDK 或修改專案設定：**
   ```xml
   <properties>
       <maven.compiler.source>11</maven.compiler.source>
       <maven.compiler.target>11</maven.compiler.target>
   </properties>
   ```

#### 7.1.2 編碼問題

**錯誤訊息：**
```
[WARNING] File encoding has not been set, using platform encoding UTF-8
```

**解決方式：**
```xml
<properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
</properties>
```

#### 7.1.3 類別找不到錯誤

**錯誤訊息：**
```
[ERROR] package com.tutorial.java does not exist
```

**可能原因：**
- 套件結構與目錄結構不匹配
- 類別檔案位置錯誤

**解決方式：**
1. 檢查檔案位置：`src/main/java/com/tutorial/java/`
2. 檢查 package 宣告：`package com.tutorial.java;`
3. 重新整理專案：`mvn clean compile`

### 7.2 依賴相關問題

#### 7.2.1 依賴下載失敗

**錯誤訊息：**
```
[ERROR] Could not resolve dependencies for project com.tutorial:java-tutorial:jar:1.0.0: 
Could not find artifact org.junit.jupiter:junit-jupiter:jar:5.9.2
```

**解決方式：**

1. **檢查網路連接**
2. **清理本地倉庫：**
   ```bash
   mvn dependency:purge-local-repository
   ```
3. **強制更新：**
   ```bash
   mvn clean install -U
   ```
4. **檢查倉庫設定：**
   ```bash
   mvn help:effective-settings
   ```

#### 7.2.2 版本衝突

**錯誤訊息：**
```
[WARNING] The POM for org.springframework:spring-core:jar:5.2.0.RELEASE is invalid
```

**解決方式：**

1. **查看依賴樹：**
   ```bash
   mvn dependency:tree -Dverbose
   ```

2. **使用 dependencyManagement 強制指定版本：**
   ```xml
   <dependencyManagement>
       <dependencies>
           <dependency>
               <groupId>org.springframework</groupId>
               <artifactId>spring-core</artifactId>
               <version>5.3.21</version>
           </dependency>
       </dependencies>
   </dependencyManagement>
   ```

#### 7.2.3 傳遞依賴問題

**錯誤訊息：**
```
java.lang.ClassNotFoundException: org.slf4j.Logger
```

**解決方式：**

1. **檢查是否排除了必要的依賴**
2. **明確添加缺失的依賴：**
   ```xml
   <dependency>
       <groupId>org.slf4j</groupId>
       <artifactId>slf4j-api</artifactId>
       <version>2.0.7</version>
   </dependency>
   ```

### 7.3 測試相關問題

#### 7.3.1 測試執行失敗

**錯誤訊息：**
```
[ERROR] No tests were executed!
```

**可能原因：**
- 測試類別命名不符合慣例
- 測試方法沒有 @Test 註解

**解決方式：**

1. **檢查測試類別命名：**
   - 必須以 `Test` 結尾或以 `Test` 開始
   - 例如：`StudentTest.java` 或 `TestStudent.java`

2. **檢查測試方法：**
   ```java
   @Test
   public void testMethod() {
       // 測試邏輯
   }
   ```

3. **檢查 Surefire 插件配置：**
   ```xml
   <plugin>
       <groupId>org.apache.maven.plugins</groupId>
       <artifactId>maven-surefire-plugin</artifactId>
       <version>3.1.2</version>
       <configuration>
           <includes>
               <include>**/*Test.java</include>
           </includes>
       </configuration>
   </plugin>
   ```

#### 7.3.2 JUnit 5 相關問題

**錯誤訊息：**
```
java.lang.NoClassDefFoundError: org/junit/platform/engine/TestEngine
```

**解決方式：**
```xml
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.9.2</version>
    <scope>test</scope>
</dependency>
```

### 7.4 IDE 整合問題

#### 7.4.1 VS Code 無法識別 Maven 專案

**症狀：**
- Java Projects 視圖中沒有顯示專案
- 無法執行 Maven 指令

**解決方式：**

1. **重新載入專案：**
   - `Ctrl+Shift+P` → "Java: Rebuild Projects"

2. **檢查擴充功能：**
   - 確保安裝了 "Extension Pack for Java"

3. **檢查 settings.json：**
   ```json
   {
       "java.configuration.maven.userSettings": "C:\\Users\\username\\.m2\\settings.xml"
   }
   ```

#### 7.4.2 IntelliJ IDEA Maven 同步問題

**解決方式：**

1. **重新同步：**
   - View → Tool Windows → Maven → Refresh

2. **重新匯入：**
   - File → Invalidate Caches and Restart

3. **檢查 Maven 設定：**
   - File → Settings → Build Tools → Maven

### 7.5 效能相關問題

#### 7.5.1 建置速度慢

**解決方式：**

1. **使用平行建置：**
   ```bash
   mvn clean install -T 4
   ```

2. **跳過不必要的步驟：**
   ```bash
   mvn compile -DskipTests
   ```

3. **增加 Maven 記憶體：**
   ```bash
   export MAVEN_OPTS="-Xmx2g -XX:ReservedCodeCacheSize=512m"
   ```

#### 7.5.2 記憶體不足

**錯誤訊息：**
```
java.lang.OutOfMemoryError: Java heap space
```

**解決方式：**

1. **設定環境變數：**
   ```bash
   # Linux/Mac
   export MAVEN_OPTS="-Xmx2g -Xms512m"
   
   # Windows
   set MAVEN_OPTS=-Xmx2g -Xms512m
   ```

2. **在插件中設定：**
   ```xml
   <plugin>
       <groupId>org.apache.maven.plugins</groupId>
       <artifactId>maven-surefire-plugin</artifactId>
       <configuration>
           <argLine>-Xmx1g</argLine>
       </configuration>
   </plugin>
   ```

### 7.6 網路相關問題

#### 7.6.1 代理伺服器設定

**錯誤訊息：**
```
[ERROR] Could not transfer artifact from/to central
```

**解決方式：**

在 `~/.m2/settings.xml` 中：
```xml
<proxies>
    <proxy>
        <id>company-proxy</id>
        <active>true</active>
        <protocol>http</protocol>
        <host>proxy.company.com</host>
        <port>8080</port>
        <username>proxyuser</username>
        <password>proxypass</password>
        <nonProxyHosts>localhost|127.0.0.1|*.company.com</nonProxyHosts>
    </proxy>
</proxies>
```

#### 7.6.2 SSL 證書問題

**錯誤訊息：**
```
sun.security.validator.ValidatorException: PKIX path building failed
```

**解決方式：**

1. **暫時跳過 SSL 驗證（不建議用於生產）：**
   ```bash
   mvn clean install -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true
   ```

2. **匯入公司證書到 Java keystore**

### 7.7 專案中注意事項

#### 7.7.1 常見錯誤預防

1. **檢查清單：**
   - [ ] JDK 版本是否正確（Java 17）
   - [ ] JAVA_HOME 是否設定正確
   - [ ] Maven 版本是否相容（3.6.0 以上）
   - [ ] 網路連接是否正常
   - [ ] 本地倉庫是否損壞

2. **定期維護：**
   ```bash
   # 每週執行一次清理
   mvn clean
   
   # 每月檢查依賴更新
   mvn versions:display-dependency-updates
   
   # 每季度清理本地倉庫
   mvn dependency:purge-local-repository
   ```

#### 7.7.2 團隊協作建議

1. **統一環境設定：**
   - 所有成員使用相同的 JDK 版本
   - 統一的 Maven 設定檔
   - 相同的 IDE 設定

2. **版本控制：**
   - 將 `.mvn/wrapper/` 目錄加入版本控制
   - 排除 `target/` 目錄
   - 包含 `pom.xml` 和必要的設定檔

#### 實務案例

在我們的教學專案中，最常遇到的問題：

1. **新人環境設定問題**：提供標準的環境設定腳本
2. **依賴版本衝突**：使用 BOM 統一管理
3. **測試執行失敗**：確保遵循命名慣例

#### 注意事項

- 遇到問題時先檢查 Maven 和 JDK 版本
- 善用 `mvn -X` 查看詳細錯誤資訊
- 定期更新依賴但要經過充分測試
- 建立團隊內部的故障排除文件

---

## 8. 附錄

### 8.1 官方文件與教學資源連結

#### 8.1.1 官方文件

- **Apache Maven 官網**：<https://maven.apache.org/>
- **Maven 官方文件**：<https://maven.apache.org/guides/>
- **Maven Central Repository**：<https://mvnrepository.com/>
- **Maven Plugin 官方清單**：<https://maven.apache.org/plugins/>

#### 8.1.2 教學資源

- **Maven Getting Started Guide**：<https://maven.apache.org/guides/getting-started/>
- **Maven by Example**：<https://books.sonatype.com/mvnex-book/reference/>
- **Maven Reference**：<https://books.sonatype.com/mvnref-book/reference/>

#### 8.1.3 最佳實務指南

- **Maven 最佳實務**：<https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html>
- **Dependency Management**：<https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html>

### 8.2 常用插件參考

#### 8.2.1 核心插件

| 插件名稱 | 用途 | 官方文件 |
|---------|------|----------|
| maven-compiler-plugin | Java 編譯 | <https://maven.apache.org/plugins/maven-compiler-plugin/> |
| maven-surefire-plugin | 單元測試執行 | <https://maven.apache.org/surefire/maven-surefire-plugin/> |
| maven-failsafe-plugin | 整合測試執行 | <https://maven.apache.org/surefire/maven-failsafe-plugin/> |
| maven-jar-plugin | JAR 打包 | <https://maven.apache.org/plugins/maven-jar-plugin/> |
| maven-war-plugin | WAR 打包 | <https://maven.apache.org/plugins/maven-war-plugin/> |

#### 8.2.2 報告插件

| 插件名稱 | 用途 | 官方文件 |
|---------|------|----------|
| maven-site-plugin | 專案網站生成 | <https://maven.apache.org/plugins/maven-site-plugin/> |
| maven-checkstyle-plugin | 程式碼風格檢查 | <https://maven.apache.org/plugins/maven-checkstyle-plugin/> |
| jacoco-maven-plugin | 程式碼覆蓋率 | <https://www.jacoco.org/jacoco/trunk/doc/maven.html> |
| maven-pmd-plugin | 程式碼品質分析 | <https://maven.apache.org/plugins/maven-pmd-plugin/> |

#### 8.2.3 工具插件

| 插件名稱 | 用途 | 官方文件 |
|---------|------|----------|
| maven-dependency-plugin | 依賴管理 | <https://maven.apache.org/plugins/maven-dependency-plugin/> |
| maven-help-plugin | 資訊查詢 | <https://maven.apache.org/plugins/maven-help-plugin/> |
| maven-versions-plugin | 版本管理 | <https://www.mojohaus.org/versions-maven-plugin/> |
| maven-enforcer-plugin | 規則強制執行 | <https://maven.apache.org/enforcer/maven-enforcer-plugin/> |

### 8.3 Maven 生命週期詳細說明

#### 8.3.1 Default 生命週期

| 階段 | 描述 | 常用指令 |
|------|------|----------|
| validate | 驗證專案正確性 | `mvn validate` |
| initialize | 初始化建置狀態 | - |
| generate-sources | 生成原始碼 | - |
| process-sources | 處理原始碼 | - |
| generate-resources | 生成資源檔案 | - |
| process-resources | 處理資源檔案 | - |
| compile | 編譯原始碼 | `mvn compile` |
| process-classes | 處理編譯後的檔案 | - |
| generate-test-sources | 生成測試原始碼 | - |
| process-test-sources | 處理測試原始碼 | - |
| generate-test-resources | 生成測試資源 | - |
| process-test-resources | 處理測試資源 | - |
| test-compile | 編譯測試程式碼 | `mvn test-compile` |
| process-test-classes | 處理測試編譯檔案 | - |
| test | 執行測試 | `mvn test` |
| prepare-package | 準備打包 | - |
| package | 打包 | `mvn package` |
| pre-integration-test | 整合測試前準備 | - |
| integration-test | 執行整合測試 | `mvn integration-test` |
| post-integration-test | 整合測試後處理 | - |
| verify | 驗證 | `mvn verify` |
| install | 安裝到本地倉庫 | `mvn install` |
| deploy | 部署到遠端倉庫 | `mvn deploy` |

#### 8.3.2 Clean 生命週期

| 階段 | 描述 | 常用指令 |
|------|------|----------|
| pre-clean | 清理前準備 | - |
| clean | 清理 | `mvn clean` |
| post-clean | 清理後處理 | - |

#### 8.3.3 Site 生命週期

| 階段 | 描述 | 常用指令 |
|------|------|----------|
| pre-site | 網站生成前準備 | - |
| site | 生成網站 | `mvn site` |
| post-site | 網站生成後處理 | - |
| site-deploy | 部署網站 | `mvn site-deploy` |

### 8.4 常用 Maven 屬性

#### 8.4.1 內建屬性

| 屬性名稱 | 描述 | 範例值 |
|----------|------|--------|
| `${basedir}` | 專案根目錄 | `/path/to/project` |
| `${project.build.directory}` | 建置目錄 | `target` |
| `${project.build.outputDirectory}` | 編譯輸出目錄 | `target/classes` |
| `${project.name}` | 專案名稱 | `Java VS Code Tutorial` |
| `${project.version}` | 專案版本 | `1.0.0` |
| `${project.groupId}` | 專案群組 ID | `com.tutorial.java` |
| `${project.artifactId}` | 專案工件 ID | `java-vscode-tutorial` |

#### 8.4.2 系統屬性

| 屬性名稱 | 描述 | 範例值 |
|----------|------|--------|
| `${user.name}` | 使用者名稱 | `developer` |
| `${user.home}` | 使用者主目錄 | `/home/developer` |
| `${java.version}` | Java 版本 | `17.0.7` |
| `${os.name}` | 作業系統名稱 | `Windows 10` |
| `${file.separator}` | 檔案分隔符 | `/` 或 `\` |

### 8.5 範例設定檔

#### 8.5.1 完整的 pom.xml 範例

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <!-- 專案基本資訊 -->
    <groupId>com.tutorial.java</groupId>
    <artifactId>java-vscode-tutorial</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>

    <name>Java VS Code Tutorial</name>
    <description>一個完整的 Java 教學專案，展示 Maven 的使用</description>
    <url>https://github.com/company/java-tutorial</url>

    <!-- 屬性設定 -->
    <properties>
        <!-- Java 版本 -->
        <java.version>17</java.version>
        <maven.compiler.source>${java.version}</maven.compiler.source>
        <maven.compiler.target>${java.version}</maven.compiler.target>
        
        <!-- 編碼設定 -->
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
        
        <!-- 依賴版本 -->
        <junit.version>5.9.2</junit.version>
        <log4j.version>2.20.0</log4j.version>
        <maven.compiler.plugin.version>3.11.0</maven.compiler.plugin.version>
        <maven.surefire.plugin.version>3.1.2</maven.surefire.plugin.version>
    </properties>

    <!-- 依賴管理 -->
    <dependencies>
        <!-- 測試框架 -->
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>${junit.version}</version>
            <scope>test</scope>
        </dependency>
        
        <!-- 日誌框架 -->
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-core</artifactId>
            <version>${log4j.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-api</artifactId>
            <version>${log4j.version}</version>
        </dependency>
    </dependencies>

    <!-- 建置設定 -->
    <build>
        <finalName>${project.artifactId}</finalName>
        
        <plugins>
            <!-- Maven Compiler Plugin -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>${maven.compiler.plugin.version}</version>
                <configuration>
                    <source>${java.version}</source>
                    <target>${java.version}</target>
                    <encoding>UTF-8</encoding>
                </configuration>
            </plugin>
            
            <!-- Maven Surefire Plugin -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>${maven.surefire.plugin.version}</version>
                <configuration>
                    <includes>
                        <include>**/*Test.java</include>
                        <include>**/*Tests.java</include>
                    </includes>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

#### 8.5.2 完整的 settings.xml 範例

```xml
<?xml version="1.0" encoding="UTF-8"?>
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0 
          http://maven.apache.org/xsd/settings-1.0.0.xsd">
    
    <!-- 本地倉庫位置 -->
    <localRepository>${user.home}/.m2/repository</localRepository>
    
    <!-- 是否與使用者互動 -->
    <interactiveMode>true</interactiveMode>
    
    <!-- 是否使用插件註冊表 -->
    <usePluginRegistry>false</usePluginRegistry>
    
    <!-- 是否離線模式 -->
    <offline>false</offline>
    
    <!-- 伺服器認證設定 -->
    <servers>
        <server>
            <id>company-nexus</id>
            <username>${env.NEXUS_USERNAME}</username>
            <password>${env.NEXUS_PASSWORD}</password>
        </server>
    </servers>
    
    <!-- 鏡像設定 -->
    <mirrors>
        <mirror>
            <id>aliyun-maven</id>
            <name>Aliyun Maven Mirror</name>
            <url>https://maven.aliyun.com/repository/central</url>
            <mirrorOf>central</mirrorOf>
        </mirror>
    </mirrors>
    
    <!-- 代理設定 -->
    <proxies>
        <!-- 如果需要代理伺服器，取消註解並設定 -->
        <!--
        <proxy>
            <id>company-proxy</id>
            <active>true</active>
            <protocol>http</protocol>
            <host>proxy.company.com</host>
            <port>8080</port>
        </proxy>
        -->
    </proxies>
    
    <!-- 設定檔 -->
    <profiles>
        <profile>
            <id>development</id>
            <activation>
                <activeByDefault>true</activeByDefault>
            </activation>
            <properties>
                <maven.compiler.source>17</maven.compiler.source>
                <maven.compiler.target>17</maven.compiler.target>
                <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
            </properties>
        </profile>
    </profiles>
    
    <!-- 啟用的設定檔 -->
    <activeProfiles>
        <activeProfile>development</activeProfile>
    </activeProfiles>
</settings>
```

### 8.6 團隊協作指南

#### 8.6.1 版本控制建議

**.gitignore 範例：**
```gitignore
# Maven
target/
pom.xml.tag
pom.xml.releaseBackup
pom.xml.versionsBackup
pom.xml.next
release.properties
dependency-reduced-pom.xml
buildNumber.properties
.mvn/timing.properties
.mvn/wrapper/maven-wrapper.jar

# IDE
.idea/
*.iml
.vscode/
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json

# OS
.DS_Store
Thumbs.db
```

#### 8.6.2 團隊開發規範

1. **統一環境**：
   - JDK 版本：17
   - Maven 版本：3.8.0+
   - 編碼格式：UTF-8

2. **依賴管理**：
   - 使用 properties 管理版本
   - 避免使用 SNAPSHOT 版本在主分支
   - 定期檢查依賴更新

3. **建置規範**：
   - 提交前必須通過 `mvn clean test`
   - 保持測試覆蓋率在 80% 以上
   - 使用 Checkstyle 確保程式碼風格一致

---

## 9. 檢查清單 Checklist

### 9.1 環境設定檢查清單

#### 9.1.1 初始安裝檢查

- [ ] **JDK 安裝確認**
  - [ ] JDK 17 已正確安裝
  - [ ] `java -version` 顯示正確版本
  - [ ] `javac -version` 顯示正確版本
  - [ ] `JAVA_HOME` 環境變數已設定

- [ ] **Maven 安裝確認**
  - [ ] Maven 3.8.0+ 已正確安裝
  - [ ] `mvn -version` 顯示正確資訊
  - [ ] `MAVEN_HOME` 環境變數已設定（如果手動安裝）
  - [ ] Maven bin 目錄已加入 PATH

- [ ] **IDE 整合確認**
  - [ ] VS Code 已安裝 Extension Pack for Java
  - [ ] Maven for Java 擴充功能已啟用
  - [ ] Java Projects 視圖正常顯示
  - [ ] Maven 任務可以正常執行

#### 9.1.2 專案設定檢查

- [ ] **專案結構確認**
  - [ ] `pom.xml` 位於專案根目錄
  - [ ] `src/main/java` 目錄存在
  - [ ] `src/test/java` 目錄存在
  - [ ] 套件結構與目錄結構一致

- [ ] **pom.xml 設定確認**
  - [ ] groupId、artifactId、version 已正確設定
  - [ ] Java 版本設定為 17
  - [ ] 編碼設定為 UTF-8
  - [ ] 必要的依賴已加入

### 9.2 日常開發檢查清單

#### 9.2.1 開始工作前

- [ ] **程式碼同步**
  - [ ] `git pull` 獲取最新程式碼
  - [ ] 檢查是否有依賴更新
  - [ ] `mvn clean compile` 確認可以正常編譯

- [ ] **環境檢查**
  - [ ] IDE 正常啟動並識別專案
  - [ ] Maven 任務可以正常執行
  - [ ] 測試環境可以正常連接

#### 9.2.2 開發過程中

- [ ] **程式碼品質**
  - [ ] 遵循 Java 命名慣例
  - [ ] 添加適當的 JavaDoc 註解
  - [ ] 編寫對應的單元測試
  - [ ] 定期執行 `mvn test` 確認測試通過

- [ ] **依賴管理**
  - [ ] 新增依賴時檢查版本相容性
  - [ ] 使用 `mvn dependency:tree` 檢查依賴衝突
  - [ ] 確認依賴的 scope 設定正確

#### 9.2.3 提交程式碼前

- [ ] **建置檢查**
  - [ ] `mvn clean compile` 編譯成功
  - [ ] `mvn test` 所有測試通過
  - [ ] `mvn package` 打包成功
  - [ ] 檢查程式碼覆蓋率是否達標

- [ ] **程式碼檢查**
  - [ ] 沒有未使用的 import
  - [ ] 沒有未使用的變數或方法
  - [ ] 遵循團隊的程式碼規範
  - [ ] 移除調試用的 print 語句

### 9.3 問題排解檢查清單

#### 9.3.1 編譯問題排解

- [ ] **基本檢查**
  - [ ] JDK 版本是否正確
  - [ ] JAVA_HOME 是否設定正確
  - [ ] 專案編碼設定是否為 UTF-8
  - [ ] 套件宣告是否與目錄結構一致

- [ ] **依賴問題檢查**
  - [ ] 網路連接是否正常
  - [ ] `mvn dependency:tree` 檢查依賴樹
  - [ ] 本地倉庫是否損壞
  - [ ] 代理設定是否正確

#### 9.3.2 測試問題排解

- [ ] **測試環境檢查**
  - [ ] 測試類別命名是否正確（以 Test 結尾）
  - [ ] 測試方法是否有 @Test 註解
  - [ ] JUnit 5 依賴是否正確加入
  - [ ] Surefire 插件配置是否正確

- [ ] **測試執行檢查**
  - [ ] 測試資源檔案是否存在
  - [ ] 測試資料庫連接是否正常
  - [ ] 測試所需的外部服務是否可用

### 9.4 發布準備檢查清單

#### 9.4.1 發布前檢查

- [ ] **版本管理**
  - [ ] 版本號已適當更新
  - [ ] SNAPSHOT 版本已改為正式版本
  - [ ] 版本標籤已正確設定
  - [ ] 更新日誌已更新

- [ ] **品質檢查**
  - [ ] 所有測試通過
  - [ ] 程式碼覆蓋率達標
  - [ ] 安全性檢查通過
  - [ ] 效能測試通過

#### 9.4.2 部署檢查

- [ ] **打包檢查**
  - [ ] JAR 檔案可以正常建立
  - [ ] 依賴都包含在打包結果中
  - [ ] 主類別設定正確
  - [ ] 資源檔案包含完整

- [ ] **部署準備**
  - [ ] 部署腳本已準備
  - [ ] 環境設定檔案已準備
  - [ ] 回滾計劃已準備
  - [ ] 監控和日誌已設定

### 9.5 新人上手檢查清單

#### 9.5.1 第一次設定

- [ ] **環境準備**
  - [ ] 閱讀本教學手冊
  - [ ] 安裝 JDK 17
  - [ ] 安裝 Maven
  - [ ] 設定 IDE（VS Code 或 IntelliJ IDEA）

- [ ] **專案匯入**
  - [ ] 複製專案程式碼：`git clone <repository-url>`
  - [ ] 進入專案目錄：`cd java_tutorial`
  - [ ] 首次建置：`mvn clean install`
  - [ ] 驗證環境：`mvn test`

#### 9.5.2 學習確認

- [ ] **基本概念理解**
  - [ ] 理解 Maven 的用途和優勢
  - [ ] 熟悉標準目錄結構
  - [ ] 理解 pom.xml 的基本結構
  - [ ] 掌握常用 Maven 指令

- [ ] **實作練習**
  - [ ] 能夠新增一個簡單的 Java 類別
  - [ ] 能夠撰寫並執行單元測試
  - [ ] 能夠新增依賴到 pom.xml
  - [ ] 能夠使用 Maven 指令建置專案

### 9.6 定期維護檢查清單

#### 9.6.1 每月檢查

- [ ] **依賴更新**
  - [ ] `mvn versions:display-dependency-updates` 檢查更新
  - [ ] 評估並更新重要的依賴版本
  - [ ] 執行完整測試確認相容性
  - [ ] 更新依賴清單文件

- [ ] **環境清理**
  - [ ] `mvn clean` 清理建置檔案
  - [ ] 清理本地倉庫的損壞檔案
  - [ ] 檢查磁碟空間使用情況

#### 9.6.2 每季檢查

- [ ] **安全性檢查**
  - [ ] 檢查依賴是否有安全性漏洞
  - [ ] 更新有安全性問題的依賴
  - [ ] 執行安全性掃描工具
  - [ ] 更新安全性相關文件

- [ ] **效能檢查**
  - [ ] 分析建置時間是否合理
  - [ ] 檢查測試執行時間
  - [ ] 優化建置腳本和設定
  - [ ] 評估是否需要升級開發環境

---

## 結語

這份 Maven 使用教學手冊涵蓋了從環境建置到進階使用的完整指南。作為新進開發同仁，建議按照以下步驟學習：

1. **第一週**：完成環境建置（第1-2章）
2. **第二週**：熟悉專案結構和 pom.xml（第3-4章）
3. **第三週**：掌握常用指令和最佳實務（第5-6章）
4. **持續改進**：參考故障排除和檢查清單（第7-9章）

記住，Maven 是一個強大的工具，但也需要時間來熟練掌握。在學習過程中遇到問題時，請善用本手冊的故障排除章節，並且不要害怕向團隊中的資深成員尋求協助。

隨著 Maven 版本的更新和團隊需求的變化，這份文件也會持續更新。建議定期檢查最新版本，確保掌握最新的最佳實務。

**祝您學習愉快，開發順利！**

---

## 10. 快速參考手冊

### 10.1 常用指令速查表

| 指令 | 用途 | 範例 |
|------|------|------|
| `mvn clean` | 清理建置檔案 | `mvn clean` |
| `mvn compile` | 編譯主程式碼 | `mvn compile` |
| `mvn test` | 執行測試 | `mvn test -Dtest=StudentTest` |
| `mvn package` | 打包專案 | `mvn clean package` |
| `mvn install` | 安裝到本地倉庫 | `mvn clean install` |
| `mvn deploy` | 部署到遠端倉庫 | `mvn deploy` |
| `mvn dependency:tree` | 查看依賴樹 | `mvn dependency:tree` |
| `mvn dependency:analyze` | 分析依賴 | `mvn dependency:analyze` |
| `mvn versions:display-dependency-updates` | 檢查依賴更新 | `mvn versions:display-dependency-updates` |
| `mvn help:effective-pom` | 查看有效 POM | `mvn help:effective-pom` |

### 10.2 常用參數速查表

| 參數 | 用途 | 範例 |
|------|------|------|
| `-DskipTests` | 跳過測試執行 | `mvn package -DskipTests` |
| `-Dmaven.test.skip=true` | 跳過測試編譯和執行 | `mvn package -Dmaven.test.skip=true` |
| `-T` | 平行建置 | `mvn clean install -T 4` |
| `-U` | 強制更新依賴 | `mvn clean install -U` |
| `-o` | 離線模式 | `mvn clean install -o` |
| `-X` | 詳細輸出 | `mvn clean compile -X` |
| `-q` | 安靜模式 | `mvn clean compile -q` |
| `-P` | 激活設定檔 | `mvn clean package -Pprod` |

### 10.3 POM 檔案基本結構速查

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <!-- 基本資訊 -->
    <groupId>com.company.project</groupId>
    <artifactId>my-project</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>

    <!-- 屬性 -->
    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <!-- 依賴 -->
    <dependencies>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>5.9.2</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <!-- 建置設定 -->
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
            </plugin>
        </plugins>
    </build>
</project>
```

### 10.4 常見問題快速解決

| 問題 | 可能原因 | 解決方法 |
|------|----------|----------|
| 編譯失敗 | JDK 版本不匹配 | 檢查 `JAVA_HOME` 和 `maven.compiler.source` |
| 依賴下載失敗 | 網路問題 | 檢查網路連接，使用 `-U` 強制更新 |
| 測試執行失敗 | 測試命名錯誤 | 確保測試類別以 `Test` 結尾 |
| IDE 無法識別 | Maven 整合問題 | 重新載入專案，檢查擴充功能 |
| 記憶體不足 | Java 堆記憶體不足 | 設定 `MAVEN_OPTS="-Xmx2g"` |

### 10.5 開發工作流程檢查清單

#### 新功能開發

- [ ] `git checkout -b feature/new-feature`
- [ ] 編寫程式碼
- [ ] `mvn test -Dtest=NewFeatureTest`
- [ ] `mvn clean test`
- [ ] `git add . && git commit -m "Add new feature"`
- [ ] `git push origin feature/new-feature`

#### 每日工作

- [ ] `git pull`
- [ ] `mvn clean compile`
- [ ] 開發
- [ ] `mvn test`
- [ ] 提交程式碼

#### 發布準備

- [ ] `mvn clean install`
- [ ] `mvn dependency:analyze`
- [ ] `mvn package`
- [ ] 測試 JAR 檔案
- [ ] 標記版本：`git tag v1.0.0`

### 10.6 實用技巧

#### 10.6.1 一行指令完成常用任務

```bash
# 快速開始新專案
mvn archetype:generate -DgroupId=com.example -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

# 只運行特定測試類別的特定方法
mvn test -Dtest=UserServiceTest#testCreateUser

# 產生依賴報告
mvn dependency:tree > dependencies.txt

# 檢查程式碼覆蓋率
mvn clean test jacoco:report

# 建置並跳過所有檢查（僅限開發階段）
mvn clean package -DskipTests -Dcheckstyle.skip -Dpmd.skip
```

#### 10.6.2 環境變數設定

**Windows：**

```cmd
set JAVA_HOME=C:\Program Files\Java\jdk-17
set MAVEN_HOME=C:\Program Files\Apache\Maven\apache-maven-3.9.4
set MAVEN_OPTS=-Xmx2g -XX:ReservedCodeCacheSize=512m
```

**Linux/Mac：**

```bash
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
export MAVEN_HOME=/opt/maven
export MAVEN_OPTS="-Xmx2g -XX:ReservedCodeCacheSize=512m"
```

#### 10.6.3 VS Code 快捷鍵

| 功能 | 快捷鍵 | 說明 |
|------|--------|------|
| 執行測試 | `Ctrl+Shift+P` → "Java: Run Tests" | 執行當前測試 |
| 重建專案 | `Ctrl+Shift+P` → "Java: Rebuild Projects" | 重新建置專案 |
| 開啟終端 | `Ctrl+`` | 開啟整合終端執行 Maven 指令 |
| 執行任務 | `Ctrl+Shift+P` → "Tasks: Run Task" | 執行預定義的 Maven 任務 |

---

## 11. 進階主題

### 11.1 自定義 Maven Archetype

#### 11.1.1 什麼是 Maven Archetype？

Maven Archetype 是一個專案範本工具，可以快速建立具有預定義結構和內容的專案。

#### 11.1.2 建立自定義 Archetype

**步驟 1：建立範本專案**
```bash
# 建立基礎專案
mvn archetype:generate -DgroupId=com.tutorial.archetype \
  -DartifactId=tutorial-archetype \
  -DarchetypeArtifactId=maven-archetype-quickstart \
  -DinteractiveMode=false
```

**步驟 2：自定義專案結構**
```
tutorial-archetype/
├── pom.xml
├── src/
│   └── main/
│       ├── java/
│       │   └── App.java
│       └── resources/
│           ├── archetype-resources/
│           │   ├── pom.xml
│           │   └── src/
│           │       ├── main/java/__packageInPathFormat__/
│           │       │   └── ${artifactId}Application.java
│           │       └── test/java/__packageInPathFormat__/
│           │           └── ${artifactId}ApplicationTest.java
│           └── META-INF/
│               └── maven/
│                   └── archetype-metadata.xml
```

**步驟 3：設定 archetype-metadata.xml**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<archetype-descriptor xmlns="http://maven.apache.org/plugins/maven-archetype-plugin/archetype-descriptor/1.0.0"
                      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                      xsi:schemaLocation="http://maven.apache.org/plugins/maven-archetype-plugin/archetype-descriptor/1.0.0
                      http://maven.apache.org/xsd/archetype-descriptor-1.0.0.xsd"
                      name="tutorial-archetype">
    
    <requiredProperties>
        <requiredProperty key="groupId"/>
        <requiredProperty key="artifactId"/>
        <requiredProperty key="package"/>
        <requiredProperty key="version"/>
    </requiredProperties>
    
    <fileSets>
        <fileSet filtered="true" packaged="true">
            <directory>src/main/java</directory>
            <includes>
                <include>**/*.java</include>
            </includes>
        </fileSet>
        <fileSet filtered="true" packaged="true">
            <directory>src/test/java</directory>
            <includes>
                <include>**/*.java</include>
            </includes>
        </fileSet>
        <fileSet filtered="true">
            <directory>src/main/resources</directory>
            <includes>
                <include>**/*</include>
            </includes>
        </fileSet>
    </fileSets>
</archetype-descriptor>
```

### 11.2 Maven 插件開發

#### 11.2.1 建立自定義插件

**專案結構：**
```
custom-maven-plugin/
├── pom.xml
└── src/
    └── main/
        └── java/
            └── com/tutorial/plugin/
                └── CustomMojo.java
```

**POM 設定：**
```xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.tutorial</groupId>
    <artifactId>custom-maven-plugin</artifactId>
    <version>1.0.0</version>
    <packaging>maven-plugin</packaging>

    <dependencies>
        <dependency>
            <groupId>org.apache.maven</groupId>
            <artifactId>maven-plugin-api</artifactId>
            <version>3.9.4</version>
        </dependency>
        <dependency>
            <groupId>org.apache.maven.plugin-tools</groupId>
            <artifactId>maven-plugin-annotations</artifactId>
            <version>3.9.0</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-plugin-plugin</artifactId>
                <version>3.9.0</version>
                <executions>
                    <execution>
                        <id>default-descriptor</id>
                        <goals>
                            <goal>descriptor</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

**Mojo 實作：**
```java
package com.tutorial.plugin;

import org.apache.maven.plugin.AbstractMojo;
import org.apache.maven.plugin.MojoExecutionException;
import org.apache.maven.plugins.annotations.Mojo;
import org.apache.maven.plugins.annotations.Parameter;

/**
 * 自定義 Maven 插件範例
 */
@Mojo(name = "greet")
public class CustomMojo extends AbstractMojo {
    
    @Parameter(property = "greeting", defaultValue = "Hello, World!")
    private String greeting;
    
    @Parameter(property = "name", required = true)
    private String name;

    public void execute() throws MojoExecutionException {
        getLog().info(String.format("%s, %s!", greeting, name));
    }
}
```

**使用插件：**
```xml
<plugin>
    <groupId>com.tutorial</groupId>
    <artifactId>custom-maven-plugin</artifactId>
    <version>1.0.0</version>
    <configuration>
        <name>Developer</name>
        <greeting>Welcome</greeting>
    </configuration>
</plugin>
```

### 11.3 Maven 與 Spring Boot 整合

#### 11.3.1 Spring Boot Maven Plugin

```xml
<plugin>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-maven-plugin</artifactId>
    <version>2.7.14</version>
    <configuration>
        <mainClass>com.tutorial.Application</mainClass>
        <executable>true</executable>
        <excludes>
            <exclude>
                <groupId>org.projectlombok</groupId>
                <artifactId>lombok</artifactId>
            </exclude>
        </excludes>
    </configuration>
    <executions>
        <execution>
            <goals>
                <goal>repackage</goal>
                <goal>build-info</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

#### 11.3.2 多環境配置

```xml
<profiles>
    <profile>
        <id>dev</id>
        <activation>
            <activeByDefault>true</activeByDefault>
        </activation>
        <properties>
            <spring.profiles.active>dev</spring.profiles.active>
            <database.url>jdbc:h2:mem:devdb</database.url>
        </properties>
    </profile>
    
    <profile>
        <id>prod</id>
        <properties>
            <spring.profiles.active>prod</spring.profiles.active>
            <database.url>jdbc:mysql://prod-db:3306/proddb</database.url>
        </properties>
        <build>
            <resources>
                <resource>
                    <directory>src/main/resources</directory>
                    <filtering>true</filtering>
                    <excludes>
                        <exclude>application-dev.yml</exclude>
                        <exclude>application-test.yml</exclude>
                    </excludes>
                </resource>
            </resources>
        </build>
    </profile>
</profiles>
```

### 11.4 Maven 與容器化部署

#### 11.4.1 使用 Fabric8 Docker Maven Plugin

```xml
<plugin>
    <groupId>io.fabric8</groupId>
    <artifactId>docker-maven-plugin</artifactId>
    <version>0.43.4</version>
    <configuration>
        <images>
            <image>
                <name>tutorial/java-app:${project.version}</name>
                <build>
                    <from>openjdk:17-jre-alpine</from>
                    <assembly>
                        <descriptorRef>artifact</descriptorRef>
                    </assembly>
                    <cmd>
                        <shell>java -jar maven/${project.build.finalName}.jar</shell>
                    </cmd>
                </build>
                <run>
                    <ports>
                        <port>8080:8080</port>
                    </ports>
                </run>
            </image>
        </images>
    </configuration>
    <executions>
        <execution>
            <id>build-docker-image</id>
            <phase>package</phase>
            <goals>
                <goal>build</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

#### 11.4.2 Kubernetes 部署配置

**k8s-deployment.yaml：**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: java-tutorial-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: java-tutorial
  template:
    metadata:
      labels:
        app: java-tutorial
    spec:
      containers:
      - name: app
        image: tutorial/java-app:${project.version}
        ports:
        - containerPort: 8080
        env:
        - name: SPRING_PROFILES_ACTIVE
          value: "kubernetes"
```

**Maven 集成：**
```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-resources-plugin</artifactId>
    <executions>
        <execution>
            <id>filter-k8s-resources</id>
            <phase>process-resources</phase>
            <goals>
                <goal>copy-resources</goal>
            </goals>
            <configuration>
                <outputDirectory>${project.build.directory}/k8s</outputDirectory>
                <resources>
                    <resource>
                        <directory>src/main/k8s</directory>
                        <filtering>true</filtering>
                    </resource>
                </resources>
            </configuration>
        </execution>
    </executions>
</plugin>
```

### 11.5 企業級 Maven 倉庫管理

#### 11.5.1 設定 Nexus Repository

**settings.xml 配置：**
```xml
<settings>
    <servers>
        <server>
            <id>nexus-releases</id>
            <username>${env.NEXUS_USERNAME}</username>
            <password>${env.NEXUS_PASSWORD}</password>
        </server>
        <server>
            <id>nexus-snapshots</id>
            <username>${env.NEXUS_USERNAME}</username>
            <password>${env.NEXUS_PASSWORD}</password>
        </server>
    </servers>
    
    <mirrors>
        <mirror>
            <id>nexus-public</id>
            <mirrorOf>*</mirrorOf>
            <url>http://nexus.company.com/repository/maven-public/</url>
        </mirror>
    </mirrors>
    
    <profiles>
        <profile>
            <id>nexus</id>
            <repositories>
                <repository>
                    <id>nexus-public</id>
                    <url>http://nexus.company.com/repository/maven-public/</url>
                    <releases><enabled>true</enabled></releases>
                    <snapshots><enabled>true</enabled></snapshots>
                </repository>
            </repositories>
            <pluginRepositories>
                <pluginRepository>
                    <id>nexus-public</id>
                    <url>http://nexus.company.com/repository/maven-public/</url>
                    <releases><enabled>true</enabled></releases>
                    <snapshots><enabled>true</enabled></snapshots>
                </pluginRepository>
            </pluginRepositories>
        </profile>
    </profiles>
    
    <activeProfiles>
        <activeProfile>nexus</activeProfile>
    </activeProfiles>
</settings>
```

#### 11.5.2 企業級部署策略

```xml
<!-- 父 POM 中的分發管理 -->
<distributionManagement>
    <repository>
        <id>nexus-releases</id>
        <name>Corporate Releases</name>
        <url>http://nexus.company.com/repository/maven-releases/</url>
    </repository>
    <snapshotRepository>
        <id>nexus-snapshots</id>
        <name>Corporate Snapshots</name>
        <url>http://nexus.company.com/repository/maven-snapshots/</url>
    </snapshotRepository>
</distributionManagement>

<!-- 版本發布插件 -->
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-release-plugin</artifactId>
    <version>3.0.1</version>
    <configuration>
        <tagNameFormat>v@{project.version}</tagNameFormat>
        <autoVersionSubmodules>true</autoVersionSubmodules>
        <releaseProfiles>release</releaseProfiles>
        <goals>deploy</goals>
    </configuration>
</plugin>
```

---

*最後更新：2025年8月29日*  
*版本：1.1.0*  
*維護者：Tutorial Team*

#### 驗證 JDK 安裝

```bash
java -version
javac -version
echo $JAVA_HOME  # Linux/Mac
echo %JAVA_HOME%  # Windows
```

### 2.2 Maven 安裝

#### 2.2.1 Windows 安裝方式

**方法一：使用 Chocolatey（推薦）**
```powershell
# 安裝 Chocolatey（如果尚未安裝）
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# 安裝 Maven
choco install maven
```

**方法二：手動安裝**
1. 下載 Maven：前往 [Maven 官網](https://maven.apache.org/download.cgi)
2. 下載 Binary zip archive（如：apache-maven-3.9.4-bin.zip）
3. 解壓縮到適當目錄（如：C:\Program Files\Apache\Maven）
4. 設定環境變數：
   - 新增 `MAVEN_HOME` = `C:\Program Files\Apache\Maven\apache-maven-3.9.4`
   - 將 `%MAVEN_HOME%\bin` 加入 `PATH`

#### 2.2.2 macOS 安裝方式

**使用 Homebrew（推薦）**
```bash
# 安裝 Homebrew（如果尚未安裝）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 安裝 Maven
brew install maven
```

#### 2.2.3 Linux 安裝方式

**Ubuntu/Debian：**
```bash
sudo apt update
sudo apt install maven
```

**CentOS/RHEL：**
```bash
sudo yum install maven
# 或使用 dnf（較新版本）
sudo dnf install maven
```

### 2.3 驗證安裝成功

安裝完成後，開啟新的終端機視窗並執行：

```bash
mvn -version
```

應該會看到類似以下的輸出：
```
Apache Maven 3.9.4 (d86a17ee24cd95b4b6dc57e87667d4e2de6ab7a)
Maven home: C:\Program Files\Apache\Maven\apache-maven-3.9.4
Java version: 17.0.7, vendor: Eclipse Adoptium
Java home: C:\Program Files\Eclipse Adoptium\jdk-17.0.7.10-hotspot
Default locale: zh_TW, platform encoding: UTF-8
OS name: "windows 10", version: "10.0", arch: "amd64", family: "windows"
```

### 2.4 IDE 整合

#### 2.4.1 VS Code 整合

1. **安裝必要擴充功能：**
   - Extension Pack for Java
   - Maven for Java

2. **VS Code 設定：**
   在 `settings.json` 中加入：
   ```json
   {
     "java.configuration.maven.userSettings": "C:\\Users\\<username>\\.m2\\settings.xml",
     "maven.executable.path": "C:\\Program Files\\Apache\\Maven\\apache-maven-3.9.4\\bin\\mvn.cmd"
   }
   ```

3. **驗證整合：**
   - 打開 Java 專案
   - 在 Explorer 中應該能看到 "JAVA PROJECTS" 區段
   - 右鍵點擊 `pom.xml` 應該能看到 Maven 相關選項

#### 2.4.2 IntelliJ IDEA 整合

IntelliJ IDEA 內建 Maven 支援：

1. **檢查 Maven 設定：**
   - File → Settings → Build, Execution, Deployment → Build Tools → Maven
   - 確認 Maven home path 正確
   - 確認 User settings file 路徑正確

2. **匯入 Maven 專案：**
   - File → Open → 選擇包含 `pom.xml` 的資料夾
   - IntelliJ 會自動識別為 Maven 專案

#### 2.4.3 Eclipse 整合

Eclipse 也內建 Maven 支援（m2e 插件）：

1. **匯入 Maven 專案：**
   - File → Import → Maven → Existing Maven Projects
   - 選擇包含 `pom.xml` 的資料夾

2. **檢查 Maven 設定：**
   - Window → Preferences → Maven
   - 確認設定正確

### 2.5 設定檔配置

#### 2.5.1 Maven 設定檔位置

Maven 有兩個主要設定檔：
- **全域設定**：`${MAVEN_HOME}/conf/settings.xml`
- **使用者設定**：`${user.home}/.m2/settings.xml`（優先級較高）

#### 2.5.2 基本設定檔範例

在 `~/.m2/settings.xml` 中：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0 
          http://maven.apache.org/xsd/settings-1.0.0.xsd">
    
    <!-- 本地倉庫位置 -->
    <localRepository>C:/Users/${user.name}/.m2/repository</localRepository>
    
    <!-- 伺服器設定（如需要認證） -->
    <servers>
        <!-- 如果公司有私有倉庫需要認證 -->
        <!--
        <server>
            <id>company-nexus</id>
            <username>your-username</username>
            <password>your-password</password>
        </server>
        -->
    </servers>
    
    <!-- 鏡像設定（加速下載） -->
    <mirrors>
        <!-- 使用阿里雲鏡像加速（中國地區） -->
        <mirror>
            <id>aliyun-maven</id>
            <name>Aliyun Maven Mirror</name>
            <url>https://maven.aliyun.com/repository/central</url>
            <mirrorOf>central</mirrorOf>
        </mirror>
    </mirrors>
    
    <!-- 預設設定檔 -->
    <profiles>
        <profile>
            <id>development</id>
            <activation>
                <activeByDefault>true</activeByDefault>
            </activation>
            <properties>
                <maven.compiler.source>17</maven.compiler.source>
                <maven.compiler.target>17</maven.compiler.target>
                <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
            </properties>
        </profile>
    </profiles>
</settings>
```

#### 實務案例

在我們的專案中，建議所有開發人員使用相同的 Maven 設定，以確保：
- 相同的 JDK 版本（Java 17）
- 相同的編碼格式（UTF-8）
- 統一的倉庫來源

#### 注意事項

- 設定檔修改後需要重新啟動 IDE
- 密碼建議使用加密方式儲存
- 公司內部倉庫設定請詢問系統管理員

---

## 12. 團隊協作與規範

### 12.1 程式碼審查規範

#### 12.1.1 Maven 相關審查要點

**POM 檔案審查：**

- [ ] 依賴版本是否使用 properties 統一管理
- [ ] 依賴範圍（scope）是否正確設定
- [ ] 是否有未使用的依賴
- [ ] 版本號是否遵循語意化版本規範
- [ ] 是否有安全性漏洞的依賴

**建置配置審查：**

- [ ] 插件版本是否明確指定
- [ ] 編譯器設定是否正確
- [ ] 測試配置是否完整
- [ ] 程式碼品質檢查是否啟用

#### 12.1.2 自動化審查工具

**Maven Enforcer Plugin 規則：**

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-enforcer-plugin</artifactId>
    <version>3.3.0</version>
    <executions>
        <execution>
            <id>enforce-rules</id>
            <goals>
                <goal>enforce</goal>
            </goals>
            <configuration>
                <rules>
                    <!-- 確保 Maven 版本 -->
                    <requireMavenVersion>
                        <version>[3.8.0,)</version>
                    </requireMavenVersion>
                    
                    <!-- 確保 Java 版本 -->
                    <requireJavaVersion>
                        <version>[17,)</version>
                    </requireJavaVersion>
                    
                    <!-- 禁止重複依賴 -->
                    <banDuplicatePomDependencyVersions/>
                    
                    <!-- 依賴收斂 -->
                    <dependencyConvergence/>
                    
                    <!-- 禁止特定依賴 -->
                    <bannedDependencies>
                        <excludes>
                            <exclude>commons-logging:commons-logging</exclude>
                            <exclude>log4j:log4j</exclude>
                        </excludes>
                    </bannedDependencies>
                </rules>
            </configuration>
        </execution>
    </executions>
</plugin>
```

### 12.2 版本管理策略

#### 12.2.1 語意化版本控制

**版本號格式：** MAJOR.MINOR.PATCH

- **MAJOR**：不相容的 API 變更
- **MINOR**：向後相容的功能新增
- **PATCH**：向後相容的錯誤修正

**範例：**

```xml
<!-- 開發版本 -->
<version>1.2.0-SNAPSHOT</version>

<!-- 發布候選版本 -->
<version>1.2.0-RC1</version>

<!-- 正式版本 -->
<version>1.2.0</version>

<!-- 熱修復版本 -->
<version>1.2.1</version>
```

#### 12.2.2 版本發布流程

**使用 Maven Release Plugin：**

```bash
# 準備發布（更新版本號、建立標籤）
mvn release:prepare

# 執行發布（建置並部署）
mvn release:perform

# 回滾發布（如果出現問題）
mvn release:rollback
```

**手動版本管理：**

```bash
# 更新版本號
mvn versions:set -DnewVersion=1.2.0

# 確認更新
mvn versions:commit

# 如果需要回滾
mvn versions:revert
```

### 12.3 分支管理與 Maven

#### 12.3.1 Git Flow 與 Maven 整合

**分支策略：**

- **master/main**：正式版本（1.0.0, 1.1.0）
- **develop**：開發版本（1.1.0-SNAPSHOT）
- **feature/**：功能分支（1.1.0-SNAPSHOT）
- **release/**：發布分支（1.1.0-RC1）
- **hotfix/**：熱修復分支（1.0.1）

#### 12.3.2 CI/CD 管道中的 Maven

**GitHub Actions 範例：**

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        java-version: [11, 17, 21]
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up JDK ${{ matrix.java-version }}
      uses: actions/setup-java@v4
      with:
        java-version: ${{ matrix.java-version }}
        distribution: 'temurin'
        
    - name: Cache Maven packages
      uses: actions/cache@v3
      with:
        path: ~/.m2
        key: ${{ runner.os }}-m2-${{ hashFiles('**/pom.xml') }}
        
    - name: Run tests
      run: mvn clean verify
      
    - name: Generate test report
      uses: dorny/test-reporter@v1
      if: success() || failure()
      with:
        name: Maven Tests (JDK ${{ matrix.java-version }})
        path: target/surefire-reports/*.xml
        reporter: java-junit
        
    - name: Upload coverage to Codecov
      if: matrix.java-version == '17'
      uses: codecov/codecov-action@v3
      with:
        file: target/site/jacoco/jacoco.xml

  build-and-deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up JDK 17
      uses: actions/setup-java@v4
      with:
        java-version: '17'
        distribution: 'temurin'
        
    - name: Cache Maven packages
      uses: actions/cache@v3
      with:
        path: ~/.m2
        key: ${{ runner.os }}-m2-${{ hashFiles('**/pom.xml') }}
        
    - name: Build and package
      run: mvn clean package -DskipTests
      
    - name: Build Docker image
      run: |
        mvn docker:build
        docker tag tutorial/java-app:latest tutorial/java-app:${{ github.sha }}
        
    - name: Deploy to staging
      run: |
        # 部署到測試環境
        kubectl apply -f k8s/staging/
```

### 12.4 自動化測試策略

#### 12.4.1 測試分層架構

```xml
<!-- 單元測試 -->
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.1.2</version>
    <configuration>
        <includes>
            <include>**/*Test.java</include>
            <include>**/*Tests.java</include>
        </includes>
        <excludes>
            <exclude>**/*IntegrationTest.java</exclude>
            <exclude>**/*IT.java</exclude>
        </excludes>
    </configuration>
</plugin>

<!-- 整合測試 -->
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-failsafe-plugin</artifactId>
    <version>3.1.2</version>
    <configuration>
        <includes>
            <include>**/*IntegrationTest.java</include>
            <include>**/*IT.java</include>
        </includes>
    </configuration>
    <executions>
        <execution>
            <goals>
                <goal>integration-test</goal>
                <goal>verify</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

#### 12.4.2 測試環境管理

```xml
<profiles>
    <!-- 快速測試（只執行單元測試） -->
    <profile>
        <id>fast</id>
        <properties>
            <skipITs>true</skipITs>
            <maven.test.failure.ignore>false</maven.test.failure.ignore>
        </properties>
    </profile>
    
    <!-- 完整測試（包含整合測試） -->
    <profile>
        <id>full</id>
        <properties>
            <skipITs>false</skipITs>
        </properties>
        <build>
            <plugins>
                <!-- Testcontainers 支援 -->
                <plugin>
                    <groupId>org.springframework.boot</groupId>
                    <artifactId>spring-boot-maven-plugin</artifactId>
                    <executions>
                        <execution>
                            <id>start-spring-boot</id>
                            <phase>pre-integration-test</phase>
                            <goals>
                                <goal>start</goal>
                            </goals>
                        </execution>
                        <execution>
                            <id>stop-spring-boot</id>
                            <phase>post-integration-test</phase>
                            <goals>
                                <goal>stop</goal>
                            </goals>
                        </execution>
                    </executions>
                </plugin>
            </plugins>
        </build>
    </profile>
</profiles>
```

#### 12.4.3 測試報告整合

```xml
<!-- 測試覆蓋率報告 -->
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.10</version>
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
        <execution>
            <id>integration-test-coverage</id>
            <phase>post-integration-test</phase>
            <goals>
                <goal>report-integration</goal>
            </goals>
        </execution>
    </executions>
</plugin>

<!-- 整合所有報告 -->
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-site-plugin</artifactId>
    <version>4.0.0-M9</version>
    <configuration>
        <reportPlugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-report-plugin</artifactId>
                <version>3.1.2</version>
            </plugin>
            <plugin>
                <groupId>org.jacoco</groupId>
                <artifactId>jacoco-maven-plugin</artifactId>
                <reportSets>
                    <reportSet>
                        <reports>
                            <report>report</report>
                        </reports>
                    </reportSet>
                </reportSets>
            </plugin>
        </reportPlugins>
    </configuration>
</plugin>
```

---

## 13. Maven 與現代 Java 開發

### 13.1 Java 模組系統（JPMS）與 Maven

從 Java 9 開始引入的模組系統（Java Platform Module System, JPMS）為 Java 應用程式提供了更好的封裝性和依賴管理。

#### 13.1.1 模組化專案結構

```
src/
  main/
    java/
      module-info.java
      com/
        tutorial/
          java/
            App.java
    resources/
  test/
    java/
      com/
        tutorial/
          java/
            AppTest.java
```

#### 13.1.2 module-info.java 範例

```java
module com.tutorial.java {
    requires java.base;
    requires java.logging;
    requires org.apache.logging.log4j;
    
    exports com.tutorial.java;
    exports com.tutorial.java.util;
    
    // 僅供測試使用
    opens com.tutorial.java to junit;
}
```

#### 13.1.3 Maven 模組化專案配置

```xml
<properties>
    <maven.compiler.source>17</maven.compiler.source>
    <maven.compiler.target>17</maven.compiler.target>
    <maven.compiler.release>17</maven.compiler.release>
</properties>

<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.11.0</version>
            <configuration>
                <release>17</release>
                <compilerArgs>
                    <arg>--enable-preview</arg>
                </compilerArgs>
            </configuration>
        </plugin>
        
        <!-- 模組路徑支援 -->
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>3.1.2</version>
            <configuration>
                <useModulePath>true</useModulePath>
            </configuration>
        </plugin>
    </plugins>
</build>
```

### 13.2 Maven 與 JDK 版本管理

#### 13.2.1 多版本 JDK 支援

使用 Maven Toolchains 管理多個 JDK 版本：

**toolchains.xml**（位於 ~/.m2/）：

```xml
<?xml version="1.0" encoding="UTF8"?>
<toolchains>
    <toolchain>
        <type>jdk</type>
        <provides>
            <version>17</version>
        </provides>
        <configuration>
            <jdkHome>C:\Program Files\Java\jdk-17</jdkHome>
        </configuration>
    </toolchain>
    <toolchain>
        <type>jdk</type>
        <provides>
            <version>21</version>
        </provides>
        <configuration>
            <jdkHome>C:\Program Files\Java\jdk-21</jdkHome>
        </configuration>
    </toolchain>
</toolchains>
```

**在 pom.xml 中使用：**

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-toolchains-plugin</artifactId>
    <version>3.1.0</version>
    <configuration>
        <toolchains>
            <jdk>
                <version>17</version>
            </jdk>
        </toolchains>
    </configuration>
    <executions>
        <execution>
            <goals>
                <goal>toolchain</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

#### 13.2.2 預覽功能支援

啟用 Java 預覽功能：

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>3.11.0</version>
    <configuration>
        <compilerArgs>
            <arg>--enable-preview</arg>
        </compilerArgs>
    </configuration>
</plugin>

<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.1.2</version>
    <configuration>
        <argLine>--enable-preview</argLine>
    </configuration>
</plugin>
```

### 13.3 Maven 與記錄（Records）和文字區塊

#### 13.3.1 Records 支援

從 Java 17 開始，Records 成為正式功能：

```java
// src/main/java/com/tutorial/java/model/Student.java
package com.tutorial.java.model;

/**
 * 學生記錄類別
 * @param id 學生編號
 * @param name 學生姓名
 * @param age 學生年齡
 */
public record Student(Long id, String name, int age) {
    
    // 驗證邏輯
    public Student {
        if (age < 0) {
            throw new IllegalArgumentException("年齡不能為負數");
        }
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("姓名不能為空");
        }
    }
    
    // 自訂方法
    public boolean isAdult() {
        return age >= 18;
    }
}
```

#### 13.3.2 文字區塊（Text Blocks）

在測試和資源檔案中使用文字區塊：

```java
@Test
void testJsonParsing() {
    String jsonData = """
        {
            "id": 1,
            "name": "張三",
            "age": 20,
            "courses": [
                "Java程式設計",
                "資料結構"
            ]
        }
        """;
    
    // 測試 JSON 解析
    Student student = parseJson(jsonData);
    assertEquals("張三", student.name());
}
```

### 13.4 Maven 與虛擬執行緒

#### 13.4.1 虛擬執行緒專案配置

使用 JDK 21 的虛擬執行緒功能：

```xml
<properties>
    <maven.compiler.source>21</maven.compiler.source>
    <maven.compiler.target>21</maven.compiler.target>
    <maven.compiler.release>21</maven.compiler.release>
</properties>

<dependencies>
    <!-- 為了更好的並行處理支援 -->
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter</artifactId>
        <version>5.10.0</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```

#### 13.4.2 虛擬執行緒範例

```java
// src/main/java/com/tutorial/java/concurrent/VirtualThreadExample.java
package com.tutorial.java.concurrent;

import java.time.Duration;
import java.util.concurrent.Executors;
import java.util.stream.IntStream;

public class VirtualThreadExample {
    
    public void demonstrateVirtualThreads() {
        try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
            
            // 建立大量虛擬執行緒
            IntStream.range(0, 10_000)
                .forEach(i -> executor.submit(() -> {
                    try {
                        Thread.sleep(Duration.ofSeconds(1));
                        System.out.println("任務 " + i + " 完成");
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                    }
                }));
        }
    }
}
```

#### 13.4.3 測試虛擬執行緒

```java
@Test
void testVirtualThreadPerformance() throws InterruptedException {
    var startTime = System.currentTimeMillis();
    
    try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
        var tasks = IntStream.range(0, 1000)
            .mapToObj(i -> executor.submit(() -> {
                try {
                    Thread.sleep(100); // 模擬 I/O 操作
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
                return i;
            }))
            .toList();
        
        // 等待所有任務完成
        for (var task : tasks) {
            task.get();
        }
    }
    
    var endTime = System.currentTimeMillis();
    var duration = endTime - startTime;
    
    // 虛擬執行緒應該能在合理時間內完成
    assertTrue(duration < 5000, "執行時間過長: " + duration + "ms");
}
```

---

## 14. 效能調校與監控

### 14.1 Maven 建置效能優化

#### 14.1.1 並行建置

使用多核心處理器加速建置：

```bash
# 使用所有可用的 CPU 核心
mvn clean install -T 1C

# 使用指定數量的執行緒
mvn clean install -T 4

# 在我們的專案中建議使用
mvn clean install -T 2C
```

#### 14.1.2 增量編譯

啟用增量編譯以加速重複建置：

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>3.11.0</version>
    <configuration>
        <useIncrementalCompilation>true</useIncrementalCompilation>
        <source>17</source>
        <target>17</target>
    </configuration>
</plugin>
```

#### 14.1.3 記憶體設定優化

設定適當的 Maven 記憶體參數：

**Windows：**

```cmd
set MAVEN_OPTS=-Xmx4g -Xms1g -XX:ReservedCodeCacheSize=512m -XX:+UseG1GC
```

**Linux/Mac：**

```bash
export MAVEN_OPTS="-Xmx4g -Xms1g -XX:ReservedCodeCacheSize=512m -XX:+UseG1GC"
```

#### 14.1.4 跳過非必要階段

在開發期間跳過耗時的檢查：

```bash
# 跳過測試和程式碼檢查（僅限開發階段）
mvn clean compile -DskipTests -Dcheckstyle.skip -Dpmd.skip -DskipITs

# 快速重新編譯
mvn compile -Dmaven.compiler.useIncrementalCompilation=true
```

### 14.2 依賴解析效能調校

#### 14.2.1 本地倉庫優化

定期清理本地倉庫：

```bash
# 清理損壞的依賴
mvn dependency:purge-local-repository

# 刪除舊版本（小心使用）
mvn dependency:purge-local-repository -DactTransitively=false
```

#### 14.2.2 使用依賴快取

配置企業級倉庫代理：

```xml
<!-- settings.xml -->
<mirrors>
    <mirror>
        <id>company-nexus</id>
        <name>Company Nexus Repository</name>
        <url>http://nexus.company.com/repository/maven-public/</url>
        <mirrorOf>*</mirrorOf>
    </mirror>
</mirrors>
```

#### 14.2.3 依賴版本固定

避免使用範圍版本以減少解析時間：

```xml
<!-- 好的做法：使用固定版本 -->
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.9.2</version>
    <scope>test</scope>
</dependency>

<!-- 避免使用範圍版本 -->
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>[5.0,6.0)</version>
    <scope>test</scope>
</dependency>
```

### 14.3 建置時間監控與分析

#### 14.3.1 建置時間分析插件

```xml
<plugin>
    <groupId>co.leantechniques</groupId>
    <artifactId>maven-buildtime-extension</artifactId>
    <version>3.0.4</version>
    <extensions>true</extensions>
</plugin>
```

#### 14.3.2 性能分析指令

```bash
# 詳細的建置時間報告
mvn clean install -Dmaven.buildtime.enabled=true

# 分析依賴解析時間
mvn dependency:resolve -X

# 查看插件執行時間
mvn clean install -Dmaven.buildtime.enabled=true -Dmaven.buildtime.print=true
```

#### 14.3.3 持續監控腳本

建立建置時間監控腳本：

```bash
#!/bin/bash
# build_monitor.sh

echo "開始建置監控 - $(date)"
start_time=$(date +%s)

mvn clean install -T 2C

end_time=$(date +%s)
duration=$((end_time - start_time))

echo "建置完成 - 耗時: ${duration} 秒"

# 記錄到日誌檔案
echo "$(date): 建置耗時 ${duration} 秒" >> build_times.log
```

### 14.4 記憶體使用最佳化

#### 14.4.1 監控記憶體使用

```bash
# 監控 Maven 記憶體使用
mvn clean install -Dmaven.buildtime.enabled=true

# 使用 JVM 記憶體分析
mvn clean install -XX:+PrintGCDetails -XX:+PrintGCTimeStamps
```

#### 14.4.2 大型專案記憶體設定

```bash
# 大型專案建議設定
export MAVEN_OPTS="-Xmx8g -Xms2g -XX:MetaspaceSize=512m -XX:+UseG1GC -XX:+UnlockExperimentalVMOptions -XX:+UseJVMCICompiler"
```

#### 14.4.3 記憶體洩漏檢測

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.1.2</version>
    <configuration>
        <argLine>
            -XX:+UnlockExperimentalVMOptions
            -XX:+UseEpsilonGC
            -Xmx512m
        </argLine>
        <forkedProcessExitTimeoutInSeconds>60</forkedProcessExitTimeoutInSeconds>
    </configuration>
</plugin>
```

---

## 15. 錯誤處理與除錯技巧

### 15.1 常見錯誤診斷流程

#### 15.1.1 系統性錯誤診斷步驟

當遇到 Maven 錯誤時，請按照以下步驟進行診斷：

1. **記錄完整錯誤訊息**

```bash
# 使用詳細模式查看完整錯誤
mvn clean install -X > build.log 2>&1
```

2. **檢查基本環境**

```bash
# 驗證 Java 環境
java -version
echo $JAVA_HOME

# 驗證 Maven 環境
mvn -version

# 檢查專案結構
find . -name "pom.xml" -exec echo "Found POM: {}" \;
```

3. **分析錯誤類型**

| 錯誤類型 | 關鍵字 | 檢查重點 |
|----------|--------|----------|
| 編譯錯誤 | `[ERROR] COMPILATION ERROR` | Java 語法、匯入、泛型 |
| 依賴錯誤 | `Could not resolve dependencies` | 網路、倉庫、版本衝突 |
| 插件錯誤 | `Plugin execution not covered` | 插件版本、配置 |
| 測試失敗 | `Tests run:`, `Failures:` | 測試邏輯、環境設定 |

#### 15.1.2 錯誤分類與對應策略

**編譯錯誤：**

```bash
# 檢查編譯錯誤
mvn compile -X

# 常見解決方法
mvn clean compile  # 清理後重新編譯
mvn clean install -U  # 強制更新依賴
```

**依賴衝突：**

```bash
# 分析依賴衝突
mvn dependency:tree -Dverbose

# 排除衝突依賴
mvn dependency:analyze-duplicate
```

### 15.2 除錯工具與技巧

#### 15.2.1 Maven 內建除錯功能

```bash
# 詳細輸出模式
mvn clean install -X

# 除錯特定插件
mvn clean install -Dmaven.plugin.debug=true

# 離線模式除錯
mvn clean install -o -X
```

#### 15.2.2 使用 Maven Wrapper 除錯

```bash
# 檢查 Wrapper 版本
./mvnw --version

# 使用 Wrapper 除錯
./mvnw clean install -X

# 更新 Wrapper
./mvnw wrapper:wrapper -Dmaven=3.9.4
```

#### 15.2.3 IDE 整合除錯

**VS Code 除錯設定：**

在 `.vscode/launch.json` 中設定：

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "java",
            "name": "Debug Maven Test",
            "request": "launch",
            "mainClass": "",
            "projectName": "java-vscode-tutorial",
            "args": "",
            "vmArgs": "-Dmaven.surefire.debug"
        }
    ]
}
```

### 15.3 日誌分析與解讀

#### 15.3.1 Maven 日誌層級

```bash
# 錯誤級別（預設）
mvn clean install

# 警告級別
mvn clean install -q

# 資訊級別
mvn clean install -X

# 除錯級別
mvn clean install -X -e
```

#### 15.3.2 關鍵日誌模式識別

**成功模式：**

```
[INFO] BUILD SUCCESS
[INFO] Total time: 45.123 s
[INFO] Finished at: 2025-08-29T10:30:00+08:00
```

**失敗模式：**

```
[ERROR] BUILD FAILURE
[ERROR] Total time: 15.456 s
[ERROR] Failed to execute goal on project java-vscode-tutorial
```

**警告模式：**

```
[WARNING] Some problems were encountered while building the effective model
[WARNING] 'build.plugins.plugin.version' for org.apache.maven.plugins:maven-compiler-plugin is missing
```

#### 15.3.3 自動化日誌分析腳本

```bash
#!/bin/bash
# analyze_build_log.sh

LOG_FILE="build.log"

echo "=== Maven 建置日誌分析 ==="
echo "分析檔案: $LOG_FILE"
echo

# 統計錯誤數量
ERROR_COUNT=$(grep -c "\[ERROR\]" "$LOG_FILE")
echo "錯誤數量: $ERROR_COUNT"

# 統計警告數量
WARNING_COUNT=$(grep -c "\[WARNING\]" "$LOG_FILE")
echo "警告數量: $WARNING_COUNT"

# 顯示主要錯誤
if [ $ERROR_COUNT -gt 0 ]; then
    echo
    echo "=== 主要錯誤 ==="
    grep "\[ERROR\]" "$LOG_FILE" | head -10
fi

# 顯示建置時間
echo
echo "=== 建置時間 ==="
grep "Total time:" "$LOG_FILE" | tail -1
```

### 15.4 遠端除錯設定

#### 15.4.1 Maven 測試遠端除錯

```bash
# 啟用遠端除錯端口
mvn test -Dmaven.surefire.debug

# 或使用指定端口
mvn test -Dmaven.surefire.debug="-agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=8000"
```

#### 15.4.2 應用程式遠端除錯

```xml
<plugin>
    <groupId>org.codehaus.mojo</groupId>
    <artifactId>exec-maven-plugin</artifactId>
    <version>3.1.0</version>
    <configuration>
        <mainClass>com.tutorial.java.App</mainClass>
        <args>
            <arg>-agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=5005</arg>
        </args>
    </configuration>
</plugin>
```

#### 15.4.3 VS Code 遠端除錯配置

```json
{
    "type": "java",
    "name": "Attach to Remote Java Application",
    "request": "attach",
    "hostName": "localhost",
    "port": 5005,
    "projectName": "java-vscode-tutorial"
}
```

---

## 16. 實戰專案範例

### 16.1 簡單控制台應用程式

#### 16.1.1 專案建立

```bash
# 使用 Maven archetype 建立專案
mvn archetype:generate \
    -DgroupId=com.tutorial.console \
    -DartifactId=console-calculator \
    -DarchetypeArtifactId=maven-archetype-quickstart \
    -DinteractiveMode=false
```

#### 16.1.2 基本 POM 配置

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.tutorial.console</groupId>
    <artifactId>console-calculator</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>

    <name>Console Calculator</name>
    <description>簡單的控制台計算機應用程式</description>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <junit.version>5.9.2</junit.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>${junit.version}</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
            </plugin>

            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.1.2</version>
            </plugin>

            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>3.1.0</version>
                <configuration>
                    <mainClass>com.tutorial.console.CalculatorApp</mainClass>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

#### 16.1.3 主要類別實作

```java
// src/main/java/com/tutorial/console/CalculatorApp.java
package com.tutorial.console;

import java.util.Scanner;

public class CalculatorApp {
    
    private final Calculator calculator = new Calculator();
    private final Scanner scanner = new Scanner(System.in);
    
    public static void main(String[] args) {
        new CalculatorApp().run();
    }
    
    public void run() {
        System.out.println("=== 控制台計算機 ===");
        System.out.println("輸入 'exit' 結束程式");
        
        while (true) {
            try {
                System.out.print("請輸入運算式 (例: 5 + 3): ");
                String input = scanner.nextLine().trim();
                
                if ("exit".equalsIgnoreCase(input)) {
                    break;
                }
                
                double result = calculator.evaluate(input);
                System.out.println("結果: " + result);
                
            } catch (Exception e) {
                System.err.println("錯誤: " + e.getMessage());
            }
        }
        
        System.out.println("感謝使用！");
        scanner.close();
    }
}

// src/main/java/com/tutorial/console/Calculator.java
package com.tutorial.console;

public class Calculator {
    
    public double evaluate(String expression) {
        String[] parts = expression.split("\\s+");
        
        if (parts.length != 3) {
            throw new IllegalArgumentException("格式錯誤，請使用: 數字 運算符 數字");
        }
        
        double a = Double.parseDouble(parts[0]);
        String operator = parts[1];
        double b = Double.parseDouble(parts[2]);
        
        return switch (operator) {
            case "+" -> a + b;
            case "-" -> a - b;
            case "*" -> a * b;
            case "/" -> {
                if (b == 0) {
                    throw new ArithmeticException("除數不能為零");
                }
                yield a / b;
            }
            default -> throw new IllegalArgumentException("不支援的運算符: " + operator);
        };
    }
}
```

#### 16.1.4 測試類別

```java
// src/test/java/com/tutorial/console/CalculatorTest.java
package com.tutorial.console;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {
    
    private Calculator calculator;
    
    @BeforeEach
    void setUp() {
        calculator = new Calculator();
    }
    
    @Test
    void testAddition() {
        assertEquals(8.0, calculator.evaluate("5 + 3"));
        assertEquals(-2.0, calculator.evaluate("-5 + 3"));
    }
    
    @Test
    void testSubtraction() {
        assertEquals(2.0, calculator.evaluate("5 - 3"));
        assertEquals(-8.0, calculator.evaluate("-5 - 3"));
    }
    
    @Test
    void testMultiplication() {
        assertEquals(15.0, calculator.evaluate("5 * 3"));
        assertEquals(-15.0, calculator.evaluate("-5 * 3"));
    }
    
    @Test
    void testDivision() {
        assertEquals(2.5, calculator.evaluate("5 / 2"));
        assertEquals(-2.5, calculator.evaluate("-5 / 2"));
    }
    
    @Test
    void testDivisionByZero() {
        assertThrows(ArithmeticException.class, 
            () -> calculator.evaluate("5 / 0"));
    }
    
    @Test
    void testInvalidFormat() {
        assertThrows(IllegalArgumentException.class, 
            () -> calculator.evaluate("5 +"));
        assertThrows(IllegalArgumentException.class, 
            () -> calculator.evaluate("invalid"));
    }
    
    @Test
    void testUnsupportedOperator() {
        assertThrows(IllegalArgumentException.class, 
            () -> calculator.evaluate("5 % 3"));
    }
}
```

#### 16.1.5 執行和測試

```bash
# 編譯專案
mvn compile

# 執行測試
mvn test

# 執行應用程式
mvn exec:java

# 打包
mvn package

# 執行打包後的 JAR
java -cp target/console-calculator-1.0.0.jar com.tutorial.console.CalculatorApp
```

### 16.2 Spring Boot Web 應用程式

#### 16.2.1 Spring Boot 專案結構

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.1.2</version>
        <relativePath/>
    </parent>

    <groupId>com.tutorial.web</groupId>
    <artifactId>student-management</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>

    <name>Student Management System</name>
    <description>學生管理系統 Web 應用程式</description>

    <properties>
        <java.version>17</java.version>
    </properties>

    <dependencies>
        <!-- Spring Boot Starters -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-validation</artifactId>
        </dependency>

        <!-- Database -->
        <dependency>
            <groupId>com.h2database</groupId>
            <artifactId>h2</artifactId>
            <scope>runtime</scope>
        </dependency>

        <!-- Testing -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
        
        <!-- Development Tools -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-devtools</artifactId>
            <scope>runtime</scope>
            <optional>true</optional>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
```

#### 16.2.2 主應用程式類別

```java
// src/main/java/com/tutorial/web/StudentManagementApplication.java
package com.tutorial.web;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class StudentManagementApplication {
    
    public static void main(String[] args) {
        SpringApplication.run(StudentManagementApplication.class, args);
    }
}
```

#### 16.2.3 Maven 指令

```bash
# Spring Boot 專案特有指令
mvn spring-boot:run              # 執行應用程式
mvn spring-boot:build-image      # 建立 Docker 映像
mvn spring-boot:repackage        # 重新打包為可執行 JAR

# 標準 Maven 指令
mvn clean package               # 清理並打包
mvn test                       # 執行測試
mvn spring-boot:run -Dspring-boot.run.profiles=dev  # 使用特定設定檔執行
```

### 16.3 多模組企業級專案

#### 16.3.1 父專案 POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.tutorial.enterprise</groupId>
    <artifactId>enterprise-system</artifactId>
    <version>1.0.0</version>
    <packaging>pom</packaging>

    <name>Enterprise System</name>
    <description>企業級多模組系統</description>

    <modules>
        <module>enterprise-common</module>
        <module>enterprise-domain</module>
        <module>enterprise-service</module>
        <module>enterprise-web</module>
        <module>enterprise-integration-tests</module>
    </modules>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        
        <!-- 版本管理 -->
        <spring-boot.version>3.1.2</spring-boot.version>
        <junit.version>5.9.2</junit.version>
        <mockito.version>5.4.0</mockito.version>
    </properties>

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
            
            <!-- 內部模組 -->
            <dependency>
                <groupId>com.tutorial.enterprise</groupId>
                <artifactId>enterprise-common</artifactId>
                <version>${project.version}</version>
            </dependency>
            
            <dependency>
                <groupId>com.tutorial.enterprise</groupId>
                <artifactId>enterprise-domain</artifactId>
                <version>${project.version}</version>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <build>
        <pluginManagement>
            <plugins>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-compiler-plugin</artifactId>
                    <version>3.11.0</version>
                </plugin>
                
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-surefire-plugin</artifactId>
                    <version>3.1.2</version>
                </plugin>
                
                <plugin>
                    <groupId>org.springframework.boot</groupId>
                    <artifactId>spring-boot-maven-plugin</artifactId>
                    <version>${spring-boot.version}</version>
                </plugin>
            </plugins>
        </pluginManagement>
    </build>
</project>
```

#### 16.3.2 多模組建置指令

```bash
# 從根目錄建置所有模組
mvn clean install

# 建置特定模組
mvn clean install -pl enterprise-web

# 建置模組及其依賴
mvn clean install -pl enterprise-web -am

# 跳過測試建置
mvn clean install -DskipTests

# 並行建置多模組
mvn clean install -T 1C

# 僅建置變更的模組
mvn clean install -amd
```

### 16.4 微服務架構專案

#### 16.4.1 微服務父 POM

```xml
<project>
    <modelVersion>4.0.0</modelVersion>
    
    <groupId>com.tutorial.microservices</groupId>
    <artifactId>microservices-parent</artifactId>
    <version>1.0.0</version>
    <packaging>pom</packaging>
    
    <modules>
        <module>user-service</module>
        <module>order-service</module>
        <module>gateway-service</module>
        <module>discovery-service</module>
    </modules>
    
    <properties>
        <spring-cloud.version>2022.0.3</spring-cloud.version>
        <spring-boot.version>3.1.2</spring-boot.version>
    </properties>
    
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>${spring-cloud.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
</project>
```

#### 16.4.2 微服務建置策略

```bash
# 建置所有微服務
mvn clean package -T 1C

# 建立 Docker 映像
mvn clean package docker:build -T 1C

# 執行整合測試
mvn clean verify -Pintegration-tests

# 本地開發環境啟動
mvn spring-boot:run -pl discovery-service &
mvn spring-boot:run -pl gateway-service &
mvn spring-boot:run -pl user-service &
mvn spring-boot:run -pl order-service &
```

---

*最後更新：2025年8月29日*  
*版本：2.0.0*  
*維護者：Tutorial Team*

---

