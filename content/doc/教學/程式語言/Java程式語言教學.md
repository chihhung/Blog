# Java 程式語言教學手冊

## 目錄

1. [Java 語言簡介](#1-java-語言簡介)
   - 1.1 [Java 的歷史與特性](#11-java-的歷史與特性)
   - 1.2 [為什麼專案使用 Java](#12-為什麼專案使用-java)
   - 1.3 [Java 認證路線簡介](#13-java-認證路線簡介)
   - 1.4 [認證考點提醒](#14-認證考點提醒)
   - 1.5 [小練習](#15-小練習)

2. [開發環境與工具](#2-開發環境與工具)
   - 2.1 [JDK 安裝（Java 21）](#21-jdk-安裝java-21)
   - 2.2 [IDE 設定](#22-ide-設定)
   - 2.3 [Build 工具](#23-build-工具)
   - 2.4 [認證考點提醒](#24-認證考點提醒)
   - 2.5 [小練習](#25-小練習)

3. [Java 基礎語法](#3-java-基礎語法)
   - 3.1 [Hello World 程式](#31-hello-world-程式)
   - 3.2 [基本資料型別、變數、常數](#32-基本資料型別變數常數)
   - 3.3 [運算子與型別轉換](#33-運算子與型別轉換)
   - 3.4 [流程控制](#34-流程控制)
   - 3.5 [陣列操作](#35-陣列操作)
   - 3.6 [字串處理](#36-字串處理)
   - 3.7 [認證考點提醒](#37-認證考點提醒)
   - 3.8 [小練習](#38-小練習)

4. [物件導向程式設計 (OOP)](#4-物件導向程式設計-oop)
   - 4.1 [類別與物件](#41-類別與物件)
   - 4.2 [建構子與方法](#42-建構子與方法)
   - 4.3 [繼承 (Inheritance)](#43-繼承-inheritance)
   - 4.4 [多型 (Polymorphism)](#44-多型-polymorphism)
   - 4.5 [封裝 (Encapsulation)](#45-封裝-encapsulation)
   - 4.6 [抽象類別與介面](#46-抽象類別與介面)
   - 4.7 [認證考點提醒](#47-認證考點提醒)
   - 4.8 [小練習](#48-小練習)

5. [核心 API 與工具](#5-核心-api-與工具)
   - 5.1 [集合框架 (Collections Framework)](#51-集合框架-collections-framework)
   - 5.2 [泛型 (Generics)](#52-泛型-generics)
   - 5.3 [日期時間 API](#53-日期時間-api)
   - 5.4 [檔案 I/O 操作](#54-檔案-io-操作)
   - 5.5 [正規表達式](#55-正規表達式)
   - 5.6 [認證考點提醒](#56-認證考點提醒)
   - 5.7 [小練習](#57-小練習)

6. [例外處理與錯誤管理](#6-例外處理與錯誤管理)
   - 6.1 [例外處理機制](#61-例外處理機制)
   - 6.2 [自訂例外](#62-自訂例外)
   - 6.3 [最佳實務](#63-最佳實務)
   - 6.4 [認證考點提醒](#64-認證考點提醒)
   - 6.5 [小練習](#65-小練習)

7. [進階語法與認證內容](#7-進階語法與認證內容)
   - 7.1 [Lambda 表達式](#71-lambda-表達式)
   - 7.2 [Stream API](#72-stream-api)
   - 7.3 [函數式介面](#73-函數式介面)
   - 7.4 [方法參考](#74-方法參考)
   - 7.5 [Optional 類別](#75-optional-類別)
   - 7.6 [Java 模組系統](#76-java-模組系統)
   - 7.7 [Record 類別（Java 14+）](#77-record-類別java-14)
   - 7.8 [Switch 表達式（Java 14+）](#78-switch-表達式java-14)
   - 7.9 [認證考點提醒](#79-認證考點提醒)
   - 7.10 [小練習](#710-小練習)

8. [多執行緒與並行處理](#8-多執行緒與並行處理)
   - 8.1 [執行緒基礎](#81-執行緒基礎)
   - 8.2 [同步機制](#82-同步機制)
   - 8.3 [並行集合](#83-並行集合)
   - 8.4 [Executor 框架](#84-executor-框架)
   - 8.5 [CompletableFuture](#85-completablefuture)
   - 8.6 [執行緒安全與效能](#86-執行緒安全與效能)
   - 8.7 [認證考點提醒](#87-認證考點提醒)
   - 8.8 [小練習](#88-小練習)

9. [專案實務應用](#9-專案實務應用)
   - 9.1 [專案架構設計](#91-專案架構設計)
   - 9.2 [設計模式應用](#92-設計模式應用)
   - 9.3 [單元測試與整合測試](#93-單元測試與整合測試)
   - 9.4 [日誌系統](#94-日誌系統)
   - 9.5 [配置管理](#95-配置管理)
   - 9.6 [資料庫連接與 JPA](#96-資料庫連接與-jpa)
   - 9.7 [RESTful API 開發](#97-restful-api-開發)
   - 9.8 [Spring Boot 入門](#98-spring-boot-入門)
   - 9.9 [微服務基礎](#99-微服務基礎)
   - 9.10 [認證考點提醒](#910-認證考點提醒)
   - 9.11 [小練習](#911-小練習)

10. [認證模擬練習](#10-認證模擬練習)
    - 10.1 [OCA 模擬題目](#101-oca-模擬題目)
    - 10.2 [OCP 模擬題目](#102-ocp-模擬題目)
    - 10.3 [實務應用題目](#103-實務應用題目)
    - 10.4 [考試技巧與策略](#104-考試技巧與策略)
    - 10.5 [錯誤分析與改進](#105-錯誤分析與改進)

11. [最佳實務與專案規範](#11-最佳實務與專案規範)
    - 11.1 [程式碼風格與規範](#111-程式碼風格與規範)
    - 11.2 [效能最佳化](#112-效能最佳化)
    - 11.3 [安全性最佳實務](#113-安全性最佳實務)
    - 11.4 [團隊協作與代碼管理](#114-團隊協作與代碼管理)

12. [附錄](#12-附錄)
    - 12.1 [常用 API 快速參考](#121-常用-api-快速參考)
    - 12.2 [開發工具清單](#122-開發工具清單)
    - 12.3 [學習資源推薦](#123-學習資源推薦)
    - 12.4 [常見問題與疑難排解](#124-常見問題與疑難排解)

13. [檢查清單 (Checklist)](#13-檢查清單-checklist)
    - 13.1 [Java 基礎技能檢查清單](#131-java-基礎技能檢查清單)
    - 13.2 [進階技能檢查清單](#132-進階技能檢查清單)
    - 13.3 [專案開發檢查清單](#133-專案開發檢查清單)
    - 13.4 [認證考試準備檢查清單](#134-認證考試準備檢查清單)
    - 13.5 [持續學習建議](#135-持續學習建議)

14. [新增補充內容](#14-新增補充內容)
    - 14.1 [容器化與雲端部署](#141-容器化與雲端部署)
    - 14.2 [現代 Java 開發工具](#142-現代-java-開發工具)
    - 14.3 [Java 生態系統與框架](#143-java-生態系統與框架)
    - 14.4 [Java 21 新特性深入](#144-java-21-新特性深入)
    - 14.5 [企業級開發模式](#145-企業級開發模式)
    - 14.6 [Java 與 AI/ML 整合](#146-java-與-aiml-整合)
    - 14.7 [ReactiveX 與響應式程式設計](#147-reactivex-與響應式程式設計)

---

## 1. Java 語言簡介

### 1.1 Java 的歷史與特性

Java 是由 Sun Microsystems（現為 Oracle Corporation）於 1995 年發布的程式語言。Java 以其「Write Once, Run Anywhere」（一次撰寫，到處執行）的特性而聞名。

#### 主要特性

- **平台獨立性**：透過 Java Virtual Machine (JVM) 實現跨平台執行
- **物件導向**：完全支援封裝、繼承、多型等 OOP 特性
- **自動記憶體管理**：Garbage Collection 自動回收記憶體
- **安全性**：內建安全機制，防止惡意程式碼執行
- **多執行緒**：原生支援多執行緒程式設計
- **強型別**：編譯時期進行型別檢查，減少執行時錯誤

#### Java 執行環境

```
Java 原始碼 (.java) → 編譯器 (javac) → 位元碼 (.class) → JVM → 機器碼
```

### 1.2 為什麼專案使用 Java

1. **企業級應用支援**
   - 豐富的企業級框架（Spring, Hibernate）
   - 成熟的生態系統
   - 優秀的效能表現

2. **開發效率**
   - 豐富的 API 和函式庫
   - 強大的 IDE 支援
   - 完善的測試工具

3. **維護性與可靠性**
   - 強型別系統減少錯誤
   - 良好的向後相容性
   - 大型社群支援

### 1.3 Java 認證路線簡介

#### Oracle Certified Associate (OCA) - 基礎認證
- **Java SE 8 Programmer I (1Z0-808)**
- 涵蓋：基礎語法、OOP、API 使用

#### Oracle Certified Professional (OCP) - 專業認證
- **Java SE 17 Programmer (1Z0-829)**
- 涵蓋：進階語法、並行處理、模組化、Lambda 表達式

#### 認證考試特色
- **多選題型**：部分題目可能有多個正確答案
- **實務導向**：考題結合實際開發情境
- **陷阱題目**：測試對細節的理解程度

### 1.4 認證考點提醒

⚠️ **常見陷阱**
- 物件初始化順序
- 方法重載 vs 方法覆寫的優先級
- 例外處理的執行順序
- 自動裝箱/拆箱的效能影響

### 1.5 小練習

**練習 1.1**：請說明 Java「一次撰寫，到處執行」的原理。

**解析**：Java 程式碼先編譯成與平台無關的位元碼，再由各平台的 JVM 解釋執行，實現跨平台特性。

---

## 2. 開發環境與工具

### 2.1 JDK 安裝（Java 21）

#### 2.1.1 下載與安裝

1. **官方下載**
   ```
   網址：https://jdk.java.net/21/
   選擇：Windows x64 Installer (msi)
   ```

2. **安裝步驟**
   - 執行下載的 msi 檔案
   - 依照安裝精靈指示進行
   - 預設安裝路徑：`C:\Program Files\Java\jdk-21`

3. **環境變數設定**
   ```powershell
   # 設定 JAVA_HOME
   setx JAVA_HOME "C:\Program Files\Java\jdk-21"
   
   # 將 Java bin 目錄加入 PATH
   setx PATH "%PATH%;%JAVA_HOME%\bin"
   ```

4. **驗證安裝**
   ```powershell
   java -version
   javac -version
   ```

#### 2.1.2 版本管理

**推薦使用 SDKMAN（Linux/Mac）或 scoop（Windows）**
```powershell
# Windows 使用 scoop
scoop install openjdk21
```

### 2.2 IDE 設定

#### 2.2.1 VS Code 設定（推薦給初學者）

1. **必備擴充套件**
   ```
   - Extension Pack for Java
   - Java Test Runner
   - Maven for Java
   - Spring Boot Extension Pack
   ```

2. **VS Code 設定檔（settings.json）**
   ```json
   {
     "java.home": "C:\\Program Files\\Java\\jdk-21",
     "java.configuration.runtimes": [
       {
         "name": "JavaSE-21",
         "path": "C:\\Program Files\\Java\\jdk-21"
       }
     ],
     "java.compile.nullAnalysis.mode": "automatic",
     "java.format.settings.url": "https://raw.githubusercontent.com/google/styleguide/gh-pages/eclipse-java-google-style.xml"
   }
   ```

#### 2.2.2 IntelliJ IDEA 設定（專業開發）

1. **Community Edition 下載**
   ```
   網址：https://www.jetbrains.com/idea/download/
   ```

2. **專案設定**
   - File → Project Structure → Project Settings → Project
   - Project SDK：選擇 Java 21
   - Project language level：21 - Record patterns, pattern matching for switch

### 2.3 Build 工具

#### 2.3.1 Maven 設定

1. **pom.xml 基本設定**
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <project xmlns="http://maven.apache.org/POM/4.0.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
            http://maven.apache.org/xsd/maven-4.0.0.xsd">
       <modelVersion>4.0.0</modelVersion>
       
       <groupId>com.tutorial</groupId>
       <artifactId>java-tutorial</artifactId>
       <version>1.0.0</version>
       <packaging>jar</packaging>
       
       <properties>
           <maven.compiler.source>21</maven.compiler.source>
           <maven.compiler.target>21</maven.compiler.target>
           <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
           <junit.version>5.10.0</junit.version>
       </properties>
       
       <dependencies>
           <!-- JUnit 5 for testing -->
           <dependency>
               <groupId>org.junit.jupiter</groupId>
               <artifactId>junit-jupiter</artifactId>
               <version>${junit.version}</version>
               <scope>test</scope>
           </dependency>
           
           <!-- Logging -->
           <dependency>
               <groupId>org.apache.logging.log4j</groupId>
               <artifactId>log4j-core</artifactId>
               <version>2.20.0</version>
           </dependency>
       </dependencies>
       
       <build>
           <plugins>
               <plugin>
                   <groupId>org.apache.maven.plugins</groupId>
                   <artifactId>maven-compiler-plugin</artifactId>
                   <version>3.11.0</version>
                   <configuration>
                       <source>21</source>
                       <target>21</target>
                   </configuration>
               </plugin>
               
               <plugin>
                   <groupId>org.apache.maven.plugins</groupId>
                   <artifactId>maven-surefire-plugin</artifactId>
                   <version>3.1.2</version>
               </plugin>
           </plugins>
       </build>
   </project>
   ```

2. **常用 Maven 指令**
   ```powershell
   mvn clean compile      # 清理並編譯
   mvn test              # 執行測試
   mvn package           # 打包成 JAR
   mvn exec:java         # 執行主程式
   ```

#### 2.3.2 目錄結構

```
project-root/
├── pom.xml
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/tutorial/
│   │   └── resources/
│   └── test/
│       ├── java/
│       │   └── com/tutorial/
│       └── resources/
├── target/
└── README.md
```

### 2.4 認證考點提醒

⚠️ **環境設定常見問題**
- `CLASSPATH` 設定錯誤導致找不到類別
- 版本不相容問題（編譯 vs 執行版本）
- 套件路徑與目錄結構不一致

### 2.5 小練習

**練習 2.1**：建立一個新的 Maven 專案，並驗證 Java 21 環境是否正確設定。

**練習 2.2**：使用命令列編譯並執行一個簡單的 Hello World 程式。

---

## 3. Java 基礎語法

### 3.1 Hello World 程式

#### 3.1.1 第一個 Java 程式

```java
package com.tutorial.basic;

/**
 * Hello World 程式範例
 * 展示 Java 程式的基本結構
 * 
 * @author Tutorial Team
 * @version 1.0
 */
public class HelloWorld {
    
    /**
     * 主程式進入點
     * @param args 命令列參數
     */
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        System.out.println("歡迎學習 Java 程式設計！");
    }
}
```

#### 3.1.2 程式結構說明

1. **套件宣告（Package Declaration）**
   ```java
   package com.tutorial.basic;
   ```
   - 必須是檔案的第一行（除了註解）
   - 定義類別所屬的套件
   - 對應目錄結構

2. **導入宣告（Import Statements）**
   ```java
   import java.util.Scanner;
   import java.time.LocalDate;
   ```

3. **類別宣告（Class Declaration）**
   ```java
   public class HelloWorld {
       // 類別內容
   }
   ```

4. **main 方法**
   ```java
   public static void main(String[] args) {
       // 程式執行進入點
   }
   ```

#### 3.1.3 編譯與執行

```powershell
# 編譯
javac -d target/classes src/main/java/com/tutorial/basic/HelloWorld.java

# 執行
java -cp target/classes com.tutorial.basic.HelloWorld
```

### 3.2 基本資料型別、變數、常數

#### 3.2.1 基本資料型別

| 型別 | 大小 | 範圍 | 預設值 | 範例 |
|------|------|------|--------|------|
| byte | 8 bits | -128 ~ 127 | 0 | `byte b = 100;` |
| short | 16 bits | -32,768 ~ 32,767 | 0 | `short s = 1000;` |
| int | 32 bits | -2³¹ ~ 2³¹-1 | 0 | `int i = 100000;` |
| long | 64 bits | -2⁶³ ~ 2⁶³-1 | 0L | `long l = 100000L;` |
| float | 32 bits | IEEE 754 | 0.0f | `float f = 3.14f;` |
| double | 64 bits | IEEE 754 | 0.0d | `double d = 3.14159;` |
| char | 16 bits | '\u0000' ~ '\uffff' | '\u0000' | `char c = 'A';` |
| boolean | 1 bit | true/false | false | `boolean flag = true;` |

#### 3.2.2 變數宣告與初始化

```java
public class VariableDemo {
    
    public static void main(String[] args) {
        // 宣告並初始化
        int age = 25;
        double salary = 50000.0;
        String name = "張三";
        boolean isEmployed = true;
        
        // 先宣告後賦值
        int count;
        count = 10;
        
        // 多變數宣告
        int x = 1, y = 2, z = 3;
        
        // 區域變數必須初始化才能使用
        int result;
        // System.out.println(result); // 編譯錯誤！
        result = x + y;
        System.out.println(result); // 正確
    }
}
```

#### 3.2.3 常數宣告

```java
public class ConstantDemo {
    
    // 類別常數（推薦）
    public static final int MAX_SIZE = 100;
    public static final String COMPANY_NAME = "Tutorial Corp";
    public static final double PI = 3.14159;
    
    public static void main(String[] args) {
        // 區域常數
        final int LOCAL_LIMIT = 50;
        
        System.out.println("最大尺寸: " + MAX_SIZE);
        System.out.println("公司名稱: " + COMPANY_NAME);
        
        // LOCAL_LIMIT = 60; // 編譯錯誤！常數不可修改
    }
}
```

#### 3.2.4 變數命名規則

✅ **正確命名**
```java
int studentAge;        // camelCase
String firstName;      // camelCase
final int MAX_COUNT;   // 常數用 UPPER_SNAKE_CASE
boolean isActive;      // boolean 變數常以 is/has 開頭
```

❌ **錯誤命名**
```java
int 2ndValue;          // 不能以數字開頭
String first-name;     // 不能包含連字號
int class;             // 不能使用關鍵字
```

### 3.3 運算子與型別轉換

#### 3.3.1 算術運算子

```java
public class ArithmeticDemo {
    
    public static void main(String[] args) {
        int a = 10, b = 3;
        
        System.out.println("加法: " + (a + b));    // 13
        System.out.println("減法: " + (a - b));    // 7
        System.out.println("乘法: " + (a * b));    // 30
        System.out.println("除法: " + (a / b));    // 3 (整數除法)
        System.out.println("餘數: " + (a % b));    // 1
        
        // 浮點數除法
        double result = (double) a / b;
        System.out.println("浮點除法: " + result); // 3.3333...
        
        // 前綴與後綴運算子
        int x = 5;
        System.out.println("x++: " + (x++)); // 5, x 變成 6
        System.out.println("++x: " + (++x)); // 7, x 變成 7
    }
}
```

#### 3.3.2 比較運算子

```java
public class ComparisonDemo {
    
    public static void main(String[] args) {
        int a = 10, b = 20;
        
        System.out.println("a == b: " + (a == b)); // false
        System.out.println("a != b: " + (a != b)); // true
        System.out.println("a > b: " + (a > b));   // false
        System.out.println("a < b: " + (a < b));   // true
        System.out.println("a >= b: " + (a >= b)); // false
        System.out.println("a <= b: " + (a <= b)); // true
        
        // 字串比較注意事項
        String str1 = "Hello";
        String str2 = "Hello";
        String str3 = new String("Hello");
        
        System.out.println("str1 == str2: " + (str1 == str2));       // true (字串池)
        System.out.println("str1 == str3: " + (str1 == str3));       // false (不同物件)
        System.out.println("str1.equals(str3): " + str1.equals(str3)); // true (內容相同)
    }
}
```

#### 3.3.3 邏輯運算子

```java
public class LogicalDemo {
    
    public static void main(String[] args) {
        boolean x = true, y = false;
        
        System.out.println("x && y: " + (x && y)); // false (且)
        System.out.println("x || y: " + (x || y)); // true (或)
        System.out.println("!x: " + (!x));         // false (非)
        
        // 短路求值
        int a = 0;
        if (a != 0 && (10 / a) > 1) { // 第二個條件不會執行
            System.out.println("不會執行");
        }
        
        // 三元運算子
        int max = (a > b) ? a : b;
        String status = (age >= 18) ? "成年" : "未成年";
    }
}
```

#### 3.3.4 型別轉換

```java
public class TypeConversionDemo {
    
    public static void main(String[] args) {
        // 隱式轉換（Widening）
        int intValue = 100;
        long longValue = intValue;     // int → long
        double doubleValue = intValue; // int → double
        
        // 明式轉換（Narrowing）
        double d = 9.78;
        int i = (int) d;               // 9 (小數部分會被截斷)
        
        // 字串轉數字
        String numStr = "123";
        int num = Integer.parseInt(numStr);
        double dNum = Double.parseDouble("123.45");
        
        // 數字轉字串
        String intStr = String.valueOf(123);
        String doubleStr = Double.toString(123.45);
        
        // 型別提升範例（認證重點）
        byte b1 = 10, b2 = 20;
        // byte result = b1 + b2; // 編譯錯誤！運算結果提升為 int
        int result = b1 + b2;     // 正確
        
        // char 運算
        char c1 = 'A';
        char c2 = 'B';
        int asciiSum = c1 + c2;   // 65 + 66 = 131
    }
}
```

### 3.4 流程控制

#### 3.4.1 條件判斷 (if-else)

```java
public class IfElseDemo {
    
    public static void main(String[] args) {
        int score = 85;
        
        // 基本 if-else
        if (score >= 90) {
            System.out.println("優秀");
        } else if (score >= 80) {
            System.out.println("良好");
        } else if (score >= 70) {
            System.out.println("及格");
        } else {
            System.out.println("不及格");
        }
        
        // 巢狀 if
        boolean isStudent = true;
        int age = 20;
        
        if (isStudent) {
            if (age < 18) {
                System.out.println("未成年學生");
            } else {
                System.out.println("成年學生");
            }
        } else {
            System.out.println("非學生");
        }
        
        // 多條件判斷
        String weather = "sunny";
        int temperature = 25;
        
        if (weather.equals("sunny") && temperature > 20) {
            System.out.println("適合戶外活動");
        } else if (weather.equals("rainy") || temperature < 10) {
            System.out.println("建議室內活動");
        }
    }
}
```

#### 3.4.2 Switch 語句

```java
public class SwitchDemo {
    
    public static void main(String[] args) {
        // 傳統 switch（Java 17 之前）
        int dayOfWeek = 3;
        String dayName;
        
        switch (dayOfWeek) {
            case 1:
                dayName = "星期一";
                break;
            case 2:
                dayName = "星期二";
                break;
            case 3:
                dayName = "星期三";
                break;
            case 4:
                dayName = "星期四";
                break;
            case 5:
                dayName = "星期五";
                break;
            case 6:
            case 7:
                dayName = "週末";
                break;
            default:
                dayName = "無效的日期";
        }
        
        // Switch 表達式（Java 14+，認證重點）
        String dayType = switch (dayOfWeek) {
            case 1, 2, 3, 4, 5 -> "工作日";
            case 6, 7 -> "週末";
            default -> "無效";
        };
        
        // 字串 switch（Java 7+，認證常考）
        String grade = "A";
        int gpa = switch (grade) {
            case "A" -> 4;
            case "B" -> 3;
            case "C" -> 2;
            case "D" -> 1;
            case "F" -> 0;
            default -> throw new IllegalArgumentException("無效成績: " + grade);
        };
        
        // Enum switch
        Status status = Status.ACTIVE;
        String message = switch (status) {
            case ACTIVE -> "用戶活躍";
            case INACTIVE -> "用戶非活躍";
            case SUSPENDED -> "用戶已暫停";
        };
    }
    
    enum Status {
        ACTIVE, INACTIVE, SUSPENDED
    }
}
```

#### 3.4.3 迴圈控制

```java
public class LoopDemo {
    
    public static void main(String[] args) {
        // for 迴圈
        System.out.println("=== For 迴圈 ===");
        for (int i = 1; i <= 5; i++) {
            System.out.println("計數: " + i);
        }
        
        // 增強型 for 迴圈（for-each）
        int[] numbers = {1, 2, 3, 4, 5};
        System.out.println("=== Enhanced For 迴圈 ===");
        for (int num : numbers) {
            System.out.println("數字: " + num);
        }
        
        // while 迴圈
        System.out.println("=== While 迴圈 ===");
        int count = 1;
        while (count <= 3) {
            System.out.println("While 計數: " + count);
            count++;
        }
        
        // do-while 迴圈
        System.out.println("=== Do-While 迴圈 ===");
        int doCount = 1;
        do {
            System.out.println("Do-While 計數: " + doCount);
            doCount++;
        } while (doCount <= 3);
        
        // 巢狀迴圈
        System.out.println("=== 九九乘法表 ===");
        for (int i = 1; i <= 9; i++) {
            for (int j = 1; j <= 9; j++) {
                System.out.printf("%d×%d=%d ", i, j, i * j);
            }
            System.out.println();
        }
        
        // break 和 continue
        System.out.println("=== Break 和 Continue ===");
        for (int i = 1; i <= 10; i++) {
            if (i == 3) {
                continue; // 跳過當前迭代
            }
            if (i == 8) {
                break; // 結束迴圈
            }
            System.out.println("處理: " + i);
        }
        
        // 標籤 break（認證可能考點）
        outer: for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 3; j++) {
                if (i == 2 && j == 2) {
                    break outer; // 跳出外層迴圈
                }
                System.out.println("i=" + i + ", j=" + j);
            }
        }
    }
}
```

### 3.5 陣列操作

#### 3.5.1 一維陣列

```java
public class ArrayDemo {
    
    public static void main(String[] args) {
        // 陣列宣告與初始化
        int[] numbers1 = new int[5];           // 建立長度為5的陣列
        int[] numbers2 = {1, 2, 3, 4, 5};      // 直接初始化
        int[] numbers3 = new int[]{1, 2, 3};   // 另一種初始化方式
        
        // 陣列賦值
        numbers1[0] = 10;
        numbers1[1] = 20;
        
        // 陣列長度
        System.out.println("陣列長度: " + numbers1.length);
        
        // 陣列走訪
        System.out.println("=== 使用 for 迴圈 ===");
        for (int i = 0; i < numbers2.length; i++) {
            System.out.println("索引 " + i + ": " + numbers2[i]);
        }
        
        System.out.println("=== 使用 enhanced for 迴圈 ===");
        for (int num : numbers2) {
            System.out.println("值: " + num);
        }
        
        // 陣列常見操作
        int[] arr = {5, 2, 8, 1, 9};
        
        // 找最大值
        int max = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        System.out.println("最大值: " + max);
        
        // 計算總和
        int sum = 0;
        for (int num : arr) {
            sum += num;
        }
        System.out.println("總和: " + sum);
        
        // 陣列複製
        int[] original = {1, 2, 3};
        int[] copy1 = original.clone();                    // 淺複製
        int[] copy2 = new int[original.length];
        System.arraycopy(original, 0, copy2, 0, original.length);
    }
}
```

#### 3.5.2 多維陣列

```java
public class MultiArrayDemo {
    
    public static void main(String[] args) {
        // 二維陣列宣告
        int[][] matrix1 = new int[3][4];           // 3列4行
        int[][] matrix2 = {{1, 2}, {3, 4}, {5, 6}}; // 直接初始化
        
        // 不規則陣列（Jagged Array）
        int[][] jagged = new int[3][];
        jagged[0] = new int[2];
        jagged[1] = new int[3];
        jagged[2] = new int[4];
        
        // 二維陣列走訪
        System.out.println("=== 二維陣列走訪 ===");
        for (int i = 0; i < matrix2.length; i++) {
            for (int j = 0; j < matrix2[i].length; j++) {
                System.out.print(matrix2[i][j] + " ");
            }
            System.out.println();
        }
        
        // 使用 enhanced for
        System.out.println("=== Enhanced For 走訪 ===");
        for (int[] row : matrix2) {
            for (int value : row) {
                System.out.print(value + " ");
            }
            System.out.println();
        }
        
        // 三維陣列範例
        int[][][] cube = new int[2][3][4];
        cube[0][1][2] = 100;
        
        System.out.println("三維陣列值: " + cube[0][1][2]);
    }
}
```

#### 3.5.3 陣列與記憶體

```java
public class ArrayMemoryDemo {
    
    public static void main(String[] args) {
        // 陣列是參考型別
        int[] arr1 = {1, 2, 3};
        int[] arr2 = arr1;    // 指向同一個陣列物件
        
        arr2[0] = 100;
        System.out.println("arr1[0]: " + arr1[0]); // 100，因為指向同一物件
        
        // 陣列比較
        int[] array1 = {1, 2, 3};
        int[] array2 = {1, 2, 3};
        
        System.out.println("== 比較: " + (array1 == array2));           // false
        System.out.println("Arrays.equals: " + 
            java.util.Arrays.equals(array1, array2));                   // true
        
        // 陣列作為方法參數
        modifyArray(arr1);
        System.out.println("修改後 arr1[0]: " + arr1[0]); // 999
        
        // 可變長度參數（Varargs）
        printNumbers(1, 2, 3, 4, 5);
        printNumbers(); // 空陣列
    }
    
    public static void modifyArray(int[] array) {
        array[0] = 999; // 會影響原陣列
    }
    
    public static void printNumbers(int... numbers) {
        System.out.println("數字個數: " + numbers.length);
        for (int num : numbers) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
```

### 3.6 字串處理

#### 3.6.1 字串基礎操作

```java
public class StringDemo {
    
    public static void main(String[] args) {
        // 字串建立方式
        String str1 = "Hello";              // 字串常數池
        String str2 = new String("Hello");  // 堆積記憶體
        String str3 = "Hello";              // 指向常數池中的同一個物件
        
        // 字串比較（認證重點！）
        System.out.println("str1 == str2: " + (str1 == str2));       // false
        System.out.println("str1 == str3: " + (str1 == str3));       // true
        System.out.println("str1.equals(str2): " + str1.equals(str2)); // true
        
        // 基本字串方法
        String text = "Java Programming";
        
        System.out.println("長度: " + text.length());                    // 16
        System.out.println("字元: " + text.charAt(0));                   // J
        System.out.println("子字串: " + text.substring(5));              // Programming
        System.out.println("子字串: " + text.substring(0, 4));           // Java
        System.out.println("索引: " + text.indexOf("Pro"));              // 5
        System.out.println("最後索引: " + text.lastIndexOf("a"));        // 3
        
        // 字串轉換
        System.out.println("大寫: " + text.toUpperCase());
        System.out.println("小寫: " + text.toLowerCase());
        System.out.println("替換: " + text.replace("Java", "Python"));
        
        // 字串檢查
        String email = "user@example.com";
        System.out.println("開頭: " + email.startsWith("user"));         // true
        System.out.println("結尾: " + email.endsWith(".com"));           // true
        System.out.println("包含: " + email.contains("@"));              // true
        System.out.println("空字串: " + "".isEmpty());                   // true
        System.out.println("空白: " + "   ".trim().isEmpty());           // true
        
        // 字串分割
        String csvData = "apple,banana,orange";
        String[] fruits = csvData.split(",");
        for (String fruit : fruits) {
            System.out.println("水果: " + fruit);
        }
    }
}
```

#### 3.6.2 StringBuilder 與 StringBuffer

```java
public class StringBuilderDemo {
    
    public static void main(String[] args) {
        // 字串連接效能問題
        System.out.println("=== 字串連接效能比較 ===");
        
        // 低效率方式（會建立很多中間字串物件）
        long start = System.currentTimeMillis();
        String result = "";
        for (int i = 0; i < 10000; i++) {
            result += "a";
        }
        long end = System.currentTimeMillis();
        System.out.println("String 連接時間: " + (end - start) + "ms");
        
        // 高效率方式
        start = System.currentTimeMillis();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 10000; i++) {
            sb.append("a");
        }
        String sbResult = sb.toString();
        end = System.currentTimeMillis();
        System.out.println("StringBuilder 時間: " + (end - start) + "ms");
        
        // StringBuilder 常用方法
        StringBuilder builder = new StringBuilder("Hello");
        
        builder.append(" World");                    // HelloWorld
        builder.insert(5, ",");                      // Hello, World
        builder.replace(7, 12, "Java");              // Hello, Java
        builder.delete(5, 6);                        // HelloJava
        builder.reverse();                           // avaJolleH
        
        System.out.println("最終結果: " + builder.toString());
        
        // StringBuffer vs StringBuilder
        // StringBuffer: 執行緒安全，但效能較慢
        // StringBuilder: 非執行緒安全，但效能較快（推薦單執行緒使用）
        
        StringBuffer buffer = new StringBuffer("Thread Safe");
        StringBuilder stringBuilder = new StringBuilder("Faster");
    }
}
```

#### 3.6.3 字串格式化

```java
public class StringFormatDemo {
    
    public static void main(String[] args) {
        // printf 風格格式化
        String name = "張三";
        int age = 25;
        double salary = 50000.5;
        
        System.out.printf("姓名: %s, 年齡: %d, 薪水: %.2f%n", name, age, salary);
        
        // String.format 方法
        String formatted = String.format("Hello %s, you are %d years old", name, age);
        System.out.println(formatted);
        
        // 常用格式說明符
        int number = 42;
        System.out.printf("十進位: %d%n", number);        // 42
        System.out.printf("十六進位: %x%n", number);      // 2a
        System.out.printf("八進位: %o%n", number);        // 52
        System.out.printf("二進位: %s%n", Integer.toBinaryString(number)); // 101010
        
        double pi = 3.14159;
        System.out.printf("浮點數: %.2f%n", pi);          // 3.14
        System.out.printf("科學記號: %.2e%n", pi);        // 3.14e+00
        
        // 對齊與寬度
        System.out.printf("右對齊: %10s%n", "Hello");      // "     Hello"
        System.out.printf("左對齊: %-10s%n", "Hello");     // "Hello     "
        System.out.printf("補零: %05d%n", 42);            // "00042"
        
        // Text Blocks (Java 15+)
        String html = """
                      <html>
                          <head>
                              <title>Test</title>
                          </head>
                          <body>
                              <h1>Hello, World!</h1>
                          </body>
                      </html>
                      """;
        System.out.println(html);
    }
}
```

#### 3.6.4 正規表達式基礎

```java
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class RegexDemo {
    
    public static void main(String[] args) {
        // 基本字串匹配
        String email = "user@example.com";
        boolean isValidEmail = email.matches("\\w+@\\w+\\.\\w+");
        System.out.println("Email 有效: " + isValidEmail);
        
        // 常用驗證模式
        String phone = "0912-345-678";
        boolean isValidPhone = phone.matches("\\d{4}-\\d{3}-\\d{3}");
        System.out.println("電話有效: " + isValidPhone);
        
        // Pattern 與 Matcher
        String text = "Java 8, Java 11, Java 17, Java 21";
        Pattern pattern = Pattern.compile("Java \\d+");
        Matcher matcher = pattern.matcher(text);
        
        System.out.println("找到的版本:");
        while (matcher.find()) {
            System.out.println("- " + matcher.group());
        }
        
        // 字串替換
        String result = text.replaceAll("Java (\\d+)", "JDK $1");
        System.out.println("替換結果: " + result);
        
        // 字串分割
        String data = "apple;banana;orange";
        String[] items = data.split(";");
        for (String item : items) {
            System.out.println("項目: " + item);
        }
    }
}
```

### 3.7 認證考點提醒

#### 3.7.1 Switch 搭配字串陷阱

```java
public class SwitchTraps {
    
    public static void main(String[] args) {
        // 陷阱 1: null 值
        String value = null;
        switch (value) { // NullPointerException!
            case "A" -> System.out.println("A");
            default -> System.out.println("其他");
        }
        
        // 陷阱 2: 大小寫敏感
        String grade = "a";
        switch (grade) {
            case "A" -> System.out.println("優秀"); // 不會執行
            case "a" -> System.out.println("優秀"); // 會執行
        }
        
        // 陷阱 3: break 遺漏
        int day = 1;
        switch (day) {
            case 1:
                System.out.println("星期一");
                // 沒有 break，會繼續執行下一個 case
            case 2:
                System.out.println("星期二");
                break;
        }
        // 輸出：星期一\n星期二
    }
}
```

#### 3.7.2 型別提升規則

```java
public class TypePromotionTraps {
    
    public static void main(String[] args) {
        // 陷阱 1: byte/short 運算提升為 int
        byte b1 = 10, b2 = 20;
        // byte result = b1 + b2; // 編譯錯誤
        int result = b1 + b2;     // 正確
        
        // 陷阱 2: char 運算
        char c = 'A';
        c++; // 正確，單元運算子不會提升
        // c = c + 1; // 編譯錯誤，右邊提升為 int
        c = (char) (c + 1); // 需要強制轉換
        
        // 陷阱 3: 浮點數精度
        double d1 = 0.1;
        double d2 = 0.2;
        double sum = d1 + d2;
        System.out.println(sum == 0.3); // false!
        System.out.println(sum); // 0.30000000000000004
        
        // 正確的浮點數比較
        double epsilon = 1e-9;
        System.out.println(Math.abs(sum - 0.3) < epsilon); // true
    }
}
```

#### 3.7.3 陣列與字串陷阱

```java
public class ArrayStringTraps {
    
    public static void main(String[] args) {
        // 陷阱 1: 陣列邊界
        int[] arr = {1, 2, 3};
        // System.out.println(arr[3]); // ArrayIndexOutOfBoundsException
        
        // 陷阱 2: 陣列比較
        int[] arr1 = {1, 2, 3};
        int[] arr2 = {1, 2, 3};
        System.out.println(arr1 == arr2);                    // false
        System.out.println(Arrays.equals(arr1, arr2));       // true
        
        // 陷阱 3: 字串比較
        String s1 = "hello";
        String s2 = "hello";
        String s3 = new String("hello");
        System.out.println(s1 == s2);       // true (字串池)
        System.out.println(s1 == s3);       // false
        System.out.println(s1.equals(s3));  // true
        
        // 陷阱 4: 字串不可變性
        String str = "Hello";
        str.toUpperCase(); // 沒有賦值，原字串不變
        System.out.println(str); // "Hello"
        
        str = str.toUpperCase(); // 正確做法
        System.out.println(str); // "HELLO"
    }
}
```

### 3.8 小練習

### 3.8 小練習

**練習 3.1**：以下程式碼的輸出結果是什麼？
```java
int x = 5;
System.out.println(x++ + ++x);
```

**解析**：
- `x++`：使用後自增，先返回 5，然後 x 變成 6
- `++x`：使用前自增，x 先變成 7，然後返回 7
- 結果：5 + 7 = 12

**練習 3.2**：這段程式碼是否能編譯成功？
```java
final int x;
if (Math.random() > 0.5) {
    x = 10;
} else {
    x = 20;
}
System.out.println(x);
```

**解析**：能編譯成功。雖然 x 是 final，但在所有可能的執行路徑中都有初始化，符合「明確賦值」規則。

**練習 3.3**：陣列練習
```java
int[] arr = {1, 2, 3, 4, 5};
// 請寫程式計算陣列的平均值
```

**解析**：
```java
double sum = 0;
for (int num : arr) {
    sum += num;
}
double average = sum / arr.length;
System.out.println("平均值: " + average); // 3.0
```

**練習 3.4**：字串操作練習
```java
String email = "USER@EXAMPLE.COM";
// 請將 email 轉換成小寫，並檢查是否包含 "@" 符號
```

**解析**：
```java
String lowerEmail = email.toLowerCase();
boolean hasAtSymbol = lowerEmail.contains("@");
System.out.println("小寫 email: " + lowerEmail);
System.out.println("包含 @: " + hasAtSymbol);
```

**練習 3.5**：Switch 表達式練習（Java 14+）
```java
// 使用 Switch 表達式將數字轉換為對應的星期
int dayNumber = 3;
// 1=星期一, 2=星期二, ..., 7=星期日
```

**解析**：
```java
String dayName = switch (dayNumber) {
    case 1 -> "星期一";
    case 2 -> "星期二";
    case 3 -> "星期三";
    case 4 -> "星期四";
    case 5 -> "星期五";
    case 6 -> "星期六";
    case 7 -> "星期日";
    default -> "無效的日期";
};
System.out.println(dayName); // 星期三
```

---

## 4. 物件導向程式設計 (OOP)

### 4.1 類別與物件

#### 4.1.1 類別的定義

類別（Class）是物件的藍圖或模板，定義了物件的屬性和行為。

```java
package com.tutorial.oop;

/**
 * 學生類別範例
 * 展示類別的基本結構與成員
 */
public class Student {
    
    // 實例變數（屬性）
    private String name;
    private int age;
    private String studentId;
    private double gpa;
    
    // 類別變數（靜態變數）
    private static int totalStudents = 0;
    
    // 常數
    public static final double MAX_GPA = 4.0;
    
    // 預設建構子
    public Student() {
        this("Unknown", 0, "0000");
    }
    
    // 參數化建構子
    public Student(String name, int age, String studentId) {
        this.name = name;
        this.age = age;
        this.studentId = studentId;
        this.gpa = 0.0;
        totalStudents++;
    }
    
    // 完整建構子
    public Student(String name, int age, String studentId, double gpa) {
        this(name, age, studentId);
        setGpa(gpa);
    }
    
    // Getter 方法
    public String getName() {
        return name;
    }
    
    public int getAge() {
        return age;
    }
    
    public String getStudentId() {
        return studentId;
    }
    
    public double getGpa() {
        return gpa;
    }
    
    // Setter 方法
    public void setName(String name) {
        if (name != null && !name.trim().isEmpty()) {
            this.name = name;
        }
    }
    
    public void setAge(int age) {
        if (age >= 0 && age <= 150) {
            this.age = age;
        }
    }
    
    public void setGpa(double gpa) {
        if (gpa >= 0.0 && gpa <= MAX_GPA) {
            this.gpa = gpa;
        }
    }
    
    // 實例方法
    public void study(String subject) {
        System.out.println(name + " 正在學習 " + subject);
    }
    
    public boolean isHonorStudent() {
        return gpa >= 3.5;
    }
    
    // 靜態方法
    public static int getTotalStudents() {
        return totalStudents;
    }
    
    public static Student createHonorStudent(String name, int age, String studentId) {
        Student student = new Student(name, age, studentId);
        student.setGpa(3.8);
        return student;
    }
    
    // toString 方法（物件的字串表示）
    @Override
    public String toString() {
        return String.format("Student{name='%s', age=%d, studentId='%s', gpa=%.2f}", 
                           name, age, studentId, gpa);
    }
    
    // equals 和 hashCode 方法
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        
        Student student = (Student) obj;
        return studentId.equals(student.studentId);
    }
    
    @Override
    public int hashCode() {
        return studentId.hashCode();
    }
}
```

#### 4.1.2 物件的建立與使用

```java
public class StudentDemo {
    
    public static void main(String[] args) {
        // 建立物件
        Student student1 = new Student();
        Student student2 = new Student("張三", 20, "S001");
        Student student3 = new Student("李四", 21, "S002", 3.7);
        
        // 使用物件
        student1.setName("王五");
        student1.setAge(19);
        student1.setGpa(3.2);
        
        // 呼叫方法
        student2.study("Java 程式設計");
        System.out.println(student3.getName() + " 是否為榮譽學生: " + student3.isHonorStudent());
        
        // 靜態方法呼叫
        System.out.println("總學生數: " + Student.getTotalStudents());
        
        // 工廠方法
        Student honorStudent = Student.createHonorStudent("趙六", 22, "S003");
        
        // 物件比較
        Student duplicateStudent = new Student("張三", 25, "S001", 2.8);
        System.out.println("student2 equals duplicateStudent: " + student2.equals(duplicateStudent));
        
        // 輸出物件資訊
        System.out.println(student1);
        System.out.println(student2);
        System.out.println(student3);
    }
}
```

### 4.2 建構子與初始化順序

#### 4.2.1 建構子類型

```java
public class Constructor Demo {
    
    private String name;
    private int value;
    private static int count = 0;
    
    // 靜態初始化區塊
    static {
        System.out.println("靜態初始化區塊執行");
        count = 100;
    }
    
    // 實例初始化區塊
    {
        System.out.println("實例初始化區塊執行");
        this.name = "預設名稱";
    }
    
    // 預設建構子
    public ConstructorDemo() {
        System.out.println("預設建構子執行");
        this.value = 0;
    }
    
    // 參數化建構子
    public ConstructorDemo(String name) {
        System.out.println("參數化建構子執行");
        this.name = name;
        this.value = 10;
    }
    
    // 建構子鏈接
    public ConstructorDemo(String name, int value) {
        this(name); // 呼叫其他建構子
        System.out.println("完整建構子執行");
        this.value = value;
    }
}
```

#### 4.2.2 初始化順序（認證重點）

```java
public class InitializationOrder {
    
    public static void main(String[] args) {
        System.out.println("=== 第一次建立物件 ===");
        ConstructorDemo obj1 = new ConstructorDemo("測試", 50);
        
        System.out.println("\n=== 第二次建立物件 ===");
        ConstructorDemo obj2 = new ConstructorDemo();
    }
}

// 執行順序：
// 1. 靜態初始化區塊（只執行一次）
// 2. 實例初始化區塊
// 3. 建構子
```

### 4.3 方法（Overloading vs Overriding）

#### 4.3.1 方法重載（Method Overloading）

```java
public class Calculator {
    
    // 基本加法
    public int add(int a, int b) {
        return a + b;
    }
    
    // 三個整數相加
    public int add(int a, int b, int c) {
        return a + b + c;
    }
    
    // 浮點數相加
    public double add(double a, double b) {
        return a + b;
    }
    
    // 字串連接
    public String add(String a, String b) {
        return a + b;
    }
    
    // 陣列元素相加
    public int add(int[] numbers) {
        int sum = 0;
        for (int num : numbers) {
            sum += num;
        }
        return sum;
    }
    
    // 可變參數
    public int add(int... numbers) {
        int sum = 0;
        for (int num : numbers) {
            sum += num;
        }
        return sum;
    }
    
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        
        System.out.println(calc.add(1, 2));              // 3
        System.out.println(calc.add(1, 2, 3));           // 6
        System.out.println(calc.add(1.5, 2.5));          // 4.0
        System.out.println(calc.add("Hello", "World"));   // HelloWorld
        System.out.println(calc.add(new int[]{1, 2, 3, 4})); // 10
        System.out.println(calc.add(1, 2, 3, 4, 5));     // 15 (可變參數)
    }
}
```

#### 4.3.2 方法覆寫（Method Overriding）

```java
// 父類別
class Animal {
    protected String name;
    
    public Animal(String name) {
        this.name = name;
    }
    
    public void makeSound() {
        System.out.println(name + " 發出聲音");
    }
    
    public void move() {
        System.out.println(name + " 正在移動");
    }
    
    // final 方法不能被覆寫
    public final void breathe() {
        System.out.println(name + " 正在呼吸");
    }
}

// 子類別
class Dog extends Animal {
    
    public Dog(String name) {
        super(name);
    }
    
    // 覆寫父類別方法
    @Override
    public void makeSound() {
        System.out.println(name + " 汪汪叫");
    }
    
    @Override
    public void move() {
        System.out.println(name + " 跑步");
    }
    
    // 新增方法
    public void wagTail() {
        System.out.println(name + " 搖尾巴");
    }
}

class Cat extends Animal {
    
    public Cat(String name) {
        super(name);
    }
    
    @Override
    public void makeSound() {
        System.out.println(name + " 喵喵叫");
    }
    
    @Override
    public void move() {
        System.out.println(name + " 優雅地走路");
    }
}
```

### 4.4 封裝、繼承、多型

#### 4.4.1 封裝（Encapsulation）

```java
public class BankAccount {
    
    // 私有屬性
    private String accountNumber;
    private String ownerName;
    private double balance;
    private boolean isActive;
    
    // 建構子
    public BankAccount(String accountNumber, String ownerName, double initialBalance) {
        this.accountNumber = accountNumber;
        this.ownerName = ownerName;
        this.balance = initialBalance >= 0 ? initialBalance : 0;
        this.isActive = true;
    }
    
    // 公開的存款方法
    public boolean deposit(double amount) {
        if (amount > 0 && isActive) {
            balance += amount;
            System.out.println("存款成功，當前餘額: " + balance);
            return true;
        }
        System.out.println("存款失敗：金額無效或帳戶未啟用");
        return false;
    }
    
    // 公開的提款方法
    public boolean withdraw(double amount) {
        if (amount > 0 && amount <= balance && isActive) {
            balance -= amount;
            System.out.println("提款成功，當前餘額: " + balance);
            return true;
        }
        System.out.println("提款失敗：餘額不足、金額無效或帳戶未啟用");
        return false;
    }
    
    // 只讀屬性
    public double getBalance() {
        return isActive ? balance : 0;
    }
    
    public String getAccountNumber() {
        return accountNumber;
    }
    
    public String getOwnerName() {
        return ownerName;
    }
    
    public boolean isActive() {
        return isActive;
    }
    
    // 受保護的帳戶操作
    protected void setActive(boolean active) {
        this.isActive = active;
    }
    
    // 私有輔助方法
    private boolean validateTransaction(double amount) {
        return amount > 0 && isActive;
    }
}
```

#### 4.4.2 繼承（Inheritance）

```java
// 基礎帳戶類別
class BasicAccount extends BankAccount {
    
    public BasicAccount(String accountNumber, String ownerName, double initialBalance) {
        super(accountNumber, ownerName, initialBalance);
    }
    
    // 基礎帳戶沒有利息
    public void calculateInterest() {
        System.out.println("基礎帳戶不提供利息");
    }
}

// 儲蓄帳戶類別
class SavingsAccount extends BankAccount {
    
    private double interestRate;
    private int withdrawalCount;
    private static final int MAX_WITHDRAWALS = 3;
    
    public SavingsAccount(String accountNumber, String ownerName, 
                         double initialBalance, double interestRate) {
        super(accountNumber, ownerName, initialBalance);
        this.interestRate = interestRate;
        this.withdrawalCount = 0;
    }
    
    @Override
    public boolean withdraw(double amount) {
        if (withdrawalCount >= MAX_WITHDRAWALS) {
            System.out.println("提款失敗：已達每月提款次數上限");
            return false;
        }
        
        if (super.withdraw(amount)) {
            withdrawalCount++;
            return true;
        }
        return false;
    }
    
    public void calculateInterest() {
        double interest = getBalance() * interestRate / 100;
        deposit(interest);
        System.out.println("利息計算完成，利息金額: " + interest);
    }
    
    public void resetMonthlyWithdrawals() {
        withdrawalCount = 0;
        System.out.println("每月提款次數已重置");
    }
}

// 信用帳戶類別
class CreditAccount extends BankAccount {
    
    private double creditLimit;
    private double creditUsed;
    
    public CreditAccount(String accountNumber, String ownerName, double creditLimit) {
        super(accountNumber, ownerName, 0); // 信用帳戶初始餘額為 0
        this.creditLimit = creditLimit;
        this.creditUsed = 0;
    }
    
    @Override
    public boolean withdraw(double amount) {
        double availableCredit = creditLimit - creditUsed;
        if (amount > 0 && amount <= (getBalance() + availableCredit) && isActive()) {
            if (amount <= getBalance()) {
                // 使用現金餘額
                return super.withdraw(amount);
            } else {
                // 使用信用額度
                double cashUsed = getBalance();
                double creditNeeded = amount - cashUsed;
                
                if (cashUsed > 0) {
                    super.withdraw(cashUsed);
                }
                creditUsed += creditNeeded;
                
                System.out.println("信用提款成功，信用額度使用: " + creditUsed + "/" + creditLimit);
                return true;
            }
        }
        System.out.println("提款失敗：超過信用額度或帳戶未啟用");
        return false;
    }
    
    public double getAvailableCredit() {
        return creditLimit - creditUsed;
    }
    
    public boolean payCredit(double amount) {
        if (amount > 0 && amount <= creditUsed) {
            creditUsed -= amount;
            System.out.println("信用還款成功，剩餘債務: " + creditUsed);
            return true;
        }
        System.out.println("還款失敗：金額無效");
        return false;
    }
}
```

#### 4.4.3 多型（Polymorphism）

```java
public class PolymorphismDemo {
    
    public static void main(String[] args) {
        // 多型陣列
        BankAccount[] accounts = {
            new BasicAccount("B001", "張三", 1000),
            new SavingsAccount("S001", "李四", 2000, 2.5),
            new CreditAccount("C001", "王五", 5000)
        };
        
        // 多型方法呼叫
        for (BankAccount account : accounts) {
            System.out.println("\n帳戶: " + account.getAccountNumber());
            System.out.println("擁有者: " + account.getOwnerName());
            System.out.println("餘額: " + account.getBalance());
            
            // 每個子類別都有不同的實作
            account.deposit(100);
            account.withdraw(50);
            
            // 執行時期型別檢查
            if (account instanceof SavingsAccount) {
                SavingsAccount savings = (SavingsAccount) account;
                savings.calculateInterest();
            } else if (account instanceof CreditAccount) {
                CreditAccount credit = (CreditAccount) account;
                System.out.println("可用信用額度: " + credit.getAvailableCredit());
            }
        }
        
        // 方法參數多型
        processAccount(new BasicAccount("B002", "趙六", 500));
        processAccount(new SavingsAccount("S002", "錢七", 1500, 3.0));
    }
    
    // 多型參數方法
    public static void processAccount(BankAccount account) {
        System.out.println("\n處理帳戶: " + account.getClass().getSimpleName());
        account.deposit(200);
        
        // Pattern Matching (Java 17+)
        switch (account) {
            case SavingsAccount sa -> sa.calculateInterest();
            case CreditAccount ca -> System.out.println("信用額度: " + ca.getAvailableCredit());
            default -> System.out.println("基礎帳戶處理完成");
        }
    }
}
```

### 4.5 介面與抽象類別

#### 4.5.1 介面定義與實作

```java
// 支付介面
public interface Payable {
    
    // 常數（隱含 public static final）
    double TAX_RATE = 0.05;
    
    // 抽象方法（隱含 public abstract）
    boolean processPayment(double amount);
    String getPaymentMethod();
    
    // 預設方法（Java 8+）
    default double calculateTax(double amount) {
        return amount * TAX_RATE;
    }
    
    default void printReceipt(double amount) {
        System.out.println("=== 付款收據 ===");
        System.out.println("付款方式: " + getPaymentMethod());
        System.out.println("金額: $" + amount);
        System.out.println("稅額: $" + calculateTax(amount));
        System.out.println("總計: $" + (amount + calculateTax(amount)));
    }
    
    // 靜態方法（Java 8+）
    static boolean isValidAmount(double amount) {
        return amount > 0 && amount <= 10000;
    }
}

// 可退款介面
public interface Refundable {
    boolean processRefund(double amount);
    int getRefundPeriodDays();
}

// 信用卡實作
public class CreditCard implements Payable, Refundable {
    
    private String cardNumber;
    private String holderName;
    private double limit;
    private double balance;
    
    public CreditCard(String cardNumber, String holderName, double limit) {
        this.cardNumber = cardNumber;
        this.holderName = holderName;
        this.limit = limit;
        this.balance = 0;
    }
    
    @Override
    public boolean processPayment(double amount) {
        if (!Payable.isValidAmount(amount)) {
            System.out.println("付款金額無效");
            return false;
        }
        
        if (balance + amount <= limit) {
            balance += amount;
            System.out.println("信用卡付款成功: $" + amount);
            printReceipt(amount);
            return true;
        }
        
        System.out.println("信用卡額度不足");
        return false;
    }
    
    @Override
    public String getPaymentMethod() {
        return "信用卡 (" + cardNumber.substring(cardNumber.length() - 4) + ")";
    }
    
    @Override
    public boolean processRefund(double amount) {
        if (amount <= balance) {
            balance -= amount;
            System.out.println("信用卡退款成功: $" + amount);
            return true;
        }
        System.out.println("退款金額超過已用額度");
        return false;
    }
    
    @Override
    public int getRefundPeriodDays() {
        return 90; // 90 天退款期
    }
    
    // 覆寫預設方法
    @Override
    public double calculateTax(double amount) {
        // 信用卡享有稅率優惠
        return amount * (TAX_RATE * 0.8);
    }
}

// 現金實作
public class Cash implements Payable {
    
    private double availableAmount;
    
    public Cash(double availableAmount) {
        this.availableAmount = availableAmount;
    }
    
    @Override
    public boolean processPayment(double amount) {
        if (!Payable.isValidAmount(amount)) {
            System.out.println("付款金額無效");
            return false;
        }
        
        if (availableAmount >= amount) {
            availableAmount -= amount;
            System.out.println("現金付款成功: $" + amount);
            printReceipt(amount);
            return true;
        }
        
        System.out.println("現金不足");
        return false;
    }
    
    @Override
    public String getPaymentMethod() {
        return "現金";
    }
}
```

#### 4.5.2 抽象類別

```java
// 抽象車輛類別
public abstract class Vehicle {
    
    protected String brand;
    protected String model;
    protected int year;
    protected boolean isRunning;
    
    // 具體建構子
    public Vehicle(String brand, String model, int year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
        this.isRunning = false;
    }
    
    // 具體方法
    public void start() {
        if (!isRunning) {
            isRunning = true;
            System.out.println(brand + " " + model + " 已啟動");
        } else {
            System.out.println("車輛已在運行中");
        }
    }
    
    public void stop() {
        if (isRunning) {
            isRunning = false;
            System.out.println(brand + " " + model + " 已停止");
        } else {
            System.out.println("車輛已停止");
        }
    }
    
    // 抽象方法（子類別必須實作）
    public abstract void accelerate(int speed);
    public abstract void brake();
    public abstract double getFuelEfficiency();
    
    // 模板方法模式
    public final void performTrip(int distance) {
        start();
        accelerate(60);
        System.out.println("行駛距離: " + distance + " 公里");
        double fuelUsed = distance / getFuelEfficiency();
        System.out.println("燃料消耗: " + fuelUsed + " 公升");
        brake();
        stop();
    }
    
    // Getter 方法
    public String getBrand() { return brand; }
    public String getModel() { return model; }
    public int getYear() { return year; }
    public boolean isRunning() { return isRunning; }
}

// 汽車實作
public class Car extends Vehicle {
    
    private int numberOfDoors;
    private String transmissionType;
    
    public Car(String brand, String model, int year, int numberOfDoors, String transmissionType) {
        super(brand, model, year);
        this.numberOfDoors = numberOfDoors;
        this.transmissionType = transmissionType;
    }
    
    @Override
    public void accelerate(int speed) {
        if (isRunning) {
            System.out.println("汽車加速至 " + speed + " km/h");
        } else {
            System.out.println("請先啟動車輛");
        }
    }
    
    @Override
    public void brake() {
        if (isRunning) {
            System.out.println("汽車正在煞車");
        }
    }
    
    @Override
    public double getFuelEfficiency() {
        return transmissionType.equals("手排") ? 12.0 : 10.0; // km/L
    }
    
    public void openTrunk() {
        System.out.println("後車廂已開啟");
    }
}

// 機車實作
public class Motorcycle extends Vehicle {
    
    private int engineCapacity;
    
    public Motorcycle(String brand, String model, int year, int engineCapacity) {
        super(brand, model, year);
        this.engineCapacity = engineCapacity;
    }
    
    @Override
    public void accelerate(int speed) {
        if (isRunning) {
            System.out.println("機車加速至 " + speed + " km/h");
        } else {
            System.out.println("請先啟動車輛");
        }
    }
    
    @Override
    public void brake() {
        if (isRunning) {
            System.out.println("機車正在煞車");
        }
    }
    
    @Override
    public double getFuelEfficiency() {
        return engineCapacity <= 125 ? 35.0 : 25.0; // km/L
    }
    
    public void wheelie() {
        if (isRunning) {
            System.out.println("機車正在翹頭");
        }
    }
}
```

### 4.6 存取修飾詞

#### 4.6.1 存取控制範例

```java
package com.tutorial.access;

public class AccessModifierDemo {
    
    // public: 任何地方都可存取
    public String publicField = "所有人都可以看到";
    
    // protected: 同套件或子類別可存取
    protected String protectedField = "同套件或子類別可以看到";
    
    // default (package-private): 同套件可存取
    String defaultField = "同套件可以看到";
    
    // private: 只有同類別可存取
    private String privateField = "只有我自己可以看到";
    
    public void demonstrateAccess() {
        // 在同一個類別內，所有存取修飾詞都可以存取
        System.out.println(publicField);
        System.out.println(protectedField);
        System.out.println(defaultField);
        System.out.println(privateField);
    }
    
    // 私有輔助方法
    private void privateMethod() {
        System.out.println("這是私有方法");
    }
    
    // 保護方法
    protected void protectedMethod() {
        System.out.println("這是保護方法");
        privateMethod(); // 可以呼叫私有方法
    }
}

// 同套件的另一個類別
class SamePackageClass {
    
    public void testAccess() {
        AccessModifierDemo demo = new AccessModifierDemo();
        
        System.out.println(demo.publicField);    // ✓ 可存取
        System.out.println(demo.protectedField); // ✓ 可存取（同套件）
        System.out.println(demo.defaultField);   // ✓ 可存取（同套件）
        // System.out.println(demo.privateField); // ✗ 編譯錯誤
        
        demo.protectedMethod(); // ✓ 可存取
        // demo.privateMethod(); // ✗ 編譯錯誤
    }
}
```

#### 4.6.2 跨套件存取

```java
package com.tutorial.other;

import com.tutorial.access.AccessModifierDemo;

public class DifferentPackageClass extends AccessModifierDemo {
    
    public void testAccess() {
        AccessModifierDemo demo = new AccessModifierDemo();
        
        System.out.println(demo.publicField);     // ✓ 可存取
        // System.out.println(demo.protectedField); // ✗ 編譯錯誤（不是透過繼承）
        // System.out.println(demo.defaultField);   // ✗ 編譯錯誤（不同套件）
        // System.out.println(demo.privateField);   // ✗ 編譯錯誤
        
        // 透過繼承存取 protected 成員
        System.out.println(this.protectedField); // ✓ 可存取（透過繼承）
        this.protectedMethod(); // ✓ 可存取（透過繼承）
    }
}
```

### 4.7 認證考點與陷阱題

#### 4.7.1 方法解析順序

```java
class Parent {
    public void method() {
        System.out.println("Parent method");
    }
    
    public static void staticMethod() {
        System.out.println("Parent static method");
    }
}

class Child extends Parent {
    public void method() {
        System.out.println("Child method");
    }
    
    // 靜態方法不是覆寫，而是隱藏
    public static void staticMethod() {
        System.out.println("Child static method");
    }
}

public class MethodResolutionTest {
    public static void main(String[] args) {
        Parent p = new Child();
        p.method();        // "Child method" - 動態綁定
        p.staticMethod();  // "Parent static method" - 靜態綁定
        
        Child c = new Child();
        c.staticMethod();  // "Child static method"
    }
}
```

#### 4.7.2 物件存活範圍

```java
public class ObjectLifecycleTest {
    
    static Object staticRef;
    
    public static void main(String[] args) {
        // 區域變數
        Object localRef = new Object(); // obj1
        
        // 方法呼叫
        createObject(); // obj2 在方法結束後符合 GC 條件
        
        // 靜態參照
        staticRef = new Object(); // obj3
        
        // 循環參照
        Node node1 = new Node();
        Node node2 = new Node();
        node1.next = node2;
        node2.next = node1;
        node1 = null;
        node2 = null; // 兩個節點都符合 GC 條件（現代 JVM 可處理）
        
        System.gc(); // 建議執行 GC（不保證立即執行）
    }
    
    static void createObject() {
        Object temp = new Object(); // obj2
        // 方法結束，temp 超出範圍
    }
    
    static class Node {
        Node next;
    }
}
```

#### 4.7.3 final/abstract 差異

```java
// 抽象類別不能實例化，但可以有建構子
abstract class AbstractClass {
    private String name;
    
    // 抽象類別可以有建構子
    public AbstractClass(String name) {
        this.name = name;
    }
    
    // 可以有具體方法
    public final void finalMethod() {
        System.out.println("final 方法不能被覆寫");
    }
    
    // 抽象方法
    public abstract void abstractMethod();
}

// final 類別不能被繼承
final class FinalClass {
    public void method() {
        System.out.println("final 類別的方法");
    }
}

class ConcreteClass extends AbstractClass {
    
    public ConcreteClass() {
        super("具體類別"); // 必須呼叫父類別建構子
    }
    
    @Override
    public void abstractMethod() {
        System.out.println("實作抽象方法");
    }
    
    // @Override
    // public void finalMethod() { } // 編譯錯誤！不能覆寫 final 方法
}

// class ExtendFinal extends FinalClass { } // 編譯錯誤！不能繼承 final 類別
```

### 4.8 小練習與解析

**練習 4.1**：以下程式碼是否能編譯成功？為什麼？

```java
abstract class Animal {
    public Animal() {
        makeSound();
    }
    public abstract void makeSound();
}

class Dog extends Animal {
    private String name = "Buddy";
    
    public void makeSound() {
        System.out.println(name + " barks");
    }
}
```

**解析**：能編譯成功，但執行時會印出 "null barks"。原因是在父類別建構子執行時，子類別的實例變數尚未初始化，所以 name 為 null。

**練習 4.2**：請說明以下程式碼的輸出結果：

```java
class Parent {
    static { System.out.print("1"); }
    { System.out.print("2"); }
    public Parent() { System.out.print("3"); }
}

class Child extends Parent {
    static { System.out.print("4"); }
    { System.out.print("5"); }
    public Child() { System.out.print("6"); }
}

public class Test {
    public static void main(String[] args) {
        new Child();
    }
}
```

**解析**：輸出 "142356"

- 1: Parent 靜態初始化區塊
- 4: Child 靜態初始化區塊  
- 2: Parent 實例初始化區塊
- 3: Parent 建構子
- 5: Child 實例初始化區塊
- 6: Child 建構子

---

## 5. 核心 API 與工具

### 5.1 字串與 StringBuilder

#### 5.1.1 String 類別特性

```java
public class StringDemo {
    
    public static void main(String[] args) {
        // 字串建立方式
        String str1 = "Hello";           // 字串池
        String str2 = "Hello";           // 同一個物件（字串池）
        String str3 = new String("Hello"); // 新物件
        String str4 = new String("Hello").intern(); // 放入字串池
        
        // 物件比較
        System.out.println("str1 == str2: " + (str1 == str2));         // true
        System.out.println("str1 == str3: " + (str1 == str3));         // false
        System.out.println("str1 == str4: " + (str1 == str4));         // true
        System.out.println("str1.equals(str3): " + str1.equals(str3)); // true
        
        // 字串不可變性
        String original = "Java";
        String modified = original.concat(" Programming");
        System.out.println("original: " + original);   // "Java" (不變)
        System.out.println("modified: " + modified);   // "Java Programming"
        
        // 常用字串方法
        String text = "  Hello World Programming  ";
        
        System.out.println("長度: " + text.length());                    // 26
        System.out.println("去除空白: '" + text.trim() + "'");           // "Hello World Programming"
        System.out.println("大寫: " + text.toUpperCase());              // "  HELLO WORLD PROGRAMMING  "
        System.out.println("小寫: " + text.toLowerCase());              // "  hello world programming  "
        System.out.println("子字串: " + text.substring(2, 7));          // "Hello"
        System.out.println("取代: " + text.replace("World", "Java"));   // "  Hello Java Programming  "
        System.out.println("包含: " + text.contains("World"));          // true
        System.out.println("開始: " + text.trim().startsWith("Hello")); // true
        System.out.println("結束: " + text.trim().endsWith("Programming")); // true
        
        // 字串分割
        String csv = "apple,banana,orange,grape";
        String[] fruits = csv.split(",");
        for (String fruit : fruits) {
            System.out.println("水果: " + fruit);
        }
        
        // 字串格式化
        String name = "張三";
        int age = 25;
        double salary = 50000.5;
        
        String formatted1 = String.format("姓名: %s, 年齡: %d, 薪水: %.2f", name, age, salary);
        String formatted2 = "%s 今年 %d 歲，月薪 $%.2f".formatted(name, age, salary); // Java 15+
        
        System.out.println(formatted1);
        System.out.println(formatted2);
    }
}
```

#### 5.1.2 StringBuilder 與 StringBuffer

```java
import java.util.StringJoiner;

public class StringBuilderDemo {
    
    public static void main(String[] args) {
        // StringBuilder（非執行緒安全，效能較好）
        StringBuilder sb = new StringBuilder();
        sb.append("Hello");
        sb.append(" ");
        sb.append("World");
        sb.insert(5, " Beautiful");
        sb.delete(6, 16); // 刪除 "Beautiful"
        sb.reverse();
        
        System.out.println("StringBuilder 結果: " + sb.toString()); // "dlroW olleH"
        
        // 重設 StringBuilder
        sb.setLength(0); // 清空內容
        sb.append("重新開始");
        
        // StringBuffer（執行緒安全）
        StringBuffer sbf = new StringBuffer("執行緒安全");
        sbf.append("的字串處理");
        
        // 效能比較
        long startTime, endTime;
        
        // String 連接（效能差）
        startTime = System.currentTimeMillis();
        String result1 = "";
        for (int i = 0; i < 10000; i++) {
            result1 += "a";
        }
        endTime = System.currentTimeMillis();
        System.out.println("String 連接時間: " + (endTime - startTime) + "ms");
        
        // StringBuilder（效能好）
        startTime = System.currentTimeMillis();
        StringBuilder sb2 = new StringBuilder();
        for (int i = 0; i < 10000; i++) {
            sb2.append("a");
        }
        String result2 = sb2.toString();
        endTime = System.currentTimeMillis();
        System.out.println("StringBuilder 時間: " + (endTime - startTime) + "ms");
        
        // StringJoiner（Java 8+）
        StringJoiner joiner = new StringJoiner(", ", "[", "]");
        joiner.add("Apple");
        joiner.add("Banana");
        joiner.add("Orange");
        System.out.println("StringJoiner: " + joiner.toString()); // [Apple, Banana, Orange]
        
        // String.join（Java 8+）
        String joined = String.join(" | ", "項目1", "項目2", "項目3");
        System.out.println("String.join: " + joined); // 項目1 | 項目2 | 項目3
        
        // 文字塊（Text Blocks，Java 15+）
        String json = """
                {
                    "name": "張三",
                    "age": 25,
                    "city": "台北"
                }
                """;
        System.out.println("JSON 文字塊:");
        System.out.println(json);
    }
}
```

### 5.2 陣列與集合框架

#### 5.2.1 陣列操作

```java
import java.util.Arrays;

public class ArrayDemo {
    
    public static void main(String[] args) {
        // 陣列宣告與初始化
        int[] numbers1 = new int[5];           // [0, 0, 0, 0, 0]
        int[] numbers2 = {1, 2, 3, 4, 5};      // 初始化列表
        int[] numbers3 = new int[]{1, 2, 3, 4, 5}; // 匿名陣列
        
        // 陣列賦值
        numbers1[0] = 10;
        numbers1[1] = 20;
        
        // 陣列長度
        System.out.println("陣列長度: " + numbers2.length);
        
        // 陣列遍歷
        System.out.println("=== 傳統 for 迴圈 ===");
        for (int i = 0; i < numbers2.length; i++) {
            System.out.println("numbers2[" + i + "] = " + numbers2[i]);
        }
        
        System.out.println("=== 增強型 for 迴圈 ===");
        for (int num : numbers2) {
            System.out.println("數字: " + num);
        }
        
        // 多維陣列
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        
        System.out.println("=== 矩陣 ===");
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
        
        // Arrays 工具類別
        int[] data = {5, 2, 8, 1, 9};
        
        System.out.println("原始陣列: " + Arrays.toString(data));
        
        // 排序
        Arrays.sort(data);
        System.out.println("排序後: " + Arrays.toString(data));
        
        // 二分搜尋（陣列必須已排序）
        int index = Arrays.binarySearch(data, 5);
        System.out.println("元素 5 的索引: " + index);
        
        // 陣列複製
        int[] copied = Arrays.copyOf(data, data.length);
        int[] partial = Arrays.copyOfRange(data, 1, 4);
        
        System.out.println("複製陣列: " + Arrays.toString(copied));
        System.out.println("部分複製: " + Arrays.toString(partial));
        
        // 陣列填充
        int[] filled = new int[5];
        Arrays.fill(filled, 99);
        System.out.println("填充陣列: " + Arrays.toString(filled));
        
        // 陣列比較
        int[] array1 = {1, 2, 3};
        int[] array2 = {1, 2, 3};
        System.out.println("陣列相等: " + Arrays.equals(array1, array2)); // true
        
        // 不規則陣列
        int[][] irregular = new int[3][];
        irregular[0] = new int[2];
        irregular[1] = new int[4];
        irregular[2] = new int[3];
        
        System.out.println("不規則陣列長度:");
        for (int i = 0; i < irregular.length; i++) {
            System.out.println("irregular[" + i + "].length = " + irregular[i].length);
        }
    }
}
```

#### 5.2.2 List 集合

```java
import java.util.*;

public class ListDemo {
    
    public static void main(String[] args) {
        // ArrayList - 動態陣列
        List<String> arrayList = new ArrayList<>();
        arrayList.add("Apple");
        arrayList.add("Banana");
        arrayList.add("Cherry");
        arrayList.add(1, "Blueberry"); // 插入到指定位置
        
        System.out.println("ArrayList: " + arrayList);
        System.out.println("第一個元素: " + arrayList.get(0));
        System.out.println("大小: " + arrayList.size());
        
        // LinkedList - 雙向連結串列
        List<String> linkedList = new LinkedList<>();
        linkedList.add("第一個");
        linkedList.add("第二個");
        ((LinkedList<String>) linkedList).addFirst("最前面");
        ((LinkedList<String>) linkedList).addLast("最後面");
        
        System.out.println("LinkedList: " + linkedList);
        
        // Vector - 執行緒安全的動態陣列
        List<Integer> vector = new Vector<>();
        vector.add(1);
        vector.add(2);
        vector.add(3);
        
        // List 常用操作
        List<String> fruits = new ArrayList<>();
        fruits.add("蘋果");
        fruits.add("香蕉");
        fruits.add("橘子");
        fruits.add("香蕉"); // 允許重複
        
        System.out.println("\n=== List 操作 ===");
        System.out.println("原始列表: " + fruits);
        
        // 檢查包含
        System.out.println("包含香蕉: " + fruits.contains("香蕉"));
        System.out.println("香蕉的索引: " + fruits.indexOf("香蕉"));
        System.out.println("香蕉的最後索引: " + fruits.lastIndexOf("香蕉"));
        
        // 移除元素
        fruits.remove("香蕉");        // 移除第一個匹配的元素
        fruits.remove(0);            // 移除指定索引的元素
        System.out.println("移除後: " + fruits);
        
        // 子列表
        List<String> subList = fruits.subList(0, 2);
        System.out.println("子列表: " + subList);
        
        // 列表轉陣列
        String[] array = fruits.toArray(new String[0]);
        System.out.println("轉換為陣列: " + Arrays.toString(array));
        
        // 陣列轉列表
        List<String> fromArray = Arrays.asList("A", "B", "C");
        System.out.println("從陣列建立: " + fromArray);
        
        // 可變參數建立列表（Java 9+）
        List<String> immutableList = List.of("不可變", "列表", "Java9+");
        System.out.println("不可變列表: " + immutableList);
        // immutableList.add("新元素"); // UnsupportedOperationException
        
        // 列表排序
        List<Integer> numbers = new ArrayList<>(Arrays.asList(5, 2, 8, 1, 9));
        System.out.println("\n=== 排序 ===");
        System.out.println("排序前: " + numbers);
        
        Collections.sort(numbers);
        System.out.println("升序: " + numbers);
        
        Collections.sort(numbers, Collections.reverseOrder());
        System.out.println("降序: " + numbers);
        
        // 自定義排序
        List<String> names = new ArrayList<>(Arrays.asList("張三", "李四", "王五", "趙六"));
        names.sort((a, b) -> a.length() - b.length()); // 按長度排序
        System.out.println("按長度排序: " + names);
        
        // 列表搜尋
        Collections.sort(numbers);
        int index = Collections.binarySearch(numbers, 5);
        System.out.println("二分搜尋 5 的索引: " + index);
        
        // 列表反轉與洗牌
        Collections.reverse(numbers);
        System.out.println("反轉: " + numbers);
        
        Collections.shuffle(numbers);
        System.out.println("洗牌: " + numbers);
    }
}
```

#### 5.2.3 Set 集合

```java
import java.util.*;

public class SetDemo {
    
    public static void main(String[] args) {
        // HashSet - 基於雜湊表，無序，不重複
        Set<String> hashSet = new HashSet<>();
        hashSet.add("Apple");
        hashSet.add("Banana");
        hashSet.add("Cherry");
        hashSet.add("Apple"); // 重複元素，不會被加入
        
        System.out.println("HashSet: " + hashSet);
        System.out.println("大小: " + hashSet.size());
        
        // LinkedHashSet - 保持插入順序
        Set<String> linkedHashSet = new LinkedHashSet<>();
        linkedHashSet.add("第一個");
        linkedHashSet.add("第二個");
        linkedHashSet.add("第三個");
        linkedHashSet.add("第一個"); // 重複，不會被加入
        
        System.out.println("LinkedHashSet: " + linkedHashSet);
        
        // TreeSet - 自動排序，基於紅黑樹
        Set<Integer> treeSet = new TreeSet<>();
        treeSet.add(5);
        treeSet.add(2);
        treeSet.add(8);
        treeSet.add(1);
        treeSet.add(9);
        
        System.out.println("TreeSet (自動排序): " + treeSet);
        
        // TreeSet 使用自定義比較器
        Set<String> customTreeSet = new TreeSet<>((a, b) -> b.compareTo(a)); // 降序
        customTreeSet.add("Zebra");
        customTreeSet.add("Apple");
        customTreeSet.add("Monkey");
        
        System.out.println("TreeSet (降序): " + customTreeSet);
        
        // Set 操作
        Set<Integer> set1 = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5));
        Set<Integer> set2 = new HashSet<>(Arrays.asList(4, 5, 6, 7, 8));
        
        System.out.println("\n=== Set 操作 ===");
        System.out.println("Set1: " + set1);
        System.out.println("Set2: " + set2);
        
        // 聯集 (Union)
        Set<Integer> union = new HashSet<>(set1);
        union.addAll(set2);
        System.out.println("聯集: " + union);
        
        // 交集 (Intersection)
        Set<Integer> intersection = new HashSet<>(set1);
        intersection.retainAll(set2);
        System.out.println("交集: " + intersection);
        
        // 差集 (Difference)
        Set<Integer> difference = new HashSet<>(set1);
        difference.removeAll(set2);
        System.out.println("差集 (Set1 - Set2): " + difference);
        
        // 對稱差集
        Set<Integer> symmetricDiff = new HashSet<>(set1);
        symmetricDiff.addAll(set2);
        Set<Integer> temp = new HashSet<>(set1);
        temp.retainAll(set2);
        symmetricDiff.removeAll(temp);
        System.out.println("對稱差集: " + symmetricDiff);
        
        // Set 遍歷
        System.out.println("\n=== Set 遍歷 ===");
        for (String item : hashSet) {
            System.out.println("項目: " + item);
        }
        
        // 使用 Iterator
        Iterator<String> iterator = hashSet.iterator();
        while (iterator.hasNext()) {
            String item = iterator.next();
            if (item.equals("Apple")) {
                iterator.remove(); // 安全移除
            }
        }
        System.out.println("移除 Apple 後: " + hashSet);
        
        // 不可變 Set（Java 9+）
        Set<String> immutableSet = Set.of("不可變", "集合", "元素");
        System.out.println("不可變 Set: " + immutableSet);
    }
}
```

#### 5.2.4 Map 集合

```java
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

public class MapDemo {
    
    public static void main(String[] args) {
        // HashMap - 基於雜湊表，鍵值不重複
        Map<String, Integer> hashMap = new HashMap<>();
        hashMap.put("張三", 85);
        hashMap.put("李四", 92);
        hashMap.put("王五", 78);
        hashMap.put("張三", 88); // 覆蓋原值
        
        System.out.println("HashMap: " + hashMap);
        System.out.println("張三的分數: " + hashMap.get("張三"));
        System.out.println("不存在的鍵: " + hashMap.get("趙六")); // null
        
        // LinkedHashMap - 保持插入順序
        Map<String, String> linkedHashMap = new LinkedHashMap<>();
        linkedHashMap.put("name", "張三");
        linkedHashMap.put("age", "25");
        linkedHashMap.put("city", "台北");
        
        System.out.println("LinkedHashMap: " + linkedHashMap);
        
        // TreeMap - 按鍵排序
        Map<String, Double> treeMap = new TreeMap<>();
        treeMap.put("產品C", 299.99);
        treeMap.put("產品A", 199.99);
        treeMap.put("產品B", 249.99);
        
        System.out.println("TreeMap (按鍵排序): " + treeMap);
        
        // ConcurrentHashMap - 執行緒安全
        Map<String, Integer> concurrentMap = new ConcurrentHashMap<>();
        concurrentMap.put("安全", 1);
        concurrentMap.put("並發", 2);
        
        // Map 常用操作
        Map<String, Integer> scores = new HashMap<>();
        scores.put("數學", 85);
        scores.put("英文", 92);
        scores.put("物理", 78);
        scores.put("化學", 89);
        
        System.out.println("\n=== Map 操作 ===");
        System.out.println("所有成績: " + scores);
        
        // 檢查鍵和值
        System.out.println("包含數學: " + scores.containsKey("數學"));
        System.out.println("包含分數 92: " + scores.containsValue(92));
        
        // 取得鍵、值、鍵值對
        System.out.println("所有科目: " + scores.keySet());
        System.out.println("所有分數: " + scores.values());
        System.out.println("所有項目: " + scores.entrySet());
        
        // Map 遍歷
        System.out.println("\n=== Map 遍歷 ===");
        
        // 方法 1: 使用 keySet()
        for (String subject : scores.keySet()) {
            System.out.println(subject + ": " + scores.get(subject));
        }
        
        // 方法 2: 使用 entrySet()（推薦）
        for (Map.Entry<String, Integer> entry : scores.entrySet()) {
            System.out.println(entry.getKey() + " = " + entry.getValue());
        }
        
        // 方法 3: 使用 forEach（Java 8+）
        scores.forEach((subject, score) -> 
            System.out.println(subject + " -> " + score));
        
        // Map 默認值操作（Java 8+）
        System.out.println("\n=== 默認值操作 ===");
        
        // getOrDefault
        int historyScore = scores.getOrDefault("歷史", 0);
        System.out.println("歷史分數（預設 0）: " + historyScore);
        
        // putIfAbsent
        scores.putIfAbsent("歷史", 75);
        scores.putIfAbsent("數學", 95); // 不會覆蓋現有值
        System.out.println("加入歷史後: " + scores);
        
        // computeIfAbsent
        scores.computeIfAbsent("地理", k -> 80);
        System.out.println("計算地理分數: " + scores);
        
        // compute
        scores.compute("數學", (k, v) -> v + 5); // 數學加 5 分
        System.out.println("數學加分後: " + scores);
        
        // merge
        scores.merge("物理", 10, (oldVal, newVal) -> oldVal + newVal); // 物理加 10 分
        System.out.println("物理加分後: " + scores);
        
        // 不可變 Map（Java 9+）
        Map<String, String> immutableMap = Map.of(
            "key1", "value1",
            "key2", "value2",
            "key3", "value3"
        );
        System.out.println("不可變 Map: " + immutableMap);
        
        // Map 與其他集合的轉換
        System.out.println("\n=== 轉換操作 ===");
        
        // 計算統計資訊
        int totalScore = scores.values().stream().mapToInt(Integer::intValue).sum();
        double averageScore = scores.values().stream().mapToInt(Integer::intValue).average().orElse(0);
        
        System.out.println("總分: " + totalScore);
        System.out.println("平均分: " + averageScore);
        
        // 找出最高分科目
        Optional<Map.Entry<String, Integer>> maxEntry = scores.entrySet().stream()
            .max(Map.Entry.comparingByValue());
        
        if (maxEntry.isPresent()) {
            System.out.println("最高分科目: " + maxEntry.get().getKey() + 
                             " (" + maxEntry.get().getValue() + "分)");
        }
    }
}
```

### 5.3 java.time API

#### 5.3.1 日期時間基礎

```java
import java.time.*;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;
import java.time.temporal.TemporalAdjusters;

public class DateTimeDemo {
    
    public static void main(String[] args) {
        // 取得當前日期時間
        LocalDate today = LocalDate.now();
        LocalTime now = LocalTime.now();
        LocalDateTime dateTime = LocalDateTime.now();
        ZonedDateTime zonedDateTime = ZonedDateTime.now();
        
        System.out.println("今天日期: " + today);
        System.out.println("現在時間: " + now);
        System.out.println("日期時間: " + dateTime);
        System.out.println("時區日期時間: " + zonedDateTime);
        
        // 建立特定日期時間
        LocalDate specificDate = LocalDate.of(2024, 12, 25);
        LocalTime specificTime = LocalTime.of(14, 30, 0);
        LocalDateTime specificDateTime = LocalDateTime.of(2024, 12, 25, 14, 30, 0);
        
        System.out.println("\n=== 特定日期時間 ===");
        System.out.println("聖誕節: " + specificDate);
        System.out.println("下午茶時間: " + specificTime);
        System.out.println("聖誕節下午茶: " + specificDateTime);
        
        // 日期時間解析
        LocalDate parsedDate = LocalDate.parse("2024-01-15");
        LocalDateTime parsedDateTime = LocalDateTime.parse("2024-01-15T10:30:00");
        
        System.out.println("\n=== 解析日期時間 ===");
        System.out.println("解析日期: " + parsedDate);
        System.out.println("解析日期時間: " + parsedDateTime);
        
        // 日期時間格式化
        DateTimeFormatter formatter1 = DateTimeFormatter.ofPattern("yyyy-MM-dd");
        DateTimeFormatter formatter2 = DateTimeFormatter.ofPattern("yyyy年MM月dd日");
        DateTimeFormatter formatter3 = DateTimeFormatter.ofPattern("HH:mm:ss");
        DateTimeFormatter formatter4 = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        
        System.out.println("\n=== 格式化 ===");
        System.out.println("ISO 格式: " + today.format(formatter1));
        System.out.println("中文格式: " + today.format(formatter2));
        System.out.println("時間格式: " + now.format(formatter3));
        System.out.println("完整格式: " + dateTime.format(formatter4));
        
        // 自定義解析格式
        DateTimeFormatter customFormatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        LocalDate customParsed = LocalDate.parse("25/12/2024", customFormatter);
        System.out.println("自定義解析: " + customParsed);
        
        // 日期時間運算
        System.out.println("\n=== 日期運算 ===");
        LocalDate tomorrow = today.plusDays(1);
        LocalDate nextWeek = today.plusWeeks(1);
        LocalDate nextMonth = today.plusMonths(1);
        LocalDate nextYear = today.plusYears(1);
        
        System.out.println("明天: " + tomorrow);
        System.out.println("下週: " + nextWeek);
        System.out.println("下個月: " + nextMonth);
        System.out.println("明年: " + nextYear);
        
        LocalDate lastWeek = today.minusWeeks(1);
        LocalDate lastMonth = today.minusMonths(1);
        
        System.out.println("上週: " + lastWeek);
        System.out.println("上個月: " + lastMonth);
        
        // 時間運算
        System.out.println("\n=== 時間運算 ===");
        LocalTime laterTime = now.plusHours(2).plusMinutes(30);
        LocalTime earlierTime = now.minusHours(1).minusMinutes(15);
        
        System.out.println("2.5 小時後: " + laterTime);
        System.out.println("1.25 小時前: " + earlierTime);
        
        // 期間計算
        System.out.println("\n=== 期間計算 ===");
        LocalDate birthday = LocalDate.of(1990, 5, 15);
        Period age = Period.between(birthday, today);
        
        System.out.println("年齡: " + age.getYears() + "年 " + 
                         age.getMonths() + "月 " + age.getDays() + "天");
        
        // 時間間隔
        LocalDateTime start = LocalDateTime.of(2024, 1, 1, 9, 0);
        LocalDateTime end = LocalDateTime.of(2024, 1, 1, 17, 30);
        Duration workTime = Duration.between(start, end);
        
        System.out.println("工作時間: " + workTime.toHours() + "小時 " + 
                         (workTime.toMinutes() % 60) + "分鐘");
        
        // 時間單位計算
        long daysBetween = ChronoUnit.DAYS.between(birthday, today);
        long hoursBetween = ChronoUnit.HOURS.between(start, end);
        
        System.out.println("距離生日天數: " + daysBetween);
        System.out.println("工作小時數: " + hoursBetween);
        
        // 日期調整器
        System.out.println("\n=== 日期調整器 ===");
        LocalDate firstDayOfMonth = today.with(TemporalAdjusters.firstDayOfMonth());
        LocalDate lastDayOfMonth = today.with(TemporalAdjusters.lastDayOfMonth());
        LocalDate nextMonday = today.with(TemporalAdjusters.next(DayOfWeek.MONDAY));
        LocalDate firstMondayOfMonth = today.with(TemporalAdjusters.firstInMonth(DayOfWeek.MONDAY));
        
        System.out.println("月初: " + firstDayOfMonth);
        System.out.println("月底: " + lastDayOfMonth);
        System.out.println("下個星期一: " + nextMonday);
        System.out.println("本月第一個星期一: " + firstMondayOfMonth);
        
        // 時區處理
        System.out.println("\n=== 時區處理 ===");
        ZoneId taipeiZone = ZoneId.of("Asia/Taipei");
        ZoneId tokyoZone = ZoneId.of("Asia/Tokyo");
        ZoneId utcZone = ZoneId.of("UTC");
        
        ZonedDateTime taipeiTime = ZonedDateTime.now(taipeiZone);
        ZonedDateTime tokyoTime = taipeiTime.withZoneSameInstant(tokyoZone);
        ZonedDateTime utcTime = taipeiTime.withZoneSameInstant(utcZone);
        
        System.out.println("台北時間: " + taipeiTime);
        System.out.println("東京時間: " + tokyoTime);
        System.out.println("UTC 時間: " + utcTime);
        
        // Instant - 時間戳
        Instant timestamp = Instant.now();
        System.out.println("時間戳: " + timestamp);
        System.out.println("Unix 時間戳: " + timestamp.getEpochSecond());
        
        // 日期比較
        System.out.println("\n=== 日期比較 ===");
        LocalDate date1 = LocalDate.of(2024, 1, 15);
        LocalDate date2 = LocalDate.of(2024, 2, 20);
        
        System.out.println("date1 在 date2 之前: " + date1.isBefore(date2));
        System.out.println("date1 在 date2 之後: " + date1.isAfter(date2));
        System.out.println("日期相等: " + date1.equals(date2));
        System.out.println("比較結果: " + date1.compareTo(date2)); // 負數表示較早
    }
}
```

### 5.4 包裝類別與自動裝箱

#### 5.4.1 包裝類別基礎

```java
public class WrapperClassDemo {
    
    public static void main(String[] args) {
        // 基本型別與包裝類別對應
        byte b = 100;
        Byte byteWrapper = Byte.valueOf(b);
        
        short s = 1000;
        Short shortWrapper = Short.valueOf(s);
        
        int i = 42;
        Integer intWrapper = Integer.valueOf(i);
        
        long l = 1000000L;
        Long longWrapper = Long.valueOf(l);
        
        float f = 3.14f;
        Float floatWrapper = Float.valueOf(f);
        
        double d = 2.718;
        Double doubleWrapper = Double.valueOf(d);
        
        char c = 'A';
        Character charWrapper = Character.valueOf(c);
        
        boolean bool = true;
        Boolean boolWrapper = Boolean.valueOf(bool);
        
        System.out.println("=== 包裝類別建立 ===");
        System.out.println("Integer: " + intWrapper);
        System.out.println("Double: " + doubleWrapper);
        System.out.println("Character: " + charWrapper);
        System.out.println("Boolean: " + boolWrapper);
        
        // 自動裝箱（Autoboxing）- 基本型別 → 包裝類別
        Integer autoBoxed = 42;          // 等同於 Integer.valueOf(42)
        Double autoBoxedDouble = 3.14;   // 等同於 Double.valueOf(3.14)
        
        // 自動拆箱（Auto-unboxing）- 包裝類別 → 基本型別
        int unboxed = autoBoxed;         // 等同於 autoBoxed.intValue()
        double unboxedDouble = autoBoxedDouble; // 等同於 autoBoxedDouble.doubleValue()
        
        System.out.println("\n=== 自動裝箱/拆箱 ===");
        System.out.println("自動裝箱: " + autoBoxed);
        System.out.println("自動拆箱: " + unboxed);
        
        // 包裝類別快取（Cache）- 認證重點
        Integer a = 127;
        Integer b = 127;
        Integer c = 128;
        Integer d = 128;
        
        System.out.println("\n=== 包裝類別快取 ===");
        System.out.println("a == b (127): " + (a == b));         // true（快取範圍內）
        System.out.println("c == d (128): " + (c == d));         // false（超出快取範圍）
        System.out.println("a.equals(b): " + a.equals(b));       // true
        System.out.println("c.equals(d): " + c.equals(d));       // true
        
        // 不同包裝類別的快取範圍
        // Integer: -128 到 127
        // Byte: 所有值（-128 到 127）
        // Short: -128 到 127
        // Long: -128 到 127
        // Character: 0 到 127
        // Boolean: true 和 false
        
        // 字串轉換
        System.out.println("\n=== 字串轉換 ===");
        
        // 包裝類別解析字串
        int parsedInt = Integer.parseInt("123");
        double parsedDouble = Double.parseDouble("3.14");
        boolean parsedBoolean = Boolean.parseBoolean("true");
        
        System.out.println("解析整數: " + parsedInt);
        System.out.println("解析浮點數: " + parsedDouble);
        System.out.println("解析布林值: " + parsedBoolean);
        
        // 不同進制解析
        int binary = Integer.parseInt("1010", 2);      // 二進制
        int octal = Integer.parseInt("12", 8);         // 八進制
        int hex = Integer.parseInt("A", 16);           // 十六進制
        
        System.out.println("二進制 1010: " + binary);  // 10
        System.out.println("八進制 12: " + octal);     // 10
        System.out.println("十六進制 A: " + hex);      // 10
        
        // 數字轉字串
        String intStr = Integer.toString(123);
        String doubleStr = Double.toString(3.14);
        String hexStr = Integer.toHexString(255);
        String binaryStr = Integer.toBinaryString(10);
        
        System.out.println("整數轉字串: " + intStr);
        System.out.println("浮點數轉字串: " + doubleStr);
        System.out.println("轉十六進制: " + hexStr);    // ff
        System.out.println("轉二進制: " + binaryStr);   // 1010
        
        // 包裝類別常用方法
        System.out.println("\n=== 包裝類別方法 ===");
        
        // 數值比較
        Integer num1 = 100;
        Integer num2 = 200;
        System.out.println("比較 100 和 200: " + num1.compareTo(num2)); // -1
        
        // 型別資訊
        System.out.println("Integer 最大值: " + Integer.MAX_VALUE);
        System.out.println("Integer 最小值: " + Integer.MIN_VALUE);
        System.out.println("Integer 位元數: " + Integer.SIZE);
        
        System.out.println("Double 最大值: " + Double.MAX_VALUE);
        System.out.println("Double 最小值: " + Double.MIN_VALUE);
        
        // Character 方法
        char ch = 'a';
        System.out.println("\n=== Character 方法 ===");
        System.out.println("是否為字母: " + Character.isLetter(ch));
        System.out.println("是否為數字: " + Character.isDigit(ch));
        System.out.println("是否為空白: " + Character.isWhitespace(ch));
        System.out.println("轉大寫: " + Character.toUpperCase(ch));
        System.out.println("轉小寫: " + Character.toLowerCase(ch));
        
        // 數值溢出檢查（Java 8+）
        System.out.println("\n=== 溢出檢查 ===");
        try {
            int result = Math.addExact(Integer.MAX_VALUE, 1);
            System.out.println("加法結果: " + result);
        } catch (ArithmeticException e) {
            System.out.println("整數溢出: " + e.getMessage());
        }
        
        try {
            int result = Math.multiplyExact(Integer.MAX_VALUE, 2);
            System.out.println("乘法結果: " + result);
        } catch (ArithmeticException e) {
            System.out.println("整數溢出: " + e.getMessage());
        }
    }
}
```

### 5.5 認證考點與陷阱題

#### 5.5.1 equals vs == 陷阱

```java
public class EqualsVsEqualityTest {
    
    public static void main(String[] args) {
        // 字串比較陷阱
        String str1 = "Hello";
        String str2 = "Hello";
        String str3 = new String("Hello");
        String str4 = str3.intern();
        
        System.out.println("=== 字串比較 ===");
        System.out.println("str1 == str2: " + (str1 == str2));         // true（字串池）
        System.out.println("str1 == str3: " + (str1 == str3));         // false（不同物件）
        System.out.println("str1 == str4: " + (str1 == str4));         // true（intern）
        System.out.println("str1.equals(str3): " + str1.equals(str3)); // true（內容相同）
        
        // 包裝類別比較陷阱
        Integer int1 = 100;
        Integer int2 = 100;
        Integer int3 = 200;
        Integer int4 = 200;
        
        System.out.println("\n=== 包裝類別比較 ===");
        System.out.println("100 == 100: " + (int1 == int2));           // true（快取）
        System.out.println("200 == 200: " + (int3 == int4));           // false（超出快取）
        System.out.println("100.equals(100): " + int1.equals(int2));   // true
        System.out.println("200.equals(200): " + int3.equals(int4));   // true
        
        // 混合型別比較
        Integer intObj = 42;
        Long longObj = 42L;
        
        System.out.println("\n=== 混合型別比較 ===");
        System.out.println("Integer(42) == Long(42L): " + (intObj.longValue() == longObj)); // true
        System.out.println("Integer(42).equals(Long(42L)): " + intObj.equals(longObj));     // false
        
        // null 比較陷阱
        String nullStr = null;
        String nonNullStr = "test";
        
        System.out.println("\n=== null 比較 ===");
        System.out.println("null == null: " + (nullStr == null));      // true
        // System.out.println(nullStr.equals("test"));                 // NullPointerException
        System.out.println("\"test\".equals(null): " + "test".equals(nullStr)); // false（安全）
        System.out.println("Objects.equals(null, \"test\"): " + 
                         java.util.Objects.equals(nullStr, nonNullStr)); // false（安全）
    }
}
```

#### 5.5.2 hashCode 規則

```java
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

public class HashCodeRules {
    
    public static void main(String[] args) {
        // 測試正確的 hashCode 實作
        Person person1 = new Person("張三", 25);
        Person person2 = new Person("張三", 25);
        Person person3 = new Person("李四", 30);
        
        System.out.println("=== hashCode 測試 ===");
        System.out.println("person1.equals(person2): " + person1.equals(person2));
        System.out.println("person1.hashCode(): " + person1.hashCode());
        System.out.println("person2.hashCode(): " + person2.hashCode());
        System.out.println("hashCode 相等: " + (person1.hashCode() == person2.hashCode()));
        
        // 在 HashMap 中測試
        Map<Person, String> map = new HashMap<>();
        map.put(person1, "第一個人");
        
        System.out.println("\n=== HashMap 測試 ===");
        System.out.println("使用 person1 查詢: " + map.get(person1));
        System.out.println("使用 person2 查詢: " + map.get(person2)); // 應該能找到
        System.out.println("使用 person3 查詢: " + map.get(person3)); // null
        
        // 錯誤示範：違反 hashCode 契約的類別
        BadPerson bad1 = new BadPerson("王五", 35);
        BadPerson bad2 = new BadPerson("王五", 35);
        
        Map<BadPerson, String> badMap = new HashMap<>();
        badMap.put(bad1, "壞例子");
        
        System.out.println("\n=== 錯誤 hashCode 示範 ===");
        System.out.println("bad1.equals(bad2): " + bad1.equals(bad2));     // true
        System.out.println("bad1.hashCode(): " + bad1.hashCode());
        System.out.println("bad2.hashCode(): " + bad2.hashCode());
        System.out.println("使用 bad1 查詢: " + badMap.get(bad1));         // 找得到
        System.out.println("使用 bad2 查詢: " + badMap.get(bad2));         // 可能找不到！
    }
    
    // 正確的 equals 和 hashCode 實作
    static class Person {
        private String name;
        private int age;
        
        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }
        
        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            
            Person person = (Person) obj;
            return age == person.age && Objects.equals(name, person.name);
        }
        
        @Override
        public int hashCode() {
            return Objects.hash(name, age);
        }
        
        @Override
        public String toString() {
            return "Person{name='" + name + "', age=" + age + "}";
        }
    }
    
    // 錯誤的 hashCode 實作（違反契約）
    static class BadPerson {
        private String name;
        private int age;
        
        public BadPerson(String name, int age) {
            this.name = name;
            this.age = age;
        }
        
        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            
            BadPerson person = (BadPerson) obj;
            return age == person.age && Objects.equals(name, person.name);
        }
        
        // 錯誤：相等物件的 hashCode 不相等
        @Override
        public int hashCode() {
            return System.identityHashCode(this); // 每個物件都不同
        }
    }
}
```

### 5.6 小練習與解析

**練習 5.1**：以下程式碼的輸出結果是什麼？

```java
List<String> list = Arrays.asList("A", "B", "C");
list.set(0, "X");
list.add("D");
System.out.println(list);
```

**解析**：會拋出 `UnsupportedOperationException`。`Arrays.asList()` 返回的是固定大小的列表，可以修改元素但不能添加或刪除元素。

**練習 5.2**：請說明以下程式碼的行為：

```java
Integer a = new Integer(1);
Integer b = new Integer(1);
Integer c = 1;
Integer d = 1;

System.out.println(a == b);  // ?
System.out.println(c == d);  // ?
```

**解析**：

- `a == b`：false（兩個不同的物件）
- `c == d`：true（自動裝箱，且在快取範圍內）

### 5.7 泛型 (Generics)

#### 5.7.1 泛型基礎

```java
import java.util.*;

public class GenericsDemo {
    
    public static void main(String[] args) {
        // 泛型的基本使用
        List<String> stringList = new ArrayList<>();
        stringList.add("Hello");
        stringList.add("World");
        // stringList.add(123); // 編譯錯誤！型別安全
        
        // 泛型方法
        String[] strArray = {"apple", "banana", "cherry"};
        Integer[] intArray = {1, 2, 3, 4, 5};
        
        printArray(strArray);
        printArray(intArray);
        
        // 有界類型參數
        NumberContainer<Integer> intContainer = new NumberContainer<>(42);
        NumberContainer<Double> doubleContainer = new NumberContainer<>(3.14);
        
        System.out.println("整數值: " + intContainer.getValue());
        System.out.println("浮點值: " + doubleContainer.getValue());
    }
    
    // 泛型方法
    public static <T> void printArray(T[] array) {
        for (T element : array) {
            System.out.print(element + " ");
        }
        System.out.println();
    }
    
    // 有界類型參數
    static class NumberContainer<T extends Number> {
        private T value;
        
        public NumberContainer(T value) {
            this.value = value;
        }
        
        public T getValue() {
            return value;
        }
        
        public double getDoubleValue() {
            return value.doubleValue(); // Number 類別的方法
        }
    }
}
```

#### 5.7.2 通配符 (Wildcards)

```java
import java.util.*;

public class WildcardsDemo {
    
    public static void main(String[] args) {
        List<Integer> integers = Arrays.asList(1, 2, 3);
        List<Double> doubles = Arrays.asList(1.1, 2.2, 3.3);
        List<Number> numbers = Arrays.asList(1, 2.5, 3);
        
        // 上界通配符（? extends）
        printNumbers(integers); // 可以
        printNumbers(doubles);  // 可以
        printNumbers(numbers);  // 可以
        
        // 下界通配符（? super）
        List<Number> numberList = new ArrayList<>();
        addNumbers(numberList); // 可以
        
        List<Object> objectList = new ArrayList<>();
        addNumbers(objectList); // 可以
        
        // 無界通配符（?）
        printSize(integers);
        printSize(Arrays.asList("a", "b", "c"));
    }
    
    // 上界通配符：只能讀取，不能寫入（除了 null）
    public static void printNumbers(List<? extends Number> list) {
        for (Number num : list) {
            System.out.println(num);
        }
        // list.add(1); // 編譯錯誤！無法寫入
    }
    
    // 下界通配符：可以寫入，但讀取只能當作 Object
    public static void addNumbers(List<? super Integer> list) {
        list.add(1);
        list.add(2);
        // Integer num = list.get(0); // 編譯錯誤！
        Object obj = list.get(0);     // 只能當作 Object
    }
    
    // 無界通配符：只能使用 Object 的方法
    public static void printSize(List<?> list) {
        System.out.println("列表大小: " + list.size());
        // Object item = list.get(0); // 可以
    }
}
```

### 5.8 檔案 I/O 操作

#### 5.8.1 NIO.2 檔案操作

```java
import java.io.*;
import java.nio.file.*;
import java.nio.charset.StandardCharsets;
import java.util.List;

public class FileIODemo {
    
    public static void main(String[] args) {
        try {
            // 檔案路徑操作
            Path filePath = Paths.get("example.txt");
            Path dirPath = Paths.get("data", "files");
            
            // 建立目錄
            if (!Files.exists(dirPath)) {
                Files.createDirectories(dirPath);
                System.out.println("建立目錄: " + dirPath);
            }
            
            // 寫入檔案
            String content = "Hello, Java NIO.2!\n這是測試檔案。\n第三行內容。";
            Path testFile = dirPath.resolve("test.txt");
            Files.write(testFile, content.getBytes(StandardCharsets.UTF_8));
            System.out.println("檔案已寫入: " + testFile);
            
            // 讀取檔案
            List<String> lines = Files.readAllLines(testFile, StandardCharsets.UTF_8);
            System.out.println("讀取檔案內容:");
            for (int i = 0; i < lines.size(); i++) {
                System.out.println((i + 1) + ": " + lines.get(i));
            }
            
            // 檔案屬性
            System.out.println("檔案大小: " + Files.size(testFile) + " bytes");
            System.out.println("是否為目錄: " + Files.isDirectory(testFile));
            System.out.println("是否可讀: " + Files.isReadable(testFile));
            System.out.println("是否可寫: " + Files.isWritable(testFile));
            
            // 複製檔案
            Path copyFile = dirPath.resolve("copy_test.txt");
            Files.copy(testFile, copyFile, StandardCopyOption.REPLACE_EXISTING);
            System.out.println("檔案已複製到: " + copyFile);
            
            // 移動檔案
            Path moveFile = dirPath.resolve("moved_test.txt");
            Files.move(copyFile, moveFile, StandardCopyOption.REPLACE_EXISTING);
            System.out.println("檔案已移動到: " + moveFile);
            
            // 刪除檔案
            Files.deleteIfExists(moveFile);
            System.out.println("檔案已刪除: " + moveFile);
            
        } catch (IOException e) {
            System.err.println("I/O 錯誤: " + e.getMessage());
        }
    }
}
```

#### 5.8.2 串流操作 (Stream-based I/O)

```java
import java.io.*;
import java.nio.file.*;

public class StreamIODemo {
    
    public static void main(String[] args) {
        String fileName = "data/stream_test.txt";
        
        // 確保目錄存在
        try {
            Files.createDirectories(Paths.get("data"));
        } catch (IOException e) {
            System.err.println("無法建立目錄: " + e.getMessage());
            return;
        }
        
        // 寫入檔案（字元串流）
        try (BufferedWriter writer = Files.newBufferedWriter(Paths.get(fileName))) {
            writer.write("Java I/O 串流操作範例");
            writer.newLine();
            writer.write("使用 BufferedWriter 寫入");
            writer.newLine();
            writer.write("第三行內容");
            System.out.println("檔案寫入完成");
        } catch (IOException e) {
            System.err.println("寫入錯誤: " + e.getMessage());
        }
        
        // 讀取檔案（字元串流）
        try (BufferedReader reader = Files.newBufferedReader(Paths.get(fileName))) {
            String line;
            int lineNumber = 1;
            System.out.println("讀取檔案內容:");
            while ((line = reader.readLine()) != null) {
                System.out.println(lineNumber + ": " + line);
                lineNumber++;
            }
        } catch (IOException e) {
            System.err.println("讀取錯誤: " + e.getMessage());
        }
        
        // 二進位檔案操作
        String binaryFile = "data/binary_test.dat";
        
        // 寫入二進位資料
        try (DataOutputStream dos = new DataOutputStream(
                new FileOutputStream(binaryFile))) {
            dos.writeInt(42);
            dos.writeDouble(3.14159);
            dos.writeUTF("Hello Binary");
            dos.writeBoolean(true);
            System.out.println("二進位檔案寫入完成");
        } catch (IOException e) {
            System.err.println("二進位寫入錯誤: " + e.getMessage());
        }
        
        // 讀取二進位資料
        try (DataInputStream dis = new DataInputStream(
                new FileInputStream(binaryFile))) {
            int intValue = dis.readInt();
            double doubleValue = dis.readDouble();
            String stringValue = dis.readUTF();
            boolean boolValue = dis.readBoolean();
            
            System.out.println("讀取二進位資料:");
            System.out.println("整數: " + intValue);
            System.out.println("浮點數: " + doubleValue);
            System.out.println("字串: " + stringValue);
            System.out.println("布林值: " + boolValue);
        } catch (IOException e) {
            System.err.println("二進位讀取錯誤: " + e.getMessage());
        }
    }
}
```

### 5.9 正規表達式

#### 5.9.1 Pattern 與 Matcher

```java
import java.util.regex.*;

public class RegexDemo {
    
    public static void main(String[] args) {
        // 基本 Pattern 與 Matcher
        String text = "聯絡電話：0912-345-678，辦公室：02-1234-5678";
        String phonePattern = "\\d{4}-\\d{3}-\\d{3}|\\d{2}-\\d{4}-\\d{4}";
        
        Pattern pattern = Pattern.compile(phonePattern);
        Matcher matcher = pattern.matcher(text);
        
        System.out.println("找到的電話號碼:");
        while (matcher.find()) {
            System.out.println("- " + matcher.group());
            System.out.println("  位置: " + matcher.start() + "-" + matcher.end());
        }
        
        // 群組捕獲
        String emailPattern = "(\\w+)@(\\w+)\\.(\\w+)";
        String emailText = "聯絡我們: support@example.com 或 admin@test.org";
        
        Pattern emailPat = Pattern.compile(emailPattern);
        Matcher emailMatcher = emailPat.matcher(emailText);
        
        System.out.println("\nEmail 分析:");
        while (emailMatcher.find()) {
            System.out.println("完整 Email: " + emailMatcher.group(0));
            System.out.println("用戶名: " + emailMatcher.group(1));
            System.out.println("域名: " + emailMatcher.group(2));
            System.out.println("頂級域名: " + emailMatcher.group(3));
            System.out.println("---");
        }
        
        // 字串替換
        String htmlText = "<p>這是段落</p><div>這是 div</div>";
        String cleanText = htmlText.replaceAll("<[^>]*>", "");
        System.out.println("移除 HTML 標籤: " + cleanText);
        
        // 驗證格式
        validateFormats();
        
        // 分割字串
        splitDemo();
    }
    
    private static void validateFormats() {
        System.out.println("\n格式驗證:");
        
        // 台灣身分證字號
        String idPattern = "[A-Z]\\d{9}";
        System.out.println("A123456789 身分證格式: " + 
            "A123456789".matches(idPattern));
        System.out.println("X987654321 身分證格式: " + 
            "X987654321".matches(idPattern));
        System.out.println("12345 身分證格式: " + 
            "12345".matches(idPattern));
        
        // Email 驗證
        String emailPattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}";
        System.out.println("test@example.com Email格式: " + 
            "test@example.com".matches(emailPattern));
        System.out.println("invalid-email Email格式: " + 
            "invalid-email".matches(emailPattern));
        
        // 密碼強度檢查（至少8字元，包含大小寫字母和數字）
        String passwordPattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)[a-zA-Z\\d@$!%*?&]{8,}$";
        System.out.println("Password123 密碼強度: " + 
            "Password123".matches(passwordPattern));
        System.out.println("weak 密碼強度: " + 
            "weak".matches(passwordPattern));
    }
    
    private static void splitDemo() {
        System.out.println("\n字串分割:");
        
        String data = "apple,banana;orange:grape";
        
        // 使用多個分隔符號
        String[] fruits = data.split("[,;:]");
        for (String fruit : fruits) {
            System.out.println("水果: " + fruit);
        }
        
        // CSV 解析（處理引號內的逗號）
        String csvLine = "\"Smith, John\",25,\"Manager\",50000";
        // 簡化版，實際應用需要更複雜的處理
        String[] csvFields = csvLine.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)");
        for (int i = 0; i < csvFields.length; i++) {
            String field = csvFields[i].replaceAll("^\"|\"$", ""); // 移除引號
            System.out.println("欄位 " + i + ": " + field);
        }
    }
}
```

---

## 6. 例外處理與錯誤管理

### 6.1 例外處理基礎

#### 6.1.1 例外類別階層

```java
/*
例外類別階層：
Throwable
├── Error (系統錯誤，不應該捕捉)
│   ├── OutOfMemoryError
│   ├── StackOverflowError
│   └── VirtualMachineError
└── Exception
    ├── RuntimeException (Unchecked Exception)
    │   ├── NullPointerException
    │   ├── ArrayIndexOutOfBoundsException
    │   ├── IllegalArgumentException
    │   ├── NumberFormatException
    │   └── ClassCastException
    └── 其他 Exception (Checked Exception)
        ├── IOException
        ├── FileNotFoundException
        ├── SQLException
        └── ClassNotFoundException
*/

public class ExceptionHierarchyDemo {
    
    public static void main(String[] args) {
        // RuntimeException 範例（Unchecked）
        demonstrateRuntimeExceptions();
        
        // Checked Exception 範例
        demonstrateCheckedExceptions();
    }
    
    private static void demonstrateRuntimeExceptions() {
        System.out.println("=== Runtime Exceptions ===");
        
        try {
            // NullPointerException
            String str = null;
            int length = str.length();
        } catch (NullPointerException e) {
            System.out.println("捕捉到 NullPointerException: " + e.getMessage());
        }
        
        try {
            // ArrayIndexOutOfBoundsException
            int[] array = {1, 2, 3};
            int value = array[5];
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("捕捉到 ArrayIndexOutOfBoundsException: " + e.getMessage());
        }
        
        try {
            // NumberFormatException
            int number = Integer.parseInt("abc");
        } catch (NumberFormatException e) {
            System.out.println("捕捉到 NumberFormatException: " + e.getMessage());
        }
        
        try {
            // IllegalArgumentException
            Thread.sleep(-1);
        } catch (IllegalArgumentException e) {
            System.out.println("捕捉到 IllegalArgumentException: " + e.getMessage());
        } catch (InterruptedException e) {
            System.out.println("捕捉到 InterruptedException: " + e.getMessage());
        }
    }
    
    private static void demonstrateCheckedExceptions() {
        System.out.println("\n=== Checked Exceptions ===");
        
        try {
            // 模擬 IOException
            java.io.FileReader reader = new java.io.FileReader("nonexistent.txt");
        } catch (java.io.FileNotFoundException e) {
            System.out.println("捕捉到 FileNotFoundException: " + e.getMessage());
        }
        
        try {
            // 模擬 ClassNotFoundException
            Class<?> clazz = Class.forName("com.nonexistent.Class");
        } catch (ClassNotFoundException e) {
            System.out.println("捕捉到 ClassNotFoundException: " + e.getMessage());
        }
    }
}
```

#### 6.1.2 try-catch-finally 基本語法

```java
import java.io.*;
import java.util.Scanner;

public class TryCatchFinallyDemo {
    
    public static void main(String[] args) {
        // 基本 try-catch
        basicTryCatch();
        
        // 多重 catch
        multipleCatch();
        
        // try-catch-finally
        tryCatchFinally();
        
        // 巢狀 try
        nestedTry();
    }
    
    private static void basicTryCatch() {
        System.out.println("=== 基本 try-catch ===");
        
        try {
            int result = 10 / 0; // 會拋出 ArithmeticException
            System.out.println("結果: " + result);
        } catch (ArithmeticException e) {
            System.out.println("捕捉到算術例外: " + e.getMessage());
            System.out.println("例外類型: " + e.getClass().getSimpleName());
        }
        
        System.out.println("程式繼續執行...\n");
    }
    
    private static void multipleCatch() {
        System.out.println("=== 多重 catch ===");
        
        String[] data = {"123", "abc", null};
        
        for (int i = 0; i < data.length; i++) {
            try {
                String str = data[i];
                int length = str.length();           // 可能 NullPointerException
                int number = Integer.parseInt(str);  // 可能 NumberFormatException
                System.out.println("處理成功: " + number + ", 長度: " + length);
                
            } catch (NullPointerException e) {
                System.out.println("字串為 null");
            } catch (NumberFormatException e) {
                System.out.println("無法解析數字: " + data[i]);
            } catch (Exception e) {
                // 捕捉所有其他例外（必須放在最後）
                System.out.println("其他例外: " + e.getClass().getSimpleName());
            }
        }
        
        System.out.println();
    }
    
    private static void tryCatchFinally() {
        System.out.println("=== try-catch-finally ===");
        
        FileInputStream fis = null;
        try {
            fis = new FileInputStream("test.txt");
            // 處理檔案...
            System.out.println("檔案處理中...");
            
        } catch (FileNotFoundException e) {
            System.out.println("檔案不存在: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("IO 錯誤: " + e.getMessage());
        } finally {
            // finally 區塊總是會執行
            System.out.println("執行清理工作...");
            if (fis != null) {
                try {
                    fis.close();
                    System.out.println("檔案已關閉");
                } catch (IOException e) {
                    System.out.println("關閉檔案時發生錯誤: " + e.getMessage());
                }
            }
        }
        
        System.out.println();
    }
    
    private static void nestedTry() {
        System.out.println("=== 巢狀 try ===");
        
        try {
            System.out.println("外層 try 開始");
            
            try {
                System.out.println("內層 try 開始");
                int result = 10 / 0;
                System.out.println("內層 try 結果: " + result);
            } catch (ArithmeticException e) {
                System.out.println("內層 catch: " + e.getMessage());
                // 重新拋出例外
                throw new RuntimeException("內層處理後重新拋出", e);
            } finally {
                System.out.println("內層 finally 執行");
            }
            
            System.out.println("外層 try 繼續");
            
        } catch (RuntimeException e) {
            System.out.println("外層 catch: " + e.getMessage());
            System.out.println("原因: " + e.getCause().getMessage());
        } finally {
            System.out.println("外層 finally 執行");
        }
        
        System.out.println();
    }
}
```

### 6.2 throws 與 throw

#### 6.2.1 throws 宣告

```java
import java.io.*;
import java.sql.*;

public class ThrowsDemo {
    
    public static void main(String[] args) {
        try {
            // 呼叫宣告 throws 的方法
            readFile("data.txt");
        } catch (IOException e) {
            System.out.println("捕捉到 IO 例外: " + e.getMessage());
        }
        
        try {
            processData(-1);
        } catch (IllegalArgumentException e) {
            System.out.println("捕捉到參數例外: " + e.getMessage());
        }
        
        try {
            chainedMethodCalls();
        } catch (Exception e) {
            System.out.println("捕捉到鏈式呼叫例外: " + e.getMessage());
        }
    }
    
    // 宣告可能拋出 Checked Exception
    public static void readFile(String filename) throws IOException {
        System.out.println("嘗試讀取檔案: " + filename);
        
        // 模擬檔案讀取
        if (!filename.endsWith(".txt")) {
            throw new IOException("檔案格式不正確，必須是 .txt 檔案");
        }
        
        FileReader reader = new FileReader(filename); // 可能拋出 FileNotFoundException
        // ... 處理檔案
        reader.close();
    }
    
    // 宣告可能拋出 Runtime Exception（可選）
    public static void processData(int value) throws IllegalArgumentException {
        if (value < 0) {
            throw new IllegalArgumentException("值不能為負數: " + value);
        }
        
        System.out.println("處理資料: " + value);
    }
    
    // 多重 throws 宣告
    public static void databaseOperation() throws SQLException, ClassNotFoundException {
        // 模擬資料庫操作
        Class.forName("com.mysql.cj.jdbc.Driver");
        
        // 模擬連線錯誤
        throw new SQLException("資料庫連線失敗");
    }
    
    // 方法鏈式 throws
    public static void chainedMethodCalls() throws Exception {
        method1();
    }
    
    private static void method1() throws Exception {
        method2();
    }
    
    private static void method2() throws Exception {
        method3();
    }
    
    private static void method3() throws Exception {
        throw new Exception("最深層的例外");
    }
    
    // 覆寫方法的 throws 規則
    public static class Parent {
        public void parentMethod() throws IOException {
            // 父類別方法
        }
    }
    
    public static class Child extends Parent {
        // 正確：可以不宣告 throws
        @Override
        public void parentMethod() {
            // 子類別不拋出例外
        }
        
        // 正確：可以宣告相同或更具體的例外
        public void anotherMethod() throws FileNotFoundException { // IOException 的子類別
            // 可以拋出更具體的例外
        }
        
        // 錯誤示範（編譯錯誤）：
        // @Override
        // public void parentMethod() throws Exception {
        //     // 不能宣告比父類別更廣泛的例外
        // }
    }
}
```

#### 6.2.2 throw 語句

```java
public class ThrowDemo {
    
    public static void main(String[] args) {
        // 測試自定義例外
        BankAccount account = new BankAccount("12345", 1000);
        
        try {
            account.withdraw(1500);
        } catch (InsufficientFundsException e) {
            System.out.println("提款失敗: " + e.getMessage());
            System.out.println("帳戶餘額: " + e.getCurrentBalance());
            System.out.println("提款金額: " + e.getRequestedAmount());
        }
        
        try {
            validateAge(-5);
        } catch (InvalidAgeException e) {
            System.out.println("年齡驗證失敗: " + e.getMessage());
            e.printStackTrace();
        }
        
        // 測試例外鏈
        try {
            processOrder("INVALID_ORDER");
        } catch (OrderProcessingException e) {
            System.out.println("訂單處理失敗: " + e.getMessage());
            System.out.println("根本原因: " + e.getCause().getMessage());
        }
    }
    
    // 驗證方法，主動拋出例外
    public static void validateAge(int age) throws InvalidAgeException {
        if (age < 0) {
            throw new InvalidAgeException("年齡不能為負數: " + age);
        }
        if (age > 150) {
            throw new InvalidAgeException("年齡不能超過 150: " + age);
        }
        
        System.out.println("年齡驗證通過: " + age);
    }
    
    // 業務邏輯例外
    public static void processOrder(String orderId) throws OrderProcessingException {
        try {
            // 模擬訂單處理
            if (orderId.startsWith("INVALID")) {
                throw new IllegalArgumentException("無效的訂單 ID: " + orderId);
            }
            
            System.out.println("處理訂單: " + orderId);
            
        } catch (IllegalArgumentException e) {
            // 包裝並重新拋出更具業務意義的例外
            throw new OrderProcessingException("訂單處理失敗: " + orderId, e);
        }
    }
    
    // 條件式拋出例外
    public static void checkStatus(String status) {
        switch (status.toUpperCase()) {
            case "ACTIVE":
                System.out.println("狀態正常");
                break;
            case "INACTIVE":
                throw new IllegalStateException("帳戶未啟用");
            case "SUSPENDED":
                throw new IllegalStateException("帳戶已暫停");
            case "DELETED":
                throw new IllegalStateException("帳戶已刪除");
            default:
                throw new IllegalArgumentException("未知狀態: " + status);
        }
    }
}

// 自定義例外類別
class InsufficientFundsException extends Exception {
    private double currentBalance;
    private double requestedAmount;
    
    public InsufficientFundsException(String message, double currentBalance, double requestedAmount) {
        super(message);
        this.currentBalance = currentBalance;
        this.requestedAmount = requestedAmount;
    }
    
    public double getCurrentBalance() { return currentBalance; }
    public double getRequestedAmount() { return requestedAmount; }
}

class InvalidAgeException extends Exception {
    public InvalidAgeException(String message) {
        super(message);
    }
    
    public InvalidAgeException(String message, Throwable cause) {
        super(message, cause);
    }
}

class OrderProcessingException extends Exception {
    public OrderProcessingException(String message) {
        super(message);
    }
    
    public OrderProcessingException(String message, Throwable cause) {
        super(message, cause);
    }
}

// 銀行帳戶類別
class BankAccount {
    private String accountNumber;
    private double balance;
    
    public BankAccount(String accountNumber, double initialBalance) {
        this.accountNumber = accountNumber;
        this.balance = initialBalance;
    }
    
    public void withdraw(double amount) throws InsufficientFundsException {
        if (amount <= 0) {
            throw new IllegalArgumentException("提款金額必須大於 0");
        }
        
        if (amount > balance) {
            throw new InsufficientFundsException(
                "餘額不足，無法提款",
                balance,
                amount
            );
        }
        
        balance -= amount;
        System.out.println("提款成功，餘額: " + balance);
    }
    
    public double getBalance() {
        return balance;
    }
}
```

### 6.3 Checked vs Unchecked Exception

#### 6.3.1 例外分類詳解

```java
import java.io.*;
import java.util.*;

public class ExceptionTypesDemo {
    
    public static void main(String[] args) {
        // Checked Exception 示範
        demonstrateCheckedExceptions();
        
        // Unchecked Exception 示範
        demonstrateUncheckedExceptions();
        
        // 例外轉換
        demonstrateExceptionConversion();
    }
    
    private static void demonstrateCheckedExceptions() {
        System.out.println("=== Checked Exceptions ===");
        
        // 必須處理或宣告 throws
        
        // 1. IOException 系列
        try {
            FileReader reader = new FileReader("nonexistent.txt");
            BufferedReader buffered = new BufferedReader(reader);
            String line = buffered.readLine();
            buffered.close();
        } catch (FileNotFoundException e) {
            System.out.println("檔案不存在: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("IO 錯誤: " + e.getMessage());
        }
        
        // 2. ClassNotFoundException
        try {
            Class<?> clazz = Class.forName("com.nonexistent.MyClass");
        } catch (ClassNotFoundException e) {
            System.out.println("找不到類別: " + e.getMessage());
        }
        
        // 3. InterruptedException
        try {
            Thread.sleep(100);
        } catch (InterruptedException e) {
            System.out.println("執行緒被中斷: " + e.getMessage());
            Thread.currentThread().interrupt(); // 恢復中斷狀態
        }
        
        // 4. ParseException
        try {
            java.text.SimpleDateFormat sdf = new java.text.SimpleDateFormat("yyyy-MM-dd");
            Date date = sdf.parse("invalid-date");
        } catch (java.text.ParseException e) {
            System.out.println("日期解析錯誤: " + e.getMessage());
        }
        
        System.out.println();
    }
    
    private static void demonstrateUncheckedExceptions() {
        System.out.println("=== Unchecked Exceptions ===");
        
        // 不需要強制處理，但建議處理
        
        // 1. NullPointerException
        try {
            String str = null;
            int length = str.length();
        } catch (NullPointerException e) {
            System.out.println("空指標例外");
        }
        
        // 2. IndexOutOfBoundsException 系列
        try {
            List<String> list = Arrays.asList("A", "B", "C");
            String item = list.get(5);
        } catch (IndexOutOfBoundsException e) {
            System.out.println("索引超出範圍: " + e.getMessage());
        }
        
        try {
            int[] array = {1, 2, 3};
            int value = array[5];
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("陣列索引超出範圍: " + e.getMessage());
        }
        
        try {
            String str = "Hello";
            char ch = str.charAt(10);
        } catch (StringIndexOutOfBoundsException e) {
            System.out.println("字串索引超出範圍: " + e.getMessage());
        }
        
        // 3. NumberFormatException
        try {
            int number = Integer.parseInt("abc123");
        } catch (NumberFormatException e) {
            System.out.println("數字格式錯誤: " + e.getMessage());
        }
        
        // 4. ClassCastException
        try {
            Object obj = "Hello";
            Integer number = (Integer) obj;
        } catch (ClassCastException e) {
            System.out.println("類型轉換錯誤: " + e.getMessage());
        }
        
        // 5. IllegalArgumentException
        try {
            Thread.sleep(-1000);
        } catch (IllegalArgumentException e) {
            System.out.println("非法參數: " + e.getMessage());
        } catch (InterruptedException e) {
            System.out.println("執行緒中斷");
        }
        
        // 6. IllegalStateException
        try {
            Iterator<String> iterator = Arrays.asList("A", "B").iterator();
            iterator.remove(); // 在 next() 之前呼叫 remove()
        } catch (IllegalStateException e) {
            System.out.println("非法狀態: " + e.getMessage());
        }
        
        // 7. UnsupportedOperationException
        try {
            List<String> fixedList = Arrays.asList("A", "B", "C");
            fixedList.add("D");
        } catch (UnsupportedOperationException e) {
            System.out.println("不支援的操作: " + e.getMessage());
        }
        
        System.out.println();
    }
    
    private static void demonstrateExceptionConversion() {
        System.out.println("=== 例外轉換 ===");
        
        // 將 Checked Exception 轉換為 Unchecked Exception
        try {
            convertCheckedException();
        } catch (RuntimeException e) {
            System.out.println("轉換後的例外: " + e.getMessage());
            System.out.println("原始例外: " + e.getCause().getClass().getSimpleName());
        }
        
        // 將 Unchecked Exception 包裝為 Checked Exception
        try {
            wrapUncheckedException();
        } catch (ProcessingException e) {
            System.out.println("包裝後的例外: " + e.getMessage());
            System.out.println("原始例外: " + e.getCause().getClass().getSimpleName());
        }
    }
    
    private static void convertCheckedException() {
        try {
            // 模擬 Checked Exception
            throw new IOException("檔案處理錯誤");
        } catch (IOException e) {
            // 轉換為 Runtime Exception
            throw new RuntimeException("處理失敗", e);
        }
    }
    
    private static void wrapUncheckedException() throws ProcessingException {
        try {
            // 模擬 Runtime Exception
            int result = 10 / 0;
        } catch (ArithmeticException e) {
            // 包裝為 Checked Exception
            throw new ProcessingException("計算處理失敗", e);
        }
    }
}

// 自定義 Checked Exception
class ProcessingException extends Exception {
    public ProcessingException(String message, Throwable cause) {
        super(message, cause);
    }
}
```

### 6.4 try-with-resources

#### 6.4.1 自動資源管理

```java
import java.io.*;
import java.sql.*;
import java.util.Scanner;

public class TryWithResourcesDemo {
    
    public static void main(String[] args) {
        // 基本 try-with-resources
        basicTryWithResources();
        
        // 多重資源
        multipleResources();
        
        // 自定義可關閉資源
        customCloseable();
        
        // 對比傳統方式
        traditionalVsTryWithResources();
    }
    
    private static void basicTryWithResources() {
        System.out.println("=== 基本 try-with-resources ===");
        
        // 自動關閉 FileReader
        try (FileReader reader = new FileReader("sample.txt")) {
            int character;
            while ((character = reader.read()) != -1) {
                System.out.print((char) character);
            }
        } catch (FileNotFoundException e) {
            System.out.println("檔案不存在: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("讀取錯誤: " + e.getMessage());
        }
        // FileReader 自動關閉，不需要 finally 區塊
        
        System.out.println();
    }
    
    private static void multipleResources() {
        System.out.println("=== 多重資源 ===");
        
        // 同時管理多個資源
        try (FileInputStream fis = new FileInputStream("input.txt");
             FileOutputStream fos = new FileOutputStream("output.txt");
             BufferedInputStream bis = new BufferedInputStream(fis);
             BufferedOutputStream bos = new BufferedOutputStream(fos)) {
            
            // 複製檔案
            byte[] buffer = new byte[1024];
            int bytesRead;
            while ((bytesRead = bis.read(buffer)) != -1) {
                bos.write(buffer, 0, bytesRead);
            }
            
            System.out.println("檔案複製完成");
            
        } catch (FileNotFoundException e) {
            System.out.println("檔案不存在: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("IO 錯誤: " + e.getMessage());
        }
        // 所有資源按照宣告的反序自動關閉
        
        System.out.println();
    }
    
    private static void customCloseable() {
        System.out.println("=== 自定義可關閉資源 ===");
        
        try (MyResource resource1 = new MyResource("資源1");
             MyResource resource2 = new MyResource("資源2")) {
            
            resource1.doSomething();
            resource2.doSomething();
            
            // 模擬例外
            if (Math.random() > 0.5) {
                throw new RuntimeException("模擬業務例外");
            }
            
        } catch (Exception e) {
            System.out.println("捕捉到例外: " + e.getMessage());
        }
        // 資源會按照 resource2 -> resource1 的順序關閉
        
        System.out.println();
    }
    
    private static void traditionalVsTryWithResources() {
        System.out.println("=== 傳統方式 vs try-with-resources ===");
        
        // 傳統方式（容易出錯）
        System.out.println("傳統方式:");
        FileReader reader = null;
        try {
            reader = new FileReader("test.txt");
            // 處理檔案...
        } catch (FileNotFoundException e) {
            System.out.println("檔案不存在");
        } finally {
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e) {
                    System.out.println("關閉檔案時發生錯誤");
                }
            }
        }
        
        // try-with-resources 方式（簡潔且安全）
        System.out.println("try-with-resources 方式:");
        try (FileReader autoReader = new FileReader("test.txt")) {
            // 處理檔案...
        } catch (FileNotFoundException e) {
            System.out.println("檔案不存在");
        } catch (IOException e) {
            System.out.println("IO 錯誤");
        }
        
        System.out.println();
    }
    
    // 資料庫連線範例
    public static void databaseExample() {
        String url = "jdbc:mysql://localhost:3306/mydb";
        String username = "user";
        String password = "password";
        
        // 自動關閉 Connection, PreparedStatement, ResultSet
        try (Connection conn = DriverManager.getConnection(url, username, password);
             PreparedStatement stmt = conn.prepareStatement("SELECT * FROM users WHERE id = ?");) {
            
            stmt.setInt(1, 123);
            
            try (ResultSet rs = stmt.executeQuery()) {
                while (rs.next()) {
                    System.out.println("用戶: " + rs.getString("name"));
                }
            }
            
        } catch (SQLException e) {
            System.out.println("資料庫錯誤: " + e.getMessage());
        }
    }
    
    // Scanner 範例
    public static void scannerExample() {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("請輸入您的姓名: ");
            String name = scanner.nextLine();
            System.out.println("您好, " + name + "!");
        }
        // Scanner 自動關閉，包括底層的 InputStream
    }
}

// 自定義可關閉資源
class MyResource implements AutoCloseable {
    private String name;
    private boolean isOpen;
    
    public MyResource(String name) {
        this.name = name;
        this.isOpen = true;
        System.out.println(name + " 已開啟");
    }
    
    public void doSomething() {
        if (!isOpen) {
            throw new IllegalStateException(name + " 已關閉");
        }
        System.out.println(name + " 正在工作...");
    }
    
    @Override
    public void close() throws Exception {
        if (isOpen) {
            isOpen = false;
            System.out.println(name + " 已關閉");
            
            // 模擬關閉時的例外
            if (name.contains("資源2")) {
                throw new Exception(name + " 關閉時發生例外");
            }
        }
    }
}

// 進階資源管理範例
class ResourceManager implements AutoCloseable {
    private final String resourceId;
    private boolean acquired = false;
    
    public ResourceManager(String resourceId) throws Exception {
        this.resourceId = resourceId;
        acquire();
    }
    
    private void acquire() throws Exception {
        // 模擬資源取得
        System.out.println("取得資源: " + resourceId);
        acquired = true;
        
        // 模擬取得失敗
        if (resourceId.contains("FAIL")) {
            throw new Exception("無法取得資源: " + resourceId);
        }
    }
    
    public void use() {
        if (!acquired) {
            throw new IllegalStateException("資源尚未取得");
        }
        System.out.println("使用資源: " + resourceId);
    }
    
    @Override
    public void close() {
        if (acquired) {
            System.out.println("釋放資源: " + resourceId);
            acquired = false;
        }
    }
}
```

### 6.5 認證考點與陷阱題

#### 6.5.1 例外捕捉順序

```java
public class ExceptionCatchOrderTest {
    
    public static void main(String[] args) {
        // 正確的捕捉順序
        correctCatchOrder();
        
        // 錯誤示範
        // incorrectCatchOrder(); // 這會導致編譯錯誤
        
        // 多重例外處理（Java 7+）
        multiCatchSyntax();
        
        // finally 執行順序
        finallyExecutionOrder();
    }
    
    private static void correctCatchOrder() {
        System.out.println("=== 正確的捕捉順序 ===");
        
        try {
            throwException(1);
        } catch (FileNotFoundException e) {
            // 最具體的例外放在前面
            System.out.println("捕捉到 FileNotFoundException");
        } catch (IOException e) {
            // 較廣泛的例外放在中間
            System.out.println("捕捉到 IOException");
        } catch (Exception e) {
            // 最廣泛的例外放在最後
            System.out.println("捕捉到 Exception");
        }
    }
    
    /*
    // 這會導致編譯錯誤：Unreachable catch block
    private static void incorrectCatchOrder() {
        try {
            throwException(1);
        } catch (Exception e) {
            // Exception 太廣泛，放在前面會使後面的 catch 永遠無法執行
            System.out.println("捕捉到 Exception");
        } catch (IOException e) {
            // 編譯錯誤：這行永遠不會執行
            System.out.println("捕捉到 IOException");
        }
    }
    */
    
    private static void multiCatchSyntax() {
        System.out.println("\n=== 多重例外處理（Java 7+）===");
        
        for (int i = 1; i <= 3; i++) {
            try {
                throwException(i);
            } catch (FileNotFoundException | IllegalArgumentException e) {
                // 同時捕捉多種例外類型
                System.out.println("捕捉到檔案或參數例外: " + e.getClass().getSimpleName());
            } catch (IOException e) {
                System.out.println("捕捉到 IO 例外: " + e.getMessage());
            }
        }
    }
    
    private static void finallyExecutionOrder() {
        System.out.println("\n=== finally 執行順序 ===");
        
        System.out.println("結果: " + testFinallyReturn());
        System.out.println("結果: " + testFinallyException());
    }
    
    // finally 與 return 的執行順序（認證重點）
    private static int testFinallyReturn() {
        try {
            System.out.println("try 區塊");
            return 1;
        } catch (Exception e) {
            System.out.println("catch 區塊");
            return 2;
        } finally {
            System.out.println("finally 區塊");
            // 注意：finally 中的 return 會覆蓋 try/catch 中的 return
            // return 3; // 如果取消註解，方法會回傳 3
        }
    }
    
    // finally 與例外的關係（認證重點）
    private static String testFinallyException() {
        try {
            System.out.println("try 區塊開始");
            throw new RuntimeException("try 例外");
        } catch (RuntimeException e) {
            System.out.println("catch 區塊: " + e.getMessage());
            throw new RuntimeException("catch 例外");
        } finally {
            System.out.println("finally 區塊");
            // 如果 finally 拋出例外，會遮蔽 catch 中的例外
            // throw new RuntimeException("finally 例外");
            return "finally 回傳"; // finally 的 return 會遮蔽例外
        }
    }
    
    private static void throwException(int type) throws IOException {
        switch (type) {
            case 1:
                throw new FileNotFoundException("檔案不存在");
            case 2:
                throw new IOException("IO 錯誤");
            case 3:
                throw new IllegalArgumentException("參數錯誤");
            default:
                System.out.println("正常執行");
        }
    }
}
```

#### 6.5.2 try-with-resources 陷阱

```java
import java.io.Closeable;

public class TryWithResourcesTraps {
    
    public static void main(String[] args) {
        // 例外遮蔽
        suppressedExceptions();
        
        // 資源關閉順序
        resourceCloseOrder();
        
        // null 資源處理
        nullResourceHandling();
        
        // 初始化失敗
        initializationFailure();
    }
    
    private static void suppressedExceptions() {
        System.out.println("=== 例外遮蔽 ===");
        
        try (ProblematicResource resource = new ProblematicResource()) {
            resource.doWork();
        } catch (Exception e) {
            System.out.println("主要例外: " + e.getMessage());
            
            // 檢查被遮蔽的例外
            Throwable[] suppressed = e.getSuppressed();
            for (Throwable s : suppressed) {
                System.out.println("被遮蔽的例外: " + s.getMessage());
            }
        }
    }
    
    private static void resourceCloseOrder() {
        System.out.println("\n=== 資源關閉順序 ===");
        
        try (OrderedResource first = new OrderedResource("第一個");
             OrderedResource second = new OrderedResource("第二個");
             OrderedResource third = new OrderedResource("第三個")) {
            
            System.out.println("使用資源...");
            
        } catch (Exception e) {
            System.out.println("例外: " + e.getMessage());
        }
        // 關閉順序：第三個 -> 第二個 -> 第一個
    }
    
    private static void nullResourceHandling() {
        System.out.println("\n=== null 資源處理 ===");
        
        OrderedResource nullResource = null;
        
        try (OrderedResource resource = nullResource) {
            // null 資源不會呼叫 close()
            System.out.println("這行不會執行");
        } catch (Exception e) {
            System.out.println("例外: " + e.getMessage());
        }
        
        System.out.println("null 資源處理完成");
    }
    
    private static void initializationFailure() {
        System.out.println("\n=== 初始化失敗 ===");
        
        try (FailingResource resource = new FailingResource()) {
            System.out.println("這行不會執行");
        } catch (Exception e) {
            System.out.println("初始化失敗: " + e.getMessage());
        }
    }
    
    // 認證陷阱：變數範圍
    public static void variableScopeTest() {
        // 錯誤示範
        /*
        FileReader reader;
        try (reader = new FileReader("test.txt")) { // 編譯錯誤！
            // 資源變數必須在 try-with-resources 中宣告
        }
        */
        
        // 正確方式
        try (FileReader reader = new FileReader("test.txt")) {
            // reader 只在這個範圍內有效
        } catch (Exception e) {
            // reader 在這裡無法存取
        }
        // reader 在這裡也無法存取
    }
}

class ProblematicResource implements AutoCloseable {
    
    public void doWork() throws Exception {
        System.out.println("執行工作...");
        throw new Exception("工作執行時發生例外");
    }
    
    @Override
    public void close() throws Exception {
        System.out.println("關閉資源...");
        throw new Exception("關閉資源時發生例外");
    }
}

class OrderedResource implements AutoCloseable {
    private String name;
    
    public OrderedResource(String name) {
        this.name = name;
        System.out.println("建立資源: " + name);
    }
    
    @Override
    public void close() throws Exception {
        System.out.println("關閉資源: " + name);
    }
}

class FailingResource implements AutoCloseable {
    
    public FailingResource() throws Exception {
        System.out.println("嘗試建立 FailingResource...");
        throw new Exception("建立資源失敗");
    }
    
    @Override
    public void close() throws Exception {
        System.out.println("這個 close() 不會被呼叫");
    }
}
```

### 6.6 小練習與解析

**練習 6.1**：以下程式碼的輸出順序是什麼？

```java
public class ExceptionOrder {
    public static void main(String[] args) {
        System.out.println(test());
    }
    
    static int test() {
        try {
            System.out.print("A");
            return 1;
        } catch (Exception e) {
            System.out.print("B");
            return 2;
        } finally {
            System.out.print("C");
        }
    }
}
```

**解析**：輸出 "AC1"。try 區塊正常執行印出 A，準備回傳 1，但 finally 區塊仍會執行印出 C，最後回傳 1。

**練習 6.2**：這段程式碼是否能編譯成功？

```java
try {
    // 一些程式碼
} catch (IOException e) {
    // 處理 IOException
} catch (FileNotFoundException e) {
    // 處理 FileNotFoundException
}
```

**解析**：編譯失敗。FileNotFoundException 是 IOException 的子類別，應該放在 IOException 之前，否則永遠不會被捕捉到。

**練習 6.3**：try-with-resources 中，如果建構子拋出例外會如何？

```java
try (MyResource resource = new MyResource()) {
    // 使用資源
}
```

**解析**：如果建構子拋出例外，資源不會被建立，因此 close() 方法不會被呼叫。例外會直接傳播到外層。

---

## 7. 進階語法與認證內容

### 7.1 泛型 (Generics)

#### 7.1.1 泛型基礎概念

```java
import java.util.*;

public class GenericsBasicDemo {
    
    public static void main(String[] args) {
        // 泛型的目的：型別安全 + 避免型別轉換
        
        // 沒有泛型的問題（Java 5 之前）
        List rawList = new ArrayList();
        rawList.add("字串");
        rawList.add(123);
        rawList.add(true);
        
        // 需要手動型別轉換，容易出錯
        String str = (String) rawList.get(0); // 正確
        // String str2 = (String) rawList.get(1); // ClassCastException!
        
        // 使用泛型
        List<String> stringList = new ArrayList<>();
        stringList.add("安全的字串");
        // stringList.add(123); // 編譯錯誤！型別不匹配
        
        String safeStr = stringList.get(0); // 不需要型別轉換
        
        System.out.println("泛型確保型別安全: " + safeStr);
        
        // 泛型類別示範
        Box<String> stringBox = new Box<>("Hello");
        Box<Integer> intBox = new Box<>(42);
        Box<List<String>> listBox = new Box<>(Arrays.asList("A", "B", "C"));
        
        System.out.println("字串盒子: " + stringBox.getContent());
        System.out.println("整數盒子: " + intBox.getContent());
        System.out.println("列表盒子: " + listBox.getContent());
        
        // 泛型方法示範
        String[] stringArray = {"Apple", "Banana", "Cherry"};
        Integer[] intArray = {1, 2, 3, 4, 5};
        
        printArray(stringArray);
        printArray(intArray);
        
        // 泛型方法返回值
        String middle = getMiddleElement(stringArray);
        Integer middleInt = getMiddleElement(intArray);
        
        System.out.println("中間字串元素: " + middle);
        System.out.println("中間整數元素: " + middleInt);
    }
    
    // 泛型方法
    public static <T> void printArray(T[] array) {
        System.out.print("陣列內容: ");
        for (T element : array) {
            System.out.print(element + " ");
        }
        System.out.println();
    }
    
    // 帶返回值的泛型方法
    public static <T> T getMiddleElement(T[] array) {
        if (array.length == 0) return null;
        return array[array.length / 2];
    }
    
    // 多個型別參數的泛型方法
    public static <K, V> void printKeyValue(K key, V value) {
        System.out.println("Key: " + key + ", Value: " + value + 
                          " (Key類型: " + key.getClass().getSimpleName() + 
                          ", Value類型: " + value.getClass().getSimpleName() + ")");
    }
    
    // 使用範例
    public static void demonstrateMultipleTypeParameters() {
        printKeyValue("name", "張三");
        printKeyValue(1, "第一個");
        printKeyValue("active", true);
    }
}

// 泛型類別
class Box<T> {
    private T content;
    
    public Box(T content) {
        this.content = content;
    }
    
    public T getContent() {
        return content;
    }
    
    public void setContent(T content) {
        this.content = content;
    }
    
    @Override
    public String toString() {
        return "Box{content=" + content + ", type=" + 
               (content != null ? content.getClass().getSimpleName() : "null") + "}";
    }
}

// 多型別參數的泛型類別
class Pair<K, V> {
    private K key;
    private V value;
    
    public Pair(K key, V value) {
        this.key = key;
        this.value = value;
    }
    
    public K getKey() { return key; }
    public V getValue() { return value; }
    
    public void setKey(K key) { this.key = key; }
    public void setValue(V value) { this.value = value; }
    
    @Override
    public String toString() {
        return String.format("Pair{key=%s, value=%s}", key, value);
    }
}
```

#### 7.1.2 萬用字元 (Wildcards)

```java
import java.util.*;

public class WildcardsDemo {
    
    public static void main(String[] args) {
        // 萬用字元的三種形式
        
        // 1. 無界萬用字元 (?)
        unboundedWildcardDemo();
        
        // 2. 上界萬用字元 (? extends Type)
        upperBoundedWildcardDemo();
        
        // 3. 下界萬用字元 (? super Type)
        lowerBoundedWildcardDemo();
        
        // PECS 原則示範
        pecsDemo();
    }
    
    private static void unboundedWildcardDemo() {
        System.out.println("=== 無界萬用字元 (?) ===");
        
        List<String> stringList = Arrays.asList("A", "B", "C");
        List<Integer> intList = Arrays.asList(1, 2, 3);
        List<Double> doubleList = Arrays.asList(1.1, 2.2, 3.3);
        
        // ? 可以代表任何型別，但只能讀取為 Object
        printListSize(stringList);
        printListSize(intList);
        printListSize(doubleList);
        
        // 無法新增元素（除了 null）
        List<?> unknownList = stringList;
        // unknownList.add("新元素"); // 編譯錯誤！
        unknownList.add(null); // 只能加入 null
        
        Object firstElement = unknownList.get(0); // 只能讀取為 Object
        System.out.println("第一個元素: " + firstElement);
    }
    
    // 接受任何型別的 List
    public static void printListSize(List<?> list) {
        System.out.println("列表大小: " + list.size());
        // 只能呼叫不依賴型別參數的方法
        System.out.println("是否為空: " + list.isEmpty());
    }
    
    private static void upperBoundedWildcardDemo() {
        System.out.println("\n=== 上界萬用字元 (? extends) ===");
        
        List<Integer> intList = Arrays.asList(1, 2, 3, 4, 5);
        List<Double> doubleList = Arrays.asList(1.1, 2.2, 3.3);
        List<Float> floatList = Arrays.asList(1.1f, 2.2f, 3.3f);
        
        // ? extends Number 表示 Number 或其子類別
        double intSum = sumNumbers(intList);
        double doubleSum = sumNumbers(doubleList);
        double floatSum = sumNumbers(floatList);
        
        System.out.println("整數總和: " + intSum);
        System.out.println("浮點數總和: " + doubleSum);
        System.out.println("Float 總和: " + floatSum);
        
        // 協變性示範
        List<? extends Number> numberList = intList; // 可以指派
        Number first = numberList.get(0); // 可以讀取為 Number
        // numberList.add(new Integer(10)); // 編譯錯誤！無法新增
    }
    
    // 上界萬用字元：只能讀取，不能寫入（除了 null）
    public static double sumNumbers(List<? extends Number> numbers) {
        double sum = 0.0;
        for (Number num : numbers) {
            sum += num.doubleValue(); // 可以呼叫 Number 的方法
        }
        return sum;
    }
    
    private static void lowerBoundedWildcardDemo() {
        System.out.println("\n=== 下界萬用字元 (? super) ===");
        
        List<Object> objectList = new ArrayList<>();
        List<Number> numberList = new ArrayList<>();
        List<Integer> integerList = new ArrayList<>();
        
        // ? super Integer 表示 Integer 或其父類別
        addIntegers(objectList);   // Object 是 Integer 的父類別
        addIntegers(numberList);   // Number 是 Integer 的父類別
        // addIntegers(integerList); // Integer 本身也可以
        
        System.out.println("Object 列表: " + objectList);
        System.out.println("Number 列表: " + numberList);
        
        // 逆變性示範
        List<? super Integer> intSuperList = numberList; // 可以指派
        intSuperList.add(42); // 可以新增 Integer
        intSuperList.add(new Integer(100)); // 可以新增 Integer
        // Integer value = intSuperList.get(0); // 編譯錯誤！只能讀取為 Object
        Object value = intSuperList.get(0); // 只能讀取為 Object
    }
    
    // 下界萬用字元：可以寫入，但讀取只能為 Object
    public static void addIntegers(List<? super Integer> list) {
        list.add(1);
        list.add(2);
        list.add(3);
        // 可以新增 Integer 或其子類別
        // Integer value = list.get(0); // 編譯錯誤！
        Object value = list.get(0); // 只能讀取為 Object
    }
    
    private static void pecsDemo() {
        System.out.println("\n=== PECS 原則 (Producer Extends, Consumer Super) ===");
        
        List<Integer> intSource = Arrays.asList(1, 2, 3, 4, 5);
        List<Number> numberTarget = new ArrayList<>();
        List<Object> objectTarget = new ArrayList<>();
        
        // Producer Extends: 從來源讀取資料
        copyElements(intSource, numberTarget);
        copyElements(intSource, objectTarget);
        
        System.out.println("複製到 Number 列表: " + numberTarget);
        System.out.println("複製到 Object 列表: " + objectTarget);
    }
    
    // PECS 實作：source 是 producer (extends)，destination 是 consumer (super)
    public static <T> void copyElements(List<? extends T> source, List<? super T> destination) {
        for (T element : source) {
            destination.add(element);
        }
    }
}

// 實際應用範例：泛型集合工具
class CollectionUtils {
    
    // 找出數字集合中的最大值
    public static <T extends Comparable<T>> T max(Collection<T> collection) {
        if (collection.isEmpty()) {
            throw new IllegalArgumentException("集合不能為空");
        }
        
        T max = null;
        for (T element : collection) {
            if (max == null || element.compareTo(max) > 0) {
                max = element;
            }
        }
        return max;
    }
    
    // 檢查列表是否包含指定元素
    public static boolean contains(List<?> list, Object element) {
        return list.contains(element);
    }
    
    // 將來源列表的所有元素新增到目標列表
    public static <T> void addAll(List<? super T> destination, List<? extends T> source) {
        for (T element : source) {
            destination.add(element);
        }
    }
    
    // 測試方法
    public static void testUtilities() {
        List<Integer> intList = Arrays.asList(3, 1, 4, 1, 5, 9);
        List<String> stringList = Arrays.asList("apple", "banana", "cherry");
        
        System.out.println("整數最大值: " + max(intList));
        System.out.println("字串最大值: " + max(stringList));
        
        List<Number> numberList = new ArrayList<>();
        addAll(numberList, intList);
        System.out.println("新增後的數字列表: " + numberList);
    }
}
```

#### 7.1.3 型別擦除與限制

```java
import java.util.*;
import java.lang.reflect.*;

public class TypeErasureDemo {
    
    public static void main(String[] args) {
        // 型別擦除示範
        demonstrateTypeErasure();
        
        // 泛型限制
        demonstrateGenericLimitations();
        
        // 橋接方法
        demonstrateBridgeMethods();
        
        // 型別推斷
        demonstrateTypeInference();
    }
    
    private static void demonstrateTypeErasure() {
        System.out.println("=== 型別擦除 ===");
        
        List<String> stringList = new ArrayList<>();
        List<Integer> intList = new ArrayList<>();
        
        // 執行時期，兩個列表的型別相同
        System.out.println("stringList 型別: " + stringList.getClass());
        System.out.println("intList 型別: " + intList.getClass());
        System.out.println("型別相同: " + stringList.getClass().equals(intList.getClass()));
        
        // 型別資訊在執行時期被擦除
        // 泛型只在編譯時期存在
        
        // 使用反射檢查型別參數
        try {
            Method addMethod = ArrayList.class.getMethod("add", Object.class);
            System.out.println("add 方法參數型別: " + addMethod.getParameters()[0].getType());
        } catch (NoSuchMethodException e) {
            e.printStackTrace();
        }
    }
    
    private static void demonstrateGenericLimitations() {
        System.out.println("\n=== 泛型限制 ===");
        
        // 1. 無法建立泛型陣列
        // List<String>[] arrays = new List<String>[10]; // 編譯錯誤！
        List<String>[] arrays = new List[10]; // 只能這樣，會有 unchecked warning
        
        // 2. 無法使用基本型別作為型別參數
        // List<int> intList = new ArrayList<>(); // 編譯錯誤！
        List<Integer> integerList = new ArrayList<>(); // 必須使用包裝類別
        
        // 3. 無法建立型別參數的實例
        // 這在泛型類別中會是問題
        GenericFactory<String> factory = new GenericFactory<>();
        // String instance = factory.createInstance(); // 這會拋出例外
        
        // 4. 無法使用 instanceof 檢查參數化型別
        Object obj = new ArrayList<String>();
        System.out.println("是 ArrayList: " + (obj instanceof ArrayList));
        // System.out.println("是 ArrayList<String>: " + (obj instanceof ArrayList<String>)); // 編譯錯誤！
        
        // 5. 靜態變數不能使用型別參數
        // 這在泛型類別中會是問題，參見 GenericClass
        
        // 6. 泛型類別無法繼承自 Throwable
        // class MyException<T> extends Exception { } // 編譯錯誤！
    }
    
    private static void demonstrateBridgeMethods() {
        System.out.println("\n=== 橋接方法 ===");
        
        StringContainer container = new StringContainer();
        container.set("Hello World");
        
        // 檢查橋接方法
        Method[] methods = StringContainer.class.getDeclaredMethods();
        for (Method method : methods) {
            System.out.printf("方法: %s, 是否橋接: %s, 參數: %s%n",
                method.getName(),
                method.isBridge(),
                Arrays.toString(method.getParameterTypes())
            );
        }
    }
    
    private static void demonstrateTypeInference() {
        System.out.println("\n=== 型別推斷 ===");
        
        // Java 7+ 鑽石運算子
        List<String> list1 = new ArrayList<>(); // 推斷為 ArrayList<String>
        Map<String, Integer> map1 = new HashMap<>(); // 推斷為 HashMap<String, Integer>
        
        // 方法呼叫的型別推斷
        String result = GenericMethods.<String>identity("Hello"); // 明確指定
        String result2 = GenericMethods.identity("Hello"); // 自動推斷
        
        System.out.println("型別推斷結果: " + result2);
        
        // 複雜的型別推斷
        List<String> stringList = Arrays.asList("A", "B", "C");
        List<Integer> intList = Arrays.asList(1, 2, 3);
        
        // 推斷為 List<? extends Serializable & Comparable<?>>
        List<?> mixed = Math.random() > 0.5 ? stringList : intList;
        
        // Java 8+ 的改進型別推斷
        Optional<String> optional = Optional.of("test")
            .filter(s -> s.length() > 3)
            .map(String::toUpperCase);
    }
}

// 泛型工廠類別示範限制
class GenericFactory<T> {
    
    // 錯誤：無法建立型別參數的實例
    /*
    public T createInstance() {
        return new T(); // 編譯錯誤！
    }
    */
    
    // 正確：使用 Class 參數
    public T createInstance(Class<T> clazz) throws Exception {
        return clazz.getDeclaredConstructor().newInstance();
    }
    
    // 正確：使用工廠介面
    public T createInstance(Supplier<T> factory) {
        return factory.get();
    }
}

// 橋接方法示範
class Container<T> {
    private T value;
    
    public void set(T value) {
        this.value = value;
    }
    
    public T get() {
        return value;
    }
}

class StringContainer extends Container<String> {
    @Override
    public void set(String value) {
        System.out.println("設定字串值: " + value);
        super.set(value);
    }
    
    @Override
    public String get() {
        System.out.println("取得字串值");
        return super.get();
    }
}

// 泛型方法工具類別
class GenericMethods {
    
    // 身分函數
    public static <T> T identity(T input) {
        return input;
    }
    
    // 交換陣列元素
    public static <T> void swap(T[] array, int i, int j) {
        T temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
    
    // 安全的型別轉換
    @SuppressWarnings("unchecked")
    public static <T> T uncheckedCast(Object obj) {
        return (T) obj;
    }
}

// 泛型類別限制示範
class GenericClass<T> {
    private T instance;
    
    // 錯誤：靜態變數不能使用型別參數
    // private static T staticInstance; // 編譯錯誤！
    
    // 正確：靜態變數使用原始型別或萬用字元
    private static Object staticInstance;
    private static List<?> staticList;
    
    public GenericClass(T instance) {
        this.instance = instance;
    }
    
    public T getInstance() {
        return instance;
    }
}

// 函數介面用於工廠模式
@FunctionalInterface
interface Supplier<T> {
    T get();
}
```

### 7.2 Lambda 表達式與 Functional Interface

#### 7.2.1 Lambda 基礎語法

```java
import java.util.*;
import java.util.function.*;

public class LambdaBasicsDemo {
    
    public static void main(String[] args) {
        // Lambda 語法演進
        demonstrateLambdaSyntax();
        
        // 常用函數介面
        demonstrateFunctionalInterfaces();
        
        // 方法參照
        demonstrateMethodReferences();
        
        // 實際應用
        practicalExamples();
    }
    
    private static void demonstrateLambdaSyntax() {
        System.out.println("=== Lambda 語法演進 ===");
        
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "Diana");
        
        // 1. 傳統匿名類別
        Collections.sort(names, new Comparator<String>() {
            @Override
            public int compare(String a, String b) {
                return a.length() - b.length();
            }
        });
        System.out.println("匿名類別排序: " + names);
        
        // 2. Lambda 表達式 - 完整語法
        names = Arrays.asList("Alice", "Bob", "Charlie", "Diana");
        Collections.sort(names, (String a, String b) -> {
            return a.length() - b.length();
        });
        System.out.println("Lambda 完整語法: " + names);
        
        // 3. Lambda 表達式 - 簡化語法（型別推斷）
        names = Arrays.asList("Alice", "Bob", "Charlie", "Diana");
        Collections.sort(names, (a, b) -> a.length() - b.length());
        System.out.println("Lambda 簡化語法: " + names);
        
        // 4. 方法參照
        names = Arrays.asList("Alice", "Bob", "Charlie", "Diana");
        Collections.sort(names, Comparator.comparing(String::length));
        System.out.println("方法參照: " + names);
        
        // Lambda 語法變化
        System.out.println("\n--- Lambda 語法變化 ---");
        
        // 無參數
        Runnable task1 = () -> System.out.println("無參數 Lambda");
        
        // 單一參數（可省略括號）
        Consumer<String> printer1 = s -> System.out.println("列印: " + s);
        Consumer<String> printer2 = (s) -> System.out.println("列印: " + s);
        
        // 多參數
        BinaryOperator<Integer> adder = (a, b) -> a + b;
        
        // 單一表達式 vs 程式碼區塊
        Function<Integer, Integer> square1 = x -> x * x; // 單一表達式
        Function<Integer, Integer> square2 = x -> {      // 程式碼區塊
            int result = x * x;
            return result;
        };
        
        // 執行測試
        task1.run();
        printer1.accept("Hello");
        System.out.println("5 + 3 = " + adder.apply(5, 3));
        System.out.println("4 的平方 = " + square1.apply(4));
    }
    
    private static void demonstrateFunctionalInterfaces() {
        System.out.println("\n=== 常用函數介面 ===");
        
        // 1. Predicate<T> - 條件判斷
        Predicate<String> isLongName = name -> name.length() > 5;
        Predicate<String> startsWithA = name -> name.startsWith("A");
        
        System.out.println("Alice 是長名字: " + isLongName.test("Alice"));
        System.out.println("Alexander 是長名字: " + isLongName.test("Alexander"));
        
        // Predicate 組合
        Predicate<String> longAndStartsWithA = isLongName.and(startsWithA);
        System.out.println("Alexander 是長名字且以A開頭: " + longAndStartsWithA.test("Alexander"));
        
        // 2. Function<T, R> - 轉換函數
        Function<String, Integer> stringLength = String::length;
        Function<String, String> toUpperCase = String::toUpperCase;
        
        System.out.println("Hello 的長度: " + stringLength.apply("Hello"));
        System.out.println("hello 轉大寫: " + toUpperCase.apply("hello"));
        
        // Function 組合
        Function<String, Integer> upperCaseLength = toUpperCase.andThen(stringLength);
        System.out.println("world 轉大寫後的長度: " + upperCaseLength.apply("world"));
        
        // 3. Consumer<T> - 消費者
        Consumer<String> consolePrinter = System.out::println;
        Consumer<String> uppercasePrinter = s -> System.out.println(s.toUpperCase());
        
        consolePrinter.accept("正常列印");
        uppercasePrinter.accept("大寫列印");
        
        // Consumer 鏈接
        Consumer<String> combined = consolePrinter.andThen(uppercasePrinter);
        combined.accept("鏈接列印");
        
        // 4. Supplier<T> - 供應者
        Supplier<String> randomGreeting = () -> {
            String[] greetings = {"Hello", "Hi", "Hey", "Greetings"};
            return greetings[(int) (Math.random() * greetings.length)];
        };
        
        System.out.println("隨機問候: " + randomGreeting.get());
        
        // 5. BinaryOperator<T> - 二元運算
        BinaryOperator<Integer> max = Integer::max;
        BinaryOperator<String> concat = (a, b) -> a + " " + b;
        
        System.out.println("10 和 20 的最大值: " + max.apply(10, 20));
        System.out.println("字串連接: " + concat.apply("Hello", "World"));
        
        // 6. UnaryOperator<T> - 一元運算
        UnaryOperator<String> reverse = s -> new StringBuilder(s).reverse().toString();
        UnaryOperator<Integer> doubled = x -> x * 2;
        
        System.out.println("Hello 反轉: " + reverse.apply("Hello"));
        System.out.println("5 的兩倍: " + doubled.apply(5));
    }
    
    private static void demonstrateMethodReferences() {
        System.out.println("\n=== 方法參照 ===");
        
        List<String> names = Arrays.asList("alice", "bob", "charlie", "diana");
        
        // 1. 靜態方法參照 Class::staticMethod
        Function<String, Integer> parseInt = Integer::parseInt;
        System.out.println("字串轉整數: " + parseInt.apply("123"));
        
        // 2. 實例方法參照 object::instanceMethod
        String prefix = "Mr. ";
        Function<String, String> addPrefix = prefix::concat;
        System.out.println("加前綴: " + addPrefix.apply("Smith"));
        
        // 3. 特定型別的實例方法參照 Class::instanceMethod
        names.sort(String::compareToIgnoreCase);
        System.out.println("排序後: " + names);
        
        // 轉換為大寫
        names.replaceAll(String::toUpperCase);
        System.out.println("大寫: " + names);
        
        // 4. 建構子參照 Class::new
        Supplier<ArrayList<String>> listSupplier = ArrayList::new;
        Function<Integer, ArrayList<String>> listWithSize = ArrayList::new;
        
        ArrayList<String> newList1 = listSupplier.get();
        ArrayList<String> newList2 = listWithSize.apply(10);
        
        System.out.println("新列表1: " + newList1);
        System.out.println("新列表2 容量: " + newList2.size());
        
        // 陣列建構子參照
        Function<Integer, String[]> stringArrayCreator = String[]::new;
        String[] stringArray = stringArrayCreator.apply(5);
        System.out.println("字串陣列長度: " + stringArray.length);
    }
    
    private static void practicalExamples() {
        System.out.println("\n=== 實際應用範例 ===");
        
        List<Person> people = Arrays.asList(
            new Person("Alice", 25, "Engineer"),
            new Person("Bob", 30, "Manager"),
            new Person("Charlie", 35, "Engineer"),
            new Person("Diana", 28, "Designer"),
            new Person("Eve", 32, "Manager")
        );
        
        // 1. 過濾和轉換
        System.out.println("工程師列表:");
        people.stream()
              .filter(p -> p.getJob().equals("Engineer"))
              .map(Person::getName)
              .forEach(System.out::println);
        
        // 2. 排序
        System.out.println("\n按年齡排序:");
        people.stream()
              .sorted(Comparator.comparing(Person::getAge))
              .forEach(p -> System.out.println(p.getName() + " (" + p.getAge() + ")"));
        
        // 3. 分組
        System.out.println("\n按職業分組:");
        Map<String, List<Person>> groupedByJob = people.stream()
            .collect(Collectors.groupingBy(Person::getJob));
        
        groupedByJob.forEach((job, personList) -> {
            System.out.println(job + ": " + 
                personList.stream()
                          .map(Person::getName)
                          .collect(Collectors.joining(", ")));
        });
        
        // 4. 計算統計
        OptionalDouble averageAge = people.stream()
            .mapToInt(Person::getAge)
            .average();
        
        System.out.println("\n平均年齡: " + averageAge.orElse(0.0));
        
        // 5. 自定義函數介面
        Calculator calc = (a, b, operation) -> {
            switch (operation) {
                case "add": return a + b;
                case "subtract": return a - b;
                case "multiply": return a * b;
                case "divide": return b != 0 ? a / b : 0;
                default: return 0;
            }
        };
        
        System.out.println("\n計算器測試:");
        System.out.println("10 + 5 = " + calc.calculate(10, 5, "add"));
        System.out.println("10 - 5 = " + calc.calculate(10, 5, "subtract"));
        System.out.println("10 * 5 = " + calc.calculate(10, 5, "multiply"));
        System.out.println("10 / 5 = " + calc.calculate(10, 5, "divide"));
    }
}

// 輔助類別
class Person {
    private String name;
    private int age;
    private String job;
    
    public Person(String name, int age, String job) {
        this.name = name;
        this.age = age;
        this.job = job;
    }
    
    // Getters
    public String getName() { return name; }
    public int getAge() { return age; }
    public String job() { return job; }
    
    @Override
    public String toString() {
        return String.format("Person{name='%s', age=%d, job='%s'}", name, age, job);
    }
}

// 自定義函數介面
@FunctionalInterface
interface Calculator {
    double calculate(double a, double b, String operation);
}
```

### 7.3 Stream API

#### 7.3.1 Stream 基礎操作

```java
import java.util.*;
import java.util.stream.*;

public class StreamBasicsDemo {
    
    public static void main(String[] args) {
        // Stream 建立方式
        demonstrateStreamCreation();
        
        // 中間操作
        demonstrateIntermediateOperations();
        
        // 終端操作
        demonstrateTerminalOperations();
        
        // 數值 Stream
        demonstrateNumericStreams();
    }
    
    private static void demonstrateStreamCreation() {
        System.out.println("=== Stream 建立方式 ===");
        
        // 1. 從集合建立
        List<String> list = Arrays.asList("a", "b", "c", "d");
        Stream<String> streamFromList = list.stream();
        System.out.println("從 List 建立: " + streamFromList.collect(Collectors.toList()));
        
        // 2. 從陣列建立
        String[] array = {"x", "y", "z"};
        Stream<String> streamFromArray = Arrays.stream(array);
        System.out.println("從陣列建立: " + streamFromArray.collect(Collectors.toList()));
        
        // 3. 使用 Stream.of()
        Stream<Integer> streamOfNumbers = Stream.of(1, 2, 3, 4, 5);
        System.out.println("使用 of(): " + streamOfNumbers.collect(Collectors.toList()));
        
        // 4. 無限 Stream
        Stream<Double> randomNumbers = Stream.generate(Math::random).limit(5);
        System.out.println("隨機數字: " + randomNumbers.collect(Collectors.toList()));
        
        Stream<Integer> evenNumbers = Stream.iterate(0, n -> n + 2).limit(5);
        System.out.println("偶數數列: " + evenNumbers.collect(Collectors.toList()));
        
        // 5. 範圍 Stream
        IntStream range = IntStream.range(1, 6); // 1 到 5
        System.out.println("範圍 1-5: " + range.boxed().collect(Collectors.toList()));
        
        IntStream rangeClosed = IntStream.rangeClosed(1, 5); // 1 到 5（包含5）
        System.out.println("範圍 1-5（含5）: " + rangeClosed.boxed().collect(Collectors.toList()));
        
        // 6. 空 Stream
        Stream<String> emptyStream = Stream.empty();
        System.out.println("空 Stream 數量: " + emptyStream.count());
        
        // 7. 從 Optional 建立
        Optional<String> optional = Optional.of("hello");
        Stream<String> streamFromOptional = optional.stream();
        System.out.println("從 Optional 建立: " + streamFromOptional.collect(Collectors.toList()));
        
        // 8. 平行 Stream
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
        Stream<Integer> parallelStream = numbers.parallelStream();
        System.out.println("平行 Stream: " + parallelStream.collect(Collectors.toList()));
    }
    
    private static void demonstrateIntermediateOperations() {
        System.out.println("\n=== 中間操作（Intermediate Operations）===");
        
        List<String> words = Arrays.asList("apple", "banana", "cherry", "date", "elderberry", "fig");
        
        // 1. filter() - 過濾
        System.out.println("長度大於5的單字:");
        words.stream()
             .filter(word -> word.length() > 5)
             .forEach(System.out::println);
        
        // 2. map() - 轉換
        System.out.println("\n轉換為大寫:");
        words.stream()
             .map(String::toUpperCase)
             .forEach(System.out::println);
        
        // 3. flatMap() - 扁平化
        List<List<String>> listOfLists = Arrays.asList(
            Arrays.asList("a", "b"),
            Arrays.asList("c", "d"),
            Arrays.asList("e", "f")
        );
        
        System.out.println("\n扁平化操作:");
        listOfLists.stream()
                   .flatMap(List::stream)
                   .forEach(System.out::println);
        
        // 4. distinct() - 去重
        List<Integer> numbersWithDuplicates = Arrays.asList(1, 2, 2, 3, 3, 3, 4, 5);
        System.out.println("\n去除重複:");
        numbersWithDuplicates.stream()
                            .distinct()
                            .forEach(System.out::println);
        
        // 5. sorted() - 排序
        System.out.println("\n字母順序排序:");
        words.stream()
             .sorted()
             .forEach(System.out::println);
        
        System.out.println("\n按長度排序:");
        words.stream()
             .sorted(Comparator.comparing(String::length))
             .forEach(System.out::println);
        
        // 6. peek() - 檢查（除錯用）
        System.out.println("\n使用 peek 檢查:");
        words.stream()
             .filter(word -> word.startsWith("a"))
             .peek(word -> System.out.println("過濾後: " + word))
             .map(String::toUpperCase)
             .peek(word -> System.out.println("轉換後: " + word))
             .collect(Collectors.toList());
        
        // 7. limit() 和 skip()
        System.out.println("\n跳過前2個，取3個:");
        words.stream()
             .skip(2)
             .limit(3)
             .forEach(System.out::println);
        
        // 8. takeWhile() 和 dropWhile() - Java 9+
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        
        System.out.println("\ntakeWhile - 取直到條件不滿足:");
        numbers.stream()
               .takeWhile(n -> n < 6)
               .forEach(System.out::println);
        
        System.out.println("\ndropWhile - 丟棄直到條件不滿足:");
        numbers.stream()
               .dropWhile(n -> n < 6)
               .forEach(System.out::println);
    }
    
    private static void demonstrateTerminalOperations() {
        System.out.println("\n=== 終端操作（Terminal Operations）===");
        
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        
        // 1. forEach() - 執行動作
        System.out.print("forEach: ");
        numbers.stream().forEach(n -> System.out.print(n + " "));
        System.out.println();
        
        // 2. collect() - 收集結果
        List<Integer> evenNumbers = numbers.stream()
                                          .filter(n -> n % 2 == 0)
                                          .collect(Collectors.toList());
        System.out.println("偶數: " + evenNumbers);
        
        Set<Integer> uniqueNumbers = numbers.stream()
                                           .collect(Collectors.toSet());
        System.out.println("去重集合: " + uniqueNumbers);
        
        String joinedNumbers = numbers.stream()
                                     .map(String::valueOf)
                                     .collect(Collectors.joining(", "));
        System.out.println("連接字串: " + joinedNumbers);
        
        // 3. reduce() - 歸約操作
        Optional<Integer> sum = numbers.stream()
                                      .reduce((a, b) -> a + b);
        System.out.println("總和: " + sum.orElse(0));
        
        Integer product = numbers.stream()
                                .reduce(1, (a, b) -> a * b);
        System.out.println("乘積: " + product);
        
        Optional<Integer> max = numbers.stream()
                                      .reduce(Integer::max);
        System.out.println("最大值: " + max.orElse(0));
        
        // 4. count() - 計數
        long count = numbers.stream()
                           .filter(n -> n > 5)
                           .count();
        System.out.println("大於5的數字個數: " + count);
        
        // 5. anyMatch(), allMatch(), noneMatch() - 匹配檢查
        boolean hasEven = numbers.stream().anyMatch(n -> n % 2 == 0);
        boolean allPositive = numbers.stream().allMatch(n -> n > 0);
        boolean noneNegative = numbers.stream().noneMatch(n -> n < 0);
        
        System.out.println("有偶數: " + hasEven);
        System.out.println("全部正數: " + allPositive);
        System.out.println("沒有負數: " + noneNegative);
        
        // 6. findFirst(), findAny() - 尋找元素
        Optional<Integer> first = numbers.stream()
                                        .filter(n -> n > 5)
                                        .findFirst();
        System.out.println("第一個大於5的數: " + first.orElse(-1));
        
        Optional<Integer> any = numbers.stream()
                                      .filter(n -> n > 5)
                                      .findAny();
        System.out.println("任一個大於5的數: " + any.orElse(-1));
        
        // 7. min(), max() - 最值
        Optional<Integer> minimum = numbers.stream().min(Integer::compareTo);
        Optional<Integer> maximum = numbers.stream().max(Integer::compareTo);
        
        System.out.println("最小值: " + minimum.orElse(-1));
        System.out.println("最大值: " + maximum.orElse(-1));
        
        // 8. toArray() - 轉陣列
        Integer[] array = numbers.stream()
                                .filter(n -> n % 2 == 0)
                                .toArray(Integer[]::new);
        System.out.println("偶數陣列: " + Arrays.toString(array));
    }
    
    private static void demonstrateNumericStreams() {
        System.out.println("\n=== 數值 Stream ===");
        
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
        
        // IntStream
        IntStream intStream = numbers.stream().mapToInt(Integer::intValue);
        System.out.println("IntStream 總和: " + intStream.sum());
        
        // 重新建立 stream（stream 只能使用一次）
        IntStream intStream2 = numbers.stream().mapToInt(Integer::intValue);
        OptionalDouble average = intStream2.average();
        System.out.println("平均值: " + average.orElse(0.0));
        
        // IntStream 統計
        IntSummaryStatistics stats = numbers.stream()
                                           .mapToInt(Integer::intValue)
                                           .summaryStatistics();
        
        System.out.println("統計資訊:");
        System.out.println("  數量: " + stats.getCount());
        System.out.println("  總和: " + stats.getSum());
        System.out.println("  平均: " + stats.getAverage());
        System.out.println("  最小: " + stats.getMin());
        System.out.println("  最大: " + stats.getMax());
        
        // DoubleStream
        DoubleStream doubleStream = DoubleStream.of(1.1, 2.2, 3.3, 4.4, 5.5);
        System.out.println("DoubleStream 總和: " + doubleStream.sum());
        
        // LongStream
        LongStream longStream = LongStream.range(1, 11);
        System.out.println("1到10的總和: " + longStream.sum());
        
        // 數值 Stream 轉換
        List<Double> doubleList = IntStream.range(1, 6)
                                          .mapToDouble(i -> i * 1.5)
                                          .boxed()
                                          .collect(Collectors.toList());
        System.out.println("整數轉浮點數: " + doubleList);
    }
}
```

---

## 8. 多執行緒與並行處理

### 8.1 Thread 與 Runnable

#### 8.1.1 建立執行緒的方式

```java
public class ThreadCreationDemo {
    
    public static void main(String[] args) {
        System.out.println("主執行緒: " + Thread.currentThread().getName());
        
        // 方法 1: 繼承 Thread 類別
        MyThread thread1 = new MyThread("Thread-1");
        thread1.start();
        
        // 方法 2: 實作 Runnable 介面
        MyRunnable runnable = new MyRunnable("Runnable-1");
        Thread thread2 = new Thread(runnable);
        thread2.start();
        
        // 方法 3: 匿名類別
        Thread thread3 = new Thread(new Runnable() {
            @Override
            public void run() {
                for (int i = 1; i <= 5; i++) {
                    System.out.println("匿名執行緒: " + i);
                    try {
                        Thread.sleep(500);
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                        break;
                    }
                }
            }
        });
        thread3.setName("Anonymous-Thread");
        thread3.start();
        
        // 方法 4: Lambda 表達式
        Thread thread4 = new Thread(() -> {
            for (int i = 1; i <= 5; i++) {
                System.out.println("Lambda 執行緒: " + i);
                try {
                    Thread.sleep(600);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    break;
                }
            }
        });
        thread4.setName("Lambda-Thread");
        thread4.start();
        
        // 等待所有執行緒完成
        try {
            thread1.join();
            thread2.join();
            thread3.join();
            thread4.join();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        
        System.out.println("所有執行緒執行完畢");
    }
}

// 方法 1: 繼承 Thread 類別
class MyThread extends Thread {
    private String threadName;
    
    public MyThread(String name) {
        this.threadName = name;
        setName(name);
    }
    
    @Override
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println(threadName + ": " + i);
            try {
                Thread.sleep(400);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                System.out.println(threadName + " 被中斷");
                break;
            }
        }
        System.out.println(threadName + " 執行完畢");
    }
}

// 方法 2: 實作 Runnable 介面（推薦）
class MyRunnable implements Runnable {
    private String taskName;
    
    public MyRunnable(String name) {
        this.taskName = name;
    }
    
    @Override
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println(taskName + ": " + i + 
                " (執行緒: " + Thread.currentThread().getName() + ")");
            try {
                Thread.sleep(450);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                System.out.println(taskName + " 被中斷");
                break;
            }
        }
        System.out.println(taskName + " 執行完畢");
    }
}
```

#### 8.1.2 執行緒狀態與生命週期

```java
public class ThreadLifecycleDemo {
    
    public static void main(String[] args) throws InterruptedException {
        System.out.println("=== 執行緒生命週期示範 ===");
        
        LifecycleThread thread = new LifecycleThread();
        
        // NEW - 新建狀態
        System.out.println("建立後狀態: " + thread.getState());
        
        // RUNNABLE - 可執行狀態
        thread.start();
        Thread.sleep(100);
        System.out.println("啟動後狀態: " + thread.getState());
        
        // TIMED_WAITING - 計時等待狀態
        Thread.sleep(1100);
        System.out.println("睡眠中狀態: " + thread.getState());
        
        // BLOCKED - 阻塞狀態（等待鎖）
        synchronized (thread.getLock()) {
            Thread.sleep(100);
            System.out.println("同步區塊中，執行緒狀態: " + thread.getState());
        }
        
        // 等待執行緒結束
        thread.join();
        
        // TERMINATED - 終止狀態
        System.out.println("結束後狀態: " + thread.getState());
        
        // 執行緒中斷示範
        demonstrateInterruption();
        
        // 執行緒優先權示範
        demonstratePriority();
        
        // Daemon 執行緒示範
        demonstrateDaemonThread();
    }
    
    private static void demonstrateInterruption() throws InterruptedException {
        System.out.println("\n=== 執行緒中斷示範 ===");
        
        Thread worker = new Thread(() -> {
            try {
                for (int i = 1; i <= 10; i++) {
                    if (Thread.currentThread().isInterrupted()) {
                        System.out.println("執行緒被中斷，停止工作");
                        return;
                    }
                    
                    System.out.println("工作進度: " + i);
                    Thread.sleep(500);
                }
            } catch (InterruptedException e) {
                System.out.println("睡眠中被中斷");
                Thread.currentThread().interrupt(); // 恢復中斷狀態
            }
        });
        
        worker.start();
        Thread.sleep(2000);
        
        System.out.println("發送中斷信號");
        worker.interrupt();
        worker.join();
    }
    
    private static void demonstratePriority() throws InterruptedException {
        System.out.println("\n=== 執行緒優先權示範 ===");
        
        Thread highPriority = new Thread(() -> {
            for (int i = 1; i <= 5; i++) {
                System.out.println("高優先權執行緒: " + i);
                Thread.yield(); // 讓出 CPU 時間
            }
        });
        
        Thread lowPriority = new Thread(() -> {
            for (int i = 1; i <= 5; i++) {
                System.out.println("低優先權執行緒: " + i);
                Thread.yield();
            }
        });
        
        // 設定優先權（1-10，預設是5）
        highPriority.setPriority(Thread.MAX_PRIORITY); // 10
        lowPriority.setPriority(Thread.MIN_PRIORITY);   // 1
        
        lowPriority.start();
        highPriority.start();
        
        highPriority.join();
        lowPriority.join();
    }
    
    private static void demonstrateDaemonThread() throws InterruptedException {
        System.out.println("\n=== Daemon 執行緒示範 ===");
        
        Thread userThread = new Thread(() -> {
            for (int i = 1; i <= 3; i++) {
                System.out.println("用戶執行緒: " + i);
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    break;
                }
            }
            System.out.println("用戶執行緒結束");
        });
        
        Thread daemonThread = new Thread(() -> {
            while (!Thread.currentThread().isInterrupted()) {
                System.out.println("Daemon 執行緒運行中...");
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    break;
                }
            }
            System.out.println("Daemon 執行緒結束");
        });
        
        // 設為 Daemon 執行緒（必須在 start() 之前設定）
        daemonThread.setDaemon(true);
        
        userThread.start();
        daemonThread.start();
        
        userThread.join();
        System.out.println("主程式結束（Daemon 執行緒會自動終止）");
    }
}

class LifecycleThread extends Thread {
    private final Object lock = new Object();
    
    @Override
    public void run() {
        try {
            System.out.println("執行緒開始運行");
            
            // 進入 TIMED_WAITING 狀態
            Thread.sleep(1000);
            
            // 嘗試取得鎖，可能進入 BLOCKED 狀態
            synchronized (lock) {
                System.out.println("取得鎖，執行同步程式碼");
                Thread.sleep(500);
            }
            
            System.out.println("執行緒即將結束");
            
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            System.out.println("執行緒被中斷");
        }
    }
    
    public Object getLock() {
        return lock;
    }
}
```

### 8.2 同步與執行緒安全

#### 8.2.1 synchronized 關鍵字

```java
public class SynchronizedDemo {
    
    public static void main(String[] args) throws InterruptedException {
        // 同步方法示範
        demonstrateSynchronizedMethod();
        
        // 同步區塊示範
        demonstrateSynchronizedBlock();
        
        // 靜態同步示範
        demonstrateStaticSynchronization();
        
        // 死鎖示範
        demonstrateDeadlock();
    }
    
    private static void demonstrateSynchronizedMethod() throws InterruptedException {
        System.out.println("=== 同步方法示範 ===");
        
        Counter counter = new Counter();
        
        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) {
                counter.increment();
            }
        });
        
        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) {
                counter.increment();
            }
        });
        
        t1.start();
        t2.start();
        
        t1.join();
        t2.join();
        
        System.out.println("同步計數器最終值: " + counter.getValue());
        System.out.println("預期值: 2000");
    }
    
    private static void demonstrateSynchronizedBlock() throws InterruptedException {
        System.out.println("\n=== 同步區塊示範 ===");
        
        BankAccount account = new BankAccount(1000);
        
        // 同時提款的執行緒
        Thread[] threads = new Thread[10];
        for (int i = 0; i < threads.length; i++) {
            threads[i] = new Thread(() -> {
                for (int j = 0; j < 10; j++) {
                    account.withdraw(10);
                    try {
                        Thread.sleep(1);
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                        break;
                    }
                }
            });
            threads[i].start();
        }
        
        // 等待所有執行緒完成
        for (Thread thread : threads) {
            thread.join();
        }
        
        System.out.println("最終餘額: " + account.getBalance());
        System.out.println("預期餘額: 0");
    }
    
    private static void demonstrateStaticSynchronization() throws InterruptedException {
        System.out.println("\n=== 靜態同步示範 ===");
        
        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 5; i++) {
                StaticCounter.increment("Thread-1");
            }
        });
        
        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 5; i++) {
                StaticCounter.increment("Thread-2");
            }
        });
        
        t1.start();
        t2.start();
        
        t1.join();
        t2.join();
        
        System.out.println("靜態計數器最終值: " + StaticCounter.getValue());
    }
    
    private static void demonstrateDeadlock() {
        System.out.println("\n=== 死鎖示範 ===");
        
        Object lock1 = new Object();
        Object lock2 = new Object();
        
        Thread t1 = new Thread(() -> {
            synchronized (lock1) {
                System.out.println("執行緒1取得 lock1");
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
                
                System.out.println("執行緒1等待 lock2");
                synchronized (lock2) {
                    System.out.println("執行緒1取得 lock2");
                }
            }
        });
        
        Thread t2 = new Thread(() -> {
            synchronized (lock2) {
                System.out.println("執行緒2取得 lock2");
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
                
                System.out.println("執行緒2等待 lock1");
                synchronized (lock1) {
                    System.out.println("執行緒2取得 lock1");
                }
            }
        });
        
        t1.start();
        t2.start();
        
        // 等待一段時間後檢查是否死鎖
        try {
            Thread.sleep(2000);
            if (t1.isAlive() || t2.isAlive()) {
                System.out.println("檢測到死鎖！強制中斷執行緒");
                t1.interrupt();
                t2.interrupt();
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}

// 同步計數器
class Counter {
    private int count = 0;
    
    // 同步方法
    public synchronized void increment() {
        count++;
    }
    
    public synchronized int getValue() {
        return count;
    }
}

// 銀行帳戶（使用同步區塊）
class BankAccount {
    private double balance;
    private final Object lock = new Object();
    
    public BankAccount(double initialBalance) {
        this.balance = initialBalance;
    }
    
    public void withdraw(double amount) {
        synchronized (lock) {
            if (balance >= amount) {
                System.out.println(Thread.currentThread().getName() + 
                    " 提款前餘額: " + balance);
                
                // 模擬處理時間
                try {
                    Thread.sleep(1);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
                
                balance -= amount;
                System.out.println(Thread.currentThread().getName() + 
                    " 提款 " + amount + "，餘額: " + balance);
            } else {
                System.out.println(Thread.currentThread().getName() + 
                    " 餘額不足，無法提款 " + amount);
            }
        }
    }
    
    public synchronized double getBalance() {
        return balance;
    }
}

// 靜態同步計數器
class StaticCounter {
    private static int count = 0;
    
    // 靜態同步方法
    public static synchronized void increment(String threadName) {
        int temp = count;
        System.out.println(threadName + " 讀取值: " + temp);
        
        try {
            Thread.sleep(10);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        
        count = temp + 1;
        System.out.println(threadName + " 設定值: " + count);
    }
    
    public static synchronized int getValue() {
        return count;
    }
}
```

#### 8.2.2 volatile 關鍵字

```java
public class VolatileDemo {
    
    // volatile 變數保證可見性
    private static volatile boolean flag = false;
    private static volatile int sharedValue = 0;
    
    // 非 volatile 變數（對比用）
    private static boolean nonVolatileFlag = false;
    
    public static void main(String[] args) throws InterruptedException {
        // volatile 可見性示範
        demonstrateVisibility();
        
        // volatile 不保證原子性
        demonstrateNonAtomicity();
        
        // 正確使用 volatile 的場景
        demonstrateCorrectUsage();
    }
    
    private static void demonstrateVisibility() throws InterruptedException {
        System.out.println("=== volatile 可見性示範 ===");
        
        // 讀取執行緒
        Thread reader = new Thread(() -> {
            while (!flag) {
                // 等待 flag 變為 true
                // 如果沒有 volatile，這個迴圈可能永遠不會結束
            }
            System.out.println("讀取執行緒檢測到 flag 變為 true");
        });
        
        reader.start();
        
        Thread.sleep(1000);
        
        // 寫入執行緒
        Thread writer = new Thread(() -> {
            System.out.println("寫入執行緒設定 flag 為 true");
            flag = true;
        });
        
        writer.start();
        
        reader.join();
        writer.join();
    }
    
    private static void demonstrateNonAtomicity() throws InterruptedException {
        System.out.println("\n=== volatile 不保證原子性 ===");
        
        sharedValue = 0;
        
        Thread[] threads = new Thread[10];
        for (int i = 0; i < threads.length; i++) {
            threads[i] = new Thread(() -> {
                for (int j = 0; j < 1000; j++) {
                    sharedValue++; // 非原子操作
                }
            });
            threads[i].start();
        }
        
        for (Thread thread : threads) {
            thread.join();
        }
        
        System.out.println("volatile 變數最終值: " + sharedValue);
        System.out.println("預期值: 10000");
        System.out.println("說明: volatile 保證可見性，但不保證原子性");
    }
    
    private static void demonstrateCorrectUsage() throws InterruptedException {
        System.out.println("\n=== volatile 正確使用場景 ===");
        
        VolatileExample example = new VolatileExample();
        
        // 生產者執行緒
        Thread producer = new Thread(() -> {
            for (int i = 1; i <= 5; i++) {
                example.setValue(i * 10);
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    break;
                }
            }
            example.setFinished(true);
        });
        
        // 消費者執行緒
        Thread consumer = new Thread(() -> {
            while (!example.isFinished()) {
                int value = example.getValue();
                if (value > 0) {
                    System.out.println("消費者讀取到值: " + value);
                }
                try {
                    Thread.sleep(200);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    break;
                }
            }
            System.out.println("消費者檢測到生產結束");
        });
        
        producer.start();
        consumer.start();
        
        producer.join();
        consumer.join();
    }
}

class VolatileExample {
    private volatile int value = 0;
    private volatile boolean finished = false;
    
    public void setValue(int value) {
        this.value = value;
        System.out.println("生產者設定值: " + value);
    }
    
    public int getValue() {
        return value;
    }
    
    public void setFinished(boolean finished) {
        this.finished = finished;
        System.out.println("生產者設定完成標誌: " + finished);
    }
    
    public boolean isFinished() {
        return finished;
    }
}
```

### 8.3 java.util.concurrent 套件

#### 8.3.1 ExecutorService 與執行緒池

```java
import java.util.concurrent.*;
import java.util.*;

public class ExecutorServiceDemo {
    
    public static void main(String[] args) {
        // 不同類型的執行緒池
        demonstrateThreadPools();
        
        // Future 與 Callable
        demonstrateFutureAndCallable();
        
        // CompletableFuture
        demonstrateCompletableFuture();
        
        // 排程執行服務
        demonstrateScheduledExecutor();
    }
    
    private static void demonstrateThreadPools() {
        System.out.println("=== 執行緒池示範 ===");
        
        // 1. 固定大小執行緒池
        ExecutorService fixedPool = Executors.newFixedThreadPool(3);
        
        System.out.println("固定大小執行緒池 (3個執行緒):");
        for (int i = 1; i <= 6; i++) {
            final int taskId = i;
            fixedPool.submit(() -> {
                System.out.println("任務 " + taskId + " 執行 (執行緒: " + 
                    Thread.currentThread().getName() + ")");
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
                System.out.println("任務 " + taskId + " 完成");
            });
        }
        
        fixedPool.shutdown();
        
        // 2. 快取執行緒池
        ExecutorService cachedPool = Executors.newCachedThreadPool();
        
        System.out.println("\n快取執行緒池:");
        for (int i = 1; i <= 5; i++) {
            final int taskId = i;
            cachedPool.submit(() -> {
                System.out.println("快取池任務 " + taskId + " (執行緒: " + 
                    Thread.currentThread().getName() + ")");
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });
        }
        
        cachedPool.shutdown();
        
        // 3. 單一執行緒池
        ExecutorService singlePool = Executors.newSingleThreadExecutor();
        
        System.out.println("\n單一執行緒池:");
        for (int i = 1; i <= 3; i++) {
            final int taskId = i;
            singlePool.submit(() -> {
                System.out.println("單一池任務 " + taskId + " (執行緒: " + 
                    Thread.currentThread().getName() + ")");
                try {
                    Thread.sleep(300);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });
        }
        
        singlePool.shutdown();
        
        // 4. 自定義執行緒池
        ThreadPoolExecutor customPool = new ThreadPoolExecutor(
            2,                      // 核心執行緒數
            4,                      // 最大執行緒數
            60L,                    // 空閒時間
            TimeUnit.SECONDS,       // 時間單位
            new LinkedBlockingQueue<>(10),  // 工作佇列
            new ThreadFactory() {   // 執行緒工廠
                private int counter = 0;
                @Override
                public Thread newThread(Runnable r) {
                    return new Thread(r, "CustomThread-" + (++counter));
                }
            },
            new ThreadPoolExecutor.CallerRunsPolicy() // 拒絕策略
        );
        
        System.out.println("\n自定義執行緒池:");
        for (int i = 1; i <= 8; i++) {
            final int taskId = i;
            customPool.submit(() -> {
                System.out.println("自定義池任務 " + taskId + " (執行緒: " + 
                    Thread.currentThread().getName() + ")");
                try {
                    Thread.sleep(800);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });
        }
        
        customPool.shutdown();
        
        // 等待所有執行緒池關閉
        waitForTermination(fixedPool, "固定池");
        waitForTermination(cachedPool, "快取池");
        waitForTermination(singlePool, "單一池");
        waitForTermination(customPool, "自定義池");
    }
    
    private static void demonstrateFutureAndCallable() {
        System.out.println("\n=== Future 與 Callable 示範 ===");
        
        ExecutorService executor = Executors.newFixedThreadPool(3);
        
        // Callable 任務（有回傳值）
        Callable<Integer> calculationTask = () -> {
            System.out.println("開始計算... (執行緒: " + Thread.currentThread().getName() + ")");
            Thread.sleep(2000);
            int result = (int) (Math.random() * 100);
            System.out.println("計算完成，結果: " + result);
            return result;
        };
        
        // 提交多個任務
        List<Future<Integer>> futures = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            Future<Integer> future = executor.submit(calculationTask);
            futures.add(future);
        }
        
        // 取得結果
        for (int i = 0; i < futures.size(); i++) {
            try {
                Future<Integer> future = futures.get(i);
                System.out.println("任務 " + (i + 1) + " 狀態:");
                System.out.println("  是否完成: " + future.isDone());
                System.out.println("  是否取消: " + future.isCancelled());
                
                // 取得結果（會阻塞直到完成）
                Integer result = future.get(3, TimeUnit.SECONDS);
                System.out.println("  結果: " + result);
                
            } catch (TimeoutException e) {
                System.out.println("任務 " + (i + 1) + " 超時");
            } catch (InterruptedException | ExecutionException e) {
                System.out.println("任務 " + (i + 1) + " 發生錯誤: " + e.getMessage());
            }
        }
        
        executor.shutdown();
        waitForTermination(executor, "Future示範");
    }
    
    private static void demonstrateCompletableFuture() {
        System.out.println("\n=== CompletableFuture 示範 ===");
        
        // 異步計算
        CompletableFuture<String> future1 = CompletableFuture.supplyAsync(() -> {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            return "Hello";
        });
        
        CompletableFuture<String> future2 = CompletableFuture.supplyAsync(() -> {
            try {
                Thread.sleep(1500);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            return "World";
        });
        
        // 組合兩個 Future
        CompletableFuture<String> combinedFuture = future1
            .thenCombine(future2, (s1, s2) -> s1 + " " + s2)
            .thenApply(String::toUpperCase)
            .thenApply(s -> s + "!");
        
        try {
            String result = combinedFuture.get();
            System.out.println("組合結果: " + result);
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
        
        // 異步鏈式操作
        CompletableFuture<Void> chainFuture = CompletableFuture
            .supplyAsync(() -> {
                System.out.println("步驟1: 取得資料");
                return "原始資料";
            })
            .thenApplyAsync(data -> {
                System.out.println("步驟2: 處理資料 - " + data);
                return data.toUpperCase();
            })
            .thenApplyAsync(processedData -> {
                System.out.println("步驟3: 轉換資料 - " + processedData);
                return processedData + " - 已處理";
            })
            .thenAcceptAsync(finalData -> {
                System.out.println("步驟4: 儲存結果 - " + finalData);
            });
        
        try {
            chainFuture.get();
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
        
        // 等待所有任務完成
        CompletableFuture<Void> allOf = CompletableFuture.allOf(
            CompletableFuture.runAsync(() -> {
                try { Thread.sleep(1000); } catch (InterruptedException e) {}
                System.out.println("任務A完成");
            }),
            CompletableFuture.runAsync(() -> {
                try { Thread.sleep(1500); } catch (InterruptedException e) {}
                System.out.println("任務B完成");
            }),
            CompletableFuture.runAsync(() -> {
                try { Thread.sleep(800); } catch (InterruptedException e) {}
                System.out.println("任務C完成");
            })
        );
        
        try {
            allOf.get();
            System.out.println("所有任務都完成了");
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
    }
    
    private static void demonstrateScheduledExecutor() {
        System.out.println("\n=== 排程執行服務示範 ===");
        
        ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(2);
        
        // 延遲執行
        System.out.println("排程延遲任務...");
        scheduler.schedule(() -> {
            System.out.println("延遲任務執行 (延遲2秒)");
        }, 2, TimeUnit.SECONDS);
        
        // 固定頻率執行
        System.out.println("排程固定頻率任務...");
        ScheduledFuture<?> fixedRateTask = scheduler.scheduleAtFixedRate(() -> {
            System.out.println("固定頻率任務 " + new Date());
        }, 1, 3, TimeUnit.SECONDS);
        
        // 固定延遲執行
        System.out.println("排程固定延遲任務...");
        ScheduledFuture<?> fixedDelayTask = scheduler.scheduleWithFixedDelay(() -> {
            System.out.println("固定延遲任務 " + new Date());
            try {
                Thread.sleep(1000); // 模擬任務執行時間
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }, 2, 2, TimeUnit.SECONDS);
        
        // 運行10秒後停止
        scheduler.schedule(() -> {
            System.out.println("停止排程任務");
            fixedRateTask.cancel(false);
            fixedDelayTask.cancel(false);
            scheduler.shutdown();
        }, 10, TimeUnit.SECONDS);
        
        waitForTermination(scheduler, "排程器");
    }
    
    private static void waitForTermination(ExecutorService executor, String name) {
        try {
            if (!executor.awaitTermination(10, TimeUnit.SECONDS)) {
                System.out.println(name + " 強制關閉");
                executor.shutdownNow();
            } else {
                System.out.println(name + " 正常關閉");
            }
        } catch (InterruptedException e) {
            executor.shutdownNow();
            Thread.currentThread().interrupt();
        }
    }
}
```

### 8.4 並發集合與原子類別

#### 8.4.1 並發集合

```java
import java.util.concurrent.*;
import java.util.*;

public class ConcurrentCollectionsDemo {
    
    public static void main(String[] args) throws InterruptedException {
        // ConcurrentHashMap
        demonstrateConcurrentHashMap();
        
        // BlockingQueue
        demonstrateBlockingQueue();
        
        // CopyOnWriteArrayList
        demonstrateCopyOnWriteArrayList();
        
        // ConcurrentLinkedQueue
        demonstrateConcurrentLinkedQueue();
    }
    
    private static void demonstrateConcurrentHashMap() throws InterruptedException {
        System.out.println("=== ConcurrentHashMap 示範 ===");
        
        ConcurrentHashMap<String, Integer> concurrentMap = new ConcurrentHashMap<>();
        
        // 多執行緒同時寫入
        ExecutorService executor = Executors.newFixedThreadPool(4);
        
        for (int i = 0; i < 4; i++) {
            final int threadId = i;
            executor.submit(() -> {
                for (int j = 0; j < 1000; j++) {
                    String key = "key-" + (threadId * 1000 + j);
                    concurrentMap.put(key, j);
                }
                System.out.println("執行緒 " + threadId + " 完成寫入");
            });
        }
        
        executor.shutdown();
        executor.awaitTermination(5, TimeUnit.SECONDS);
        
        System.out.println("ConcurrentHashMap 大小: " + concurrentMap.size());
        
        // 原子操作示範
        ConcurrentHashMap<String, Integer> counter = new ConcurrentHashMap<>();
        
        ExecutorService counterExecutor = Executors.newFixedThreadPool(10);
        
        for (int i = 0; i < 10; i++) {
            final String threadName = "Thread-" + i;
            counterExecutor.submit(() -> {
                for (int j = 0; j < 100; j++) {
                    // 原子性增加計數
                    counter.compute("count", (key, val) -> (val == null) ? 1 : val + 1);
                    
                    // 如果不存在則放入
                    counter.putIfAbsent(threadName, 0);
                    counter.compute(threadName, (key, val) -> val + 1);
                }
            });
        }
        
        counterExecutor.shutdown();
        counterExecutor.awaitTermination(5, TimeUnit.SECONDS);
        
        System.out.println("總計數: " + counter.get("count"));
        System.out.println("各執行緒計數: " + counter);
    }
    
    private static void demonstrateBlockingQueue() throws InterruptedException {
        System.out.println("\n=== BlockingQueue 示範 ===");
        
        BlockingQueue<String> queue = new ArrayBlockingQueue<>(5);
        
        // 生產者
        Thread producer = new Thread(() -> {
            try {
                for (int i = 1; i <= 10; i++) {
                    String product = "產品-" + i;
                    queue.put(product); // 如果佇列滿了會阻塞
                    System.out.println("生產: " + product + " (佇列大小: " + queue.size() + ")");
                    Thread.sleep(300);
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });
        
        // 消費者
        Thread consumer = new Thread(() -> {
            try {
                while (true) {
                    String product = queue.take(); // 如果佇列空了會阻塞
                    System.out.println("消費: " + product + " (佇列大小: " + queue.size() + ")");
                    Thread.sleep(500);
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                System.out.println("消費者被中斷");
            }
        });
        
        producer.start();
        consumer.start();
        
        producer.join();
        Thread.sleep(3000); // 讓消費者處理剩餘產品
        consumer.interrupt();
        
        // 其他 BlockingQueue 實作
        demonstrateOtherBlockingQueues();
    }
    
    private static void demonstrateOtherBlockingQueues() throws InterruptedException {
        System.out.println("\n--- 其他 BlockingQueue 實作 ---");
        
        // LinkedBlockingQueue - 可選容量
        BlockingQueue<Integer> linkedQueue = new LinkedBlockingQueue<>(3);
        
        // PriorityBlockingQueue - 優先權佇列
        BlockingQueue<Task> priorityQueue = new PriorityBlockingQueue<>();
        
        // 新增優先權任務
        priorityQueue.offer(new Task("低優先權任務", 1));
        priorityQueue.offer(new Task("高優先權任務", 10));
        priorityQueue.offer(new Task("中優先權任務", 5));
        
        System.out.println("優先權佇列任務執行順序:");
        while (!priorityQueue.isEmpty()) {
            Task task = priorityQueue.poll();
            System.out.println("執行: " + task);
        }
        
        // DelayQueue - 延遲佇列
        BlockingQueue<DelayedTask> delayQueue = new DelayQueue<>();
        long currentTime = System.currentTimeMillis();
        
        delayQueue.offer(new DelayedTask("任務1", currentTime + 3000));
        delayQueue.offer(new DelayedTask("任務2", currentTime + 1000));
        delayQueue.offer(new DelayedTask("任務3", currentTime + 2000));
        
        System.out.println("\n延遲佇列任務執行:");
        for (int i = 0; i < 3; i++) {
            DelayedTask task = delayQueue.take();
            System.out.println("執行: " + task.getName() + " 在 " + new Date());
        }
    }
    
    private static void demonstrateCopyOnWriteArrayList() throws InterruptedException {
        System.out.println("\n=== CopyOnWriteArrayList 示範 ===");
        
        CopyOnWriteArrayList<String> cowList = new CopyOnWriteArrayList<>();
        
        // 初始化一些資料
        cowList.add("初始元素1");
        cowList.add("初始元素2");
        cowList.add("初始元素3");
        
        ExecutorService executor = Executors.newFixedThreadPool(3);
        
        // 讀取執行緒
        executor.submit(() -> {
            for (int i = 0; i < 10; i++) {
                System.out.println("讀取執行緒 - 列表內容: " + cowList);
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    break;
                }
            }
        });
        
        // 寫入執行緒1
        executor.submit(() -> {
            for (int i = 0; i < 5; i++) {
                String element = "寫入元素-A" + i;
                cowList.add(element);
                System.out.println("寫入執行緒A新增: " + element);
                try {
                    Thread.sleep(800);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    break;
                }
            }
        });
        
        // 寫入執行緒2
        executor.submit(() -> {
            for (int i = 0; i < 3; i++) {
                String element = "寫入元素-B" + i;
                cowList.add(element);
                System.out.println("寫入執行緒B新增: " + element);
                try {
                    Thread.sleep(1200);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    break;
                }
            }
        });
        
        executor.shutdown();
        executor.awaitTermination(10, TimeUnit.SECONDS);
        
        System.out.println("最終列表: " + cowList);
    }
    
    private static void demonstrateConcurrentLinkedQueue() throws InterruptedException {
        System.out.println("\n=== ConcurrentLinkedQueue 示範 ===");
        
        ConcurrentLinkedQueue<String> queue = new ConcurrentLinkedQueue<>();
        
        ExecutorService executor = Executors.newFixedThreadPool(4);
        
        // 生產者執行緒
        for (int i = 0; i < 2; i++) {
            final int producerId = i;
            executor.submit(() -> {
                for (int j = 0; j < 5; j++) {
                    String item = "Item-" + producerId + "-" + j;
                    queue.offer(item);
                    System.out.println("生產者" + producerId + " 新增: " + item);
                    try {
                        Thread.sleep(200);
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                        break;
                    }
                }
            });
        }
        
        // 消費者執行緒
        for (int i = 0; i < 2; i++) {
            final int consumerId = i;
            executor.submit(() -> {
                for (int j = 0; j < 5; j++) {
                    String item = queue.poll();
                    if (item != null) {
                        System.out.println("消費者" + consumerId + " 取得: " + item);
                    } else {
                        System.out.println("消費者" + consumerId + " 佇列為空");
                        j--; // 重試
                    }
                    try {
                        Thread.sleep(300);
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                        break;
                    }
                }
            });
        }
        
        executor.shutdown();
        executor.awaitTermination(5, TimeUnit.SECONDS);
        
        System.out.println("剩餘佇列內容: " + queue);
    }
}

// 優先權任務
class Task implements Comparable<Task> {
    private String name;
    private int priority;
    
    public Task(String name, int priority) {
        this.name = name;
        this.priority = priority;
    }
    
    @Override
    public int compareTo(Task other) {
        return Integer.compare(other.priority, this.priority); // 高優先權在前
    }
    
    @Override
    public String toString() {
        return name + " (優先權: " + priority + ")";
    }
}

// 延遲任務
class DelayedTask implements Delayed {
    private String name;
    private long executeTime;
    
    public DelayedTask(String name, long executeTime) {
        this.name = name;
        this.executeTime = executeTime;
    }
    
    @Override
    public long getDelay(TimeUnit unit) {
        return unit.convert(executeTime - System.currentTimeMillis(), TimeUnit.MILLISECONDS);
    }
    
    @Override
    public int compareTo(Delayed other) {
        return Long.compare(this.executeTime, ((DelayedTask) other).executeTime);
    }
    
    public String getName() {
        return name;
    }
}
```

#### 8.4.2 原子類別 (Atomic Classes)

```java
import java.util.concurrent.atomic.*;
import java.util.concurrent.*;

public class AtomicClassesDemo {
    
    // 原子基本型別
    private static AtomicInteger atomicCounter = new AtomicInteger(0);
    private static AtomicLong atomicLong = new AtomicLong(0);
    private static AtomicBoolean atomicFlag = new AtomicBoolean(false);
    
    // 原子參考型別
    private static AtomicReference<String> atomicString = new AtomicReference<>("初始值");
    private static AtomicStampedReference<String> stampedRef = 
        new AtomicStampedReference<>("初始值", 0);
    private static AtomicMarkableReference<String> markableRef = 
        new AtomicMarkableReference<>("初始值", false);
    
    // 原子陣列
    private static AtomicIntegerArray atomicArray = new AtomicIntegerArray(10);
    
    // 原子欄位更新器
    private static AtomicIntegerFieldUpdater<Person> ageUpdater = 
        AtomicIntegerFieldUpdater.newUpdater(Person.class, "age");
    
    public static void main(String[] args) throws InterruptedException {
        // 基本原子操作
        demonstrateBasicAtomicOperations();
        
        // CAS 操作
        demonstrateCompareAndSwap();
        
        // 原子參考與 ABA 問題
        demonstrateAtomicReference();
        
        // 原子陣列操作
        demonstrateAtomicArray();
        
        // 原子欄位更新器
        demonstrateAtomicFieldUpdater();
        
        // LongAdder 和 LongAccumulator
        demonstrateLongAdder();
    }
    
    private static void demonstrateBasicAtomicOperations() throws InterruptedException {
        System.out.println("=== 基本原子操作示範 ===");
        
        atomicCounter.set(0);
        
        ExecutorService executor = Executors.newFixedThreadPool(10);
        
        // 10個執行緒同時進行原子操作
        for (int i = 0; i < 10; i++) {
            executor.submit(() -> {
                for (int j = 0; j < 1000; j++) {
                    // 原子遞增
                    int newValue = atomicCounter.incrementAndGet();
                    
                    // 原子加法
                    atomicLong.addAndGet(1);
                    
                    if (j % 100 == 0) {
                        System.out.println(Thread.currentThread().getName() + 
                            " - Counter: " + newValue + ", Long: " + atomicLong.get());
                    }
                }
            });
        }
        
        executor.shutdown();
        executor.awaitTermination(5, TimeUnit.SECONDS);
        
        System.out.println("最終計數器值: " + atomicCounter.get());
        System.out.println("最終長整數值: " + atomicLong.get());
        System.out.println("預期值: 10000");
        
        // 其他原子操作
        System.out.println("\n其他原子操作:");
        System.out.println("getAndIncrement: " + atomicCounter.getAndIncrement());
        System.out.println("當前值: " + atomicCounter.get());
        System.out.println("decrementAndGet: " + atomicCounter.decrementAndGet());
        System.out.println("getAndAdd(5): " + atomicCounter.getAndAdd(5));
        System.out.println("當前值: " + atomicCounter.get());
    }
    
    private static void demonstrateCompareAndSwap() {
        System.out.println("\n=== Compare And Swap (CAS) 操作示範 ===");
        
        AtomicInteger casDemo = new AtomicInteger(100);
        
        System.out.println("初始值: " + casDemo.get());
        
        // CAS 成功的情況
        boolean success1 = casDemo.compareAndSet(100, 200);
        System.out.println("CAS(100->200): " + success1 + ", 當前值: " + casDemo.get());
        
        // CAS 失敗的情況
        boolean success2 = casDemo.compareAndSet(100, 300);
        System.out.println("CAS(100->300): " + success2 + ", 當前值: " + casDemo.get());
        
        // 自旋鎖實作
        SpinLockDemo spinLock = new SpinLockDemo();
        
        Thread t1 = new Thread(() -> {
            spinLock.lock();
            try {
                System.out.println("執行緒1取得鎖");
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            } finally {
                spinLock.unlock();
                System.out.println("執行緒1釋放鎖");
            }
        });
        
        Thread t2 = new Thread(() -> {
            spinLock.lock();
            try {
                System.out.println("執行緒2取得鎖");
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            } finally {
                spinLock.unlock();
                System.out.println("執行緒2釋放鎖");
            }
        });
        
        t1.start();
        try { Thread.sleep(100); } catch (InterruptedException e) {}
        t2.start();
        
        try {
            t1.join();
            t2.join();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
    
    private static void demonstrateAtomicReference() {
        System.out.println("\n=== 原子參考與 ABA 問題示範 ===");
        
        // 基本原子參考操作
        System.out.println("原子參考初始值: " + atomicString.get());
        
        boolean updated = atomicString.compareAndSet("初始值", "新值");
        System.out.println("更新成功: " + updated + ", 當前值: " + atomicString.get());
        
        // ABA 問題示範
        System.out.println("\nABA 問題示範:");
        AtomicReference<String> abaRef = new AtomicReference<>("A");
        
        Thread t1 = new Thread(() -> {
            String originalValue = abaRef.get();
            System.out.println("執行緒1讀取到: " + originalValue);
            
            // 模擬一些處理時間
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            
            // 嘗試更新（此時值可能已經改變過了）
            boolean success = abaRef.compareAndSet(originalValue, "A1");
            System.out.println("執行緒1 CAS 結果: " + success + " (值: " + abaRef.get() + ")");
        });
        
        Thread t2 = new Thread(() -> {
            try {
                Thread.sleep(500);
                
                // A -> B
                abaRef.compareAndSet("A", "B");
                System.out.println("執行緒2將 A 改為 B");
                
                Thread.sleep(100);
                
                // B -> A (回到原值，造成 ABA 問題)
                abaRef.compareAndSet("B", "A");
                System.out.println("執行緒2將 B 改回 A");
                
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });
        
        t1.start();
        t2.start();
        
        try {
            t1.join();
            t2.join();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        
        // 使用 AtomicStampedReference 解決 ABA 問題
        System.out.println("\n使用 AtomicStampedReference 解決 ABA:");
        
        int[] stamp = {0};
        String initialValue = stampedRef.get(stamp);
        System.out.println("初始值: " + initialValue + ", 版本: " + stamp[0]);
        
        // 更新值和版本號
        boolean stampSuccess = stampedRef.compareAndSet(
            initialValue, "新值", stamp[0], stamp[0] + 1);
        System.out.println("帶版本更新: " + stampSuccess);
        
        String currentValue = stampedRef.get(stamp);
        System.out.println("當前值: " + currentValue + ", 版本: " + stamp[0]);
    }
    
    private static void demonstrateAtomicArray() throws InterruptedException {
        System.out.println("\n=== 原子陣列操作示範 ===");
        
        // 初始化陣列
        for (int i = 0; i < atomicArray.length(); i++) {
            atomicArray.set(i, i * 10);
        }
        
        System.out.println("初始陣列:");
        printAtomicArray();
        
        ExecutorService executor = Executors.newFixedThreadPool(5);
        
        // 多執行緒修改陣列
        for (int i = 0; i < 5; i++) {
            final int threadId = i;
            executor.submit(() -> {
                for (int j = 0; j < atomicArray.length(); j++) {
                    // 原子遞增
                    int newValue = atomicArray.incrementAndGet(j);
                    
                    if (j == threadId) {
                        System.out.println("執行緒" + threadId + " 將索引" + j + 
                            " 增加到: " + newValue);
                    }
                }
            });
        }
        
        executor.shutdown();
        executor.awaitTermination(3, TimeUnit.SECONDS);
        
        System.out.println("最終陣列:");
        printAtomicArray();
        
        // CAS 操作
        System.out.println("\n陣列 CAS 操作:");
        int index = 3;
        int expected = atomicArray.get(index);
        int newValue = expected + 100;
        
        boolean success = atomicArray.compareAndSet(index, expected, newValue);
        System.out.println("索引" + index + " CAS(" + expected + "->" + newValue + "): " + 
            success + ", 實際值: " + atomicArray.get(index));
    }
    
    private static void demonstrateAtomicFieldUpdater() throws InterruptedException {
        System.out.println("\n=== 原子欄位更新器示範 ===");
        
        Person person = new Person("張三", 25);
        System.out.println("初始年齡: " + person.getAge());
        
        ExecutorService executor = Executors.newFixedThreadPool(3);
        
        // 多執行緒原子更新欄位
        for (int i = 0; i < 3; i++) {
            executor.submit(() -> {
                for (int j = 0; j < 5; j++) {
                    int newAge = ageUpdater.incrementAndGet(person);
                    System.out.println(Thread.currentThread().getName() + 
                        " 將年齡增加到: " + newAge);
                    try {
                        Thread.sleep(100);
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                        break;
                    }
                }
            });
        }
        
        executor.shutdown();
        executor.awaitTermination(5, TimeUnit.SECONDS);
        
        System.out.println("最終年齡: " + person.getAge());
    }
    
    private static void demonstrateLongAdder() throws InterruptedException {
        System.out.println("\n=== LongAdder 與 LongAccumulator 示範 ===");
        
        LongAdder adder = new LongAdder();
        
        // LongAdder 在高競爭環境下性能更好
        ExecutorService executor = Executors.newFixedThreadPool(10);
        long startTime = System.currentTimeMillis();
        
        for (int i = 0; i < 10; i++) {
            executor.submit(() -> {
                for (int j = 0; j < 100000; j++) {
                    adder.increment();
                }
            });
        }
        
        executor.shutdown();
        executor.awaitTermination(5, TimeUnit.SECONDS);
        
        long endTime = System.currentTimeMillis();
        System.out.println("LongAdder 結果: " + adder.sum());
        System.out.println("執行時間: " + (endTime - startTime) + "ms");
        
        // LongAccumulator 示範
        LongAccumulator accumulator = new LongAccumulator(Long::max, Long.MIN_VALUE);
        
        ExecutorService executor2 = Executors.newFixedThreadPool(5);
        
        for (int i = 0; i < 5; i++) {
            final int value = (i + 1) * 100;
            executor2.submit(() -> {
                accumulator.accumulate(value);
                System.out.println("累積值 " + value + ", 當前最大值: " + accumulator.get());
            });
        }
        
        executor2.shutdown();
        executor2.awaitTermination(3, TimeUnit.SECONDS);
        
        System.out.println("LongAccumulator 最終最大值: " + accumulator.get());
    }
    
    private static void printAtomicArray() {
        System.out.print("[");
        for (int i = 0; i < atomicArray.length(); i++) {
            System.out.print(atomicArray.get(i));
            if (i < atomicArray.length() - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }
}

// 自旋鎖實作
class SpinLockDemo {
    private AtomicReference<Thread> owner = new AtomicReference<>();
    
    public void lock() {
        Thread currentThread = Thread.currentThread();
        
        // 自旋等待
        while (!owner.compareAndSet(null, currentThread)) {
            // 可以加入 yield 減少 CPU 使用
            Thread.yield();
        }
    }
    
    public void unlock() {
        Thread currentThread = Thread.currentThread();
        owner.compareAndSet(currentThread, null);
    }
}

// 用於原子欄位更新器的類別
class Person {
    private String name;
    public volatile int age; // 必須是 volatile
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public String getName() { return name; }
    public int getAge() { return age; }
}
```

### 8.5 認證重點整理

#### 8.5.1 OCP 考試要點

**執行緒基礎概念：**
- Thread vs Runnable 的差異與選擇
- 執行緒狀態轉換：NEW → RUNNABLE → BLOCKED/WAITING/TIMED_WAITING → TERMINATED
- join(), sleep(), yield(), interrupt() 方法的使用
- 優先權設定與 Daemon 執行緒

**同步機制：**
- synchronized 關鍵字（方法級別與程式碼區塊）
- volatile 關鍵字的作用與限制
- wait(), notify(), notifyAll() 的正確使用
- 死鎖的產生條件與預防

**並發 API：**
- ExecutorService 與不同類型的執行緒池
- Callable 與 Future 的使用
- CompletableFuture 的異步程式設計
- 並發集合的特性與適用場景

#### 8.5.2 實務最佳實踐

```java
// 執行緒池最佳實踐
public class ThreadPoolBestPractices {
    
    // 推薦：自定義執行緒池而非 Executors 工廠方法
    public static ThreadPoolExecutor createCustomThreadPool(
            int corePoolSize,
            int maximumPoolSize,
            String threadNamePrefix) {
        
        return new ThreadPoolExecutor(
            corePoolSize,
            maximumPoolSize,
            60L, TimeUnit.SECONDS,
            new LinkedBlockingQueue<>(100),
            new ThreadFactory() {
                private final AtomicInteger counter = new AtomicInteger(0);
                @Override
                public Thread newThread(Runnable r) {
                    Thread t = new Thread(r, threadNamePrefix + "-" + counter.incrementAndGet());
                    t.setDaemon(false);
                    return t;
                }
            },
            new ThreadPoolExecutor.CallerRunsPolicy()
        );
    }
    
    // 正確的執行緒池關閉
    public static void shutdownThreadPool(ExecutorService executor) {
        executor.shutdown();
        try {
            if (!executor.awaitTermination(60, TimeUnit.SECONDS)) {
                executor.shutdownNow();
                if (!executor.awaitTermination(60, TimeUnit.SECONDS)) {
                    System.err.println("執行緒池未能正常關閉");
                }
            }
        } catch (InterruptedException ie) {
            executor.shutdownNow();
            Thread.currentThread().interrupt();
        }
    }
}
```

#### 8.5.3 常見陷阱與錯誤

```java
public class CommonConcurrencyPitfalls {
    
    // 錯誤：在 synchronized 方法中呼叫可能阻塞的操作
    public synchronized void badMethod() {
        try {
            // 錯誤：長時間阻塞會影響其他執行緒
            Thread.sleep(10000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
    
    // 正確：縮小同步範圍
    public void goodMethod() {
        // 非同步操作
        doSomeWork();
        
        synchronized (this) {
            // 只同步關鍵部分
            updateSharedState();
        }
    }
    
    // 錯誤：忽略 InterruptedException
    public void badInterruptHandling() {
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            // 錯誤：吞掉異常
        }
    }
    
    // 正確：適當處理中斷
    public void goodInterruptHandling() {
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            // 恢復中斷狀態
            Thread.currentThread().interrupt();
            // 執行清理工作
            cleanup();
        }
    }
    
    private void doSomeWork() { /* 實作 */ }
    private void updateSharedState() { /* 實作 */ }
    private void cleanup() { /* 實作 */ }
}
```

---

## 9. 專案實務應用

### 9.1 Maven 專案管理

#### 9.1.1 POM.xml 配置詳解

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    
    <modelVersion>4.0.0</modelVersion>
    
    <!-- 專案基本資訊 -->
    <groupId>com.tutorial</groupId>
    <artifactId>java-tutorial-project</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <packaging>jar</packaging>
    
    <name>Java Tutorial Project</name>
    <description>Java 教學專案範例</description>
    <url>https://github.com/example/java-tutorial</url>
    
    <!-- 專案屬性 -->
    <properties>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
        
        <!-- 依賴版本管理 -->
        <junit.version>5.10.0</junit.version>
        <mockito.version>5.5.0</mockito.version>
        <slf4j.version>2.0.9</slf4j.version>
        <logback.version>1.4.11</logback.version>
        <jackson.version>2.15.2</jackson.version>
        
        <!-- 插件版本 -->
        <maven.compiler.plugin.version>3.11.0</maven.compiler.plugin.version>
        <maven.surefire.plugin.version>3.1.2</maven.surefire.plugin.version>
        <maven.failsafe.plugin.version>3.1.2</maven.failsafe.plugin.version>
        <jacoco.plugin.version>0.8.10</jacoco.plugin.version>
    </properties>
    
    <!-- 依賴管理 -->
    <dependencies>
        <!-- 測試相關 -->
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>${junit.version}</version>
            <scope>test</scope>
        </dependency>
        
        <dependency>
            <groupId>org.mockito</groupId>
            <artifactId>mockito-core</artifactId>
            <version>${mockito.version}</version>
            <scope>test</scope>
        </dependency>
        
        <dependency>
            <groupId>org.mockito</groupId>
            <artifactId>mockito-junit-jupiter</artifactId>
            <version>${mockito.version}</version>
            <scope>test</scope>
        </dependency>
        
        <!-- 日誌相關 -->
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-api</artifactId>
            <version>${slf4j.version}</version>
        </dependency>
        
        <dependency>
            <groupId>ch.qos.logback</groupId>
            <artifactId>logback-classic</artifactId>
            <version>${logback.version}</version>
        </dependency>
        
        <!-- JSON 處理 -->
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
            <version>${jackson.version}</version>
        </dependency>
        
        <dependency>
            <groupId>com.fasterxml.jackson.datatype</groupId>
            <artifactId>jackson-datatype-jsr310</artifactId>
            <version>${jackson.version}</version>
        </dependency>
    </dependencies>
    
    <!-- 建置配置 -->
    <build>
        <plugins>
            <!-- 編譯插件 -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>${maven.compiler.plugin.version}</version>
                <configuration>
                    <source>21</source>
                    <target>21</target>
                    <encoding>UTF-8</encoding>
                    <compilerArgs>
                        <arg>--enable-preview</arg>
                    </compilerArgs>
                </configuration>
            </plugin>
            
            <!-- 單元測試插件 -->
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
            
            <!-- 整合測試插件 -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-failsafe-plugin</artifactId>
                <version>${maven.failsafe.plugin.version}</version>
                <configuration>
                    <includes>
                        <include>**/*IT.java</include>
                        <include>**/*Integration*.java</include>
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
            
            <!-- 代碼覆蓋率插件 -->
            <plugin>
                <groupId>org.jacoco</groupId>
                <artifactId>jacoco-maven-plugin</artifactId>
                <version>${jacoco.plugin.version}</version>
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
    
    <!-- 開發者資訊 -->
    <developers>
        <developer>
            <id>developer1</id>
            <name>開發者姓名</name>
            <email>developer@example.com</email>
            <organization>公司名稱</organization>
            <roles>
                <role>developer</role>
            </roles>
        </developer>
    </developers>
    
    <!-- SCM 資訊 -->
    <scm>
        <connection>scm:git:git://github.com/example/java-tutorial.git</connection>
        <developerConnection>scm:git:ssh://github.com/example/java-tutorial.git</developerConnection>
        <url>https://github.com/example/java-tutorial</url>
    </scm>
</project>
```

#### 9.1.2 Maven 生命週期與命令

```bash
# 清理專案
mvn clean

# 編譯主程式碼
mvn compile

# 執行測試
mvn test

# 打包專案
mvn package

# 安裝到本地倉庫
mvn install

# 部署到遠端倉庫
mvn deploy

# 常用組合命令
mvn clean compile
mvn clean test
mvn clean package
mvn clean install

# 跳過測試
mvn package -DskipTests
mvn package -Dmaven.test.skip=true

# 執行特定測試
mvn test -Dtest=StudentTest
mvn test -Dtest=*UtilTest

# 查看依賴樹
mvn dependency:tree

# 查看有效 POM
mvn help:effective-pom

# 查看專案資訊
mvn help:describe -Dplugin=compiler

# 更新依賴
mvn versions:display-dependency-updates

# 執行主類
mvn exec:java -Dexec.mainClass="com.tutorial.Main"
```

### 9.2 日誌系統 (Logging)

#### 9.2.1 Logback 配置

建立 `src/main/resources/logback.xml`：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    
    <!-- 控制台輸出 -->
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
            <charset>UTF-8</charset>
        </encoder>
    </appender>
    
    <!-- 檔案輸出 -->
    <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>logs/application.log</file>
        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
            <charset>UTF-8</charset>
        </encoder>
        
        <!-- 滾動策略 -->
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>logs/application.%d{yyyy-MM-dd}.%i.log</fileNamePattern>
            <maxFileSize>10MB</maxFileSize>
            <maxHistory>30</maxHistory>
            <totalSizeCap>1GB</totalSizeCap>
        </rollingPolicy>
    </appender>
    
    <!-- 錯誤檔案輸出 -->
    <appender name="ERROR_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>logs/error.log</file>
        <filter class="ch.qos.logback.classic.filter.LevelFilter">
            <level>ERROR</level>
            <onMatch>ACCEPT</onMatch>
            <onMismatch>DENY</onMismatch>
        </filter>
        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
            <charset>UTF-8</charset>
        </encoder>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>logs/error.%d{yyyy-MM-dd}.log</fileNamePattern>
            <maxHistory>30</maxHistory>
        </rollingPolicy>
    </appender>
    
    <!-- 非同步輸出 -->
    <appender name="ASYNC_FILE" class="ch.qos.logback.classic.AsyncAppender">
        <appender-ref ref="FILE"/>
        <queueSize>512</queueSize>
        <discardingThreshold>0</discardingThreshold>
        <includeCallerData>false</includeCallerData>
    </appender>
    
    <!-- Logger 配置 -->
    <logger name="com.tutorial" level="DEBUG" additivity="false">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="ASYNC_FILE"/>
    </logger>
    
    <logger name="org.springframework" level="INFO"/>
    <logger name="org.hibernate" level="WARN"/>
    <logger name="com.zaxxer.hikari" level="WARN"/>
    
    <!-- Root Logger -->
    <root level="INFO">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="FILE"/>
        <appender-ref ref="ERROR_FILE"/>
    </root>
    
    <!-- 環境特定配置 -->
    <springProfile name="dev">
        <logger name="root" level="DEBUG"/>
    </springProfile>
    
    <springProfile name="prod">
        <logger name="root" level="WARN"/>
    </springProfile>
    
</configuration>
```

#### 9.2.2 日誌使用範例

```java
package com.tutorial.logging;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.slf4j.MDC;

public class LoggingExample {
    
    // 使用 slf4j Logger
    private static final Logger logger = LoggerFactory.getLogger(LoggingExample.class);
    
    public static void main(String[] args) {
        // 基本日誌級別
        demonstrateLogLevels();
        
        // 參數化日誌
        demonstrateParameterizedLogging();
        
        // 異常日誌
        demonstrateExceptionLogging();
        
        // MDC 使用
        demonstrateMDC();
        
        // 效能日誌
        demonstratePerformanceLogging();
    }
    
    private static void demonstrateLogLevels() {
        logger.info("=== 日誌級別示範 ===");
        
        logger.trace("TRACE 級別 - 最詳細的日誌資訊");
        logger.debug("DEBUG 級別 - 調試資訊");
        logger.info("INFO 級別 - 一般資訊");
        logger.warn("WARN 級別 - 警告資訊");
        logger.error("ERROR 級別 - 錯誤資訊");
        
        // 條件日誌（提升效能）
        if (logger.isDebugEnabled()) {
            String expensiveOperation = performExpensiveOperation();
            logger.debug("昂貴操作結果: {}", expensiveOperation);
        }
    }
    
    private static void demonstrateParameterizedLogging() {
        logger.info("=== 參數化日誌示範 ===");
        
        String userName = "張三";
        int userAge = 25;
        double salary = 50000.0;
        
        // 推薦：使用參數化日誌（效能更好）
        logger.info("用戶資訊 - 姓名: {}, 年齡: {}, 薪資: {}", userName, userAge, salary);
        
        // 不推薦：字串串接（效能較差）
        // logger.info("用戶資訊 - 姓名: " + userName + ", 年齡: " + userAge);
        
        // 多參數
        logger.info("處理訂單 {} 於 {} 時間，金額 {}，狀態 {}", 
            "ORD001", "2024-01-15", 1500.0, "已完成");
    }
    
    private static void demonstrateExceptionLogging() {
        logger.info("=== 異常日誌示範 ===");
        
        try {
            // 模擬異常
            int result = 10 / 0;
        } catch (ArithmeticException e) {
            // 記錄異常堆疊
            logger.error("計算過程中發生錯誤", e);
            
            // 帶參數的異常日誌
            logger.error("處理用戶 {} 的訂單 {} 時發生錯誤: {}", 
                "張三", "ORD001", e.getMessage(), e);
        }
        
        try {
            processBusinessLogic();
        } catch (BusinessException e) {
            logger.warn("業務處理警告: {}, 錯誤代碼: {}", e.getMessage(), e.getErrorCode());
        } catch (Exception e) {
            logger.error("未預期的系統錯誤", e);
        }
    }
    
    private static void demonstrateMDC() {
        logger.info("=== MDC (Mapped Diagnostic Context) 示範 ===");
        
        try {
            // 設定 MDC 資訊
            MDC.put("userId", "USER123");
            MDC.put("requestId", "REQ456");
            MDC.put("sessionId", "SES789");
            
            logger.info("開始處理用戶請求");
            processUserRequest();
            logger.info("用戶請求處理完成");
            
        } finally {
            // 清理 MDC（重要！）
            MDC.clear();
        }
    }
    
    private static void demonstratePerformanceLogging() {
        logger.info("=== 效能日誌示範 ===");
        
        String operationName = "資料庫查詢";
        long startTime = System.currentTimeMillis();
        
        try {
            // 模擬操作
            Thread.sleep(100);
            
            long duration = System.currentTimeMillis() - startTime;
            
            if (duration > 50) {
                logger.warn("操作 {} 執行時間過長: {}ms", operationName, duration);
            } else {
                logger.debug("操作 {} 執行時間: {}ms", operationName, duration);
            }
            
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            logger.error("操作 {} 被中斷", operationName, e);
        }
    }
    
    private static String performExpensiveOperation() {
        return "昂貴操作的結果";
    }
    
    private static void processBusinessLogic() throws BusinessException {
        if (Math.random() > 0.5) {
            throw new BusinessException("業務規則違反", "BIZ001");
        }
    }
    
    private static void processUserRequest() {
        logger.debug("驗證用戶權限");
        logger.debug("查詢用戶資料");
        logger.debug("處理業務邏輯");
        logger.debug("返回處理結果");
    }
}

// 自定義業務異常
class BusinessException extends Exception {
    private final String errorCode;
    
    public BusinessException(String message, String errorCode) {
        super(message);
        this.errorCode = errorCode;
    }
    
    public String getErrorCode() {
        return errorCode;
    }
}
```

### 9.3 單元測試與 TDD

#### 9.3.1 JUnit 5 基礎測試

```java
package com.tutorial.testing;

import org.junit.jupiter.api.*;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.*;
import org.mockito.*;
import org.mockito.junit.jupiter.MockitoExtension;

import java.time.Duration;
import java.util.concurrent.TimeUnit;
import java.util.stream.Stream;
import java.util.List;
import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
@DisplayName("學生服務測試")
class StudentServiceTest {
    
    @Mock
    private StudentRepository studentRepository;
    
    @InjectMocks
    private StudentService studentService;
    
    private Student testStudent;
    
    @BeforeAll
    static void setUpAll() {
        System.out.println("開始執行 StudentService 測試套件");
    }
    
    @AfterAll
    static void tearDownAll() {
        System.out.println("完成 StudentService 測試套件");
    }
    
    @BeforeEach
    void setUp() {
        testStudent = new Student("S001", "張三", 20);
        System.out.println("測試方法開始執行");
    }
    
    @AfterEach
    void tearDown() {
        System.out.println("測試方法執行完成");
    }
    
    @Test
    @DisplayName("測試建立學生 - 成功情況")
    void testCreateStudent_Success() {
        // Given (準備)
        when(studentRepository.save(any(Student.class))).thenReturn(testStudent);
        
        // When (執行)
        Student result = studentService.createStudent("張三", 20);
        
        // Then (驗證)
        assertNotNull(result);
        assertEquals("張三", result.getName());
        assertEquals(20, result.getAge());
        assertNotNull(result.getId());
        
        // 驗證 Mock 互動
        verify(studentRepository, times(1)).save(any(Student.class));
    }
    
    @Test
    @DisplayName("測試建立學生 - 無效年齡")
    void testCreateStudent_InvalidAge() {
        // Given & When & Then
        IllegalArgumentException exception = assertThrows(
            IllegalArgumentException.class,
            () -> studentService.createStudent("李四", -1)
        );
        
        assertEquals("年齡必須大於 0", exception.getMessage());
        
        // 驗證沒有呼叫 repository
        verify(studentRepository, never()).save(any(Student.class));
    }
    
    @ParameterizedTest
    @DisplayName("測試年齡驗證 - 多組資料")
    @ValueSource(ints = {-1, 0, 151, 200})
    void testInvalidAges(int age) {
        assertThrows(
            IllegalArgumentException.class,
            () -> studentService.validateAge(age)
        );
    }
    
    @ParameterizedTest
    @DisplayName("測試有效年齡範圍")
    @CsvSource({
        "1, true",
        "18, true", 
        "65, true",
        "150, true"
    })
    void testValidAgeRange(int age, boolean expected) {
        assertEquals(expected, studentService.isValidAge(age));
    }
    
    @ParameterizedTest
    @DisplayName("測試學生姓名驗證")
    @MethodSource("provideStudentNames")
    void testStudentNameValidation(String name, boolean expectedValid) {
        if (expectedValid) {
            assertDoesNotThrow(() -> studentService.validateName(name));
        } else {
            assertThrows(IllegalArgumentException.class, 
                () -> studentService.validateName(name));
        }
    }
    
    static Stream<Arguments> provideStudentNames() {
        return Stream.of(
            Arguments.of("張三", true),
            Arguments.of("李四", true),
            Arguments.of("", false),
            Arguments.of(null, false),
            Arguments.of("   ", false),
            Arguments.of("a".repeat(51), false) // 超過長度限制
        );
    }
    
    @Test
    @DisplayName("測試執行時間斷言")
    void testPerformanceAssertion() {
        // Given
        when(studentRepository.save(any(Student.class))).thenReturn(testStudent);
        
        // When & Then - 斷言執行時間
        assertTimeout(Duration.ofMillis(100), () -> {
            studentService.createStudent("快速建立", 25);
        });
    }
    
    @RepeatedTest(value = 3, name = "重複測試 {currentRepetition}/{totalRepetitions}")
    @DisplayName("重複測試學生 ID 生成")
    void testStudentIdGeneration(RepetitionInfo repetitionInfo) {
        // Given
        when(studentRepository.save(any(Student.class))).thenReturn(testStudent);
        
        // When
        Student student = studentService.createStudent("測試", 20);
        
        // Then
        assertNotNull(student.getId());
        assertTrue(student.getId().startsWith("S"));
        
        System.out.println("重複執行第 " + repetitionInfo.getCurrentRepetition() + " 次");
    }
    
    @Nested
    @DisplayName("學生驗證相關測試")
    class StudentValidationTests {
        
        @Test
        @DisplayName("測試姓名長度驗證")
        void testNameLengthValidation() {
            assertThrows(IllegalArgumentException.class,
                () -> studentService.validateName("a".repeat(51)));
        }
        
        @Test
        @DisplayName("測試姓名格式驗證")
        void testNameFormatValidation() {
            assertThrows(IllegalArgumentException.class,
                () -> studentService.validateName("123"));
        }
    }
}

// 測試資料建構器模式
class StudentTestDataBuilder {
    private String id = "S001";
    private String name = "測試學生";
    private int age = 20;
    
    public StudentTestDataBuilder withId(String id) {
        this.id = id;
        return this;
    }
    
    public StudentTestDataBuilder withName(String name) {
        this.name = name;
        return this;
    }
    
    public StudentTestDataBuilder withAge(int age) {
        this.age = age;
        return this;
    }
    
    public Student build() {
        return new Student(id, name, age);
    }
}
```

### 9.4 設計模式實踐

#### 9.4.1 常用設計模式實作

```java
package com.tutorial.patterns;

import java.util.*;

// 1. 單例模式 (Singleton Pattern)
public class DatabaseConnection {
    private static volatile DatabaseConnection instance;
    private static final Object lock = new Object();
    
    private DatabaseConnection() {
        // 私有建構子
    }
    
    // 雙重檢查鎖定
    public static DatabaseConnection getInstance() {
        if (instance == null) {
            synchronized (lock) {
                if (instance == null) {
                    instance = new DatabaseConnection();
                }
            }
        }
        return instance;
    }
    
    // 或使用 enum 實作（推薦）
    public enum DatabaseConnectionEnum {
        INSTANCE;
        
        public void connect() {
            System.out.println("連接資料庫");
        }
    }
}

// 2. 建造者模式 (Builder Pattern)
class Student {
    private final String id;
    private final String name;
    private final int age;
    private final String email;
    private final String phone;
    private final String address;
    
    private Student(Builder builder) {
        this.id = builder.id;
        this.name = builder.name;
        this.age = builder.age;
        this.email = builder.email;
        this.phone = builder.phone;
        this.address = builder.address;
    }
    
    public static class Builder {
        private String id;
        private String name;
        private int age;
        private String email;
        private String phone;
        private String address;
        
        public Builder id(String id) {
            this.id = id;
            return this;
        }
        
        public Builder name(String name) {
            this.name = name;
            return this;
        }
        
        public Builder age(int age) {
            this.age = age;
            return this;
        }
        
        public Builder email(String email) {
            this.email = email;
            return this;
        }
        
        public Builder phone(String phone) {
            this.phone = phone;
            return this;
        }
        
        public Builder address(String address) {
            this.address = address;
            return this;
        }
        
        public Student build() {
            if (id == null || name == null) {
                throw new IllegalStateException("ID 和姓名為必填欄位");
            }
            return new Student(this);
        }
    }
    
    // Getters
    public String getId() { return id; }
    public String getName() { return name; }
    public int getAge() { return age; }
    public String getEmail() { return email; }
    public String getPhone() { return phone; }
    public String getAddress() { return address; }
}

// 3. 工廠模式 (Factory Pattern)
interface Animal {
    void makeSound();
}

class Dog implements Animal {
    @Override
    public void makeSound() {
        System.out.println("汪汪");
    }
}

class Cat implements Animal {
    @Override
    public void makeSound() {
        System.out.println("喵喵");
    }
}

class AnimalFactory {
    public static Animal createAnimal(String type) {
        return switch (type.toLowerCase()) {
            case "dog" -> new Dog();
            case "cat" -> new Cat();
            default -> throw new IllegalArgumentException("未知的動物類型: " + type);
        };
    }
}

// 4. 觀察者模式 (Observer Pattern)
interface NewsObserver {
    void update(String news);
}

class NewsAgency {
    private final List<NewsObserver> observers = new ArrayList<>();
    private String latestNews;
    
    public void addObserver(NewsObserver observer) {
        observers.add(observer);
    }
    
    public void removeObserver(NewsObserver observer) {
        observers.remove(observer);
    }
    
    public void setNews(String news) {
        this.latestNews = news;
        notifyObservers();
    }
    
    private void notifyObservers() {
        observers.forEach(observer -> observer.update(latestNews));
    }
}

class NewsSubscriber implements NewsObserver {
    private final String name;
    
    public NewsSubscriber(String name) {
        this.name = name;
    }
    
    @Override
    public void update(String news) {
        System.out.println(name + " 收到新聞: " + news);
    }
}

// 5. 策略模式 (Strategy Pattern)
interface PaymentStrategy {
    void pay(double amount);
}

class CreditCardPayment implements PaymentStrategy {
    private final String cardNumber;
    
    public CreditCardPayment(String cardNumber) {
        this.cardNumber = cardNumber;
    }
    
    @Override
    public void pay(double amount) {
        System.out.printf("使用信用卡 %s 支付 %.2f 元%n", cardNumber, amount);
    }
}

class PayPalPayment implements PaymentStrategy {
    private final String email;
    
    public PayPalPayment(String email) {
        this.email = email;
    }
    
    @Override
    public void pay(double amount) {
        System.out.printf("使用 PayPal (%s) 支付 %.2f 元%n", email, amount);
    }
}

class PaymentContext {
    private PaymentStrategy strategy;
    
    public void setPaymentStrategy(PaymentStrategy strategy) {
        this.strategy = strategy;
    }
    
    public void executePayment(double amount) {
        if (strategy == null) {
            throw new IllegalStateException("未設定支付策略");
        }
    }
}
```

---

## 10. 認證模擬練習

### 10.1 OCP Java SE 17 考試概覽

#### 10.1.1 考試基本資訊

**考試代碼：** 1Z0-829
**考試時間：** 90 分鐘
**題目數量：** 50 題
**及格分數：** 68%
**題型：** 選擇題（單選/多選）、程式碼分析題

**主要考試主題：**

1. **處理日期、時間、文字、數值和布林值** (20%)
2. **控制程式流程** (13%)
3. **利用物件導向概念** (11%)
4. **處理異常** (10%)
5. **使用陣列和集合** (11%)
6. **使用 Streams 和 Lambda 表達式** (9%)
7. **打包和部署 Java 程式碼，使用 Java Platform Module System** (6%)
8. **管理並發程式碼執行** (8%)
9. **使用 Java I/O API** (10%)
10. **使用 JDBC 存取資料庫** (2%)

### 10.2 模擬試題 - 基礎語法篇

#### 10.2.1 變數與資料型別

**題目 1：** 下列程式碼的輸出結果為何？

```java
public class DataTypeTest {
    public static void main(String[] args) {
        byte b = 10;
        short s = 20;
        int result = b + s;
        System.out.println(result);
        System.out.println(result instanceof Integer); // 編譯錯誤行
    }
}
```

A) 30, true
B) 30, false  
C) 編譯錯誤
D) 執行時期異常

**答案：C**
**解析：** instanceof 運算子不能用於基本型別，只能用於物件型別。

---

**題目 2：** 下列哪個變數宣告是有效的？

A) `int 2variable = 10;`
B) `int variable-name = 10;`
C) `int $variable = 10;`
D) `int class = 10;`

**答案：C**
**解析：** 變數名稱可以包含字母、數字、底線和美元符號，但不能以數字開頭，也不能使用保留字。

---

**題目 3：** 下列程式碼的輸出為何？

```java
public class VarTest {
    public static void main(String[] args) {
        var x = 10;
        var y = 20.5;
        var z = x + y;
        System.out.println(z);
        System.out.println(z.getClass().getSimpleName());
    }
}
```

A) 30.5, Double
B) 30, Integer
C) 編譯錯誤
D) 30.5, Float

**答案：A**
**解析：** var 會推斷為最寬泛的型別，int + double = double

### 10.2.2 運算子與控制結構

**題目 4：** 下列程式碼的輸出為何？

```java
public class OperatorTest {
    public static void main(String[] args) {
        int a = 5;
        int b = ++a + a-- - --a + a++;
        System.out.println("a=" + a + ", b=" + b);
    }
}
```

A) a=5, b=16
B) a=5, b=18
C) a=6, b=16
D) a=5, b=20

**答案：A**
**解析：** 
- ++a: a變為6，運算式值為6
- a--: 運算式值為6，之後a變為5  
- --a: a變為4，運算式值為4
- a++: 運算式值為4，之後a變為5
- 計算：6 + 6 - 4 + 4 = 12... 需要仔細計算

---

**題目 5：** 下列 switch 表達式哪個是正確的？

```java
String dayType = switch (day) {
    case 1, 2, 3, 4, 5 -> "工作日";
    case 6, 7 -> "週末";
};
```

A) 正確
B) 缺少 default 分支
C) 語法錯誤
D) 需要加上 yield

**答案：B**
**解析：** switch 表達式必須處理所有可能的值，或者提供 default 分支。

### 10.3 模擬試題 - 物件導向篇

#### 10.3.1 類別與繼承

**題目 6：** 下列程式碼的輸出為何？

```java
class Parent {
    static void print() {
        System.out.print("Parent ");
    }
}

class Child extends Parent {
    static void print() {
        System.out.print("Child ");
    }
}

public class InheritanceTest {
    public static void main(String[] args) {
        Parent p = new Child();
        p.print();
        Child c = new Child();
        c.print();
    }
}
```

A) Parent Child
B) Child Child
C) Parent Parent
D) Child Parent

**答案：A**
**解析：** 靜態方法不會被覆寫（override），而是被隱藏（hide）。呼叫哪個方法取決於宣告的型別。

---

**題目 7：** 下列程式碼能否編譯成功？

```java
abstract class Animal {
    abstract void makeSound();
    void sleep() {
        System.out.println("Sleeping...");
    }
}

class Dog extends Animal {
    void makeSound() {
        System.out.println("Woof!");
    }
}

public class Test {
    public static void main(String[] args) {
        Animal a = new Dog();
        a.makeSound();
        a.sleep();
    }
}
```

A) 編譯成功，輸出 "Woof! Sleeping..."
B) 編譯錯誤：抽象類別不能實例化
C) 編譯錯誤：Dog 類別缺少 sleep() 方法
D) 編譯錯誤：makeSound() 方法存取修飾符錯誤

**答案：A**
**解析：** 程式碼正確，抽象類別不能直接實例化，但可以透過子類別實例化。

### 10.4 模擬試題 - 集合與泛型篇

#### 10.4.1 List 和 Set 操作

**題目 8：** 下列程式碼的輸出為何？

```java
import java.util.*;

public class CollectionTest {
    public static void main(String[] args) {
        List<String> list = Arrays.asList("A", "B", "C");
        list.set(1, "X");
        System.out.println(list);
        list.add("D"); // 這一行會發生什麼？
    }
}
```

A) [A, X, C, D]
B) [A, X, C] 然後拋出異常
C) 編譯錯誤
D) [A, B, C, D]

**答案：B**
**解析：** Arrays.asList() 回傳固定大小的 List，可以修改元素但不能新增或刪除。

---

**題目 9：** 下列泛型宣告哪個是正確的？

A) `List<? extends Number> list = new ArrayList<Integer>();`
B) `List<? super Integer> list = new ArrayList<Number>();`
C) `List<?> list = new ArrayList<String>();`
D) 以上皆正確

**答案：D**
**解析：** 
- A: 正確，Integer extends Number
- B: 正確，Number 是 Integer 的父類別
- C: 正確，萬用字元可以接受任何型別

### 10.5 模擬試題 - Stream 與 Lambda 篇

#### 10.5.1 Stream API 操作

**題目 10：** 下列程式碼的輸出為何？

```java
import java.util.*;
import java.util.stream.*;

public class StreamTest {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
        
        long count = numbers.stream()
            .filter(n -> n % 2 == 0)
            .map(n -> n * 2)
            .count();
            
        System.out.println(count);
    }
}
```

A) 2
B) 4
C) 5
D) 10

**答案：A**
**解析：** 先過濾偶數 (2, 4)，然後對每個數乘以2 (4, 8)，最後計算個數為 2。

### 10.6 綜合練習與備考建議

#### 10.6.1 複合型題目

**題目 11：** 下列程式碼的完整輸出為何？

```java
import java.util.*;
import java.util.stream.*;

public class ComprehensiveTest {
    public static void main(String[] args) {
        List<String> words = Arrays.asList("java", "python", "javascript", "go");
        
        words.stream()
            .filter(w -> w.length() > 4)
            .map(String::toUpperCase)
            .sorted()
            .forEach(System.out::println);
    }
}
```

A) PYTHON, JAVASCRIPT
B) JAVASCRIPT, PYTHON  
C) java, python, javascript
D) JAVA, PYTHON, JAVASCRIPT

**答案：B**
**解析：** 篩選長度 > 4 的字串，轉大寫，排序後輸出。

#### 10.6.2 備考策略

**時間管理：**
- 平均每題 1.8 分鐘
- 先做會的題目，再回頭處理難題
- 預留 10 分鐘檢查答案

**常見陷阱：**
1. **NullPointerException** - 注意 null 檢查
2. **不可變物件** - LocalDateTime, String 等
3. **集合的固定大小** - Arrays.asList()
4. **泛型的通配符** - extends vs super
5. **靜態方法隱藏** - 不是覆寫
6. **執行緒安全** - 同步問題

**重點複習主題：**

1. **Stream API (必考)**
   - filter, map, reduce, collect
   - 方法參考 (Method References)
   - Optional 使用

2. **日期時間 API**
   - LocalDate, LocalTime, LocalDateTime
   - Period, Duration
   - DateTimeFormatter

3. **模組系統**
   - module-info.java 語法
   - requires, exports, opens
   - 服務載入器

4. **並發程式設計**
   - ExecutorService
   - CompletableFuture
   - 同步機制

5. **I/O 與 NIO.2**
   - Path, Files 類別
   - 檔案操作方法

**練習建議：**
- 每天至少做 10-15 題模擬題
- 重點練習程式碼追蹤
- 理解概念，不要死記答案
- 多練習實際程式設計

---

## 11. 最佳實務與專案規範

### 11.1 程式碼品質與規範

#### 11.1.1 命名規範

```java
package com.tutorial.bestpractices;

/**
 * 良好的命名規範示範
 * 
 * @author 開發者姓名
 * @version 1.0
 * @since 2024-01-01
 */
public class NamingConventionsExample {
    
    // 常數：全大寫，底線分隔
    public static final int MAX_RETRY_COUNT = 3;
    public static final String DEFAULT_CONFIG_FILE = "application.properties";
    
    // 類別變數：駝峰命名
    private final UserService userService;
    private final EmailNotificationService emailNotificationService;
    
    // 方法參數與區域變數：駝峰命名，具有描述性
    public void processUserRegistration(String userEmail, String firstName, String lastName) {
        // 區域變數：簡潔但清楚
        boolean isValidEmail = validateEmailFormat(userEmail);
        User newUser = createUserAccount(userEmail, firstName, lastName);
        
        if (isValidEmail && newUser != null) {
            sendWelcomeEmail(newUser);
        }
    }
    
    // 方法名：動詞開頭，清楚表達意圖
    private boolean validateEmailFormat(String email) {
        return email != null && email.contains("@") && email.contains(".");
    }
    
    private User createUserAccount(String email, String firstName, String lastName) {
        return new User.Builder()
            .email(email)
            .firstName(firstName)
            .lastName(lastName)
            .createdAt(LocalDateTime.now())
            .build();
    }
    
    private void sendWelcomeEmail(User user) {
        emailNotificationService.sendWelcomeEmail(user.getEmail(), user.getFirstName());
    }
    
    // 布林方法：is, has, can, should 開頭
    public boolean isActiveUser(User user) {
        return user.getStatus() == UserStatus.ACTIVE;
    }
    
    public boolean hasValidSubscription(User user) {
        return user.getSubscription() != null && 
               user.getSubscription().getExpiryDate().isAfter(LocalDate.now());
    }
    
    public boolean canAccessFeature(User user, Feature feature) {
        return isActiveUser(user) && 
               user.getPermissions().contains(feature.getRequiredPermission());
    }
}

/**
 * 錯誤的命名範例（避免使用）
 */
class BadNamingExample {
    // 錯誤：不具描述性
    private String s;
    private int x, y, z;
    
    // 錯誤：縮寫過度
    public void procUsrReg(String e, String fn, String ln) {
        // 錯誤：變數名稱無意義
        boolean b = checkEmailFmt(e);
        User u = mkUsr(e, fn, ln);
    }
    
    // 錯誤：方法名稱不清楚
    private boolean check(String email) {
        return email.contains("@");
    }
    
    // 錯誤：使用匈牙利命名法（Java 不推薦）
    private String strUserName;
    private int intUserAge;
}
```

#### 11.1.2 程式碼註解最佳實務

```java
package com.tutorial.bestpractices;

/**
 * 用戶服務類別 - 處理用戶相關的業務邏輯
 * 
 * <p>此類別提供用戶註冊、登入、密碼重設等核心功能。
 * 所有的用戶操作都會記錄到審計日誌中。</p>
 * 
 * <p><strong>使用範例：</strong></p>
 * <pre>{@code
 * UserService userService = new UserService(userRepository, emailService);
 * User newUser = userService.registerUser("john@example.com", "John", "Doe");
 * }</pre>
 * 
 * @author 開發團隊
 * @version 2.1.0
 * @since 1.0.0
 * @see User
 * @see UserRepository
 */
public class UserService {
    
    private static final Logger logger = LoggerFactory.getLogger(UserService.class);
    
    private final UserRepository userRepository;
    private final EmailService emailService;
    private final AuditService auditService;
    
    /**
     * 建構子
     * 
     * @param userRepository 用戶資料存取物件，不可為 null
     * @param emailService 郵件服務，不可為 null
     * @throws IllegalArgumentException 如果任何參數為 null
     */
    public UserService(UserRepository userRepository, EmailService emailService) {
        this.userRepository = Objects.requireNonNull(userRepository, "UserRepository 不可為 null");
        this.emailService = Objects.requireNonNull(emailService, "EmailService 不可為 null");
        this.auditService = new AuditService();
    }
    
    /**
     * 註冊新用戶
     * 
     * <p>此方法會執行以下步驟：</p>
     * <ol>
     *   <li>驗證電子郵件格式</li>
     *   <li>檢查電子郵件是否已被使用</li>
     *   <li>建立新用戶帳號</li>
     *   <li>發送歡迎郵件</li>
     *   <li>記錄審計日誌</li>
     * </ol>
     * 
     * @param email 用戶電子郵件，必須是有效的郵件格式
     * @param firstName 用戶名字，長度不可超過 50 字元
     * @param lastName 用戶姓氏，長度不可超過 50 字元
     * @return 建立成功的用戶物件
     * @throws IllegalArgumentException 如果參數無效
     * @throws UserAlreadyExistsException 如果電子郵件已被使用
     * @throws ServiceException 如果註冊過程中發生系統錯誤
     */
    public User registerUser(String email, String firstName, String lastName) 
            throws UserAlreadyExistsException, ServiceException {
        
        logger.info("開始註冊用戶: {}", email);
        
        // 參數驗證
        validateRegistrationParameters(email, firstName, lastName);
        
        // 檢查用戶是否已存在
        if (userRepository.existsByEmail(email)) {
            throw new UserAlreadyExistsException("電子郵件已被使用: " + email);
        }
        
        try {
            // 建立用戶
            User newUser = createUser(email, firstName, lastName);
            User savedUser = userRepository.save(newUser);
            
            // 發送歡迎郵件（非同步）
            CompletableFuture.runAsync(() -> {
                try {
                    emailService.sendWelcomeEmail(savedUser);
                } catch (Exception e) {
                    logger.warn("發送歡迎郵件失敗: {}", email, e);
                }
            });
            
            // 記錄審計日誌
            auditService.logUserRegistration(savedUser);
            
            logger.info("用戶註冊成功: {}", email);
            return savedUser;
            
        } catch (Exception e) {
            logger.error("用戶註冊失敗: {}", email, e);
            throw new ServiceException("註冊過程中發生錯誤", e);
        }
    }
    
    /**
     * 重設用戶密碼
     * 
     * @param email 用戶電子郵件
     * @return 重設令牌，有效期為 24 小時
     * @throws UserNotFoundException 如果用戶不存在
     */
    public String resetPassword(String email) throws UserNotFoundException {
        User user = userRepository.findByEmail(email)
            .orElseThrow(() -> new UserNotFoundException("找不到用戶: " + email));
        
        // 生成重設令牌
        String resetToken = generateSecureToken();
        
        // 設定令牌過期時間（24小時）
        LocalDateTime expiryTime = LocalDateTime.now().plusHours(24);
        
        // 儲存重設令牌
        user.setPasswordResetToken(resetToken);
        user.setPasswordResetTokenExpiry(expiryTime);
        userRepository.save(user);
        
        // 發送重設郵件
        emailService.sendPasswordResetEmail(user, resetToken);
        
        auditService.logPasswordResetRequest(user);
        
        return resetToken;
    }
    
    /**
     * 驗證註冊參數
     */
    private void validateRegistrationParameters(String email, String firstName, String lastName) {
        if (!isValidEmail(email)) {
            throw new IllegalArgumentException("無效的電子郵件格式: " + email);
        }
        
        if (firstName == null || firstName.trim().isEmpty() || firstName.length() > 50) {
            throw new IllegalArgumentException("名字必須在 1-50 字元之間");
        }
        
        if (lastName == null || lastName.trim().isEmpty() || lastName.length() > 50) {
            throw new IllegalArgumentException("姓氏必須在 1-50 字元之間");
        }
    }
    
    private boolean isValidEmail(String email) {
        // 簡化的郵件驗證，實際專案中應使用更嚴格的驗證
        return email != null && 
               email.matches("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$");
    }
    
    private User createUser(String email, String firstName, String lastName) {
        return new User.Builder()
            .id(UUID.randomUUID().toString())
            .email(email)
            .firstName(firstName)
            .lastName(lastName)
            .status(UserStatus.ACTIVE)
            .createdAt(LocalDateTime.now())
            .build();
    }
    
    private String generateSecureToken() {
        // 實際實作應該使用加密安全的隨機數生成器
        return UUID.randomUUID().toString();
    }
}

/**
 * 錯誤的註解範例（避免使用）
 */
class BadCommentExample {
    
    // 錯誤：過度明顯的註解
    private int age; // 年齡變數
    
    // 錯誤：註解與程式碼不一致
    // 將年齡設為 25
    public void setAge(int newAge) {
        this.age = newAge; // 實際上可以設定任何年齡
    }
    
    // 錯誤：使用註解來"註解掉"程式碼
    public void someMethod() {
        doSomething();
        // doSomethingElse(); // 暫時不執行
        // anotherMethod(); // 可能之後會用到
    }
    
    // 錯誤：無意義的註解
    /**
     * 這個方法會做一些事情
     */
    public void doSomething() {
        // 執行一些操作
        System.out.println("做了一些事情");
    }
}
```

### 11.2 效能最佳化

#### 11.2.1 記憶體管理

```java
package com.tutorial.bestpractices.performance;

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

/**
 * 記憶體管理最佳實務
 */
public class MemoryManagementBestPractices {
    
    /**
     * 字串處理最佳實務
     */
    public static class StringOptimization {
        
        // 錯誤：大量字串串接
        public String buildStringBadWay(List<String> items) {
            String result = "";
            for (String item : items) {
                result += item + ", "; // 每次都創建新的 String 物件
            }
            return result;
        }
        
        // 正確：使用 StringBuilder
        public String buildStringGoodWay(List<String> items) {
            StringBuilder sb = new StringBuilder();
            for (String item : items) {
                sb.append(item).append(", ");
            }
            return sb.toString();
        }
        
        // 更好：使用 String.join()
        public String buildStringBestWay(List<String> items) {
            return String.join(", ", items);
        }
        
        // 字串池最佳化
        public void demonstrateStringPooling() {
            // 推薦：使用字面量（會進入字串池）
            String s1 = "Hello";
            String s2 = "Hello";
            System.out.println(s1 == s2); // true
            
            // 避免：不必要的 new String()
            String s3 = new String("Hello"); // 不會使用字串池
            System.out.println(s1 == s3); // false
            
            // 必要時使用 intern()
            String s4 = s3.intern();
            System.out.println(s1 == s4); // true
        }
    }
    
    /**
     * 集合類別效能最佳化
     */
    public static class CollectionOptimization {
        
        // 預分配容量避免重新調整大小
        public List<Integer> createOptimizedList(int expectedSize) {
            // 好：預設容量
            return new ArrayList<>(expectedSize);
            
            // 不好：使用預設容量，可能需要多次擴容
            // return new ArrayList<>();
        }
        
        // 選擇適當的集合型別
        public void demonstrateCollectionChoice() {
            // 頻繁查詢：使用 HashMap
            Map<String, User> userCache = new HashMap<>();
            
            // 執行緒安全需求：使用 ConcurrentHashMap
            Map<String, String> sessionCache = new ConcurrentHashMap<>();
            
            // 保持插入順序：使用 LinkedHashMap
            Map<String, Integer> orderedMap = new LinkedHashMap<>();
            
            // 自動排序：使用 TreeMap
            Map<String, String> sortedMap = new TreeMap<>();
            
            // 固定大小陣列操作：使用 Arrays
            int[] numbers = new int[1000];
            
            // 頻繁增刪操作：使用 LinkedList
            List<String> frequentInsertDelete = new LinkedList<>();
            
            // 隨機存取：使用 ArrayList
            List<String> randomAccess = new ArrayList<>();
        }
        
        // 避免記憶體洩漏
        public class LeakPrevention {
            private final Map<String, Object> cache = new HashMap<>();
            
            // 錯誤：可能導致記憶體洩漏
            public void addToCacheBadWay(String key, Object value) {
                cache.put(key, value); // 永遠不會被清理
            }
            
            // 正確：使用 WeakHashMap 或實作清理機制
            private final Map<String, Object> betterCache = new WeakHashMap<>();
            
            public void addToCacheGoodWay(String key, Object value) {
                betterCache.put(key, value); // 會自動清理未使用的條目
            }
            
            // 更好：使用 LRU 快取
            private final Map<String, Object> lruCache = new LinkedHashMap<String, Object>(16, 0.75f, true) {
                @Override
                protected boolean removeEldestEntry(Map.Entry<String, Object> eldest) {
                    return size() > 100; // 限制快取大小
                }
            };
        }
    }
    
    /**
     * 物件創建最佳化
     */
    public static class ObjectCreationOptimization {
        
        // 物件池模式（適用於昂貴物件）
        public static class DatabaseConnectionPool {
            private final Queue<DatabaseConnection> pool = new LinkedList<>();
            private final int maxSize;
            
            public DatabaseConnectionPool(int maxSize) {
                this.maxSize = maxSize;
                // 預先創建連線
                for (int i = 0; i < maxSize; i++) {
                    pool.offer(new DatabaseConnection());
                }
            }
            
            public DatabaseConnection borrowConnection() {
                return pool.poll();
            }
            
            public void returnConnection(DatabaseConnection connection) {
                if (pool.size() < maxSize) {
                    pool.offer(connection);
                }
            }
        }
        
        // 單例模式避免重複創建
        public enum ConfigurationManager {
            INSTANCE;
            
            private final Properties config = new Properties();
            
            public String getProperty(String key) {
                return config.getProperty(key);
            }
        }
        
        // 工廠方法重用物件
        public static class UserFactory {
            private static final Map<String, User> userCache = new ConcurrentHashMap<>();
            
            public static User getUser(String email) {
                return userCache.computeIfAbsent(email, User::new);
            }
        }
        
        // 避免自動裝箱/拆箱
        public void demonstrateAutoboxing() {
            // 錯誤：頻繁的自動裝箱
            List<Integer> numbers = new ArrayList<>();
            for (int i = 0; i < 1000; i++) {
                numbers.add(i); // int -> Integer 自動裝箱
            }
            
            // 正確：使用基本型別陣列
            int[] primitiveNumbers = new int[1000];
            for (int i = 0; i < 1000; i++) {
                primitiveNumbers[i] = i; // 沒有裝箱
            }
            
            // 或使用專門的集合（如 TIntArrayList from Trove）
        }
    }
}
```

#### 11.2.2 並發效能最佳化

```java
package com.tutorial.bestpractices.performance;

import java.util.concurrent.*;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.LongAdder;

/**
 * 並發效能最佳化
 */
public class ConcurrencyOptimization {
    
    /**
     * 執行緒池最佳化
     */
    public static class ThreadPoolOptimization {
        
        // 自定義執行緒池（推薦）
        public static ThreadPoolExecutor createOptimizedThreadPool() {
            int corePoolSize = Runtime.getRuntime().availableProcessors();
            int maximumPoolSize = corePoolSize * 2;
            long keepAliveTime = 60L;
            TimeUnit unit = TimeUnit.SECONDS;
            
            // 使用有界佇列避免記憶體問題
            BlockingQueue<Runnable> workQueue = new ArrayBlockingQueue<>(100);
            
            // 自定義執行緒工廠
            ThreadFactory threadFactory = new ThreadFactory() {
                private final AtomicInteger threadNumber = new AtomicInteger(1);
                
                @Override
                public Thread newThread(Runnable r) {
                    Thread t = new Thread(r, "CustomPool-" + threadNumber.getAndIncrement());
                    t.setDaemon(false);
                    t.setPriority(Thread.NORM_PRIORITY);
                    return t;
                }
            };
            
            // 拒絕策略
            RejectedExecutionHandler handler = new ThreadPoolExecutor.CallerRunsPolicy();
            
            return new ThreadPoolExecutor(
                corePoolSize, maximumPoolSize, keepAliveTime, unit,
                workQueue, threadFactory, handler);
        }
        
        // 避免：直接使用 Executors 的工廠方法
        public static void avoidTheseExecutors() {
            // 危險：無界佇列，可能導致 OOM
            // ExecutorService bad1 = Executors.newFixedThreadPool(10);
            
            // 危險：無界執行緒數，可能耗盡系統資源
            // ExecutorService bad2 = Executors.newCachedThreadPool();
            
            // 危險：單執行緒，無界佇列
            // ExecutorService bad3 = Executors.newSingleThreadExecutor();
        }
    }
    
    /**
     * 鎖最佳化
     */
    public static class LockOptimization {
        
        // 減少鎖的粒度
        public static class FineTunedLocking {
            private final Object lock1 = new Object();
            private final Object lock2 = new Object();
            
            private int counter1 = 0;
            private int counter2 = 0;
            
            // 好：細粒度鎖
            public void incrementCounter1() {
                synchronized (lock1) {
                    counter1++;
                }
            }
            
            public void incrementCounter2() {
                synchronized (lock2) {
                    counter2++;
                }
            }
            
            // 避免：粗粒度鎖
            public synchronized void incrementBothCounters() {
                counter1++;
                counter2++;
            }
        }
        
        // 使用讀寫鎖
        public static class ReadWriteLockExample {
            private final ReadWriteLock lock = new ReentrantReadWriteLock();
            private final Map<String, String> cache = new HashMap<>();
            
            public String get(String key) {
                lock.readLock().lock();
                try {
                    return cache.get(key);
                } finally {
                    lock.readLock().unlock();
                }
            }
            
            public void put(String key, String value) {
                lock.writeLock().lock();
                try {
                    cache.put(key, value);
                } finally {
                    lock.writeLock().unlock();
                }
            }
        }
        
        // 使用無鎖資料結構
        public static class LockFreeOptimization {
            private final AtomicInteger atomicCounter = new AtomicInteger();
            private final LongAdder longAdder = new LongAdder();
            
            // 高競爭情況下，LongAdder 比 AtomicLong 效能更好
            public void increment() {
                longAdder.increment();
            }
            
            public long getSum() {
                return longAdder.sum();
            }
            
            // 使用 ConcurrentHashMap 替代同步的 HashMap
            private final ConcurrentHashMap<String, String> concurrentMap = new ConcurrentHashMap<>();
            
            public void putIfAbsent(String key, String value) {
                concurrentMap.putIfAbsent(key, value);
            }
        }
    }
    
    /**
     * 異步程式設計最佳化
     */
    public static class AsyncOptimization {
        
        private final ExecutorService executor = createOptimizedThreadPool();
        
        // 使用 CompletableFuture 進行異步處理
        public CompletableFuture<String> processDataAsync(String input) {
            return CompletableFuture
                .supplyAsync(() -> {
                    // 第一步：預處理
                    return preprocessData(input);
                }, executor)
                .thenCompose(this::validateDataAsync)
                .thenApply(this::transformData)
                .thenCompose(this::saveDataAsync)
                .exceptionally(throwable -> {
                    logger.error("處理資料時發生錯誤", throwable);
                    return "錯誤：" + throwable.getMessage();
                });
        }
        
        private String preprocessData(String input) {
            // 模擬預處理
            return input.trim().toLowerCase();
        }
        
        private CompletableFuture<String> validateDataAsync(String data) {
            return CompletableFuture.supplyAsync(() -> {
                // 模擬驗證
                if (data.isEmpty()) {
                    throw new IllegalArgumentException("資料不能為空");
                }
                return data;
            }, executor);
        }
        
        private String transformData(String data) {
            // 模擬轉換
            return data.toUpperCase();
        }
        
        private CompletableFuture<String> saveDataAsync(String data) {
            return CompletableFuture.supplyAsync(() -> {
                // 模擬儲存
                return "已儲存：" + data;
            }, executor);
        }
        
        // 批次處理最佳化
        public CompletableFuture<List<String>> processBatchAsync(List<String> inputs) {
            List<CompletableFuture<String>> futures = inputs.stream()
                .map(this::processDataAsync)
                .collect(Collectors.toList());
            
            return CompletableFuture.allOf(futures.toArray(new CompletableFuture[0]))
                .thenApply(v -> futures.stream()
                    .map(CompletableFuture::join)
                    .collect(Collectors.toList()));
        }
    }
}
```

### 11.3 安全性最佳實務

#### 11.3.1 輸入驗證與防護

```java
package com.tutorial.bestpractices.security;

import java.security.SecureRandom;
import java.sql.PreparedStatement;
import java.sql.Connection;
import java.util.regex.Pattern;
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import java.util.Base64;

/**
 * 安全性最佳實務示範
 */
public class SecurityBestPractices {
    
    /**
     * 輸入驗證與清理
     */
    public static class InputValidation {
        
        // 使用正則表達式驗證輸入
        private static final Pattern EMAIL_PATTERN = 
            Pattern.compile("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$");
        
        private static final Pattern PHONE_PATTERN = 
            Pattern.compile("^\\+?[1-9]\\d{1,14}$");
        
        private static final Pattern ALPHANUMERIC_PATTERN = 
            Pattern.compile("^[a-zA-Z0-9]+$");
        
        /**
         * 驗證電子郵件格式
         */
        public static boolean isValidEmail(String email) {
            return email != null && 
                   email.length() <= 254 && 
                   EMAIL_PATTERN.matcher(email).matches();
        }
        
        /**
         * 驗證電話號碼
         */
        public static boolean isValidPhoneNumber(String phone) {
            return phone != null && 
                   phone.length() <= 15 && 
                   PHONE_PATTERN.matcher(phone).matches();
        }
        
        /**
         * 清理用戶輸入，防止 XSS 攻擊
         */
        public static String sanitizeInput(String input) {
            if (input == null) {
                return null;
            }
            
            return input
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace("&", "&amp;")
                .replace("\"", "&quot;")
                .replace("'", "&#x27;")
                .replace("/", "&#x2F;");
        }
        
        /**
         * 驗證檔案名稱，防止路徑遍歷攻擊
         */
        public static boolean isValidFileName(String fileName) {
            if (fileName == null || fileName.trim().isEmpty()) {
                return false;
            }
            
            // 檢查危險字元
            String[] dangerousPatterns = {"..", "/", "\\", ":", "*", "?", "\"", "<", ">", "|"};
            for (String pattern : dangerousPatterns) {
                if (fileName.contains(pattern)) {
                    return false;
                }
            }
            
            // 檢查檔案名稱長度
            return fileName.length() <= 255;
        }
        
        /**
         * 驗證數值範圍
         */
        public static boolean isValidAge(int age) {
            return age >= 0 && age <= 150;
        }
        
        public static boolean isValidAmount(double amount) {
            return amount >= 0 && amount <= 1_000_000;
        }
        
        /**
         * 驗證字串長度
         */
        public static boolean isValidLength(String input, int minLength, int maxLength) {
            return input != null && 
                   input.length() >= minLength && 
                   input.length() <= maxLength;
        }
    }
    
    /**
     * SQL 注入防護
     */
    public static class SQLInjectionPrevention {
        
        // 錯誤：容易受到 SQL 注入攻擊
        public User findUserBadWay(Connection conn, String email) throws Exception {
            String sql = "SELECT * FROM users WHERE email = '" + email + "'";
            // 如果 email = "'; DROP TABLE users; --"，會刪除整個表
            return null; // 危險的實作
        }
        
        // 正確：使用 PreparedStatement
        public User findUserSafeWay(Connection conn, String email) throws Exception {
            String sql = "SELECT * FROM users WHERE email = ?";
            try (PreparedStatement stmt = conn.prepareStatement(sql)) {
                stmt.setString(1, email);
                // PreparedStatement 會自動處理特殊字元
                ResultSet rs = stmt.executeQuery();
                
                if (rs.next()) {
                    return new User(
                        rs.getString("id"),
                        rs.getString("email"),
                        rs.getString("name")
                    );
                }
            }
            return null;
        }
        
        // 使用 JPA/Hibernate 命名查詢
        @Repository
        public interface UserRepository extends JpaRepository<User, String> {
            
            // 安全：使用參數化查詢
            @Query("SELECT u FROM User u WHERE u.email = :email")
            Optional<User> findByEmailSafe(@Param("email") String email);
            
            // 危險：字串串接
            // @Query("SELECT u FROM User u WHERE u.email = '" + "#{#email}" + "'")
            // Optional<User> findByEmailUnsafe(@Param("email") String email);
        }
    }
    
    /**
     * 密碼安全處理
     */
    public static class PasswordSecurity {
        
        private static final SecureRandom RANDOM = new SecureRandom();
        private static final int SALT_LENGTH = 32;
        
        /**
         * 生成安全的鹽值
         */
        public static byte[] generateSalt() {
            byte[] salt = new byte[SALT_LENGTH];
            RANDOM.nextBytes(salt);
            return salt;
        }
        
        /**
         * 使用 BCrypt 加密密碼（推薦）
         */
        public static String hashPassword(String password) {
            return BCrypt.hashpw(password, BCrypt.gensalt(12));
        }
        
        /**
         * 驗證密碼
         */
        public static boolean verifyPassword(String password, String hashedPassword) {
            return BCrypt.checkpw(password, hashedPassword);
        }
        
        /**
         * 密碼強度驗證
         */
        public static boolean isStrongPassword(String password) {
            if (password == null || password.length() < 8) {
                return false;
            }
            
            boolean hasUpper = password.chars().anyMatch(Character::isUpperCase);
            boolean hasLower = password.chars().anyMatch(Character::isLowerCase);
            boolean hasDigit = password.chars().anyMatch(Character::isDigit);
            boolean hasSpecial = password.chars().anyMatch(ch -> "!@#$%^&*()_+-=[]{}|;:,.<>?".indexOf(ch) >= 0);
            
            return hasUpper && hasLower && hasDigit && hasSpecial;
        }
        
        /**
         * 生成安全的隨機密碼
         */
        public static String generateSecurePassword(int length) {
            String chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*";
            StringBuilder password = new StringBuilder();
            
            for (int i = 0; i < length; i++) {
                password.append(chars.charAt(RANDOM.nextInt(chars.length())));
            }
            
            return password.toString();
        }
    }
    
    /**
     * 資料加密
     */
    public static class DataEncryption {
        
        private static final String ALGORITHM = "AES";
        private static final String TRANSFORMATION = "AES/GCM/NoPadding";
        
        /**
         * 生成 AES 金鑰
         */
        public static SecretKey generateAESKey() throws Exception {
            KeyGenerator keyGenerator = KeyGenerator.getInstance(ALGORITHM);
            keyGenerator.init(256);
            return keyGenerator.generateKey();
        }
        
        /**
         * 加密資料
         */
        public static String encrypt(String plainText, SecretKey key) throws Exception {
            Cipher cipher = Cipher.getInstance(TRANSFORMATION);
            cipher.init(Cipher.ENCRYPT_MODE, key);
            
            byte[] encryptedData = cipher.doFinal(plainText.getBytes());
            byte[] iv = cipher.getIV();
            
            // 將 IV 和加密資料組合
            byte[] encryptedWithIv = new byte[iv.length + encryptedData.length];
            System.arraycopy(iv, 0, encryptedWithIv, 0, iv.length);
            System.arraycopy(encryptedData, 0, encryptedWithIv, iv.length, encryptedData.length);
            
            return Base64.getEncoder().encodeToString(encryptedWithIv);
        }
        
        /**
         * 解密資料
         */
        public static String decrypt(String encryptedText, SecretKey key) throws Exception {
            byte[] encryptedWithIv = Base64.getDecoder().decode(encryptedText);
            
            Cipher cipher = Cipher.getInstance(TRANSFORMATION);
            
            // 提取 IV
            byte[] iv = new byte[12]; // GCM mode IV length
            System.arraycopy(encryptedWithIv, 0, iv, 0, iv.length);
            
            // 提取加密資料
            byte[] encryptedData = new byte[encryptedWithIv.length - iv.length];
            System.arraycopy(encryptedWithIv, iv.length, encryptedData, 0, encryptedData.length);
            
            GCMParameterSpec gcmSpec = new GCMParameterSpec(128, iv);
            cipher.init(Cipher.DECRYPT_MODE, key, gcmSpec);
            
            byte[] decryptedData = cipher.doFinal(encryptedData);
            return new String(decryptedData);
        }
    }
    
    /**
     * 安全的亂數生成
     */
    public static class SecureRandomGeneration {
        
        private static final SecureRandom SECURE_RANDOM = new SecureRandom();
        
        /**
         * 生成安全的隨機 Token
         */
        public static String generateSecureToken(int length) {
            byte[] bytes = new byte[length];
            SECURE_RANDOM.nextBytes(bytes);
            return Base64.getUrlEncoder().withoutPadding().encodeToString(bytes);
        }
        
        /**
         * 生成 UUID（不依賴系統時間）
         */
        public static String generateSecureUUID() {
            byte[] randomBytes = new byte[16];
            SECURE_RANDOM.nextBytes(randomBytes);
            
            // 設定版本和變體位元
            randomBytes[6] &= 0x0f;  // 清除版本位元
            randomBytes[6] |= 0x40;  // 設定版本為 4
            randomBytes[8] &= 0x3f;  // 清除變體位元
            randomBytes[8] |= 0x80;  // 設定變體
            
            return bytesToHex(randomBytes);
        }
        
        private static String bytesToHex(byte[] bytes) {
            StringBuilder result = new StringBuilder();
            for (byte b : bytes) {
                result.append(String.format("%02x", b));
            }
            return result.toString();
        }
    }
}
```

### 11.4 團隊協作與代碼管理

#### 11.4.1 Git 工作流程最佳實務

```bash
# Git 分支策略 - Git Flow

# 主要分支
# master/main - 生產環境代碼
# develop - 開發整合分支

# 建立新功能分支
git checkout develop
git pull origin develop
git checkout -b feature/user-authentication

# 開發過程中的提交
git add .
git commit -m "feat: 添加用戶認證模組

- 實作登入功能
- 添加JWT token驗證
- 新增密碼加密
- 增加單元測試

Closes #123"

# 推送功能分支
git push origin feature/user-authentication

# 建立 Pull Request/Merge Request
# 在 GitHub/GitLab 上建立 PR，包含：
# - 清楚的標題和描述
# - 相關的 issue 連結
# - 測試說明
# - 截圖（如適用）

# 合併前的準備
git checkout develop
git pull origin develop
git checkout feature/user-authentication
git rebase develop  # 或 git merge develop

# 解決衝突後
git push origin feature/user-authentication --force-with-lease

# 合併後清理
git checkout develop
git pull origin develop
git branch -d feature/user-authentication
git push origin --delete feature/user-authentication
```

#### 11.4.2 代碼審查最佳實務

```java
/**
 * 代碼審查檢查清單
 */
public class CodeReviewChecklist {
    
    /**
     * 1. 功能性檢查
     * - 代碼是否實作了需求？
     * - 邊界條件是否處理？
     * - 錯誤處理是否完整？
     */
    
    /**
     * 2. 可讀性檢查
     * - 命名是否清楚描述用途？
     * - 方法是否過長？（建議 < 20 行）
     * - 是否有適當的註解？
     */
    
    /**
     * 3. 效能檢查
     * - 是否有不必要的物件創建？
     * - 演算法複雜度是否合理？
     * - 是否有記憶體洩漏風險？
     */
    
    /**
     * 4. 安全性檢查
     * - 輸入是否經過驗證？
     * - 是否有 SQL 注入風險？
     * - 敏感資料是否被妥善處理？
     */
    
    /**
     * 5. 測試覆蓋
     * - 是否有對應的單元測試？
     * - 測試是否涵蓋主要場景？
     * - 是否有整合測試？
     */
    
    // 好的代碼範例
    public class GoodExample {
        private static final Logger logger = LoggerFactory.getLogger(GoodExample.class);
        private static final int MAX_RETRY_ATTEMPTS = 3;
        
        /**
         * 處理用戶註冊
         * 
         * @param registrationRequest 註冊請求
         * @return 註冊結果
         * @throws ValidationException 當輸入無效時
         * @throws ServiceException 當系統錯誤時
         */
        public RegistrationResult registerUser(RegistrationRequest registrationRequest) 
                throws ValidationException, ServiceException {
            
            // 1. 輸入驗證
            validateRegistrationRequest(registrationRequest);
            
            // 2. 業務邏輯處理
            try {
                User newUser = createUser(registrationRequest);
                User savedUser = userRepository.save(newUser);
                
                // 3. 後續處理（異步）
                sendWelcomeEmailAsync(savedUser);
                
                // 4. 回傳結果
                return RegistrationResult.success(savedUser.getId());
                
            } catch (DataIntegrityViolationException e) {
                logger.warn("用戶註冊失敗 - 郵件已存在: {}", registrationRequest.getEmail());
                throw new ValidationException("該郵件地址已被註冊");
            } catch (Exception e) {
                logger.error("用戶註冊過程中發生系統錯誤", e);
                throw new ServiceException("註冊失敗，請稍後再試");
            }
        }
        
        private void validateRegistrationRequest(RegistrationRequest request) throws ValidationException {
            if (request == null) {
                throw new ValidationException("註冊請求不能為空");
            }
            
            if (!InputValidator.isValidEmail(request.getEmail())) {
                throw new ValidationException("無效的郵件格式");
            }
            
            if (!PasswordValidator.isStrongPassword(request.getPassword())) {
                throw new ValidationException("密碼強度不足");
            }
        }
    }
    
    // 需要改進的代碼範例
    public class NeedsImprovement {
        
        // 問題：方法過長，職責不清
        public String doStuff(String input) {
            String result = "";
            if (input != null) {
                if (input.length() > 0) {
                    if (input.contains("@")) {
                        String[] parts = input.split("@");
                        if (parts.length == 2) {
                            String username = parts[0];
                            String domain = parts[1];
                            if (username.length() > 0 && domain.length() > 0) {
                                if (domain.contains(".")) {
                                    String[] domainParts = domain.split("\\.");
                                    if (domainParts.length >= 2) {
                                        result = "valid email";
                                    } else {
                                        result = "invalid domain";
                                    }
                                } else {
                                    result = "invalid domain";
                                }
                            } else {
                                result = "invalid format";
                            }
                        } else {
                            result = "invalid format";    
                        }
                    } else {
                        result = "no @ symbol";
                    }
                } else {
                    result = "empty string";
                }
            } else {
                result = "null input";
            }
            return result;
        }
    }
}
```

---

## 12. 附錄

### 12.1 常用 API 快速參考

#### 12.1.1 String 類別常用方法

```java
// 字串建立與基本操作
String str = "Hello World";
String str2 = new String("Hello World");

// 長度與字元
int length = str.length();                    // 取得長度
char ch = str.charAt(0);                      // 取得指定位置字元
boolean isEmpty = str.isEmpty();               // 檢查是否為空

// 比較
boolean equals = str.equals("Hello World");    // 內容比較
boolean equalsIgnoreCase = str.equalsIgnoreCase("hello world");  // 忽略大小寫比較
int compare = str.compareTo("Hello");          // 字典順序比較

// 搜尋
int index = str.indexOf("World");              // 尋找子字串位置
int lastIndex = str.lastIndexOf("l");          // 最後出現位置
boolean contains = str.contains("Hello");      // 是否包含子字串
boolean startsWith = str.startsWith("Hello"); // 是否以指定字串開始
boolean endsWith = str.endsWith("World");     // 是否以指定字串結束

// 子字串與分割
String sub = str.substring(0, 5);              // 取得子字串
String[] parts = str.split(" ");               // 分割字串

// 修改
String upper = str.toUpperCase();              // 轉大寫
String lower = str.toLowerCase();              // 轉小寫
String trimmed = str.trim();                   // 去除頭尾空白
String replaced = str.replace("World", "Java"); // 替換
String formatted = String.format("Hello %s", "Java"); // 格式化
```

#### 12.1.2 集合框架常用方法

```java
// List 常用操作
List<String> list = new ArrayList<>();
list.add("Item");                    // 添加元素
list.add(0, "First");               // 在指定位置添加
list.get(0);                        // 取得指定位置元素
list.set(0, "Updated");             // 更新指定位置元素
list.remove(0);                     // 移除指定位置元素
list.remove("Item");                // 移除指定元素
list.size();                        // 取得大小
list.isEmpty();                     // 檢查是否為空
list.contains("Item");              // 檢查是否包含
list.clear();                       // 清空

// Map 常用操作
Map<String, Integer> map = new HashMap<>();
map.put("key", 100);                // 添加鍵值對
Integer value = map.get("key");     // 取得值
Integer defaultValue = map.getOrDefault("key", 0); // 取得值或預設值
map.remove("key");                  // 移除鍵值對
map.containsKey("key");             // 檢查是否包含鍵
map.containsValue(100);             // 檢查是否包含值
map.size();                         // 取得大小
map.keySet();                       // 取得所有鍵
map.values();                       // 取得所有值
map.entrySet();                     // 取得所有鍵值對

// Set 常用操作
Set<String> set = new HashSet<>();
set.add("Item");                    // 添加元素
set.remove("Item");                 // 移除元素
set.contains("Item");               // 檢查是否包含
set.size();                         // 取得大小
set.isEmpty();                      // 檢查是否為空
```

#### 12.1.3 日期時間 API

```java
// 當前日期時間
LocalDate today = LocalDate.now();
LocalTime now = LocalTime.now();
LocalDateTime dateTime = LocalDateTime.now();
ZonedDateTime zonedDateTime = ZonedDateTime.now();

// 建立特定日期時間
LocalDate date = LocalDate.of(2024, 12, 25);
LocalTime time = LocalTime.of(14, 30, 0);
LocalDateTime specific = LocalDateTime.of(2024, 12, 25, 14, 30, 0);

// 解析字串
LocalDate parsed = LocalDate.parse("2024-12-25");
LocalDateTime parsedDateTime = LocalDateTime.parse("2024-12-25T14:30:00");

// 格式化
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
String formatted = dateTime.format(formatter);

// 計算
LocalDate tomorrow = today.plusDays(1);
LocalDate lastWeek = today.minusWeeks(1);
LocalDateTime oneHourLater = dateTime.plusHours(1);

// 比較
boolean isBefore = date.isBefore(today);
boolean isAfter = date.isAfter(today);
boolean isEqual = date.isEqual(today);

// 取得部分
int year = date.getYear();
Month month = date.getMonth();
int dayOfMonth = date.getDayOfMonth();
DayOfWeek dayOfWeek = date.getDayOfWeek();
```

### 12.2 開發工具清單

#### 12.2.1 IDE 推薦

1. **IntelliJ IDEA**
   - Ultimate Edition（付費）：完整企業級功能
   - Community Edition（免費）：基本 Java 開發功能
   - 特色：智能程式碼補全、重構工具、除錯器

2. **Eclipse**
   - 免費開源 IDE
   - 豐富的外掛生態系統
   - 適合大型專案開發

3. **Visual Studio Code**
   - 輕量級編輯器
   - Java Extension Pack
   - 適合小型專案和學習

#### 12.2.2 建置工具

1. **Maven**
   - 專案物件模型（POM）
   - 依賴管理
   - 生命周期管理
   ```xml
   <groupId>com.example</groupId>
   <artifactId>my-app</artifactId>
   <version>1.0-SNAPSHOT</version>
   <packaging>jar</packaging>
   ```

2. **Gradle**
   - Groovy/Kotlin DSL
   - 增量建置
   - 多專案支援
   ```gradle
   plugins {
       id 'java'
   }
   
   repositories {
       mavenCentral()
   }
   
   dependencies {
       testImplementation 'junit:junit:4.13.2'
   }
   ```

#### 12.2.3 測試工具

1. **JUnit 5**
   - 單元測試框架
   - 參數化測試
   - 動態測試

2. **Mockito**
   - Mock 物件框架
   - 行為驗證
   - Spy 功能

3. **TestContainers**
   - 整合測試
   - Docker 容器
   - 資料庫測試

### 12.3 學習資源推薦

#### 12.3.1 官方文檔

1. **Oracle Java Documentation**
   - API 文檔：https://docs.oracle.com/en/java/javase/21/docs/api/
   - 語言規範：https://docs.oracle.com/javase/specs/
   - 教學：https://docs.oracle.com/javase/tutorial/

2. **OpenJDK**
   - 原始碼：https://github.com/openjdk/jdk
   - JEP（JDK Enhancement Proposals）

#### 12.3.2 線上學習平台

1. **Coursera**
   - Java Programming Specialization (Duke University)
   - Object-Oriented Programming in Java (UC San Diego)

2. **edX**
   - Introduction to Java Programming (Microsoft)
   - Object Oriented Programming with Java (Georgia Tech)

3. **Udemy**
   - Java Programming Masterclass
   - Spring Framework 完整課程

#### 12.3.3 練習平台

1. **LeetCode**
   - 演算法練習
   - 面試準備
   - Java 解法討論

2. **HackerRank**
   - 程式設計挑戰
   - Java 專門題目
   - 技能認證

3. **Codewars**
   - Kata 挑戰
   - 社群解法
   - 程式設計思維訓練

### 12.4 常見問題與疑難排解

#### 12.4.1 編譯問題

**問題：`javac` 命令不存在**
```bash
# 解決方案：
# 1. 檢查 JDK 是否安裝
java -version
javac -version

# 2. 設定 JAVA_HOME 環境變數
export JAVA_HOME=/path/to/jdk
export PATH=$JAVA_HOME/bin:$PATH

# 3. Windows 系統設定
# 系統變數 -> 新增 JAVA_HOME
# PATH 變數 -> 新增 %JAVA_HOME%\bin
```

**問題：ClassNotFoundException**
```java
// 解決方案：
// 1. 檢查 CLASSPATH
// 2. 確認類別檔案位置
// 3. 檢查套件聲明

// 執行時指定 classpath
java -cp /path/to/classes com.example.Main
```

#### 12.4.2 記憶體問題

**問題：OutOfMemoryError**
```bash
# 解決方案：調整 JVM 記憶體參數

# 增加堆記憶體
java -Xmx2g -Xms1g MyApp

# 增加元空間（Java 8+）
java -XX:MetaspaceSize=256m -XX:MaxMetaspaceSize=512m MyApp

# 啟用記憶體垃圾收集日誌
java -XX:+PrintGC -XX:+PrintGCDetails MyApp
```

#### 12.4.3 效能問題

**問題：程式執行緩慢**
```java
// 使用 JProfiler 或 VisualVM 進行效能分析

// 常見效能問題：
// 1. 不必要的物件創建
// 錯誤：
String result = "";
for (int i = 0; i < 1000; i++) {
    result += "item" + i; // 每次都創建新的 String 物件
}

// 正確：
StringBuilder result = new StringBuilder();
for (int i = 0; i < 1000; i++) {
    result.append("item").append(i);
}

// 2. 不當的集合使用
// 錯誤：頻繁搜尋 List
List<String> list = new ArrayList<>();
for (String item : items) {
    if (!list.contains(item)) { // O(n) 複雜度
        list.add(item);
    }
}

// 正確：使用 Set
Set<String> set = new HashSet<>();
for (String item : items) {
    set.add(item); // O(1) 複雜度
}
```

#### 12.4.4 Maven/Gradle 問題

**問題：依賴衝突**
```xml
<!-- Maven 解決方案 -->
<dependency>
    <groupId>com.example</groupId>
    <artifactId>library</artifactId>
    <version>1.0</version>
    <exclusions>
        <exclusion>
            <groupId>conflicting.group</groupId>
            <artifactId>conflicting-artifact</artifactId>
        </exclusion>
    </exclusions>
</dependency>

<!-- 查看依賴樹 -->
<!-- mvn dependency:tree -->
```

```gradle
// Gradle 解決方案
dependencies {
    implementation('com.example:library:1.0') {
        exclude group: 'conflicting.group', module: 'conflicting-artifact'
    }
}

// 查看依賴
// ./gradlew dependencies
```

---

## 13. 檢查清單 (Checklist)

### 13.1 Java 基礎技能檢查清單

#### 13.1.1 語言基礎 ✅

- [ ] **資料型別與變數**
  - [ ] 瞭解原始資料型別（int, double, boolean, char 等）
  - [ ] 理解參考型別與原始型別的差異
  - [ ] 正確使用變數宣告與初始化
  - [ ] 理解變數作用域（scope）

- [ ] **運算子與控制結構**
  - [ ] 熟練使用算術、比較、邏輯運算子
  - [ ] 掌握 if-else、switch 條件控制
  - [ ] 熟練使用 for、while、do-while 迴圈
  - [ ] 理解 break 和 continue 的使用

- [ ] **陣列與字串**
  - [ ] 會建立和操作一維、多維陣列
  - [ ] 熟練使用 String 類別的方法
  - [ ] 理解 String 的不可變性
  - [ ] 適當使用 StringBuilder 和 StringBuffer

#### 13.1.2 物件導向程式設計 ✅

- [ ] **類別與物件**
  - [ ] 能夠設計和實作類別
  - [ ] 理解建構子的作用和重載
  - [ ] 掌握存取修飾符（public, private, protected）
  - [ ] 理解靜態成員（static）的概念

- [ ] **繼承與多型**
  - [ ] 正確使用 extends 關鍵字
  - [ ] 理解方法覆寫（Override）
  - [ ] 掌握抽象類別和介面的設計
  - [ ] 理解多型的概念和應用

- [ ] **封裝與資訊隱藏**
  - [ ] 實作 getter 和 setter 方法
  - [ ] 理解資料封裝的重要性
  - [ ] 會設計物件的公開介面

#### 13.1.3 核心 API 應用 ✅

- [ ] **集合框架**
  - [ ] 熟練使用 List、Set、Map 介面
  - [ ] 理解不同實作類別的特性
  - [ ] 會使用泛型（Generics）
  - [ ] 理解 Iterator 的使用

- [ ] **例外處理**
  - [ ] 正確使用 try-catch-finally
  - [ ] 理解檢查例外與執行期例外
  - [ ] 會建立自訂例外類別
  - [ ] 使用 try-with-resources

- [ ] **日期時間 API**
  - [ ] 使用 LocalDate、LocalTime、LocalDateTime
  - [ ] 進行日期時間的計算和比較
  - [ ] 格式化和解析日期時間字串

### 13.2 進階技能檢查清單

#### 13.2.1 Lambda 表達式與 Stream API ✅

- [ ] **Lambda 表達式**
  - [ ] 理解函數式介面
  - [ ] 會寫 Lambda 表達式
  - [ ] 使用方法參考（Method Reference）
  - [ ] 理解閉包（Closure）概念

- [ ] **Stream API**
  - [ ] 熟練使用 map、filter、reduce 操作
  - [ ] 理解中間操作與終端操作
  - [ ] 使用 Collector 進行資料收集
  - [ ] 平行流（Parallel Stream）的使用

#### 13.2.2 多執行緒與並行程式設計 ✅

- [ ] **基礎多執行緒**
  - [ ] 理解 Thread 和 Runnable
  - [ ] 掌握執行緒的生命週期
  - [ ] 使用 synchronized 關鍵字
  - [ ] 理解執行緒安全概念

- [ ] **並行程式設計**
  - [ ] 使用 java.util.concurrent 套件
  - [ ] 理解 Executor 框架
  - [ ] 使用 CompletableFuture
  - [ ] 掌握並行集合類別

#### 13.2.3 設計模式與最佳實務 ✅

- [ ] **常用設計模式**
  - [ ] 實作 Singleton 模式
  - [ ] 理解 Factory 模式
  - [ ] 使用 Observer 模式
  - [ ] 掌握 Strategy 模式

- [ ] **程式碼品質**
  - [ ] 遵循命名規範
  - [ ] 寫有意義的註解
  - [ ] 進行程式碼重構
  - [ ] 使用靜態分析工具

### 13.3 專案開發檢查清單

#### 13.3.1 開發環境設定 ✅

- [ ] **IDE 設定**
  - [ ] 安裝並設定 IDE（IntelliJ IDEA 或 Eclipse）
  - [ ] 設定程式碼格式化規則
  - [ ] 安裝必要的外掛
  - [ ] 設定版本控制整合

- [ ] **建置工具**
  - [ ] 建立 Maven 或 Gradle 專案
  - [ ] 設定依賴管理
  - [ ] 設定編譯和打包任務
  - [ ] 整合 IDE 與建置工具

#### 13.3.2 測試驗證 ✅

- [ ] **單元測試**
  - [ ] 設定 JUnit 5 測試框架
  - [ ] 寫基本的單元測試
  - [ ] 使用 Mockito 進行模擬測試
  - [ ] 計算測試覆蓋率

- [ ] **整合測試**
  - [ ] 設定測試資料庫
  - [ ] 寫 API 整合測試
  - [ ] 使用 TestContainers
  - [ ] 建立端到端測試

#### 13.3.3 程式碼品質控制 ✅

- [ ] **靜態分析**
  - [ ] 設定 Checkstyle
  - [ ] 使用 SpotBugs 或 PMD
  - [ ] 程式碼覆蓋率檢查
  - [ ] 持續整合設定

- [ ] **版本控制**
  - [ ] 使用 Git 版本控制
  - [ ] 遵循分支策略
  - [ ] 寫有意義的 commit 訊息
  - [ ] 進行 code review

### 13.4 認證考試準備檢查清單

#### 13.4.1 OCA（Oracle Certified Associate）準備 ✅

- [ ] **Java 基礎（20-25%）**
  - [ ] Java 平台概述和歷史
  - [ ] JVM、JRE、JDK 的區別
  - [ ] Java 程式的執行流程
  - [ ] 命令列工具使用

- [ ] **使用 Java 資料型別（15-20%）**
  - [ ] 宣告和初始化變數
  - [ ] 原始資料型別的範圍和預設值
  - [ ] 包裝類別的使用
  - [ ] 型別轉換和提升

- [ ] **使用運算子和判斷結構（15-20%）**
  - [ ] 運算子優先級
  - [ ] if-else 和 switch 語句
  - [ ] 三元運算子
  - [ ] 比較物件的等價性

#### 13.4.2 OCP（Oracle Certified Professional）準備 ✅

- [ ] **Java 類別設計（15-20%）**
  - [ ] 存取修飾符的使用
  - [ ] 類別繼承和介面實作
  - [ ] 多型和方法覆寫
  - [ ] 抽象類別和介面設計

- [ ] **進階 Java 類別設計（10-15%）**
  - [ ] 內部類別和匿名類別
  - [ ] Enum 的使用
  - [ ] Lambda 表達式
  - [ ] 函數式介面

- [ ] **泛型和集合（20-25%）**
  - [ ] 泛型類別和方法
  - [ ] 萬用字元（Wildcards）
  - [ ] 集合框架的效能特性
  - [ ] Comparable 和 Comparator

#### 13.4.3 學習進度追蹤 ✅

**第一階段：基礎知識（建議時間：4-6 週）**
- [ ] 完成第 1-4 章學習
- [ ] 完成基礎練習題
- [ ] 參加模擬考試並達到 70% 以上

**第二階段：進階應用（建議時間：6-8 週）**
- [ ] 完成第 5-8 章學習
- [ ] 完成進階練習專案
- [ ] 參加進階模擬考試並達到 75% 以上

**第三階段：專案實務（建議時間：4-6 週）**
- [ ] 完成第 9-11 章學習
- [ ] 完成完整專案開發
- [ ] 通過程式碼審查

**第四階段：認證準備（建議時間：2-4 週）**
- [ ] 完成認證模擬練習
- [ ] 複習弱點章節
- [ ] 參加認證考試

### 13.5 持續學習建議

#### 13.5.1 技術趨勢關注 ✅

- [ ] **新版本 Java 特性**
  - [ ] 關注 Java 版本發布週期
  - [ ] 學習新語言特性
  - [ ] 了解效能改進
  - [ ] 遷移策略規劃

- [ ] **相關技術棧**
  - [ ] Spring Framework
  - [ ] 微服務架構
  - [ ] 容器化技術（Docker、Kubernetes）
  - [ ] 雲端平台服務

#### 13.5.2 職涯發展路徑 ✅

- [ ] **技術專精**
  - [ ] 後端開發專家
  - [ ] 全端開發工程師
  - [ ] 系統架構師
  - [ ] DevOps 工程師

- [ ] **管理發展**
  - [ ] 技術團隊領導
  - [ ] 專案經理
  - [ ] 產品經理
  - [ ] 技術顧問

恭喜你完成了這份完整的 Java 程式語言教學手冊！記住，程式設計是一個需要持續練習和學習的領域。建議你：

1. **定期複習**：每週花時間複習已學內容
2. **實際練習**：多寫程式、多做專案
3. **參與社群**：加入 Java 開發者社群，與其他開發者交流
4. **跟上趨勢**：關注 Java 新版本和相關技術發展
5. **建立作品集**：將你的專案和程式碼放在 GitHub 上展示

祝你在 Java 程式設計的學習旅程中取得成功！🎉

---

## 14. 新增補充內容

### 14.1 容器化與雲端部署

#### 14.1.1 Docker 容器化

**Dockerfile 範例**
```dockerfile
# 使用 OpenJDK 21 作為基礎映像
FROM openjdk:21-jdk-slim

# 設定工作目錄
WORKDIR /app

# 複製 Maven 設定檔案
COPY pom.xml .
COPY src ./src

# 安裝 Maven 並建置應用程式
RUN apt-get update && apt-get install -y maven && \
    mvn clean package -DskipTests && \
    mv target/*.jar app.jar && \
    rm -rf ~/.m2 && \
    apt-get remove -y maven && \
    apt-get autoremove -y

# 設定執行用戶（安全性考量）
RUN groupadd -r appuser && useradd -r -g appuser appuser
USER appuser

# 暴露端口
EXPOSE 8080

# 設定健康檢查
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8080/actuator/health || exit 1

# 執行應用程式
ENTRYPOINT ["java", "-jar", "app.jar"]
```

**Docker Compose 設定**
```yaml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      - SPRING_PROFILES_ACTIVE=docker
      - DATABASE_URL=jdbc:postgresql://db:5432/myapp
    depends_on:
      - db
      - redis
    volumes:
      - ./logs:/app/logs
    networks:
      - app-network

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=myapp
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    networks:
      - app-network

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    networks:
      - app-network

volumes:
  postgres_data:

networks:
  app-network:
    driver: bridge
```

#### 14.1.2 Kubernetes 部署

**Deployment 設定**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: java-app
  namespace: production
spec:
  replicas: 3
  selector:
    matchLabels:
      app: java-app
  template:
    metadata:
      labels:
        app: java-app
    spec:
      containers:
      - name: java-app
        image: myregistry/java-app:1.0.0
        ports:
        - containerPort: 8080
        env:
        - name: SPRING_PROFILES_ACTIVE
          value: "kubernetes"
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: database-url
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
          initialDelaySeconds: 60
          periodSeconds: 30
        readinessProbe:
          httpGet:
            path: /actuator/ready
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
```

#### 14.1.3 雲端平台部署

**AWS ECS 任務定義**
```json
{
  "family": "java-app",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "512",
  "memory": "1024",
  "executionRoleArn": "arn:aws:iam::account:role/ecsTaskExecutionRole",
  "containerDefinitions": [
    {
      "name": "java-app",
      "image": "account.dkr.ecr.region.amazonaws.com/java-app:latest",
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
          "name": "DATABASE_PASSWORD",
          "valueFrom": "arn:aws:secretsmanager:region:account:secret:prod/db/password"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/java-app",
          "awslogs-region": "us-west-2",
          "awslogs-stream-prefix": "ecs"
        }
      }
    }
  ]
}
```

### 14.2 現代 Java 開發工具

#### 14.2.1 建置工具進階應用

**Gradle 多模組設定**
```kotlin
// settings.gradle.kts
rootProject.name = "java-tutorial-multimodule"

include(
    "core",
    "web",
    "data",
    "security",
    "integration-tests"
)

// build.gradle.kts (根專案)
plugins {
    java
    id("org.springframework.boot") version "3.2.0" apply false
    id("io.spring.dependency-management") version "1.1.4" apply false
}

allprojects {
    group = "com.tutorial"
    version = "1.0.0"
    
    repositories {
        mavenCentral()
    }
}

subprojects {
    apply(plugin = "java")
    apply(plugin = "io.spring.dependency-management")
    
    dependencies {
        implementation("org.springframework.boot:spring-boot-starter")
        testImplementation("org.springframework.boot:spring-boot-starter-test")
    }
    
    java {
        sourceCompatibility = JavaVersion.VERSION_21
        targetCompatibility = JavaVersion.VERSION_21
    }
    
    tasks.withType<Test> {
        useJUnitPlatform()
    }
}
```

#### 14.2.2 程式碼品質工具

**SonarQube 整合**
```xml
<!-- Maven pom.xml -->
<plugin>
    <groupId>org.sonarsource.scanner.maven</groupId>
    <artifactId>sonar-maven-plugin</artifactId>
    <version>3.10.0.2594</version>
</plugin>

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
    </executions>
</plugin>
```

**SpotBugs 設定**
```xml
<plugin>
    <groupId>com.github.spotbugs</groupId>
    <artifactId>spotbugs-maven-plugin</artifactId>
    <version>4.7.3.6</version>
    <configuration>
        <effort>Max</effort>
        <threshold>Low</threshold>
        <failOnError>true</failOnError>
        <includeFilterFile>spotbugs-include.xml</includeFilterFile>
        <excludeFilterFile>spotbugs-exclude.xml</excludeFilterFile>
    </configuration>
</plugin>
```

#### 14.2.3 現代化測試框架

**TestContainers 進階應用**
```java
@Testcontainers
@SpringBootTest
class IntegrationTest {

    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:15")
            .withDatabaseName("testdb")
            .withUsername("test")
            .withPassword("test");

    @Container
    static RedisContainer redis = new RedisContainer("redis:7-alpine")
            .withExposedPorts(6379);

    @DynamicPropertySource
    static void configureProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", postgres::getJdbcUrl);
        registry.add("spring.datasource.username", postgres::getUsername);
        registry.add("spring.datasource.password", postgres::getPassword);
        
        registry.add("spring.redis.host", redis::getHost);
        registry.add("spring.redis.port", () -> redis.getMappedPort(6379));
    }

    @Test
    void shouldCreateAndRetrieveUser() {
        // 測試實作
    }
}
```

**Playwright 端到端測試**
```java
@Test
void shouldCompleteUserJourney() {
    try (Playwright playwright = Playwright.create()) {
        Browser browser = playwright.chromium().launch();
        Page page = browser.newPage();
        
        // 導航到登入頁面
        page.navigate("http://localhost:8080/login");
        
        // 填寫登入表單
        page.fill("#username", "testuser");
        page.fill("#password", "password");
        page.click("#login-button");
        
        // 驗證重導向到儀表板
        expect(page).toHaveURL("http://localhost:8080/dashboard");
        expect(page.locator("h1")).toContainText("歡迎回來");
        
        browser.close();
    }
}
```

### 14.3 Java 生態系統與框架

#### 14.3.1 現代化 Web 開發

**Spring WebFlux 響應式程式設計**
```java
@RestController
@RequestMapping("/api/users")
public class UserController {

    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping(produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<User> getAllUsersStream() {
        return userService.getAllUsersReactive()
                .delayElements(Duration.ofSeconds(1));
    }

    @GetMapping("/{id}")
    public Mono<ResponseEntity<User>> getUserById(@PathVariable String id) {
        return userService.findByIdReactive(id)
                .map(ResponseEntity::ok)
                .defaultIfEmpty(ResponseEntity.notFound().build());
    }

    @PostMapping
    public Mono<ResponseEntity<User>> createUser(@RequestBody @Valid Mono<User> userMono) {
        return userMono
                .flatMap(userService::saveReactive)
                .map(user -> ResponseEntity.status(HttpStatus.CREATED).body(user))
                .onErrorResume(ValidationException.class, 
                    ex -> Mono.just(ResponseEntity.badRequest().build()));
    }
}

@Service
public class UserService {

    private final ReactiveMongoTemplate mongoTemplate;

    public UserService(ReactiveMongoTemplate mongoTemplate) {
        this.mongoTemplate = mongoTemplate;
    }

    public Flux<User> getAllUsersReactive() {
        return mongoTemplate.findAll(User.class);
    }

    public Mono<User> findByIdReactive(String id) {
        return mongoTemplate.findById(id, User.class);
    }

    public Mono<User> saveReactive(User user) {
        return mongoTemplate.save(user);
    }
}
```

#### 14.3.2 微服務架構模式

**服務發現與配置**
```java
// Eureka 客戶端設定
@SpringBootApplication
@EnableEurekaClient
@EnableConfigServer
public class ConfigServerApplication {
    public static void main(String[] args) {
        SpringApplication.run(ConfigServerApplication.class, args);
    }
}

// 服務間通信
@FeignClient(name = "user-service", path = "/api/users")
public interface UserServiceClient {
    
    @GetMapping("/{id}")
    ResponseEntity<User> getUser(@PathVariable("id") String id);
    
    @PostMapping
    ResponseEntity<User> createUser(@RequestBody User user);
}

// 斷路器模式
@Component
public class UserServiceFallback implements UserServiceClient {
    
    @Override
    public ResponseEntity<User> getUser(String id) {
        User defaultUser = new User();
        defaultUser.setId(id);
        defaultUser.setName("服務暫時不可用");
        return ResponseEntity.ok(defaultUser);
    }
    
    @Override
    public ResponseEntity<User> createUser(User user) {
        return ResponseEntity.status(HttpStatus.SERVICE_UNAVAILABLE).build();
    }
}
```

#### 14.3.3 消息驅動架構

**Apache Kafka 整合**
```java
@Configuration
@EnableKafka
public class KafkaConfig {

    @Bean
    public ProducerFactory<String, Object> producerFactory() {
        Map<String, Object> configProps = new HashMap<>();
        configProps.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        configProps.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        configProps.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, JsonSerializer.class);
        configProps.put(ProducerConfig.ACKS_CONFIG, "all");
        configProps.put(ProducerConfig.RETRIES_CONFIG, 3);
        return new DefaultKafkaProducerFactory<>(configProps);
    }

    @Bean
    public KafkaTemplate<String, Object> kafkaTemplate() {
        return new KafkaTemplate<>(producerFactory());
    }
}

@Service
public class EventPublisher {

    private final KafkaTemplate<String, Object> kafkaTemplate;

    public EventPublisher(KafkaTemplate<String, Object> kafkaTemplate) {
        this.kafkaTemplate = kafkaTemplate;
    }

    public void publishUserCreatedEvent(UserCreatedEvent event) {
        kafkaTemplate.send("user-events", event.getUserId(), event)
                .whenComplete((result, ex) -> {
                    if (ex == null) {
                        log.info("事件發送成功: {}", event);
                    } else {
                        log.error("事件發送失敗: {}", event, ex);
                    }
                });
    }
}

@Component
public class EventListener {

    @KafkaListener(topics = "user-events", groupId = "notification-service")
    public void handleUserCreatedEvent(UserCreatedEvent event) {
        // 處理用戶創建事件
        log.info("收到用戶創建事件: {}", event);
        // 發送歡迎郵件等後續處理
    }
}
```

### 14.4 Java 21 新特性深入

#### 14.4.1 Virtual Threads（虛擬執行緒）

```java
// 使用虛擬執行緒改善並行處理效能
public class VirtualThreadsDemo {

    public static void main(String[] args) throws InterruptedException {
        // 傳統執行緒池方式
        try (ExecutorService traditionalExecutor = Executors.newFixedThreadPool(100)) {
            runTasksWithTraditionalThreads(traditionalExecutor);
        }

        // 虛擬執行緒方式
        try (ExecutorService virtualExecutor = Executors.newVirtualThreadPerTaskExecutor()) {
            runTasksWithVirtualThreads(virtualExecutor);
        }
    }

    private static void runTasksWithVirtualThreads(ExecutorService executor) throws InterruptedException {
        long startTime = System.currentTimeMillis();
        
        // 建立 10,000 個並行任務
        List<Future<String>> futures = new ArrayList<>();
        for (int i = 0; i < 10_000; i++) {
            int taskId = i;
            futures.add(executor.submit(() -> {
                // 模擬 I/O 密集型操作
                try {
                    Thread.sleep(1000); // 模擬網路請求
                    return "Task " + taskId + " completed";
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    return "Task " + taskId + " interrupted";
                }
            }));
        }

        // 等待所有任務完成
        for (Future<String> future : futures) {
            try {
                future.get();
            } catch (ExecutionException e) {
                e.printStackTrace();
            }
        }

        long endTime = System.currentTimeMillis();
        System.out.println("虛擬執行緒完成時間: " + (endTime - startTime) + "ms");
    }

    // HTTP 服務器使用虛擬執行緒
    public static void startVirtualThreadHttpServer() throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);
        
        server.createContext("/api/data", exchange -> {
            // 每個請求在虛擬執行緒中處理
            Thread.startVirtualThread(() -> {
                try {
                    // 模擬資料庫查詢
                    Thread.sleep(100);
                    
                    String response = "Hello from Virtual Thread: " + Thread.currentThread();
                    exchange.sendResponseHeaders(200, response.length());
                    try (OutputStream os = exchange.getResponseBody()) {
                        os.write(response.getBytes());
                    }
                } catch (Exception e) {
                    e.printStackTrace();
                }
            });
        });

        server.start();
        System.out.println("伺服器啟動在 http://localhost:8080");
    }
}
```

#### 14.4.2 Pattern Matching 進階應用

```java
public class PatternMatchingAdvanced {

    // Record 模式匹配
    public record Point(int x, int y) {}
    public record Rectangle(Point topLeft, Point bottomRight) {}
    public record Circle(Point center, int radius) {}

    public double calculateArea(Object shape) {
        return switch (shape) {
            case Rectangle(var p1, var p2) -> {
                int width = Math.abs(p2.x() - p1.x());
                int height = Math.abs(p2.y() - p1.y());
                yield width * height;
            }
            case Circle(var center, var radius) -> Math.PI * radius * radius;
            case Point p -> 0.0; // 點沒有面積
            default -> throw new IllegalArgumentException("未知的形狀: " + shape);
        };
    }

    // 多層嵌套模式匹配
    public String analyzeData(Object data) {
        return switch (data) {
            case String s when s.length() > 10 -> "長字串: " + s.substring(0, 10) + "...";
            case String s -> "短字串: " + s;
            case Integer i when i > 100 -> "大數字: " + i;
            case Integer i -> "小數字: " + i;
            case List<?> list when list.isEmpty() -> "空列表";
            case List<?> list -> "列表大小: " + list.size();
            case null -> "空值";
            default -> "未知類型: " + data.getClass().getSimpleName();
        };
    }

    // 結合 Optional 的模式匹配
    public String processOptionalValue(Optional<String> opt) {
        return switch (opt) {
            case Optional<?> o when o.isEmpty() -> "無值";
            case Optional<?> o -> "有值: " + o.get();
        };
    }
}
```

#### 14.4.3 String Templates（預覽特性）

```java
// 注意：這是預覽特性，需要使用 --enable-preview 標誌
public class StringTemplatesDemo {

    public void demonstrateStringTemplates() {
        String name = "張三";
        int age = 30;
        double salary = 50000.0;

        // 基本字串模板
        String greeting = STR."你好，\{name}！你今年\{age}歲。";
        
        // 格式化模板
        String formatted = FMT."薪水：%,.2f\{salary} 元";
        
        // HTML 模板（安全的 HTML 生成）
        String html = RAW."""
            <div class="user-info">
                <h2>\{name}</h2>
                <p>年齡：\{age}</p>
                <p>薪水：\{salary}</p>
            </div>
            """;

        // JSON 模板
        String json = STR."""
            {
                "name": "\{name}",
                "age": \{age},
                "salary": \{salary},
                "active": \{age < 65}
            }
            """;

        // SQL 查詢模板（防止 SQL 注入）
        String userId = "user123";
        String query = STR."SELECT * FROM users WHERE id = '\{userId}' AND active = true";
    }

    // 自訂模板處理器
    public static final StringTemplate.Processor<String, RuntimeException> UPPER = 
        (template) -> {
            StringBuilder sb = new StringBuilder();
            Iterator<String> fragments = template.fragments().iterator();
            Iterator<Object> values = template.values().iterator();
            
            while (fragments.hasNext()) {
                sb.append(fragments.next());
                if (values.hasNext()) {
                    sb.append(String.valueOf(values.next()).toUpperCase());
                }
            }
            return sb.toString();
        };
}
```

### 14.5 企業級開發模式

#### 14.5.1 Clean Architecture 實作

```java
// 領域層（Domain Layer）
public abstract class User {
    private final UserId id;
    private final Email email;
    private final UserName name;
    private final UserStatus status;

    protected User(UserId id, Email email, UserName name, UserStatus status) {
        this.id = requireNonNull(id);
        this.email = requireNonNull(email);
        this.name = requireNonNull(name);
        this.status = requireNonNull(status);
    }

    public void activate() {
        if (this.status == UserStatus.BANNED) {
            throw new UserActivationException("被禁用的用戶無法啟動");
        }
        // 發布領域事件
        DomainEventPublisher.publish(new UserActivatedEvent(this.id));
    }

    // getters...
}

// 值物件（Value Objects）
public record Email(String value) {
    public Email {
        if (!isValidEmail(value)) {
            throw new IllegalArgumentException("無效的電子郵件格式");
        }
    }

    private static boolean isValidEmail(String email) {
        return email != null && email.matches("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}");
    }
}

// 倉庫介面（Repository Interface）
public interface UserRepository {
    Optional<User> findById(UserId id);
    Optional<User> findByEmail(Email email);
    void save(User user);
    void delete(UserId id);
}

// 應用服務層（Application Service Layer）
@Service
@Transactional
public class UserApplicationService {
    
    private final UserRepository userRepository;
    private final EmailService emailService;
    private final DomainEventPublisher eventPublisher;

    public UserApplicationService(UserRepository userRepository, 
                                EmailService emailService,
                                DomainEventPublisher eventPublisher) {
        this.userRepository = userRepository;
        this.emailService = emailService;
        this.eventPublisher = eventPublisher;
    }

    public UserId registerUser(RegisterUserCommand command) {
        // 驗證電子郵件唯一性
        if (userRepository.findByEmail(command.email()).isPresent()) {
            throw new EmailAlreadyExistsException(command.email());
        }

        // 建立領域物件
        User user = User.create(
            UserIdGenerator.nextId(),
            command.email(),
            command.name()
        );

        // 儲存用戶
        userRepository.save(user);

        // 發送歡迎郵件
        emailService.sendWelcomeEmail(user.getEmail());

        return user.getId();
    }
}

// 基礎設施層（Infrastructure Layer）
@Repository
public class JpaUserRepository implements UserRepository {
    
    private final UserJpaRepository jpaRepository;
    private final UserMapper mapper;

    @Override
    public Optional<User> findById(UserId id) {
        return jpaRepository.findById(id.value())
                .map(mapper::toDomain);
    }

    @Override
    public void save(User user) {
        UserEntity entity = mapper.toEntity(user);
        jpaRepository.save(entity);
    }
}
```

#### 14.5.2 CQRS（命令查詢責任分離）模式

```java
// 命令（Commands）
public sealed interface UserCommand {
    record CreateUser(String email, String name) implements UserCommand {}
    record UpdateUser(String id, String name) implements UserCommand {}
    record DeleteUser(String id) implements UserCommand {}
}

// 查詢（Queries）
public sealed interface UserQuery {
    record GetUserById(String id) implements UserQuery {}
    record GetUsersByEmail(String email) implements UserQuery {}
    record GetActiveUsers(int page, int size) implements UserQuery {}
}

// 命令處理器
@Component
public class UserCommandHandler {
    
    private final UserRepository repository;
    private final EventStore eventStore;

    public void handle(UserCommand.CreateUser command) {
        // 驗證
        validateCreateUserCommand(command);
        
        // 建立聚合
        User user = User.create(command.email(), command.name());
        
        // 儲存
        repository.save(user);
        
        // 儲存事件
        eventStore.append(user.getId(), user.getUncommittedEvents());
    }

    public void handle(UserCommand.UpdateUser command) {
        User user = repository.findById(new UserId(command.id()))
                .orElseThrow(() -> new UserNotFoundException(command.id()));
        
        user.updateName(new UserName(command.name()));
        repository.save(user);
        eventStore.append(user.getId(), user.getUncommittedEvents());
    }
}

// 查詢處理器
@Component
public class UserQueryHandler {
    
    private final UserReadModelRepository readModelRepository;

    public UserReadModel handle(UserQuery.GetUserById query) {
        return readModelRepository.findById(query.id())
                .orElseThrow(() -> new UserNotFoundException(query.id()));
    }

    public List<UserReadModel> handle(UserQuery.GetActiveUsers query) {
        return readModelRepository.findActiveUsers(
                PageRequest.of(query.page(), query.size())
        );
    }
}

// 事件溯源
@Component
public class UserEventHandler {
    
    private final UserReadModelRepository readModelRepository;

    @EventHandler
    public void on(UserCreatedEvent event) {
        UserReadModel readModel = new UserReadModel(
                event.getUserId(),
                event.getEmail(),
                event.getName(),
                UserStatus.ACTIVE
        );
        readModelRepository.save(readModel);
    }

    @EventHandler
    public void on(UserUpdatedEvent event) {
        readModelRepository.findById(event.getUserId())
                .ifPresent(readModel -> {
                    readModel.updateName(event.getName());
                    readModelRepository.save(readModel);
                });
    }
}
```

### 14.6 Java 與 AI/ML 整合

#### 14.6.1 Deep Java Library (DJL) 使用

```java
// Maven 依賴
/*
<dependency>
    <groupId>ai.djl</groupId>
    <artifactId>api</artifactId>
    <version>0.24.0</version>
</dependency>
<dependency>
    <groupId>ai.djl.pytorch</groupId>
    <artifactId>pytorch-engine</artifactId>
    <version>0.24.0</version>
</dependency>
*/

@Service
public class ImageClassificationService {
    
    private Model model;
    private Predictor<Image, Classifications> predictor;

    @PostConstruct
    public void initializeModel() throws Exception {
        // 載入預訓練模型
        Criteria<Image, Classifications> criteria = Criteria.builder()
                .optApplication(Application.CV.IMAGE_CLASSIFICATION)
                .setTypes(Image.class, Classifications.class)
                .optFilter("layer", "18")
                .optEngine("PyTorch")
                .optProgress(new ProgressBar())
                .build();

        ZooModel<Image, Classifications> model = criteria.loadModel();
        this.predictor = model.newPredictor();
    }

    public ClassificationResult classifyImage(byte[] imageBytes) throws Exception {
        // 轉換圖片
        Image image = ImageFactory.getInstance().fromInputStream(
                new ByteArrayInputStream(imageBytes)
        );

        // 執行推理
        Classifications classifications = predictor.predict(image);
        
        // 取得最高信心度的分類
        Classification bestClassification = classifications.best();
        
        return new ClassificationResult(
                bestClassification.getClassName(),
                bestClassification.getProbability(),
                classifications.topK(5)
        );
    }

    public record ClassificationResult(
            String className,
            double confidence,
            List<Classification> topClassifications
    ) {}
}

// 自然語言處理
@Service
public class TextAnalysisService {
    
    private Predictor<String, String> sentimentPredictor;

    @PostConstruct
    public void initializeNLP() throws Exception {
        Criteria<String, String> criteria = Criteria.builder()
                .optApplication(Application.NLP.SENTIMENT_ANALYSIS)
                .setTypes(String.class, String.class)
                .optEngine("PyTorch")
                .build();

        ZooModel<String, String> model = criteria.loadModel();
        this.sentimentPredictor = model.newPredictor();
    }

    public SentimentResult analyzeSentiment(String text) throws Exception {
        String result = sentimentPredictor.predict(text);
        
        // 解析結果
        return parseSentimentResult(result);
    }

    private SentimentResult parseSentimentResult(String result) {
        // 實作結果解析邏輯
        return new SentimentResult(
                result.contains("POSITIVE") ? "POSITIVE" : "NEGATIVE",
                extractConfidence(result)
        );
    }

    public record SentimentResult(String sentiment, double confidence) {}
}
```

#### 14.6.2 Weka 機器學習整合

```java
@Service
public class MachineLearningService {
    
    public ClassificationModel trainModel(String dataPath) throws Exception {
        // 載入資料
        DataSource source = new DataSource(dataPath);
        Instances data = source.getDataSet();
        
        // 設定類別屬性
        if (data.classIndex() == -1) {
            data.setClassIndex(data.numAttributes() - 1);
        }

        // 分割訓練和測試資料
        data.randomize(new Random(1));
        int trainSize = (int) Math.round(data.numInstances() * 0.8);
        int testSize = data.numInstances() - trainSize;
        
        Instances trainData = new Instances(data, 0, trainSize);
        Instances testData = new Instances(data, trainSize, testSize);

        // 建立分類器
        RandomForest classifier = new RandomForest();
        classifier.setNumIterations(100);
        classifier.buildClassifier(trainData);

        // 評估模型
        Evaluation eval = new Evaluation(trainData);
        eval.evaluateModel(classifier, testData);

        return new ClassificationModel(classifier, eval);
    }

    public PredictionResult predict(ClassificationModel model, double[] features) throws Exception {
        Instances schema = model.getSchema();
        Instance instance = new DenseInstance(features.length);
        instance.setDataset(schema);
        
        for (int i = 0; i < features.length - 1; i++) {
            instance.setValue(i, features[i]);
        }

        double prediction = model.getClassifier().classifyInstance(instance);
        double[] distribution = model.getClassifier().distributionForInstance(instance);

        return new PredictionResult(
                schema.classAttribute().value((int) prediction),
                distribution[0],
                distribution
        );
    }

    public static class ClassificationModel {
        private final RandomForest classifier;
        private final Evaluation evaluation;

        public ClassificationModel(RandomForest classifier, Evaluation evaluation) {
            this.classifier = classifier;
            this.evaluation = evaluation;
        }

        public double getAccuracy() {
            return (1.0 - evaluation.errorRate()) * 100;
        }

        // getters...
    }

    public record PredictionResult(
            String predictedClass,
            double confidence,
            double[] classDistribution
    ) {}
}
```

### 14.7 ReactiveX 與響應式程式設計

#### 14.7.1 RxJava 進階應用

```java
@Service
public class ReactiveDataProcessingService {
    
    private final WebClient webClient;
    private final DatabaseClient databaseClient;

    public ReactiveDataProcessingService(WebClient webClient, DatabaseClient databaseClient) {
        this.webClient = webClient;
        this.databaseClient = databaseClient;
    }

    // 複雜的資料流處理
    public Observable<ProcessedData> processDataStream() {
        return Observable.fromCallable(this::fetchUserIds)
                .flatMapObservable(Observable::fromIterable)
                .flatMap(this::enrichUserData, 10) // 並行處理，最多10個並行請求
                .filter(user -> user.isActive())
                .groupBy(User::getDepartment)
                .flatMap(this::aggregateByDepartment)
                .doOnNext(this::logProgress)
                .doOnError(this::handleError)
                .retry(3) // 重試機制
                .timeout(30, TimeUnit.SECONDS); // 超時設定
    }

    private Observable<User> enrichUserData(String userId) {
        // 結合多個資料源
        Observable<UserProfile> profileObs = fetchUserProfile(userId);
        Observable<UserPreferences> preferencesObs = fetchUserPreferences(userId);
        Observable<UserActivity> activityObs = fetchUserActivity(userId);

        return Observable.zip(profileObs, preferencesObs, activityObs,
                (profile, preferences, activity) -> new User(profile, preferences, activity));
    }

    private Observable<ProcessedData> aggregateByDepartment(GroupedObservable<String, User> groupedUsers) {
        return groupedUsers
                .buffer(100) // 批次處理
                .map(users -> new ProcessedData(
                        groupedUsers.getKey(),
                        users.size(),
                        calculateAverageActivity(users),
                        extractTopSkills(users)
                ));
    }

    // 背壓處理
    public Flowable<SensorData> processSensorStream() {
        return Flowable.interval(100, TimeUnit.MILLISECONDS)
                .map(tick -> generateSensorData())
                .onBackpressureBuffer(1000) // 緩衝區大小
                .observeOn(Schedulers.computation())
                .map(this::analyzeSensorData)
                .filter(analysis -> analysis.isAnomalous())
                .doOnNext(this::sendAlert);
    }

    // 錯誤處理和恢復策略
    public Single<ApiResponse> resilientApiCall(String endpoint) {
        return webClient.get()
                .uri(endpoint)
                .retrieve()
                .toEntity(String.class)
                .toObservable()
                .toSingle()
                .map(response -> new ApiResponse(response.getBody()))
                .retryWhen(errors -> 
                    errors.zipWith(Observable.range(1, 3), (error, attempt) -> {
                        if (attempt >= 3) {
                            throw new RuntimeException("重試次數已用盡", error);
                        }
                        return Observable.timer(attempt * 1000, TimeUnit.MILLISECONDS);
                    }).flatMap(timer -> timer)
                )
                .onErrorReturn(error -> new ApiResponse("服務暫時不可用"));
    }

    // 複雜的組合操作
    public Observable<RecommendationResult> generateRecommendations(String userId) {
        return Observable.just(userId)
                .flatMap(id -> Observable.zip(
                    getUserBehavior(id),
                    getSimilarUsers(id),
                    getPopularItems(),
                    (behavior, similarUsers, popularItems) -> 
                        new RecommendationContext(behavior, similarUsers, popularItems)
                ))
                .flatMap(context -> 
                    Observable.fromIterable(context.getSimilarUsers())
                        .flatMap(similarUser -> getUserPreferences(similarUser.getId()))
                        .reduce(new HashMap<String, Double>(), this::mergePreferences)
                        .toObservable()
                        .map(mergedPreferences -> 
                            generateRecommendations(context, mergedPreferences))
                )
                .doOnSubscribe(disposable -> log.info("開始生成推薦"))
                .doOnNext(result -> log.info("推薦生成完成: {}", result))
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread()); // 在 Android 中使用
    }
}

// 自訂操作符
public class CustomRxOperators {
    
    // 批次化操作符
    public static <T> ObservableTransformer<T, List<T>> bufferWithTimeout(
            int maxSize, long timeout, TimeUnit timeUnit) {
        
        return upstream -> upstream.publish(shared -> 
            Observable.merge(
                shared.buffer(maxSize),
                shared.buffer(timeout, timeUnit).filter(list -> !list.isEmpty())
            )
        );
    }

    // 去重操作符
    public static <T, K> ObservableTransformer<T, T> distinctUntilChanged(
            Function<T, K> keySelector, long windowDuration, TimeUnit timeUnit) {
        
        return upstream -> upstream
            .groupBy(keySelector)
            .flatMap(group -> group
                .distinctUntilChanged()
                .window(windowDuration, timeUnit)
                .flatMap(window -> window.takeLast(1))
            );
    }

    // 重試與指數退避
    public static <T> ObservableTransformer<T, T> retryWithExponentialBackoff(
            int maxRetries, long initialDelay, TimeUnit timeUnit) {
        
        return upstream -> upstream.retryWhen(errors -> 
            errors.zipWith(Observable.range(1, maxRetries + 1), (error, attempt) -> {
                if (attempt > maxRetries) {
                    throw new RuntimeException("重試次數已用盡", error);
                }
                long delay = initialDelay * (long) Math.pow(2, attempt - 1);
                return Observable.timer(delay, timeUnit);
            }).flatMap(timer -> timer)
        );
    }
}
```

通過這些補充內容，您的Java教學文件現在包含了：

1. **容器化與雲端部署** - Docker、Kubernetes、AWS等現代部署方式
2. **現代Java開發工具** - 最新的建置工具、測試框架、程式碼品質工具
3. **Java生態系統與框架** - Spring WebFlux、微服務、消息驅動架構
4. **Java 21新特性** - Virtual Threads、Pattern Matching、String Templates
5. **企業級開發模式** - Clean Architecture、CQRS模式
6. **AI/ML整合** - DJL、Weka等機器學習框架的使用
7. **響應式程式設計** - RxJava進階應用和自訂操作符

這些內容涵蓋了現代Java開發的各個重要面向，讓學習者能夠掌握從基礎到企業級應用的完整技能棧。