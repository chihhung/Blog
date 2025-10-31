# C# 程式語言教學手冊

## 目錄

1. [基礎入門](#1-基礎入門)
   - 1.1 [C# 與 .NET 基本概念](#11-c-與-net-基本概念)
   - 1.2 [開發環境設定](#12-開發環境設定)
   - 1.3 [基本語法](#13-基本語法)
     - 1.3.1 [變數與資料型別](#131-變數與資料型別)
     - 1.3.2 [流程控制](#132-流程控制)
     - 1.3.3 [函式 (方法)](#133-函式-方法)
     - 1.3.4 [例外處理](#134-例外處理)

2. [物件導向程式設計 (OOP)](#2-物件導向程式設計-oop)
   - 2.1 [類別與物件基礎](#21-類別與物件基礎)
     - 2.1.1 [類別定義](#211-類別定義)
     - 2.1.2 [存取修飾詞](#212-存取修飾詞)
   - 2.2 [繼承 (Inheritance)](#22-繼承-inheritance)
     - 2.2.1 [基本繼承](#221-基本繼承)
   - 2.3 [多型 (Polymorphism)](#23-多型-polymorphism)
     - 2.3.1 [虛擬方法與覆寫](#231-虛擬方法與覆寫)
   - 2.4 [介面 (Interface)](#24-介面-interface)
     - 2.4.1 [介面定義與實作](#241-介面定義與實作)
   - 2.5 [抽象類別](#25-抽象類別)

3. [進階語法與實務](#3-進階語法與實務)
   - 3.1 [泛型 (Generics)](#31-泛型-generics)
     - 3.1.1 [泛型基礎概念](#311-泛型基礎概念)
     - 3.1.2 [泛型約束](#312-泛型約束)
   - 3.2 [委派與事件 (Delegates & Events)](#32-委派與事件-delegates--events)
     - 3.2.1 [委派基礎](#321-委派基礎)
     - 3.2.2 [內建委派型別 (Func, Action, Predicate)](#322-內建委派型別-func-action-predicate)
   - 3.3 [LINQ 語法與集合操作](#33-linq-語法與集合操作)
     - 3.3.1 [LINQ 基礎查詢](#331-linq-基礎查詢)
     - 3.3.2 [進階 LINQ 操作與實務應用](#332-進階-linq-操作與實務應用)
   - 3.4 [非同步程式設計 (async/await)](#34-非同步程式設計-asyncawait)
     - 3.4.1 [非同步基礎概念](#341-非同步基礎概念)
     - 3.4.2 [非同步最佳實務與進階應用](#342-非同步最佳實務與進階應用)

4. [專案實務應用](#4-專案實務應用)
   - 4.1 [Web API 開發 (ASP.NET Core)](#41-web-api-開發-aspnet-core)
     - 4.1.1 [建立基本 Web API](#411-建立基本-web-api)
   - 4.2 [資料庫存取 (Entity Framework Core)](#42-資料庫存取-entity-framework-core)
     - 4.2.1 [Entity Framework 設定](#421-entity-framework-設定)
   - 4.3 [單元測試 (xUnit)](#43-單元測試-xunit)
     - 4.3.1 [基本單元測試](#431-基本單元測試)
   - 4.4 [錯誤處理與日誌紀錄](#44-錯誤處理與日誌紀錄)
     - 4.4.1 [全域錯誤處理](#441-全域錯誤處理)

5. [認證考試對應](#5-認證考試對應)
   - 5.1 [Microsoft C# 認證考試概述](#51-microsoft-c-認證考試概述)
     - 5.1.1 [考試架構](#511-考試架構)
     - 5.1.2 [考試準備策略](#512-考試準備策略)
   - 5.2 [考試重點整理](#52-考試重點整理)
     - 5.2.1 [語言基礎考點](#521-語言基礎考點)
     - 5.2.2 [物件導向考點](#522-物件導向考點)
     - 5.2.3 [進階考點](#523-進階考點)
   - 5.3 [模擬考題](#53-模擬考題)
     - 5.3.1 [選擇題範例](#531-選擇題範例)
     - 5.3.2 [程式題範例](#532-程式題範例)
   - 5.4 [考試策略與技巧](#54-考試策略與技巧)
     - 5.4.1 [時間管理](#541-時間管理)
     - 5.4.2 [答題技巧](#542-答題技巧)

6. [附錄](#6-附錄)
   - 6.1 [常見問題 FAQ](#61-常見問題-faq)
   - 6.2 [學習資源](#62-學習資源)
     - 6.2.1 [官方文件](#621-官方文件)
     - 6.2.2 [練習網站](#622-練習網站)
     - 6.2.3 [推薦書籍](#623-推薦書籍)
     - 6.2.4 [開發工具](#624-開發工具)
   - 6.3 [建議學習路徑](#63-建議學習路徑)
     - 6.3.1 [初級階段 (1-2 個月)](#631-初級階段-1-2-個月)
     - 6.3.2 [中級階段 (2-3 個月)](#632-中級階段-2-3-個月)
     - 6.3.3 [高級階段 (3-4 個月)](#633-高級階段-3-4-個月)
   - 6.4 [檢查清單 (Checklist)](#64-檢查清單-checklist)
     - 6.4.1 [基礎知識檢查](#641-基礎知識檢查)
     - 6.4.2 [物件導向檢查](#642-物件導向檢查)
     - 6.4.3 [進階技術檢查](#643-進階技術檢查)
     - 6.4.4 [實務開發檢查](#644-實務開發檢查)
     - 6.4.5 [認證準備檢查](#645-認證準備檢查)
   - 6.5 [總結](#65-總結)

---

## 1. 基礎入門

### 1.1 C# 與 .NET 基本概念

#### 什麼是 C#？
C# (C Sharp) 是 Microsoft 開發的現代物件導向程式語言，具有以下特色：
- **型別安全**：編譯時期檢查型別，減少執行時期錯誤
- **垃圾回收**：自動記憶體管理，不需手動釋放記憶體
- **跨平台**：可在 Windows、Linux、macOS 上執行
- **豐富的函式庫**：擁有完整的 .NET 類別庫

#### .NET 生態系統
- **.NET Framework**：Windows 專用的傳統版本
- **.NET Core/.NET 5+**：跨平台的現代版本
- **.NET Standard**：統一的 API 規範

#### C# 的應用領域
- Web 應用程式 (ASP.NET Core)
- 桌面應用程式 (WPF, WinForms)
- 手機應用程式 (Xamarin, .NET MAUI)
- 遊戲開發 (Unity)
- 雲端服務 (Azure)

**認證考點提示**：
- 理解 .NET 生態系統的差異
- 掌握 C# 的核心特性與應用範圍

---

### 1.2 開發環境設定

#### Visual Studio 安裝
1. 下載 Visual Studio Community (免費版)
2. 選擇工作負載：
   - .NET 桌面開發
   - ASP.NET 和 Web 開發
   - .NET Core 跨平台開發

#### VS Code 替代方案
如果偏好輕量級編輯器：
1. 安裝 VS Code
2. 安裝 C# 擴充功能
3. 安裝 .NET SDK

#### 第一個 C# 程式

```csharp
using System;

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
            Console.WriteLine("歡迎學習 C#！");
            Console.ReadLine(); // 等待使用者按 Enter
        }
    }
}
```

**程式說明**：
- `using System`：引用系統命名空間
- `namespace`：定義命名空間，避免名稱衝突
- `class Program`：定義主要類別
- `Main` 方法：程式進入點
- `Console.WriteLine`：輸出文字到控制台

**小練習**：
1. 修改程式，輸出您的姓名
2. 加入多行輸出，顯示今天的日期

**認證考點提示**：
- 熟悉基本程式結構
- 理解命名空間的用途

---

### 1.3 基本語法

#### 1.3.1 變數與資料型別

##### 基本資料型別

```csharp
// 整數型別
int age = 25;
long bigNumber = 1234567890L;

// 浮點數型別
float height = 175.5f;
double weight = 70.5;
decimal price = 99.99m; // 金額計算建議使用

// 字元與字串
char grade = 'A';
string name = "王小明";

// 布林值
bool isStudent = true;
```

##### 變數宣告方式

```csharp
// 明確指定型別
string firstName = "John";

// 型別推斷 (var)
var lastName = "Doe"; // 編譯器自動推斷為 string
var count = 10;       // 編譯器自動推斷為 int

// 常數
const double PI = 3.14159;
```

##### 字串操作

```csharp
string firstName = "王";
string lastName = "小明";

// 字串連接
string fullName1 = firstName + lastName;
string fullName2 = string.Concat(firstName, lastName);

// 字串插值 (建議使用)
string greeting = $"你好，{firstName}{lastName}！";

// 字串格式化
string info = string.Format("姓名：{0}，年齡：{1}", fullName1, 25);
```

**小練習**：
```csharp
// 練習：計算兩個數字的運算
int a = 10;
int b = 3;

Console.WriteLine($"加法：{a} + {b} = {a + b}");
Console.WriteLine($"減法：{a} - {b} = {a - b}");
Console.WriteLine($"乘法：{a} * {b} = {a * b}");
Console.WriteLine($"除法：{a} / {b} = {(double)a / b:F2}");
Console.WriteLine($"餘數：{a} % {b} = {a % b}");
```

#### 1.3.2 流程控制

##### if-else 條件判斷

```csharp
int score = 85;

if (score >= 90)
{
    Console.WriteLine("優秀");
}
else if (score >= 70)
{
    Console.WriteLine("良好");
}
else if (score >= 60)
{
    Console.WriteLine("及格");
}
else
{
    Console.WriteLine("不及格");
}

// 三元運算子
string result = score >= 60 ? "及格" : "不及格";
```

##### switch 語句

```csharp
char grade = 'B';

switch (grade)
{
    case 'A':
        Console.WriteLine("優秀");
        break;
    case 'B':
        Console.WriteLine("良好");
        break;
    case 'C':
        Console.WriteLine("普通");
        break;
    default:
        Console.WriteLine("需要改進");
        break;
}

// C# 8.0+ 的 switch 表達式
string gradeDescription = grade switch
{
    'A' => "優秀",
    'B' => "良好",
    'C' => "普通",
    _ => "需要改進"
};
```

##### 迴圈

```csharp
// for 迴圈
Console.WriteLine("for 迴圈：");
for (int i = 1; i <= 5; i++)
{
    Console.WriteLine($"第 {i} 次");
}

// while 迴圈
Console.WriteLine("\nwhile 迴圈：");
int count = 1;
while (count <= 3)
{
    Console.WriteLine($"計數：{count}");
    count++;
}

// do-while 迴圈
Console.WriteLine("\ndo-while 迴圈：");
int number;
do
{
    Console.Write("請輸入 1-10 之間的數字：");
    string input = Console.ReadLine();
    int.TryParse(input, out number);
} while (number < 1 || number > 10);

// foreach 迴圈 (用於集合)
string[] fruits = { "蘋果", "香蕉", "橘子" };
Console.WriteLine("\nforeach 迴圈：");
foreach (string fruit in fruits)
{
    Console.WriteLine($"水果：{fruit}");
}
```

**小練習**：
```csharp
// 練習：九九乘法表
for (int i = 1; i <= 9; i++)
{
    for (int j = 1; j <= 9; j++)
    {
        Console.Write($"{i} × {j} = {i * j:D2}  ");
    }
    Console.WriteLine();
}
```

#### 1.3.3 函式 (方法)

##### 基本函式定義

```csharp
class Calculator
{
    // 無回傳值的方法
    public static void PrintWelcome()
    {
        Console.WriteLine("歡迎使用計算機！");
    }

    // 有回傳值的方法
    public static int Add(int a, int b)
    {
        return a + b;
    }

    // 多個參數的方法
    public static double CalculateArea(double width, double height)
    {
        return width * height;
    }

    // 預設參數值
    public static void Greet(string name, string message = "您好")
    {
        Console.WriteLine($"{message}，{name}！");
    }

    // 參數陣列 (params)
    public static int Sum(params int[] numbers)
    {
        int total = 0;
        foreach (int number in numbers)
        {
            total += number;
        }
        return total;
    }
}

// 使用範例
class Program
{
    static void Main()
    {
        Calculator.PrintWelcome();
        
        int result = Calculator.Add(5, 3);
        Console.WriteLine($"5 + 3 = {result}");
        
        double area = Calculator.CalculateArea(10.5, 8.2);
        Console.WriteLine($"面積 = {area:F2}");
        
        Calculator.Greet("王小明");
        Calculator.Greet("李小華", "早安");
        
        int sum = Calculator.Sum(1, 2, 3, 4, 5);
        Console.WriteLine($"總和 = {sum}");
    }
}
```

##### 方法多載 (Method Overloading)

```csharp
public class MathHelper
{
    // 整數版本
    public static int Max(int a, int b)
    {
        return a > b ? a : b;
    }
    
    // 浮點數版本
    public static double Max(double a, double b)
    {
        return a > b ? a : b;
    }
    
    // 三個參數版本
    public static int Max(int a, int b, int c)
    {
        return Max(Max(a, b), c);
    }
}
```

#### 1.3.4 例外處理

##### try-catch-finally

```csharp
public class ExceptionDemo
{
    public static void DivisionExample()
    {
        try
        {
            Console.Write("請輸入被除數：");
            int dividend = int.Parse(Console.ReadLine());
            
            Console.Write("請輸入除數：");
            int divisor = int.Parse(Console.ReadLine());
            
            int result = dividend / divisor;
            Console.WriteLine($"結果：{dividend} ÷ {divisor} = {result}");
        }
        catch (DivideByZeroException ex)
        {
            Console.WriteLine("錯誤：除數不能為零！");
            Console.WriteLine($"詳細錯誤：{ex.Message}");
        }
        catch (FormatException ex)
        {
            Console.WriteLine("錯誤：輸入格式不正確，請輸入數字！");
            Console.WriteLine($"詳細錯誤：{ex.Message}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"發生未預期的錯誤：{ex.Message}");
        }
        finally
        {
            Console.WriteLine("計算結束。");
        }
    }
    
    // 安全的型別轉換
    public static void SafeParsingExample()
    {
        Console.Write("請輸入一個數字：");
        string input = Console.ReadLine();
        
        if (int.TryParse(input, out int number))
        {
            Console.WriteLine($"您輸入的數字是：{number}");
        }
        else
        {
            Console.WriteLine("輸入的不是有效數字。");
        }
    }
}
```

##### 自訂例外

```csharp
// 自訂例外類別
public class InvalidAgeException : Exception
{
    public InvalidAgeException() : base("年齡必須在 0 到 150 之間")
    {
    }
    
    public InvalidAgeException(string message) : base(message)
    {
    }
}

// 使用自訂例外
public class Person
{
    private int age;
    
    public int Age
    {
        get { return age; }
        set
        {
            if (value < 0 || value > 150)
            {
                throw new InvalidAgeException($"無效的年齡：{value}");
            }
            age = value;
        }
    }
}
```

**實務案例**：檔案讀取的例外處理

```csharp
using System.IO;

public class FileHelper
{
    public static string ReadTextFile(string filePath)
    {
        try
        {
            return File.ReadAllText(filePath);
        }
        catch (FileNotFoundException)
        {
            Console.WriteLine($"檔案不存在：{filePath}");
            return string.Empty;
        }
        catch (UnauthorizedAccessException)
        {
            Console.WriteLine("沒有權限讀取檔案。");
            return string.Empty;
        }
        catch (IOException ex)
        {
            Console.WriteLine($"檔案讀取錯誤：{ex.Message}");
            return string.Empty;
        }
    }
}
```

**小練習**：
```csharp
// 練習：建立一個安全的除法計算器
public static class SafeCalculator
{
    public static double SafeDivide(double dividend, double divisor)
    {
        try
        {
            if (divisor == 0)
                throw new DivideByZeroException("除數不能為零");
                
            return dividend / divisor;
        }
        catch (DivideByZeroException ex)
        {
            Console.WriteLine($"計算錯誤：{ex.Message}");
            return double.NaN; // 回傳 NaN 表示無效結果
        }
    }
}
```

**認證考點提示**：
- 熟悉各種資料型別的使用場合
- 掌握流程控制的語法和應用
- 理解方法的定義、呼叫和多載
- 了解例外處理的最佳實務
- 學會使用 TryParse 等安全的轉換方法

**注意事項**：
1. 使用 `decimal` 進行金額計算，避免浮點數精度問題
2. 字串比較建議使用 `string.Equals()` 或 `StringComparison`
3. 例外處理應該具體化，不要只用泛用的 `Exception`
4. 在 `finally` 區塊中釋放資源 (如檔案、資料庫連線)

---

## 2. 物件導向程式設計 (OOP)

### 2.1 類別與物件基礎

#### 2.1.1 類別定義

類別是物件的藍圖，定義了物件的屬性（資料）和方法（行為）。

```csharp
public class Student
{
    // 欄位 (Fields) - 私有資料
    private string name;
    private int age;
    private string studentId;
    
    // 屬性 (Properties) - 封裝的存取方式
    public string Name
    {
        get { return name; }
        set 
        { 
            if (!string.IsNullOrEmpty(value))
                name = value; 
        }
    }
    
    public int Age
    {
        get { return age; }
        set 
        { 
            if (value >= 0 && value <= 150)
                age = value; 
        }
    }
    
    // 自動屬性 (Auto-implemented Properties)
    public string StudentId { get; set; }
    public double GPA { get; set; }
    
    // 建構子 (Constructor)
    public Student()
    {
        StudentId = "未設定";
        GPA = 0.0;
    }
    
    public Student(string name, int age, string studentId)
    {
        Name = name;
        Age = age;
        StudentId = studentId;
        GPA = 0.0;
    }
    
    // 方法 (Methods)
    public void DisplayInfo()
    {
        Console.WriteLine($"學生資訊：");
        Console.WriteLine($"姓名：{Name}");
        Console.WriteLine($"年齡：{Age}");
        Console.WriteLine($"學號：{StudentId}");
        Console.WriteLine($"GPA：{GPA:F2}");
    }
    
    public void UpdateGPA(double newGPA)
    {
        if (newGPA >= 0.0 && newGPA <= 4.0)
        {
            GPA = newGPA;
            Console.WriteLine($"{Name} 的 GPA 已更新為 {GPA:F2}");
        }
        else
        {
            Console.WriteLine("GPA 必須在 0.0 到 4.0 之間");
        }
    }
}

// 使用範例
class Program
{
    static void Main()
    {
        // 建立物件
        Student student1 = new Student();
        student1.Name = "王小明";
        student1.Age = 20;
        student1.StudentId = "S001";
        
        Student student2 = new Student("李小華", 19, "S002");
        
        // 呼叫方法
        student1.DisplayInfo();
        student1.UpdateGPA(3.75);
        
        Console.WriteLine("\n" + new string('-', 30) + "\n");
        
        student2.DisplayInfo();
        student2.UpdateGPA(3.92);
    }
}
```

#### 2.1.2 存取修飾詞

```csharp
public class AccessModifierDemo
{
    public string PublicField;        // 任何地方都可存取
    private string privateField;     // 只有同類別內可存取
    protected string protectedField; // 同類別或衍生類別可存取
    internal string internalField;   // 同組件內可存取
    
    public void PublicMethod() 
    { 
        // 可從任何地方呼叫
        Console.WriteLine("這是公開方法");
    }
    
    private void PrivateMethod() 
    { 
        // 只能在同類別內呼叫
        Console.WriteLine("這是私有方法");
    }
    
    protected void ProtectedMethod() 
    { 
        // 同類別或衍生類別可呼叫
        Console.WriteLine("這是受保護方法");
    }
    
    internal void InternalMethod() 
    { 
        // 同組件內可呼叫
        Console.WriteLine("這是內部方法");
    }
}
```

### 2.2 繼承 (Inheritance)

#### 2.2.1 基本繼承

```csharp
// 基底類別 (Base Class)
public class Person
{
    public string Name { get; set; }
    public int Age { get; set; }
    
    public Person(string name, int age)
    {
        Name = name;
        Age = age;
    }
    
    public virtual void Introduce()
    {
        Console.WriteLine($"我是 {Name}，今年 {Age} 歲");
    }
    
    public virtual void Work()
    {
        Console.WriteLine($"{Name} 正在工作");
    }
}

// 衍生類別 (Derived Class)
public class Student : Person
{
    public string StudentId { get; set; }
    public string Major { get; set; }
    
    public Student(string name, int age, string studentId, string major) 
        : base(name, age) // 呼叫基底類別建構子
    {
        StudentId = studentId;
        Major = major;
    }
    
    // 覆寫 (Override) 基底類別的方法
    public override void Introduce()
    {
        base.Introduce(); // 呼叫基底類別的方法
        Console.WriteLine($"我是 {Major} 系的學生，學號是 {StudentId}");
    }
    
    public override void Work()
    {
        Console.WriteLine($"學生 {Name} 正在讀書和做作業");
    }
    
    // 新增學生特有的方法
    public void Study(string subject)
    {
        Console.WriteLine($"{Name} 正在學習 {subject}");
    }
}

public class Teacher : Person
{
    public string Subject { get; set; }
    public decimal Salary { get; set; }
    
    public Teacher(string name, int age, string subject, decimal salary) 
        : base(name, age)
    {
        Subject = subject;
        Salary = salary;
    }
    
    public override void Introduce()
    {
        base.Introduce();
        Console.WriteLine($"我教授 {Subject}");
    }
    
    public override void Work()
    {
        Console.WriteLine($"老師 {Name} 正在教授 {Subject}");
    }
    
    public void Teach(string lesson)
    {
        Console.WriteLine($"{Name} 老師正在教授：{lesson}");
    }
}

// 使用範例
class Program
{
    static void Main()
    {
        Student student = new Student("王小明", 20, "S001", "資訊工程");
        Teacher teacher = new Teacher("李老師", 35, "程式設計", 60000);
        
        student.Introduce();
        student.Work();
        student.Study("C# 程式設計");
        
        Console.WriteLine("\n" + new string('-', 40) + "\n");
        
        teacher.Introduce();
        teacher.Work();
        teacher.Teach("物件導向程式設計");
        
        // 多型應用
        Console.WriteLine("\n多型範例：");
        Person[] people = { student, teacher };
        
        foreach (Person person in people)
        {
            person.Work(); // 會呼叫各自覆寫的版本
        }
    }
}
```

### 2.3 多型 (Polymorphism)

#### 2.3.1 虛擬方法與覆寫

```csharp
public abstract class Shape
{
    public string Name { get; set; }
    
    public Shape(string name)
    {
        Name = name;
    }
    
    // 抽象方法 - 子類別必須實作
    public abstract double CalculateArea();
    
    // 虛擬方法 - 子類別可以選擇覆寫
    public virtual void DisplayInfo()
    {
        Console.WriteLine($"圖形：{Name}");
        Console.WriteLine($"面積：{CalculateArea():F2}");
    }
}

public class Rectangle : Shape
{
    public double Width { get; set; }
    public double Height { get; set; }
    
    public Rectangle(double width, double height) : base("矩形")
    {
        Width = width;
        Height = height;
    }
    
    public override double CalculateArea()
    {
        return Width * Height;
    }
    
    public override void DisplayInfo()
    {
        base.DisplayInfo();
        Console.WriteLine($"寬度：{Width}, 高度：{Height}");
    }
}

public class Circle : Shape
{
    public double Radius { get; set; }
    
    public Circle(double radius) : base("圓形")
    {
        Radius = radius;
    }
    
    public override double CalculateArea()
    {
        return Math.PI * Radius * Radius;
    }
    
    public override void DisplayInfo()
    {
        base.DisplayInfo();
        Console.WriteLine($"半徑：{Radius}");
    }
}

// 多型應用
public class ShapeCalculator
{
    public static void ProcessShapes(Shape[] shapes)
    {
        double totalArea = 0;
        
        Console.WriteLine("處理所有圖形：");
        foreach (Shape shape in shapes)
        {
            shape.DisplayInfo(); // 多型：會呼叫各自的實作
            totalArea += shape.CalculateArea();
            Console.WriteLine(new string('-', 30));
        }
        
        Console.WriteLine($"總面積：{totalArea:F2}");
    }
}

// 使用範例
class Program
{
    static void Main()
    {
        Shape[] shapes = 
        {
            new Rectangle(5.0, 3.0),
            new Circle(2.5),
            new Rectangle(4.0, 4.0),
            new Circle(1.8)
        };
        
        ShapeCalculator.ProcessShapes(shapes);
    }
}
```

### 2.4 介面 (Interface)

#### 2.4.1 介面定義與實作

```csharp
// 介面定義
public interface IDrawable
{
    void Draw();
    void SetColor(string color);
}

public interface IMovable
{
    void Move(int x, int y);
    int X { get; set; }
    int Y { get; set; }
}

// 實作多個介面
public class GameCharacter : IDrawable, IMovable
{
    public string Name { get; set; }
    public string Color { get; private set; }
    public int X { get; set; }
    public int Y { get; set; }
    
    public GameCharacter(string name)
    {
        Name = name;
        Color = "白色";
        X = 0;
        Y = 0;
    }
    
    // 實作 IDrawable 介面
    public void Draw()
    {
        Console.WriteLine($"在位置 ({X}, {Y}) 繪製{Color}的 {Name}");
    }
    
    public void SetColor(string color)
    {
        Color = color;
        Console.WriteLine($"{Name} 的顏色設定為 {Color}");
    }
    
    // 實作 IMovable 介面
    public void Move(int x, int y)
    {
        X = x;
        Y = y;
        Console.WriteLine($"{Name} 移動到位置 ({X}, {Y})");
    }
}

// 介面作為參數型別
public class GameEngine
{
    public static void DrawAllObjects(IDrawable[] objects)
    {
        Console.WriteLine("繪製所有物件：");
        foreach (IDrawable obj in objects)
        {
            obj.Draw();
        }
    }
    
    public static void MoveAllObjects(IMovable[] objects, int deltaX, int deltaY)
    {
        Console.WriteLine("移動所有物件：");
        foreach (IMovable obj in objects)
        {
            obj.Move(obj.X + deltaX, obj.Y + deltaY);
        }
    }
}

// 使用範例
class Program
{
    static void Main()
    {
        GameCharacter player = new GameCharacter("玩家");
        GameCharacter enemy = new GameCharacter("敵人");
        
        // 設定屬性
        player.SetColor("藍色");
        enemy.SetColor("紅色");
        
        // 移動物件
        player.Move(10, 5);
        enemy.Move(20, 15);
        
        // 使用介面作為型別
        IDrawable[] drawableObjects = { player, enemy };
        GameEngine.DrawAllObjects(drawableObjects);
        
        IMovable[] movableObjects = { player, enemy };
        GameEngine.MoveAllObjects(movableObjects, 5, 3);
        
        // 重新繪製
        GameEngine.DrawAllObjects(drawableObjects);
    }
}
```

### 2.5 抽象類別

```csharp
public abstract class Vehicle
{
    public string Brand { get; set; }
    public string Model { get; set; }
    public int Year { get; set; }
    
    protected Vehicle(string brand, string model, int year)
    {
        Brand = brand;
        Model = model;
        Year = year;
    }
    
    // 抽象方法 - 子類別必須實作
    public abstract void Start();
    public abstract void Stop();
    public abstract double CalculateFuelConsumption(double distance);
    
    // 一般方法 - 子類別可以使用
    public virtual void DisplayInfo()
    {
        Console.WriteLine($"車輛資訊：{Year} {Brand} {Model}");
    }
    
    // 受保護的方法 - 只有子類別可以使用
    protected void LogOperation(string operation)
    {
        Console.WriteLine($"[{DateTime.Now:HH:mm:ss}] {Brand} {Model}: {operation}");
    }
}

public class Car : Vehicle
{
    public int Doors { get; set; }
    public double EngineSize { get; set; }
    
    public Car(string brand, string model, int year, int doors, double engineSize)
        : base(brand, model, year)
    {
        Doors = doors;
        EngineSize = engineSize;
    }
    
    public override void Start()
    {
        LogOperation("汽車引擎啟動");
        Console.WriteLine($"{Brand} {Model} 汽車已啟動");
    }
    
    public override void Stop()
    {
        LogOperation("汽車引擎關閉");
        Console.WriteLine($"{Brand} {Model} 汽車已停止");
    }
    
    public override double CalculateFuelConsumption(double distance)
    {
        // 簡化的油耗計算：引擎越大，油耗越高
        double consumptionRate = EngineSize * 8; // 每100公里消耗的升數
        return (distance / 100) * consumptionRate;
    }
    
    public override void DisplayInfo()
    {
        base.DisplayInfo();
        Console.WriteLine($"車門數：{Doors}，引擎大小：{EngineSize}L");
    }
}

public class Motorcycle : Vehicle
{
    public int CylinderCount { get; set; }
    
    public Motorcycle(string brand, string model, int year, int cylinderCount)
        : base(brand, model, year)
    {
        CylinderCount = cylinderCount;
    }
    
    public override void Start()
    {
        LogOperation("機車引擎啟動");
        Console.WriteLine($"{Brand} {Model} 機車已啟動");
    }
    
    public override void Stop()
    {
        LogOperation("機車引擎關閉");
        Console.WriteLine($"{Brand} {Model} 機車已停止");
    }
    
    public override double CalculateFuelConsumption(double distance)
    {
        // 機車通常比汽車省油
        double consumptionRate = CylinderCount * 2.5;
        return (distance / 100) * consumptionRate;
    }
    
    public override void DisplayInfo()
    {
        base.DisplayInfo();
        Console.WriteLine($"汽缸數：{CylinderCount}");
    }
}

// 使用範例
class Program
{
    static void Main()
    {
        Vehicle[] vehicles = 
        {
            new Car("Toyota", "Camry", 2023, 4, 2.5),
            new Motorcycle("Yamaha", "R3", 2023, 2),
            new Car("BMW", "X5", 2023, 4, 3.0)
        };
        
        foreach (Vehicle vehicle in vehicles)
        {
            Console.WriteLine(new string('=', 50));
            vehicle.DisplayInfo();
            vehicle.Start();
            
            double distance = 100; // 100公里
            double fuel = vehicle.CalculateFuelConsumption(distance);
            Console.WriteLine($"行駛 {distance} 公里需要 {fuel:F2} 升燃油");
            
            vehicle.Stop();
            Console.WriteLine();
        }
    }
}
```

**小練習**：

```csharp
// 練習：建立一個圖書管理系統
public abstract class LibraryItem
{
    public string Title { get; set; }
    public string Author { get; set; }
    public string ISBN { get; set; }
    public bool IsAvailable { get; set; }
    
    public LibraryItem(string title, string author, string isbn)
    {
        Title = title;
        Author = author;
        ISBN = isbn;
        IsAvailable = true;
    }
    
    public abstract void DisplayDetails();
    public abstract int GetLoanPeriodDays();
    
    public virtual bool BorrowItem()
    {
        if (IsAvailable)
        {
            IsAvailable = false;
            Console.WriteLine($"已借出：{Title}");
            return true;
        }
        Console.WriteLine($"無法借出：{Title} 目前不可借用");
        return false;
    }
    
    public virtual void ReturnItem()
    {
        IsAvailable = true;
        Console.WriteLine($"已歸還：{Title}");
    }
}

public class Book : LibraryItem
{
    public int Pages { get; set; }
    public string Genre { get; set; }
    
    public Book(string title, string author, string isbn, int pages, string genre)
        : base(title, author, isbn)
    {
        Pages = pages;
        Genre = genre;
    }
    
    public override void DisplayDetails()
    {
        Console.WriteLine($"書籍：{Title}");
        Console.WriteLine($"作者：{Author}");
        Console.WriteLine($"ISBN：{ISBN}");
        Console.WriteLine($"頁數：{Pages}");
        Console.WriteLine($"類型：{Genre}");
        Console.WriteLine($"狀態：{(IsAvailable ? "可借用" : "已借出")}");
    }
    
    public override int GetLoanPeriodDays()
    {
        return 14; // 書籍可借14天
    }
}

public class DVD : LibraryItem
{
    public int DurationMinutes { get; set; }
    public string Director { get; set; }
    
    public DVD(string title, string director, string isbn, int duration)
        : base(title, director, isbn)
    {
        DurationMinutes = duration;
        Director = director;
    }
    
    public override void DisplayDetails()
    {
        Console.WriteLine($"DVD：{Title}");
        Console.WriteLine($"導演：{Director}");
        Console.WriteLine($"ISBN：{ISBN}");
        Console.WriteLine($"片長：{DurationMinutes} 分鐘");
        Console.WriteLine($"狀態：{(IsAvailable ? "可借用" : "已借出")}");
    }
    
    public override int GetLoanPeriodDays()
    {
        return 7; // DVD可借7天
    }
}
```

**認證考點提示**：

- 理解類別與物件的關係
- 掌握繼承的語法和 `base` 關鍵字使用
- 了解多型的概念和虛擬方法覆寫
- 分辨抽象類別與介面的差異和使用時機
- 熟悉存取修飾詞的作用範圍
- 理解建構子的繼承和呼叫順序

**注意事項**：

1. 優先使用屬性而非公開欄位
2. 抽象類別用於有共同實作的繼承關係
3. 介面用於定義契約，支援多重實作
4. 適當使用 `virtual` 和 `override` 關鍵字
5. 在建構子中進行適當的驗證

---

## 3. 進階語法與實務

### 3.1 泛型 (Generics)

#### 3.1.1 泛型基礎概念

泛型允許您在不指定具體型別的情況下撰寫程式碼，提供型別安全和效能優化。

```csharp
// 泛型類別
public class GenericList<T>
{
    private T[] items;
    private int count;
    
    public GenericList(int capacity = 10)
    {
        items = new T[capacity];
        count = 0;
    }
    
    public void Add(T item)
    {
        if (count >= items.Length)
        {
            Array.Resize(ref items, items.Length * 2);
        }
        items[count++] = item;
    }
    
    public T Get(int index)
    {
        if (index < 0 || index >= count)
        {
            throw new IndexOutOfRangeException("索引超出範圍");
        }
        return items[index];
    }
    
    public int Count => count;
    
    public void Display()
    {
        Console.WriteLine($"清單內容 (共 {count} 項):");
        for (int i = 0; i < count; i++)
        {
            Console.WriteLine($"[{i}] {items[i]}");
        }
    }
}

// 泛型方法
public class GenericMethods
{
    public static void Swap<T>(ref T first, ref T second)
    {
        T temp = first;
        first = second;
        second = temp;
    }
    
    public static T FindMax<T>(T[] array) where T : IComparable<T>
    {
        if (array == null || array.Length == 0)
        {
            throw new ArgumentException("陣列不能為空");
        }
        
        T max = array[0];
        for (int i = 1; i < array.Length; i++)
        {
            if (array[i].CompareTo(max) > 0)
            {
                max = array[i];
            }
        }
        return max;
    }
    
    public static bool AreEqual<T>(T first, T second) where T : IEquatable<T>
    {
        return first.Equals(second);
    }
}

// 使用範例
class Program
{
    static void Main()
    {
        // 使用泛型類別
        GenericList<string> stringList = new GenericList<string>();
        stringList.Add("Apple");
        stringList.Add("Banana");
        stringList.Add("Cherry");
        stringList.Display();
        
        GenericList<int> intList = new GenericList<int>();
        intList.Add(10);
        intList.Add(20);
        intList.Add(30);
        intList.Display();
        
        // 使用泛型方法
        int a = 5, b = 10;
        Console.WriteLine($"交換前：a = {a}, b = {b}");
        GenericMethods.Swap(ref a, ref b);
        Console.WriteLine($"交換後：a = {a}, b = {b}");
        
        int[] numbers = { 3, 7, 2, 9, 1, 8 };
        int maxNumber = GenericMethods.FindMax(numbers);
        Console.WriteLine($"最大值：{maxNumber}");
        
        string[] words = { "apple", "zebra", "banana", "cherry" };
        string maxWord = GenericMethods.FindMax(words);
        Console.WriteLine($"最大字串：{maxWord}");
    }
}
```

#### 3.1.2 泛型約束

```csharp
// 不同類型的泛型約束
public class GenericConstraints
{
    // 類型約束：T 必須是類別
    public static T CreateInstance<T>() where T : class, new()
    {
        return new T();
    }
    
    // 值類型約束：T 必須是值類型
    public static bool IsDefault<T>(T value) where T : struct
    {
        return value.Equals(default(T));
    }
    
    // 介面約束：T 必須實作 IComparable
    public static void SortArray<T>(T[] array) where T : IComparable<T>
    {
        Array.Sort(array);
    }
    
    // 基類約束：T 必須繼承自 Animal
    public static void FeedAnimal<T>(T animal) where T : Animal
    {
        animal.Eat();
        Console.WriteLine($"餵食了 {animal.Name}");
    }
    
    // 多重約束
    public static void ProcessItem<T>(T item) 
        where T : class, IDisposable, new()
    {
        using (T instance = new T())
        {
            // 處理項目
            Console.WriteLine($"處理項目：{instance.GetType().Name}");
        }
    }
}

// 用於約束示範的基類
public abstract class Animal
{
    public string Name { get; set; }
    
    public Animal(string name)
    {
        Name = name;
    }
    
    public abstract void Eat();
}

public class Dog : Animal
{
    public Dog() : base("狗") { }
    public Dog(string name) : base(name) { }
    
    public override void Eat()
    {
        Console.WriteLine($"{Name} 正在吃狗糧");
    }
}

// 泛型集合自訂實作
public class Stack<T>
{
    private T[] items;
    private int top;
    
    public Stack(int capacity = 10)
    {
        items = new T[capacity];
        top = -1;
    }
    
    public void Push(T item)
    {
        if (top >= items.Length - 1)
        {
            Array.Resize(ref items, items.Length * 2);
        }
        items[++top] = item;
    }
    
    public T Pop()
    {
        if (IsEmpty())
        {
            throw new InvalidOperationException("堆疊是空的");
        }
        return items[top--];
    }
    
    public T Peek()
    {
        if (IsEmpty())
        {
            throw new InvalidOperationException("堆疊是空的");
        }
        return items[top];
    }
    
    public bool IsEmpty() => top == -1;
    public int Count => top + 1;
}
```

### 3.2 委派與事件 (Delegates & Events)

#### 3.2.1 委派基礎

```csharp
// 宣告委派型別
public delegate int MathOperation(int a, int b);
public delegate void NotificationHandler(string message);

public class DelegateDemo
{
    // 符合委派簽章的方法
    public static int Add(int a, int b)
    {
        Console.WriteLine($"執行加法：{a} + {b}");
        return a + b;
    }
    
    public static int Multiply(int a, int b)
    {
        Console.WriteLine($"執行乘法：{a} × {b}");
        return a * b;
    }
    
    public static int Subtract(int a, int b)
    {
        Console.WriteLine($"執行減法：{a} - {b}");
        return a - b;
    }
    
    public static void SendEmail(string message)
    {
        Console.WriteLine($"發送郵件：{message}");
    }
    
    public static void SendSMS(string message)
    {
        Console.WriteLine($"發送簡訊：{message}");
    }
    
    public static void LogMessage(string message)
    {
        Console.WriteLine($"記錄日誌：{message}");
    }
}

// 計算器類別使用委派
public class Calculator
{
    public static void ExecuteOperation(MathOperation operation, int a, int b)
    {
        try
        {
            int result = operation(a, b);
            Console.WriteLine($"結果：{result}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"計算錯誤：{ex.Message}");
        }
    }
    
    public static void ExecuteMultipleOperations(MathOperation[] operations, int a, int b)
    {
        Console.WriteLine($"對數字 {a} 和 {b} 執行多個運算：");
        foreach (var operation in operations)
        {
            ExecuteOperation(operation, a, b);
        }
    }
}

// 多播委派示範
public class NotificationService
{
    public static void SendNotifications(NotificationHandler handlers, string message)
    {
        Console.WriteLine("開始發送通知...");
        handlers?.Invoke(message); // 呼叫所有註冊的方法
        Console.WriteLine("通知發送完成。");
    }
}

// 使用範例
class Program
{
    static void Main()
    {
        // 單一委派
        MathOperation operation = DelegateDemo.Add;
        Calculator.ExecuteOperation(operation, 10, 5);
        
        // 變更委派指向的方法
        operation = DelegateDemo.Multiply;
        Calculator.ExecuteOperation(operation, 10, 5);
        
        // 多個委派
        MathOperation[] operations = 
        {
            DelegateDemo.Add,
            DelegateDemo.Subtract,
            DelegateDemo.Multiply
        };
        Calculator.ExecuteMultipleOperations(operations, 15, 3);
        
        // 多播委派
        NotificationHandler notificationHandler = DelegateDemo.SendEmail;
        notificationHandler += DelegateDemo.SendSMS;  // 加入另一個方法
        notificationHandler += DelegateDemo.LogMessage; // 再加入一個方法
        
        NotificationService.SendNotifications(notificationHandler, "系統維護通知");
        
        // 移除委派
        notificationHandler -= DelegateDemo.SendSMS;
        Console.WriteLine("\n移除簡訊通知後：");
        NotificationService.SendNotifications(notificationHandler, "重要更新通知");
    }
}
```

#### 3.2.2 內建委派型別 (Func, Action, Predicate)

```csharp
public class BuiltInDelegates
{
    public static void DemonstrateAction()
    {
        Console.WriteLine("=== Action 委派示範 ===");
        
        // Action：無回傳值的委派
        Action simpleAction = () => Console.WriteLine("執行簡單動作");
        simpleAction();
        
        Action<string> printMessage = message => Console.WriteLine($"訊息：{message}");
        printMessage("Hello World");
        
        Action<int, int> printSum = (a, b) => Console.WriteLine($"{a} + {b} = {a + b}");
        printSum(5, 3);
    }
    
    public static void DemonstrateFunc()
    {
        Console.WriteLine("\n=== Func 委派示範 ===");
        
        // Func：有回傳值的委派
        Func<int> getRandomNumber = () => new Random().Next(1, 101);
        Console.WriteLine($"隨機數字：{getRandomNumber()}");
        
        Func<int, int, int> add = (a, b) => a + b;
        Console.WriteLine($"5 + 3 = {add(5, 3)}");
        
        Func<string, int> getStringLength = text => text?.Length ?? 0;
        Console.WriteLine($"字串長度：{getStringLength("Hello C#")}");
        
        // 複雜的 Func 範例
        Func<int[], int> findMax = numbers =>
        {
            if (numbers == null || numbers.Length == 0)
                return 0;
            
            int max = numbers[0];
            foreach (int num in numbers)
            {
                if (num > max) max = num;
            }
            return max;
        };
        
        int[] testNumbers = { 3, 7, 2, 9, 1, 8 };
        Console.WriteLine($"最大值：{findMax(testNumbers)}");
    }
    
    public static void DemonstratePredicate()
    {
        Console.WriteLine("\n=== Predicate 委派示範 ===");
        
        // Predicate：回傳 bool 的委派
        Predicate<int> isEven = number => number % 2 == 0;
        Predicate<string> isLongString = text => text?.Length > 5;
        
        int[] numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        string[] words = { "C#", "Java", "Python", "JavaScript", "Go" };
        
        Console.WriteLine("偶數：");
        foreach (int num in numbers)
        {
            if (isEven(num))
                Console.Write($"{num} ");
        }
        
        Console.WriteLine("\n長字串：");
        foreach (string word in words)
        {
            if (isLongString(word))
                Console.Write($"{word} ");
        }
        Console.WriteLine();
    }
}

// 實際應用：事件處理系統
public class EventDemo
{
    // 事件相關委派
    public delegate void OrderEventHandler(string orderInfo);
    
    public class OrderService
    {
        // 宣告事件
        public event OrderEventHandler OrderCreated;
        public event OrderEventHandler OrderCancelled;
        public event Action<string, decimal> OrderPaid;
        
        public void CreateOrder(string orderInfo)
        {
            Console.WriteLine($"建立訂單：{orderInfo}");
            
            // 觸發事件
            OrderCreated?.Invoke(orderInfo);
        }
        
        public void CancelOrder(string orderInfo)
        {
            Console.WriteLine($"取消訂單：{orderInfo}");
            
            // 觸發事件
            OrderCancelled?.Invoke(orderInfo);
        }
        
        public void PayOrder(string orderInfo, decimal amount)
        {
            Console.WriteLine($"付款訂單：{orderInfo}，金額：{amount:C}");
            
            // 觸發事件
            OrderPaid?.Invoke(orderInfo, amount);
        }
    }
    
    public class EmailService
    {
        public void OnOrderCreated(string orderInfo)
        {
            Console.WriteLine($"[郵件] 訂單建立通知：{orderInfo}");
        }
        
        public void OnOrderCancelled(string orderInfo)
        {
            Console.WriteLine($"[郵件] 訂單取消通知：{orderInfo}");
        }
    }
    
    public class InventoryService
    {
        public void OnOrderCreated(string orderInfo)
        {
            Console.WriteLine($"[庫存] 保留商品：{orderInfo}");
        }
        
        public void OnOrderCancelled(string orderInfo)
        {
            Console.WriteLine($"[庫存] 釋放商品：{orderInfo}");
        }
    }
    
    public class AccountingService
    {
        public void OnOrderPaid(string orderInfo, decimal amount)
        {
            Console.WriteLine($"[會計] 記錄收入：{orderInfo}，金額：{amount:C}");
        }
    }
    
    public static void RunDemo()
    {
        OrderService orderService = new OrderService();
        EmailService emailService = new EmailService();
        InventoryService inventoryService = new InventoryService();
        AccountingService accountingService = new AccountingService();
        
        // 訂閱事件
        orderService.OrderCreated += emailService.OnOrderCreated;
        orderService.OrderCreated += inventoryService.OnOrderCreated;
        orderService.OrderCancelled += emailService.OnOrderCancelled;
        orderService.OrderCancelled += inventoryService.OnOrderCancelled;
        orderService.OrderPaid += accountingService.OnOrderPaid;
        
        // 使用 Lambda 表達式訂閱事件
        orderService.OrderPaid += (order, amount) => 
            Console.WriteLine($"[日誌] 訂單 {order} 付款 {amount:C} 已記錄");
        
        // 執行業務操作
        Console.WriteLine("=== 訂單處理示範 ===");
        orderService.CreateOrder("ORD-001: iPhone 14");
        Console.WriteLine();
        
        orderService.PayOrder("ORD-001: iPhone 14", 30000);
        Console.WriteLine();
        
        orderService.CancelOrder("ORD-002: iPad Air");
    }
}
```

### 3.3 LINQ 語法與集合操作

#### 3.3.1 LINQ 基礎查詢

```csharp
using System.Linq;

public class Student
{
    public int Id { get; set; }
    public string Name { get; set; }
    public int Age { get; set; }
    public string Major { get; set; }
    public double GPA { get; set; }
    public List<string> Courses { get; set; }
    
    public Student(int id, string name, int age, string major, double gpa)
    {
        Id = id;
        Name = name;
        Age = age;
        Major = major;
        GPA = gpa;
        Courses = new List<string>();
    }
    
    public override string ToString()
    {
        return $"[{Id}] {Name} ({Age}歲) - {Major} - GPA: {GPA:F2}";
    }
}

public class LinqDemo
{
    public static List<Student> GetSampleStudents()
    {
        return new List<Student>
        {
            new Student(1, "王小明", 20, "資訊工程", 3.75) 
                { Courses = { "程式設計", "資料結構", "資料庫" } },
            new Student(2, "李小華", 19, "電機工程", 3.92) 
                { Courses = { "電路學", "訊號處理", "程式設計" } },
            new Student(3, "張小強", 21, "資訊工程", 3.45) 
                { Courses = { "演算法", "網路安全", "軟體工程" } },
            new Student(4, "陳小美", 20, "企業管理", 3.88) 
                { Courses = { "管理學", "會計學", "行銷學" } },
            new Student(5, "林小志", 22, "資訊工程", 3.21) 
                { Courses = { "人工智慧", "機器學習", "資料科學" } },
            new Student(6, "黃小花", 18, "電機工程", 3.95) 
                { Courses = { "微積分", "物理學", "程式設計" } }
        };
    }
    
    public static void BasicQueries()
    {
        var students = GetSampleStudents();
        
        Console.WriteLine("=== LINQ 基本查詢 ===");
        
        // Where：條件篩選
        var topStudents = students.Where(s => s.GPA >= 3.8);
        Console.WriteLine("GPA >= 3.8 的學生：");
        foreach (var student in topStudents)
        {
            Console.WriteLine($"  {student}");
        }
        
        // Select：投影 (選擇特定欄位)
        var studentNames = students.Select(s => s.Name);
        Console.WriteLine($"\n所有學生姓名：{string.Join(", ", studentNames)}");
        
        // Select with transformation
        var studentInfo = students.Select(s => new 
        { 
            Name = s.Name, 
            Level = s.GPA >= 3.8 ? "優秀" : s.GPA >= 3.5 ? "良好" : "普通"
        });
        
        Console.WriteLine("\n學生評等：");
        foreach (var info in studentInfo)
        {
            Console.WriteLine($"  {info.Name}: {info.Level}");
        }
        
        // OrderBy：排序
        var sortedByGPA = students.OrderByDescending(s => s.GPA).ThenBy(s => s.Age);
        Console.WriteLine("\n按 GPA 降序，年齡升序排列：");
        foreach (var student in sortedByGPA)
        {
            Console.WriteLine($"  {student}");
        }
        
        // GroupBy：分組
        var groupedByMajor = students.GroupBy(s => s.Major);
        Console.WriteLine("\n按科系分組：");
        foreach (var group in groupedByMajor)
        {
            Console.WriteLine($"  {group.Key} ({group.Count()} 人):");
            foreach (var student in group)
            {
                Console.WriteLine($"    {student}");
            }
        }
    }
    
    public static void AggregateQueries()
    {
        var students = GetSampleStudents();
        
        Console.WriteLine("\n=== LINQ 聚合查詢 ===");
        
        // Count：計數
        int totalStudents = students.Count();
        int csStudents = students.Count(s => s.Major == "資訊工程");
        Console.WriteLine($"總學生數：{totalStudents}");
        Console.WriteLine($"資訊工程學生數：{csStudents}");
        
        // Average, Min, Max, Sum
        double averageGPA = students.Average(s => s.GPA);
        double minGPA = students.Min(s => s.GPA);
        double maxGPA = students.Max(s => s.GPA);
        int totalAge = students.Sum(s => s.Age);
        
        Console.WriteLine($"平均 GPA：{averageGPA:F2}");
        Console.WriteLine($"最低 GPA：{minGPA:F2}");
        Console.WriteLine($"最高 GPA：{maxGPA:F2}");
        Console.WriteLine($"年齡總和：{totalAge}");
        
        // First, Last, Single
        var firstStudent = students.First();
        var lastCSStudent = students.Where(s => s.Major == "資訊工程").Last();
        var youngestStudent = students.OrderBy(s => s.Age).First();
        
        Console.WriteLine($"第一個學生：{firstStudent.Name}");
        Console.WriteLine($"最後一個資工學生：{lastCSStudent.Name}");
        Console.WriteLine($"年紀最小的學生：{youngestStudent.Name} ({youngestStudent.Age}歲)");
        
        // Any, All
        bool hasExcellentStudent = students.Any(s => s.GPA >= 3.9);
        bool allPassedGPA = students.All(s => s.GPA >= 2.0);
        
        Console.WriteLine($"是否有優秀學生 (GPA >= 3.9)：{hasExcellentStudent}");
        Console.WriteLine($"所有學生都及格 (GPA >= 2.0)：{allPassedGPA}");
    }
    
    public static void ComplexQueries()
    {
        var students = GetSampleStudents();
        
        Console.WriteLine("\n=== LINQ 複合查詢 ===");
        
        // 複合條件查詢
        var qualifiedStudents = students
            .Where(s => s.Age >= 20 && s.GPA >= 3.5)
            .OrderByDescending(s => s.GPA)
            .Select(s => new { s.Name, s.Major, s.GPA })
            .Take(3); // 取前3名
        
        Console.WriteLine("年齡 >= 20 且 GPA >= 3.5 的前3名學生：");
        foreach (var student in qualifiedStudents)
        {
            Console.WriteLine($"  {student.Name} - {student.Major} - {student.GPA:F2}");
        }
        
        // 分組後的聚合
        var majorStats = students
            .GroupBy(s => s.Major)
            .Select(g => new
            {
                Major = g.Key,
                Count = g.Count(),
                AverageGPA = g.Average(s => s.GPA),
                MaxGPA = g.Max(s => s.GPA)
            })
            .OrderByDescending(x => x.AverageGPA);
        
        Console.WriteLine("\n各科系統計：");
        foreach (var stat in majorStats)
        {
            Console.WriteLine($"  {stat.Major}: {stat.Count}人, 平均GPA: {stat.AverageGPA:F2}, 最高GPA: {stat.MaxGPA:F2}");
        }
        
        // SelectMany：展開集合
        var allCourses = students
            .SelectMany(s => s.Courses)
            .Distinct()
            .OrderBy(course => course);
        
        Console.WriteLine($"\n所有課程：{string.Join(", ", allCourses)}");
        
        // 課程統計
        var courseStats = students
            .SelectMany(s => s.Courses.Select(course => new { Student = s.Name, Course = course }))
            .GroupBy(x => x.Course)
            .Select(g => new { Course = g.Key, StudentCount = g.Count() })
            .OrderByDescending(x => x.StudentCount);
        
        Console.WriteLine("\n課程選修統計：");
        foreach (var stat in courseStats)
        {
            Console.WriteLine($"  {stat.Course}: {stat.StudentCount} 人選修");
        }
    }
    
    // LINQ 查詢語法 vs 方法語法
    public static void QuerySyntaxDemo()
    {
        var students = GetSampleStudents();
        
        Console.WriteLine("\n=== 查詢語法 vs 方法語法 ===");
        
        // 查詢語法 (Query Syntax)
        var queryResult = from s in students
                         where s.Major == "資訊工程" && s.GPA >= 3.5
                         orderby s.GPA descending
                         select new { s.Name, s.GPA };
        
        Console.WriteLine("查詢語法結果：");
        foreach (var result in queryResult)
        {
            Console.WriteLine($"  {result.Name}: {result.GPA:F2}");
        }
        
        // 方法語法 (Method Syntax) - 等價的查詢
        var methodResult = students
            .Where(s => s.Major == "資訊工程" && s.GPA >= 3.5)
            .OrderByDescending(s => s.GPA)
            .Select(s => new { s.Name, s.GPA });
        
        Console.WriteLine("\n方法語法結果：");
        foreach (var result in methodResult)
        {
            Console.WriteLine($"  {result.Name}: {result.GPA:F2}");
        }
    }
}
```

#### 3.3.2 進階 LINQ 操作與實務應用

```csharp
public class AdvancedLinqDemo
{
    // 複雜的資料模型
    public class Order
    {
        public int OrderId { get; set; }
        public string CustomerName { get; set; }
        public DateTime OrderDate { get; set; }
        public decimal TotalAmount { get; set; }
        public List<OrderItem> Items { get; set; } = new List<OrderItem>();
        public string Status { get; set; }
    }
    
    public class OrderItem
    {
        public int ProductId { get; set; }
        public string ProductName { get; set; }
        public int Quantity { get; set; }
        public decimal UnitPrice { get; set; }
        public string Category { get; set; }
    }
    
    public static List<Order> GetSampleOrders()
    {
        return new List<Order>
        {
            new Order
            {
                OrderId = 1001,
                CustomerName = "王大明",
                OrderDate = DateTime.Now.AddDays(-10),
                TotalAmount = 2500,
                Status = "已完成",
                Items = 
                {
                    new OrderItem { ProductId = 1, ProductName = "筆記型電腦", Quantity = 1, UnitPrice = 2000, Category = "電子" },
                    new OrderItem { ProductId = 2, ProductName = "滑鼠", Quantity = 2, UnitPrice = 250, Category = "電子" }
                }
            },
            new Order
            {
                OrderId = 1002,
                CustomerName = "李小華",
                OrderDate = DateTime.Now.AddDays(-5),
                TotalAmount = 1800,
                Status = "進行中",
                Items = 
                {
                    new OrderItem { ProductId = 3, ProductName = "書桌", Quantity = 1, UnitPrice = 1500, Category = "家具" },
                    new OrderItem { ProductId = 4, ProductName = "台燈", Quantity = 1, UnitPrice = 300, Category = "家具" }
                }
            },
            new Order
            {
                OrderId = 1003,
                CustomerName = "張小強",
                OrderDate = DateTime.Now.AddDays(-3),
                TotalAmount = 950,
                Status = "已取消",
                Items = 
                {
                    new OrderItem { ProductId = 5, ProductName = "咖啡杯", Quantity = 3, UnitPrice = 150, Category = "生活用品" },
                    new OrderItem { ProductId = 6, ProductName = "保溫瓶", Quantity = 2, UnitPrice = 250, Category = "生活用品" }
                }
            }
        };
    }
    
    // Join 操作
    public static void JoinOperations()
    {
        var orders = GetSampleOrders();
        var customers = new List<dynamic>
        {
            new { Name = "王大明", City = "台北", VIPLevel = "金卡" },
            new { Name = "李小華", City = "台中", VIPLevel = "銀卡" },
            new { Name = "張小強", City = "高雄", VIPLevel = "一般" }
        };
        
        Console.WriteLine("=== Join 操作示範 ===");
        
        // Inner Join
        var customerOrders = from order in orders
                           join customer in customers on order.CustomerName equals customer.Name
                           select new
                           {
                               OrderId = order.OrderId,
                               Customer = customer.Name,
                               City = customer.City,
                               VIPLevel = customer.VIPLevel,
                               Amount = order.TotalAmount,
                               Status = order.Status
                           };
        
        Console.WriteLine("客戶訂單資訊：");
        foreach (var item in customerOrders)
        {
            Console.WriteLine($"  訂單 {item.OrderId}: {item.Customer} ({item.City}, {item.VIPLevel}) - ${item.Amount} [{item.Status}]");
        }
        
        // Group Join
        var customerWithOrders = from customer in customers
                               join order in orders on customer.Name equals order.CustomerName into customerOrders
                               select new
                               {
                                   Customer = customer,
                                   Orders = customerOrders.ToList(),
                                   TotalSpent = customerOrders.Sum(o => o.TotalAmount)
                               };
        
        Console.WriteLine("\n客戶訂單匯總：");
        foreach (var item in customerWithOrders)
        {
            Console.WriteLine($"  {item.Customer.Name} ({item.Customer.City}): {item.Orders.Count} 筆訂單, 總消費 ${item.TotalSpent}");
        }
    }
    
    // 分組與統計
    public static void GroupingAndAggregation()
    {
        var orders = GetSampleOrders();
        
        Console.WriteLine("\n=== 分組與統計 ===");
        
        // 多層分組
        var categoryStats = orders
            .SelectMany(o => o.Items)
            .GroupBy(item => item.Category)
            .Select(g => new
            {
                Category = g.Key,
                TotalQuantity = g.Sum(item => item.Quantity),
                TotalRevenue = g.Sum(item => item.Quantity * item.UnitPrice),
                ProductCount = g.Select(item => item.ProductId).Distinct().Count(),
                AveragePrice = g.Average(item => item.UnitPrice)
            })
            .OrderByDescending(x => x.TotalRevenue);
        
        Console.WriteLine("產品類別統計：");
        foreach (var stat in categoryStats)
        {
            Console.WriteLine($"  {stat.Category}: 銷量 {stat.TotalQuantity}, 營收 ${stat.TotalRevenue}, " +
                            $"產品數 {stat.ProductCount}, 平均價格 ${stat.AveragePrice:F2}");
        }
        
        // 時間分組
        var monthlyStats = orders
            .Where(o => o.Status == "已完成")
            .GroupBy(o => new { Year = o.OrderDate.Year, Month = o.OrderDate.Month })
            .Select(g => new
            {
                Period = $"{g.Key.Year}-{g.Key.Month:D2}",
                OrderCount = g.Count(),
                TotalRevenue = g.Sum(o => o.TotalAmount),
                AverageOrderValue = g.Average(o => o.TotalAmount)
            })
            .OrderBy(x => x.Period);
        
        Console.WriteLine("\n月份統計 (僅已完成訂單)：");
        foreach (var stat in monthlyStats)
        {
            Console.WriteLine($"  {stat.Period}: {stat.OrderCount} 筆訂單, 營收 ${stat.TotalRevenue}, " +
                            $"平均訂單價值 ${stat.AverageOrderValue:F2}");
        }
    }
    
    // 條件式查詢與動態篩選
    public static void ConditionalQueries()
    {
        var orders = GetSampleOrders();
        
        Console.WriteLine("\n=== 條件式查詢 ===");
        
        // 動態建構查詢條件
        string statusFilter = "已完成"; // 可來自使用者輸入
        decimal? minAmount = 1000;      // 可選的金額篩選
        string categoryFilter = null;   // 可選的類別篩選
        
        var query = orders.AsQueryable();
        
        if (!string.IsNullOrEmpty(statusFilter))
        {
            query = query.Where(o => o.Status == statusFilter);
        }
        
        if (minAmount.HasValue)
        {
            query = query.Where(o => o.TotalAmount >= minAmount.Value);
        }
        
        if (!string.IsNullOrEmpty(categoryFilter))
        {
            query = query.Where(o => o.Items.Any(item => item.Category == categoryFilter));
        }
        
        var results = query.ToList();
        
        Console.WriteLine($"符合條件的訂單 (狀態: {statusFilter}, 最低金額: ${minAmount})：");
        foreach (var order in results)
        {
            Console.WriteLine($"  訂單 {order.OrderId}: {order.CustomerName} - ${order.TotalAmount} [{order.Status}]");
        }
        
        // 使用 Where 的條件式邏輯
        var flexibleQuery = orders
            .Where(o => (statusFilter == null || o.Status == statusFilter) &&
                       (!minAmount.HasValue || o.TotalAmount >= minAmount.Value))
            .Select(o => new { o.OrderId, o.CustomerName, o.TotalAmount, o.Status });
        
        Console.WriteLine("\n彈性查詢結果：");
        foreach (var item in flexibleQuery)
        {
            Console.WriteLine($"  {item.OrderId}: {item.CustomerName} - ${item.TotalAmount} [{item.Status}]");
        }
    }
    
    // 複雜的數據轉換
    public static void DataTransformation()
    {
        var orders = GetSampleOrders();
        
        Console.WriteLine("\n=== 數據轉換 ===");
        
        // 階層式資料轉換
        var customerReport = orders
            .GroupBy(o => o.CustomerName)
            .Select(customerGroup => new
            {
                CustomerName = customerGroup.Key,
                TotalOrders = customerGroup.Count(),
                TotalSpent = customerGroup.Sum(o => o.TotalAmount),
                OrderDetails = customerGroup.Select(o => new
                {
                    OrderId = o.OrderId,
                    Date = o.OrderDate.ToString("yyyy-MM-dd"),
                    Amount = o.TotalAmount,
                    Status = o.Status,
                    Categories = o.Items.Select(item => item.Category).Distinct().ToList()
                }).ToList(),
                PreferredCategories = customerGroup
                    .SelectMany(o => o.Items)
                    .GroupBy(item => item.Category)
                    .OrderByDescending(g => g.Sum(item => item.Quantity * item.UnitPrice))
                    .Take(2)
                    .Select(g => g.Key)
                    .ToList()
            });
        
        Console.WriteLine("客戶詳細報告：");
        foreach (var report in customerReport)
        {
            Console.WriteLine($"\n客戶：{report.CustomerName}");
            Console.WriteLine($"  訂單總數：{report.TotalOrders}");
            Console.WriteLine($"  總消費：${report.TotalSpent}");
            Console.WriteLine($"  偏好類別：{string.Join(", ", report.PreferredCategories)}");
            Console.WriteLine("  訂單明細：");
            foreach (var order in report.OrderDetails)
            {
                Console.WriteLine($"    {order.OrderId} ({order.Date}): ${order.Amount} [{order.Status}] - " +
                                $"類別: {string.Join(", ", order.Categories)}");
            }
        }
    }
    
    // 效能考量與最佳實務
    public static void PerformanceConsiderations()
    {
        var orders = GetSampleOrders();
        
        Console.WriteLine("\n=== 效能最佳實務 ===");
        
        // 避免多次列舉
        Console.WriteLine("✓ 好的做法 - 使用 ToList() 快取結果：");
        var expensiveQuery = orders
            .Where(o => o.TotalAmount > 1000)
            .ToList(); // 快取結果，避免重複計算
        
        Console.WriteLine($"符合條件的訂單數：{expensiveQuery.Count}");
        Console.WriteLine($"總金額：${expensiveQuery.Sum(o => o.TotalAmount)}");
        
        // 使用 Any() 而非 Count() > 0
        Console.WriteLine("\n✓ 好的做法 - 使用 Any() 檢查存在性：");
        bool hasExpensiveOrders = orders.Any(o => o.TotalAmount > 2000);
        Console.WriteLine($"是否有高價訂單：{hasExpensiveOrders}");
        
        // 適當使用 Take() 限制結果數量
        Console.WriteLine("\n✓ 好的做法 - 使用 Take() 限制結果：");
        var topOrders = orders
            .OrderByDescending(o => o.TotalAmount)
            .Take(2) // 只取前2筆，提升效能
            .Select(o => new { o.OrderId, o.TotalAmount });
        
        Console.WriteLine("前2高價訂單：");
        foreach (var order in topOrders)
        {
            Console.WriteLine($"  訂單 {order.OrderId}: ${order.TotalAmount}");
        }
        
        // 推遲執行 (Deferred Execution) 示範
        Console.WriteLine("\n推遲執行示範：");
        var deferredQuery = orders.Where(o => o.Status == "已完成"); // 此時尚未執行
        
        Console.WriteLine("查詢已建立，但尚未執行");
        
        // 修改原始資料
        orders.Add(new Order { OrderId = 1004, Status = "已完成", CustomerName = "新客戶", TotalAmount = 500 });
        
        // 現在執行查詢，會包含新加入的資料
        var results = deferredQuery.ToList();
        Console.WriteLine($"執行後的結果數量：{results.Count} (包含新加入的資料)");
    }
}

// 使用範例
class Program
{
    static void Main()
    {
        AdvancedLinqDemo.JoinOperations();
        AdvancedLinqDemo.GroupingAndAggregation();
        AdvancedLinqDemo.ConditionalQueries();
        AdvancedLinqDemo.DataTransformation();
        AdvancedLinqDemo.PerformanceConsiderations();
    }

}
```

### 3.4 非同步程式設計 (async/await)

#### 3.4.1 非同步基礎概念

```csharp
using System.Threading.Tasks;
using System.Net.Http;

public class AsyncBasics
{
    // 基本的非同步方法
    public static async Task<string> GetDataAsync(string url)
    {
        Console.WriteLine($"開始下載：{url}");
        
        using (HttpClient client = new HttpClient())
        {
            try
            {
                string result = await client.GetStringAsync(url);
                Console.WriteLine($"下載完成：{url}");
                return result;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"下載失敗：{ex.Message}");
                return string.Empty;
            }
        }
    }
    
    // 模擬耗時操作
    public static async Task<int> CalculateAsync(int number)
    {
        Console.WriteLine($"開始計算：{number}");
        
        // 模擬耗時計算
        await Task.Delay(2000); // 等待2秒
        
        int result = number * number;
        Console.WriteLine($"計算完成：{number}² = {result}");
        return result;
    }
    
    // 無回傳值的非同步方法
    public static async Task ProcessDataAsync(string data)
    {
        Console.WriteLine("開始處理資料...");
        
        await Task.Delay(1500); // 模擬處理時間
        
        Console.WriteLine($"資料處理完成：{data.Length} 個字元");
    }
    
    // 並行執行多個非同步操作
    public static async Task RunParallelOperationsAsync()
    {
        Console.WriteLine("=== 並行操作示範 ===");
        
        // 建立多個任務
        Task<int> task1 = CalculateAsync(5);
        Task<int> task2 = CalculateAsync(10);
        Task<int> task3 = CalculateAsync(15);
        
        // 等待所有任務完成
        int[] results = await Task.WhenAll(task1, task2, task3);
        
        Console.WriteLine("所有計算完成，結果：");
        for (int i = 0; i < results.Length; i++)
        {
            Console.WriteLine($"  任務 {i + 1}：{results[i]}");
        }
        
        int totalSum = results.Sum();
        Console.WriteLine($"總和：{totalSum}");
    }
    
    // 逐步執行的非同步操作
    public static async Task RunSequentialOperationsAsync()
    {
        Console.WriteLine("\n=== 逐步操作示範 ===");
        
        var stopwatch = System.Diagnostics.Stopwatch.StartNew();
        
        int result1 = await CalculateAsync(3);
        int result2 = await CalculateAsync(7);
        int result3 = await CalculateAsync(12);
        
        stopwatch.Stop();
        
        Console.WriteLine($"逐步執行總時間：{stopwatch.ElapsedMilliseconds} 毫秒");
        Console.WriteLine($"結果總和：{result1 + result2 + result3}");
    }
}

// 實際應用：檔案處理
public class FileProcessor
{
    public static async Task<string> ReadFileAsync(string filePath)
    {
        try
        {
            Console.WriteLine($"開始讀取檔案：{filePath}");
            
            using (var reader = new StreamReader(filePath))
            {
                string content = await reader.ReadToEndAsync();
                Console.WriteLine($"檔案讀取完成：{content.Length} 個字元");
                return content;
            }
        }
        catch (FileNotFoundException)
        {
            Console.WriteLine($"檔案不存在：{filePath}");
            return string.Empty;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"讀取檔案時發生錯誤：{ex.Message}");
            return string.Empty;
        }
    }
    
    public static async Task WriteFileAsync(string filePath, string content)
    {
        try
        {
            Console.WriteLine($"開始寫入檔案：{filePath}");
            
            using (var writer = new StreamWriter(filePath))
            {
                await writer.WriteAsync(content);
                Console.WriteLine($"檔案寫入完成：{content.Length} 個字元");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"寫入檔案時發生錯誤：{ex.Message}");
        }
    }
    
    public static async Task ProcessMultipleFilesAsync(string[] filePaths)
    {
        Console.WriteLine("=== 處理多個檔案 ===");
        
        var tasks = filePaths.Select(async filePath =>
        {
            string content = await ReadFileAsync(filePath);
            int wordCount = content.Split(new char[] { ' ', '\n', '\r', '\t' }, 
                StringSplitOptions.RemoveEmptyEntries).Length;
            
            return new { FilePath = filePath, WordCount = wordCount };
        });
        
        var results = await Task.WhenAll(tasks);
        
        Console.WriteLine("檔案處理結果：");
        foreach (var result in results)
        {
            Console.WriteLine($"  {result.FilePath}: {result.WordCount} 個字");
        }
    }
}

// 網路請求示範
public class WebService
{
    private static readonly HttpClient httpClient = new HttpClient();
    
    public static async Task<string> GetJsonDataAsync(string apiUrl)
    {
        try
        {
            Console.WriteLine($"呼叫 API：{apiUrl}");
            
            HttpResponseMessage response = await httpClient.GetAsync(apiUrl);
            
            if (response.IsSuccessStatusCode)
            {
                string jsonData = await response.Content.ReadAsStringAsync();
                Console.WriteLine($"API 呼叫成功，回傳 {jsonData.Length} 個字元");
                return jsonData;
            }
            else
            {
                Console.WriteLine($"API 呼叫失敗：{response.StatusCode}");
                return string.Empty;
            }
        }
        catch (HttpRequestException ex)
        {
            Console.WriteLine($"網路請求錯誤：{ex.Message}");
            return string.Empty;
        }
        catch (TaskCanceledException)
        {
            Console.WriteLine("請求逾時");
            return string.Empty;
        }
    }
    
    public static async Task<List<string>> GetMultipleUrlsAsync(string[] urls)
    {
        Console.WriteLine("=== 並行網路請求 ===");
        
        var tasks = urls.Select(url => GetJsonDataAsync(url));
        string[] results = await Task.WhenAll(tasks);
        
        return results.Where(result => !string.IsNullOrEmpty(result)).ToList();
    }
}

// 非同步錯誤處理
public class AsyncErrorHandling
{
    public static async Task<T> ExecuteWithRetryAsync<T>(
        Func<Task<T>> operation, 
        int maxRetries = 3,
        TimeSpan delay = default)
    {
        if (delay == default)
            delay = TimeSpan.FromSeconds(1);
        
        for (int attempt = 1; attempt <= maxRetries; attempt++)
        {
            try
            {
                Console.WriteLine($"嘗試執行 (第 {attempt} 次)...");
                return await operation();
            }
            catch (Exception ex) when (attempt < maxRetries)
            {
                Console.WriteLine($"第 {attempt} 次嘗試失敗：{ex.Message}");
                Console.WriteLine($"等待 {delay.TotalSeconds} 秒後重試...");
                await Task.Delay(delay);
            }
        }
        
        // 最後一次嘗試，讓例外拋出
        Console.WriteLine($"最後嘗試 (第 {maxRetries} 次)...");
        return await operation();
    }
    
    public static async Task DemoRetryLogic()
    {
        Console.WriteLine("=== 重試機制示範 ===");
        
        try
        {
            // 模擬會失敗的操作
            int result = await ExecuteWithRetryAsync(async () =>
            {
                await Task.Delay(500);
                
                // 70% 機率失敗
                if (new Random().NextDouble() < 0.7)
                {
                    throw new InvalidOperationException("模擬的隨機失敗");
                }
                
                return 42;
            }, maxRetries: 5, delay: TimeSpan.FromSeconds(1));
            
            Console.WriteLine($"操作最終成功，結果：{result}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"操作最終失敗：{ex.Message}");
        }
    }
}

// 使用範例
class Program
{
    static async Task Main(string[] args)
    {
        // 基本非同步操作
        await AsyncBasics.RunParallelOperationsAsync();
        await AsyncBasics.RunSequentialOperationsAsync();
        
        // 非同步錯誤處理
        await AsyncErrorHandling.DemoRetryLogic();
        
        // 模擬網路請求
        string[] testUrls = 
        {
            "https://api.github.com/users/octocat",
            "https://jsonplaceholder.typicode.com/posts/1",
            "https://httpbin.org/delay/1"
        };
        
        var results = await WebService.GetMultipleUrlsAsync(testUrls);
        Console.WriteLine($"\n成功取得 {results.Count} 個回應");
    }
}
```

**小練習**：

```csharp
// 練習：建立一個非同步的資料處理管線
public class DataPipeline
{
    public static async Task<string> FetchDataAsync(string source)
    {
        await Task.Delay(1000); // 模擬網路延遲
        return $"從 {source} 取得的原始資料";
    }
    
    public static async Task<string> ProcessDataAsync(string rawData)
    {
        await Task.Delay(800); // 模擬處理時間
        return $"處理後的資料：{rawData.ToUpper()}";
    }
    
    public static async Task<bool> SaveDataAsync(string processedData)
    {
        await Task.Delay(500); // 模擬儲存時間
        Console.WriteLine($"已儲存：{processedData}");
        return true;
    }
    
    public static async Task RunPipelineAsync(string[] sources)
    {
        var tasks = sources.Select(async source =>
        {
            try
            {
                string rawData = await FetchDataAsync(source);
                string processedData = await ProcessDataAsync(rawData);
                bool saved = await SaveDataAsync(processedData);
                return saved;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"處理 {source} 時發生錯誤：{ex.Message}");
                return false;
            }
        });
        
        bool[] results = await Task.WhenAll(tasks);
        int successCount = results.Count(r => r);
        
        Console.WriteLine($"管線處理完成：{successCount}/{sources.Length} 個來源處理成功");
    }
}
```

#### 3.4.2 非同步最佳實務與進階應用

```csharp
public class AsyncBestPractices
{
    // 最佳實務 1：配置 ConfigureAwait(false)
    public static async Task<string> ProcessWithConfigureAwaitAsync(string data)
    {
        // 在不需要回到原始同步化內容時使用 ConfigureAwait(false)
        await Task.Delay(1000).ConfigureAwait(false);
        
        // 處理資料
        return data.ToUpper();
    }
    
    // 最佳實務 2：避免 async void，除了事件處理程序
    public static async Task HandleDataAsync() // 好的做法：使用 async Task
    {
        try
        {
            await ProcessDataAsync();
        }
        catch (Exception ex)
        {
            Console.WriteLine($"錯誤：{ex.Message}");
        }
    }
    
    // 事件處理程序的例外：可以使用 async void
    public static async void Button_Click(object sender, EventArgs e) // 只有事件處理程序可以這樣做
    {
        try
        {
            await HandleDataAsync();
        }
        catch (Exception ex)
        {
            // 記錄錯誤，因為 async void 的例外無法被呼叫者捕獲
            Console.WriteLine($"未處理的錯誤：{ex.Message}");
        }
    }
    
    // 最佳實務 3：使用 CancellationToken 支援取消
    public static async Task<string> DownloadDataAsync(string url, CancellationToken cancellationToken = default)
    {
        using var client = new HttpClient();
        
        try
        {
            // 將 CancellationToken 傳遞給支援的方法
            string result = await client.GetStringAsync(url, cancellationToken);
            
            // 定期檢查取消請求
            cancellationToken.ThrowIfCancellationRequested();
            
            return result;
        }
        catch (OperationCanceledException)
        {
            Console.WriteLine("下載被取消");
            throw; // 重新拋出取消例外
        }
    }
    
    // 最佳實務 4：正確的例外處理
    public static async Task<Result<T>> SafeExecuteAsync<T>(Func<Task<T>> operation)
    {
        try
        {
            T result = await operation();
            return Result<T>.Success(result);
        }
        catch (Exception ex)
        {
            return Result<T>.Failure(ex.Message);
        }
    }
    
    // 結果包裝類別
    public class Result<T>
    {
        public bool IsSuccess { get; private set; }
        public T Value { get; private set; }
        public string Error { get; private set; }
        
        private Result(bool isSuccess, T value, string error)
        {
            IsSuccess = isSuccess;
            Value = value;
            Error = error;
        }
        
        public static Result<T> Success(T value) => new Result<T>(true, value, null);
        public static Result<T> Failure(string error) => new Result<T>(false, default(T), error);
    }
    
    // 最佳實務 5：使用 SemaphoreSlim 控制並發
    private static readonly SemaphoreSlim _semaphore = new SemaphoreSlim(3, 3); // 最多3個並發
    
    public static async Task<string> ProcessWithThrottlingAsync(string data)
    {
        await _semaphore.WaitAsync();
        try
        {
            Console.WriteLine($"處理開始：{data}");
            await Task.Delay(2000); // 模擬處理時間
            Console.WriteLine($"處理完成：{data}");
            return data.ToUpper();
        }
        finally
        {
            _semaphore.Release();
        }
    }
    
    // 最佳實務 6：進度報告
    public static async Task ProcessWithProgressAsync(IProgress<int> progress = null)
    {
        int totalSteps = 10;
        
        for (int i = 0; i <= totalSteps; i++)
        {
            // 執行工作
            await Task.Delay(500);
            
            // 報告進度
            progress?.Report((i * 100) / totalSteps);
        }
    }
    
    // 最佳實務 7：重試機制
    public static async Task<T> RetryAsync<T>(Func<Task<T>> operation, int maxRetries = 3, TimeSpan delay = default)
    {
        if (delay == default)
            delay = TimeSpan.FromSeconds(1);
        
        Exception lastException = null;
        
        for (int attempt = 0; attempt <= maxRetries; attempt++)
        {
            try
            {
                return await operation();
            }
            catch (Exception ex)
            {
                lastException = ex;
                
                if (attempt == maxRetries)
                    break;
                
                Console.WriteLine($"嘗試 {attempt + 1} 失敗，{delay.TotalSeconds} 秒後重試：{ex.Message}");
                await Task.Delay(delay);
                
                // 指數退避
                delay = TimeSpan.FromMilliseconds(delay.TotalMilliseconds * 2);
            }
        }
        
        throw new Exception($"操作在 {maxRetries + 1} 次嘗試後仍然失敗", lastException);
    }
    
    // 最佳實務 8：超時控制
    public static async Task<T> ExecuteWithTimeoutAsync<T>(Func<Task<T>> operation, TimeSpan timeout)
    {
        using var cts = new CancellationTokenSource(timeout);
        
        try
        {
            return await operation();
        }
        catch (OperationCanceledException) when (cts.Token.IsCancellationRequested)
        {
            throw new TimeoutException($"操作在 {timeout.TotalSeconds} 秒內未完成");
        }
    }
    
    // 示範方法
    public static async Task DemonstrateBestPracticesAsync()
    {
        Console.WriteLine("=== 非同步最佳實務示範 ===\n");
        
        // 1. 使用 CancellationToken
        using var cts = new CancellationTokenSource(TimeSpan.FromSeconds(5));
        try
        {
            string data = await DownloadDataAsync("https://example.com", cts.Token);
            Console.WriteLine($"下載完成：{data.Length} 字元");
        }
        catch (OperationCanceledException)
        {
            Console.WriteLine("下載被取消");
        }
        
        // 2. 進度報告
        var progress = new Progress<int>(percentage => 
            Console.WriteLine($"進度：{percentage}%"));
        
        await ProcessWithProgressAsync(progress);
        
        // 3. 並發控制
        var tasks = Enumerable.Range(1, 10)
            .Select(i => ProcessWithThrottlingAsync($"項目-{i}"))
            .ToArray();
        
        await Task.WhenAll(tasks);
        
        // 4. 重試機制
        var result = await RetryAsync(async () =>
        {
            // 模擬可能失敗的操作
            if (Random.Shared.NextDouble() < 0.7) // 70% 機率失敗
                throw new Exception("模擬失敗");
                
            return "成功";
        });
        
        Console.WriteLine($"重試結果：{result}");
        
        // 5. 超時控制
        try
        {
            var timeoutResult = await ExecuteWithTimeoutAsync(async () =>
            {
                await Task.Delay(3000); // 模擬耗時操作
                return "完成";
            }, TimeSpan.FromSeconds(2));
            
            Console.WriteLine($"超時測試結果：{timeoutResult}");
        }
        catch (TimeoutException ex)
        {
            Console.WriteLine($"操作超時：{ex.Message}");
        }
    }
}

// 常見錯誤示範
public class AsyncAntiPatterns
{
    // ❌ 錯誤做法：使用 .Result 或 .Wait()
    public static void BadExample_Blocking()
    {
        // 這會造成死鎖風險
        // string result = GetDataAsync().Result; // 不要這樣做！
        // GetDataAsync().Wait(); // 不要這樣做！
    }
    
    // ❌ 錯誤做法：不必要的 async/await
    public static async Task<string> BadExample_UnnecessaryAsync()
    {
        return await GetDataAsync(); // 不必要的 async/await
    }
    
    // ✅ 正確做法：直接返回 Task
    public static Task<string> GoodExample_DirectReturn()
    {
        return GetDataAsync(); // 直接返回 Task
    }
    
    // ❌ 錯誤做法：忘記 await
    public static async Task BadExample_ForgotAwait()
    {
        GetDataAsync(); // 忘記 await，方法會立即返回
        Console.WriteLine("這會立即執行，而不是等待完成");
    }
    
    // ✅ 正確做法：正確使用 await
    public static async Task GoodExample_ProperAwait()
    {
        string result = await GetDataAsync();
        Console.WriteLine($"等待完成後執行：{result}");
    }
    
    private static async Task<string> GetDataAsync()
    {
        await Task.Delay(1000);
        return "資料";
    }
}
```

**實務開發重點**：

1. **效能考量**：
   - 使用 `ConfigureAwait(false)` 在函式庫程式碼中
   - 避免不必要的 async/await
   - 使用 `Task.WhenAll` 並行執行

2. **錯誤處理**：
   - 使用 try-catch 包裝 async 操作
   - 避免 async void，除了事件處理程序
   - 正確處理 `OperationCanceledException`

3. **資源管理**：
   - 使用 `CancellationToken` 支援取消
   - 用 `SemaphoreSlim` 控制並發數量
   - 實作超時機制

4. **使用者體驗**：
   - 提供進度報告
   - 實作重試機制
   - 適當的錯誤訊息

**認證考點提示**：

- 理解泛型的用途和約束語法
- 掌握委派、事件的宣告和使用
- 熟悉 LINQ 的查詢語法和方法語法
- 了解 async/await 的工作原理和最佳實務
- 學會使用 Task.WhenAll 和 Task.WhenAny
- 理解並行與並發的差異
- 掌握 CancellationToken 的正確使用

**注意事項**：

1. 泛型約束要合理，避免過度限制
2. 事件應該使用 event 關鍵字，提供封裝
3. LINQ 查詢要注意效能，避免多次列舉
4. async 方法應該以 Async 結尾
5. 不要在非同步方法中使用 .Result 或 .Wait()
6. 正確處理非同步方法中的例外
7. 在函式庫程式碼中使用 ConfigureAwait(false)
8. 使用 CancellationToken 支援操作取消

---

## 4. 專案實務應用

### 4.1 Web API 開發 (ASP.NET Core)

#### 4.1.1 建立基本 Web API

```csharp
// Models/Product.cs
public class Product
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Description { get; set; }
    public decimal Price { get; set; }
    public int Stock { get; set; }
    public string Category { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime UpdatedAt { get; set; }
    
    public Product()
    {
        CreatedAt = DateTime.UtcNow;
        UpdatedAt = DateTime.UtcNow;
    }
}

// DTOs/ProductDto.cs
public class CreateProductDto
{
    public string Name { get; set; }
    public string Description { get; set; }
    public decimal Price { get; set; }
    public int Stock { get; set; }
    public string Category { get; set; }
}

public class UpdateProductDto
{
    public string Name { get; set; }
    public string Description { get; set; }
    public decimal Price { get; set; }
    public int Stock { get; set; }
    public string Category { get; set; }
}

public class ProductResponseDto
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Description { get; set; }
    public decimal Price { get; set; }
    public int Stock { get; set; }
    public string Category { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime UpdatedAt { get; set; }
}

// Services/IProductService.cs
public interface IProductService
{
    Task<IEnumerable<ProductResponseDto>> GetAllProductsAsync();
    Task<ProductResponseDto> GetProductByIdAsync(int id);
    Task<ProductResponseDto> CreateProductAsync(CreateProductDto createDto);
    Task<ProductResponseDto> UpdateProductAsync(int id, UpdateProductDto updateDto);
    Task<bool> DeleteProductAsync(int id);
    Task<IEnumerable<ProductResponseDto>> GetProductsByCategoryAsync(string category);
}

// Services/ProductService.cs
public class ProductService : IProductService
{
    private readonly List<Product> _products;
    private int _nextId;

    public ProductService()
    {
        _products = new List<Product>
        {
            new Product { Id = 1, Name = "筆記型電腦", Description = "高效能筆電", Price = 35000, Stock = 10, Category = "電腦" },
            new Product { Id = 2, Name = "智慧手機", Description = "最新款手機", Price = 25000, Stock = 15, Category = "手機" },
            new Product { Id = 3, Name = "平板電腦", Description = "輕薄平板", Price = 18000, Stock = 8, Category = "電腦" }
        };
        _nextId = 4;
    }

    public async Task<IEnumerable<ProductResponseDto>> GetAllProductsAsync()
    {
        await Task.Delay(100); // 模擬非同步操作
        
        return _products.Select(p => new ProductResponseDto
        {
            Id = p.Id,
            Name = p.Name,
            Description = p.Description,
            Price = p.Price,
            Stock = p.Stock,
            Category = p.Category,
            CreatedAt = p.CreatedAt,
            UpdatedAt = p.UpdatedAt
        });
    }

    public async Task<ProductResponseDto> GetProductByIdAsync(int id)
    {
        await Task.Delay(50);
        
        var product = _products.FirstOrDefault(p => p.Id == id);
        if (product == null)
            return null;

        return new ProductResponseDto
        {
            Id = product.Id,
            Name = product.Name,
            Description = product.Description,
            Price = product.Price,
            Stock = product.Stock,
            Category = product.Category,
            CreatedAt = product.CreatedAt,
            UpdatedAt = product.UpdatedAt
        };
    }

    public async Task<ProductResponseDto> CreateProductAsync(CreateProductDto createDto)
    {
        await Task.Delay(100);
        
        var product = new Product
        {
            Id = _nextId++,
            Name = createDto.Name,
            Description = createDto.Description,
            Price = createDto.Price,
            Stock = createDto.Stock,
            Category = createDto.Category
        };

        _products.Add(product);

        return new ProductResponseDto
        {
            Id = product.Id,
            Name = product.Name,
            Description = product.Description,
            Price = product.Price,
            Stock = product.Stock,
            Category = product.Category,
            CreatedAt = product.CreatedAt,
            UpdatedAt = product.UpdatedAt
        };
    }

    public async Task<ProductResponseDto> UpdateProductAsync(int id, UpdateProductDto updateDto)
    {
        await Task.Delay(100);
        
        var product = _products.FirstOrDefault(p => p.Id == id);
        if (product == null)
            return null;

        product.Name = updateDto.Name ?? product.Name;
        product.Description = updateDto.Description ?? product.Description;
        product.Price = updateDto.Price;
        product.Stock = updateDto.Stock;
        product.Category = updateDto.Category ?? product.Category;
        product.UpdatedAt = DateTime.UtcNow;

        return new ProductResponseDto
        {
            Id = product.Id,
            Name = product.Name,
            Description = product.Description,
            Price = product.Price,
            Stock = product.Stock,
            Category = product.Category,
            CreatedAt = product.CreatedAt,
            UpdatedAt = product.UpdatedAt
        };
    }

    public async Task<bool> DeleteProductAsync(int id)
    {
        await Task.Delay(50);
        
        var product = _products.FirstOrDefault(p => p.Id == id);
        if (product == null)
            return false;

        _products.Remove(product);
        return true;
    }

    public async Task<IEnumerable<ProductResponseDto>> GetProductsByCategoryAsync(string category)
    {
        await Task.Delay(100);
        
        var products = _products.Where(p => p.Category.Equals(category, StringComparison.OrdinalIgnoreCase));
        
        return products.Select(p => new ProductResponseDto
        {
            Id = p.Id,
            Name = p.Name,
            Description = p.Description,
            Price = p.Price,
            Stock = p.Stock,
            Category = p.Category,
            CreatedAt = p.CreatedAt,
            UpdatedAt = p.UpdatedAt
        });
    }
}

// Controllers/ProductsController.cs
[ApiController]
[Route("api/[controller]")]
public class ProductsController : ControllerBase
{
    private readonly IProductService _productService;
    private readonly ILogger<ProductsController> _logger;

    public ProductsController(IProductService productService, ILogger<ProductsController> logger)
    {
        _productService = productService;
        _logger = logger;
    }

    // GET api/products
    [HttpGet]
    public async Task<ActionResult<IEnumerable<ProductResponseDto>>> GetProducts([FromQuery] string category = null)
    {
        try
        {
            _logger.LogInformation("取得產品清單，類別篩選：{Category}", category ?? "全部");

            IEnumerable<ProductResponseDto> products;
            
            if (string.IsNullOrEmpty(category))
            {
                products = await _productService.GetAllProductsAsync();
            }
            else
            {
                products = await _productService.GetProductsByCategoryAsync(category);
            }

            return Ok(products);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "取得產品清單時發生錯誤");
            return StatusCode(500, "內部伺服器錯誤");
        }
    }

    // GET api/products/5
    [HttpGet("{id}")]
    public async Task<ActionResult<ProductResponseDto>> GetProduct(int id)
    {
        try
        {
            _logger.LogInformation("取得產品詳細資訊，ID：{ProductId}", id);

            var product = await _productService.GetProductByIdAsync(id);
            
            if (product == null)
            {
                _logger.LogWarning("找不到產品，ID：{ProductId}", id);
                return NotFound($"找不到 ID 為 {id} 的產品");
            }

            return Ok(product);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "取得產品詳細資訊時發生錯誤，ID：{ProductId}", id);
            return StatusCode(500, "內部伺服器錯誤");
        }
    }

    // POST api/products
    [HttpPost]
    public async Task<ActionResult<ProductResponseDto>> CreateProduct([FromBody] CreateProductDto createDto)
    {
        try
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }

            _logger.LogInformation("建立新產品：{ProductName}", createDto.Name);

            var product = await _productService.CreateProductAsync(createDto);
            
            return CreatedAtAction(nameof(GetProduct), new { id = product.Id }, product);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "建立產品時發生錯誤：{ProductName}", createDto.Name);
            return StatusCode(500, "內部伺服器錯誤");
        }
    }

    // PUT api/products/5
    [HttpPut("{id}")]
    public async Task<ActionResult<ProductResponseDto>> UpdateProduct(int id, [FromBody] UpdateProductDto updateDto)
    {
        try
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }

            _logger.LogInformation("更新產品，ID：{ProductId}", id);

            var product = await _productService.UpdateProductAsync(id, updateDto);
            
            if (product == null)
            {
                return NotFound($"找不到 ID 為 {id} 的產品");
            }

            return Ok(product);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "更新產品時發生錯誤，ID：{ProductId}", id);
            return StatusCode(500, "內部伺服器錯誤");
        }
    }

    // DELETE api/products/5
    [HttpDelete("{id}")]
    public async Task<ActionResult> DeleteProduct(int id)
    {
        try
        {
            _logger.LogInformation("刪除產品，ID：{ProductId}", id);

            var success = await _productService.DeleteProductAsync(id);
            
            if (!success)
            {
                return NotFound($"找不到 ID 為 {id} 的產品");
            }

            return NoContent();
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "刪除產品時發生錯誤，ID：{ProductId}", id);
            return StatusCode(500, "內部伺服器錯誤");
        }
    }
}

// Program.cs (ASP.NET Core 6+)
var builder = WebApplication.CreateBuilder(args);

// 註冊服務
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddScoped<IProductService, ProductService>();

// 設定 CORS
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAll", policy =>
    {
        policy.AllowAnyOrigin()
              .AllowAnyMethod()
              .AllowAnyHeader();
    });
});

var app = builder.Build();

// 設定 HTTP 管線
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();
app.UseCors("AllowAll");
app.UseAuthorization();
app.MapControllers();

app.Run();
```

### 4.2 資料庫存取 (Entity Framework Core)

#### 4.2.1 Entity Framework 設定

```csharp
// Models/DatabaseModels.cs
public class ApplicationDbContext : DbContext
{
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options)
    {
    }

    public DbSet<Product> Products { get; set; }
    public DbSet<Category> Categories { get; set; }
    public DbSet<Order> Orders { get; set; }
    public DbSet<OrderItem> OrderItems { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);

        // Product 設定
        modelBuilder.Entity<Product>(entity =>
        {
            entity.HasKey(e => e.Id);
            entity.Property(e => e.Name).HasMaxLength(100).IsRequired();
            entity.Property(e => e.Description).HasMaxLength(500);
            entity.Property(e => e.Price).HasColumnType("decimal(18,2)");
            entity.HasOne(e => e.Category)
                  .WithMany(c => c.Products)
                  .HasForeignKey(e => e.CategoryId);
        });

        // Category 設定
        modelBuilder.Entity<Category>(entity =>
        {
            entity.HasKey(e => e.Id);
            entity.Property(e => e.Name).HasMaxLength(50).IsRequired();
            entity.HasIndex(e => e.Name).IsUnique();
        });

        // Order 設定
        modelBuilder.Entity<Order>(entity =>
        {
            entity.HasKey(e => e.Id);
            entity.Property(e => e.CustomerName).HasMaxLength(100).IsRequired();
            entity.Property(e => e.TotalAmount).HasColumnType("decimal(18,2)");
        });

        // OrderItem 設定
        modelBuilder.Entity<OrderItem>(entity =>
        {
            entity.HasKey(e => e.Id);
            entity.Property(e => e.UnitPrice).HasColumnType("decimal(18,2)");
            entity.HasOne(e => e.Order)
                  .WithMany(o => o.OrderItems)
                  .HasForeignKey(e => e.OrderId);
            entity.HasOne(e => e.Product)
                  .WithMany()
                  .HasForeignKey(e => e.ProductId);
        });

        // 種子資料
        modelBuilder.Entity<Category>().HasData(
            new Category { Id = 1, Name = "電腦" },
            new Category { Id = 2, Name = "手機" },
            new Category { Id = 3, Name = "配件" }
        );

        modelBuilder.Entity<Product>().HasData(
            new Product { Id = 1, Name = "筆記型電腦", Description = "高效能筆電", Price = 35000, Stock = 10, CategoryId = 1, CreatedAt = DateTime.UtcNow, UpdatedAt = DateTime.UtcNow },
            new Product { Id = 2, Name = "智慧手機", Description = "最新款手機", Price = 25000, Stock = 15, CategoryId = 2, CreatedAt = DateTime.UtcNow, UpdatedAt = DateTime.UtcNow },
            new Product { Id = 3, Name = "無線滑鼠", Description = "藍牙滑鼠", Price = 800, Stock = 25, CategoryId = 3, CreatedAt = DateTime.UtcNow, UpdatedAt = DateTime.UtcNow }
        );
    }
}

// 更新的 Product 模型
public class Product
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Description { get; set; }
    public decimal Price { get; set; }
    public int Stock { get; set; }
    public int CategoryId { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime UpdatedAt { get; set; }

    // 導覽屬性
    public Category Category { get; set; }
}

public class Category
{
    public int Id { get; set; }
    public string Name { get; set; }

    // 導覽屬性
    public ICollection<Product> Products { get; set; } = new List<Product>();
}

public class Order
{
    public int Id { get; set; }
    public string CustomerName { get; set; }
    public string CustomerEmail { get; set; }
    public DateTime OrderDate { get; set; }
    public decimal TotalAmount { get; set; }
    public OrderStatus Status { get; set; }

    // 導覽屬性
    public ICollection<OrderItem> OrderItems { get; set; } = new List<OrderItem>();
}

public class OrderItem
{
    public int Id { get; set; }
    public int OrderId { get; set; }
    public int ProductId { get; set; }
    public int Quantity { get; set; }
    public decimal UnitPrice { get; set; }

    // 導覽屬性
    public Order Order { get; set; }
    public Product Product { get; set; }
}

public enum OrderStatus
{
    Pending,
    Processing,
    Shipped,
    Delivered,
    Cancelled
}

// Repository 模式實作
public interface IProductRepository
{
    Task<IEnumerable<Product>> GetAllAsync();
    Task<Product> GetByIdAsync(int id);
    Task<IEnumerable<Product>> GetByCategoryAsync(int categoryId);
    Task<Product> CreateAsync(Product product);
    Task<Product> UpdateAsync(Product product);
    Task<bool> DeleteAsync(int id);
    Task<bool> ExistsAsync(int id);
}

public class ProductRepository : IProductRepository
{
    private readonly ApplicationDbContext _context;
    private readonly ILogger<ProductRepository> _logger;

    public ProductRepository(ApplicationDbContext context, ILogger<ProductRepository> logger)
    {
        _context = context;
        _logger = logger;
    }

    public async Task<IEnumerable<Product>> GetAllAsync()
    {
        try
        {
            return await _context.Products
                .Include(p => p.Category)
                .OrderBy(p => p.Name)
                .ToListAsync();
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "取得所有產品時發生錯誤");
            throw;
        }
    }

    public async Task<Product> GetByIdAsync(int id)
    {
        try
        {
            return await _context.Products
                .Include(p => p.Category)
                .FirstOrDefaultAsync(p => p.Id == id);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "取得產品時發生錯誤，ID：{ProductId}", id);
            throw;
        }
    }

    public async Task<IEnumerable<Product>> GetByCategoryAsync(int categoryId)
    {
        try
        {
            return await _context.Products
                .Include(p => p.Category)
                .Where(p => p.CategoryId == categoryId)
                .OrderBy(p => p.Name)
                .ToListAsync();
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "依類別取得產品時發生錯誤，CategoryId：{CategoryId}", categoryId);
            throw;
        }
    }

    public async Task<Product> CreateAsync(Product product)
    {
        try
        {
            product.CreatedAt = DateTime.UtcNow;
            product.UpdatedAt = DateTime.UtcNow;

            _context.Products.Add(product);
            await _context.SaveChangesAsync();

            return await GetByIdAsync(product.Id);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "建立產品時發生錯誤：{ProductName}", product.Name);
            throw;
        }
    }

    public async Task<Product> UpdateAsync(Product product)
    {
        try
        {
            var existingProduct = await _context.Products.FindAsync(product.Id);
            if (existingProduct == null)
                return null;

            existingProduct.Name = product.Name;
            existingProduct.Description = product.Description;
            existingProduct.Price = product.Price;
            existingProduct.Stock = product.Stock;
            existingProduct.CategoryId = product.CategoryId;
            existingProduct.UpdatedAt = DateTime.UtcNow;

            await _context.SaveChangesAsync();

            return await GetByIdAsync(product.Id);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "更新產品時發生錯誤，ID：{ProductId}", product.Id);
            throw;
        }
    }

    public async Task<bool> DeleteAsync(int id)
    {
        try
        {
            var product = await _context.Products.FindAsync(id);
            if (product == null)
                return false;

            _context.Products.Remove(product);
            await _context.SaveChangesAsync();

            return true;
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "刪除產品時發生錯誤，ID：{ProductId}", id);
            throw;
        }
    }

    public async Task<bool> ExistsAsync(int id)
    {
        try
        {
            return await _context.Products.AnyAsync(p => p.Id == id);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "檢查產品存在時發生錯誤，ID：{ProductId}", id);
            throw;
        }
    }
}

// 訂單服務
public interface IOrderService
{
    Task<Order> CreateOrderAsync(CreateOrderDto orderDto);
    Task<Order> GetOrderByIdAsync(int orderId);
    Task<IEnumerable<Order>> GetOrdersByCustomerAsync(string customerEmail);
    Task<bool> UpdateOrderStatusAsync(int orderId, OrderStatus status);
}

public class CreateOrderDto
{
    public string CustomerName { get; set; }
    public string CustomerEmail { get; set; }
    public List<OrderItemDto> Items { get; set; } = new List<OrderItemDto>();
}

public class OrderItemDto
{
    public int ProductId { get; set; }
    public int Quantity { get; set; }
}

public class OrderService : IOrderService
{
    private readonly ApplicationDbContext _context;
    private readonly IProductRepository _productRepository;
    private readonly ILogger<OrderService> _logger;

    public OrderService(
        ApplicationDbContext context, 
        IProductRepository productRepository, 
        ILogger<OrderService> logger)
    {
        _context = context;
        _productRepository = productRepository;
        _logger = logger;
    }

    public async Task<Order> CreateOrderAsync(CreateOrderDto orderDto)
    {
        using var transaction = await _context.Database.BeginTransactionAsync();
        
        try
        {
            // 建立訂單
            var order = new Order
            {
                CustomerName = orderDto.CustomerName,
                CustomerEmail = orderDto.CustomerEmail,
                OrderDate = DateTime.UtcNow,
                Status = OrderStatus.Pending
            };

            _context.Orders.Add(order);
            await _context.SaveChangesAsync();

            decimal totalAmount = 0;

            // 建立訂單項目
            foreach (var itemDto in orderDto.Items)
            {
                var product = await _productRepository.GetByIdAsync(itemDto.ProductId);
                if (product == null)
                {
                    throw new ArgumentException($"找不到產品 ID：{itemDto.ProductId}");
                }

                if (product.Stock < itemDto.Quantity)
                {
                    throw new InvalidOperationException($"產品 {product.Name} 庫存不足");
                }

                var orderItem = new OrderItem
                {
                    OrderId = order.Id,
                    ProductId = itemDto.ProductId,
                    Quantity = itemDto.Quantity,
                    UnitPrice = product.Price
                };

                _context.OrderItems.Add(orderItem);

                // 更新庫存
                product.Stock -= itemDto.Quantity;
                _context.Products.Update(product);

                totalAmount += orderItem.UnitPrice * orderItem.Quantity;
            }

            // 更新訂單總金額
            order.TotalAmount = totalAmount;
            _context.Orders.Update(order);

            await _context.SaveChangesAsync();
            await transaction.CommitAsync();

            _logger.LogInformation("成功建立訂單，ID：{OrderId}，總金額：{TotalAmount}", order.Id, totalAmount);

            return await GetOrderByIdAsync(order.Id);
        }
        catch (Exception ex)
        {
            await transaction.RollbackAsync();
            _logger.LogError(ex, "建立訂單時發生錯誤");
            throw;
        }
    }

    public async Task<Order> GetOrderByIdAsync(int orderId)
    {
        return await _context.Orders
            .Include(o => o.OrderItems)
            .ThenInclude(oi => oi.Product)
            .FirstOrDefaultAsync(o => o.Id == orderId);
    }

    public async Task<IEnumerable<Order>> GetOrdersByCustomerAsync(string customerEmail)
    {
        return await _context.Orders
            .Include(o => o.OrderItems)
            .ThenInclude(oi => oi.Product)
            .Where(o => o.CustomerEmail == customerEmail)
            .OrderByDescending(o => o.OrderDate)
            .ToListAsync();
    }

    public async Task<bool> UpdateOrderStatusAsync(int orderId, OrderStatus status)
    {
        try
        {
            var order = await _context.Orders.FindAsync(orderId);
            if (order == null)
                return false;

            order.Status = status;
            await _context.SaveChangesAsync();

            _logger.LogInformation("訂單狀態已更新，ID：{OrderId}，新狀態：{Status}", orderId, status);
            return true;
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "更新訂單狀態時發生錯誤，ID：{OrderId}", orderId);
            throw;
        }
    }
}
```

### 4.3 單元測試 (xUnit)

#### 4.3.1 基本單元測試

```csharp
// Tests/ProductServiceTests.cs
using Xunit;
using Moq;
using Microsoft.Extensions.Logging;

public class ProductServiceTests
{
    private readonly Mock<IProductRepository> _mockRepository;
    private readonly Mock<ILogger<ProductService>> _mockLogger;
    private readonly ProductService _productService;

    public ProductServiceTests()
    {
        _mockRepository = new Mock<IProductRepository>();
        _mockLogger = new Mock<ILogger<ProductService>>();
        _productService = new ProductService(_mockRepository.Object, _mockLogger.Object);
    }

    [Fact]
    public async Task GetAllProductsAsync_ShouldReturnAllProducts()
    {
        // Arrange
        var expectedProducts = new List<Product>
        {
            new Product { Id = 1, Name = "Product 1", Price = 100, Stock = 10 },
            new Product { Id = 2, Name = "Product 2", Price = 200, Stock = 5 }
        };

        _mockRepository.Setup(r => r.GetAllAsync())
                      .ReturnsAsync(expectedProducts);

        // Act
        var result = await _productService.GetAllProductsAsync();

        // Assert
        Assert.NotNull(result);
        Assert.Equal(2, result.Count());
        Assert.Equal("Product 1", result.First().Name);
    }

    [Fact]
    public async Task GetProductByIdAsync_WithValidId_ShouldReturnProduct()
    {
        // Arrange
        var expectedProduct = new Product 
        { 
            Id = 1, 
            Name = "Test Product", 
            Price = 100, 
            Stock = 10 
        };

        _mockRepository.Setup(r => r.GetByIdAsync(1))
                      .ReturnsAsync(expectedProduct);

        // Act
        var result = await _productService.GetProductByIdAsync(1);

        // Assert
        Assert.NotNull(result);
        Assert.Equal(1, result.Id);
        Assert.Equal("Test Product", result.Name);
    }

    [Fact]
    public async Task GetProductByIdAsync_WithInvalidId_ShouldReturnNull()
    {
        // Arrange
        _mockRepository.Setup(r => r.GetByIdAsync(999))
                      .ReturnsAsync((Product)null);

        // Act
        var result = await _productService.GetProductByIdAsync(999);

        // Assert
        Assert.Null(result);
    }

    [Fact]
    public async Task CreateProductAsync_WithValidData_ShouldCreateProduct()
    {
        // Arrange
        var createDto = new CreateProductDto
        {
            Name = "New Product",
            Description = "Test Description",
            Price = 150,
            Stock = 20,
            CategoryId = 1
        };

        var expectedProduct = new Product
        {
            Id = 1,
            Name = createDto.Name,
            Description = createDto.Description,
            Price = createDto.Price,
            Stock = createDto.Stock,
            CategoryId = createDto.CategoryId
        };

        _mockRepository.Setup(r => r.CreateAsync(It.IsAny<Product>()))
                      .ReturnsAsync(expectedProduct);

        // Act
        var result = await _productService.CreateProductAsync(createDto);

        // Assert
        Assert.NotNull(result);
        Assert.Equal(createDto.Name, result.Name);
        Assert.Equal(createDto.Price, result.Price);
        
        _mockRepository.Verify(r => r.CreateAsync(It.IsAny<Product>()), Times.Once);
    }

    [Theory]
    [InlineData(0)]
    [InlineData(-1)]
    [InlineData(-100)]
    public async Task CreateProductAsync_WithInvalidPrice_ShouldThrowException(decimal invalidPrice)
    {
        // Arrange
        var createDto = new CreateProductDto
        {
            Name = "Test Product",
            Price = invalidPrice,
            Stock = 10,
            CategoryId = 1
        };

        // Act & Assert
        await Assert.ThrowsAsync<ArgumentException>(() => 
            _productService.CreateProductAsync(createDto));
    }

    [Fact]
    public async Task DeleteProductAsync_WithExistingProduct_ShouldReturnTrue()
    {
        // Arrange
        _mockRepository.Setup(r => r.DeleteAsync(1))
                      .ReturnsAsync(true);

        // Act
        var result = await _productService.DeleteProductAsync(1);

        // Assert
        Assert.True(result);
        _mockRepository.Verify(r => r.DeleteAsync(1), Times.Once);
    }

    [Fact]
    public async Task DeleteProductAsync_WithNonExistingProduct_ShouldReturnFalse()
    {
        // Arrange
        _mockRepository.Setup(r => r.DeleteAsync(999))
                      .ReturnsAsync(false);

        // Act
        var result = await _productService.DeleteProductAsync(999);

        // Assert
        Assert.False(result);
    }
}

// Tests/ProductsControllerTests.cs
public class ProductsControllerTests
{
    private readonly Mock<IProductService> _mockService;
    private readonly Mock<ILogger<ProductsController>> _mockLogger;
    private readonly ProductsController _controller;

    public ProductsControllerTests()
    {
        _mockService = new Mock<IProductService>();
        _mockLogger = new Mock<ILogger<ProductsController>>();
        _controller = new ProductsController(_mockService.Object, _mockLogger.Object);
    }

    [Fact]
    public async Task GetProducts_ShouldReturnOkResult()
    {
        // Arrange
        var expectedProducts = new List<ProductResponseDto>
        {
            new ProductResponseDto { Id = 1, Name = "Product 1" },
            new ProductResponseDto { Id = 2, Name = "Product 2" }
        };

        _mockService.Setup(s => s.GetAllProductsAsync())
                   .ReturnsAsync(expectedProducts);

        // Act
        var result = await _controller.GetProducts();

        // Assert
        var okResult = Assert.IsType<OkObjectResult>(result.Result);
        var products = Assert.IsAssignableFrom<IEnumerable<ProductResponseDto>>(okResult.Value);
        Assert.Equal(2, products.Count());
    }

    [Fact]
    public async Task GetProduct_WithValidId_ShouldReturnOkResult()
    {
        // Arrange
        var expectedProduct = new ProductResponseDto 
        { 
            Id = 1, 
            Name = "Test Product" 
        };

        _mockService.Setup(s => s.GetProductByIdAsync(1))
                   .ReturnsAsync(expectedProduct);

        // Act
        var result = await _controller.GetProduct(1);

        // Assert
        var okResult = Assert.IsType<OkObjectResult>(result.Result);
        var product = Assert.IsType<ProductResponseDto>(okResult.Value);
        Assert.Equal(1, product.Id);
    }

    [Fact]
    public async Task GetProduct_WithInvalidId_ShouldReturnNotFound()
    {
        // Arrange
        _mockService.Setup(s => s.GetProductByIdAsync(999))
                   .ReturnsAsync((ProductResponseDto)null);

        // Act
        var result = await _controller.GetProduct(999);

        // Assert
        Assert.IsType<NotFoundObjectResult>(result.Result);
    }

    [Fact]
    public async Task CreateProduct_WithValidData_ShouldReturnCreatedResult()
    {
        // Arrange
        var createDto = new CreateProductDto
        {
            Name = "New Product",
            Price = 100,
            Stock = 10
        };

        var expectedProduct = new ProductResponseDto
        {
            Id = 1,
            Name = createDto.Name,
            Price = createDto.Price,
            Stock = createDto.Stock
        };

        _mockService.Setup(s => s.CreateProductAsync(createDto))
                   .ReturnsAsync(expectedProduct);

        // Act
        var result = await _controller.CreateProduct(createDto);

        // Assert
        var createdResult = Assert.IsType<CreatedAtActionResult>(result.Result);
        var product = Assert.IsType<ProductResponseDto>(createdResult.Value);
        Assert.Equal(createDto.Name, product.Name);
    }
}

// Tests/IntegrationTests/ProductsIntegrationTests.cs
public class ProductsIntegrationTests : IClassFixture<WebApplicationFactory<Program>>
{
    private readonly WebApplicationFactory<Program> _factory;
    private readonly HttpClient _client;

    public ProductsIntegrationTests(WebApplicationFactory<Program> factory)
    {
        _factory = factory;
        _client = _factory.CreateClient();
    }

    [Fact]
    public async Task GetProducts_ShouldReturnSuccessStatusCode()
    {
        // Act
        var response = await _client.GetAsync("/api/products");

        // Assert
        response.EnsureSuccessStatusCode();
        
        var content = await response.Content.ReadAsStringAsync();
        Assert.NotEmpty(content);
    }

    [Fact]
    public async Task CreateProduct_ShouldReturnCreatedStatusCode()
    {
        // Arrange
        var createDto = new CreateProductDto
        {
            Name = "Integration Test Product",
            Description = "Created by integration test",
            Price = 99.99m,
            Stock = 5,
            CategoryId = 1
        };

        var json = JsonSerializer.Serialize(createDto);
        var content = new StringContent(json, Encoding.UTF8, "application/json");

        // Act
        var response = await _client.PostAsync("/api/products", content);

        // Assert
        Assert.Equal(HttpStatusCode.Created, response.StatusCode);
        
        var responseContent = await response.Content.ReadAsStringAsync();
        var product = JsonSerializer.Deserialize<ProductResponseDto>(responseContent, 
            new JsonSerializerOptions { PropertyNameCaseInsensitive = true });
        
        Assert.Equal(createDto.Name, product.Name);
        Assert.Equal(createDto.Price, product.Price);
    }
}

// Tests/Utilities/TestDataBuilder.cs
public class TestDataBuilder
{
    public static Product CreateProduct(
        int id = 1,
        string name = "Test Product",
        decimal price = 100,
        int stock = 10,
        int categoryId = 1)
    {
        return new Product
        {
            Id = id,
            Name = name,
            Description = $"Description for {name}",
            Price = price,
            Stock = stock,
            CategoryId = categoryId,
            CreatedAt = DateTime.UtcNow,
            UpdatedAt = DateTime.UtcNow
        };
    }

    public static CreateProductDto CreateProductDto(
        string name = "Test Product",
        decimal price = 100,
        int stock = 10,
        int categoryId = 1)
    {
        return new CreateProductDto
        {
            Name = name,
            Description = $"Description for {name}",
            Price = price,
            Stock = stock,
            CategoryId = categoryId
        };
    }

    public static List<Product> CreateProductList(int count = 3)
    {
        var products = new List<Product>();
        
        for (int i = 1; i <= count; i++)
        {
            products.Add(CreateProduct(
                id: i,
                name: $"Product {i}",
                price: 100 * i,
                stock: 10 + i
            ));
        }
        
        return products;
    }
}
```

### 4.4 錯誤處理與日誌紀錄

#### 4.4.1 全域錯誤處理

```csharp
// Middleware/ErrorHandlingMiddleware.cs
public class ErrorHandlingMiddleware
{
    private readonly RequestDelegate _next;
    private readonly ILogger<ErrorHandlingMiddleware> _logger;

    public ErrorHandlingMiddleware(RequestDelegate next, ILogger<ErrorHandlingMiddleware> logger)
    {
        _next = next;
        _logger = logger;
    }

    public async Task InvokeAsync(HttpContext context)
    {
        try
        {
            await _next(context);
        }
        catch (Exception ex)
        {
            await HandleExceptionAsync(context, ex);
        }
    }

    private async Task HandleExceptionAsync(HttpContext context, Exception exception)
    {
        _logger.LogError(exception, "發生未處理的例外：{ExceptionMessage}", exception.Message);

        var response = context.Response;
        response.ContentType = "application/json";

        var errorResponse = new ErrorResponse();

        switch (exception)
        {
            case ArgumentException argEx:
                response.StatusCode = (int)HttpStatusCode.BadRequest;
                errorResponse.Message = argEx.Message;
                errorResponse.Details = "請求參數不正確";
                break;

            case KeyNotFoundException notFoundEx:
                response.StatusCode = (int)HttpStatusCode.NotFound;
                errorResponse.Message = "找不到指定的資源";
                errorResponse.Details = notFoundEx.Message;
                break;

            case UnauthorizedAccessException:
                response.StatusCode = (int)HttpStatusCode.Unauthorized;
                errorResponse.Message = "未授權的存取";
                break;

            case InvalidOperationException invalidOpEx:
                response.StatusCode = (int)HttpStatusCode.BadRequest;
                errorResponse.Message = invalidOpEx.Message;
                errorResponse.Details = "操作無效";
                break;

            default:
                response.StatusCode = (int)HttpStatusCode.InternalServerError;
                errorResponse.Message = "內部伺服器錯誤";
                errorResponse.Details = "請聯絡系統管理員";
                break;
        }

        errorResponse.StatusCode = response.StatusCode;
        errorResponse.Timestamp = DateTime.UtcNow;
        errorResponse.Path = context.Request.Path;

        var jsonResponse = JsonSerializer.Serialize(errorResponse);
        await response.WriteAsync(jsonResponse);
    }
}

public class ErrorResponse
{
    public int StatusCode { get; set; }
    public string Message { get; set; }
    public string Details { get; set; }
    public DateTime Timestamp { get; set; }
    public string Path { get; set; }
}

// Logging/LoggingExtensions.cs
public static class LoggingExtensions
{
    public static void LogProductCreated(this ILogger logger, int productId, string productName)
    {
        logger.LogInformation("產品已建立 - ID: {ProductId}, 名稱: {ProductName}", productId, productName);
    }

    public static void LogProductUpdated(this ILogger logger, int productId, string productName)
    {
        logger.LogInformation("產品已更新 - ID: {ProductId}, 名稱: {ProductName}", productId, productName);
    }

    public static void LogProductDeleted(this ILogger logger, int productId)
    {
        logger.LogWarning("產品已刪除 - ID: {ProductId}", productId);
    }

    public static void LogOrderCreated(this ILogger logger, int orderId, decimal totalAmount, string customerEmail)
    {
        logger.LogInformation("訂單已建立 - ID: {OrderId}, 總金額: {TotalAmount:C}, 客戶: {CustomerEmail}", 
            orderId, totalAmount, customerEmail);
    }

    public static void LogInventoryWarning(this ILogger logger, int productId, string productName, int currentStock)
    {
        logger.LogWarning("庫存不足警告 - 產品: {ProductName} (ID: {ProductId}), 目前庫存: {CurrentStock}", 
            productName, productId, currentStock);
    }

    public static void LogUnexpectedError(this ILogger logger, Exception exception, string operation)
    {
        logger.LogError(exception, "執行 {Operation} 時發生未預期錯誤", operation);
    }
}

// Configuration/Logging/appsettings.json
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning",
      "Microsoft.EntityFrameworkCore.Database.Command": "Warning"
    },
    "Console": {
      "LogLevel": {
        "Default": "Information"
      }
    },
    "File": {
      "LogLevel": {
        "Default": "Information"
      },
      "Path": "logs/app-.log",
      "RollingInterval": "Day",
      "RetainedFileCountLimit": 7
    }
  },
  "ConnectionStrings": {
    "DefaultConnection": "Server=localhost;Database=ProductCatalog;Trusted_Connection=true;TrustServerCertificate=true;"
  },
  "AllowedHosts": "*"
}
```

**小練習**：

```csharp
// 練習：建立一個完整的 RESTful API
// 1. 建立 Category 的 CRUD 操作
// 2. 加入資料驗證
// 3. 撰寫對應的單元測試

[ApiController]
[Route("api/[controller]")]
public class CategoriesController : ControllerBase
{
    private readonly ICategoryService _categoryService;
    private readonly ILogger<CategoriesController> _logger;

    public CategoriesController(ICategoryService categoryService, ILogger<CategoriesController> logger)
    {
        _categoryService = categoryService;
        _logger = logger;
    }

    [HttpGet]
    public async Task<ActionResult<IEnumerable<CategoryResponseDto>>> GetCategories()
    {
        // 實作取得所有類別
        // TODO: 學員練習實作
    }

    [HttpPost]
    public async Task<ActionResult<CategoryResponseDto>> CreateCategory([FromBody] CreateCategoryDto createDto)
    {
        // 實作建立類別
        // TODO: 學員練習實作
        // 記得加入資料驗證
    }

    // 其他 CRUD 操作...
}

// 資料驗證 DTO
public class CreateCategoryDto
{
    [Required(ErrorMessage = "類別名稱為必填")]
    [StringLength(50, ErrorMessage = "類別名稱不能超過 50 個字元")]
    public string Name { get; set; }

    [StringLength(200, ErrorMessage = "描述不能超過 200 個字元")]
    public string Description { get; set; }
}
```

**認證考點提示**：

- 了解 ASP.NET Core Web API 的建立流程
- 掌握 Entity Framework Core 的設定和使用
- 熟悉 Repository 模式和依賴注入
- 理解單元測試和整合測試的差異
- 學會使用 Mock 物件進行測試
- 掌握例外處理和日誌記錄的最佳實務

**注意事項**：

1. API 應該遵循 RESTful 設計原則
2. 使用 DTO 來分離資料傳輸和領域模型
3. 實作適當的錯誤處理和日誌記錄
4. 單元測試應該覆蓋主要業務邏輯
5. 使用交易確保資料一致性
6. 適當使用快取提升效能

---

## 5. 認證考試對應

### 5.1 Microsoft C# 認證考試概述

#### 5.1.1 考試架構

**主要認證路徑**：
- **Microsoft Certified: Azure Developer Associate (AZ-204)**
- **Microsoft Certified: Azure Solutions Architect Expert (AZ-305)**
- **Microsoft Certified: DevOps Engineer Expert (AZ-400)**

**核心技能範圍**：
1. C# 程式語言基礎 (20-25%)
2. 物件導向程式設計 (25-30%)
3. .NET Framework/.NET Core 應用 (20-25%)
4. 資料存取和處理 (15-20%)
5. 除錯和測試 (10-15%)

#### 5.1.2 考試準備策略

```csharp
// 考試常見題型範例

// 1. 語法理解題
public class ExamExample1
{
    public static void Main()
    {
        int[] numbers = { 1, 2, 3, 4, 5 };
        
        // 問題：下列程式碼的輸出是什麼？
        for (int i = 0; i < numbers.Length; i++)
        {
            if (numbers[i] % 2 == 0)
                continue;
            Console.WriteLine(numbers[i]);
        }
        // 答案：1, 3, 5
    }
}

// 2. 物件導向概念題
public abstract class Vehicle
{
    protected string brand;
    
    public Vehicle(string brand)
    {
        this.brand = brand;
    }
    
    public abstract void Start();
    
    public virtual void Stop()
    {
        Console.WriteLine($"{brand} 車輛停止");
    }
}

public class Car : Vehicle
{
    public Car(string brand) : base(brand) { }
    
    public override void Start()
    {
        Console.WriteLine($"{brand} 汽車啟動");
    }
    
    public override void Stop()
    {
        Console.WriteLine($"{brand} 汽車煞車停止");
    }
}

// 問題：polymorphism 的應用
public class PolymorphismExample
{
    public static void TestVehicles()
    {
        Vehicle[] vehicles = 
        {
            new Car("Toyota"),
            new Car("BMW")
        };
        
        foreach (Vehicle vehicle in vehicles)
        {
            vehicle.Start(); // 呼叫 Car 的 Start 方法
            vehicle.Stop();  // 呼叫 Car 的 Stop 方法
        }
    }
}

// 3. 例外處理題
public class ExceptionExample
{
    public static int ParseAndDivide(string numerator, string denominator)
    {
        try
        {
            int num = int.Parse(numerator);
            int den = int.Parse(denominator);
            return num / den;
        }
        catch (FormatException)
        {
            Console.WriteLine("格式錯誤");
            return -1;
        }
        catch (DivideByZeroException)
        {
            Console.WriteLine("除以零錯誤");
            return -1;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"其他錯誤：{ex.Message}");
            return -1;
        }
        finally
        {
            Console.WriteLine("清理資源");
        }
    }
}

// 4. LINQ 查詢題
public class LinqExample
{
    public static void QueryExamples()
    {
        var students = new[]
        {
            new { Name = "Alice", Age = 20, Grade = 85 },
            new { Name = "Bob", Age = 22, Grade = 92 },
            new { Name = "Charlie", Age = 19, Grade = 78 },
            new { Name = "David", Age = 21, Grade = 88 }
        };
        
        // 問題：找出年齡大於 20 且成績大於 85 的學生姓名
        var result = students
            .Where(s => s.Age > 20 && s.Grade > 85)
            .Select(s => s.Name)
            .ToList();
        
        // 答案：Bob, David
    }
}
```

### 5.2 考試重點整理

#### 5.2.1 語言基礎考點

**1. 資料型別和變數**
```csharp
// 重要考點：型別轉換
public class TypeConversion
{
    public static void Examples()
    {
        // 隱式轉換
        int intValue = 10;
        long longValue = intValue; // OK
        
        // 明式轉換
        double doubleValue = 10.5;
        int intValue2 = (int)doubleValue; // 需要明式轉換
        
        // 安全轉換
        string strValue = "123";
        if (int.TryParse(strValue, out int result))
        {
            Console.WriteLine($"轉換成功：{result}");
        }
        
        // 考點：nullable 型別
        int? nullableInt = null;
        int safeValue = nullableInt ?? 0; // null coalescing operator
        
        // 考點：var 關鍵字
        var autoType = "這是字串"; // 編譯器推斷為 string
        // var invalidVar; // 編譯錯誤：無法推斷型別
    }
}
```

**2. 運算子和表達式**
```csharp
public class OperatorExamples
{
    public static void Examples()
    {
        // 考點：運算子優先順序
        int result1 = 5 + 3 * 2; // 結果：11 (先乘除後加減)
        int result2 = (5 + 3) * 2; // 結果：16
        
        // 考點：邏輯運算子短路評估
        bool condition1 = false;
        bool condition2 = true;
        
        if (condition1 && CheckSomething()) // CheckSomething() 不會被呼叫
        {
            Console.WriteLine("不會執行");
        }
        
        // 考點：三元運算子
        string message = result1 > 10 ? "大於10" : "小於等於10";
        
        // 考點：null coalescing operators
        string nullString = null;
        string result = nullString ?? "預設值";
        string result2 = nullString ?.ToUpper() ?? "NULL";
    }
    
    private static bool CheckSomething()
    {
        Console.WriteLine("這不會被呼叫");
        return true;
    }
}
```

#### 5.2.2 物件導向考點

**1. 繼承和多型**
```csharp
// 重要考點：方法覆寫和隱藏
public class BaseClass
{
    public virtual void VirtualMethod()
    {
        Console.WriteLine("Base Virtual Method");
    }
    
    public void NonVirtualMethod()
    {
        Console.WriteLine("Base Non-Virtual Method");
    }
}

public class DerivedClass : BaseClass
{
    // 覆寫虛擬方法
    public override void VirtualMethod()
    {
        Console.WriteLine("Derived Override Method");
    }
    
    // 隱藏非虛擬方法
    public new void NonVirtualMethod()
    {
        Console.WriteLine("Derived New Method");
    }
}

public class InheritanceTest
{
    public static void TestPolymorphism()
    {
        BaseClass obj = new DerivedClass();
        
        obj.VirtualMethod();     // 輸出：Derived Override Method (多型)
        obj.NonVirtualMethod();  // 輸出：Base Non-Virtual Method (非多型)
        
        DerivedClass derived = (DerivedClass)obj;
        derived.NonVirtualMethod(); // 輸出：Derived New Method
    }
}
```

**2. 介面和抽象類別**
```csharp
// 考點：介面 vs 抽象類別的選擇
public interface IFlyable
{
    void Fly();
    
    // C# 8.0+ 預設實作
    void Land()
    {
        Console.WriteLine("預設降落實作");
    }
}

public abstract class Animal
{
    protected string name;
    
    public Animal(string name)
    {
        this.name = name;
    }
    
    // 抽象方法
    public abstract void MakeSound();
    
    // 具體方法
    public void Sleep()
    {
        Console.WriteLine($"{name} 正在睡覺");
    }
}

public class Bird : Animal, IFlyable
{
    public Bird(string name) : base(name) { }
    
    public override void MakeSound()
    {
        Console.WriteLine($"{name} 在鳴叫");
    }
    
    public void Fly()
    {
        Console.WriteLine($"{name} 正在飛行");
    }
}
```

#### 5.2.3 進階考點

**1. 泛型約束**
```csharp
// 考點：泛型約束的正確使用
public class GenericConstraintExamples
{
    // where T : class - 參考型別約束
    public static T CreateInstance<T>() where T : class, new()
    {
        return new T();
    }
    
    // where T : struct - 值型別約束
    public static bool IsDefault<T>(T value) where T : struct
    {
        return value.Equals(default(T));
    }
    
    // where T : IComparable<T> - 介面約束
    public static T Max<T>(T a, T b) where T : IComparable<T>
    {
        return a.CompareTo(b) > 0 ? a : b;
    }
    
    // 多重約束
    public static void ProcessEntity<T>(T entity) 
        where T : class, IDisposable, new()
    {
        using (T instance = new T())
        {
            // 處理邏輯
        }
    }
}
```

**2. 委派和事件**
```csharp
// 考點：委派和事件的差異
public class EventExample
{
    // 委派可以直接賦值和呼叫
    public Action<string> SimpleDelegate;
    
    // 事件只能透過 += 和 -= 操作
    public event Action<string> MessageEvent;
    
    private Action<string> messageHandler;
    
    // 正確的事件實作
    public event Action<string> SecureMessageEvent
    {
        add { messageHandler += value; }
        remove { messageHandler -= value; }
    }
    
    public void TriggerEvents(string message)
    {
        // 直接呼叫委派
        SimpleDelegate?.Invoke(message);
        
        // 觸發事件
        MessageEvent?.Invoke(message);
        messageHandler?.Invoke(message);
    }
}

// 考點：內建委派型別
public class BuiltInDelegateExamples
{
    public static void Examples()
    {
        // Action：無回傳值
        Action<string> printAction = message => Console.WriteLine(message);
        
        // Func：有回傳值
        Func<int, int, int> addFunc = (a, b) => a + b;
        
        // Predicate：回傳 bool
        Predicate<int> isEven = number => number % 2 == 0;
        
        // 使用範例
        printAction("Hello World");
        int sum = addFunc(5, 3);
        bool result = isEven(4);
    }
}
```

### 5.3 模擬考題

#### 5.3.1 選擇題範例

**問題 1：下列程式碼的輸出是什麼？**
```csharp
class Program
{
    static void Main()
    {
        int x = 5;
        int y = ++x + x++;
        Console.WriteLine($"x = {x}, y = {y}");
    }
}
```
A) x = 6, y = 11  
B) x = 7, y = 11  
C) x = 7, y = 12  
D) x = 6, y = 12  

**答案：C) x = 7, y = 12**  
**解析：++x 先遞增再使用 (6)，x++ 先使用再遞增，所以 y = 6 + 6 = 12，最後 x = 7**

**問題 2：關於介面和抽象類別，下列敘述何者正確？**
A) 介面可以包含建構子  
B) 抽象類別不能有具體方法  
C) 一個類別只能實作一個介面  
D) 抽象類別可以包含欄位，介面不能  

**答案：D) 抽象類別可以包含欄位，介面不能**

**問題 3：下列 LINQ 查詢的結果是什麼？**
```csharp
var numbers = new[] { 1, 2, 3, 4, 5, 6 };
var result = numbers.Where(n => n % 2 == 0).Select(n => n * 2).Sum();
```
A) 12  
B) 24  
C) 18  
D) 36  

**答案：B) 24**  
**解析：偶數 {2, 4, 6} → 乘以2 {4, 8, 12} → 總和 = 24**

#### 5.3.2 程式題範例

**問題 4：實作一個泛型方法，能夠找出陣列中的最大值**
```csharp
// 您的實作：
public static T FindMax<T>(T[] array) where T : IComparable<T>
{
    if (array == null || array.Length == 0)
        throw new ArgumentException("陣列不能為空");
    
    T max = array[0];
    for (int i = 1; i < array.Length; i++)
    {
        if (array[i].CompareTo(max) > 0)
            max = array[i];
    }
    return max;
}

// 測試程式碼
public static void TestFindMax()
{
    int[] numbers = { 3, 7, 2, 9, 1 };
    string[] words = { "apple", "zebra", "banana" };
    
    Console.WriteLine(FindMax(numbers)); // 輸出：9
    Console.WriteLine(FindMax(words));   // 輸出：zebra
}
```

**問題 5：建立一個事件處理系統**
```csharp
// 您的實作：
public class TemperatureMonitor
{
    private double temperature;
    
    public event Action<double> TemperatureChanged;
    public event Action<double> HighTemperatureAlert;
    
    public double Temperature
    {
        get { return temperature; }
        set
        {
            temperature = value;
            OnTemperatureChanged(value);
            
            if (value > 35.0)
            {
                OnHighTemperatureAlert(value);
            }
        }
    }
    
    protected virtual void OnTemperatureChanged(double temp)
    {
        TemperatureChanged?.Invoke(temp);
    }
    
    protected virtual void OnHighTemperatureAlert(double temp)
    {
        HighTemperatureAlert?.Invoke(temp);
    }
}

// 使用範例
public static void TestTemperatureMonitor()
{
    var monitor = new TemperatureMonitor();
    
    monitor.TemperatureChanged += temp => 
        Console.WriteLine($"溫度變化：{temp}°C");
    
    monitor.HighTemperatureAlert += temp => 
        Console.WriteLine($"高溫警報：{temp}°C");
    
    monitor.Temperature = 25.0; // 溫度變化：25°C
    monitor.Temperature = 37.0; // 溫度變化：37°C, 高溫警報：37°C
}
```

### 5.4 考試策略與技巧

#### 5.4.1 時間管理

1. **快速瀏覽**：先快速瀏覽所有題目，標記難題
2. **先易後難**：先做有把握的題目
3. **時間分配**：選擇題 1-2 分鐘，程式題 5-10 分鐘
4. **預留檢查**：保留 10-15 分鐘檢查答案

#### 5.4.2 答題技巧

```csharp
// 技巧 1：注意關鍵字的差異
public class KeywordDifferences
{
    // virtual vs override vs new
    public virtual void Method1() { } // 可被覆寫
    public override void Method2() { } // 覆寫基類方法
    public new void Method3() { } // 隱藏基類方法
    
    // ref vs out vs in
    public void RefExample(ref int value) { } // 必須初始化，可讀可寫
    public void OutExample(out int value) { value = 0; } // 不需初始化，必須賦值
    public void InExample(in int value) { } // 只讀參考
}

// 技巧 2：理解執行順序
public class ExecutionOrder
{
    static ExecutionOrder()
    {
        Console.WriteLine("1. 靜態建構子");
    }
    
    public ExecutionOrder()
    {
        Console.WriteLine("3. 執行個體建構子");
    }
    
    private string field = InitializeField();
    
    private static string InitializeField()
    {
        Console.WriteLine("2. 欄位初始化");
        return "initialized";
    }
}
```

---

## 6. 附錄

### 6.1 常見問題 FAQ

#### Q1: C# 和 Java 有什麼主要差異？
**A:** 
- **語法差異**：C# 有屬性 (Properties)，Java 使用 getter/setter 方法
- **記憶體管理**：C# 有垃圾回收和析構子，Java 只有垃圾回收
- **平台支援**：C# 原生 Windows 但現在支援跨平台，Java 原生跨平台
- **泛型實作**：C# 使用真泛型，Java 使用類型擦除

#### Q2: 什麼時候使用抽象類別，什麼時候使用介面？
**A:**
- **抽象類別**：有共同實作代碼、需要建構子、單一繼承關係
- **介面**：純粹的合約定義、支援多重實作、相關性較低的類別

#### Q3: async/await 和 Task 有什麼關係？
**A:**
- **Task**：代表一個非同步操作
- **async**：標記方法為非同步方法
- **await**：等待 Task 完成，不阻塞線程

#### Q4: 什麼是 IDisposable，何時需要實作？
**A:**
```csharp
public class ResourceManager : IDisposable
{
    private bool disposed = false;
    
    public void Dispose()
    {
        Dispose(true);
        GC.SuppressFinalize(this);
    }
    
    protected virtual void Dispose(bool disposing)
    {
        if (!disposed)
        {
            if (disposing)
            {
                // 釋放託管資源
            }
            // 釋放非託管資源
            disposed = true;
        }
    }
}
```

### 6.2 學習資源

#### 6.2.1 官方文件
- [Microsoft C# 文件](https://docs.microsoft.com/zh-tw/dotnet/csharp/)
- [.NET API 文件](https://docs.microsoft.com/zh-tw/dotnet/api/)
- [ASP.NET Core 文件](https://docs.microsoft.com/zh-tw/aspnet/core/)

#### 6.2.2 練習網站
- [LeetCode](https://leetcode.com/) - 演算法練習
- [HackerRank](https://www.hackerrank.com/) - 程式設計挑戰
- [Codewars](https://www.codewars.com/) - 程式技能訓練
- [Microsoft Learn](https://docs.microsoft.com/zh-tw/learn/) - 免費線上課程

#### 6.2.3 推薦書籍
1. **C# 10 in a Nutshell** - Joseph Albahari
2. **Clean Code** - Robert C. Martin
3. **Effective C#** - Bill Wagner
4. **Pro C# 10 with .NET 6** - Andrew Troelsen

#### 6.2.4 開發工具
- **Visual Studio Community** (免費)
- **Visual Studio Code** (輕量級，免費)
- **JetBrains Rider** (付費，功能強大)
- **LINQPad** (LINQ 查詢測試工具)

### 6.3 建議學習路徑

#### 6.3.1 初級階段 (1-2 個月)
1. **環境設定和基本語法**
   - 安裝開發環境
   - 變數、資料型別、流程控制
   - 方法和例外處理

2. **物件導向基礎**
   - 類別和物件
   - 繼承和多型
   - 介面和抽象類別

**實作專案**：建立一個簡單的主控台應用程式 (計算機、學生管理系統)

#### 6.3.2 中級階段 (2-3 個月)
1. **進階語法**
   - 泛型和委派
   - LINQ 查詢
   - 非同步程式設計

2. **實務應用**
   - 檔案 I/O 操作
   - 基本 Web API 開發
   - 單元測試

**實作專案**：建立一個 RESTful Web API (產品管理系統)

#### 6.3.3 高級階段 (3-4 個月)
1. **企業級應用**
   - Entity Framework Core
   - 設計模式應用
   - 微服務架構

2. **認證準備**
   - 模擬考試練習
   - 深入理解核心概念
   - 實際專案經驗

**實作專案**：完整的企業級應用 (電商系統、CRM 系統)

### 6.4 檢查清單 (Checklist)

#### 6.4.1 基礎知識檢查
- [ ] 了解 C# 基本語法和資料型別
- [ ] 掌握流程控制語句的使用
- [ ] 理解方法的定義和呼叫
- [ ] 熟悉例外處理機制
- [ ] 能夠使用基本的類別和物件

#### 6.4.2 物件導向檢查
- [ ] 理解封裝、繼承、多型的概念
- [ ] 能夠設計和實作類別階層
- [ ] 掌握介面和抽象類別的使用時機
- [ ] 了解存取修飾詞的作用
- [ ] 能夠實作設計模式

#### 6.4.3 進階技術檢查
- [ ] 熟悉泛型的概念和約束
- [ ] 掌握委派和事件的使用
- [ ] 能夠撰寫 LINQ 查詢
- [ ] 理解非同步程式設計
- [ ] 具備錯誤處理和除錯能力

#### 6.4.4 實務開發檢查
- [ ] 能夠建立 Web API 專案
- [ ] 掌握資料庫存取技術
- [ ] 撰寫有效的單元測試
- [ ] 實作適當的日誌記錄
- [ ] 遵循程式碼品質標準

#### 6.4.5 認證準備檢查
- [ ] 完成所有章節的學習
- [ ] 實作至少 2-3 個完整專案
- [ ] 通過模擬考試 (80% 以上)
- [ ] 熟悉考試題型和時間管理
- [ ] 具備實際工作經驗或實習經驗

### 6.5 總結

這份 C# 程式語言教學手冊涵蓋了從基礎入門到進階應用的完整學習路徑。透過系統性的學習和大量的實作練習，新進開發同仁能夠：

1. **建立紮實的基礎**：掌握 C# 語言的核心概念和語法
2. **培養程式思維**：理解物件導向程式設計的精髓
3. **獲得實務經驗**：透過專案實作學習最佳實務
4. **準備認證考試**：具備通過 Microsoft C# 認證的能力
5. **持續成長**：建立終身學習的基礎

**成功的關鍵在於**：
- 持續的練習和實作
- 從錯誤中學習
- 與同事交流和討論
- 關注最新技術趨勢
- 參與開源專案貢獻

祝您在 C# 程式設計的學習旅程中順利成功！

---

**文件版本**：v1.0  
**最後更新**：2025年8月31日  
**適用對象**：新進開發同仁  
**維護者**：技術培訓團隊

---
