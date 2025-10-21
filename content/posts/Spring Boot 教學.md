+++
date = '2025-10-21T17:05:04+08:00'
draft = false
title = 'Spring Boot 教學'
tags = ['教學','framework' ,'Spring Boot']
categories = ['技術']
author = 'Eric Cheng'
summary = '提供完整Spring Boot framework教學'
+++

# Spring Boot 教學手冊

## 文件資訊
- **作者**: 技術團隊
- **版本**: 1.0
- **更新日期**: 2025-08-31
- **目標對象**: 新進開發同仁、Spring Boot 初學者、認證考試準備者

## 目錄
1. [Spring Boot 簡介](#1-spring-boot-簡介)
   - 1.1 [什麼是 Spring Boot？](#11-什麼是-spring-boot)
   - 1.2 [Spring Boot 的核心特點](#12-spring-boot-的核心特點)
   - 1.3 [Spring Boot vs Spring Framework](#13-spring-boot-vs-spring-framework)
   - 1.4 [專案常見應用場景](#14-專案常見應用場景)
   - 1.5 [Spring Boot 版本選擇](#15-spring-boot-版本選擇)
   - 1.6 [章節小練習](#16-章節小練習)
   - 1.7 [實務注意事項](#17-實務注意事項)

2. [開發環境建置](#2-開發環境建置)
   - 2.1 [系統需求](#21-系統需求)
   - 2.2 [JDK 安裝與設定](#22-jdk-安裝與設定)
   - 2.3 [Maven 安裝與設定](#23-maven-安裝與設定)
   - 2.4 [IDE 設定](#24-ide-設定)
   - 2.5 [Spring Initializr 使用](#25-spring-initializr-使用)
   - 2.6 [開發工具設定](#26-開發工具設定)
   - 2.7 [專案建立實作](#27-專案建立實作)
   - 2.8 [執行與測試](#28-執行與測試)
   - 2.9 [章節小練習](#29-章節小練習)
   - 2.10 [實務注意事項](#210-實務注意事項)

3. [Spring Boot 基礎](#3-spring-boot-基礎)
   - 3.1 [專案結構](#31-專案結構)
   - 3.2 [Application Properties 設定](#32-application-properties-設定)
   - 3.3 [依賴注入 (Dependency Injection)](#33-依賴注入-dependency-injection)
   - 3.4 [Spring Boot Starter](#34-spring-boot-starter)
   - 3.5 [Bean 生命週期與作用域](#35-bean-生命週期與作用域)
   - 3.6 [Profile 環境管理](#36-profile-環境管理)
   - 3.7 [章節小練習](#37-章節小練習)
   - 3.8 [實務注意事項](#38-實務注意事項)

4. [RESTful API 開發](#4-restful-api-開發)
   - 4.1 [REST 基本概念](#41-rest-基本概念)
   - 4.2 [Controller 層開發](#42-controller-層開發)
   - 4.3 [Service 層開發](#43-service-層開發)
   - 4.4 [Repository 層開發](#44-repository-層開發)
   - 4.5 [章節小練習](#45-章節小練習)
   - 4.6 [實務注意事項](#46-實務注意事項)

5. [與資料庫整合](#5-與資料庫整合)
   - 5.1 [JPA 基礎配置](#51-jpa-基礎配置)
   - 5.2 [實體類別設計](#52-實體類別設計)
   - 5.3 [Repository 層進階應用](#53-repository-層進階應用)
   - 5.4 [事務管理](#54-事務管理)
   - 5.5 [資料庫連線池配置](#55-資料庫連線池配置)
   - 5.6 [章節小練習](#56-章節小練習)
   - 5.7 [實務注意事項](#57-實務注意事項)

6. [常用功能](#6-常用功能)
   - 6.1 [資料驗證 (Validation)](#61-資料驗證-validation)
   - 6.2 [異常處理 (Exception Handling)](#62-異常處理-exception-handling)
   - 6.3 [日誌記錄 (Logging)](#63-日誌記錄-logging)
   - 6.4 [安全性基礎 (Security)](#64-安全性基礎-security)
   - 6.5 [章節小練習](#65-章節小練習)
   - 6.6 [實務注意事項](#66-實務注意事項)

7. [測試與品質](#7-測試與品質)
   - 7.1 [單元測試 (Unit Testing)](#71-單元測試-unit-testing)
   - 7.2 [整合測試 (Integration Testing)](#72-整合測試-integration-testing)
   - 7.3 [測試配置與工具](#73-測試配置與工具)
   - 7.4 [效能測試](#74-效能測試)
   - 7.5 [測試覆蓋率](#75-測試覆蓋率)
   - 7.6 [章節小練習](#76-章節小練習)
   - 7.7 [實務注意事項](#77-實務注意事項)

8. [部署與實務應用](#8-部署與實務應用)
   - 8.1 [內嵌伺服器配置](#81-內嵌伺服器配置)
   - 8.2 [Docker 容器化](#82-docker-容器化)
   - 8.3 [雲端部署](#83-雲端部署)
   - 8.4 [監控與維運](#84-監控與維運)
   - 8.5 [CI/CD 整合](#85-cicd-整合)
   - 8.6 [章節小練習](#86-章節小練習)
   - 8.7 [實務注意事項](#87-實務注意事項)

9. [認證考試重點](#9-認證考試重點)
   - 9.1 [Spring Boot 核心概念考點](#91-spring-boot-核心概念考點)
   - 9.2 [Web 開發考點](#92-web-開發考點)
   - 9.3 [資料存取考點](#93-資料存取考點)
   - 9.4 [安全性考點](#94-安全性考點)
   - 9.5 [測試考點](#95-測試考點)
   - 9.6 [Actuator 與監控](#96-actuator-與監控-)
   - 9.7 [模擬練習題](#97-模擬練習題)
   - 9.8 [考試準備策略](#98-考試準備策略)

10. [常見問題與最佳實務](#10-常見問題與最佳實務)
    - 10.1 [常見問題 FAQ](#101-常見問題-faq)
    - 10.2 [最佳實務總結](#102-最佳實務總結)

11. [檢查清單](#11-檢查清單)
    - 11.1 [開發環境檢查清單](#111-開發環境檢查清單)
    - 11.2 [開發階段檢查清單](#112-開發階段檢查清單)
    - 11.3 [測試階段檢查清單](#113-測試階段檢查清單)
    - 11.4 [安全性檢查清單](#114-安全性檢查清單)
    - 11.5 [部署前檢查清單](#115-部署前檢查清單)
    - 11.6 [生產環境檢查清單](#116-生產環境檢查清單)
    - 11.7 [認證考試檢查清單](#117-認證考試檢查清單)

---

## 1. Spring Boot 簡介

### 1.1 什麼是 Spring Boot？

Spring Boot 是基於 Spring Framework 的快速開發框架，旨在簡化 Spring 應用程式的建立與配置。它遵循「約定勝於配置」(Convention over Configuration) 的原則，讓開發者能夠快速建立獨立的、生產級別的 Spring 應用程式。

### 1.2 Spring Boot 的核心特點

#### 1.2.1 自動配置 (Auto Configuration)
```java
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

**說明**：
- `@SpringBootApplication` 包含了自動配置註解
- 自動掃描並配置相關元件
- 減少手動配置的工作量

#### 1.2.2 內嵌伺服器
```yaml
# application.yml
server:
  port: 8080
  servlet:
    context-path: /api
```

**優點**：
- 內建 Tomcat、Jetty、Undertow
- 無需外部部署容器
- 支援微服務架構

#### 1.2.3 起始依賴 (Starter Dependencies)
```xml
<!-- pom.xml -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

**作用**：
- 預設依賴版本管理
- 相容性保證
- 簡化 Maven/Gradle 配置

### 1.3 Spring Boot vs Spring Framework

| 特點 | Spring Framework | Spring Boot |
|------|------------------|-------------|
| 配置複雜度 | 需要大量 XML 或 Java 配置 | 自動配置，最小配置 |
| 專案啟動 | 需要外部應用伺服器 | 內嵌伺服器，獨立執行 |
| 依賴管理 | 手動管理版本相容性 | Starter 自動管理 |
| 開發速度 | 較慢 | 快速開發 |
| 學習曲線 | 陡峭 | 相對平緩 |

### 1.4 專案常見應用場景

#### 1.4.1 微服務架構
```java
@RestController
@RequestMapping("/users")
public class UserController {
    
    @Autowired
    private UserService userService;
    
    @GetMapping("/{id}")
    public ResponseEntity<User> getUser(@PathVariable Long id) {
        User user = userService.findById(id);
        return ResponseEntity.ok(user);
    }
}
```

#### 1.4.2 企業級應用程式
- RESTful API 服務
- 資料處理應用程式
- 批次處理系統
- 即時訊息系統

#### 1.4.3 雲端原生應用
- 容器化部署
- 彈性擴展
- 監控和健康檢查

### 1.5 Spring Boot 版本選擇

#### 1.5.1 版本策略
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>3.1.0</version>
    <relativePath/>
</parent>
```

**建議**：
- 生產環境使用 LTS 版本
- 開發環境可嘗試最新穩定版
- 關注安全更新

### 1.6 章節小練習

**問題 1**: Spring Boot 的核心設計原則是什麼？
**答案**: 約定勝於配置 (Convention over Configuration)

**問題 2**: 列出 Spring Boot 相較於傳統 Spring Framework 的三個主要優勢。
**答案**: 
1. 自動配置減少手動設定
2. 內嵌伺服器支援獨立部署
3. Starter 依賴簡化版本管理

**問題 3**: 下列哪個註解包含了 Spring Boot 的自動配置功能？
A) @Configuration
B) @SpringBootApplication 
C) @ComponentScan
D) @EnableAutoConfiguration

**答案**: B) @SpringBootApplication（包含了 @EnableAutoConfiguration）

### 1.7 實務注意事項

#### ⚠️ 重要提醒
1. **版本相容性**: 確保 Java 版本與 Spring Boot 版本相容
2. **記憶體管理**: 注意 JVM 記憶體設定，特別是在容器環境中
3. **安全性**: 生產環境務必關閉不必要的端點和功能
4. **監控**: 啟用 Actuator 進行應用程式監控

#### 💡 最佳實務
- 使用 Spring Initializr 建立專案
- 遵循標準的專案結構
- 適當使用 Profile 管理不同環境
- 定期更新版本以獲得安全修補

---

## 2. 開發環境建置

### 2.1 系統需求

#### 2.1.1 基本需求
| 軟體 | 最低版本 | 建議版本 | 備註 |
|------|----------|----------|------|
| JDK | 17 | 21 | Spring Boot 3.x 需求 |
| Maven | 3.6.3 | 3.9.x | 專案建置工具 |
| IDE | - | IntelliJ IDEA / VS Code | 開發環境 |

#### 2.1.2 作業系統支援
- Windows 10/11
- macOS 10.14+
- Linux (Ubuntu 18.04+)

### 2.2 JDK 安裝與設定

#### 2.2.1 下載與安裝
```bash
# 檢查當前 Java 版本
java -version

# 檢查 JAVA_HOME 環境變數
echo $JAVA_HOME
```

#### 2.2.2 環境變數設定
**Windows 環境**：
```powershell
# 設定 JAVA_HOME
$env:JAVA_HOME = "C:\Program Files\Java\jdk-21"
$env:PATH += ";$env:JAVA_HOME\bin"
```

**Linux/macOS 環境**：
```bash
# 在 ~/.bashrc 或 ~/.zshrc 中添加
export JAVA_HOME=/usr/lib/jvm/java-21-openjdk
export PATH=$JAVA_HOME/bin:$PATH
```

### 2.3 Maven 安裝與設定

#### 2.3.1 下載與安裝
```bash
# 檢查 Maven 版本
mvn -version

# 輸出範例
Apache Maven 3.9.4
Maven home: /usr/share/maven
Java version: 21.0.1
```

#### 2.3.2 Maven 設定檔
**settings.xml 設定**：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0 
          http://maven.apache.org/xsd/settings-1.0.0.xsd">
  
  <localRepository>${user.home}/.m2/repository</localRepository>
  
  <mirrors>
    <mirror>
      <id>central</id>
      <name>Maven Central</name>
      <url>https://repo1.maven.org/maven2</url>
      <mirrorOf>central</mirrorOf>
    </mirror>
  </mirrors>
  
  <profiles>
    <profile>
      <id>default</id>
      <properties>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
      </properties>
    </profile>
  </profiles>
  
  <activeProfiles>
    <activeProfile>default</activeProfile>
  </activeProfiles>
</settings>
```

### 2.4 IDE 設定

#### 2.4.1 IntelliJ IDEA 設定
```
1. 安裝 IntelliJ IDEA Community/Ultimate
2. 安裝必要外掛：
   - Spring Boot
   - Lombok
   - SonarLint
3. 設定 JDK 和 Maven 路徑
4. 匯入程式碼樣式設定
```

#### 2.4.2 VS Code 設定
**必要擴充功能**：
```json
{
  "recommendations": [
    "redhat.java",
    "vscjava.vscode-java-pack",
    "vmware.vscode-spring-boot",
    "pivotal.vscode-spring-boot",
    "gabrielbb.vscode-lombok"
  ]
}
```

**設定檔 (settings.json)**：
```json
{
  "java.home": "C:\\Program Files\\Java\\jdk-21",
  "maven.executable.path": "C:\\Program Files\\Apache\\maven\\bin\\mvn.cmd",
  "spring-boot.ls.logfile": {
    "on": true
  },
  "java.format.settings.url": "https://raw.githubusercontent.com/google/styleguide/gh-pages/eclipse-java-google-style.xml"
}
```

### 2.5 Spring Initializr 使用

#### 2.5.1 網頁版使用
```
1. 訪問 https://start.spring.io/
2. 選擇專案設定：
   - Project: Maven
   - Language: Java
   - Spring Boot: 3.1.x
   - Group: com.example
   - Artifact: demo
   - Packaging: Jar
   - Java: 21
3. 添加依賴：
   - Spring Web
   - Spring Data JPA
   - H2 Database
   - Spring Boot DevTools
4. 產生並下載專案
```

#### 2.5.2 IDE 整合使用
**IntelliJ IDEA**：
```
File → New → Project → Spring Initializr
```

**VS Code**：
```
Ctrl+Shift+P → Spring Initializr: Generate a Maven Project
```

#### 2.5.3 命令列使用
```bash
# 使用 Spring Boot CLI
spring init --dependencies=web,data-jpa,h2 --java-version=21 my-project

# 使用 curl
curl https://start.spring.io/starter.zip \
  -d dependencies=web,data-jpa,h2 \
  -d javaVersion=21 \
  -d bootVersion=3.1.0 \
  -d groupId=com.example \
  -d artifactId=demo \
  -o demo.zip
```

### 2.6 開發工具設定

#### 2.6.1 Git 設定
```bash
# 基本設定
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 設定預設編輯器
git config --global core.editor "code --wait"

# 設定換行符處理
git config --global core.autocrlf true  # Windows
git config --global core.autocrlf input # macOS/Linux
```

#### 2.6.2 必要工具
```bash
# 安裝 Node.js (用於前端工具)
node --version
npm --version

# 安裝 Docker (用於容器化)
docker --version
docker-compose --version

# 安裝 Postman 或 Insomnia (API 測試)
```

### 2.7 專案建立實作

#### 2.7.1 建立第一個 Spring Boot 專案
```xml
<!-- pom.xml -->
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.1.0</version>
        <relativePath/>
    </parent>
    
    <groupId>com.tutorial</groupId>
    <artifactId>spring-boot-demo</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>spring-boot-demo</name>
    <description>Spring Boot Tutorial Demo</description>
    
    <properties>
        <java.version>21</java.version>
    </properties>
    
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-devtools</artifactId>
            <scope>runtime</scope>
            <optional>true</optional>
        </dependency>
        
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
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

#### 2.7.2 主程式類別
```java
package com.tutorial;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * Spring Boot 應用程式主程式
 * 
 * @author Tutorial Team
 */
@SpringBootApplication
public class SpringBootDemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(SpringBootDemoApplication.class, args);
    }
}
```

#### 2.7.3 第一個 Controller
```java
package com.tutorial.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Hello World 控制器
 */
@RestController
public class HelloController {

    @GetMapping("/hello")
    public String hello() {
        return "Hello, Spring Boot!";
    }
    
    @GetMapping("/")
    public String home() {
        return "Welcome to Spring Boot Tutorial!";
    }
}
```

### 2.8 執行與測試

#### 2.8.1 啟動應用程式
```bash
# 使用 Maven 啟動
mvn spring-boot:run

# 或編譯後執行 JAR
mvn clean package
java -jar target/spring-boot-demo-0.0.1-SNAPSHOT.jar
```

#### 2.8.2 測試端點
```bash
# 測試 Hello 端點
curl http://localhost:8080/hello

# 預期輸出: Hello, Spring Boot!

# 測試首頁
curl http://localhost:8080/

# 預期輸出: Welcome to Spring Boot Tutorial!
```

### 2.9 章節小練習

**問題 1**: Spring Boot 3.x 最低需要哪個版本的 JDK？
**答案**: JDK 17

**問題 2**: 列出建立 Spring Boot 專案的三種方式。
**答案**: 
1. 使用 Spring Initializr 網站
2. 在 IDE 中使用 Spring Initializr 外掛
3. 使用命令列工具 (Spring Boot CLI 或 curl)

**問題 3**: 完成以下 pom.xml 設定：
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>______________________</artifactId>
    <version>3.1.0</version>
</parent>
```
**答案**: `spring-boot-starter-parent`

### 2.10 實務注意事項

#### ⚠️ 重要提醒
1. **JDK 版本**: 確保使用正確的 JDK 版本，Spring Boot 3.x 需要 JDK 17+
2. **IDE 設定**: 正確設定 IDE 的 JDK 和 Maven 路徑
3. **網路環境**: 企業環境可能需要設定代理伺服器
4. **版本一致性**: 團隊開發時確保環境版本一致

#### 💡 最佳實務
- 使用版本管理工具 (如 SDKMAN) 管理多個 JDK 版本
- 設定 IDE 的程式碼格式和檢查規則
- 建立專案範本，統一團隊開發標準
- 使用 Docker 確保開發環境一致性

---

## 3. Spring Boot 基礎

### 3.1 專案結構

#### 3.1.1 標準目錄結構
```
src/
├── main/
│   ├── java/
│   │   └── com/
│   │       └── tutorial/
│   │           ├── SpringBootDemoApplication.java    # 主程式
│   │           ├── controller/                       # 控制層
│   │           ├── service/                         # 服務層
│   │           ├── repository/                      # 資料存取層
│   │           ├── model/                          # 資料模型
│   │           ├── config/                         # 配置類別
│   │           └── dto/                            # 資料傳輸物件
│   └── resources/
│       ├── application.properties                   # 主要配置檔
│       ├── application-dev.properties              # 開發環境配置
│       ├── application-prod.properties             # 生產環境配置
│       ├── static/                                 # 靜態資源
│       └── templates/                              # 範本檔案
└── test/
    └── java/
        └── com/
            └── tutorial/
                ├── SpringBootDemoApplicationTests.java
                ├── controller/                     # 控制層測試
                ├── service/                       # 服務層測試
                └── repository/                    # 資料層測試
```

#### 3.1.2 主程式類別詳解
```java
package com.tutorial;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;

/**
 * Spring Boot 應用程式主程式
 * 
 * @SpringBootApplication 相當於以下三個註解的組合：
 * - @Configuration: 標識為配置類別
 * - @EnableAutoConfiguration: 啟用自動配置
 * - @ComponentScan: 啟用元件掃描
 */
@SpringBootApplication
public class SpringBootDemoApplication {

    public static void main(String[] args) {
        // 啟動 Spring Boot 應用程式
        ConfigurableApplicationContext context = 
            SpringApplication.run(SpringBootDemoApplication.class, args);
        
        // 輸出已載入的 Bean 數量
        System.out.println("已載入的 Bean 數量: " + context.getBeanDefinitionCount());
    }
}
```

#### 3.1.3 自動配置原理
```java
/**
 * 自動配置示例 - 當 H2 資料庫在 classpath 時自動配置
 */
@Configuration
@ConditionalOnClass(H2ConsoleAutoConfiguration.class)
@ConditionalOnProperty(name = "spring.h2.console.enabled", havingValue = "true")
public class H2ConsoleConfiguration {
    
    @Bean
    @ConditionalOnMissingBean
    public H2ConsoleProperties h2ConsoleProperties() {
        return new H2ConsoleProperties();
    }
}
```

### 3.2 Application Properties 設定

#### 3.2.1 基本配置格式
**application.properties 格式**：
```properties
# 應用程式基本資訊
spring.application.name=spring-boot-demo
server.port=8080
server.servlet.context-path=/api

# 資料庫配置
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=password

# JPA 配置
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true

# 日誌配置
logging.level.com.tutorial=DEBUG
logging.pattern.console=%d{yyyy-MM-dd HH:mm:ss} - %msg%n
```

**application.yml 格式**：
```yaml
spring:
  application:
    name: spring-boot-demo
  datasource:
    url: jdbc:h2:mem:testdb
    driver-class-name: org.h2.Driver
    username: sa
    password: password
  jpa:
    database-platform: org.hibernate.dialect.H2Dialect
    hibernate:
      ddl-auto: update
    show-sql: true

server:
  port: 8080
  servlet:
    context-path: /api

logging:
  level:
    com.tutorial: DEBUG
  pattern:
    console: '%d{yyyy-MM-dd HH:mm:ss} - %msg%n'
```

#### 3.2.2 環境專用配置
```yaml
# application.yml (預設配置)
spring:
  profiles:
    active: dev

---
# application-dev.yml (開發環境)
spring:
  config:
    activate:
      on-profile: dev
  datasource:
    url: jdbc:h2:mem:devdb
  jpa:
    show-sql: true
logging:
  level:
    root: DEBUG

---
# application-prod.yml (生產環境)
spring:
  config:
    activate:
      on-profile: prod
  datasource:
    url: jdbc:mysql://localhost:3306/proddb
    username: ${DB_USERNAME}
    password: ${DB_PASSWORD}
  jpa:
    show-sql: false
logging:
  level:
    root: WARN
```

#### 3.2.3 自定義配置屬性
```java
/**
 * 自定義配置屬性類別
 */
@Component
@ConfigurationProperties(prefix = "app")
@Data
public class AppProperties {
    
    private String name;
    private String version;
    private Security security = new Security();
    private List<String> allowedOrigins = new ArrayList<>();
    
    @Data
    public static class Security {
        private boolean enabled = true;
        private int tokenExpiry = 3600;
    }
}
```

```yaml
# 對應的配置
app:
  name: Spring Boot Tutorial
  version: 1.0.0
  security:
    enabled: true
    token-expiry: 7200
  allowed-origins:
    - http://localhost:3000
    - https://app.example.com
```

```java
/**
 * 使用自定義配置
 */
@RestController
public class ConfigController {
    
    @Autowired
    private AppProperties appProperties;
    
    @GetMapping("/config")
    public AppProperties getConfig() {
        return appProperties;
    }
}
```

### 3.3 依賴注入 (Dependency Injection)

#### 3.3.1 註解驅動的依賴注入
```java
/**
 * 服務介面
 */
public interface UserService {
    List<User> findAllUsers();
    User findUserById(Long id);
    User saveUser(User user);
}

/**
 * 服務實作
 */
@Service
public class UserServiceImpl implements UserService {
    
    private final UserRepository userRepository;
    
    // 建構式注入 (推薦方式)
    public UserServiceImpl(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    @Override
    public List<User> findAllUsers() {
        return userRepository.findAll();
    }
    
    @Override
    public User findUserById(Long id) {
        return userRepository.findById(id)
            .orElseThrow(() -> new UserNotFoundException("User not found: " + id));
    }
    
    @Override
    public User saveUser(User user) {
        return userRepository.save(user);
    }
}
```

#### 3.3.2 不同的注入方式
```java
@RestController
@RequestMapping("/users")
public class UserController {
    
    // 1. 建構式注入 (推薦)
    private final UserService userService;
    
    public UserController(UserService userService) {
        this.userService = userService;
    }
    
    // 2. Setter 注入
    private EmailService emailService;
    
    @Autowired
    public void setEmailService(EmailService emailService) {
        this.emailService = emailService;
    }
    
    // 3. 欄位注入 (不推薦)
    @Autowired
    private LoggingService loggingService;
    
    @GetMapping
    public List<User> getAllUsers() {
        return userService.findAllUsers();
    }
}
```

#### 3.3.3 條件式注入
```java
/**
 * 根據條件決定是否建立 Bean
 */
@Configuration
public class ServiceConfiguration {
    
    @Bean
    @ConditionalOnProperty(name = "app.email.enabled", havingValue = "true")
    public EmailService realEmailService() {
        return new SmtpEmailService();
    }
    
    @Bean
    @ConditionalOnMissingBean(EmailService.class)
    public EmailService mockEmailService() {
        return new MockEmailService();
    }
    
    @Bean
    @ConditionalOnClass(RedisTemplate.class)
    public CacheService redisCache() {
        return new RedisCacheService();
    }
    
    @Bean
    @ConditionalOnMissingClass("org.springframework.data.redis.core.RedisTemplate")
    public CacheService memoryCache() {
        return new MemoryCacheService();
    }
}
```

### 3.4 Spring Boot Starter

#### 3.4.1 常用 Starter 依賴
```xml
<!-- Web 開發 -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>

<!-- 資料庫存取 -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>

<!-- 安全性 -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>

<!-- 測試 -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>

<!-- 監控與管理 -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>

<!-- Redis -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
```

#### 3.4.2 自定義 Starter
```java
/**
 * 自定義 Starter 的自動配置類別
 */
@Configuration
@ConditionalOnClass(CustomService.class)
@EnableConfigurationProperties(CustomProperties.class)
public class CustomAutoConfiguration {
    
    @Bean
    @ConditionalOnMissingBean
    public CustomService customService(CustomProperties properties) {
        return new CustomService(properties);
    }
}
```

```java
/**
 * 自定義 Starter 的配置屬性
 */
@ConfigurationProperties(prefix = "custom")
@Data
public class CustomProperties {
    private boolean enabled = true;
    private String apiKey;
    private int timeout = 5000;
}
```

```
# src/main/resources/META-INF/spring.factories
org.springframework.boot.autoconfigure.EnableAutoConfiguration=\
com.tutorial.starter.CustomAutoConfiguration
```

### 3.5 Bean 生命週期與作用域

#### 3.5.1 Bean 生命週期
```java
/**
 * 展示 Bean 生命週期的服務
 */
@Component
public class LifecycleService implements InitializingBean, DisposableBean {
    
    private static final Logger logger = LoggerFactory.getLogger(LifecycleService.class);
    
    public LifecycleService() {
        logger.info("1. LifecycleService 建構子被呼叫");
    }
    
    @PostConstruct
    public void postConstruct() {
        logger.info("2. @PostConstruct 方法被呼叫");
    }
    
    @Override
    public void afterPropertiesSet() throws Exception {
        logger.info("3. InitializingBean.afterPropertiesSet() 被呼叫");
    }
    
    @PreDestroy
    public void preDestroy() {
        logger.info("4. @PreDestroy 方法被呼叫");
    }
    
    @Override
    public void destroy() throws Exception {
        logger.info("5. DisposableBean.destroy() 被呼叫");
    }
}
```

#### 3.5.2 Bean 作用域
```java
/**
 * 不同作用域的 Bean 示例
 */
@Configuration
public class BeanScopeConfiguration {
    
    // 單例模式 (預設)
    @Bean
    @Scope("singleton")
    public SingletonService singletonService() {
        return new SingletonService();
    }
    
    // 原型模式
    @Bean
    @Scope("prototype")
    public PrototypeService prototypeService() {
        return new PrototypeService();
    }
    
    // 請求作用域 (Web 環境)
    @Bean
    @Scope("request")
    public RequestScopedService requestScopedService() {
        return new RequestScopedService();
    }
    
    // 會話作用域 (Web 環境)
    @Bean
    @Scope("session")
    public SessionScopedService sessionScopedService() {
        return new SessionScopedService();
    }
}
```

### 3.6 Profile 環境管理

#### 3.6.1 使用 @Profile 註解
```java
/**
 * 根據 Profile 建立不同的 Bean
 */
@Configuration
public class ProfileConfiguration {
    
    @Bean
    @Profile("dev")
    public DataSource devDataSource() {
        return new HikariDataSource(createDevConfig());
    }
    
    @Bean
    @Profile("prod")
    public DataSource prodDataSource() {
        return new HikariDataSource(createProdConfig());
    }
    
    @Bean
    @Profile("test")
    public DataSource testDataSource() {
        return new HikariDataSource(createTestConfig());
    }
    
    @Bean
    @Profile("!prod")  // 非生產環境
    public DebugService debugService() {
        return new DebugService();
    }
}
```

#### 3.6.2 Profile 啟用方式
```bash
# 1. 命令列參數
java -jar app.jar --spring.profiles.active=prod

# 2. 環境變數
export SPRING_PROFILES_ACTIVE=prod

# 3. JVM 系統屬性
java -Dspring.profiles.active=prod -jar app.jar

# 4. 程式設定
SpringApplication app = new SpringApplication(Application.class);
app.setAdditionalProfiles("prod");
app.run(args);
```

### 3.7 章節小練習

**問題 1**: `@SpringBootApplication` 註解包含了哪三個核心註解？
**答案**: 
1. `@Configuration`
2. `@EnableAutoConfiguration`
3. `@ComponentScan`

**問題 2**: Spring Boot 推薦使用哪種依賴注入方式？為什麼？
**答案**: 建構式注入，因為：
- 保證依賴的不可變性
- 易於進行單元測試
- 避免循環依賴
- 保證必要依賴不為 null

**問題 3**: 完成以下配置類別：
```java
@Configuration
public class DatabaseConfig {
    
    @Bean
    @Profile("______")
    public DataSource devDataSource() {
        // 開發環境資料來源
    }
    
    @Bean
    @Profile("______")
    public DataSource prodDataSource() {
        // 生產環境資料來源
    }
}
```
**答案**: "dev" 和 "prod"

**問題 4**: 以下程式碼的執行順序是什麼？
```java
@Component
public class TestBean implements InitializingBean {
    public TestBean() { /* 建構子 */ }
    
    @PostConstruct
    public void init() { /* 初始化 */ }
    
    @Override
    public void afterPropertiesSet() { /* 屬性設定後 */ }
}
```
**答案**: 建構子 → @PostConstruct → afterPropertiesSet()

### 3.8 實務注意事項

#### ⚠️ 重要提醒
1. **循環依賴**: 避免建構式注入中的循環依賴
2. **Profile 命名**: 使用有意義的 Profile 名稱
3. **配置外部化**: 敏感資訊使用環境變數
4. **Bean 作用域**: 正確選擇 Bean 的作用域

---

## 4. RESTful API 開發

### 4.1 REST 基本概念

#### 4.1.1 REST 架構原則
```
REST (Representational State Transfer) 基本原則：
1. 無狀態 (Stateless)：每個請求都是獨立的
2. 統一介面 (Uniform Interface)：使用標準 HTTP 方法
3. 資源導向 (Resource-Oriented)：以資源為核心
4. 可快取 (Cacheable)：支援快取機制
5. 分層系統 (Layered System)：支援多層架構
```

#### 4.1.2 HTTP 方法對應
| HTTP 方法 | 操作 | 範例 | 冪等性 |
|-----------|------|------|--------|
| GET | 查詢 | GET /users/1 | 是 |
| POST | 建立 | POST /users | 否 |
| PUT | 更新/建立 | PUT /users/1 | 是 |
| PATCH | 部分更新 | PATCH /users/1 | 否 |
| DELETE | 刪除 | DELETE /users/1 | 是 |

#### 4.1.3 HTTP 狀態碼
```java
/**
 * 常用 HTTP 狀態碼
 */
public class HttpStatusCodes {
    // 成功回應
    public static final int OK = 200;              // 成功
    public static final int CREATED = 201;         // 已建立
    public static final int NO_CONTENT = 204;      // 無內容
    
    // 客戶端錯誤
    public static final int BAD_REQUEST = 400;     // 請求錯誤
    public static final int UNAUTHORIZED = 401;    // 未授權
    public static final int FORBIDDEN = 403;       // 禁止存取
    public static final int NOT_FOUND = 404;       // 找不到資源
    public static final int CONFLICT = 409;        // 衝突
    
    // 伺服器錯誤
    public static final int INTERNAL_SERVER_ERROR = 500;  // 內部伺服器錯誤
}
```

### 4.2 Controller 層開發

#### 4.2.1 基本 Controller 結構
```java
package com.tutorial.controller;

import com.tutorial.model.User;
import com.tutorial.service.UserService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;

/**
 * 使用者管理 API 控制器
 * 
 * @author Tutorial Team
 */
@RestController
@RequestMapping("/api/users")
@CrossOrigin(origins = "*")
public class UserController {

    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    /**
     * 查詢所有使用者
     * GET /api/users
     */
    @GetMapping
    public ResponseEntity<List<User>> getAllUsers() {
        List<User> users = userService.findAllUsers();
        return ResponseEntity.ok(users);
    }

    /**
     * 根據 ID 查詢使用者
     * GET /api/users/{id}
     */
    @GetMapping("/{id}")
    public ResponseEntity<User> getUserById(@PathVariable Long id) {
        User user = userService.findUserById(id);
        return ResponseEntity.ok(user);
    }

    /**
     * 建立新使用者
     * POST /api/users
     */
    @PostMapping
    public ResponseEntity<User> createUser(@Valid @RequestBody User user) {
        User savedUser = userService.saveUser(user);
        return ResponseEntity.status(HttpStatus.CREATED).body(savedUser);
    }

    /**
     * 更新使用者資訊
     * PUT /api/users/{id}
     */
    @PutMapping("/{id}")
    public ResponseEntity<User> updateUser(@PathVariable Long id, 
                                         @Valid @RequestBody User user) {
        user.setId(id);
        User updatedUser = userService.updateUser(user);
        return ResponseEntity.ok(updatedUser);
    }

    /**
     * 部分更新使用者資訊
     * PATCH /api/users/{id}
     */
    @PatchMapping("/{id}")
    public ResponseEntity<User> patchUser(@PathVariable Long id, 
                                        @RequestBody User userPatch) {
        User updatedUser = userService.patchUser(id, userPatch);
        return ResponseEntity.ok(updatedUser);
    }

    /**
     * 刪除使用者
     * DELETE /api/users/{id}
     */
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
        return ResponseEntity.noContent().build();
    }
}
```

#### 4.2.2 請求參數處理
```java
/**
 * 展示各種請求參數處理方式
 */
@RestController
@RequestMapping("/api/search")
public class SearchController {

    /**
     * 查詢參數 (Query Parameters)
     * GET /api/search/users?name=John&age=25&active=true
     */
    @GetMapping("/users")
    public ResponseEntity<List<User>> searchUsers(
            @RequestParam(required = false) String name,
            @RequestParam(required = false) Integer age,
            @RequestParam(defaultValue = "true") Boolean active,
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size) {
        
        SearchCriteria criteria = SearchCriteria.builder()
            .name(name)
            .age(age)
            .active(active)
            .page(page)
            .size(size)
            .build();
            
        List<User> users = userService.searchUsers(criteria);
        return ResponseEntity.ok(users);
    }

    /**
     * 路徑變數 (Path Variables)
     * GET /api/search/users/department/IT/role/ADMIN
     */
    @GetMapping("/users/department/{dept}/role/{role}")
    public ResponseEntity<List<User>> getUsersByDeptAndRole(
            @PathVariable("dept") String department,
            @PathVariable String role) {
        
        List<User> users = userService.findByDepartmentAndRole(department, role);
        return ResponseEntity.ok(users);
    }

    /**
     * 請求標頭 (Request Headers)
     */
    @GetMapping("/profile")
    public ResponseEntity<User> getUserProfile(
            @RequestHeader("Authorization") String token,
            @RequestHeader(value = "X-Client-Version", defaultValue = "1.0") String clientVersion) {
        
        String userId = jwtService.extractUserId(token);
        User user = userService.findUserById(Long.valueOf(userId));
        return ResponseEntity.ok(user);
    }

    /**
     * 多值參數處理
     * GET /api/search/users?skills=Java&skills=Spring&skills=Docker
     */
    @GetMapping("/by-skills")
    public ResponseEntity<List<User>> getUsersBySkills(
            @RequestParam List<String> skills) {
        
        List<User> users = userService.findBySkillsIn(skills);
        return ResponseEntity.ok(users);
    }
}
```

#### 4.2.3 回應處理
```java
/**
 * 回應處理示例
 */
@RestController
@RequestMapping("/api/files")
public class FileController {

    /**
     * 檔案上傳
     */
    @PostMapping("/upload")
    public ResponseEntity<FileUploadResponse> uploadFile(
            @RequestParam("file") MultipartFile file) {
        
        String fileName = fileService.storeFile(file);
        
        FileUploadResponse response = FileUploadResponse.builder()
            .fileName(fileName)
            .fileSize(file.getSize())
            .contentType(file.getContentType())
            .uploadTime(LocalDateTime.now())
            .build();
            
        return ResponseEntity.status(HttpStatus.CREATED).body(response);
    }

    /**
     * 檔案下載
     */
    @GetMapping("/download/{fileName}")
    public ResponseEntity<Resource> downloadFile(@PathVariable String fileName) {
        
        Resource resource = fileService.loadFileAsResource(fileName);
        
        return ResponseEntity.ok()
            .contentType(MediaType.parseMediaType("application/octet-stream"))
            .header(HttpHeaders.CONTENT_DISPOSITION, 
                    "attachment; filename=\"" + resource.getFilename() + "\"")
            .body(resource);
    }

    /**
     * 自定義回應標頭
     */
    @GetMapping("/info/{id}")
    public ResponseEntity<FileInfo> getFileInfo(@PathVariable String id) {
        
        FileInfo fileInfo = fileService.getFileInfo(id);
        
        return ResponseEntity.ok()
            .header("X-File-Version", fileInfo.getVersion())
            .header("X-Last-Modified", fileInfo.getLastModified().toString())
            .cacheControl(CacheControl.maxAge(Duration.ofHours(1)))
            .body(fileInfo);
    }
}
```

### 4.3 Service 層開發

#### 4.3.1 Service 層架構
```java
/**
 * 使用者服務介面
 */
public interface UserService {
    List<User> findAllUsers();
    User findUserById(Long id);
    User saveUser(User user);
    User updateUser(User user);
    User patchUser(Long id, User userPatch);
    void deleteUser(Long id);
    List<User> searchUsers(SearchCriteria criteria);
    boolean existsByEmail(String email);
}

/**
 * 使用者服務實作
 */
@Service
@Transactional
public class UserServiceImpl implements UserService {

    private static final Logger logger = LoggerFactory.getLogger(UserServiceImpl.class);

    private final UserRepository userRepository;
    private final EmailService emailService;

    public UserServiceImpl(UserRepository userRepository, EmailService emailService) {
        this.userRepository = userRepository;
        this.emailService = emailService;
    }

    @Override
    @Transactional(readOnly = true)
    public List<User> findAllUsers() {
        logger.debug("正在查詢所有使用者");
        return userRepository.findAll();
    }

    @Override
    @Transactional(readOnly = true)
    public User findUserById(Long id) {
        logger.debug("正在查詢使用者，ID: {}", id);
        return userRepository.findById(id)
            .orElseThrow(() -> new UserNotFoundException("找不到使用者，ID: " + id));
    }

    @Override
    public User saveUser(User user) {
        logger.info("正在建立新使用者: {}", user.getEmail());
        
        // 驗證 Email 是否已存在
        if (existsByEmail(user.getEmail())) {
            throw new DuplicateEmailException("Email 已存在: " + user.getEmail());
        }
        
        // 設定預設值
        user.setCreatedAt(LocalDateTime.now());
        user.setActive(true);
        
        User savedUser = userRepository.save(user);
        
        // 發送歡迎郵件
        emailService.sendWelcomeEmail(savedUser);
        
        logger.info("使用者建立成功，ID: {}", savedUser.getId());
        return savedUser;
    }

    @Override
    public User updateUser(User user) {
        logger.info("正在更新使用者，ID: {}", user.getId());
        
        User existingUser = findUserById(user.getId());
        
        // 更新欄位
        existingUser.setName(user.getName());
        existingUser.setEmail(user.getEmail());
        existingUser.setDepartment(user.getDepartment());
        existingUser.setUpdatedAt(LocalDateTime.now());
        
        return userRepository.save(existingUser);
    }

    @Override
    public User patchUser(Long id, User userPatch) {
        logger.info("正在部分更新使用者，ID: {}", id);
        
        User existingUser = findUserById(id);
        
        // 只更新非空值
        if (userPatch.getName() != null) {
            existingUser.setName(userPatch.getName());
        }
        if (userPatch.getEmail() != null) {
            existingUser.setEmail(userPatch.getEmail());
        }
        if (userPatch.getDepartment() != null) {
            existingUser.setDepartment(userPatch.getDepartment());
        }
        
        existingUser.setUpdatedAt(LocalDateTime.now());
        
        return userRepository.save(existingUser);
    }

    @Override
    public void deleteUser(Long id) {
        logger.info("正在刪除使用者，ID: {}", id);
        
        User user = findUserById(id);
        userRepository.delete(user);
        
        logger.info("使用者刪除成功，ID: {}", id);
    }

    @Override
    @Transactional(readOnly = true)
    public boolean existsByEmail(String email) {
        return userRepository.existsByEmail(email);
    }
}
```

#### 4.3.2 業務邏輯封裝
```java
/**
 * 訂單服務 - 展示複雜業務邏輯處理
 */
@Service
@Transactional
public class OrderService {

    private final OrderRepository orderRepository;
    private final ProductService productService;
    private final InventoryService inventoryService;
    private final PaymentService paymentService;
    private final NotificationService notificationService;

    public OrderService(OrderRepository orderRepository,
                       ProductService productService,
                       InventoryService inventoryService,
                       PaymentService paymentService,
                       NotificationService notificationService) {
        this.orderRepository = orderRepository;
        this.productService = productService;
        this.inventoryService = inventoryService;
        this.paymentService = paymentService;
        this.notificationService = notificationService;
    }

    /**
     * 建立訂單 - 包含複雜業務邏輯
     */
    public Order createOrder(CreateOrderRequest request) {
        // 1. 驗證產品存在性和價格
        List<OrderItem> orderItems = validateAndCalculateOrderItems(request.getItems());
        
        // 2. 檢查庫存
        validateInventory(orderItems);
        
        // 3. 計算總金額
        BigDecimal totalAmount = calculateTotalAmount(orderItems);
        
        // 4. 建立訂單
        Order order = Order.builder()
            .userId(request.getUserId())
            .orderItems(orderItems)
            .totalAmount(totalAmount)
            .status(OrderStatus.PENDING)
            .createdAt(LocalDateTime.now())
            .build();
        
        // 5. 保存訂單
        Order savedOrder = orderRepository.save(order);
        
        // 6. 扣減庫存
        inventoryService.reserveInventory(orderItems);
        
        // 7. 發送通知
        notificationService.sendOrderCreatedNotification(savedOrder);
        
        return savedOrder;
    }

    /**
     * 處理付款
     */
    public Order processPayment(Long orderId, PaymentRequest paymentRequest) {
        Order order = findOrderById(orderId);
        
        // 驗證訂單狀態
        if (order.getStatus() != OrderStatus.PENDING) {
            throw new InvalidOrderStatusException("訂單狀態不允許付款: " + order.getStatus());
        }
        
        try {
            // 處理付款
            PaymentResult paymentResult = paymentService.processPayment(
                order.getTotalAmount(), paymentRequest);
            
            // 更新訂單狀態
            order.setStatus(OrderStatus.PAID);
            order.setPaymentId(paymentResult.getPaymentId());
            order.setPaidAt(LocalDateTime.now());
            
            Order savedOrder = orderRepository.save(order);
            
            // 發送付款成功通知
            notificationService.sendPaymentSuccessNotification(savedOrder);
            
            return savedOrder;
            
        } catch (PaymentException e) {
            // 付款失敗，釋放庫存
            inventoryService.releaseInventory(order.getOrderItems());
            
            order.setStatus(OrderStatus.PAYMENT_FAILED);
            orderRepository.save(order);
            
            throw new OrderPaymentException("付款失敗: " + e.getMessage(), e);
        }
    }

    private List<OrderItem> validateAndCalculateOrderItems(List<CreateOrderItemRequest> items) {
        return items.stream()
            .map(item -> {
                Product product = productService.findById(item.getProductId());
                return OrderItem.builder()
                    .productId(product.getId())
                    .productName(product.getName())
                    .quantity(item.getQuantity())
                    .unitPrice(product.getPrice())
                    .totalPrice(product.getPrice().multiply(BigDecimal.valueOf(item.getQuantity())))
                    .build();
            })
            .collect(Collectors.toList());
    }
}
```

### 4.4 Repository 層開發

#### 4.4.1 基本 Repository
```java
/**
 * 使用者資料存取介面
 */
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    
    // 基本查詢方法
    Optional<User> findByEmail(String email);
    boolean existsByEmail(String email);
    List<User> findByActiveTrue();
    List<User> findByDepartment(String department);
    
    // 複合查詢
    List<User> findByDepartmentAndActiveTrue(String department);
    List<User> findByNameContainingIgnoreCase(String name);
    
    // 分頁查詢
    Page<User> findByDepartment(String department, Pageable pageable);
    
    // 自定義查詢 - JPQL
    @Query("SELECT u FROM User u WHERE u.createdAt >= :startDate")
    List<User> findUsersCreatedAfter(@Param("startDate") LocalDateTime startDate);
    
    @Query("SELECT u FROM User u WHERE u.department = :dept AND u.active = true ORDER BY u.createdAt DESC")
    List<User> findActiveUsersByDepartmentOrderByCreatedAtDesc(@Param("dept") String department);
    
    // 自定義查詢 - Native SQL
    @Query(value = "SELECT * FROM users u WHERE u.last_login < ?1", nativeQuery = true)
    List<User> findInactiveUsers(LocalDateTime cutoffDate);
    
    // 更新操作
    @Modifying
    @Query("UPDATE User u SET u.active = false WHERE u.lastLogin < :cutoffDate")
    int deactivateInactiveUsers(@Param("cutoffDate") LocalDateTime cutoffDate);
    
    // 統計查詢
    @Query("SELECT u.department, COUNT(u) FROM User u GROUP BY u.department")
    List<Object[]> countUsersByDepartment();
    
    @Query("SELECT COUNT(u) FROM User u WHERE u.active = true")
    long countActiveUsers();
}
```

#### 4.4.2 複雜查詢與動態查詢
```java
/**
 * 自定義 Repository 實作
 */
public interface UserRepositoryCustom {
    List<User> findUsersByCriteria(UserSearchCriteria criteria);
    Page<User> findUsersByCriteriaWithPaging(UserSearchCriteria criteria, Pageable pageable);
}

/**
 * 使用 JPA Criteria API 實作動態查詢
 */
@Repository
public class UserRepositoryCustomImpl implements UserRepositoryCustom {

    @PersistenceContext
    private EntityManager entityManager;

    @Override
    public List<User> findUsersByCriteria(UserSearchCriteria criteria) {
        CriteriaBuilder cb = entityManager.getCriteriaBuilder();
        CriteriaQuery<User> query = cb.createQuery(User.class);
        Root<User> user = query.from(User.class);

        List<Predicate> predicates = new ArrayList<>();

        // 動態添加查詢條件
        if (criteria.getName() != null && !criteria.getName().isEmpty()) {
            predicates.add(cb.like(cb.lower(user.get("name")), 
                "%" + criteria.getName().toLowerCase() + "%"));
        }

        if (criteria.getEmail() != null && !criteria.getEmail().isEmpty()) {
            predicates.add(cb.equal(user.get("email"), criteria.getEmail()));
        }

        if (criteria.getDepartment() != null && !criteria.getDepartment().isEmpty()) {
            predicates.add(cb.equal(user.get("department"), criteria.getDepartment()));
        }

        if (criteria.getActive() != null) {
            predicates.add(cb.equal(user.get("active"), criteria.getActive()));
        }

        if (criteria.getCreatedAfter() != null) {
            predicates.add(cb.greaterThanOrEqualTo(user.get("createdAt"), criteria.getCreatedAfter()));
        }

        if (criteria.getCreatedBefore() != null) {
            predicates.add(cb.lessThanOrEqualTo(user.get("createdAt"), criteria.getCreatedBefore()));
        }

        // 組合查詢條件
        query.where(predicates.toArray(new Predicate[0]));
        
        // 添加排序
        if (criteria.getSortBy() != null) {
            if ("desc".equalsIgnoreCase(criteria.getSortDirection())) {
                query.orderBy(cb.desc(user.get(criteria.getSortBy())));
            } else {
                query.orderBy(cb.asc(user.get(criteria.getSortBy())));
            }
        }

        return entityManager.createQuery(query).getResultList();
    }

    @Override
    public Page<User> findUsersByCriteriaWithPaging(UserSearchCriteria criteria, Pageable pageable) {
        // 查詢總數
        long total = countUsersByCriteria(criteria);
        
        // 查詢資料
        List<User> users = findUsersByCriteriaWithPaging(criteria, pageable);
        
        return new PageImpl<>(users, pageable, total);
    }

    private long countUsersByCriteria(UserSearchCriteria criteria) {
        CriteriaBuilder cb = entityManager.getCriteriaBuilder();
        CriteriaQuery<Long> query = cb.createQuery(Long.class);
        Root<User> user = query.from(User.class);

        // ... 同樣的查詢條件邏輯
        
        query.select(cb.count(user));
        return entityManager.createQuery(query).getSingleResult();
    }
}
```

#### 4.4.3 Repository 最佳實務
```java
/**
 * Repository 最佳實務示例
 */
@Repository
public interface ProductRepository extends JpaRepository<Product, Long> {
    
    // 1. 使用 Optional 避免 null
    Optional<Product> findByCode(String code);
    
    // 2. 使用具體的回傳類型
    List<Product> findTop10ByOrderByCreatedAtDesc();
    
    // 3. 使用投影減少資料傳輸
    @Query("SELECT new com.tutorial.dto.ProductSummary(p.id, p.name, p.price) FROM Product p")
    List<ProductSummary> findAllProductSummaries();
    
    // 4. 使用 Stream 處理大量資料
    @Query("SELECT p FROM Product p WHERE p.category = :category")
    Stream<Product> findByCategory(@Param("category") String category);
    
    // 5. 使用批次操作提升效能
    @Modifying
    @Query("UPDATE Product p SET p.price = p.price * 1.1 WHERE p.category = :category")
    int increasePriceByCategory(@Param("category") String category);
    
    // 6. 使用命名查詢
    @NamedQuery(
        name = "Product.findExpensiveProducts",
        query = "SELECT p FROM Product p WHERE p.price > :threshold ORDER BY p.price DESC"
    )
    List<Product> findExpensiveProducts(@Param("threshold") BigDecimal threshold);
}
```

### 4.5 章節小練習

**問題 1**: REST API 中，哪個 HTTP 方法是冪等的？
A) POST B) GET C) DELETE D) B 和 C

**答案**: D) B 和 C (GET 和 DELETE 都是冪等的)

**問題 2**: 完成以下 Controller 方法：
```java
@RestController
@RequestMapping("/api/books")
public class BookController {
    
    @______("/search")
    public ResponseEntity<List<Book>> searchBooks(
            @______ String title,
            @______ String author) {
        // 實作查詢邏輯
    }
}
```
**答案**: `@GetMapping` 和 `@RequestParam`

**問題 3**: 以下哪個註解用於處理 HTTP POST 請求？
A) @PostMapping B) @RequestMapping(method = RequestMethod.POST) 
C) 兩者都可以 D) 都不對

**答案**: C) 兩者都可以

**問題 4**: 在 Repository 中，如何實現根據名稱模糊查詢？
**答案**: 
```java
List<User> findByNameContainingIgnoreCase(String name);
// 或
@Query("SELECT u FROM User u WHERE LOWER(u.name) LIKE LOWER(CONCAT('%', :name, '%'))")
List<User> findByNameLike(@Param("name") String name);
```

### 4.6 實務注意事項

#### ⚠️ 重要提醒
1. **HTTP 狀態碼**: 正確使用 HTTP 狀態碼表達操作結果
2. **異常處理**: 提供統一的錯誤回應格式
3. **驗證**: 對輸入資料進行完整驗證
4. **分頁**: 大量資料查詢務必實現分頁機制

---

## 5. 與資料庫整合

### 5.1 JPA 基礎配置

#### 5.1.1 依賴配置
```xml
<!-- pom.xml -->
<dependencies>
    <!-- Spring Boot Data JPA Starter -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>
    
    <!-- H2 Database (開發測試用) -->
    <dependency>
        <groupId>com.h2database</groupId>
        <artifactId>h2</artifactId>
        <scope>runtime</scope>
    </dependency>
    
    <!-- MySQL Driver (生產環境用) -->
    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <scope>runtime</scope>
    </dependency>
    
    <!-- PostgreSQL Driver (替代選擇) -->
    <dependency>
        <groupId>org.postgresql</groupId>
        <artifactId>postgresql</artifactId>
        <scope>runtime</scope>
    </dependency>
</dependencies>
```

#### 5.1.2 資料庫連線配置
```yaml
# application.yml
spring:
  # H2 資料庫配置 (開發環境)
  datasource:
    url: jdbc:h2:mem:testdb
    driver-class-name: org.h2.Driver
    username: sa
    password: password
  
  # H2 控制台啟用
  h2:
    console:
      enabled: true
      path: /h2-console
  
  # JPA 配置
  jpa:
    database-platform: org.hibernate.dialect.H2Dialect
    hibernate:
      ddl-auto: create-drop  # 開發環境用，生產環境改為 validate
    show-sql: true
    format-sql: true
    properties:
      hibernate:
        generate_statistics: true
        use_sql_comments: true

---
# 生產環境配置
spring:
  config:
    activate:
      on-profile: prod
  datasource:
    url: jdbc:mysql://localhost:3306/springboot_tutorial?useSSL=false&serverTimezone=UTC
    driver-class-name: com.mysql.cj.jdbc.Driver
    username: ${DB_USERNAME}
    password: ${DB_PASSWORD}
    hikari:
      maximum-pool-size: 20
      minimum-idle: 5
      connection-timeout: 20000
      idle-timeout: 300000
      max-lifetime: 1200000
  
  jpa:
    database-platform: org.hibernate.dialect.MySQL8Dialect
    hibernate:
      ddl-auto: validate
    show-sql: false
```

### 5.2 實體類別設計

#### 5.2.1 基本實體類別
```java
package com.tutorial.model;

import jakarta.persistence.*;
import jakarta.validation.constraints.*;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;
import lombok.Builder;

import java.time.LocalDateTime;

/**
 * 使用者實體類別
 */
@Entity
@Table(name = "users", 
       indexes = {
           @Index(name = "idx_email", columnList = "email"),
           @Index(name = "idx_department", columnList = "department")
       })
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name", nullable = false, length = 100)
    @NotBlank(message = "姓名不能為空")
    @Size(min = 2, max = 100, message = "姓名長度必須在 2-100 字元之間")
    private String name;

    @Column(name = "email", nullable = false, unique = true, length = 255)
    @NotBlank(message = "Email 不能為空")
    @Email(message = "Email 格式不正確")
    private String email;

    @Column(name = "department", length = 50)
    private String department;

    @Column(name = "phone", length = 20)
    @Pattern(regexp = "^[0-9-+()\\s]*$", message = "電話號碼格式不正確")
    private String phone;

    @Column(name = "active")
    @Builder.Default
    private Boolean active = true;

    @Column(name = "created_at", nullable = false, updatable = false)
    @Builder.Default
    private LocalDateTime createdAt = LocalDateTime.now();

    @Column(name = "updated_at")
    private LocalDateTime updatedAt;

    @Column(name = "last_login")
    private LocalDateTime lastLogin;

    @PreUpdate
    protected void onUpdate() {
        updatedAt = LocalDateTime.now();
    }
}
```

#### 5.2.2 實體關係對應
```java
/**
 * 部門實體
 */
@Entity
@Table(name = "departments")
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Department {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name", nullable = false, unique = true)
    private String name;

    @Column(name = "description")
    private String description;

    // 一對多關係：一個部門有多個使用者
    @OneToMany(mappedBy = "department", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private List<User> users = new ArrayList<>();

    @Column(name = "created_at")
    @Builder.Default
    private LocalDateTime createdAt = LocalDateTime.now();
}

/**
 * 更新的使用者實體 (包含部門關係)
 */
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

    // ... 其他欄位

    // 多對一關係：多個使用者屬於一個部門
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "department_id")
    private Department department;

    // 多對多關係：使用者可以有多個角色
    @ManyToMany(fetch = FetchType.LAZY)
    @JoinTable(
        name = "user_roles",
        joinColumns = @JoinColumn(name = "user_id"),
        inverseJoinColumns = @JoinColumn(name = "role_id")
    )
    private Set<Role> roles = new HashSet<>();

    // 一對一關係：使用者詳細資料
    @OneToOne(mappedBy = "user", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private UserProfile profile;
}

/**
 * 角色實體
 */
@Entity
@Table(name = "roles")
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Role {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name", nullable = false, unique = true)
    @Enumerated(EnumType.STRING)
    private RoleName name;

    @Column(name = "description")
    private String description;

    @ManyToMany(mappedBy = "roles")
    private Set<User> users = new HashSet<>();
}

/**
 * 使用者詳細資料實體
 */
@Entity
@Table(name = "user_profiles")
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class UserProfile {

    @Id
    private Long id;

    @OneToOne(fetch = FetchType.LAZY)
    @MapsId
    @JoinColumn(name = "user_id")
    private User user;

    @Column(name = "avatar_url")
    private String avatarUrl;

    @Column(name = "bio", columnDefinition = "TEXT")
    private String bio;

    @Column(name = "birth_date")
    private LocalDate birthDate;

    @Column(name = "address")
    private String address;
}
```

#### 5.2.3 繼承對應策略
```java
/**
 * 基礎實體類別 - 包含共同欄位
 */
@MappedSuperclass
@Data
public abstract class BaseEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;

    @Column(name = "updated_at")
    private LocalDateTime updatedAt;

    @Column(name = "created_by")
    private String createdBy;

    @Column(name = "updated_by")
    private String updatedBy;

    @PrePersist
    protected void onCreate() {
        createdAt = LocalDateTime.now();
        // 從安全上下文獲取當前使用者
        createdBy = getCurrentUser();
    }

    @PreUpdate
    protected void onUpdate() {
        updatedAt = LocalDateTime.now();
        updatedBy = getCurrentUser();
    }

    private String getCurrentUser() {
        // 實際專案中從 Spring Security 獲取
        return "system";
    }
}

/**
 * 繼承基礎實體的產品類別
 */
@Entity
@Table(name = "products")
@Data
@EqualsAndHashCode(callSuper = true)
public class Product extends BaseEntity {

    @Column(name = "name", nullable = false)
    private String name;

    @Column(name = "code", nullable = false, unique = true)
    private String code;

    @Column(name = "price", precision = 10, scale = 2)
    private BigDecimal price;

    @Column(name = "description", columnDefinition = "TEXT")
    private String description;

    @Enumerated(EnumType.STRING)
    @Column(name = "status")
    private ProductStatus status;
}
```

### 5.3 Repository 層進階應用

#### 5.3.1 自定義查詢方法
```java
/**
 * 使用者 Repository 進階範例
 */
@Repository
public interface UserRepository extends JpaRepository<User, Long>, UserRepositoryCustom {

    // 基本查詢方法
    Optional<User> findByEmail(String email);
    List<User> findByActiveTrue();
    
    // 關聯查詢
    List<User> findByDepartmentName(String departmentName);
    List<User> findByRolesName(RoleName roleName);
    
    // 複合條件查詢
    List<User> findByDepartmentNameAndActiveTrue(String departmentName);
    
    // 分頁和排序
    Page<User> findByDepartmentName(String departmentName, Pageable pageable);
    
    // 投影查詢 - 只查詢需要的欄位
    @Query("SELECT new com.tutorial.dto.UserSummaryDto(u.id, u.name, u.email, d.name) " +
           "FROM User u LEFT JOIN u.department d")
    List<UserSummaryDto> findAllUserSummaries();
    
    // 聚合查詢
    @Query("SELECT d.name, COUNT(u) FROM User u JOIN u.department d GROUP BY d.name")
    List<Object[]> countUsersByDepartment();
    
    // 子查詢
    @Query("SELECT u FROM User u WHERE u.id IN " +
           "(SELECT ur.user.id FROM UserRole ur WHERE ur.role.name = :roleName)")
    List<User> findUsersWithRole(@Param("roleName") RoleName roleName);
    
    // 原生 SQL 查詢
    @Query(value = "SELECT * FROM users u WHERE u.last_login < DATE_SUB(NOW(), INTERVAL :days DAY)", 
           nativeQuery = true)
    List<User> findInactiveUsers(@Param("days") int days);
    
    // 批次更新
    @Modifying
    @Transactional
    @Query("UPDATE User u SET u.lastLogin = :loginTime WHERE u.id = :userId")
    int updateLastLogin(@Param("userId") Long userId, @Param("loginTime") LocalDateTime loginTime);
    
    // 批次刪除
    @Modifying
    @Transactional
    @Query("DELETE FROM User u WHERE u.active = false AND u.updatedAt < :cutoffDate")
    int deleteInactiveUsers(@Param("cutoffDate") LocalDateTime cutoffDate);
}
```

#### 5.3.2 Specification 動態查詢
```java
/**
 * 使用 JPA Specification 實現動態查詢
 */
@Repository
public interface UserRepository extends JpaRepository<User, Long>, JpaSpecificationExecutor<User> {
    // 其他方法...
}

/**
 * 使用者查詢規範工廠
 */
public class UserSpecifications {

    public static Specification<User> hasName(String name) {
        return (root, query, criteriaBuilder) -> {
            if (name == null || name.isEmpty()) {
                return criteriaBuilder.conjunction();
            }
            return criteriaBuilder.like(
                criteriaBuilder.lower(root.get("name")), 
                "%" + name.toLowerCase() + "%"
            );
        };
    }

    public static Specification<User> hasEmail(String email) {
        return (root, query, criteriaBuilder) -> {
            if (email == null || email.isEmpty()) {
                return criteriaBuilder.conjunction();
            }
            return criteriaBuilder.equal(root.get("email"), email);
        };
    }

    public static Specification<User> belongsToDepartment(String departmentName) {
        return (root, query, criteriaBuilder) -> {
            if (departmentName == null || departmentName.isEmpty()) {
                return criteriaBuilder.conjunction();
            }
            return criteriaBuilder.equal(root.get("department").get("name"), departmentName);
        };
    }

    public static Specification<User> isActive(Boolean active) {
        return (root, query, criteriaBuilder) -> {
            if (active == null) {
                return criteriaBuilder.conjunction();
            }
            return criteriaBuilder.equal(root.get("active"), active);
        };
    }

    public static Specification<User> createdAfter(LocalDateTime date) {
        return (root, query, criteriaBuilder) -> {
            if (date == null) {
                return criteriaBuilder.conjunction();
            }
            return criteriaBuilder.greaterThanOrEqualTo(root.get("createdAt"), date);
        };
    }

    public static Specification<User> hasRole(RoleName roleName) {
        return (root, query, criteriaBuilder) -> {
            if (roleName == null) {
                return criteriaBuilder.conjunction();
            }
            return criteriaBuilder.isMember(roleName, root.get("roles"));
        };
    }
}

/**
 * 使用 Specification 的服務範例
 */
@Service
@Transactional
public class UserSearchService {

    private final UserRepository userRepository;

    public UserSearchService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public Page<User> searchUsers(UserSearchCriteria criteria, Pageable pageable) {
        Specification<User> spec = Specification.where(null);

        spec = spec.and(UserSpecifications.hasName(criteria.getName()))
                  .and(UserSpecifications.hasEmail(criteria.getEmail()))
                  .and(UserSpecifications.belongsToDepartment(criteria.getDepartmentName()))
                  .and(UserSpecifications.isActive(criteria.getActive()))
                  .and(UserSpecifications.createdAfter(criteria.getCreatedAfter()))
                  .and(UserSpecifications.hasRole(criteria.getRole()));

        return userRepository.findAll(spec, pageable);
    }
}
```

### 5.4 事務管理

#### 5.4.1 聲明式事務
```java
/**
 * 事務管理範例
 */
@Service
@Transactional
public class UserManagementService {

    private final UserRepository userRepository;
    private final DepartmentRepository departmentRepository;
    private final EmailService emailService;
    private final AuditService auditService;

    public UserManagementService(UserRepository userRepository,
                               DepartmentRepository departmentRepository,
                               EmailService emailService,
                               AuditService auditService) {
        this.userRepository = userRepository;
        this.departmentRepository = departmentRepository;
        this.emailService = emailService;
        this.auditService = auditService;
    }

    /**
     * 建立使用者 - 預設事務設定
     */
    public User createUser(CreateUserRequest request) {
        // 驗證部門存在
        Department department = departmentRepository.findByName(request.getDepartmentName())
            .orElseThrow(() -> new DepartmentNotFoundException("部門不存在: " + request.getDepartmentName()));

        // 建立使用者
        User user = User.builder()
            .name(request.getName())
            .email(request.getEmail())
            .department(department)
            .active(true)
            .createdAt(LocalDateTime.now())
            .build();

        User savedUser = userRepository.save(user);

        // 發送歡迎郵件 (如果失敗，整個事務會回滾)
        emailService.sendWelcomeEmail(savedUser);

        // 記錄審計日誌
        auditService.logUserCreation(savedUser);

        return savedUser;
    }

    /**
     * 唯讀事務 - 提升效能
     */
    @Transactional(readOnly = true)
    public List<User> findAllActiveUsers() {
        return userRepository.findByActiveTrue();
    }

    /**
     * 指定事務傳播行為
     */
    @Transactional(propagation = Propagation.REQUIRES_NEW)
    public void logUserActivity(Long userId, String activity) {
        // 此方法總是在新事務中執行
        auditService.logActivity(userId, activity);
    }

    /**
     * 指定異常回滾規則
     */
    @Transactional(rollbackFor = {Exception.class}, noRollbackFor = {EmailException.class})
    public User updateUser(Long id, UpdateUserRequest request) {
        User user = userRepository.findById(id)
            .orElseThrow(() -> new UserNotFoundException("使用者不存在: " + id));

        user.setName(request.getName());
        user.setEmail(request.getEmail());
        user.setUpdatedAt(LocalDateTime.now());

        User savedUser = userRepository.save(user);

        try {
            // 即使郵件發送失敗，使用者更新也不會回滾
            emailService.sendUpdateNotification(savedUser);
        } catch (EmailException e) {
            // 記錄錯誤但不影響主要操作
            log.warn("郵件發送失敗: {}", e.getMessage());
        }

        return savedUser;
    }

    /**
     * 手動事務控制
     */
    @Transactional
    public void batchUpdateUsers(List<UpdateUserRequest> requests) {
        for (UpdateUserRequest request : requests) {
            try {
                updateUser(request.getId(), request);
            } catch (Exception e) {
                // 記錄錯誤但繼續處理其他使用者
                log.error("更新使用者失敗: {}", request.getId(), e);
            }
        }
    }
}
```

#### 5.4.2 程式化事務
```java
/**
 * 程式化事務管理範例
 */
@Service
public class UserBatchService {

    private final PlatformTransactionManager transactionManager;
    private final TransactionTemplate transactionTemplate;
    private final UserRepository userRepository;

    public UserBatchService(PlatformTransactionManager transactionManager,
                          UserRepository userRepository) {
        this.transactionManager = transactionManager;
        this.transactionTemplate = new TransactionTemplate(transactionManager);
        this.userRepository = userRepository;
    }

    /**
     * 使用 TransactionTemplate
     */
    public void batchCreateUsers(List<CreateUserRequest> requests) {
        transactionTemplate.execute(new TransactionCallbackWithoutResult() {
            @Override
            protected void doInTransactionWithoutResult(TransactionStatus status) {
                try {
                    for (CreateUserRequest request : requests) {
                        User user = User.builder()
                            .name(request.getName())
                            .email(request.getEmail())
                            .active(true)
                            .createdAt(LocalDateTime.now())
                            .build();
                        userRepository.save(user);
                    }
                } catch (Exception e) {
                    status.setRollbackOnly();
                    throw new BatchProcessException("批次建立使用者失敗", e);
                }
            }
        });
    }

    /**
     * 使用 PlatformTransactionManager
     */
    public void importUsersFromFile(String filePath) {
        TransactionDefinition def = new DefaultTransactionDefinition();
        TransactionStatus status = transactionManager.getTransaction(def);

        try {
            List<String> lines = Files.readAllLines(Paths.get(filePath));
            
            for (String line : lines) {
                String[] parts = line.split(",");
                User user = User.builder()
                    .name(parts[0])
                    .email(parts[1])
                    .active(true)
                    .createdAt(LocalDateTime.now())
                    .build();
                userRepository.save(user);
            }

            transactionManager.commit(status);
        } catch (Exception e) {
            transactionManager.rollback(status);
            throw new FileImportException("檔案匯入失敗", e);
        }
    }
}
```

### 5.5 資料庫連線池配置

#### 5.5.1 HikariCP 配置
```yaml
# application.yml
spring:
  datasource:
    type: com.zaxxer.hikari.HikariDataSource
    hikari:
      # 連線池基本設定
      maximum-pool-size: 20          # 最大連線數
      minimum-idle: 5                # 最小空閒連線數
      idle-timeout: 300000           # 空閒連線超時時間 (5分鐘)
      max-lifetime: 1800000          # 連線最大生命週期 (30分鐘)
      connection-timeout: 20000      # 連線超時時間 (20秒)
      
      # 連線驗證
      validation-timeout: 5000       # 連線驗證超時
      connection-test-query: SELECT 1
      
      # 效能調整
      auto-commit: true
      read-only: false
      isolation-level: TRANSACTION_READ_COMMITTED
      
      # 監控設定
      leak-detection-threshold: 60000 # 連線洩漏檢測閾值 (60秒)
      register-mbeans: true           # 註冊 MBeans 供監控
      
      # 連線池名稱
      pool-name: SpringBootHikariCP
```

#### 5.5.2 多資料來源配置
```java
/**
 * 多資料來源配置
 */
@Configuration
public class DatabaseConfig {

    @Primary
    @Bean(name = "primaryDataSource")
    @ConfigurationProperties("spring.datasource.primary")
    public DataSource primaryDataSource() {
        return DataSourceBuilder.create().build();
    }

    @Bean(name = "secondaryDataSource")
    @ConfigurationProperties("spring.datasource.secondary")
    public DataSource secondaryDataSource() {
        return DataSourceBuilder.create().build();
    }

    @Primary
    @Bean(name = "primaryEntityManagerFactory")
    public LocalContainerEntityManagerFactoryBean primaryEntityManagerFactory(
            EntityManagerFactoryBuilder builder,
            @Qualifier("primaryDataSource") DataSource dataSource) {
        
        return builder
                .dataSource(dataSource)
                .packages("com.tutorial.model.primary")
                .persistenceUnit("primary")
                .build();
    }

    @Bean(name = "secondaryEntityManagerFactory")
    public LocalContainerEntityManagerFactoryBean secondaryEntityManagerFactory(
            EntityManagerFactoryBuilder builder,
            @Qualifier("secondaryDataSource") DataSource dataSource) {
        
        return builder
                .dataSource(dataSource)
                .packages("com.tutorial.model.secondary")
                .persistenceUnit("secondary")
                .build();
    }

    @Primary
    @Bean(name = "primaryTransactionManager")
    public PlatformTransactionManager primaryTransactionManager(
            @Qualifier("primaryEntityManagerFactory") EntityManagerFactory entityManagerFactory) {
        
        return new JpaTransactionManager(entityManagerFactory);
    }

    @Bean(name = "secondaryTransactionManager")
    public PlatformTransactionManager secondaryTransactionManager(
            @Qualifier("secondaryEntityManagerFactory") EntityManagerFactory entityManagerFactory) {
        
        return new JpaTransactionManager(entityManagerFactory);
    }
}

/**
 * 主要資料來源的 Repository 配置
 */
@Configuration
@EnableJpaRepositories(
    basePackages = "com.tutorial.repository.primary",
    entityManagerFactoryRef = "primaryEntityManagerFactory",
    transactionManagerRef = "primaryTransactionManager"
)
public class PrimaryRepositoryConfig {
}

/**
 * 次要資料來源的 Repository 配置
 */
@Configuration
@EnableJpaRepositories(
    basePackages = "com.tutorial.repository.secondary",
    entityManagerFactoryRef = "secondaryEntityManagerFactory",
    transactionManagerRef = "secondaryTransactionManager"
)
public class SecondaryRepositoryConfig {
}
```

### 5.6 章節小練習

**問題 1**: JPA 中，`@GeneratedValue(strategy = GenerationType.IDENTITY)` 的作用是什麼？
**答案**: 指定主鍵的生成策略為自動遞增，由資料庫自動生成唯一的 ID 值。

**問題 2**: 以下哪種關係對應是正確的？
A) `@OneToMany(mappedBy = "department")` 
B) `@ManyToOne @JoinColumn(name = "department_id")`
C) 兩者配合使用
D) 只能使用其中一種

**答案**: C) 兩者配合使用（在雙向關係中）

**問題 3**: 完成以下 Repository 查詢方法：
```java
public interface UserRepository extends JpaRepository<User, Long> {
    // 根據部門名稱和活躍狀態查詢使用者
    List<User> findBy______And______(String departmentName, Boolean active);
}
```
**答案**: `findByDepartmentNameAndActive`

**問題 4**: `@Transactional(readOnly = true)` 的作用是什麼？
**答案**: 
1. 告知 JPA 這是唯讀操作，可以進行效能優化
2. 防止在事務中進行寫入操作
3. 某些資料庫驅動可以將連線路由到唯讀副本

### 5.7 實務注意事項

#### ⚠️ 重要提醒
1. **連線池設定**: 根據應用負載合理設定連線池大小
2. **N+1 問題**: 注意 Lazy Loading 可能導致的 N+1 查詢問題
3. **事務邊界**: 合理設定事務邊界，避免事務過大或過小
4. **索引優化**: 為經常查詢的欄位建立適當的索引

---

## 6. 常用功能

### 6.1 資料驗證 (Validation)

#### 6.1.1 Bean Validation 基礎
```xml
<!-- pom.xml -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-validation</artifactId>
</dependency>
```

```java
/**
 * 使用者註冊請求 DTO - 展示各種驗證註解
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
public class UserRegistrationDto {

    @NotBlank(message = "姓名不能為空")
    @Size(min = 2, max = 50, message = "姓名長度必須在 2-50 字元之間")
    private String name;

    @NotBlank(message = "Email 不能為空")
    @Email(message = "Email 格式不正確")
    private String email;

    @NotBlank(message = "密碼不能為空")
    @Size(min = 8, max = 20, message = "密碼長度必須在 8-20 字元之間")
    @Pattern(regexp = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]+$", 
             message = "密碼必須包含大小寫字母、數字和特殊字元")
    private String password;

    @NotBlank(message = "確認密碼不能為空")
    private String confirmPassword;

    @NotNull(message = "年齡不能為空")
    @Min(value = 18, message = "年齡不能小於 18 歲")
    @Max(value = 120, message = "年齡不能大於 120 歲")
    private Integer age;

    @Past(message = "生日必須是過去的日期")
    @DateTimeFormat(pattern = "yyyy-MM-dd")
    private LocalDate birthDate;

    @Pattern(regexp = "^[0-9-+()\\s]*$", message = "電話號碼格式不正確")
    private String phone;

    @DecimalMin(value = "0.0", inclusive = false, message = "薪資必須大於 0")
    @DecimalMax(value = "999999.99", message = "薪資不能超過 999,999.99")
    @Digits(integer = 6, fraction = 2, message = "薪資格式不正確")
    private BigDecimal salary;

    @Valid
    @NotNull(message = "地址資訊不能為空")
    private AddressDto address;

    @Size(max = 3, message = "最多只能選擇 3 個技能")
    @NotEmpty(message = "至少要選擇一個技能")
    private List<@NotBlank(message = "技能名稱不能為空") String> skills;
}

/**
 * 地址 DTO
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
public class AddressDto {

    @NotBlank(message = "城市不能為空")
    private String city;

    @NotBlank(message = "區域不能為空")
    private String district;

    @NotBlank(message = "詳細地址不能為空")
    @Size(max = 200, message = "詳細地址不能超過 200 字元")
    private String detail;

    @Pattern(regexp = "^\\d{5}$", message = "郵遞區號必須是 5 位數字")
    private String zipCode;
}
```

#### 6.1.2 自定義驗證註解
```java
/**
 * 密碼確認驗證註解
 */
@Target({ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Constraint(validatedBy = PasswordMatchValidator.class)
@Documented
public @interface PasswordMatch {
    String message() default "密碼與確認密碼不一致";
    Class<?>[] groups() default {};
    Class<? extends Payload>[] payload() default {};
}

/**
 * 密碼確認驗證器
 */
public class PasswordMatchValidator implements ConstraintValidator<PasswordMatch, UserRegistrationDto> {

    @Override
    public void initialize(PasswordMatch constraintAnnotation) {
        // 初始化邏輯
    }

    @Override
    public boolean isValid(UserRegistrationDto dto, ConstraintValidatorContext context) {
        if (dto == null) {
            return true;
        }

        String password = dto.getPassword();
        String confirmPassword = dto.getConfirmPassword();

        boolean isValid = Objects.equals(password, confirmPassword);

        if (!isValid) {
            context.disableDefaultConstraintViolation();
            context.buildConstraintViolationWithTemplate("密碼與確認密碼不一致")
                   .addPropertyNode("confirmPassword")
                   .addConstraintViolation();
        }

        return isValid;
    }
}

/**
 * 唯一 Email 驗證註解
 */
@Target({ElementType.FIELD})
@Retention(RetentionPolicy.RUNTIME)
@Constraint(validatedBy = UniqueEmailValidator.class)
@Documented
public @interface UniqueEmail {
    String message() default "Email 已存在";
    Class<?>[] groups() default {};
    Class<? extends Payload>[] payload() default {};
}

/**
 * 唯一 Email 驗證器
 */
@Component
public class UniqueEmailValidator implements ConstraintValidator<UniqueEmail, String> {

    @Autowired
    private UserRepository userRepository;

    @Override
    public boolean isValid(String email, ConstraintValidatorContext context) {
        if (email == null || email.isEmpty()) {
            return true; // 讓 @NotBlank 處理空值驗證
        }
        return !userRepository.existsByEmail(email);
    }
}

/**
 * 更新後的註冊 DTO
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@PasswordMatch
public class UserRegistrationDto {
    
    // ... 其他欄位

    @NotBlank(message = "Email 不能為空")
    @Email(message = "Email 格式不正確")
    @UniqueEmail
    private String email;

    // ... 其他欄位
}
```

#### 6.1.3 Controller 層驗證處理
```java
/**
 * 使用者註冊控制器
 */
@RestController
@RequestMapping("/api/auth")
@Validated
public class AuthController {

    private final UserService userService;

    public AuthController(UserService userService) {
        this.userService = userService;
    }

    /**
     * 使用者註冊
     */
    @PostMapping("/register")
    public ResponseEntity<ApiResponse<User>> register(@Valid @RequestBody UserRegistrationDto dto) {
        User user = userService.registerUser(dto);
        ApiResponse<User> response = ApiResponse.<User>builder()
            .success(true)
            .message("註冊成功")
            .data(user)
            .build();
        return ResponseEntity.status(HttpStatus.CREATED).body(response);
    }

    /**
     * 驗證單一欄位
     */
    @GetMapping("/validate-email")
    public ResponseEntity<ApiResponse<Boolean>> validateEmail(
            @RequestParam @Email(message = "Email 格式不正確") String email) {
        
        boolean isAvailable = !userService.existsByEmail(email);
        ApiResponse<Boolean> response = ApiResponse.<Boolean>builder()
            .success(true)
            .message(isAvailable ? "Email 可用" : "Email 已存在")
            .data(isAvailable)
            .build();
        return ResponseEntity.ok(response);
    }
}
```

### 6.2 異常處理 (Exception Handling)

#### 6.2.1 自定義異常類別
```java
/**
 * 基礎業務異常
 */
public abstract class BusinessException extends RuntimeException {
    private final String errorCode;

    public BusinessException(String errorCode, String message) {
        super(message);
        this.errorCode = errorCode;
    }

    public BusinessException(String errorCode, String message, Throwable cause) {
        super(message, cause);
        this.errorCode = errorCode;
    }

    public String getErrorCode() {
        return errorCode;
    }
}

/**
 * 使用者不存在異常
 */
public class UserNotFoundException extends BusinessException {
    public UserNotFoundException(String message) {
        super("USER_NOT_FOUND", message);
    }
}

/**
 * 重複 Email 異常
 */
public class DuplicateEmailException extends BusinessException {
    public DuplicateEmailException(String message) {
        super("DUPLICATE_EMAIL", message);
    }
}

/**
 * 驗證異常
 */
public class ValidationException extends BusinessException {
    private final List<String> errors;

    public ValidationException(String message, List<String> errors) {
        super("VALIDATION_ERROR", message);
        this.errors = errors;
    }

    public List<String> getErrors() {
        return errors;
    }
}
```

#### 6.2.2 全域異常處理器
```java
/**
 * 全域異常處理器
 */
@RestControllerAdvice
@Slf4j
public class GlobalExceptionHandler {

    /**
     * 處理驗證異常
     */
    @ExceptionHandler(MethodArgumentNotValidException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public ApiResponse<Object> handleValidationExceptions(MethodArgumentNotValidException ex) {
        List<String> errors = ex.getBindingResult()
                .getFieldErrors()
                .stream()
                .map(error -> error.getField() + ": " + error.getDefaultMessage())
                .collect(Collectors.toList());

        log.warn("驗證失敗: {}", errors);

        return ApiResponse.builder()
                .success(false)
                .message("資料驗證失敗")
                .errors(errors)
                .timestamp(LocalDateTime.now())
                .build();
    }

    /**
     * 處理業務異常
     */
    @ExceptionHandler(BusinessException.class)
    public ResponseEntity<ApiResponse<Object>> handleBusinessException(BusinessException ex) {
        log.warn("業務異常: {}", ex.getMessage());

        ApiResponse<Object> response = ApiResponse.builder()
                .success(false)
                .errorCode(ex.getErrorCode())
                .message(ex.getMessage())
                .timestamp(LocalDateTime.now())
                .build();

        HttpStatus status = getHttpStatusForBusinessException(ex);
        return ResponseEntity.status(status).body(response);
    }

    /**
     * 處理資源不存在異常
     */
    @ExceptionHandler(UserNotFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public ApiResponse<Object> handleUserNotFoundException(UserNotFoundException ex) {
        log.warn("使用者不存在: {}", ex.getMessage());

        return ApiResponse.builder()
                .success(false)
                .errorCode(ex.getErrorCode())
                .message(ex.getMessage())
                .timestamp(LocalDateTime.now())
                .build();
    }

    /**
     * 處理參數驗證異常 (RequestParam 等)
     */
    @ExceptionHandler(ConstraintViolationException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public ApiResponse<Object> handleConstraintViolationException(ConstraintViolationException ex) {
        List<String> errors = ex.getConstraintViolations()
                .stream()
                .map(violation -> violation.getPropertyPath() + ": " + violation.getMessage())
                .collect(Collectors.toList());

        log.warn("參數驗證失敗: {}", errors);

        return ApiResponse.builder()
                .success(false)
                .message("參數驗證失敗")
                .errors(errors)
                .timestamp(LocalDateTime.now())
                .build();
    }

    /**
     * 處理資料庫異常
     */
    @ExceptionHandler(DataIntegrityViolationException.class)
    @ResponseStatus(HttpStatus.CONFLICT)
    public ApiResponse<Object> handleDataIntegrityViolationException(DataIntegrityViolationException ex) {
        log.error("資料完整性違反", ex);

        String message = "資料操作失敗";
        if (ex.getMessage().contains("Duplicate entry")) {
            message = "資料重複，無法執行操作";
        } else if (ex.getMessage().contains("foreign key constraint")) {
            message = "資料存在關聯，無法執行操作";
        }

        return ApiResponse.builder()
                .success(false)
                .errorCode("DATA_INTEGRITY_VIOLATION")
                .message(message)
                .timestamp(LocalDateTime.now())
                .build();
    }

    /**
     * 處理存取拒絕異常
     */
    @ExceptionHandler(AccessDeniedException.class)
    @ResponseStatus(HttpStatus.FORBIDDEN)
    public ApiResponse<Object> handleAccessDeniedException(AccessDeniedException ex) {
        log.warn("存取被拒絕: {}", ex.getMessage());

        return ApiResponse.builder()
                .success(false)
                .errorCode("ACCESS_DENIED")
                .message("沒有權限執行此操作")
                .timestamp(LocalDateTime.now())
                .build();
    }

    /**
     * 處理系統異常
     */
    @ExceptionHandler(Exception.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public ApiResponse<Object> handleGenericException(Exception ex) {
        log.error("系統異常", ex);

        return ApiResponse.builder()
                .success(false)
                .errorCode("INTERNAL_ERROR")
                .message("系統內部錯誤，請稍後再試")
                .timestamp(LocalDateTime.now())
                .build();
    }

    private HttpStatus getHttpStatusForBusinessException(BusinessException ex) {
        switch (ex.getErrorCode()) {
            case "USER_NOT_FOUND":
                return HttpStatus.NOT_FOUND;
            case "DUPLICATE_EMAIL":
                return HttpStatus.CONFLICT;
            case "VALIDATION_ERROR":
                return HttpStatus.BAD_REQUEST;
            default:
                return HttpStatus.BAD_REQUEST;
        }
    }
}

/**
 * API 回應封裝類別
 */
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class ApiResponse<T> {
    private boolean success;
    private String message;
    private String errorCode;
    private T data;
    private List<String> errors;
    @Builder.Default
    private LocalDateTime timestamp = LocalDateTime.now();
}
```

### 6.3 日誌記錄 (Logging)

#### 6.3.1 Logback 配置
```xml
<!-- src/main/resources/logback-spring.xml -->
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <!-- 彩色日誌配置 -->
    <conversionRule conversionWord="clr" converterClass="org.springframework.boot.logging.logback.ColorConverter"/>
    
    <!-- 控制台輸出 -->
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%clr(%d{yyyy-MM-dd HH:mm:ss.SSS}){faint} %clr(%5p) %clr(${PID:- }){magenta} %clr(---){faint} %clr([%15.15t]){faint} %clr(%-40.40logger{39}){cyan} %clr(:){faint} %m%n</pattern>
        </encoder>
    </appender>
    
    <!-- 檔案輸出 -->
    <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>logs/application.log</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>logs/application.%d{yyyy-MM-dd}.%i.log</fileNamePattern>
            <timeBasedFileNamingAndTriggeringPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedFNATP">
                <maxFileSize>10MB</maxFileSize>
            </timeBasedFileNamingAndTriggeringPolicy>
            <maxHistory>30</maxHistory>
        </rollingPolicy>
        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>
    
    <!-- 錯誤日誌單獨記錄 -->
    <appender name="ERROR_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>logs/error.log</file>
        <filter class="ch.qos.logback.classic.filter.LevelFilter">
            <level>ERROR</level>
            <onMatch>ACCEPT</onMatch>
            <onMismatch>DENY</onMismatch>
        </filter>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>logs/error.%d{yyyy-MM-dd}.log</fileNamePattern>
            <maxHistory>30</maxHistory>
        </rollingPolicy>
        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>
    
    <!-- 開發環境配置 -->
    <springProfile name="dev">
        <root level="DEBUG">
            <appender-ref ref="CONSOLE"/>
            <appender-ref ref="FILE"/>
        </root>
        <logger name="com.tutorial" level="DEBUG"/>
        <logger name="org.springframework.web" level="DEBUG"/>
    </springProfile>
    
    <!-- 生產環境配置 -->
    <springProfile name="prod">
        <root level="INFO">
            <appender-ref ref="FILE"/>
            <appender-ref ref="ERROR_FILE"/>
        </root>
        <logger name="com.tutorial" level="INFO"/>
        <logger name="org.springframework" level="WARN"/>
        <logger name="org.hibernate" level="WARN"/>
    </springProfile>
</configuration>
```

#### 6.3.2 結構化日誌
```java
/**
 * 日誌工具類別
 */
@Slf4j
@Component
public class LoggingService {

    /**
     * 記錄使用者操作
     */
    public void logUserAction(String userId, String action, Object details) {
        MDC.put("userId", userId);
        MDC.put("action", action);
        
        try {
            log.info("使用者操作: {}", objectMapper.writeValueAsString(details));
        } catch (Exception e) {
            log.warn("日誌記錄失敗", e);
        } finally {
            MDC.clear();
        }
    }

    /**
     * 記錄 API 請求
     */
    public void logApiRequest(HttpServletRequest request, Object requestBody) {
        MDC.put("method", request.getMethod());
        MDC.put("uri", request.getRequestURI());
        MDC.put("userAgent", request.getHeader("User-Agent"));
        
        try {
            log.info("API 請求: {}", objectMapper.writeValueAsString(requestBody));
        } catch (Exception e) {
            log.info("API 請求記錄");
        } finally {
            MDC.clear();
        }
    }

    /**
     * 記錄效能指標
     */
    public void logPerformance(String operation, long duration) {
        MDC.put("operation", operation);
        MDC.put("duration", String.valueOf(duration));
        
        if (duration > 1000) {
            log.warn("操作執行緩慢: {} ms", duration);
        } else {
            log.debug("操作執行時間: {} ms", duration);
        }
        
        MDC.clear();
    }

    @Autowired
    private ObjectMapper objectMapper;
}

/**
 * 請求日誌攔截器
 */
@Component
@Slf4j
public class RequestLoggingInterceptor implements HandlerInterceptor {

    private final LoggingService loggingService;

    public RequestLoggingInterceptor(LoggingService loggingService) {
        this.loggingService = loggingService;
    }

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) {
        long startTime = System.currentTimeMillis();
        request.setAttribute("startTime", startTime);
        
        // 記錄請求資訊
        log.info("請求開始: {} {}", request.getMethod(), request.getRequestURI());
        
        return true;
    }

    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, 
                              Object handler, Exception ex) {
        
        long startTime = (Long) request.getAttribute("startTime");
        long duration = System.currentTimeMillis() - startTime;
        
        // 記錄回應資訊
        log.info("請求完成: {} {} - 狀態: {} - 執行時間: {} ms", 
                request.getMethod(), request.getRequestURI(), response.getStatus(), duration);
        
        // 記錄效能
        loggingService.logPerformance(request.getRequestURI(), duration);
        
        if (ex != null) {
            log.error("請求處理異常", ex);
        }
    }
}
```

### 6.4 安全性基礎 (Security)

#### 6.4.1 Spring Security 基本配置
```xml
<!-- pom.xml -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt-api</artifactId>
    <version>0.11.5</version>
</dependency>
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt-impl</artifactId>
    <version>0.11.5</version>
    <scope>runtime</scope>
</dependency>
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt-jackson</artifactId>
    <version>0.11.5</version>
    <scope>runtime</scope>
</dependency>
```

```java
/**
 * Spring Security 配置
 */
@Configuration
@EnableWebSecurity
@EnableMethodSecurity(prePostEnabled = true)
public class SecurityConfig {

    private final JwtAuthenticationEntryPoint jwtAuthenticationEntryPoint;
    private final JwtRequestFilter jwtRequestFilter;

    public SecurityConfig(JwtAuthenticationEntryPoint jwtAuthenticationEntryPoint,
                         JwtRequestFilter jwtRequestFilter) {
        this.jwtAuthenticationEntryPoint = jwtAuthenticationEntryPoint;
        this.jwtRequestFilter = jwtRequestFilter;
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    @Bean
    public AuthenticationManager authenticationManager(AuthenticationConfiguration config) throws Exception {
        return config.getAuthenticationManager();
    }

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http.csrf(csrf -> csrf.disable())
            .authorizeHttpRequests(authz -> authz
                .requestMatchers("/api/auth/**").permitAll()
                .requestMatchers("/h2-console/**").permitAll()
                .requestMatchers("/swagger-ui/**", "/v3/api-docs/**").permitAll()
                .requestMatchers(HttpMethod.GET, "/api/users").hasRole("USER")
                .requestMatchers(HttpMethod.POST, "/api/users").hasRole("ADMIN")
                .requestMatchers(HttpMethod.PUT, "/api/users/**").hasRole("ADMIN")
                .requestMatchers(HttpMethod.DELETE, "/api/users/**").hasRole("ADMIN")
                .anyRequest().authenticated()
            )
            .exceptionHandling(ex -> ex.authenticationEntryPoint(jwtAuthenticationEntryPoint))
            .sessionManagement(session -> session.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
            .headers(headers -> headers.frameOptions().deny());

        http.addFilterBefore(jwtRequestFilter, UsernamePasswordAuthenticationFilter.class);

        return http.build();
    }
}

/**
 * JWT 工具類別
 */
@Component
public class JwtUtil {

    private static final String SECRET = "mySecretKey";
    private static final int JWT_TOKEN_VALIDITY = 5 * 60 * 60; // 5 hours

    private Key getSigningKey() {
        byte[] keyBytes = Decoders.BASE64.decode(SECRET);
        return Keys.hmacShaKeyFor(keyBytes);
    }

    public String getUsernameFromToken(String token) {
        return getClaimFromToken(token, Claims::getSubject);
    }

    public Date getExpirationDateFromToken(String token) {
        return getClaimFromToken(token, Claims::getExpiration);
    }

    public <T> T getClaimFromToken(String token, Function<Claims, T> claimsResolver) {
        final Claims claims = getAllClaimsFromToken(token);
        return claimsResolver.apply(claims);
    }

    private Claims getAllClaimsFromToken(String token) {
        return Jwts.parserBuilder()
                .setSigningKey(getSigningKey())
                .build()
                .parseClaimsJws(token)
                .getBody();
    }

    private Boolean isTokenExpired(String token) {
        final Date expiration = getExpirationDateFromToken(token);
        return expiration.before(new Date());
    }

    public String generateToken(UserDetails userDetails) {
        Map<String, Object> claims = new HashMap<>();
        return createToken(claims, userDetails.getUsername());
    }

    private String createToken(Map<String, Object> claims, String subject) {
        return Jwts.builder()
                .setClaims(claims)
                .setSubject(subject)
                .setIssuedAt(new Date(System.currentTimeMillis()))
                .setExpiration(new Date(System.currentTimeMillis() + JWT_TOKEN_VALIDITY * 1000))
                .signWith(getSigningKey(), SignatureAlgorithm.HS512)
                .compact();
    }

    public Boolean validateToken(String token, UserDetails userDetails) {
        final String username = getUsernameFromToken(token);
        return (username.equals(userDetails.getUsername()) && !isTokenExpired(token));
    }
}
```

### 6.5 章節小練習

**問題 1**: Bean Validation 中，哪個註解用於驗證 Email 格式？
**答案**: `@Email`

**問題 2**: 在 Spring Boot 中，如何處理全域異常？
**答案**: 使用 `@RestControllerAdvice` 註解的類別，並在方法上使用 `@ExceptionHandler` 註解

**問題 3**: 完成以下自定義驗證註解：
```java
@Target({ElementType.FIELD})
@Retention(RetentionPolicy.RUNTIME)
@Constraint(validatedBy = ______.class)
public @interface UniqueEmail {
    String message() default "Email 已存在";
    // ...
}
```
**答案**: `UniqueEmailValidator`

**問題 4**: 在 Logback 配置中，如何設定日誌檔案的滾動策略？
**答案**: 使用 `<rollingPolicy>` 標籤，通常配合 `TimeBasedRollingPolicy` 或 `SizeAndTimeBasedFNATP`

### 6.6 實務注意事項

#### ⚠️ 重要提醒
1. **驗證層級**: 在 Controller、Service 和 Entity 層都要適當進行驗證
2. **異常處理**: 避免暴露系統內部資訊給客戶端
3. **日誌安全**: 不要記錄敏感資訊如密碼、金鑰等
4. **安全配置**: 生產環境要使用強密碼和適當的權限控制

---

## 7. 測試與品質

### 7.1 單元測試 (Unit Testing)

#### 7.1.1 基本測試配置
```xml
<!-- pom.xml 測試依賴 -->
<dependencies>
    <!-- Spring Boot Test Starter -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
    
    <!-- Testcontainers (用於整合測試) -->
    <dependency>
        <groupId>org.testcontainers</groupId>
        <artifactId>junit-jupiter</artifactId>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.testcontainers</groupId>
        <artifactId>mysql</artifactId>
        <scope>test</scope>
    </dependency>
</dependencies>
```

#### 7.1.2 Service 層測試
```java
/**
 * UserService 單元測試
 */
@ExtendWith(MockitoExtension.class)
class UserServiceTest {

    @Mock
    private UserRepository userRepository;

    @Mock
    private EmailService emailService;

    @InjectMocks
    private UserServiceImpl userService;

    @Test
    @DisplayName("根據 ID 查詢使用者 - 成功情況")
    void findUserById_Success() {
        // Given
        Long userId = 1L;
        User expectedUser = User.builder()
            .id(userId)
            .name("測試使用者")
            .email("test@example.com")
            .active(true)
            .build();
        
        when(userRepository.findById(userId)).thenReturn(Optional.of(expectedUser));

        // When
        User actualUser = userService.findUserById(userId);

        // Then
        assertThat(actualUser).isNotNull();
        assertThat(actualUser.getId()).isEqualTo(userId);
        assertThat(actualUser.getName()).isEqualTo("測試使用者");
        assertThat(actualUser.getEmail()).isEqualTo("test@example.com");
        
        verify(userRepository).findById(userId);
        verifyNoMoreInteractions(userRepository);
    }

    @Test
    @DisplayName("根據 ID 查詢使用者 - 使用者不存在")
    void findUserById_UserNotFound() {
        // Given
        Long userId = 999L;
        when(userRepository.findById(userId)).thenReturn(Optional.empty());

        // When & Then
        assertThatThrownBy(() -> userService.findUserById(userId))
            .isInstanceOf(UserNotFoundException.class)
            .hasMessage("找不到使用者，ID: " + userId);
        
        verify(userRepository).findById(userId);
    }

    @Test
    @DisplayName("建立使用者 - 成功情況")
    void saveUser_Success() {
        // Given
        User userToSave = User.builder()
            .name("新使用者")
            .email("new@example.com")
            .build();
        
        User savedUser = User.builder()
            .id(1L)
            .name("新使用者")
            .email("new@example.com")
            .active(true)
            .createdAt(LocalDateTime.now())
            .build();

        when(userRepository.existsByEmail("new@example.com")).thenReturn(false);
        when(userRepository.save(any(User.class))).thenReturn(savedUser);
        doNothing().when(emailService).sendWelcomeEmail(any(User.class));

        // When
        User result = userService.saveUser(userToSave);

        // Then
        assertThat(result).isNotNull();
        assertThat(result.getId()).isEqualTo(1L);
        assertThat(result.getName()).isEqualTo("新使用者");
        assertThat(result.getEmail()).isEqualTo("new@example.com");
        assertThat(result.getActive()).isTrue();
        
        verify(userRepository).existsByEmail("new@example.com");
        verify(userRepository).save(any(User.class));
        verify(emailService).sendWelcomeEmail(savedUser);
    }

    @Test
    @DisplayName("建立使用者 - Email 重複")
    void saveUser_DuplicateEmail() {
        // Given
        User userToSave = User.builder()
            .name("重複用戶")
            .email("duplicate@example.com")
            .build();

        when(userRepository.existsByEmail("duplicate@example.com")).thenReturn(true);

        // When & Then
        assertThatThrownBy(() -> userService.saveUser(userToSave))
            .isInstanceOf(DuplicateEmailException.class)
            .hasMessage("Email 已存在: duplicate@example.com");
        
        verify(userRepository).existsByEmail("duplicate@example.com");
        verify(userRepository, never()).save(any(User.class));
        verify(emailService, never()).sendWelcomeEmail(any(User.class));
    }

    @Test
    @DisplayName("查詢所有活躍使用者")
    void findAllActiveUsers() {
        // Given
        List<User> activeUsers = Arrays.asList(
            User.builder().id(1L).name("使用者1").active(true).build(),
            User.builder().id(2L).name("使用者2").active(true).build()
        );

        when(userRepository.findByActiveTrue()).thenReturn(activeUsers);

        // When
        List<User> result = userService.findAllUsers();

        // Then
        assertThat(result).hasSize(2);
        assertThat(result.get(0).getName()).isEqualTo("使用者1");
        assertThat(result.get(1).getName()).isEqualTo("使用者2");
        
        verify(userRepository).findByActiveTrue();
    }

    @ParameterizedTest
    @ValueSource(strings = {"test@example.com", "user@domain.org", "admin@company.co.uk"})
    @DisplayName("驗證 Email 存在性 - 參數化測試")
    void existsByEmail_ParameterizedTest(String email) {
        // Given
        when(userRepository.existsByEmail(email)).thenReturn(true);

        // When
        boolean result = userService.existsByEmail(email);

        // Then
        assertThat(result).isTrue();
        verify(userRepository).existsByEmail(email);
    }
}
```

#### 7.1.3 Repository 層測試
```java
/**
 * UserRepository 測試
 */
@DataJpaTest
@TestPropertySource(properties = {
    "spring.jpa.hibernate.ddl-auto=create-drop",
    "spring.jpa.show-sql=true"
})
class UserRepositoryTest {

    @Autowired
    private TestEntityManager entityManager;

    @Autowired
    private UserRepository userRepository;

    @Test
    @DisplayName("根據 Email 查詢使用者")
    void findByEmail_Success() {
        // Given
        User user = User.builder()
            .name("測試使用者")
            .email("test@example.com")
            .active(true)
            .createdAt(LocalDateTime.now())
            .build();
        
        entityManager.persistAndFlush(user);

        // When
        Optional<User> result = userRepository.findByEmail("test@example.com");

        // Then
        assertThat(result).isPresent();
        assertThat(result.get().getName()).isEqualTo("測試使用者");
        assertThat(result.get().getEmail()).isEqualTo("test@example.com");
    }

    @Test
    @DisplayName("根據部門查詢活躍使用者")
    void findByDepartmentAndActiveTrue() {
        // Given
        Department department = Department.builder()
            .name("IT")
            .build();
        entityManager.persistAndFlush(department);

        User activeUser = User.builder()
            .name("活躍使用者")
            .email("active@example.com")
            .department(department)
            .active(true)
            .createdAt(LocalDateTime.now())
            .build();

        User inactiveUser = User.builder()
            .name("非活躍使用者")
            .email("inactive@example.com")
            .department(department)
            .active(false)
            .createdAt(LocalDateTime.now())
            .build();

        entityManager.persistAndFlush(activeUser);
        entityManager.persistAndFlush(inactiveUser);

        // When
        List<User> result = userRepository.findByDepartmentNameAndActiveTrue("IT");

        // Then
        assertThat(result).hasSize(1);
        assertThat(result.get(0).getName()).isEqualTo("活躍使用者");
        assertThat(result.get(0).getActive()).isTrue();
    }

    @Test
    @DisplayName("自定義查詢 - 根據創建日期查詢")
    void findUsersCreatedAfter() {
        // Given
        LocalDateTime cutoffDate = LocalDateTime.now().minusDays(1);
        
        User oldUser = User.builder()
            .name("舊使用者")
            .email("old@example.com")
            .active(true)
            .createdAt(LocalDateTime.now().minusDays(2))
            .build();

        User newUser = User.builder()
            .name("新使用者")
            .email("new@example.com")
            .active(true)
            .createdAt(LocalDateTime.now())
            .build();

        entityManager.persistAndFlush(oldUser);
        entityManager.persistAndFlush(newUser);

        // When
        List<User> result = userRepository.findUsersCreatedAfter(cutoffDate);

        // Then
        assertThat(result).hasSize(1);
        assertThat(result.get(0).getName()).isEqualTo("新使用者");
    }

    @Test
    @DisplayName("分頁查詢測試")
    void findByDepartment_WithPaging() {
        // Given
        Department department = Department.builder().name("HR").build();
        entityManager.persistAndFlush(department);

        for (int i = 1; i <= 5; i++) {
            User user = User.builder()
                .name("使用者" + i)
                .email("user" + i + "@example.com")
                .department(department)
                .active(true)
                .createdAt(LocalDateTime.now())
                .build();
            entityManager.persistAndFlush(user);
        }

        Pageable pageable = PageRequest.of(0, 3, Sort.by("name"));

        // When
        Page<User> result = userRepository.findByDepartmentName("HR", pageable);

        // Then
        assertThat(result.getContent()).hasSize(3);
        assertThat(result.getTotalElements()).isEqualTo(5);
        assertThat(result.getTotalPages()).isEqualTo(2);
        assertThat(result.isFirst()).isTrue();
        assertThat(result.isLast()).isFalse();
    }
}
```

### 7.2 整合測試 (Integration Testing)

#### 7.2.1 Web 層測試
```java
/**
 * UserController 整合測試
 */
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@AutoConfigureTestDatabase(replace = AutoConfigureTestDatabase.Replace.NONE)
@Testcontainers
class UserControllerIntegrationTest {

    @Container
    static MySQLContainer<?> mysql = new MySQLContainer<>("mysql:8.0")
            .withDatabaseName("testdb")
            .withUsername("test")
            .withPassword("test");

    @Autowired
    private TestRestTemplate restTemplate;

    @Autowired
    private UserRepository userRepository;

    @DynamicPropertySource
    static void configureProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", mysql::getJdbcUrl);
        registry.add("spring.datasource.username", mysql::getUsername);
        registry.add("spring.datasource.password", mysql::getPassword);
    }

    @BeforeEach
    void setUp() {
        userRepository.deleteAll();
    }

    @Test
    @DisplayName("建立使用者 - 整合測試")
    void createUser_IntegrationTest() {
        // Given
        UserRegistrationDto registrationDto = UserRegistrationDto.builder()
            .name("整合測試使用者")
            .email("integration@example.com")
            .password("Password@123")
            .confirmPassword("Password@123")
            .age(25)
            .build();

        // When
        ResponseEntity<ApiResponse> response = restTemplate.postForEntity(
            "/api/users", registrationDto, ApiResponse.class);

        // Then
        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.CREATED);
        assertThat(response.getBody().isSuccess()).isTrue();
        assertThat(response.getBody().getMessage()).isEqualTo("使用者建立成功");

        // 驗證資料庫中的資料
        Optional<User> savedUser = userRepository.findByEmail("integration@example.com");
        assertThat(savedUser).isPresent();
        assertThat(savedUser.get().getName()).isEqualTo("整合測試使用者");
    }

    @Test
    @DisplayName("查詢使用者列表 - 分頁測試")
    void getAllUsers_WithPaging() {
        // Given
        createTestUsers(5);

        // When
        ResponseEntity<String> response = restTemplate.getForEntity(
            "/api/users?page=0&size=3&sort=name,asc", String.class);

        // Then
        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.OK);
        
        // 可以使用 JsonPath 或 ObjectMapper 進一步驗證回應內容
    }

    @Test
    @DisplayName("更新使用者 - 樂觀鎖測試")
    void updateUser_OptimisticLocking() {
        // Given
        User user = createTestUser("原始使用者", "original@example.com");
        
        UpdateUserDto updateDto1 = UpdateUserDto.builder()
            .id(user.getId())
            .name("更新使用者1")
            .version(user.getVersion())
            .build();

        UpdateUserDto updateDto2 = UpdateUserDto.builder()
            .id(user.getId())
            .name("更新使用者2")
            .version(user.getVersion())
            .build();

        // When
        ResponseEntity<ApiResponse> response1 = restTemplate.exchange(
            "/api/users/" + user.getId(), HttpMethod.PUT, 
            new HttpEntity<>(updateDto1), ApiResponse.class);

        ResponseEntity<ApiResponse> response2 = restTemplate.exchange(
            "/api/users/" + user.getId(), HttpMethod.PUT, 
            new HttpEntity<>(updateDto2), ApiResponse.class);

        // Then
        assertThat(response1.getStatusCode()).isEqualTo(HttpStatus.OK);
        assertThat(response2.getStatusCode()).isEqualTo(HttpStatus.CONFLICT);
    }

    private User createTestUser(String name, String email) {
        User user = User.builder()
            .name(name)
            .email(email)
            .active(true)
            .createdAt(LocalDateTime.now())
            .build();
        return userRepository.save(user);
    }

    private void createTestUsers(int count) {
        for (int i = 1; i <= count; i++) {
            createTestUser("使用者" + i, "user" + i + "@example.com");
        }
    }
}
```

#### 7.2.2 MockMvc 測試
```java
/**
 * UserController MockMvc 測試
 */
@WebMvcTest(UserController.class)
class UserControllerMockMvcTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private UserService userService;

    @Autowired
    private ObjectMapper objectMapper;

    @Test
    @DisplayName("GET /api/users/{id} - 成功情況")
    void getUserById_Success() throws Exception {
        // Given
        Long userId = 1L;
        User user = User.builder()
            .id(userId)
            .name("測試使用者")
            .email("test@example.com")
            .active(true)
            .build();

        when(userService.findUserById(userId)).thenReturn(user);

        // When & Then
        mockMvc.perform(get("/api/users/{id}", userId)
                .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id").value(userId))
                .andExpect(jsonPath("$.name").value("測試使用者"))
                .andExpect(jsonPath("$.email").value("test@example.com"))
                .andExpect(jsonPath("$.active").value(true));

        verify(userService).findUserById(userId);
    }

    @Test
    @DisplayName("GET /api/users/{id} - 使用者不存在")
    void getUserById_NotFound() throws Exception {
        // Given
        Long userId = 999L;
        when(userService.findUserById(userId))
            .thenThrow(new UserNotFoundException("使用者不存在: " + userId));

        // When & Then
        mockMvc.perform(get("/api/users/{id}", userId)
                .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isNotFound())
                .andExpect(jsonPath("$.success").value(false))
                .andExpect(jsonPath("$.errorCode").value("USER_NOT_FOUND"))
                .andExpect(jsonPath("$.message").value("使用者不存在: " + userId));
    }

    @Test
    @DisplayName("POST /api/users - 驗證失敗")
    void createUser_ValidationFailed() throws Exception {
        // Given
        UserRegistrationDto invalidDto = UserRegistrationDto.builder()
            .name("") // 空名稱
            .email("invalid-email") // 無效 Email
            .age(15) // 年齡不足
            .build();

        // When & Then
        mockMvc.perform(post("/api/users")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(invalidDto)))
                .andExpect(status().isBadRequest())
                .andExpect(jsonPath("$.success").value(false))
                .andExpect(jsonPath("$.message").value("資料驗證失敗"))
                .andExpect(jsonPath("$.errors").isArray())
                .andExpect(jsonPath("$.errors.length()").value(greaterThan(0)));

        verify(userService, never()).saveUser(any(User.class));
    }

    @Test
    @DisplayName("POST /api/users - 成功建立")
    void createUser_Success() throws Exception {
        // Given
        UserRegistrationDto validDto = UserRegistrationDto.builder()
            .name("新使用者")
            .email("new@example.com")
            .password("Password@123")
            .confirmPassword("Password@123")
            .age(25)
            .build();

        User savedUser = User.builder()
            .id(1L)
            .name("新使用者")
            .email("new@example.com")
            .active(true)
            .createdAt(LocalDateTime.now())
            .build();

        when(userService.saveUser(any(User.class))).thenReturn(savedUser);

        // When & Then
        mockMvc.perform(post("/api/users")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(validDto)))
                .andExpect(status().isCreated())
                .andExpect(jsonPath("$.id").value(1))
                .andExpect(jsonPath("$.name").value("新使用者"))
                .andExpect(jsonPath("$.email").value("new@example.com"));

        verify(userService).saveUser(any(User.class));
    }
}
```

### 7.3 測試配置與工具

#### 7.3.1 測試配置檔案
```yaml
# src/test/resources/application-test.yml
spring:
  datasource:
    url: jdbc:h2:mem:testdb;DB_CLOSE_DELAY=-1;DB_CLOSE_ON_EXIT=FALSE
    driver-class-name: org.h2.Driver
    username: sa
    password: password
  
  jpa:
    hibernate:
      ddl-auto: create-drop
    show-sql: true
    database-platform: org.hibernate.dialect.H2Dialect
  
  h2:
    console:
      enabled: true
  
  # 測試環境日誌配置
  logging:
    level:
      com.tutorial: DEBUG
      org.springframework.web: DEBUG
      org.hibernate.SQL: DEBUG
      org.hibernate.type.descriptor.sql.BasicBinder: TRACE

# 測試環境特定配置
test:
  data:
    cleanup: true
  performance:
    timeout: 5000
```

#### 7.3.2 測試工具類別
```java
/**
 * 測試資料建立工具
 */
@Component
@TestPropertySource
public class TestDataBuilder {

    public static User createTestUser(String name, String email) {
        return User.builder()
            .name(name)
            .email(email)
            .active(true)
            .createdAt(LocalDateTime.now())
            .build();
    }

    public static List<User> createTestUsers(int count) {
        List<User> users = new ArrayList<>();
        for (int i = 1; i <= count; i++) {
            users.add(createTestUser("使用者" + i, "user" + i + "@example.com"));
        }
        return users;
    }

    public static Department createTestDepartment(String name) {
        return Department.builder()
            .name(name)
            .description(name + " 部門")
            .createdAt(LocalDateTime.now())
            .build();
    }

    public static UserRegistrationDto createValidRegistrationDto() {
        return UserRegistrationDto.builder()
            .name("測試使用者")
            .email("test@example.com")
            .password("Password@123")
            .confirmPassword("Password@123")
            .age(25)
            .birthDate(LocalDate.of(1998, 1, 1))
            .phone("0912345678")
            .build();
    }
}

/**
 * 測試基底類別
 */
@TestPropertySource(locations = "classpath:application-test.yml")
@ActiveProfiles("test")
public abstract class BaseIntegrationTest {

    @Autowired
    protected TestEntityManager entityManager;

    @BeforeEach
    void setUpBase() {
        // 每個測試前的通用設定
    }

    @AfterEach
    void tearDownBase() {
        // 每個測試後的清理工作
    }

    protected void flushAndClear() {
        entityManager.flush();
        entityManager.clear();
    }
}
```

### 7.4 效能測試

#### 7.4.1 簡單效能測試
```java
/**
 * 效能測試範例
 */
@SpringBootTest
class PerformanceTest {

    @Autowired
    private UserService userService;

    @Autowired
    private UserRepository userRepository;

    @Test
    @DisplayName("批次建立使用者效能測試")
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    void batchCreateUsers_PerformanceTest() {
        // Given
        int userCount = 1000;
        List<User> users = TestDataBuilder.createTestUsers(userCount);

        // When
        long startTime = System.currentTimeMillis();
        
        userRepository.saveAll(users);
        
        long endTime = System.currentTimeMillis();
        long duration = endTime - startTime;

        // Then
        assertThat(userRepository.count()).isEqualTo(userCount);
        assertThat(duration).isLessThan(5000); // 應在 5 秒內完成
        
        System.out.println("批次建立 " + userCount + " 個使用者耗時: " + duration + " ms");
    }

    @Test
    @DisplayName("分頁查詢效能測試")
    void pageQuery_PerformanceTest() {
        // Given
        int totalUsers = 10000;
        List<User> users = TestDataBuilder.createTestUsers(totalUsers);
        userRepository.saveAll(users);

        Pageable pageable = PageRequest.of(0, 100);

        // When
        long startTime = System.currentTimeMillis();
        
        Page<User> page = userRepository.findAll(pageable);
        
        long endTime = System.currentTimeMillis();
        long duration = endTime - startTime;

        // Then
        assertThat(page.getContent()).hasSize(100);
        assertThat(page.getTotalElements()).isEqualTo(totalUsers);
        assertThat(duration).isLessThan(1000); // 應在 1 秒內完成
        
        System.out.println("分頁查詢耗時: " + duration + " ms");
    }
}
```

### 7.5 測試覆蓋率

#### 7.5.1 JaCoCo 配置
```xml
<!-- pom.xml -->
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.8</version>
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
                        <element>CLASS</element>
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

### 7.6 章節小練習

**問題 1**: 在 Spring Boot 測試中，`@DataJpaTest` 註解的作用是什麼？
**答案**: 用於測試 JPA Repository 層，只載入 JPA 相關配置，提供嵌入式資料庫和 TestEntityManager

**問題 2**: `@WebMvcTest` 和 `@SpringBootTest` 的差異是什麼？
**答案**: 
- `@WebMvcTest`: 只載入 Web 層相關元件，適合單元測試
- `@SpringBootTest`: 載入完整應用程式上下文，適合整合測試

**問題 3**: 如何在測試中模擬外部服務？
**答案**: 使用 `@MockBean` 註解來模擬 Spring Bean，或使用 `@Mock` 配合 `@InjectMocks` 進行純單元測試

### 7.7 實務注意事項

#### ⚠️ 重要提醒
1. **測試隔離**: 確保測試之間不會相互影響
2. **測試資料**: 使用獨立的測試資料庫
3. **效能測試**: 避免在 CI/CD 中執行長時間的效能測試
4. **覆蓋率**: 追求合理的測試覆蓋率，不要盲目追求 100%

---

## 8. 部署與實務應用

### 8.1 內嵌伺服器配置

#### 8.1.1 Tomcat 配置調整
```yaml
# application.yml
server:
  port: 8080
  servlet:
    context-path: /api
  compression:
    enabled: true
    mime-types: text/html,text/xml,text/plain,text/css,text/javascript,application/javascript,application/json
    min-response-size: 1024
  http2:
    enabled: true
  tomcat:
    threads:
      max: 200
      min-spare: 10
    connection-timeout: 20000
    max-connections: 8192
    accept-count: 100
    max-http-form-post-size: 2MB
    max-swallow-size: 2MB
```

#### 8.1.2 替代伺服器配置
```xml
<!-- 使用 Jetty 替代 Tomcat -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <exclusions>
        <exclusion>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-tomcat</artifactId>
        </exclusion>
    </exclusions>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-jetty</artifactId>
</dependency>
```

```yaml
# Jetty 配置
server:
  jetty:
    threads:
      max: 200
      min: 8
      idle-timeout: 60000
    connection-idle-timeout: 30000
    max-http-form-post-size: 2MB
```

### 8.2 Docker 容器化

#### 8.2.1 多階段 Dockerfile
```dockerfile
# Dockerfile
FROM eclipse-temurin:21-jdk-alpine AS builder

WORKDIR /app

# 複製 Maven 配置檔案
COPY pom.xml .
COPY .mvn .mvn
COPY mvnw .

# 下載依賴（利用 Docker 快取）
RUN ./mvnw dependency:go-offline -B

# 複製原始碼並建置
COPY src src
RUN ./mvnw clean package -DskipTests

# 執行階段
FROM eclipse-temurin:21-jre-alpine

# 建立非 root 使用者
RUN addgroup -g 1001 -S spring && \
    adduser -u 1001 -S spring -G spring

WORKDIR /app

# 複製建置產生的 JAR 檔案
COPY --from=builder /app/target/*.jar app.jar

# 設定檔案擁有者
RUN chown -R spring:spring /app

# 切換到非 root 使用者
USER spring:spring

# 健康檢查
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/actuator/health || exit 1

# 暴露埠號
EXPOSE 8080

# 使用 exec 形式的 ENTRYPOINT
ENTRYPOINT ["java", "-jar", "app.jar"]
```

#### 8.2.2 Docker Compose 配置
```yaml
# docker-compose.yml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      - SPRING_PROFILES_ACTIVE=docker
      - DB_HOST=mysql
      - DB_PORT=3306
      - DB_NAME=springboot_tutorial
      - DB_USERNAME=app_user
      - DB_PASSWORD=app_password
    depends_on:
      mysql:
        condition: service_healthy
    networks:
      - spring-network
    restart: unless-stopped

  mysql:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: root_password
      MYSQL_DATABASE: springboot_tutorial
      MYSQL_USER: app_user
      MYSQL_PASSWORD: app_password
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      timeout: 20s
      retries: 10
    networks:
      - spring-network
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
    networks:
      - spring-network
    restart: unless-stopped

volumes:
  mysql_data:
  redis_data:

networks:
  spring-network:
    driver: bridge
```

#### 8.2.3 Docker 環境配置
```yaml
# application-docker.yml
spring:
  datasource:
    url: jdbc:mysql://${DB_HOST:mysql}:${DB_PORT:3306}/${DB_NAME:springboot_tutorial}
    username: ${DB_USERNAME:app_user}
    password: ${DB_PASSWORD:app_password}
    hikari:
      maximum-pool-size: 20
      minimum-idle: 5
      connection-timeout: 20000
      idle-timeout: 300000
      max-lifetime: 1200000

  redis:
    host: ${REDIS_HOST:redis}
    port: ${REDIS_PORT:6379}
    timeout: 2000ms
    lettuce:
      pool:
        max-active: 8
        max-idle: 8
        min-idle: 0

  jpa:
    hibernate:
      ddl-auto: validate
    show-sql: false

logging:
  level:
    com.tutorial: INFO
    org.springframework: WARN
    org.hibernate: WARN
  pattern:
    console: "%d{yyyy-MM-dd HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n"
```

### 8.3 雲端部署

#### 8.3.1 Kubernetes 部署配置
```yaml
# k8s/namespace.yml
apiVersion: v1
kind: Namespace
metadata:
  name: spring-tutorial

---
# k8s/configmap.yml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
  namespace: spring-tutorial
data:
  SPRING_PROFILES_ACTIVE: "k8s"
  DB_HOST: "mysql-service"
  DB_PORT: "3306"
  DB_NAME: "springboot_tutorial"

---
# k8s/secret.yml
apiVersion: v1
kind: Secret
metadata:
  name: app-secret
  namespace: spring-tutorial
type: Opaque
data:
  DB_USERNAME: YXBwX3VzZXI=  # base64: app_user
  DB_PASSWORD: YXBwX3Bhc3N3b3Jk  # base64: app_password

---
# k8s/deployment.yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: spring-tutorial-app
  namespace: spring-tutorial
spec:
  replicas: 3
  selector:
    matchLabels:
      app: spring-tutorial-app
  template:
    metadata:
      labels:
        app: spring-tutorial-app
    spec:
      containers:
      - name: app
        image: spring-tutorial:latest
        ports:
        - containerPort: 8080
        env:
        - name: SPRING_PROFILES_ACTIVE
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: SPRING_PROFILES_ACTIVE
        - name: DB_HOST
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: DB_HOST
        - name: DB_USERNAME
          valueFrom:
            secretKeyRef:
              name: app-secret
              key: DB_USERNAME
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: app-secret
              key: DB_PASSWORD
        resources:
          requests:
            memory: "512Mi"
            cpu: "250m"
          limits:
            memory: "1Gi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /actuator/health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /actuator/health/readiness
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5

---
# k8s/service.yml
apiVersion: v1
kind: Service
metadata:
  name: spring-tutorial-service
  namespace: spring-tutorial
spec:
  selector:
    app: spring-tutorial-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
  type: ClusterIP

---
# k8s/ingress.yml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: spring-tutorial-ingress
  namespace: spring-tutorial
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: spring-tutorial.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: spring-tutorial-service
            port:
              number: 80
```

#### 8.3.2 AWS ECS 部署
```json
{
  "family": "spring-tutorial-task",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "512",
  "memory": "1024",
  "executionRoleArn": "arn:aws:iam::ACCOUNT:role/ecsTaskExecutionRole",
  "taskRoleArn": "arn:aws:iam::ACCOUNT:role/ecsTaskRole",
  "containerDefinitions": [
    {
      "name": "spring-tutorial-app",
      "image": "your-registry/spring-tutorial:latest",
      "portMappings": [
        {
          "containerPort": 8080,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {
          "name": "SPRING_PROFILES_ACTIVE",
          "value": "aws"
        }
      ],
      "secrets": [
        {
          "name": "DB_PASSWORD",
          "valueFrom": "arn:aws:secretsmanager:region:account:secret:db-password"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/spring-tutorial",
          "awslogs-region": "us-west-2",
          "awslogs-stream-prefix": "ecs"
        }
      },
      "healthCheck": {
        "command": ["CMD-SHELL", "curl -f http://localhost:8080/actuator/health || exit 1"],
        "interval": 30,
        "timeout": 5,
        "retries": 3,
        "startPeriod": 60
      }
    }
  ]
}
```

### 8.4 監控與維運

#### 8.4.1 Spring Boot Actuator
```xml
<!-- pom.xml -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
<dependency>
    <groupId>io.micrometer</groupId>
    <artifactId>micrometer-registry-prometheus</artifactId>
</dependency>
```

```yaml
# application.yml - Actuator 配置
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,prometheus,loggers,threaddump,heapdump
      base-path: /actuator
  endpoint:
    health:
      show-details: when_authorized
      show-components: always
      probes:
        enabled: true
    metrics:
      enabled: true
  health:
    defaults:
      enabled: true
    diskspace:
      enabled: true
      threshold: 10GB
    db:
      enabled: true
  info:
    env:
      enabled: true
    java:
      enabled: true
    os:
      enabled: true
  metrics:
    export:
      prometheus:
        enabled: true
    web:
      server:
        request:
          autotime:
            enabled: true
```

#### 8.4.2 自定義健康檢查
```java
/**
 * 自定義健康檢查指標
 */
@Component
public class DatabaseHealthIndicator implements HealthIndicator {

    private final UserRepository userRepository;

    public DatabaseHealthIndicator(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Override
    public Health health() {
        try {
            long userCount = userRepository.count();
            
            if (userCount >= 0) {
                return Health.up()
                    .withDetail("database", "Available")
                    .withDetail("userCount", userCount)
                    .withDetail("timestamp", LocalDateTime.now())
                    .build();
            } else {
                return Health.down()
                    .withDetail("database", "Query returned negative count")
                    .build();
            }
        } catch (Exception e) {
            return Health.down()
                .withDetail("database", "Unavailable")
                .withDetail("error", e.getMessage())
                .build();
        }
    }
}

/**
 * 外部服務健康檢查
 */
@Component
public class ExternalServiceHealthIndicator implements HealthIndicator {

    private final RestTemplate restTemplate;

    public ExternalServiceHealthIndicator(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    @Override
    public Health health() {
        try {
            ResponseEntity<String> response = restTemplate.getForEntity(
                "https://api.external-service.com/health", String.class);
            
            if (response.getStatusCode() == HttpStatus.OK) {
                return Health.up()
                    .withDetail("externalService", "Available")
                    .withDetail("responseTime", "< 1000ms")
                    .build();
            } else {
                return Health.down()
                    .withDetail("externalService", "Unhealthy")
                    .withDetail("statusCode", response.getStatusCode())
                    .build();
            }
        } catch (Exception e) {
            return Health.down()
                .withDetail("externalService", "Unreachable")
                .withDetail("error", e.getMessage())
                .build();
        }
    }
}
```

#### 8.4.3 自定義指標
```java
/**
 * 自定義業務指標
 */
@Component
public class UserMetrics {

    private final Counter userCreatedCounter;
    private final Timer userOperationTimer;
    private final Gauge activeUsersGauge;
    private final UserRepository userRepository;

    public UserMetrics(MeterRegistry meterRegistry, UserRepository userRepository) {
        this.userRepository = userRepository;
        
        this.userCreatedCounter = Counter.builder("users.created")
            .description("Number of users created")
            .register(meterRegistry);
        
        this.userOperationTimer = Timer.builder("users.operation.duration")
            .description("User operation duration")
            .register(meterRegistry);
        
        this.activeUsersGauge = Gauge.builder("users.active")
            .description("Number of active users")
            .register(meterRegistry, this, UserMetrics::getActiveUserCount);
    }

    public void incrementUserCreated() {
        userCreatedCounter.increment();
    }

    public Timer.Sample startTimer() {
        return Timer.start();
    }

    public void recordOperationTime(Timer.Sample sample) {
        sample.stop(userOperationTimer);
    }

    private double getActiveUserCount() {
        return userRepository.countByActiveTrue();
    }
}

/**
 * 在服務中使用指標
 */
@Service
@Transactional
public class UserServiceImpl implements UserService {

    private final UserRepository userRepository;
    private final UserMetrics userMetrics;

    public UserServiceImpl(UserRepository userRepository, UserMetrics userMetrics) {
        this.userRepository = userRepository;
        this.userMetrics = userMetrics;
    }

    @Override
    public User saveUser(User user) {
        Timer.Sample sample = userMetrics.startTimer();
        
        try {
            User savedUser = userRepository.save(user);
            userMetrics.incrementUserCreated();
            return savedUser;
        } finally {
            userMetrics.recordOperationTime(sample);
        }
    }
}
```

### 8.5 CI/CD 整合

#### 8.5.1 GitHub Actions 配置
```yaml
# .github/workflows/ci-cd.yml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

env:
  JAVA_VERSION: '21'
  DOCKER_REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}/spring-tutorial

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      mysql:
        image: mysql:8.0
        env:
          MYSQL_ROOT_PASSWORD: root
          MYSQL_DATABASE: testdb
        ports:
          - 3306:3306
        options: >-
          --health-cmd="mysqladmin ping"
          --health-interval=10s
          --health-timeout=5s
          --health-retries=3

    steps:
    - uses: actions/checkout@v3
    
    - name: Set up JDK ${{ env.JAVA_VERSION }}
      uses: actions/setup-java@v3
      with:
        java-version: ${{ env.JAVA_VERSION }}
        distribution: 'temurin'
        
    - name: Cache Maven dependencies
      uses: actions/cache@v3
      with:
        path: ~/.m2
        key: ${{ runner.os }}-m2-${{ hashFiles('**/pom.xml') }}
        restore-keys: ${{ runner.os }}-m2
        
    - name: Run tests
      run: mvn clean test
      
    - name: Generate test report
      uses: dorny/test-reporter@v1
      if: success() || failure()
      with:
        name: Maven Tests
        path: target/surefire-reports/*.xml
        reporter: java-junit
        
    - name: Code coverage
      run: mvn jacoco:report
      
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: target/site/jacoco/jacoco.xml

  build:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up JDK ${{ env.JAVA_VERSION }}
      uses: actions/setup-java@v3
      with:
        java-version: ${{ env.JAVA_VERSION }}
        distribution: 'temurin'
        
    - name: Build application
      run: mvn clean package -DskipTests
      
    - name: Log in to Container Registry
      uses: docker/login-action@v2
      with:
        registry: ${{ env.DOCKER_REGISTRY }}
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}
        
    - name: Extract metadata
      id: meta
      uses: docker/metadata-action@v4
      with:
        images: ${{ env.DOCKER_REGISTRY }}/${{ env.IMAGE_NAME }}
        tags: |
          type=ref,event=branch
          type=ref,event=pr
          type=sha
          
    - name: Build and push Docker image
      uses: docker/build-push-action@v4
      with:
        context: .
        push: true
        tags: ${{ steps.meta.outputs.tags }}
        labels: ${{ steps.meta.outputs.labels }}

  deploy:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    environment: production
    
    steps:
    - name: Deploy to production
      run: |
        echo "Deploying to production environment"
        # 這裡會有實際的部署腳本
```

### 8.6 章節小練習

**問題 1**: Docker 多階段建置的主要優點是什麼？
**答案**: 
1. 減少最終映像檔大小
2. 提高安全性（移除建置工具）
3. 利用 Docker 快取層
4. 分離建置和執行環境

**問題 2**: Spring Boot Actuator 的 `/actuator/health` 端點有什麼作用？
**答案**: 提供應用程式健康狀態檢查，包括資料庫連線、磁碟空間、外部服務等狀態資訊

**問題 3**: 在 Kubernetes 中，liveness probe 和 readiness probe 的差異是什麼？
**答案**: 
- Liveness probe: 檢查容器是否存活，失敗時重啟容器
- Readiness probe: 檢查容器是否準備好接收流量，失敗時從服務中移除

### 8.7 實務注意事項

#### ⚠️ 重要提醒
1. **容器安全**: 使用非 root 使用者執行應用程式
2. **資源限制**: 合理設定記憶體和 CPU 限制
3. **健康檢查**: 實作完整的健康檢查機制
4. **監控告警**: 建立完善的監控和告警系統

---

## 9. 認證考試重點

### 9.1 Spring Boot 核心概念考點

#### 9.1.1 自動配置原理 ⭐⭐⭐
**常考知識點：**
- `@SpringBootApplication` 註解組成
- `@EnableAutoConfiguration` 工作原理
- `@ConditionalOn*` 註解系列
- 自動配置類別載入順序

**範例題目：**
```java
// 問：以下哪個註解組合等同於 @SpringBootApplication？
A) @Configuration + @EnableAutoConfiguration + @ComponentScan
B) @Component + @EnableAutoConfiguration + @ComponentScan  
C) @Configuration + @EnableAutoConfiguration + @Service
D) @Controller + @EnableAutoConfiguration + @ComponentScan

// 答案：A
```

#### 9.1.2 依賴注入考點 ⭐⭐⭐
**重點：**
- 建構式注入 vs 欄位注入 vs Setter 注入
- `@Autowired` 注入方式
- `@Qualifier` 用法
- 循環依賴問題

**範例題目：**
```java
@Service
public class UserService {
    private final UserRepository userRepository;
    
    // 問：推薦的注入方式是？
    // A) @Autowired private UserRepository userRepository;
    // B) 建構式注入（如下）
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    // 答案：B - 建構式注入
}
```

#### 9.1.3 配置管理考點 ⭐⭐
**重點：**
- `application.properties` vs `application.yml`
- Profile 使用
- `@ConfigurationProperties` 用法
- 外部化配置

### 9.2 Web 開發考點

#### 9.2.1 RESTful API 設計 ⭐⭐⭐
**重點：**
- HTTP 方法語義
- 狀態碼使用
- `@RestController` vs `@Controller`
- 請求參數處理

**範例題目：**
```java
// 問：以下哪個 HTTP 方法是冪等的？
A) POST
B) GET  
C) PUT
D) B 和 C

// 答案：D
```

#### 9.2.2 資料驗證考點 ⭐⭐
**重點：**
- Bean Validation 註解
- `@Valid` vs `@Validated`
- 群組驗證
- 自定義驗證器

### 9.3 資料存取考點

#### 9.3.1 JPA 基礎 ⭐⭐⭐
**重點：**
- Entity 關係對應
- Repository 方法命名規則
- JPQL 查詢
- 事務管理

**範例題目：**
```java
// 問：以下 Repository 方法會產生什麼 SQL？
List<User> findByNameAndActive(String name, Boolean active);

// 答案：SELECT * FROM user WHERE name = ? AND active = ?
```

#### 9.3.2 事務管理考點 ⭐⭐
**重點：**
- `@Transactional` 屬性
- 事務傳播行為
- 回滾規則
- 唯讀事務優化

### 9.4 安全性考點

#### 9.4.1 Spring Security 基礎 ⭐⭐
**重點：**
- 認證 vs 授權
- JWT 工作原理
- 密碼編碼
- CORS 配置

#### 9.4.2 方法級安全 ⭐
**重點：**
- `@PreAuthorize` 用法
- `@PostAuthorize` 用法
- SpEL 表達式

### 9.5 測試考點

#### 9.5.1 測試註解 ⭐⭐
**重點：**
- `@SpringBootTest` vs `@WebMvcTest`
- `@DataJpaTest` 用法
- `@MockBean` vs `@Mock`
- 測試 Profile

#### 9.5.2 測試最佳實務 ⭐
**重點：**
- 測試金字塔
- 測試隔離
- 測試資料管理

### 9.6 Actuator 與監控 ⭐⭐

**重點：**
- 常用端點功能
- 自定義健康檢查
- 指標收集
- 安全配置

### 9.7 模擬練習題

#### 9.7.1 選擇題練習
**題目 1：**
Spring Boot 中，以下哪個註解用於條件化配置？
A) `@Profile`
B) `@ConditionalOnProperty` 
C) `@Value`
D) `@ConfigurationProperties`

**答案：B**

**題目 2：**
在 Spring Boot 中，預設的嵌入式伺服器是？
A) Jetty
B) Tomcat
C) Undertow
D) Netty

**答案：B**

**題目 3：**
`@Transactional(readOnly = true)` 的主要作用是？
A) 防止資料被修改
B) 效能優化
C) 事務隔離
D) A 和 B

**答案：D**

#### 9.7.2 程式碼分析題
**題目：**
```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    @Autowired
    private UserService userService;
    
    @GetMapping("/{id}")
    public ResponseEntity<User> getUser(@PathVariable Long id) {
        User user = userService.findById(id);
        return ResponseEntity.ok(user);
    }
}
```

**問題：這段程式碼有什麼潛在問題？如何改善？**

**答案：**
1. 使用欄位注入，應改為建構式注入
2. 沒有異常處理，當使用者不存在時會拋出異常
3. 建議使用 `Optional<User>` 處理空值

**改善後：**
```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    private final UserService userService;
    
    public UserController(UserService userService) {
        this.userService = userService;
    }
    
    @GetMapping("/{id}")
    public ResponseEntity<User> getUser(@PathVariable Long id) {
        return userService.findById(id)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }
}
```

### 9.8 考試準備策略

#### 9.8.1 重點複習順序
1. **核心概念** (40%)：自動配置、依賴注入、配置管理
2. **Web 開發** (25%)：RESTful API、資料驗證、異常處理
3. **資料存取** (20%)：JPA、事務管理、Repository
4. **安全性** (10%)：Spring Security 基礎
5. **其他** (5%)：測試、Actuator、部署

#### 9.8.2 實作練習建議
- 建立完整的 CRUD 應用程式
- 實作使用者認證授權
- 撰寫完整的測試用例
- 配置不同環境的設定檔

---

## 10. 常見問題與最佳實務

### 10.1 常見問題 FAQ

#### 10.1.1 啟動相關問題

**Q1: 應用程式啟動失敗，提示 "Consider defining a bean of type..."**
```
A: 這通常是依賴注入問題，檢查：
1. 是否缺少 @Service、@Repository 等註解
2. 包掃描路徑是否正確
3. 是否需要手動配置 Bean
```

**Q2: 連接埠衝突錯誤**
```yaml
# 解決方案：修改 application.yml
server:
  port: 8081  # 或其他可用連接埠
```

#### 10.1.2 資料庫相關問題

**Q3: JPA 實體關係對應錯誤**
```java
// 問題：N+1 查詢問題
@Entity
public class User {
    @OneToMany(mappedBy = "user", fetch = FetchType.LAZY)
    private List<Order> orders;
}

// 解決方案：使用 JOIN FETCH
@Query("SELECT u FROM User u LEFT JOIN FETCH u.orders WHERE u.id = :id")
Optional<User> findByIdWithOrders(@Param("id") Long id);
```

**Q4: 事務不生效**
```java
// 問題：同一類別內部方法呼叫
@Service
public class UserService {
    public void method1() {
        method2(); // 事務不會生效
    }
    
    @Transactional
    public void method2() {
        // 事務邏輯
    }
}

// 解決方案：分離到不同類別或使用 self-injection
```

#### 10.1.3 效能相關問題

**Q5: 應用程式回應緩慢**
```
A: 檢查項目：
1. 資料庫查詢效能（使用 explain）
2. JVM 記憶體設定
3. 連線池配置
4. 快取策略
```

### 10.2 最佳實務總結

#### 10.2.1 程式碼組織
```
✅ 良好實務：
- 按功能分層：controller、service、repository
- 使用 DTO 進行資料傳輸
- 統一的異常處理
- 完整的日誌記錄

❌ 避免的做法：
- 所有邏輯都寫在 Controller
- 直接暴露 Entity 給前端
- 忽略異常處理
- 缺乏日誌記錄
```

#### 10.2.2 安全性最佳實務
```
✅ 良好實務：
- 使用 HTTPS
- 實施適當的認證授權
- 輸入驗證和輸出編碼
- 敏感資訊加密存儲

❌ 避免的做法：
- 明文存儲密碼
- 暴露敏感端點
- 缺乏輸入驗證
- 詳細錯誤資訊洩露
```

#### 10.2.3 效能最佳實務
```
✅ 良好實務：
- 合理使用快取
- 資料庫索引優化
- 連線池調整
- 分頁查詢大量資料

❌ 避免的做法：
- N+1 查詢問題
- 過度的資料獲取
- 缺乏監控指標
- 忽略記憶體洩漏
```

#### 10.2.4 測試最佳實務
```
✅ 良好實務：
- 測試金字塔：更多單元測試，適量整合測試
- 使用測試資料庫
- Mock 外部依賴
- 測試覆蓋率監控

❌ 避免的做法：
- 只寫整合測試
- 測試相互依賴
- 缺乏邊界測試
- 忽略測試維護
```

---

## 11. 檢查清單

### 11.1 開發環境檢查清單

#### ✅ 基礎環境
- [ ] JDK 17+ 安裝並配置 JAVA_HOME
- [ ] Maven 3.6+ 安裝並配置
- [ ] IDE 安裝 (IntelliJ IDEA 或 VS Code)
- [ ] Git 安裝並配置使用者資訊
- [ ] Docker 安裝（可選，用於容器化部署）

#### ✅ 專案初始化
- [ ] 使用 Spring Initializr 建立專案
- [ ] 選擇正確的 Spring Boot 版本
- [ ] 添加必要的 Starter 依賴
- [ ] 配置專案結構
- [ ] 建立 .gitignore 檔案

### 11.2 開發階段檢查清單

#### ✅ 程式碼品質
- [ ] 遵循命名慣例（駝峰式命名）
- [ ] 添加必要的註解（@Service、@Repository 等）
- [ ] 撰寫 JavaDoc 註解
- [ ] 使用建構式注入
- [ ] 實施異常處理

#### ✅ 配置管理
- [ ] 建立不同環境的配置檔案
- [ ] 外部化敏感配置
- [ ] 使用 Profile 管理環境差異
- [ ] 配置資料庫連線池
- [ ] 設定日誌等級和輸出格式

#### ✅ 資料層設計
- [ ] Entity 關係正確對應
- [ ] 添加適當的索引
- [ ] 使用合適的 fetch 策略
- [ ] 實施事務管理
- [ ] 添加資料驗證

#### ✅ Web 層設計
- [ ] RESTful API 設計規範
- [ ] 正確使用 HTTP 狀態碼
- [ ] 實施請求驗證
- [ ] 統一回應格式
- [ ] CORS 配置（如需要）

### 11.3 測試階段檢查清單

#### ✅ 測試策略
- [ ] 撰寫單元測試（Service 層）
- [ ] 撰寫整合測試（Repository 層）
- [ ] 撰寫 API 測試（Controller 層）
- [ ] 測試覆蓋率達到 80% 以上
- [ ] 效能測試（如需要）

#### ✅ 測試品質
- [ ] 測試命名清晰描述
- [ ] 測試資料隔離
- [ ] 使用測試專用配置
- [ ] Mock 外部依賴
- [ ] 邊界條件測試

### 11.4 安全性檢查清單

#### ✅ 基礎安全
- [ ] 實施認證機制
- [ ] 配置授權規則
- [ ] 密碼加密存儲
- [ ] 輸入資料驗證
- [ ] SQL 注入防護

#### ✅ API 安全
- [ ] HTTPS 配置
- [ ] JWT Token 配置
- [ ] API 限流（如需要）
- [ ] 敏感端點保護
- [ ] 錯誤資訊脫敏

### 11.5 部署前檢查清單

#### ✅ 建置配置
- [ ] Maven 建置無錯誤
- [ ] 單元測試全部通過
- [ ] 整合測試全部通過
- [ ] 程式碼靜態分析通過
- [ ] 安全掃描通過

#### ✅ 容器化
- [ ] Dockerfile 最佳實務
- [ ] 多階段建置
- [ ] 非 root 使用者執行
- [ ] 健康檢查配置
- [ ] 資源限制設定

#### ✅ 監控配置
- [ ] Actuator 端點配置
- [ ] 健康檢查實施
- [ ] 指標收集配置
- [ ] 日誌輸出格式
- [ ] 監控告警設定

### 11.6 生產環境檢查清單

#### ✅ 環境配置
- [ ] 生產環境配置檔案
- [ ] 資料庫連線配置
- [ ] 快取配置
- [ ] 外部服務配置
- [ ] 備份策略

#### ✅ 效能優化
- [ ] JVM 記憶體設定
- [ ] 連線池調整
- [ ] 資料庫索引優化
- [ ] 快取策略實施
- [ ] CDN 配置（靜態資源）

#### ✅ 維運準備
- [ ] 部署腳本準備
- [ ] 回滾計畫
- [ ] 監控儀表板
- [ ] 告警規則設定
- [ ] 文件更新

### 11.7 認證考試檢查清單

#### ✅ 知識點複習
- [ ] Spring Boot 核心概念
- [ ] 自動配置原理
- [ ] 依賴注入機制
- [ ] Web 開發基礎
- [ ] 資料存取 (JPA)
- [ ] 安全性 (Spring Security)
- [ ] 測試框架
- [ ] Actuator 監控

#### ✅ 實作練習
- [ ] 建立完整 CRUD 應用
- [ ] 實施使用者認證
- [ ] 撰寫測試用例
- [ ] 配置多環境
- [ ] 部署應用程式

#### ✅ 考試準備
- [ ] 熟悉考試格式
- [ ] 練習選擇題
- [ ] 實作程式碼題目
- [ ] 時間管理練習
- [ ] 模擬考試

---

## 結語

本手冊涵蓋了 Spring Boot 從基礎到進階的所有重要主題，既適合初學者學習，也能幫助有經驗的開發者準備認證考試。建議讀者：

1. **循序漸進學習**：按章節順序學習，每章完成練習題
2. **動手實作**：跟著範例程式碼實際操作
3. **建立專案**：將所學知識整合到完整專案中
4. **持續實踐**：在實際工作中應用所學技術
5. **關注更新**：Spring Boot 版本更新頻繁，保持學習

希望這份手冊能幫助您掌握 Spring Boot 開發技能，並在認證考試中取得好成績！

**文件版本**: 1.0  
**最後更新**: 2025-08-31  
**作者**: 技術團隊  


---

