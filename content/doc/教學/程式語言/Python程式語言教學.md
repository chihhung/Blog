+++
date = '2025-10-31T00:00:00+08:00'
draft = false
title = 'Python程式語言教學'
tags = ['教學', '程式語言']
categories = ['教學']
+++

<!-- markdownlint-disable MD013 MD024 MD025 MD033 MD036 MD041 -->
<!--
  本檔案的 markdownlint 例外說明（刻意保留、非疏漏）：
  - MD013 line-length：技術白皮書含長表格、長 URL 與長引用，不強制折行。
  - MD024 no-duplicate-heading：各章固定樣板小節必然重複，且刻意不進目錄，包含
    「🎯 學習目標」「💡 實務案例」「⚠️ 注意事項」「📝 小測驗」「🏷️ 認證考試對應」。
    這些重複錨點為設計結果，不應以改寫標題的方式消除。
  - MD025 single-title：檔首為 Hugo TOML front matter，H1 僅一個（手冊標題）。
  - MD033 inline-html：以一對 HTML 註解標記界定自動產生的目錄區塊，供 check-toc.ps1 驗證。
  - MD036 no-emphasis-as-heading：步驟／Case 等流程標籤刻意不進目錄，故以粗體呈現。
  - MD041 first-line-heading：檔首為 Hugo TOML front matter。

  另注意：本檔 5.x 節的 Markdown 範例使用「四個反引號」巢狀圍籬（````markdown），
  這是 CommonMark 的合法巢狀寫法，請勿改為三個反引號，否則渲染會壞掉。
  倉庫的 check-md.ps1 會因此誤報「程式碼區塊未關閉（檔尾）」，該筆為已知誤報。
-->

# Python 程式語言教學手冊

> - **版本**：2.0
> - **最後更新**：2026 年 9 月（內容查核基準日 2026-09-21）
> - **適用於**：Python 3.13 / 3.14（現行穩定版）～ 3.15（2026-10-01 發布）
> - **適用對象**：初學者至企業級開發人員、PCEP／PCAP 認證考生
> - **目標**：語言基礎 ＋ 企業工程實務（工具鏈、非同步、安全供應鏈）＋ 認證準備

---

<!-- TOC-AUTO-BEGIN -->

## 目錄

1. [Python 基礎入門](#1-python-基礎入門)
   - 1.1 [Python 安裝與環境設置](#11-python-安裝與環境設置)
     - 1.1.1 [Python 簡介](#111-python-簡介)
     - 1.1.2 [Windows 系統安裝](#112-windows-系統安裝)
     - 1.1.3 [Linux 系統安裝](#113-linux-系統安裝)
     - 1.1.4 [開發環境設置](#114-開發環境設置)
     - 1.1.5 [虛擬環境管理](#115-虛擬環境管理)
   - 1.2 [語法基礎](#12-語法基礎)
     - 1.2.1 [Python 語法規則](#121-python-語法規則)
     - 1.2.2 [變數與命名規則](#122-變數與命名規則)
     - 1.2.3 [資料型態](#123-資料型態)
     - 1.2.4 [運算子](#124-運算子)（含海象運算子 `:=`）
     - 1.2.5 [型別提示 (Type Hints)](#125-型別提示-type-hints)
   - 1.3 [流程控制](#13-流程控制)
     - 1.3.1 [條件判斷 (if 語句)](#131-條件判斷-if-語句)
     - 1.3.1.1 [結構化模式匹配 (match/case)](#1311-結構化模式匹配-matchcase-python-310)
     - 1.3.2 [迴圈結構](#132-迴圈結構)
     - 1.3.3 [例外處理](#133-例外處理)（含例外群組 `except*`）
     - 1.3.4 [進階流程控制](#134-進階流程控制)
   - 1.4 [函式、模組與套件管理](#14-函式模組與套件管理)
     - 1.4.1 [函式基礎](#141-函式基礎)
     - 1.4.2 [模組系統](#142-模組系統)
     - 1.4.3 [套件管理](#143-套件管理)（含 uv、PEP 735、PEP 751 與套件發布）

2. [進階應用](#2-進階應用)
   - 2.1 [面向物件程式設計](#21-面向物件程式設計)
     - 2.1.1 [類別與物件基礎](#211-類別與物件基礎)
     - 2.1.2 [封裝與屬性](#212-封裝與屬性)
     - 2.1.3 [繼承](#213-繼承)
     - 2.1.4 [多型](#214-多型)
     - 2.1.5 [特殊方法 (Magic Methods)](#215-特殊方法-magic-methods)
     - 2.1.6 [資料類別 (dataclasses)](#216-資料類別-dataclasses-python-37)
   - 2.2 [檔案處理與例外處理](#22-檔案處理與例外處理)
     - 2.2.1 [檔案基本操作](#221-檔案基本操作)
     - 2.2.2 [進階檔案處理](#222-進階檔案處理)
     - 2.2.3 [例外處理機制](#223-例外處理機制)
     - 2.2.4 [上下文管理器](#224-上下文管理器)
   - 2.3 [常用標準函式庫](#23-常用標準函式庫)
     - 2.3.1 [日期時間處理](#231-日期時間處理)
     - 2.3.2 [正規表達式](#232-正規表達式)
     - 2.3.3 [系統操作](#233-系統操作)
     - 2.3.4 [網路程式設計基礎](#234-網路程式設計基礎)
     - 2.3.5 [其他重要模組](#235-其他重要模組)
   - 2.4 [測試與除錯](#24-測試與除錯)
     - 2.4.1 [單元測試基礎](#241-單元測試基礎)
     - 2.4.2 [進階測試技術](#242-進階測試技術)
     - 2.4.3 [pytest 框架](#243-pytest-框架)
     - 2.4.4 [除錯技巧](#244-除錯技巧)
     - 2.4.5 [測試驅動開發 (TDD)](#245-測試驅動開發-tdd)
   - 2.5 [Python 現代特性（3.11 ~ 3.15）](#25-python-現代特性311--315)
     - 2.5.1 [Python 3.11 新特性](#251-python-311-新特性)
     - 2.5.2 [Python 3.12 新特性](#252-python-312-新特性)
     - 2.5.3 [Python 3.13 新特性](#253-python-313-新特性)
     - 2.5.4 [Python 3.14 新特性](#254-python-314-新特性2025-年-10-月發布)
     - 2.5.5 [Python 3.15 新特性](#255-python-315-新特性2026-年-10-月發布)
     - 2.5.6 [版本生命週期與遷移策略](#256-版本生命週期與遷移策略)
   - 2.6 [非同步與併發程式設計](#26-非同步與併發程式設計)
     - 2.6.1 [併發模型選型](#261-併發模型選型)
     - 2.6.2 [asyncio 基礎](#262-asyncio-基礎)
     - 2.6.3 [結構化併發](#263-結構化併發)
     - 2.6.4 [同步原語與佇列](#264-同步原語與佇列)
     - 2.6.5 [free-threaded 與子直譯器實戰](#265-free-threaded-與子直譯器實戰)
     - 2.6.6 [除錯、觀測與常見反模式](#266-除錯觀測與常見反模式)

3. [專案實務應用](#3-專案實務應用)
   - 3.1 [程式碼風格與規範](#31-程式碼風格與規範)
     - 3.1.1 [PEP 8 風格指南](#311-pep-8-風格指南)
     - 3.1.2 [文件字串與註解](#312-文件字串與註解)
     - 3.1.3 [程式碼檢查工具](#313-程式碼檢查工具)
     - 3.1.4 [程式碼品質實務](#314-程式碼品質實務)
   - 3.2 [專案開發實務](#32-專案開發實務)
     - 3.2.1 [專案結構設計](#321-專案結構設計)
     - 3.2.2 [版本控制最佳實務](#322-版本控制最佳實務)
     - 3.2.3 [持續整合與部署](#323-持續整合與部署)
     - 3.2.4 [專案文件撰寫](#324-專案文件撰寫)
   - 3.3 [團隊協作工具](#33-團隊協作工具)
     - 3.3.1 [程式碼審查 (Code Review)](#331-程式碼審查-code-review)
     - 3.3.2 [專案管理工具](#332-專案管理工具)
     - 3.3.3 [溝通協作工具](#333-溝通協作工具)
     - 3.3.4 [自動化工具](#334-自動化工具)
   - 3.4 [安全性與供應鏈管理](#34-安全性與供應鏈管理)
     - 3.4.1 [相依套件弱點掃描](#341-相依套件弱點掃描)
     - 3.4.2 [靜態安全分析](#342-靜態安全分析)
     - 3.4.3 [密鑰與設定管理](#343-密鑰與設定管理)
     - 3.4.4 [供應鏈完整性](#344-供應鏈完整性)
     - 3.4.5 [常見 Python 安全陷阱](#345-常見-python-安全陷阱)

4. [Python 認證考試指引](#4-python-認證考試指引)
   - 4.1 [PCEP 認證指引](#41-pcep-認證指引)
     - 4.1.1 [考試範圍與重點](#411-考試範圍與重點)
     - 4.1.2 [PCEP 考試技巧](#412-pcep-考試技巧)
   - 4.2 [PCAP 認證指引](#42-pcap-認證指引)
     - 4.2.1 [考試範圍重點](#421-考試範圍重點)
   - 4.3 [考試準備與技巧](#43-考試準備與技巧)
     - 4.3.1 [學習路線規劃](#431-學習路線規劃)
     - 4.3.2 [練習資源](#432-練習資源)
     - 4.3.3 [考試當天技巧](#433-考試當天技巧)
     - 4.3.4 [完整認證階梯](#434-完整認證階梯)

5. [檢查清單](#5-檢查清單)
   - 5.1 [環境設置檢查清單](#51-環境設置檢查清單)
   - 5.2 [程式碼品質檢查清單](#52-程式碼品質檢查清單)
   - 5.3 [專案結構檢查清單](#53-專案結構檢查清單)
   - 5.4 [測試檢查清單](#54-測試檢查清單)
   - 5.5 [部署準備檢查清單](#55-部署準備檢查清單)
   - 5.6 [認證考試檢查清單](#56-認證考試檢查清單)
   - 5.7 [持續學習檢查清單](#57-持續學習檢查清單)
   - 5.8 [安全與供應鏈檢查清單](#58-安全與供應鏈檢查清單)

[結語](#結語)
<!-- TOC-AUTO-END -->

---

## 1. Python 基礎入門

### 1.1 Python 安裝與環境設置

#### 🎯 學習目標

- 了解 Python 的特性與應用領域
- 在 Windows 和 Linux 系統上安裝 Python
- 設定開發環境與工具
- 建立虛擬環境管理專案依賴

#### 1.1.1 Python 簡介

Python 是一種高階、直譯式的程式語言，具有以下特點：

- **簡潔易讀**：語法簡單，接近自然語言
- **跨平台**：可在 Windows、Linux、macOS 上執行
- **豐富生態系統**：擁有大量第三方函式庫
- **多用途**：適用於網頁開發、資料科學、AI、自動化等

##### 版本生命週期與選版依據

Python 採 **PEP 602** 的年度發布節奏：每年 10 月發布一個新的功能版本，之後約 2 年的 bugfix 階段、再 3 年的 security-only 階段，合計 5 年支援期。企業選版務必以官方生命週期為準，不要只看「最新版」。

| 版本 | 首次發布 | 目前狀態 | 終止支援 |
| --- | --- | --- | --- |
| 3.15 | 2026-10-01 | Prerelease（RC 階段） | 2031-10 |
| 3.14 | 2025-10-07 | Bugfix | 2030-10 |
| 3.13 | 2024-10-07 | Bugfix | 2029-10 |
| 3.12 | 2023-10-02 | Security-only | 2028-10 |
| 3.11 | 2022-10-24 | Security-only | 2027-10 |
| 3.10 | 2021-10-04 | Security-only | 2026-10 |
| 3.9 | 2020-10-05 | End-of-life | 已於 2025-10-31 終止 |

> 資料來源：[Status of Python versions — Python Developer's Guide](https://devguide.python.org/versions/)（查核日期：2026-09-21）

**選版建議（2026 年基準）：**

- **新專案**：Python 3.14（處於 bugfix 階段、生態系相容性已成熟）
- **既有生產系統**：3.13 或 3.14；仍停留在 3.12 以下者應排定升級，因 3.12 已無 bug 修補、僅收安全性修補
- **需立即汰換**：3.9 已 EOL、3.10 將於 2026-10 EOL，這兩者已不應出現在生產環境
- **評估中**：3.15（2026-10-01 發布）帶來 UTF-8 預設編碼等行為變更，建議先在 CI 加入 3.15 矩陣測試，確認相容後再導入

#### 1.1.2 Windows 系統安裝

##### 步驟 1：下載 Python

1. 前往 [Python 官網](https://www.python.org/downloads/)
2. 下載穩定版本（建議 Python 3.13 以上；新專案建議 3.14）
3. 選擇 Windows x86-64 executable installer
4. 若需 free-threaded 版本（無 GIL），在安裝程式的 **Customize installation → Advanced Options** 勾選 *Download free-threaded binaries*，安裝後以 `python3.14t` 啟動

##### 步驟 2：安裝 Python

```bash
# 安裝選項建議：
☑ Add Python to PATH
☑ Install for all users
☑ Create shortcuts for installed applications
☑ Add Python to environment variables
```

##### 步驟 3：驗證安裝

```powershell
# 在 PowerShell 中執行
python --version
pip --version
```

#### 1.1.3 Linux 系統安裝

##### Ubuntu/Debian 系統：

```bash
# 更新套件清單
sudo apt update

# 安裝 Python 3 和 pip
sudo apt install python3 python3-pip python3-venv

# 驗證安裝
python3 --version
pip3 --version
```

##### CentOS/RHEL 系統：

```bash
# 安裝 Python 3
sudo yum install python3 python3-pip

# 或使用 dnf (較新版本)
sudo dnf install python3 python3-pip

# 驗證安裝
python3 --version
pip3 --version
```

#### 1.1.4 開發環境設置

##### 推薦的開發工具：

1. **Visual Studio Code**（免費，目前市占最高）

   推薦擴充套件：

   - **Python**（Microsoft）—— 基礎支援
   - **Pylance** —— 型別檢查與 IntelliSense（底層為 pyright）
   - **Ruff**（Astral）—— 檢查與格式化，取代舊的 flake8／black／isort 擴充套件
   - **Python Debugger**（debugpy）—— 除錯器

2. **PyCharm**
   - 功能完整的 Python IDE，內建除錯器、測試執行器與重構工具
   - 2025 年起 Community 與 Professional 合併為單一發行版，基礎功能免費

3. **命令列工具鏈（建議一併安裝）**

   ```bash
   # uv：環境、套件與 Python 版本的一站式管理工具（Astral）
   # Windows (PowerShell)
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

   # Linux / macOS
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # 用 uv 直接安裝與切換 Python 版本，不必另外裝 pyenv
   uv python install 3.14
   uv python list
   ```

#### 1.1.5 虛擬環境管理

虛擬環境讓每個專案擁有獨立的套件目錄，避免不同專案的依賴互相污染。以下先介紹標準函式庫的 `venv`（PCEP／PCAP 考試範圍），再介紹 uv 的現代做法。

##### 建立虛擬環境：

```bash
# Windows
python -m venv myproject_env

# Linux/macOS
python3 -m venv myproject_env
```

##### 啟動虛擬環境：

```bash
# Windows
myproject_env\Scripts\activate

# Linux/macOS
source myproject_env/bin/activate
```

##### 停用虛擬環境：

```bash
deactivate
```

##### 管理套件：

```bash
# 安裝套件
pip install package_name

# 安裝特定版本
pip install package_name==1.2.3

# 列出已安裝套件
pip list

# 匯出依賴清單
pip freeze > requirements.txt

# 從檔案安裝依賴
pip install -r requirements.txt
```

##### 現代做法：使用 uv 管理環境

`uv` 把「建立虛擬環境、安裝依賴、鎖定版本、執行程式」整合為單一工具，且因以 Rust 實作，解析與安裝速度通常比 pip 快一個數量級。自 2025 年起已成為 Python 專案的主流選擇。

```bash
# 在現有目錄初始化專案（產生 pyproject.toml）
uv init myproject
cd myproject

# 新增依賴：自動建立 .venv、寫入 pyproject.toml 並更新 uv.lock
uv add requests
uv add --dev pytest ruff        # 開發依賴寫入 [dependency-groups]

# 依 lock 檔還原完全一致的環境（CI 用這個）
uv sync

# 不必手動 activate，直接在專案環境中執行
uv run python main.py
uv run pytest

# 指定專案使用的 Python 版本
uv python pin 3.14
```

> `venv` + `pip` 仍是認證考試的標準答案，且在無法安裝額外工具的受限環境中必備；uv 則是日常開發與 CI 的推薦做法。詳細的依賴宣告與鎖檔格式見 [1.4.3 套件管理](#143-套件管理)。

#### 💡 實務案例

**專案目錄結構範例：**

```text
my_python_project/
│
├── .venv/                  # 虛擬環境（慣例目錄名，uv 預設使用）
├── src/                    # 原始碼（src-layout，避免誤 import 到未安裝的套件）
│   └── my_python_project/
│       ├── __init__.py
│       ├── main.py
│       └── utils/
├── tests/                  # 測試檔案
├── docs/                   # 文件
├── pyproject.toml          # 專案設定：依賴、建置後端、工具設定（PEP 621／PEP 735）
├── uv.lock                 # uv 的跨平台鎖檔
├── pylock.toml             # PEP 751 標準鎖檔（可由 uv export 產生，供其他工具使用）
├── README.md               # 專案說明
└── .gitignore              # Git 忽略檔案
```

#### ⚠️ 注意事項

1. **版本相容性**：建議使用 Python 3.13 以上版本（3.12 已進入 security-only、3.9 已 EOL）
2. **路徑問題**：確保 Python 已加入 PATH 環境變數
3. **權限問題**：Linux 系統可能需要 sudo 權限安裝套件
4. **虛擬環境**：每個專案都應使用獨立的虛擬環境

#### 📝 小測驗

1. Python 的哪個特性讓它適合初學者學習？
2. 如何在 Windows 系統中驗證 Python 是否安裝成功？
3. 為什麼要使用虛擬環境？
4. `pip freeze` 指令的作用是什麼？

**參考答案：**

1. 語法簡潔易讀，接近自然語言
2. 執行 `python --version` 和 `pip --version`
3. 隔離不同專案的依賴，避免版本衝突
4. 列出當前環境中所有已安裝的套件及其版本

#### 🏷️ 認證考試對應

- **PCEP**: 模組 1 - Python 基礎概念
- **PCAP**: 模組 1 - 控制和評估、使用模組和套件

---

### 1.2 語法基礎

#### 🎯 學習目標

- 掌握 Python 基本語法規則
- 了解變數宣告與命名規則
- 學習各種資料型態的使用
- 熟悉運算子的種類與使用

#### 1.2.1 Python 語法規則

##### 縮排 (Indentation)

Python 使用縮排來定義程式碼區塊，這是 Python 最重要的語法特色：

```python
# 正確的縮排
if True:
    print("這是正確的縮排")
    print("使用 4 個空格")

# 錯誤的縮排 - 會產生 IndentationError
if True:
print("這會產生錯誤")
```

##### 註解 (Comments)

```python
# 單行註解
print("Hello, World!")  # 行末註解

"""
多行註解
可以用三個引號包圍
"""

'''
也可以使用單引號
進行多行註解
'''
```

##### 分號與分行

```python
# Python 不需要分號結尾
print("Hello")
print("World")

# 可以使用分號在同一行寫多個語句（不建議）
print("Hello"); print("World")

# 長行可以使用反斜線換行
total = 1 + 2 + 3 + \
        4 + 5 + 6

# 或使用括號自動換行
total = (1 + 2 + 3 +
         4 + 5 + 6)
```

#### 1.2.2 變數與命名規則

##### 變數宣告

```python
# Python 是動態型別語言，不需要宣告變數型別
name = "張三"
age = 25
height = 175.5
is_student = True
```

##### 命名規則

```python
# 合法的變數名稱
user_name = "John"
_private_var = "private"
age2 = 25
PI = 3.14159

# 不合法的變數名稱
# 2age = 25        # 不能以數字開頭
# user-name = ""   # 不能包含連字號
# class = "A"      # 不能使用保留字
```

##### 命名慣例

```python
# 變數和函式：使用小寫字母和底線
user_name = "張三"
def calculate_total():
    pass

# 常數：使用大寫字母和底線
MAX_SIZE = 100
DEFAULT_TIMEOUT = 30

# 類別：使用 PascalCase
class UserAccount:
    pass

# 私有變數：以底線開頭
_internal_var = "internal"
__private_var = "private"
```

#### 1.2.3 資料型態

##### 數值型態

```python
# 整數 (int)
age = 25
population = 1000000
negative_num = -50

# 浮點數 (float)
price = 99.99
temperature = -15.5
scientific = 1.23e-4  # 科學記號

# 複數 (complex)
complex_num = 3 + 4j
```

##### 字串型態 (str)

```python
# 字串建立
name = "張三"
message = '歡迎使用 Python'
multiline = """這是
多行字串
的範例"""

# 字串操作
full_name = "張" + "三"           # 串接
repeated = "Hello " * 3          # 重複
length = len("Python")           # 長度
upper_case = "hello".upper()     # 轉大寫
lower_case = "WORLD".lower()     # 轉小寫

# 字串格式化
name = "Alice"
age = 30

# 舊式格式化
message1 = "我是 %s，今年 %d 歲" % (name, age)

# 新式格式化
message2 = "我是 {}，今年 {} 歲".format(name, age)

# f-string (Python 3.6+，推薦使用)
message3 = f"我是 {name}，今年 {age} 歲"

# 字串索引和切片
text = "Python"
first_char = text[0]        # 'P'
last_char = text[-1]        # 'n'
substring = text[1:4]       # 'yth'
reversed_text = text[::-1]  # 'nohtyP'
```

##### 布林型態 (bool)

```python
# 布林值
is_active = True
is_expired = False

# 布林運算
result = True and False     # False
result = True or False      # True
result = not True          # False

# 真假值判斷
if "":           # 空字串為 False
    pass
if 0:            # 零為 False
    pass
if []:           # 空串列為 False
    pass
if None:         # None 為 False
    pass
```

##### 串列型態 (list)

```python
# 建立串列
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "hello", 3.14, True]

# 串列操作
numbers.append(6)           # 加入元素
numbers.insert(0, 0)        # 插入元素
removed = numbers.pop()     # 移除並返回最後一個元素
numbers.remove(3)           # 移除指定值
length = len(numbers)       # 取得長度

# 串列索引和切片
first = numbers[0]          # 第一個元素
last = numbers[-1]          # 最後一個元素
subset = numbers[1:4]       # 切片
```

##### 字典型態 (dict)

```python
# 建立字典
student = {
    "name": "張三",
    "age": 20,
    "major": "資訊工程"
}

# 字典操作
student["grade"] = "A"      # 新增鍵值對
name = student["name"]      # 取得值
age = student.get("age", 0) # 安全取得值（有預設值）
keys = student.keys()       # 取得所有鍵
values = student.values()   # 取得所有值

# 字典遍歷
for key, value in student.items():
    print(f"{key}: {value}")
```

##### 元組型態 (tuple)

```python
# 建立元組
coordinates = (10, 20)
rgb_color = (255, 128, 0)
single_tuple = (42,)        # 單一元素元組需要逗號

# 元組特性：不可變 (immutable)
# coordinates[0] = 5        # 這會產生錯誤

# 元組解包
x, y = coordinates
red, green, blue = rgb_color
```

##### 集合型態 (set)

```python
# 建立集合
numbers = {1, 2, 3, 4, 5}
unique_chars = set("hello")  # {'h', 'e', 'l', 'o'}

# 集合操作
numbers.add(6)              # 加入元素
numbers.discard(3)          # 移除元素（不存在也不會錯誤）
numbers.remove(4)           # 移除元素（不存在會錯誤）

# 集合運算
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1 | set2         # 聯集: {1, 2, 3, 4, 5}
intersection = set1 & set2  # 交集: {3}
difference = set1 - set2    # 差集: {1, 2}
```

#### 1.2.4 運算子

##### 算術運算子

```python
a = 10
b = 3

# 基本運算
addition = a + b        # 13 (加法)
subtraction = a - b     # 7  (減法)
multiplication = a * b  # 30 (乘法)
division = a / b        # 3.333... (除法)
floor_division = a // b # 3  (整數除法)
modulus = a % b         # 1  (餘數)
power = a ** b          # 1000 (次方)
```

##### 比較運算子

```python
x = 5
y = 10

equal = x == y          # False (等於)
not_equal = x != y      # True  (不等於)
greater = x > y         # False (大於)
greater_equal = x >= y  # False (大於等於)
less = x < y            # True  (小於)
less_equal = x <= y     # True  (小於等於)
```

##### 邏輯運算子

```python
# and, or, not
result1 = True and False   # False
result2 = True or False    # True
result3 = not True         # False

# 實際應用
age = 25
has_license = True
can_drive = age >= 18 and has_license  # True
```

##### 賦值運算子

```python
x = 10

x += 5    # x = x + 5,  結果: 15
x -= 3    # x = x - 3,  結果: 12
x *= 2    # x = x * 2,  結果: 24
x /= 4    # x = x / 4,  結果: 6.0
x //= 2   # x = x // 2, 結果: 3.0
x %= 2    # x = x % 2,  結果: 1.0
x **= 3   # x = x ** 3, 結果: 1.0
```

##### 身份運算子

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

# is 檢查是否為同一個物件
print(a is b)        # True  (同一個物件)
print(a is c)        # False (不同物件，但內容相同)
print(a is not c)    # True

# == 檢查內容是否相同
print(a == c)        # True  (內容相同)
```

##### 成員運算子

```python
# in 和 not in
fruits = ["apple", "banana", "orange"]
has_apple = "apple" in fruits      # True
no_grape = "grape" not in fruits   # True

# 字串中的成員測試
text = "Hello, World!"
has_hello = "Hello" in text        # True
```

##### 海象運算子 (Walrus Operator, Python 3.8+)

```python
# := 賦值表達式，可在表達式中同時賦值並使用
# 傳統寫法
data = input("請輸入資料: ")
while data != "quit":
    print(f"你輸入了: {data}")
    data = input("請輸入資料: ")

# 使用海象運算子簡化
while (data := input("請輸入資料: ")) != "quit":
    print(f"你輸入了: {data}")

# 在串列推導式中使用
import math
numbers = [2, 5, 10, 20, 50, 100]
# 計算 log 並同時過濾
results = [(n, log_n) for n in numbers if (log_n := math.log(n)) > 2]
print(results)  # [(10, 2.302...), (20, 2.995...), (50, 3.912...), (100, 4.605...)]

# 在條件判斷中使用
text = "Hello, Python 3.12!"
if (match := len(text)) > 10:
    print(f"文字長度 {match}，超過 10 個字元")
```

#### 💡 實務案例

**型別轉換與驗證：**

```python
def safe_input_number(prompt):
    """安全地從使用者輸入取得數字"""
    while True:
        try:
            user_input = input(prompt)
            number = float(user_input)
            return number
        except ValueError:
            print("請輸入有效的數字")

# 使用範例
age = safe_input_number("請輸入年齡: ")
```

**資料型態檢查：**

```python
def analyze_data(data):
    """分析資料的型態和內容"""
    print(f"資料: {data}")
    print(f"型態: {type(data).__name__}")
    
    if isinstance(data, str):
        print(f"字串長度: {len(data)}")
    elif isinstance(data, (list, tuple)):
        print(f"序列長度: {len(data)}")
    elif isinstance(data, dict):
        print(f"字典鍵數: {len(data)}")
    elif isinstance(data, (int, float)):
        print(f"數值: {data}")

# 測試不同型態
analyze_data("Hello")
analyze_data([1, 2, 3])
analyze_data({"name": "John", "age": 30})
```

#### ⚠️ 注意事項

1. **縮排一致性**：務必使用一致的縮排（建議 4 個空格）
2. **變數命名**：使用有意義的變數名稱，遵循 PEP 8 規範
3. **型別轉換**：注意隱式和顯式型別轉換可能造成的問題
4. **可變與不可變**：了解哪些型態是可變的，哪些是不可變的

#### 📝 小測驗

1. Python 使用什麼來定義程式碼區塊？
2. 以下哪個變數名稱是合法的？`2name`, `user_name`, `class`, `_private`
3. `"5" + "3"` 的結果是什麼？
4. 如何檢查 "apple" 是否在串列 `["apple", "banana"]` 中？
5. `10 // 3` 和 `10 / 3` 的差異是什麼？

**參考答案：**

1. 縮排 (Indentation)
2. `user_name` 和 `_private` 是合法的
3. `"53"` (字串串接)
4. `"apple" in ["apple", "banana"]`
5. `//` 是整數除法 (結果: 3)，`/` 是一般除法 (結果: 3.333...)

#### 🏷️ 認證考試對應

- **PCEP**: 模組 2 - 資料型態、變數、基本 I/O 操作、運算子
- **PCAP**: 模組 1 - 控制和評估、資料聚合

---

#### 1.2.5 型別提示 (Type Hints)

Python 3.5+ 引入了型別提示，3.9+ 大幅簡化語法，3.12+ 引入了新的型別參數語法，3.14+ 改為延遲求值。型別提示不會影響執行時行為，但有助於程式碼可讀性和靜態分析。

##### 基本型別標註

```python
# 變數型別標註
name: str = "Alice"
age: int = 25
height: float = 165.5
is_student: bool = True

# 函式參數與回傳值標註
def greet(name: str, times: int = 1) -> str:
    return f"Hello, {name}! " * times

def calculate_bmi(weight: float, height: float) -> float:
    """計算 BMI 指數"""
    return weight / (height / 100) ** 2

# Python 3.9+: 可直接使用內建型別作為泛型
numbers: list[int] = [1, 2, 3]
config: dict[str, str] = {"host": "localhost", "port": "8080"}
coordinates: tuple[float, float] = (25.0, 121.5)
unique_ids: set[int] = {1, 2, 3}

# Python 3.10+: 使用 | 取代 Union
def parse_input(value: str | int) -> str:
    return str(value)

# Optional 等同於 X | None
def find_user(user_id: int) -> dict | None:
    # 可能回傳 None
    return None
```

##### 進階型別提示

```python
from typing import (
    Callable, Iterator, Generator,
    TypeAlias, TypeVar, Generic
)

# 型別別名
Vector: TypeAlias = list[float]
Matrix: TypeAlias = list[Vector]

def dot_product(v1: Vector, v2: Vector) -> float:
    return sum(a * b for a, b in zip(v1, v2))

# Callable 型別
Handler: TypeAlias = Callable[[str, int], bool]

def register_handler(name: str, handler: Handler) -> None:
    pass

# 泛型 (Python 3.12+ 新語法 PEP 695)
type Point[T] = tuple[T, T]  # Python 3.12+ type 語句

# 等效的傳統寫法
T = TypeVar("T")
class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        return self._items.pop()

# Python 3.12+ 新寫法
class Stack[T]:
    def __init__(self) -> None:
        self._items: list[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        return self._items.pop()

stack = Stack[int]()
stack.push(42)
```

##### 靜態型別檢查工具

型別提示本身不會在執行時被強制，必須搭配靜態檢查器才有價值。兩大主流：

```bash
# mypy：型別檢查的參考實作，規則最貼近 PEP 定義
uv add --dev mypy
mypy src/
mypy --strict src/            # 嚴格模式：要求所有函式都有完整標註

# pyright：微軟開發，VS Code 的 Pylance 底層引擎，速度快、推斷較積極
uv add --dev pyright
pyright src/
```

設定寫在 `pyproject.toml`，讓 IDE 與 CI 使用同一組規則：

```toml
[tool.mypy]
python_version = "3.14"
strict = true
warn_unreachable = true
# 第三方套件缺少型別資訊時不報錯
ignore_missing_imports = true

[tool.pyright]
pythonVersion = "3.14"
typeCheckingMode = "strict"
include = ["src"]
```

##### 標註的執行時行為（Python 3.14+ 重要變更）

Python 3.14 起標註改為**延遲求值**（PEP 649／PEP 749），不再需要 `from __future__ import annotations`，且前向參考不必再寫成字串：

```python
# Python 3.14+：TreeNode 尚未定義完成也能直接寫在標註中
class TreeNode:
    def add_child(self, child: TreeNode) -> None: ...

# 需要在執行時取得標註時，使用 annotationlib（Python 3.14+）
import annotationlib

annotationlib.get_annotations(TreeNode.add_child, format=annotationlib.Format.VALUE)
# 也可取得未求值的字串形式，避免觸發匯入
annotationlib.get_annotations(TreeNode.add_child, format=annotationlib.Format.STRING)
```

詳見 [2.5.4 Python 3.14 新特性](#254-python-314-新特性2025-年-10-月發布)。

---

### 1.3 流程控制

#### 🎯 學習目標

- 掌握條件判斷的語法與應用
- 學習各種迴圈結構的使用
- 了解例外處理機制
- 熟悉程式流程控制技巧

#### 1.3.1 條件判斷 (if 語句)

##### 基本 if 語句

```python
# 基本條件判斷
age = 18
if age >= 18:
    print("已成年")

# if-else 語句
score = 85
if score >= 60:
    print("及格")
else:
    print("不及格")

# if-elif-else 語句
grade = 88
if grade >= 90:
    print("A 級")
elif grade >= 80:
    print("B 級")
elif grade >= 70:
    print("C 級")
elif grade >= 60:
    print("D 級")
else:
    print("F 級")
```

##### 複合條件

```python
age = 25
has_license = True
has_car = False

# 邏輯運算子
if age >= 18 and has_license:
    print("可以開車")

if has_car or has_license:
    print("具備開車條件之一")

if not has_car:
    print("沒有車子")

# 成員運算子
valid_grades = ["A", "B", "C", "D"]
student_grade = "B"
if student_grade in valid_grades:
    print("有效的成績")
```

##### 條件表達式 (三元運算子)

```python
# 一般寫法
age = 20
if age >= 18:
    status = "成人"
else:
    status = "未成年"

# 條件表達式寫法
status = "成人" if age >= 18 else "未成年"

# 實際應用
def get_discount(is_member):
    return 0.1 if is_member else 0.0

discount = get_discount(True)  # 0.1
```

#### 1.3.1.1 結構化模式匹配 (match/case, Python 3.10+)

`match/case` 語句提供了比多個 `if-elif-else` 更強大且可讀的分支邏輯：

##### 基本模式匹配

```python
# 基本 match/case
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 301:
            return "Moved Permanently"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:   # 萬用模式（預設）
            return f"Unknown status: {status}"

print(http_status(200))  # OK
print(http_status(999))  # Unknown status: 999
```

##### 結構化模式 (Structural Patterns)

```python
# 匹配序列
def process_command(command):
    match command.split():
        case ["quit"]:
            print("退出程式")
        case ["hello", name]:
            print(f"你好, {name}!")
        case ["move", direction, steps]:
            print(f"向 {direction} 移動 {steps} 步")
        case ["add", *items]:
            print(f"新增項目: {items}")
        case _:
            print(f"未知命令: {command}")

process_command("hello Alice")       # 你好, Alice!
process_command("move north 5")      # 向 north 移動 5 步
process_command("add a b c")         # 新增項目: ['a', 'b', 'c']
```

##### 匹配類別與守衛條件

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

def describe_point(point):
    match point:
        case Point(x=0, y=0):
            return "原點"
        case Point(x=0, y=y):
            return f"在 Y 軸上, y={y}"
        case Point(x=x, y=0):
            return f"在 X 軸上, x={x}"
        case Point(x=x, y=y) if x == y:
            return f"在對角線上, x=y={x}"
        case Point(x=x, y=y):
            return f"一般點 ({x}, {y})"

print(describe_point(Point(0, 0)))    # 原點
print(describe_point(Point(3, 3)))    # 在對角線上, x=y=3
print(describe_point(Point(1, 2)))    # 一般點 (1, 2)

# 匹配字典
def process_event(event):
    match event:
        case {"type": "click", "x": x, "y": y}:
            print(f"滑鼠點擊 ({x}, {y})")
        case {"type": "keypress", "key": key}:
            print(f"按下按鍵: {key}")
        case {"type": str(t)}:
            print(f"未處理的事件類型: {t}")
```

#### 1.3.2 迴圈結構

##### for 迴圈

```python
# 遍歷序列
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"我喜歡 {fruit}")

# 使用 range
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
    print(i)

# 遍歷字典
student = {"name": "Alice", "age": 20, "major": "CS"}
for key, value in student.items():
    print(f"{key}: {value}")

# 只遍歷鍵
for key in student.keys():
    print(key)

# 只遍歷值
for value in student.values():
    print(value)

# enumerate：同時取得索引和值
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"{index}: {name}")

# 從指定索引開始
for index, name in enumerate(names, start=1):
    print(f"{index}: {name}")
```

##### while 迴圈

```python
# 基本 while 迴圈
count = 0
while count < 5:
    print(f"計數: {count}")
    count += 1

# 使用者輸入驗證
while True:
    user_input = input("請輸入 'quit' 結束: ")
    if user_input.lower() == 'quit':
        break
    print(f"您輸入了: {user_input}")

# 計算累加
total = 0
number = 1
while number <= 100:
    total += number
    number += 1
print(f"1 到 100 的總和: {total}")
```

##### 迴圈控制

###### break 語句

```python
# 在 for 迴圈中使用 break
for i in range(10):
    if i == 5:
        break
    print(i)  # 輸出: 0, 1, 2, 3, 4

# 在 while 迴圈中使用 break
count = 0
while True:
    if count >= 3:
        break
    print(f"計數: {count}")
    count += 1
```

###### continue 語句

```python
# 跳過偶數
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 輸出: 1, 3, 5, 7, 9

# 跳過特定條件
numbers = [1, -2, 3, -4, 5]
for num in numbers:
    if num < 0:
        continue
    print(f"正數: {num}")
```

###### else 子句

```python
# for-else：迴圈正常結束時執行
for i in range(5):
    print(i)
else:
    print("迴圈正常結束")

# while-else：條件為 False 時執行
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("while 迴圈結束")

# 搜尋範例
numbers = [1, 3, 5, 7, 9]
target = 4
for num in numbers:
    if num == target:
        print(f"找到目標數字: {target}")
        break
else:
    print(f"未找到目標數字: {target}")
```

##### 巢狀迴圈

```python
# 九九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j:2d}", end="  ")
    print()  # 換行

# 矩陣處理
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
```

#### 1.3.3 例外處理

##### 基本例外處理

```python
# try-except 基本語法
try:
    number = int(input("請輸入一個數字: "))
    result = 10 / number
    print(f"結果: {result}")
except ValueError:
    print("輸入的不是有效數字")
except ZeroDivisionError:
    print("不能除以零")
```

##### 捕獲多種例外

```python
try:
    value = input("請輸入數字: ")
    number = float(value)
    result = 100 / number
    print(f"100 / {number} = {result}")
except (ValueError, TypeError):
    print("輸入值錯誤")
except ZeroDivisionError:
    print("除數不能為零")
except Exception as e:
    print(f"發生未知錯誤: {e}")
```

##### 完整的例外處理結構

```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("錯誤：除數不能為零")
        return None
    except TypeError:
        print("錯誤：參數必須是數字")
        return None
    else:
        print("計算成功")
        return result
    finally:
        print("清理資源")

# 測試
print(safe_divide(10, 2))   # 正常情況
print(safe_divide(10, 0))   # 除零錯誤
print(safe_divide(10, "2")) # 型別錯誤
```

##### 自定義例外

```python
# 定義自定義例外
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class AgeError(Exception):
    """年齡相關的例外"""
    pass

# 使用自定義例外
def validate_age(age):
    if age < 0:
        raise AgeError("年齡不能為負數")
    if age > 150:
        raise AgeError("年齡不能超過 150 歲")
    return True

try:
    age = int(input("請輸入年齡: "))
    validate_age(age)
    print(f"年齡 {age} 是有效的")
except AgeError as e:
    print(f"年齡錯誤: {e}")
except ValueError:
    print("請輸入有效的數字")
```

##### 例外群組 (Exception Groups, Python 3.11+)

```python
# ExceptionGroup 可同時處理多個例外
def validate_form(data):
    """驗證表單資料，收集所有錯誤"""
    errors = []
    if not data.get("name"):
        errors.append(ValueError("姓名不能為空"))
    if not data.get("email") or "@" not in data.get("email", ""):
        errors.append(ValueError("電子郵件格式無效"))
    if not isinstance(data.get("age"), int) or data["age"] < 0:
        errors.append(TypeError("年齡必須是正整數"))
    
    if errors:
        raise ExceptionGroup("表單驗證失敗", errors)

# 使用 except* 捕捉特定類型的例外
try:
    validate_form({"name": "", "email": "invalid", "age": -1})
except* ValueError as eg:
    print(f"值錯誤 ({len(eg.exceptions)} 個):")
    for e in eg.exceptions:
        print(f"  - {e}")
except* TypeError as eg:
    print(f"型別錯誤 ({len(eg.exceptions)} 個):")
    for e in eg.exceptions:
        print(f"  - {e}")

```

##### 免括號的多重例外捕捉（Python 3.14+，PEP 758）

Python 3.14 起，**在未使用 `as` 子句時**，`except` 與 `except*` 可省略括號：

```python
# Python 3.14+ 新語法
try:
    connect_to_server()
except TimeoutError, ConnectionRefusedError:
    print("網路連線失敗")

# 注意：有 as 子句時仍必須加括號
try:
    connect_to_server()
except (TimeoutError, ConnectionRefusedError) as e:
    print(f"網路連線失敗: {e}")
```

##### finally 區塊的控制流警告（Python 3.14+，PEP 765）

在 `finally` 區塊中使用 `return`／`break`／`continue` 會吞掉正在傳播的例外，是長年的錯誤來源。Python 3.14 起編譯器會對此發出 `SyntaxWarning`：

```python
def risky():
    try:
        raise ValueError("重要錯誤")
    finally:
        return "OK"   # SyntaxWarning：例外被默默吞掉，函式回傳 "OK"

# 正確做法：finally 只做資源清理，不改變控制流
def safe():
    try:
        raise ValueError("重要錯誤")
    finally:
        cleanup()     # 只清理，讓例外正常傳播
```

#### 1.3.4 進階流程控制

##### 列表推導式 (List Comprehension)

```python
# 基本列表推導式
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  # [1, 4, 9, 16, 25]

# 帶條件的列表推導式
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)  # [4, 16]

# 多層迴圈的列表推導式
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# 實際應用：處理字串
words = ["hello", "world", "python", "programming"]
uppercase_words = [word.upper() for word in words if len(word) > 5]
print(uppercase_words)  # ['PYTHON', 'PROGRAMMING']
```

##### 字典推導式和集合推導式

```python
# 字典推導式
numbers = [1, 2, 3, 4, 5]
square_dict = {x: x**2 for x in numbers}
print(square_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 集合推導式
text = "hello world"
unique_chars = {char.upper() for char in text if char.isalpha()}
print(unique_chars)  # {'H', 'E', 'L', 'O', 'W', 'R', 'D'}
```

##### 生成器表達式

```python
# 生成器表達式（記憶體效率更高）
numbers = (x**2 for x in range(1000000))  # 不會立即計算所有值

# 使用生成器
for i, square in enumerate(numbers):
    if i >= 5:  # 只取前 5 個
        break
    print(square)
```

#### 💡 實務案例

**輸入驗證函式：**

```python
def get_valid_input(prompt, input_type=str, validator=None):
    """
    獲取有效的使用者輸入
    
    Args:
        prompt: 提示訊息
        input_type: 期望的資料型態
        validator: 驗證函式
    """
    while True:
        try:
            user_input = input(prompt)
            
            # 型態轉換
            if input_type == int:
                value = int(user_input)
            elif input_type == float:
                value = float(user_input)
            else:
                value = user_input
            
            # 自定義驗證
            if validator and not validator(value):
                print("輸入值不符合要求，請重新輸入")
                continue
                
            return value
            
        except ValueError:
            print(f"請輸入有效的 {input_type.__name__}")

# 使用範例
age = get_valid_input(
    "請輸入年齡: ", 
    int, 
    lambda x: 0 <= x <= 150
)

grade = get_valid_input(
    "請輸入成績: ", 
    float, 
    lambda x: 0 <= x <= 100
)
```

**批次資料處理：**

```python
def process_student_data(students):
    """處理學生資料並產生統計報告"""
    
    results = {
        'passed': [],
        'failed': [],
        'honor_roll': [],
        'statistics': {}
    }
    
    total_score = 0
    
    for student in students:
        try:
            name = student['name']
            score = float(student['score'])
            
            # 分類學生
            if score >= 60:
                results['passed'].append(name)
                if score >= 90:
                    results['honor_roll'].append(name)
            else:
                results['failed'].append(name)
            
            total_score += score
            
        except (KeyError, ValueError, TypeError) as e:
            print(f"處理學生資料時發生錯誤: {e}")
            continue
    
    # 計算統計資訊
    total_students = len(students)
    if total_students > 0:
        results['statistics'] = {
            'total': total_students,
            'passed': len(results['passed']),
            'failed': len(results['failed']),
            'pass_rate': len(results['passed']) / total_students * 100,
            'average_score': total_score / total_students
        }
    
    return results

# 測試資料
students = [
    {'name': '張三', 'score': '85'},
    {'name': '李四', 'score': '92'},
    {'name': '王五', 'score': '45'},
    {'name': '趙六', 'score': '78'}
]

report = process_student_data(students)
print("統計報告:", report['statistics'])
```

#### ⚠️ 注意事項

1. **縮排一致性**：在條件和迴圈中保持一致的縮排
2. **避免無窮迴圈**：確保 while 迴圈有適當的結束條件
3. **例外處理粒度**：捕獲具體的例外類型，避免過於寬泛的例外處理
4. **資源清理**：使用 finally 或 with 語句確保資源正確釋放

#### 📝 小測驗

1. `if age >= 18 and has_license:` 中，如果 `age = 16`，還會檢查 `has_license` 嗎？
2. `for-else` 結構中，`else` 在什麼情況下會執行？
3. `continue` 和 `break` 的差異是什麼？
4. 什麼時候會執行 `finally` 區塊？
5. 列表推導式 `[x for x in range(10) if x % 2 == 0]` 的結果是什麼？

**參考答案：**

1. 不會，因為 `and` 運算子會短路評估
2. 當迴圈正常結束（沒有遇到 `break`）時執行
3. `continue` 跳過本次迭代，`break` 完全跳出迴圈
4. 無論是否發生例外，`finally` 都會執行
5. `[0, 2, 4, 6, 8]`

#### 🏷️ 認證考試對應

- **PCEP**: 模組 3 - 布林值、條件執行、迴圈、串列和串列處理、邏輯和位元運算
- **PCAP**: 模組 1 - 控制和評估、資料聚合

---

### 1.4 函式、模組與套件管理

#### 🎯 學習目標

- 學習函式的定義與呼叫
- 掌握參數傳遞的各種方式
- 了解模組的建立與使用
- 學習套件管理工具的使用

#### 1.4.1 函式基礎

##### 函式定義與呼叫

```python
# 基本函式定義
def greet():
    """簡單的問候函式"""
    print("Hello, World!")

# 呼叫函式
greet()

# 帶參數的函式
def greet_person(name):
    """問候特定人員的函式"""
    print(f"Hello, {name}!")

greet_person("Alice")

# 帶返回值的函式
def add_numbers(a, b):
    """計算兩數相加"""
    return a + b

result = add_numbers(5, 3)
print(f"結果: {result}")

# 多個返回值
def get_name_age():
    """返回姓名和年齡"""
    return "John", 25

name, age = get_name_age()
print(f"姓名: {name}, 年齡: {age}")
```

##### 參數類型

###### 位置參數

```python
def introduce(name, age, city):
    print(f"我是 {name}，{age} 歲，住在 {city}")

# 按順序傳遞參數
introduce("Alice", 25, "台北")
```

###### 關鍵字參數

```python
# 使用關鍵字指定參數
introduce(city="高雄", name="Bob", age=30)

# 混合使用（位置參數必須在關鍵字參數之前）
introduce("Charlie", age=35, city="台中")
```

###### 預設參數

```python
def greet_with_title(name, title="先生"):
    """帶有預設稱謂的問候函式"""
    print(f"您好，{title} {name}")

greet_with_title("王明")        # 使用預設值
greet_with_title("李小姐", "女士")  # 覆蓋預設值

# 注意：預設參數的陷阱
def add_item(item, target_list=[]):  # 危險！
    target_list.append(item)
    return target_list

# 正確的寫法
def add_item_safe(item, target_list=None):
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list
```

###### 可變參數

```python
# *args：接收任意數量的位置參數
def sum_all(*numbers):
    """計算所有數字的總和"""
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# **kwargs：接收任意數量的關鍵字參數
def print_info(**info):
    """印出所有資訊"""
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="台北")

# 混合使用
def flexible_function(required_arg, *args, **kwargs):
    print(f"必需參數: {required_arg}")
    print(f"位置參數: {args}")
    print(f"關鍵字參數: {kwargs}")

flexible_function("hello", 1, 2, 3, name="Bob", age=30)
```

##### 函式進階特性

###### 函式作為物件

```python
# 函式可以賦值給變數
def square(x):
    return x ** 2

my_function = square
print(my_function(5))  # 25

# 函式可以作為參數
def apply_operation(numbers, operation):
    """對數字串列應用操作"""
    return [operation(num) for num in numbers]

numbers = [1, 2, 3, 4, 5]
squared = apply_operation(numbers, square)
print(squared)  # [1, 4, 9, 16, 25]

# 函式可以作為返回值
def create_multiplier(factor):
    """建立乘法函式"""
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(10))  # 20
print(triple(10))  # 30
```

###### Lambda 函式

```python
# 基本 lambda 函式
square = lambda x: x ** 2
print(square(5))  # 25

# 多參數 lambda
add = lambda x, y: x + y
print(add(3, 4))  # 7

# 在 map, filter, sort 中使用
numbers = [1, 2, 3, 4, 5]

# map：對每個元素應用函式
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# filter：篩選元素
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# sort：自定義排序
students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
students.sort(key=lambda student: student[1])  # 按成績排序
print(students)
```

###### 裝飾器基礎

```python
# 簡單的裝飾器
def timing_decorator(func):
    """計算函式執行時間的裝飾器"""
    import time
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 執行時間: {end_time - start_time:.4f} 秒")
        return result
    
    return wrapper

# 使用裝飾器
@timing_decorator
def slow_function():
    import time
    time.sleep(1)
    return "完成"

result = slow_function()  # 會印出執行時間
```

#### 1.4.2 模組系統

##### 建立模組

```python
# math_utils.py 檔案內容
"""
數學工具模組
提供常用的數學計算函式
"""

PI = 3.14159

def circle_area(radius):
    """計算圓面積"""
    return PI * radius ** 2

def circle_circumference(radius):
    """計算圓周長"""
    return 2 * PI * radius

def factorial(n):
    """計算階乘"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

class Calculator:
    """簡單計算器類別"""
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
```

##### 匯入模組

```python
# 完整匯入
import math_utils
area = math_utils.circle_area(5)
calc = math_utils.Calculator()

# 匯入特定函式
from math_utils import circle_area, PI
area = circle_area(5)

# 匯入所有（不建議）
from math_utils import *

# 使用別名
import math_utils as mu
from math_utils import circle_area as calc_area

area = mu.circle_area(5)
area2 = calc_area(5)
```

##### 模組搜尋路徑

```python
import sys

# 檢視模組搜尋路徑
for path in sys.path:
    print(path)

# 動態添加路徑
sys.path.append("/path/to/my/modules")

# 環境變數 PYTHONPATH 也會影響搜尋路徑
```

##### 套件 (Packages)

```python
# 套件目錄結構
"""
my_package/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        submodule.py
"""

# __init__.py 檔案可以控制套件的匯入行為
# my_package/__init__.py
from .module1 import function1
from .module2 import function2

__all__ = ['function1', 'function2']  # 控制 from package import * 的行為

# 使用套件
from my_package import function1
from my_package.subpackage import submodule
```

#### 1.4.3 套件管理

##### pip 基本使用

```bash
# 安裝套件
pip install package_name

# 安裝特定版本
pip install package_name==1.2.3
pip install package_name>=1.2.0

# 從 requirements.txt 安裝
pip install -r requirements.txt

# 升級套件
pip install --upgrade package_name

# 解除安裝
pip uninstall package_name

# 列出已安裝套件
pip list

# 顯示套件資訊
pip show package_name

# 搜尋套件（注意：pip search 已於 2020 年停用）
# 請改用 https://pypi.org 網站搜尋
# pip search keyword  # 已停用
```

##### 虛擬環境管理

```bash
# 建立虛擬環境
python -m venv myproject_env

# 啟動虛擬環境
# Windows
myproject_env\Scripts\activate
# Linux/macOS
source myproject_env/bin/activate

# 停用虛擬環境
deactivate

# 匯出依賴清單
pip freeze > requirements.txt

# 依賴清單範例 (requirements.txt)
requests==2.32.3
numpy>=2.1.0
pandas==2.2.3
matplotlib==3.9.2
```

##### 以 pyproject.toml 宣告依賴（PEP 621 / PEP 735）

`requirements.txt` 沒有正式規格，且無法區分「發布用依賴」與「開發用依賴」。現代做法是把所有專案中繼資料集中在 `pyproject.toml`：

```toml
[project]
name = "myproject"
version = "0.1.0"
requires-python = ">=3.13"
# 執行時依賴：安裝本套件的人也會裝到
dependencies = [
    "httpx>=0.28",
    "pydantic>=2.10",
]

# PEP 735 依賴群組：不會發布到 PyPI，也不會被下游安裝
[dependency-groups]
dev = [
    "pytest>=8.3",
    "pytest-cov>=6.0",
    "ruff>=0.8",
    "mypy>=1.14",
]
docs = ["sphinx>=8.1"]
# 群組可互相引用
all = [{ include-group = "dev" }, { include-group = "docs" }]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

| 宣告位置 | 用途 | 會被下游安裝？ |
| --- | --- | --- |
| `[project].dependencies` | 執行時必需 | 是 |
| `[project.optional-dependencies]` | 選用功能，如 `pip install myproject[redis]` | 使用者指定時 |
| `[dependency-groups]`（PEP 735） | 開發期工具，如測試、檢查、文件 | **否** |

> PEP 735 於 2024 年 10 月定案，填補了「開發依賴無標準宣告位置」的長年缺口。新專案應直接使用 `[dependency-groups]`。

```bash
# 安裝依賴群組
uv sync --group dev
pip install --group dev        # pip 亦已支援
```

##### 鎖檔與可重現建置（PEP 751）

`pyproject.toml` 記錄的是**版本範圍**，兩次安裝可能得到不同版本。要讓建置可重現，必須有鎖檔——記錄每個套件的**確切版本與雜湊值**。

PEP 751 定義了標準鎖檔格式 `pylock.toml`，讓鎖檔不再綁定單一工具：

```bash
# uv：以 uv.lock 為主要格式，可匯出為標準格式供其他工具使用
uv lock
uv export --format pylock.toml -o pylock.toml

# pip：25.1 起提供實驗性的 pip lock
pip lock -r requirements.txt -o pylock.toml

# 從標準鎖檔安裝（pip 26.1 起，實驗性）
pip install -r pylock.toml
```

| 工具 | 原生鎖檔 | PEP 751 支援狀況 |
| --- | --- | --- |
| uv | `uv.lock`（跨平台） | 可匯出 `pylock.toml` |
| pip | 無 | `pip lock`（25.1+）與 `pip install -r pylock.toml`（26.1+），皆為實驗性 |
| PDM | `pdm.lock` | 可匯出 |
| Poetry | `poetry.lock` | 截至 2026 年 4 月尚未支援 |

**實務建議**：鎖檔必須提交進版本控制；CI 使用 `uv sync --frozen` 確保不會意外更新依賴。鎖檔中的雜湊值同時具備供應鏈防護作用，詳見 [3.4.4 供應鏈完整性](#344-供應鏈完整性)。

##### 套件建置與發布

```bash
# 1. 建置：產生 wheel（.whl）與原始碼發行版（.tar.gz）
uv build
# 或使用標準工具
python -m build

# 2. 檢查產物中繼資料是否正確
uv run twine check dist/*

# 3. 先發到 TestPyPI 驗證
uv publish --publish-url https://test.pypi.org/legacy/

# 4. 正式發布
uv publish
```

**建議改用 Trusted Publishing**：以 GitHub Actions 的 OIDC 身分直接向 PyPI 驗證，不需在 CI 中保存長期 API token，可根除 token 外洩風險：

```yaml
# .github/workflows/publish.yml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  publish:
    runs-on: ubuntu-latest
    environment: pypi
    permissions:
      id-token: write          # Trusted Publishing 必需，取得 OIDC token
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v5
      - run: uv build
      - uses: pypa/gh-action-pypi-publish@release/v1
        # 不需要 password / api-token
```

##### 常用第三方套件

```python
# requests - HTTP 請求
import requests
response = requests.get('https://api.github.com')
data = response.json()

# numpy - 數值計算
import numpy as np
array = np.array([1, 2, 3, 4, 5])
mean = np.mean(array)

# pandas - 資料分析
import pandas as pd
df = pd.read_csv('data.csv')
summary = df.describe()

# datetime - 日期時間處理
from datetime import datetime, timedelta
now = datetime.now()
tomorrow = now + timedelta(days=1)
```

#### 💡 實務案例

**模組化設計範例：**

```python
# config.py - 設定檔模組
"""應用程式設定"""

DATABASE_URL = "sqlite:///app.db"
DEBUG = True
SECRET_KEY = "your-secret-key"

# 設定類別
class Config:
    DEBUG = False
    TESTING = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    
class ProductionConfig(Config):
    DEBUG = False

# utils.py - 工具函式模組
"""常用工具函式"""

import json
import logging
from datetime import datetime

def setup_logging(level=logging.INFO):
    """設定日誌系統"""
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def save_json(data, filename):
    """儲存資料為 JSON 檔案"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        logging.error(f"儲存檔案失敗: {e}")
        return False

def load_json(filename):
    """載入 JSON 檔案"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"載入檔案失敗: {e}")
        return None

# main.py - 主程式
"""主應用程式"""

from config import DevelopmentConfig
from utils import setup_logging, save_json, load_json
import logging

def main():
    # 初始化
    setup_logging(logging.DEBUG if DevelopmentConfig.DEBUG else logging.INFO)
    logger = logging.getLogger(__name__)
    
    logger.info("應用程式啟動")
    
    # 業務邏輯
    data = {"message": "Hello, World!", "timestamp": str(datetime.now())}
    
    if save_json(data, "output.json"):
        logger.info("資料儲存成功")
    
    loaded_data = load_json("output.json")
    if loaded_data:
        logger.info(f"載入資料: {loaded_data}")

if __name__ == "__main__":
    main()
```

**自動化腳本範例：**

```python
# file_processor.py
"""檔案處理自動化腳本"""

import os
import shutil
from pathlib import Path
from typing import List, Optional

def organize_files_by_extension(source_dir: str, target_dir: str) -> dict:
    """
    根據副檔名整理檔案
    
    Args:
        source_dir: 來源目錄
        target_dir: 目標目錄
    
    Returns:
        處理結果統計
    """
    source_path = Path(source_dir)
    target_path = Path(target_dir)
    
    if not source_path.exists():
        raise FileNotFoundError(f"來源目錄不存在: {source_dir}")
    
    target_path.mkdir(exist_ok=True)
    
    stats = {"processed": 0, "errors": 0, "extensions": {}}
    
    for file_path in source_path.iterdir():
        if file_path.is_file():
            try:
                extension = file_path.suffix.lower() or "no_extension"
                
                # 建立副檔名目錄
                ext_dir = target_path / extension.lstrip('.')
                ext_dir.mkdir(exist_ok=True)
                
                # 移動檔案
                target_file = ext_dir / file_path.name
                shutil.move(str(file_path), str(target_file))
                
                # 更新統計
                stats["processed"] += 1
                stats["extensions"][extension] = stats["extensions"].get(extension, 0) + 1
                
            except Exception as e:
                print(f"處理檔案 {file_path} 時發生錯誤: {e}")
                stats["errors"] += 1
    
    return stats

# 使用範例
if __name__ == "__main__":
    result = organize_files_by_extension("./downloads", "./organized")
    print(f"處理完成: {result}")
```

#### ⚠️ 注意事項

1. **函式設計原則**：每個函式應該只做一件事情，遵循單一職責原則
2. **模組命名**：使用小寫字母和底線，避免與內建模組名稱衝突
3. **循環匯入**：避免模組之間的循環匯入問題
4. **虛擬環境**：每個專案都應該使用獨立的虛擬環境

#### 📝 小測驗

1. 如何定義一個接受任意數量參數的函式？
2. `from module import *` 有什麼潛在問題？
3. `__init__.py` 檔案的作用是什麼？
4. 如何查看當前環境安裝了哪些套件？
5. lambda 函式有什麼限制？

**參考答案：**

1. 使用 `*args` 和 `**kwargs`
2. 可能會污染命名空間，造成名稱衝突
3. 標示目錄為 Python 套件，控制套件匯入行為
4. 使用 `pip list` 指令
5. 只能包含表達式，不能包含語句，通常用於簡單的函式

#### 🏷️ 認證考試對應

- **PCEP**: 模組 4 - 函式、元組、字典、例外處理
- **PCAP**: 模組 2 - 模組和套件

---

## 2. 進階應用

### 2.1 面向物件程式設計

#### 🎯 學習目標

- 理解類別和物件的概念
- 掌握封裝、繼承、多型的原理
- 學習特殊方法的使用
- 了解設計模式的基本應用

#### 2.1.1 類別與物件基礎

##### 定義類別

```python
class Student:
    """學生類別"""
    
    # 類別變數（所有實例共享）
    school_name = "Python 學院"
    
    def __init__(self, name, age, student_id):
        """建構子 - 初始化實例"""
        self.name = name        # 實例變數
        self.age = age
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, subject, score):
        """新增成績"""
        self.grades.append({"subject": subject, "score": score})
    
    def get_average(self):
        """計算平均成績"""
        if not self.grades:
            return 0
        total = sum(grade["score"] for grade in self.grades)
        return total / len(self.grades)
    
    def display_info(self):
        """顯示學生資訊"""
        print(f"姓名: {self.name}")
        print(f"年齡: {self.age}")
        print(f"學號: {self.student_id}")
        print(f"學校: {self.school_name}")
        print(f"平均成績: {self.get_average():.2f}")

# 建立物件實例
student1 = Student("張三", 20, "S001")
student2 = Student("李四", 21, "S002")

# 使用物件方法
student1.add_grade("數學", 85)
student1.add_grade("英語", 92)
student1.display_info()
```

##### 屬性訪問控制

```python
class BankAccount:
    """銀行帳戶類別"""
    
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self._balance = initial_balance  # 受保護屬性（慣例）
        self.__pin = "1234"             # 私有屬性（名稱重整）
    
    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        """提款"""
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False
    
    def get_balance(self):
        """查詢餘額"""
        return self._balance
    
    def __validate_pin(self, pin):
        """私有方法：驗證 PIN"""
        return pin == self.__pin

# 使用範例
account = BankAccount("12345", 1000)
account.deposit(500)
print(f"餘額: {account.get_balance()}")  # 1500

# print(account.__pin)  # AttributeError: 沒有 __pin 屬性
# 實際上可以透過 _BankAccount__pin 訪問，但不建議
```

#### 2.1.2 封裝與屬性

##### 使用 property 裝飾器

```python
class Temperature:
    """溫度類別，支援攝氏和華氏轉換"""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """攝氏溫度 getter"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """攝氏溫度 setter"""
        if value < -273.15:
            raise ValueError("溫度不能低於絕對零度")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """華氏溫度"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """設定華氏溫度"""
        self.celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        """克氏溫度"""
        return self._celsius + 273.15

# 使用範例
temp = Temperature(25)
print(f"攝氏: {temp.celsius}°C")
print(f"華氏: {temp.fahrenheit}°F")
print(f"克氏: {temp.kelvin}K")

temp.fahrenheit = 100  # 設定華氏溫度
print(f"攝氏: {temp.celsius:.2f}°C")  # 自動轉換
```

##### 描述器 (Descriptors)

```python
class ValidatedAttribute:
    """驗證屬性的描述器"""
    
    def __init__(self, name, validator=None):
        self.name = name
        self.validator = validator
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)
    
    def __set__(self, obj, value):
        if self.validator and not self.validator(value):
            raise ValueError(f"Invalid value for {self.name}: {value}")
        obj.__dict__[self.name] = value

class Person:
    """使用描述器的人員類別"""
    
    # 定義驗證規則
    name = ValidatedAttribute("name", lambda x: isinstance(x, str) and len(x) > 0)
    age = ValidatedAttribute("age", lambda x: isinstance(x, int) and 0 <= x <= 150)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 使用範例
person = Person("Alice", 25)
# person.age = -5  # ValueError: Invalid value for age: -5
```

#### 2.1.3 繼承

##### 基本繼承

```python
class Animal:
    """動物基類"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def speak(self):
        """發出聲音（基本實現）"""
        print(f"{self.name} 發出聲音")
    
    def sleep(self):
        """睡覺"""
        print(f"{self.name} 正在睡覺")

class Dog(Animal):
    """狗類別，繼承自 Animal"""
    
    def __init__(self, name, breed):
        super().__init__(name, "犬科")  # 呼叫父類建構子
        self.breed = breed
    
    def speak(self):
        """覆寫父類方法"""
        print(f"{self.name} 汪汪叫")
    
    def fetch(self):
        """狗特有的行為"""
        print(f"{self.name} 去撿球")

class Cat(Animal):
    """貓類別，繼承自 Animal"""
    
    def __init__(self, name, breed):
        super().__init__(name, "貓科")
        self.breed = breed
    
    def speak(self):
        """覆寫父類方法"""
        print(f"{self.name} 喵喵叫")
    
    def climb(self):
        """貓特有的行為"""
        print(f"{self.name} 爬樹")

# 使用範例
dog = Dog("小白", "黃金獵犬")
cat = Cat("小黑", "波斯貓")

dog.speak()  # 小白 汪汪叫
cat.speak()  # 小黑 喵喵叫
dog.sleep()  # 小白 正在睡覺（繼承的方法）
```

##### 多重繼承

```python
class Flyable:
    """飛行能力 mixin"""
    
    def fly(self):
        print(f"{self.name} 正在飛行")

class Swimmable:
    """游泳能力 mixin"""
    
    def swim(self):
        print(f"{self.name} 正在游泳")

class Duck(Animal, Flyable, Swimmable):
    """鴨子，具備多種能力"""
    
    def __init__(self, name):
        super().__init__(name, "鳥類")
    
    def speak(self):
        print(f"{self.name} 嘎嘎叫")

# 使用範例
duck = Duck("小鴨")
duck.speak()  # 小鴨 嘎嘎叫
duck.fly()    # 小鴨 正在飛行
duck.swim()   # 小鴨 正在游泳

# 檢查方法解析順序 (MRO)
print(Duck.__mro__)
```

#### 2.1.4 多型

##### 方法重寫與多型

```python
class Shape:
    """形狀基類"""
    
    def __init__(self, name):
        self.name = name
    
    def area(self):
        """計算面積（抽象方法）"""
        raise NotImplementedError("子類必須實現此方法")
    
    def perimeter(self):
        """計算周長（抽象方法）"""
        raise NotImplementedError("子類必須實現此方法")

class Rectangle(Shape):
    """矩形類別"""
    
    def __init__(self, width, height):
        super().__init__("矩形")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    """圓形類別"""
    
    def __init__(self, radius):
        super().__init__("圓形")
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

# 多型的使用
def print_shape_info(shape):
    """列印形狀資訊（多型函式）"""
    print(f"形狀: {shape.name}")
    print(f"面積: {shape.area():.2f}")
    print(f"周長: {shape.perimeter():.2f}")
    print("-" * 20)

# 測試多型
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Rectangle(2, 8)
]

for shape in shapes:
    print_shape_info(shape)  # 同一個函式處理不同類型的物件
```

#### 2.1.5 特殊方法 (Magic Methods)

##### 常用特殊方法

```python
class Vector:
    """向量類別，展示特殊方法的使用"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """字串表示（使用者友善）"""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """物件表示（開發者友善）"""
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        """向量相加"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        """向量相減"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, scalar):
        """向量乘以純量"""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    def __eq__(self, other):
        """相等比較"""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
    
    def __len__(self):
        """向量長度"""
        return int((self.x**2 + self.y**2)**0.5)
    
    def __getitem__(self, index):
        """索引訪問"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("向量只有 x 和 y 分量")
    
    def __setitem__(self, index, value):
        """索引設定"""
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("向量只有 x 和 y 分量")

# 使用範例
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1)           # Vector(3, 4)
print(v1 + v2)      # Vector(4, 6)
print(v1 * 2)       # Vector(6, 8)
print(v1 == v2)     # False
print(len(v1))      # 5
print(v1[0])        # 3
v1[1] = 5
print(v1)           # Vector(3, 5)
```

#### 💡 實務案例

**設計模式：單例模式**

```python
class Singleton:
    """單例模式實現"""
    
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.value = 0
            self._initialized = True

# 資料庫連線管理器
class DatabaseManager(Singleton):
    """資料庫管理器（單例）"""
    
    def __init__(self):
        super().__init__()
        if not hasattr(self, 'connected'):
            self.connected = False
            self.connection = None
    
    def connect(self, host, port, database):
        """連接資料庫"""
        if not self.connected:
            print(f"連接到資料庫 {database} @ {host}:{port}")
            self.connection = f"Connection to {database}"
            self.connected = True
        return self.connection
    
    def disconnect(self):
        """斷開資料庫連接"""
        if self.connected:
            print("斷開資料庫連接")
            self.connected = False
            self.connection = None

# 測試單例
db1 = DatabaseManager()
db2 = DatabaseManager()
print(db1 is db2)  # True，同一個實例
```

**觀察者模式**

```python
class Subject:
    """主題（被觀察者）"""
    
    def __init__(self):
        self._observers = []
        self._state = None
    
    def attach(self, observer):
        """附加觀察者"""
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        """移除觀察者"""
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self):
        """通知所有觀察者"""
        for observer in self._observers:
            observer.update(self)
    
    def set_state(self, state):
        """設定狀態並通知觀察者"""
        self._state = state
        self.notify()
    
    def get_state(self):
        """取得狀態"""
        return self._state

class Observer:
    """觀察者介面"""
    
    def update(self, subject):
        """更新方法（由子類實現）"""
        raise NotImplementedError

class EmailNotifier(Observer):
    """電子郵件通知器"""
    
    def __init__(self, email):
        self.email = email
    
    def update(self, subject):
        print(f"發送郵件到 {self.email}: 狀態變更為 {subject.get_state()}")

class SMSNotifier(Observer):
    """簡訊通知器"""
    
    def __init__(self, phone):
        self.phone = phone
    
    def update(self, subject):
        print(f"發送簡訊到 {self.phone}: 狀態變更為 {subject.get_state()}")

# 使用範例
order_system = Subject()
email_notifier = EmailNotifier("user@example.com")
sms_notifier = SMSNotifier("0912345678")

order_system.attach(email_notifier)
order_system.attach(sms_notifier)

order_system.set_state("訂單已確認")
order_system.set_state("商品已出貨")
```

#### 2.1.6 資料類別 (dataclasses, Python 3.7+)

`dataclasses` 模組可自動產生 `__init__`、`__repr__`、`__eq__` 等方法，大幅簡化資料導向類別的定義：

```python
from dataclasses import dataclass, field, asdict, astuple
from typing import ClassVar

@dataclass
class Product:
    """產品資料類別"""
    name: str
    price: float
    quantity: int = 0
    tags: list[str] = field(default_factory=list)
    
    # 類別變數（不會成為 __init__ 參數）
    currency: ClassVar[str] = "TWD"
    
    @property
    def total_value(self) -> float:
        return self.price * self.quantity

# 自動產生 __init__、__repr__、__eq__
p1 = Product("筆電", 35000, 5)
p2 = Product("滑鼠", 500, 10, tags=["周邊", "辦公"])
print(p1)  # Product(name='筆電', price=35000, quantity=5, tags=[])
print(p1 == Product("筆電", 35000, 5))  # True

# 轉換為字典或元組
print(asdict(p1))   # {'name': '筆電', 'price': 35000, ...}
print(astuple(p2))  # ('滑鼠', 500, 10, ['周邊', '辦公'])
```

##### 進階 dataclass 功能

```python
from dataclasses import dataclass, field

# frozen=True 建立不可變物件（類似 namedtuple）
@dataclass(frozen=True)
class Coordinate:
    latitude: float
    longitude: float

# 可作為字典的鍵或放入集合
coord = Coordinate(25.0330, 121.5654)
locations = {coord: "台北101"}

# slots=True (Python 3.10+) 減少記憶體使用
@dataclass(slots=True)
class Point:
    x: float
    y: float

# kw_only=True (Python 3.10+) 強制使用關鍵字引數
@dataclass(kw_only=True)
class Config:
    host: str
    port: int
    debug: bool = False

config = Config(host="localhost", port=8080)

# __post_init__ 自訂初始化後邏輯
@dataclass
class Employee:
    first_name: str
    last_name: str
    full_name: str = field(init=False)
    
    def __post_init__(self):
        self.full_name = f"{self.first_name} {self.last_name}"

emp = Employee("John", "Doe")
print(emp.full_name)  # John Doe
```

#### ⚠️ 注意事項

1. **避免過度設計**：不要為了使用物件導向而過度複雜化簡單問題
2. **繼承 vs 組合**：優先考慮組合而非繼承（"has-a" vs "is-a"）
3. **多重繼承**：謹慎使用，注意方法解析順序 (MRO)
4. **抽象基類**：使用 `abc` 模組定義真正的抽象基類

#### 📝 小測驗

1. `__init__` 和 `__new__` 方法的差別是什麼？
2. 如何讓一個類別支援 `len()` 函式？
3. `super()` 函式的作用是什麼？
4. 什麼是方法解析順序 (MRO)？
5. `@property` 裝飾器的用途是什麼？

**參考答案：**

1. `__new__` 建立實例，`__init__` 初始化實例
2. 實現 `__len__` 方法
3. 呼叫父類的方法，支援多重繼承
4. Python 決定在多重繼承中呼叫哪個方法的順序
5. 將方法轉換為屬性，支援 getter/setter

#### 🏷️ 認證考試對應

- **PCEP**: 不涉及（PCEP 不包含 OOP）
- **PCAP**: 模組 3 - 物件導向程式設計

---

### 2.2 檔案處理與例外處理

#### 🎯 學習目標

- 掌握檔案讀寫操作
- 學習各種檔案格式處理
- 熟悉例外處理機制
- 了解上下文管理器的使用

#### 2.2.1 檔案基本操作

##### 檔案讀取

```python
# 基本讀取方式
file = open('example.txt', 'r', encoding='utf-8')
content = file.read()
file.close()

# 推薦使用 with 語句（自動關閉檔案）
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# 逐行讀取
with open('example.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())  # strip() 移除換行符

# 讀取所有行到串列
with open('example.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
```

##### 檔案寫入

```python
# 寫入模式（覆蓋原檔案）
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write('Hello, World!\n')
    file.write('這是第二行')

# 附加模式（在檔案末尾添加內容）
with open('output.txt', 'a', encoding='utf-8') as file:
    file.write('\n這是新增的內容')

# 寫入多行
lines = ['第一行\n', '第二行\n', '第三行\n']
with open('output.txt', 'w', encoding='utf-8') as file:
    file.writelines(lines)
```

##### 檔案模式

```python
# 常用檔案模式
modes = {
    'r': '只讀（預設）',
    'w': '寫入（覆蓋）',
    'a': '附加',
    'x': '獨佔創建（檔案存在則失敗）',
    'b': '二進位模式',
    't': '文字模式（預設）',
    '+': '讀寫模式'
}

# 二進位檔案操作
with open('image.jpg', 'rb') as file:
    binary_data = file.read()

with open('copy.jpg', 'wb') as file:
    file.write(binary_data)
```

#### 2.2.2 進階檔案處理

##### CSV 檔案處理

```python
import csv

# 讀取 CSV
with open('data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)  # 讀取標題行
    for row in reader:
        print(row)

# 使用 DictReader
with open('data.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"姓名: {row['name']}, 年齡: {row['age']}")

# 寫入 CSV
data = [
    ['姓名', '年齡', '城市'],
    ['張三', '25', '台北'],
    ['李四', '30', '高雄']
]

with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)
```

##### JSON 檔案處理

```python
import json

# 讀取 JSON
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    print(data)

# 寫入 JSON
data = {
    'name': '張三',
    'age': 25,
    'skills': ['Python', 'JavaScript', 'SQL']
}

with open('output.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

# 字串與 JSON 轉換
json_string = json.dumps(data, ensure_ascii=False)
parsed_data = json.loads(json_string)
```

##### XML 檔案處理

```python
import xml.etree.ElementTree as ET

# 解析 XML
tree = ET.parse('data.xml')
root = tree.getroot()

# 遍歷元素
for child in root:
    print(f"標籤: {child.tag}, 文字: {child.text}")

# 查找特定元素
books = root.findall('book')
for book in books:
    title = book.find('title').text
    author = book.find('author').text
    print(f"書名: {title}, 作者: {author}")

# 創建 XML
root = ET.Element('library')
book = ET.SubElement(root, 'book', id='1')
title = ET.SubElement(book, 'title')
title.text = 'Python 程式設計'

tree = ET.ElementTree(root)
tree.write('output.xml', encoding='utf-8', xml_declaration=True)
```

#### 2.2.3 例外處理機制

##### 基本例外處理

```python
# try-except 基本結構
try:
    number = int(input("請輸入一個數字: "))
    result = 10 / number
    print(f"結果: {result}")
except ValueError:
    print("輸入的不是有效數字")
except ZeroDivisionError:
    print("除數不能為零")
except Exception as e:
    print(f"發生未預期的錯誤: {e}")
```

##### 完整例外處理結構

```python
try:
    # 可能發生例外的程式碼
    file = open('data.txt', 'r')
    data = file.read()
    number = int(data)
    result = 100 / number
except FileNotFoundError:
    print("檔案不存在")
except ValueError:
    print("檔案內容不是有效數字")
except ZeroDivisionError:
    print("除數不能為零")
except Exception as e:
    print(f"其他錯誤: {e}")
else:
    # 沒有例外時執行
    print(f"計算結果: {result}")
finally:
    # 無論是否有例外都會執行
    try:
        file.close()
        print("檔案已關閉")
    except NameError:
        print("檔案未開啟")
```

##### 自定義例外

```python
class CustomError(Exception):
    """自定義例外類別"""
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code

class ValidationError(CustomError):
    """資料驗證錯誤"""
    pass

def validate_age(age):
    if not isinstance(age, int):
        raise ValidationError("年齡必須是整數", "TYPE_ERROR")
    if age < 0:
        raise ValidationError("年齡不能為負數", "VALUE_ERROR")
    if age > 150:
        raise ValidationError("年齡不能超過150歲", "RANGE_ERROR")
    return True

# 使用自定義例外
try:
    validate_age(-5)
except ValidationError as e:
    print(f"驗證錯誤: {e}")
    print(f"錯誤代碼: {e.error_code}")
```

##### 例外鏈與重新拋出

```python
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"無法找到檔案: {filename}")
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON 格式錯誤: {e}") from e

def main():
    try:
        data = process_file('config.json')
        print(data)
    except (FileNotFoundError, ValueError) as e:
        print(f"處理檔案時發生錯誤: {e}")
        # 記錄詳細錯誤資訊
        import traceback
        traceback.print_exc()
```

#### 2.2.4 上下文管理器

##### 自定義上下文管理器

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"開啟檔案: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(f"關閉檔案: {self.filename}")
        if self.file:
            self.file.close()
        if exc_type:
            print(f"處理例外: {exc_type.__name__}: {exc_value}")
        return False  # 不抑制例外

# 使用自定義上下文管理器
with FileManager('test.txt', 'w') as f:
    f.write('Hello, World!')
```

##### 使用 contextlib

```python
from contextlib import contextmanager
import os

@contextmanager
def change_directory(new_path):
    old_path = os.getcwd()
    try:
        os.chdir(new_path)
        yield new_path
    finally:
        os.chdir(old_path)

# 使用
with change_directory('/tmp'):
    print(f"當前目錄: {os.getcwd()}")
    # 在這裡執行需要在特定目錄下的操作

print(f"回到原目錄: {os.getcwd()}")
```

#### 💡 實務案例

**日誌檔案分析器：**

```python
import re
from datetime import datetime
from collections import defaultdict

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.stats = defaultdict(int)
    
    def parse_log_line(self, line):
        # 解析日誌格式: [timestamp] LEVEL: message
        pattern = r'\[(.+?)\] (\w+): (.+)'
        match = re.match(pattern, line.strip())
        if match:
            timestamp_str, level, message = match.groups()
            timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
            return timestamp, level, message
        return None
    
    def analyze(self):
        try:
            with open(self.log_file, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, 1):
                    try:
                        parsed = self.parse_log_line(line)
                        if parsed:
                            timestamp, level, message = parsed
                            self.stats[level] += 1
                            
                            if 'ERROR' in level:
                                print(f"第 {line_num} 行發現錯誤: {message}")
                    except Exception as e:
                        print(f"解析第 {line_num} 行時發生錯誤: {e}")
                        continue
        
        except FileNotFoundError:
            print(f"找不到日誌檔案: {self.log_file}")
        except PermissionError:
            print(f"沒有權限讀取檔案: {self.log_file}")
        except Exception as e:
            print(f"分析日誌時發生錯誤: {e}")
    
    def print_summary(self):
        print("\n=== 日誌統計摘要 ===")
        for level, count in sorted(self.stats.items()):
            print(f"{level}: {count} 條")

# 使用範例
analyzer = LogAnalyzer('application.log')
analyzer.analyze()
analyzer.print_summary()
```

#### ⚠️ 注意事項

1. **編碼問題**：處理中文檔案時一定要指定 `encoding='utf-8'`
2. **檔案關閉**：始終使用 `with` 語句確保檔案正確關閉
3. **例外處理**：不要忽略例外，至少要記錄錯誤訊息
4. **效能考慮**：處理大檔案時考慮逐行讀取而非一次讀取全部

#### 📝 小測驗

1. `with` 語句的優點是什麼？
2. 如何處理 CSV 檔案中的中文字元？
3. `except Exception` 和 `except:` 的差別是什麼？
4. 什麼時候會執行 `finally` 區塊？
5. 如何創建自定義例外類別？

**參考答案：**

1. 自動管理資源，確保檔案等資源得到正確釋放
2. 指定正確的編碼格式，如 `encoding='utf-8'`
3. `except Exception` 可以取得例外物件，`except:` 會捕捉所有例外包括系統退出
4. 無論是否發生例外都會執行
5. 繼承 `Exception` 類別並定義 `__init__` 方法

#### 🏷️ 認證考試對應

- **PCEP**: 模組 4 - 函式、元組、字典、例外處理
- **PCAP**: 模組 2 - 字串、串列操作、例外處理

---

### 2.3 常用標準函式庫

#### 🎯 學習目標

- 熟悉 Python 標準函式庫的重要模組
- 學習日期時間處理
- 掌握正規表達式的使用
- 了解系統操作與網路程式設計基礎

#### 2.3.1 日期時間處理

##### datetime 模組

```python
from datetime import datetime, date, time, timedelta

# 取得當前時間
now = datetime.now()
today = date.today()
current_time = datetime.now().time()

print(f"現在時間: {now}")
print(f"今天日期: {today}")
print(f"當前時間: {current_time}")

# 創建特定日期時間
birthday = datetime(1990, 5, 15, 10, 30, 0)
special_date = date(2024, 12, 25)

# 時間格式化
formatted = now.strftime("%Y年%m月%d日 %H:%M:%S")
print(f"格式化時間: {formatted}")

# 字串解析為時間
date_string = "2024-03-15 14:30:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

# 時間運算
tomorrow = today + timedelta(days=1)
last_week = now - timedelta(weeks=1)
two_hours_later = now + timedelta(hours=2)

print(f"明天: {tomorrow}")
print(f"一週前: {last_week}")
print(f"兩小時後: {two_hours_later}")
```

##### 時區處理

```python
from datetime import datetime, timezone, timedelta
import pytz  # 需要安裝: pip install pytz

# UTC 時間
utc_now = datetime.now(timezone.utc)
print(f"UTC 時間: {utc_now}")

# 台北時區
taipei_tz = pytz.timezone('Asia/Taipei')
taipei_time = datetime.now(taipei_tz)
print(f"台北時間: {taipei_time}")

# 時區轉換
utc_time = datetime(2024, 3, 15, 12, 0, 0, tzinfo=timezone.utc)
local_time = utc_time.astimezone(taipei_tz)
print(f"轉換後時間: {local_time}")
```

#### 2.3.2 正規表達式

##### re 模組基礎

```python
import re

# 基本匹配
text = "我的電話是 0912-345-678，郵箱是 user@example.com"

# 搜尋第一個匹配
phone_pattern = r'\d{4}-\d{3}-\d{3}'
phone_match = re.search(phone_pattern, text)
if phone_match:
    print(f"找到電話: {phone_match.group()}")

# 搜尋所有匹配
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_pattern, text)
print(f"所有郵箱: {emails}")

# 替換
cleaned_text = re.sub(r'\d{4}-\d{3}-\d{3}', '[電話已隱藏]', text)
print(f"替換後: {cleaned_text}")
```

##### 進階正規表達式

```python
# 群組捕獲
log_pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) \[(\w+)\] (.+)'
log_line = "2024-03-15 14:30:25 [INFO] 用戶登入成功"

match = re.match(log_pattern, log_line)
if match:
    date, time, level, message = match.groups()
    print(f"日期: {date}, 時間: {time}, 級別: {level}, 訊息: {message}")

# 命名群組
pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
match = re.search(pattern, "今天是 2024-03-15")
if match:
    print(f"年: {match.group('year')}")
    print(f"月: {match.group('month')}")
    print(f"日: {match.group('day')}")

# 編譯正規表達式（提升效能）
compiled_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
emails = compiled_pattern.findall(text)
```

#### 2.3.3 系統操作

##### os 模組

```python
import os

# 目錄操作
current_dir = os.getcwd()
print(f"當前目錄: {current_dir}")

# 建立目錄
os.makedirs('test/subfolder', exist_ok=True)

# 列出目錄內容
files = os.listdir('.')
print(f"當前目錄檔案: {files}")

# 路徑操作
file_path = os.path.join('test', 'data.txt')
print(f"檔案路徑: {file_path}")
print(f"目錄名: {os.path.dirname(file_path)}")
print(f"檔名: {os.path.basename(file_path)}")
print(f"檔案存在: {os.path.exists(file_path)}")

# 環境變數
path_env = os.environ.get('PATH')
os.environ['MY_VAR'] = 'Hello World'
```

##### pathlib 模組（推薦）

```python
from pathlib import Path

# 路徑操作
current_path = Path.cwd()
file_path = Path('test') / 'data.txt'

# 檔案操作
if file_path.exists():
    content = file_path.read_text(encoding='utf-8')
    print(content)

# 目錄遍歷
for file in Path('.').glob('*.py'):
    print(f"Python 檔案: {file}")

# 檔案資訊
if file_path.exists():
    stat = file_path.stat()
    print(f"檔案大小: {stat.st_size} bytes")
    print(f"修改時間: {datetime.fromtimestamp(stat.st_mtime)}")
```

##### subprocess 模組

```python
import subprocess

# 執行系統命令
result = subprocess.run(['python', '--version'], 
                       capture_output=True, 
                       text=True)
print(f"Python 版本: {result.stdout}")

# 執行 shell 命令
try:
    output = subprocess.check_output('dir', shell=True, text=True)
    print(output)
except subprocess.CalledProcessError as e:
    print(f"命令執行失敗: {e}")
```

#### 2.3.4 網路程式設計基礎

##### urllib 模組

```python
import urllib.request
import urllib.parse
from urllib.error import URLError, HTTPError

# HTTP GET 請求
try:
    with urllib.request.urlopen('https://api.github.com/users/octocat') as response:
        data = response.read().decode('utf-8')
        print(data)
except HTTPError as e:
    print(f"HTTP 錯誤: {e.code} - {e.reason}")
except URLError as e:
    print(f"URL 錯誤: {e.reason}")

# 處理查詢參數
params = {'q': 'python', 'sort': 'stars'}
query_string = urllib.parse.urlencode(params)
url = f'https://api.github.com/search/repositories?{query_string}'
```

##### http.server 模組

```python
import http.server
import socketserver
from pathlib import Path

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/hello':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = '{"message": "Hello, World!"}'
            self.wfile.write(response.encode())
        else:
            super().do_GET()

# 啟動簡單 HTTP 伺服器
def start_server(port=8000):
    with socketserver.TCPServer(("", port), CustomHandler) as httpd:
        print(f"伺服器啟動在 http://localhost:{port}")
        httpd.serve_forever()

# start_server()  # 取消註解以啟動伺服器
```

#### 2.3.5 其他重要模組

##### collections 模組

```python
from collections import Counter, defaultdict, namedtuple, deque

# Counter - 計數器
text = "hello world"
counter = Counter(text)
print(f"字母計數: {counter}")
print(f"最常見的3個字母: {counter.most_common(3)}")

# defaultdict - 預設字典
dd = defaultdict(list)
dd['fruits'].append('apple')
dd['vegetables'].append('carrot')

# namedtuple - 命名元組
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"座標: ({p.x}, {p.y})")

# deque - 雙端佇列
dq = deque([1, 2, 3])
dq.appendleft(0)  # 左側添加
dq.append(4)      # 右側添加
print(f"雙端佇列: {list(dq)}")
```

##### itertools 模組

```python
import itertools

# 無限迭代器
counter = itertools.count(1, 2)  # 從1開始，步長為2
first_five = list(itertools.islice(counter, 5))
print(f"前5個奇數: {first_five}")

# 組合與排列
items = ['A', 'B', 'C']
combinations = list(itertools.combinations(items, 2))
permutations = list(itertools.permutations(items, 2))
print(f"組合: {combinations}")
print(f"排列: {permutations}")

# 產品
colors = ['red', 'blue']
sizes = ['S', 'M', 'L']
products = list(itertools.product(colors, sizes))
print(f"產品組合: {products}")
```

##### functools 模組

```python
import functools
import time

# 快取裝飾器
@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 部分函式
def multiply(x, y):
    return x * y

double = functools.partial(multiply, 2)
print(f"雙倍: {double(5)}")  # 輸出: 10

# 執行時間裝飾器
def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 執行時間: {end - start:.4f} 秒")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    return "完成"
```

#### 💡 實務案例

**網頁內容分析器：**

```python
import urllib.request
import re
from collections import Counter
from datetime import datetime
import json

class WebContentAnalyzer:
    def __init__(self, url):
        self.url = url
        self.content = ""
        self.analysis_time = None
    
    def fetch_content(self):
        try:
            with urllib.request.urlopen(self.url) as response:
                self.content = response.read().decode('utf-8')
                self.analysis_time = datetime.now()
                return True
        except Exception as e:
            print(f"獲取網頁內容失敗: {e}")
            return False
    
    def extract_links(self):
        link_pattern = r'href=[\'"]([^\'"]+)[\'"]'
        links = re.findall(link_pattern, self.content)
        return [link for link in links if link.startswith('http')]
    
    def extract_emails(self):
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.findall(email_pattern, self.content)
    
    def word_frequency(self, top_n=10):
        # 移除 HTML 標籤
        text = re.sub(r'<[^>]+>', ' ', self.content)
        # 提取單字
        words = re.findall(r'\b[A-Za-z]{3,}\b', text.lower())
        counter = Counter(words)
        return counter.most_common(top_n)
    
    def generate_report(self):
        if not self.content:
            return "尚未獲取網頁內容"
        
        report = {
            'url': self.url,
            'analysis_time': self.analysis_time.isoformat(),
            'content_length': len(self.content),
            'links_count': len(self.extract_links()),
            'emails_count': len(self.extract_emails()),
            'top_words': self.word_frequency()
        }
        
        return json.dumps(report, indent=2, ensure_ascii=False)

# 使用範例
# analyzer = WebContentAnalyzer('https://example.com')
# if analyzer.fetch_content():
#     print(analyzer.generate_report())
```

#### ⚠️ 注意事項

1. **效能考慮**：對於需要重複執行的正規表達式，使用 `re.compile()` 編譯
2. **時區處理**：處理國際化應用時注意時區轉換
3. **網路安全**：網路請求時要處理例外和設定超時
4. **資源管理**：使用完系統資源後要適當清理

#### 📝 小測驗

1. 如何獲取昨天的日期？
2. 正規表達式中 `\d+` 代表什麼？
3. `os.path.join()` 和字串串接的差別是什麼？
4. `functools.lru_cache` 的作用是什麼？
5. 如何安全地執行系統命令？

**參考答案：**

1. `datetime.now() - timedelta(days=1)`
2. 一個或多個數字字元
3. `os.path.join()` 會根據作業系統使用正確的路徑分隔符
4. 快取函式結果，避免重複計算
5. 使用 `subprocess.run()` 並處理例外

#### 🏷️ 認證考試對應

- **PCEP**: 模組 2 - 基本運算子、資料型態
- **PCAP**: 模組 2 - 字串、串列操作、模組和套件

---

### 2.4 測試與除錯

#### 🎯 學習目標

- 學習 Python 測試框架的使用
- 掌握單元測試的撰寫方法
- 了解除錯技巧與工具
- 建立測試驅動開發的概念

#### 2.4.1 單元測試基礎

##### unittest 模組

```python
import unittest

def add(a, b):
    """加法函式"""
    return a + b

def divide(a, b):
    """除法函式"""
    if b == 0:
        raise ValueError("除數不能為零")
    return a / b

class TestMathFunctions(unittest.TestCase):
    
    def setUp(self):
        """每個測試方法執行前都會呼叫"""
        self.test_data = [1, 2, 3, 4, 5]
    
    def tearDown(self):
        """每個測試方法執行後都會呼叫"""
        pass
    
    def test_add_positive_numbers(self):
        """測試正數加法"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(0, 0), 0)
    
    def test_add_negative_numbers(self):
        """測試負數加法"""
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(-5, 3), -2)
    
    def test_divide_normal(self):
        """測試正常除法"""
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(1, 3), 0.3333, places=4)
    
    def test_divide_by_zero(self):
        """測試除零例外"""
        with self.assertRaises(ValueError):
            divide(10, 0)
    
    def test_data_types(self):
        """測試資料型態"""
        self.assertIsInstance(add(1, 2), int)
        self.assertIsInstance(divide(1, 2), float)
    
    @unittest.skip("暫時跳過此測試")
    def test_skip_example(self):
        """示範跳過測試"""
        pass

if __name__ == '__main__':
    unittest.main()
```

##### 測試斷言方法

```python
class TestAssertions(unittest.TestCase):
    
    def test_equality_assertions(self):
        """等值斷言"""
        self.assertEqual(1 + 1, 2)
        self.assertNotEqual(1, 2)
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=7)
    
    def test_boolean_assertions(self):
        """布林斷言"""
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertIsNone(None)
        self.assertIsNotNone("Hello")
    
    def test_membership_assertions(self):
        """成員斷言"""
        self.assertIn('a', 'banana')
        self.assertNotIn('x', 'banana')
    
    def test_type_assertions(self):
        """型態斷言"""
        self.assertIsInstance([], list)
        self.assertIsInstance("hello", str)
    
    def test_sequence_assertions(self):
        """序列斷言"""
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        self.assertListEqual(list1, list2)
        self.assertCountEqual([1, 2, 3], [3, 2, 1])  # 順序無關
```

#### 2.4.2 進階測試技術

##### 測試類別和物件

```python
class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("存款金額必須為正數")
        self._balance += amount
        return self._balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("提款金額必須為正數")
        if amount > self._balance:
            raise ValueError("餘額不足")
        self._balance -= amount
        return self._balance
    
    @property
    def balance(self):
        return self._balance

class TestBankAccount(unittest.TestCase):
    
    def setUp(self):
        self.account = BankAccount(1000)
    
    def test_initial_balance(self):
        """測試初始餘額"""
        new_account = BankAccount()
        self.assertEqual(new_account.balance, 0)
        
        account_with_balance = BankAccount(500)
        self.assertEqual(account_with_balance.balance, 500)
    
    def test_deposit(self):
        """測試存款"""
        balance = self.account.deposit(200)
        self.assertEqual(balance, 1200)
        self.assertEqual(self.account.balance, 1200)
    
    def test_withdraw(self):
        """測試提款"""
        balance = self.account.withdraw(300)
        self.assertEqual(balance, 700)
        self.assertEqual(self.account.balance, 700)
    
    def test_deposit_invalid_amount(self):
        """測試無效存款金額"""
        with self.assertRaises(ValueError):
            self.account.deposit(-100)
        with self.assertRaises(ValueError):
            self.account.deposit(0)
    
    def test_withdraw_insufficient_funds(self):
        """測試餘額不足"""
        with self.assertRaises(ValueError):
            self.account.withdraw(1500)
```

##### 測試替身（Test Doubles）

```python
import unittest.mock as mock
import requests

def get_user_data(user_id):
    """從 API 獲取用戶資料"""
    response = requests.get(f'https://api.example.com/users/{user_id}')
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API 錯誤: {response.status_code}")

class TestApiCalls(unittest.TestCase):
    
    @mock.patch('requests.get')
    def test_get_user_data_success(self, mock_get):
        """測試成功獲取用戶資料"""
        # 設定模擬回應
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'id': 1, 'name': 'John'}
        mock_get.return_value = mock_response
        
        # 執行測試
        result = get_user_data(1)
        
        # 驗證結果
        self.assertEqual(result, {'id': 1, 'name': 'John'})
        mock_get.assert_called_once_with('https://api.example.com/users/1')
    
    @mock.patch('requests.get')
    def test_get_user_data_error(self, mock_get):
        """測試 API 錯誤"""
        mock_response = mock.Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        with self.assertRaises(Exception):
            get_user_data(999)
```

#### 2.4.3 pytest 框架

##### pytest 基礎

```python
# test_with_pytest.py
import pytest

def test_simple_addition():
    """簡單加法測試"""
    assert 1 + 1 == 2

def test_string_operations():
    """字串操作測試"""
    text = "Hello World"
    assert "Hello" in text
    assert text.upper() == "HELLO WORLD"
    assert len(text) == 11

def test_list_operations():
    """串列操作測試"""
    numbers = [1, 2, 3, 4, 5]
    assert len(numbers) == 5
    assert numbers[0] == 1
    assert numbers[-1] == 5
    assert sum(numbers) == 15

# 測試例外
def test_division_by_zero():
    """測試除零例外"""
    with pytest.raises(ZeroDivisionError):
        result = 1 / 0

# 參數化測試
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (10, -5, 5)
])
def test_addition_parametrized(a, b, expected):
    """參數化加法測試"""
    assert a + b == expected
```

##### pytest fixtures

```python
import pytest

@pytest.fixture
def sample_data():
    """提供測試資料的 fixture"""
    return {
        'users': [
            {'id': 1, 'name': 'Alice', 'age': 25},
            {'id': 2, 'name': 'Bob', 'age': 30}
        ],
        'products': [
            {'id': 1, 'name': 'Laptop', 'price': 50000},
            {'id': 2, 'name': 'Mouse', 'price': 500}
        ]
    }

@pytest.fixture
def temp_file(tmp_path):
    """提供臨時檔案的 fixture"""
    file_path = tmp_path / "test.txt"
    file_path.write_text("Hello, World!")
    return file_path

def test_user_data(sample_data):
    """使用 fixture 的測試"""
    users = sample_data['users']
    assert len(users) == 2
    assert users[0]['name'] == 'Alice'

def test_file_operations(temp_file):
    """測試檔案操作"""
    content = temp_file.read_text()
    assert content == "Hello, World!"
    assert temp_file.exists()

# 設定和清理
@pytest.fixture(scope="function")
def database_connection():
    """模擬資料庫連接"""
    print("\n設定資料庫連接")
    connection = "mock_db_connection"
    yield connection  # 提供給測試使用
    print("\n關閉資料庫連接")

def test_database_query(database_connection):
    """測試資料庫查詢"""
    assert database_connection == "mock_db_connection"
```

#### 2.4.4 除錯技巧

##### 使用 pdb 除錯器

```python
import pdb

def problematic_function(numbers):
    """有問題的函式，用於示範除錯"""
    total = 0
    for i, num in enumerate(numbers):
        pdb.set_trace()  # 設定中斷點
        if i % 2 == 0:
            total += num * 2
        else:
            total -= num
    return total

# 除錯命令：
# n (next) - 執行下一行
# s (step) - 進入函式內部
# c (continue) - 繼續執行
# l (list) - 顯示程式碼
# p variable_name - 印出變數值
# q (quit) - 退出除錯器

# numbers = [1, 2, 3, 4, 5]
# result = problematic_function(numbers)
```

##### 日誌除錯

```python
import logging

# 設定日誌
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def complex_calculation(data):
    """複雜計算函式，使用日誌除錯"""
    logger.info(f"開始處理資料，共 {len(data)} 筆")
    
    results = []
    for i, item in enumerate(data):
        logger.debug(f"處理第 {i+1} 筆資料: {item}")
        
        try:
            if isinstance(item, (int, float)):
                result = item ** 2 + 10
                logger.debug(f"計算結果: {result}")
                results.append(result)
            else:
                logger.warning(f"跳過非數值資料: {item}")
                
        except Exception as e:
            logger.error(f"處理資料時發生錯誤: {e}")
            continue
    
    logger.info(f"處理完成，共產生 {len(results)} 筆結果")
    return results

# 使用範例
# data = [1, 2, 3, "hello", 4.5, None, 6]
# results = complex_calculation(data)
```

##### 效能分析

```python
import time
import cProfile
import pstats
from functools import wraps

def timing_decorator(func):
    """計時裝飾器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 執行時間: {end_time - start_time:.4f} 秒")
        return result
    return wrapper

@timing_decorator
def slow_function():
    """模擬耗時函式"""
    total = 0
    for i in range(1000000):
        total += i ** 2
    return total

# 使用 cProfile 進行詳細分析
def profile_function():
    """分析函式效能"""
    profiler = cProfile.Profile()
    profiler.enable()
    
    # 執行要分析的程式碼
    result = slow_function()
    
    profiler.disable()
    
    # 輸出分析結果
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats(10)  # 顯示前10個最耗時的函式

# profile_function()
```

#### 2.4.5 測試驅動開發 (TDD)

##### TDD 開發流程示例

```python
import unittest

# 第一步：寫測試（紅燈）
class TestPasswordValidator(unittest.TestCase):
    
    def test_password_length_too_short(self):
        """密碼長度太短"""
        validator = PasswordValidator()
        self.assertFalse(validator.is_valid("123"))
    
    def test_password_length_valid(self):
        """密碼長度有效"""
        validator = PasswordValidator()
        self.assertTrue(validator.is_valid("12345678"))
    
    def test_password_must_contain_number(self):
        """密碼必須包含數字"""
        validator = PasswordValidator()
        self.assertFalse(validator.is_valid("abcdefgh"))
        self.assertTrue(validator.is_valid("abcdefg1"))
    
    def test_password_must_contain_uppercase(self):
        """密碼必須包含大寫字母"""
        validator = PasswordValidator()
        self.assertFalse(validator.is_valid("abcdefg1"))
        self.assertTrue(validator.is_valid("Abcdefg1"))

# 第二步：寫實作（綠燈）
class PasswordValidator:
    """密碼驗證器"""
    
    def is_valid(self, password):
        """驗證密碼是否有效"""
        if len(password) < 8:
            return False
        
        has_number = any(char.isdigit() for char in password)
        if not has_number:
            return False
        
        has_uppercase = any(char.isupper() for char in password)
        if not has_uppercase:
            return False
        
        return True

# 第三步：重構（改善程式碼品質）
import re

class PasswordValidator:
    """重構後的密碼驗證器"""
    
    def __init__(self, min_length=8):
        self.min_length = min_length
        self.rules = [
            (r'.{8,}', '密碼長度至少8個字元'),
            (r'.*\d', '密碼必須包含至少一個數字'),
            (r'.*[A-Z]', '密碼必須包含至少一個大寫字母'),
            (r'.*[a-z]', '密碼必須包含至少一個小寫字母')
        ]
    
    def is_valid(self, password):
        """驗證密碼是否有效"""
        return all(re.search(pattern, password) for pattern, _ in self.rules)
    
    def get_validation_errors(self, password):
        """取得驗證錯誤訊息"""
        errors = []
        for pattern, message in self.rules:
            if not re.search(pattern, password):
                errors.append(message)
        return errors
```

#### 💡 實務案例

**測試覆蓋率報告：**

```python
# 安裝 coverage: pip install coverage
# 執行: coverage run -m pytest test_module.py
# 報告: coverage report -m
# HTML 報告: coverage html

import coverage

def run_tests_with_coverage():
    """執行測試並產生覆蓋率報告"""
    cov = coverage.Coverage()
    cov.start()
    
    # 執行測試
    import unittest
    loader = unittest.TestLoader()
    suite = loader.discover('tests')
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    cov.stop()
    cov.save()
    
    # 產生報告
    print("\n=== 測試覆蓋率報告 ===")
    cov.report()
    
    return result.wasSuccessful()

# 自動化測試配置檔案 (pytest.ini)
"""
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    --verbose
    --tb=short
    --cov=src
    --cov-report=html
    --cov-report=term-missing
"""
```

#### ⚠️ 注意事項

1. **測試隔離**：每個測試應該獨立，不依賴其他測試的結果
2. **測試命名**：使用描述性的測試名稱，說明測試的目的
3. **測試資料**：使用固定的測試資料，避免隨機性
4. **效能測試**：不要在單元測試中包含耗時的操作

#### 📝 小測驗

1. `setUp()` 和 `tearDown()` 方法的作用是什麼？
2. 什麼是測試替身（Test Double）？
3. TDD 的三個步驟是什麼？
4. `pytest.fixture` 的作用是什麼？
5. 如何測試程式碼中的例外處理？

**參考答案：**

1. `setUp()` 在每個測試前執行初始化，`tearDown()` 在每個測試後執行清理
2. 用來替代真實依賴的物件，包括 Mock、Stub、Fake 等
3. 紅燈（寫測試）→ 綠燈（寫實作）→ 重構（改善程式碼）
4. 提供測試所需的資源和資料，支援設定和清理
5. 使用 `assertRaises()` 或 `pytest.raises()`

#### 🏷️ 認證考試對應

- **PCEP**: 不涉及（PCEP 不包含測試）
- **PCAP**: 模組 4 - 雜項（包含基本測試概念）

---

### 2.5 Python 現代特性（3.11 ~ 3.15）

#### 🎯 學習目標

- 了解 Python 3.11 ～ 3.15 的重要新特性與其對應的 PEP
- 掌握 f-string 改進、tomllib、free-threaded 模式等功能
- 認識模板字串（t-string）、懶惰匯入（lazy imports）等前沿特性
- 具備判斷「何時該升級、升級有何風險」的版本遷移能力

> **本節體例**：每個特性標註引入版本與 PEP 編號；涉及行為變更者另列**遷移風險**與**回退開關**。
> Python 3.15 的內容以 3.15 RC 階段文件為準（查核日期 2026-09-21），正式版發布後請覆核。

#### 2.5.1 Python 3.11 新特性

##### 增強的錯誤訊息

```python
# Python 3.11 的錯誤訊息會精確標示問題位置
# 例如以下程式碼：
# x = {"a": {"b": {"c": 1}}}
# print(x["a"]["b"]["d"]["e"])
#                    ^^^^
# KeyError: 'd'
# 箭頭直接指向有問題的鍵
```

##### tomllib 標準函式庫

```python
# Python 3.11+ 內建 TOML 解析器
import tomllib

# 讀取 TOML 設定檔
with open("pyproject.toml", "rb") as f:
    config = tomllib.loads(f.read().decode())
    # 或使用 tomllib.load(f)

print(config["project"]["name"])
print(config["project"]["version"])

# 注意：tomllib 只支援讀取，不支援寫入
# 若需寫入 TOML，請使用第三方套件 tomli-w 或 tomlkit
```

##### asyncio.TaskGroup

```python
import asyncio

async def fetch_data(url: str) -> str:
    """模擬非同步資料獲取"""
    await asyncio.sleep(1)
    return f"Data from {url}"

async def main():
    # TaskGroup 確保所有任務完成或在錯誤時取消
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch_data("https://api.example.com/users"))
        task2 = tg.create_task(fetch_data("https://api.example.com/products"))
        task3 = tg.create_task(fetch_data("https://api.example.com/orders"))
    
    # 所有任務完成後才會執行到這裡
    print(task1.result())
    print(task2.result())
    print(task3.result())

# asyncio.run(main())
```

#### 2.5.2 Python 3.12 新特性

##### f-string 改進

```python
# Python 3.12+ 允許在 f-string 中使用嵌套引號和反斜線
members = ["Alice", "Bob", "Charlie"]

# 嵌套引號（3.12 之前需要不同引號類型）
print(f"Members: {", ".join(members)}")

# f-string 中可使用反斜線
print(f"Path: {"\\".join(["C:", "Users", "Documents"])}")

# 多行表達式
matrix = [[1, 2], [3, 4]]
result = f"Matrix sum: {
    sum(
        val
        for row in matrix
        for val in row
    )
}"
print(result)  # Matrix sum: 10
```

##### 型別參數語法 (PEP 695)

```python
# Python 3.12+ 新的型別參數語法
# 舊寫法
from typing import TypeVar, Generic
T = TypeVar("T")
class OldStack(Generic[T]):
    pass

# Python 3.12+ 新寫法
class Stack[T]:
    def __init__(self) -> None:
        self._items: list[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        return self._items.pop()

# 泛型函式
def first[T](items: list[T]) -> T:
    return items[0]

# 型別別名
type Vector = list[float]
type Matrix = list[Vector]
```

#### 2.5.3 Python 3.13 新特性

##### 改進的互動式直譯器 (REPL)

```python
# Python 3.13 的新 REPL 功能：
# - 多行編輯與歷史記錄
# - 彩色輸出（錯誤訊息、語法高亮）
# - 支援 help、exit、quit 直接呼叫（不需括號）
# - 自動縮排
# - 貼上模式（自動偵測多行程式碼）

# 啟動新 REPL
# $ python3  (Python 3.13+)
```

##### Free-threaded CPython（實驗性，PEP 703）

```python
# Python 3.13 引入實驗性的 free-threaded 模式（無 GIL）
# 需要在編譯或安裝時啟用：python3.13t
# 或設定環境變數：PYTHON_GIL=0

import threading
import time

def cpu_intensive_task(n):
    """CPU 密集型任務"""
    total = 0
    for i in range(n):
        total += i ** 2
    return total

# 在 free-threaded 模式下，多執行緒可真正並行執行 CPU 密集任務
# 傳統 CPython 受 GIL 限制，多執行緒無法充分利用多核心

# 注意：Python 3.14 正式支援 free-threaded 模式（PEP 779）
# Python 3.13 中僅為實驗性功能
```

##### JIT 編譯器（實驗性，PEP 744）

```python
# Python 3.13 引入實驗性的 JIT (Just-In-Time) 編譯器
# 基於 copy-and-patch 技術，可提升部分場景下的執行效能

# 特點：
# - 自動將熱點程式碼編譯為機器碼
# - 對大多數程式碼無需任何修改
# - Python 3.14 擴展支援 Windows 和 macOS
# - Python 3.15 進一步升級 JIT 效能

# 啟用 JIT（需要特殊建置）：
# PYTHON_JIT=1 python my_script.py
```

#### 2.5.4 Python 3.14 新特性（2025 年 10 月發布）

##### 模板字串 (Template Strings / t-strings, PEP 750)

```python
# t-string 是 f-string 的延伸，提供結構化的字串處理能力
# 使用 t"..." 前綴，回傳 Template 物件而非直接產生字串

from string.templatelib import Template, Interpolation

name = "Alice"
age = 30

# t-string 不會直接產生字串，而是保留結構資訊
template = t"Hello, {name}! You are {age} years old."
# template 是 Template 物件，包含靜態文字和插值資訊

# 可用於安全的 HTML 生成、SQL 查詢等
def html_escape(template: Template) -> str:
    """安全的 HTML 模板處理"""
    parts = []
    for item in template:
        if isinstance(item, str):
            parts.append(item)
        elif isinstance(item, Interpolation):
            # 對插值進行 HTML 跳脫
            import html
            parts.append(html.escape(str(item.value)))
    return "".join(parts)

# 防止 XSS 攻擊
user_input = '<script>alert("XSS")</script>'
safe_html = html_escape(t"<p>User said: {user_input}</p>")
# 輸出: <p>User said: &lt;script&gt;alert(&quot;XSS&quot;)&lt;/script&gt;</p>
```

##### 延遲標註求值 (PEP 649/749)

```python
# Python 3.14 將標註（annotations）改為延遲求值
# 可以在標註中使用尚未定義的名稱

class TreeNode:
    def __init__(self, value: int, children: list["TreeNode"] | None = None):
        self.value = value
        self.children = children or []
    
    # 不再需要 from __future__ import annotations
    def add_child(self, child: "TreeNode") -> None:
        self.children.append(child)

# 標註在實際需要時才會被求值（如呼叫 typing.get_type_hints()）
# 這改善了啟動效能並解決了前向參考的問題
```

##### 多重直譯器 (PEP 734)

```python
# Python 3.14 在標準函式庫中加入 concurrent.interpreters 模組
# 注意模組路徑是 concurrent.interpreters，不是頂層的 interpreters
# 每個子直譯器有獨立的 GIL，可在同一個行程內實現真正的並行
from concurrent import interpreters

# 建立子直譯器
interp = interpreters.create()

# 在子直譯器中執行程式碼
interp.exec("print('Hello from sub-interpreter!')")

# 也可呼叫函式並取回結果
def square(n):
    return n * n

result = interp.call(square, 12)
print(result)  # 144

interp.close()
```

搭配 `concurrent.futures` 的執行器，可用熟悉的 API 把 CPU 密集工作分散到多個直譯器：

```python
from concurrent.futures import InterpreterPoolExecutor

def cpu_bound(n: int) -> int:
    return sum(i * i for i in range(n))

with InterpreterPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(cpu_bound, [10**6] * 4))
print(results)
```

> **限制**：子直譯器之間不共用物件，傳遞的資料必須可序列化或屬於可共享型別；部分 C 擴充套件尚未支援多直譯器，導入前務必實測。

##### 安全的外部除錯介面 (PEP 768)

Python 3.14 提供零開銷的除錯附掛介面，可對**正在執行中的生產程序**取得堆疊，不必事先埋入除錯碼——這是企業維運上價值極高的能力：

```bash
# 直接附掛到執行中的程序（PID 12345）
python -m pdb -p 12345
```

```python
import sys

# 底層 API：在目標程序中執行一段程式碼
sys.remote_exec(pid, "/path/to/script.py")
```

**安全控管**：此介面預設啟用，可用 `PYTHON_DISABLE_REMOTE_DEBUG` 環境變數或 `-X disable-remote-debug` 關閉；在多租戶或高敏感環境中建議於容器映像層級關閉。

##### asyncio 內省工具

排查「非同步任務卡住」過去極為困難，Python 3.14 提供了現成工具：

```bash
# 列出執行中程序的所有 asyncio 任務
python -m asyncio ps 12345

# 以樹狀結構顯示任務的呼叫關係（找出誰在等誰）
python -m asyncio pstree 12345
```

```python
import asyncio

# 在程式內取得目前的非同步呼叫圖
asyncio.print_call_graph()
graph = asyncio.capture_call_graph()
```

##### 其他重要改進

| 項目 | 說明 |
| --- | --- |
| REPL 語法高亮 | 互動式直譯器預設啟用語法著色與匯入自動補全；設 `PYTHON_BASIC_REPL` 可回退 |
| `annotationlib` | 新模組，以 `VALUE`／`FORWARDREF`／`STRING` 三種格式取得延遲求值的標註 |
| `pathlib` 強化 | 新增 `Path.copy()`、`Path.move()` 與 `Path.info` 屬性 |
| UUIDv7 | `uuid.uuid7()`，時間排序的 UUID，適合作為資料庫主鍵 |
| `map(strict=True)` | 長度不一致時拋出 `ValueError`，與 `zip(strict=)` 一致 |
| free-threaded 成熟 | 相對於預設建置的效能損耗自 3.13 的約 40% 降至 5–10% |
| tail-call 直譯器 | 以 Clang 19+ 建置可再獲約 3–5% 效能；需 `--with-tail-call-interp` |
| 免括號 except | PEP 758，見 [1.3.3 例外處理](#133-例外處理) |
| finally 控制流警告 | PEP 765，見 [1.3.3 例外處理](#133-例外處理) |

##### Zstandard 壓縮支援 (PEP 784)

```python
# Python 3.14 標準函式庫新增 compression.zstd 模組
import compression.zstd as zstd

# 壓縮資料
data = b"Hello, World! " * 1000
compressed = zstd.compress(data)
print(f"原始大小: {len(data)}, 壓縮後: {len(compressed)}")

# 解壓縮
decompressed = zstd.decompress(compressed)
assert decompressed == data
```

#### 2.5.5 Python 3.15 新特性（2026 年 10 月發布）

Python 3.15 依 PEP 790 的排程於 **2026-10-01** 發布（RC2 為 2026-09-01），支援至 2031-10。

> 本節內容以 3.15 RC 階段的官方文件為準（查核日期 2026-09-21）。正式版發布後，細節請以 [What's new in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html) 覆核。

##### UTF-8 成為預設編碼 (PEP 686) —— 影響最大的變更

這是 3.15 對既有專案**衝擊面最廣**的變更。在此之前，`open()` 未指定 `encoding` 時會採用系統的地區設定編碼；在繁體中文 Windows 上即為 `cp950`，長年是亂碼與 `UnicodeDecodeError` 的主要來源。3.15 起一律預設 UTF-8：

```python
# Python 3.15 起，未指定 encoding 時一律使用 UTF-8，與作業系統地區設定無關
with open("data.txt") as f:      # 等同 encoding="utf-8"
    content = f.read()

# 仍需讀取舊的 cp950 / big5 檔案時，必須明確指定
with open("legacy.txt", encoding="cp950") as f:
    content = f.read()
```

- **遷移風險**：若既有程式碼依賴系統編碼讀寫本地檔案（例如處理舊系統匯出的 Big5 檔），升級後會讀出亂碼或拋例外。
- **回退開關**：設定 `PYTHONUTF8=0` 或啟動時加 `-X utf8=0` 可恢復舊行為。
- **建議做法**：不要依賴回退開關。升級前先在 3.14 以 `-X warn_default_encoding` 執行測試套件，找出所有未指定 `encoding` 的呼叫點並逐一補上。

##### 明確懶惰匯入 (PEP 810)

```python
# lazy 為軟關鍵字，將模組的實際載入延後到第一次使用該名稱時
lazy import numpy as np
lazy from pandas import DataFrame

# 此時 numpy 與 pandas 都尚未載入，程式啟動不受其影響
def analyze(path: str):
    df = DataFrame()        # 到這一行才真正載入 pandas
    return np.mean(df.values)
```

對匯入大型套件的 CLI 工具，啟動時間改善相當可觀。三種控制方式：

| 方式 | 用途 |
| --- | --- |
| `lazy import` 語句 | 逐條指定，最精確 |
| `-X lazy_imports` / `PYTHON_LAZY_IMPORTS` | 全域啟用，適合 CLI 入口 |
| 模組層級 `__lazy_modules__` 清單 | 供向後相容，不需改寫 import 語句 |

> **注意**：具有匯入副作用的模組（例如在匯入時註冊 plugin 或修改全域狀態）不適合延遲匯入，副作用發生的時機會改變。

##### frozendict 內建型別 (PEP 814)

```python
# frozendict 進入 builtins，與 frozenset 地位相同，不需匯入
config = frozendict({"host": "localhost", "port": 8080})

# 所有鍵與值皆可雜湊時，frozendict 本身即可雜湊
settings_cache = {config: "cached_result"}

config["host"] = "remote"   # TypeError：不支援項目指派

# 保留插入順序，但比較時忽略順序
assert frozendict({"a": 1, "b": 2}) == frozendict({"b": 2, "a": 1})
```

適用於「想傳出設定字典但不希望呼叫端改動」的場合，可取代過去的防禦性複製。`copy`、`json`、`pickle`、`pprint` 等模組均已支援。

##### 推導式支援解包 (PEP 798)

```python
# 串列、集合、字典推導式與生成器運算式都支援 * 與 ** 解包
lists = [[1, 2], [3, 4], [5]]
flat = [*L for L in lists]              # [1, 2, 3, 4, 5]

# 取代過去的巢狀寫法 [x for L in lists for x in L]
dicts = [{"a": 1}, {"b": 2}]
merged = {**d for d in dicts}           # {'a': 1, 'b': 2}
```

##### sentinel 內建型別 (PEP 661)

用於區分「沒有傳入參數」與「傳入了 `None`」，取代過去自訂哨兵物件的各種土法：

```python
MISSING = sentinel("MISSING")

def update(value=MISSING):
    if value is MISSING:
        return "未提供參數"
    return f"設定為 {value}"   # 包含 value=None 的情況

update()        # '未提供參數'
update(None)    # '設定為 None'
```

哨兵物件具有簡潔的 `repr`、複製後維持同一性，且可被 pickle。

##### 型別系統強化

| PEP | 內容 |
| --- | --- |
| PEP 800 | Disjoint bases：讓型別檢查器理解兩個類別永不共用實例，強化 `isinstance` 的型別窄化 |
| PEP 728 | `TypedDict` 支援宣告額外項目的型別 |
| PEP 747 | `TypeForm`，可標註「型別本身」作為值傳遞 |

##### 效能分析套件 (PEP 799) 與 Tachyon

標準函式庫新增 `profiling` 套件，把既有的分析工具整理到統一命名空間下，並加入全新的高頻取樣分析器 **Tachyon**：

```bash
# 取樣分析器：對執行中的程序取樣，不需修改程式碼，開銷極低
python -m profiling.sampling -p 12345

# 分析一支腳本並輸出火焰圖
python -m profiling.sampling --flamegraph -o profile.html my_script.py
```

```python
# 傳統的確定性追蹤分析器移到 profiling.tracing
from profiling import tracing

tracing.run("sum(i ** 2 for i in range(1_000_000))")
```

- `profiling.sampling`（Tachyon）：取樣率最高可達 1,000,000 Hz，支援 wall-clock／CPU／GIL 持有時間等多種模式，輸出格式含 pstats、collapsed stacks、flamegraph、gecko、heatmap 與即時 TUI，並支援非同步程式的分析。
- `profiling.tracing`：確定性追蹤，`cProfile` 保留為相容別名；舊的 `profile` 模組已棄用，預計 3.17 移除。

##### JIT 效能提升

3.13 引入的 copy-and-patch JIT 在 3.15 大幅升級，相對於標準直譯器的幾何平均提升：**x86-64 Linux 約 8–9%**、**AArch64 macOS 約 12–13%**。同時 PEP 831 讓 CPython 預設保留 frame pointer，使 `perf` 等系統級分析器能正確還原 Python 堆疊。

##### 其他變更與棄用

| 項目 | 說明 |
| --- | --- |
| `math.integer`（PEP 791） | 新模組，收納整數專用的數學函式 |
| `re.prefixmatch()` | 新名稱；`re.match()` 語意易混淆，已軟性棄用 |
| `tomllib` | 支援 TOML 1.1.0 |
| `asyncio` | 新增 `TaskGroup.cancel()` 可提早中止整個任務群組 |
| `subprocess` | Linux 5.3+ 上 `Popen.wait()` 改為事件驅動，不再輪詢 |
| `threading` | 新增 `serialize_iterator()`、`synchronized_iterator()`、`concurrent_tee()`，配合 free-threaded 使用 |
| `sqlite3` | CLI 支援 SQL 關鍵字與資料表名稱補全、彩色輸出 |
| 錯誤訊息 | 巢狀屬性建議（`Did you mean '.inner.area'?`）、跨語言方法名提示（`.push()` → `.append()`） |
| 移除 | `__cached__` 模組屬性（自 3.13 起棄用） |

#### 2.5.6 版本生命週期與遷移策略

##### 版本選擇建議（2026 年基準）

| 情境 | 建議版本 | 理由 |
| --- | --- | --- |
| 新專案 | **3.14** | 處於 bugfix 階段，生態系相容性已成熟 |
| 既有生產系統 | 3.13 或 3.14 | 皆在 bugfix 階段，可持續取得缺陷修補 |
| 停留在 3.12 | 排定升級 | 已進入 security-only，不再修補一般缺陷 |
| 停留在 3.10／3.9 | **立即汰換** | 3.9 已 EOL；3.10 於 2026-10 EOL |
| 需要 CPU 平行 | 3.14 free-threaded（`python3.14t`） | PEP 779 起為正式支援，效能損耗已降至 5–10% |
| 前瞻評估 | 3.15 | 先加入 CI 矩陣測試，重點驗證 PEP 686 的編碼變更 |

##### 升級作業流程

```bash
# 1. 以新版本建立平行環境，不動既有環境
uv venv --python 3.14 .venv-314

# 2. 檢查第三方套件是否支援目標版本
uv pip install --python .venv-314 -r requirements.txt

# 3. 自動更新語法至目標版本慣用寫法
uv run pyupgrade --py314-plus $(git ls-files '*.py')
# 或使用 ruff 的 pyupgrade 規則集
uv run ruff check --select UP --fix .

# 4. 開啟棄用警告執行完整測試套件，讓問題浮現
uv run --python .venv-314 python -W error::DeprecationWarning -m pytest

# 5. 升級到 3.15 前，先找出所有未指定 encoding 的檔案操作
uv run python -X warn_default_encoding -m pytest
```

##### 升級注意事項

1. **一次跨一個版本**：3.11 → 3.12 → 3.13，不要直接從 3.9 跳到 3.14，問題難以歸因。
2. **在 CI 中加入目標版本的矩陣**：正式切換前讓新版本先跑上數週。
3. **優先檢查 C 擴充套件**：純 Python 套件通常無痛，含原生擴充者（numpy、pandas、lxml、psycopg）需確認已發布對應 ABI 的 wheel。
4. **free-threaded 建置需獨立驗證**：套件即使支援 3.14，也未必支援 3.14t。
5. **鎖定版本後再升級**：先有 `uv.lock` 或 `pylock.toml`，才能在出問題時精確回退。

---

### 2.6 非同步與併發程式設計

#### 🎯 學習目標

- 依工作性質（I/O-bound vs CPU-bound）正確選擇併發模型
- 掌握 `async`／`await` 與事件迴圈的運作方式
- 使用 `TaskGroup` 撰寫具備結構化併發保證的程式
- 了解 free-threaded 與子直譯器在 CPU 平行上的定位與限制
- 辨識並避免非同步程式的常見反模式

#### 2.6.1 併發模型選型

Python 提供的併發機制不只一種，選錯模型會讓效能不升反降。**先判斷工作是 I/O-bound 還是 CPU-bound，再選模型。**

| 模型 | 適用工作 | 平行執行 CPU？ | 記憶體共享 | 典型場景 |
| --- | --- | --- | --- | --- |
| `asyncio` | I/O-bound、高併發 | 否（單執行緒） | 共享 | 大量網路請求、Web 服務、爬蟲 |
| `threading` | I/O-bound、阻塞式 API | 否（受 GIL 限制） | 共享 | 呼叫沒有 async 版本的阻塞式函式庫 |
| `multiprocessing` | CPU-bound | 是 | 不共享（需序列化） | 影像處理、數值運算 |
| free-threaded（3.14+） | CPU-bound、需共享狀態 | **是** | 共享 | 記憶體中的大型資料結構平行處理 |
| 子直譯器（3.14+） | CPU-bound、需隔離 | **是** | 不共享（同行程） | 外掛沙箱、多租戶工作負載 |

**判斷準則：**

- 程式大部分時間在**等待**（網路、磁碟、資料庫）→ `asyncio`；若函式庫沒有 async 版本則用 `threading`。
- 程式大部分時間在**計算** → `multiprocessing`；若資料量大到序列化成本無法接受，改用 free-threaded。
- 需要隔離、避免互相影響 → 子直譯器。

```python
# 快速判斷：用 time 分別量測 CPU 時間與牆鐘時間
import time

t_wall = time.perf_counter()
t_cpu = time.process_time()

do_work()

wall = time.perf_counter() - t_wall
cpu = time.process_time() - t_cpu
# cpu / wall 接近 1 → CPU-bound；接近 0 → I/O-bound
print(f"CPU 佔比: {cpu / wall:.1%}")
```

#### 2.6.2 asyncio 基礎

##### 協程與事件迴圈

```python
import asyncio

async def fetch_user(user_id: int) -> dict:
    """以 async def 定義的函式稱為協程 (coroutine)"""
    await asyncio.sleep(0.5)        # 模擬 I/O 等待，期間事件迴圈可執行其他任務
    return {"id": user_id, "name": f"User{user_id}"}

async def main() -> None:
    # 直接 await：循序執行，總耗時 1.0 秒
    a = await fetch_user(1)
    b = await fetch_user(2)
    print(a, b)

asyncio.run(main())     # 建立事件迴圈、執行 main()、結束後關閉迴圈
```

**關鍵觀念**：`await` 讓出控制權給事件迴圈，不是「平行執行」。單純連續 `await` 仍是循序的——要真正併發，必須先把協程包成任務。

##### 併發執行多個任務

```python
async def main() -> None:
    # 方式一：gather —— 併發執行並依序取得結果，總耗時 0.5 秒
    results = await asyncio.gather(
        fetch_user(1),
        fetch_user(2),
        fetch_user(3),
    )
    print(results)

    # 方式二：as_completed —— 誰先完成先處理，適合逐筆串流輸出
    tasks = [fetch_user(i) for i in range(5)]
    for coro in asyncio.as_completed(tasks):
        result = await coro
        print(f"完成: {result}")
```

##### 把阻塞式函式接進事件迴圈

事件迴圈是單執行緒的，**任何阻塞呼叫都會凍結整個迴圈**。使用 `asyncio.to_thread()` 將其移至執行緒池：

```python
import asyncio
import requests          # 同步的 HTTP 函式庫，會阻塞

async def fetch_sync_api(url: str) -> str:
    # 錯誤：直接呼叫會阻塞整個事件迴圈
    # return requests.get(url).text

    # 正確：丟到執行緒池，事件迴圈得以繼續運作
    response = await asyncio.to_thread(requests.get, url)
    return response.text
```

> 更好的做法是改用原生支援非同步的函式庫，例如以 `httpx` 或 `aiohttp` 取代 `requests`。

#### 2.6.3 結構化併發

##### TaskGroup（Python 3.11+）

`TaskGroup` 保證「離開 `async with` 區塊時，所有子任務必定已完成或已被取消」，杜絕任務洩漏：

```python
import asyncio

async def fetch_data(url: str) -> str:
    await asyncio.sleep(1)
    return f"Data from {url}"

async def main() -> None:
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(fetch_data("https://api.example.com/users"))
        t2 = tg.create_task(fetch_data("https://api.example.com/products"))
        t3 = tg.create_task(fetch_data("https://api.example.com/orders"))
    # 離開區塊時，三個任務都已結束，可安全取結果
    print(t1.result(), t2.result(), t3.result())

asyncio.run(main())
```

**與 `gather` 的差別**：任一子任務拋出例外時，`TaskGroup` 會**自動取消其餘任務**，並以 `ExceptionGroup` 一次回報所有錯誤；`gather` 預設會讓其他任務繼續跑完。

```python
async def unreliable(n: int) -> int:
    await asyncio.sleep(n * 0.1)
    if n == 2:
        raise ValueError(f"任務 {n} 失敗")
    return n

async def main() -> None:
    try:
        async with asyncio.TaskGroup() as tg:
            for i in range(5):
                tg.create_task(unreliable(i))
    except* ValueError as eg:
        # 以 except* 處理例外群組，見 1.3.3 例外處理
        for e in eg.exceptions:
            print(f"捕捉到: {e}")
```

> Python 3.15 起新增 `TaskGroup.cancel()`，可在區塊內主動中止整個群組（例如已取得足夠結果時）。

##### 逾時控制

```python
async def main() -> None:
    # asyncio.timeout()：Python 3.11+ 的建議寫法
    try:
        async with asyncio.timeout(2.0):
            await fetch_data("https://slow.example.com")
    except TimeoutError:
        print("請求逾時")

    # 需要動態延長期限時
    async with asyncio.timeout(5.0) as cm:
        await first_step()
        cm.reschedule(asyncio.get_running_loop().time() + 10.0)
        await second_step()
```

##### 取消與清理

```python
async def worker() -> None:
    try:
        while True:
            await do_one_unit()
    except asyncio.CancelledError:
        await cleanup()      # 清理資源
        raise                # 務必重新拋出，否則取消機制會失效
```

> **常見錯誤**：捕捉 `CancelledError` 後不重新拋出，會讓 `TaskGroup` 與 `timeout` 無法正常終止任務。

#### 2.6.4 同步原語與佇列

即使 asyncio 是單執行緒，只要在 `await` 之間存取共享狀態，仍可能出現競態條件：

```python
import asyncio

# Semaphore：限制同時進行的請求數，避免打爆對方伺服器
semaphore = asyncio.Semaphore(10)

async def fetch_limited(url: str) -> str:
    async with semaphore:
        return await fetch(url)

# Lock：保護跨 await 的臨界區
lock = asyncio.Lock()
balance = 0

async def deposit(amount: int) -> None:
    global balance
    async with lock:
        current = balance
        await asyncio.sleep(0)      # 沒有 lock 的話，這裡會讓出控制權造成競態
        balance = current + amount
```

##### 生產者—消費者模式

```python
async def producer(queue: asyncio.Queue[int], n: int) -> None:
    for i in range(n):
        await queue.put(i)
    await queue.join()              # 等待所有項目被處理完畢

async def consumer(queue: asyncio.Queue[int], worker_id: int) -> None:
    while True:
        item = await queue.get()
        try:
            await process(item)
        finally:
            queue.task_done()       # 務必在 finally 中呼叫

async def main() -> None:
    queue: asyncio.Queue[int] = asyncio.Queue(maxsize=100)  # 設上限以產生背壓
    async with asyncio.TaskGroup() as tg:
        workers = [tg.create_task(consumer(queue, i)) for i in range(5)]
        await producer(queue, 1000)
        for w in workers:
            w.cancel()              # 佇列清空後收掉消費者
```

#### 2.6.5 free-threaded 與子直譯器實戰

##### free-threaded 建置（PEP 703／PEP 779）

自 Python 3.14 起，free-threaded 建置為**正式支援**（3.13 時僅為實驗性），可讓多執行緒真正平行使用多核心：

```bash
# 以 uv 安裝 free-threaded 版本
uv python install 3.14t
uv run --python 3.14t python -c "import sys; print(sys._is_gil_enabled())"   # False
```

```python
from concurrent.futures import ThreadPoolExecutor

def cpu_bound(n: int) -> int:
    return sum(i * i for i in range(n))

# 標準建置：受 GIL 限制，多執行緒對 CPU 密集工作幾乎沒有加速
# free-threaded 建置：可線性擴展到多核心，且執行緒間共享記憶體、無序列化成本
with ThreadPoolExecutor(max_workers=8) as pool:
    results = list(pool.map(cpu_bound, [10**7] * 8))
```

**導入注意事項：**

- 需另行安裝，可執行檔名為 `python3.14t`，與一般建置並存。
- 相較預設建置，單執行緒效能損耗約 **5–10%**（3.13 時約 40%）。
- **C 擴充套件必須另行編譯支援**，尚未支援者會退回啟用 GIL；升級前務必確認 numpy、pandas 等關鍵依賴的支援狀況。
- 原本被 GIL 意外「保護」的競態條件會浮現，共享狀態需明確加鎖。

##### 子直譯器（PEP 734）

若需要平行又要隔離，子直譯器是比 `multiprocessing` 更輕量的選擇——同一行程、無行程建立成本，但各自擁有獨立的 GIL 與模組狀態。用法見 [2.5.4 Python 3.14 新特性](#254-python-314-新特性2025-年-10-月發布)。

##### 三者取捨

| 面向 | multiprocessing | free-threaded | 子直譯器 |
| --- | --- | --- | --- |
| 平行 CPU | 是 | 是 | 是 |
| 資料傳遞成本 | 高（跨行程序列化） | 極低（直接共享） | 中（同行程但需序列化） |
| 隔離性 | 最高 | 無 | 高 |
| 啟動成本 | 高 | 極低 | 低 |
| 生態系支援 | 成熟 | 發展中 | 發展中 |

#### 2.6.6 除錯、觀測與常見反模式

##### 線上診斷

```bash
# 找出卡住的任務（Python 3.14+）
python -m asyncio ps 12345
python -m asyncio pstree 12345

# 附掛到執行中的程序除錯（PEP 768）
python -m pdb -p 12345

# 非同步感知的取樣分析（Python 3.15+）
python -m profiling.sampling -p 12345
```

##### 開發期偵錯模式

```python
# 啟用 debug 模式：偵測未被 await 的協程、執行過久的回呼
asyncio.run(main(), debug=True)
# 或以環境變數 PYTHONASYNCIODEBUG=1 啟用
```

##### 常見反模式

| 反模式 | 後果 | 正確做法 |
| --- | --- | --- |
| 在協程中呼叫 `time.sleep()`、`requests.get()` 等阻塞函式 | 整個事件迴圈凍結 | 改用 `asyncio.sleep()`、`httpx`，或包 `asyncio.to_thread()` |
| 忘記 `await`，只呼叫協程 | 協程從未執行，發出 `RuntimeWarning` | 開啟 `debug=True` 及早發現 |
| `asyncio.create_task()` 後不保留參考 | 任務可能被 GC 回收而中途消失 | 使用 `TaskGroup`，或把任務存進集合 |
| 捕捉 `CancelledError` 後不重新拋出 | 取消與逾時機制失效 | `except asyncio.CancelledError: ...; raise` |
| 無上限地 `gather` 數千個請求 | 耗盡連線與記憶體，或被對方限流 | 以 `Semaphore` 限制併發數 |
| 用 `asyncio` 處理 CPU 密集工作 | 完全沒有加速，還增加複雜度 | 改用 `multiprocessing` 或 free-threaded |

#### 💡 實務案例

**帶重試、限流與逾時的併發抓取器：**

```python
import asyncio
import httpx

async def fetch_with_retry(
    client: httpx.AsyncClient,
    url: str,
    semaphore: asyncio.Semaphore,
    max_retries: int = 3,
) -> str | None:
    """限流 + 逾時 + 指數退避重試"""
    async with semaphore:
        for attempt in range(max_retries):
            try:
                async with asyncio.timeout(10.0):
                    response = await client.get(url)
                    response.raise_for_status()
                    return response.text
            except (httpx.HTTPError, TimeoutError) as e:
                if attempt == max_retries - 1:
                    print(f"{url} 最終失敗: {e}")
                    return None
                # 指數退避：1s, 2s, 4s
                await asyncio.sleep(2 ** attempt)
    return None

async def fetch_all(urls: list[str], concurrency: int = 10) -> dict[str, str]:
    semaphore = asyncio.Semaphore(concurrency)
    results: dict[str, str] = {}

    async with httpx.AsyncClient() as client:
        async with asyncio.TaskGroup() as tg:
            tasks = {
                url: tg.create_task(fetch_with_retry(client, url, semaphore))
                for url in urls
            }

    for url, task in tasks.items():
        if (content := task.result()) is not None:
            results[url] = content
    return results

if __name__ == "__main__":
    urls = [f"https://example.com/page/{i}" for i in range(100)]
    data = asyncio.run(fetch_all(urls))
    print(f"成功取得 {len(data)} / {len(urls)} 筆")
```

#### ⚠️ 注意事項

1. **不要混用模型**：在同一段邏輯中同時使用 `asyncio` 與 `threading` 共享狀態，是極難除錯的來源。
2. **事件迴圈只有一個**：`asyncio.run()` 不可巢狀呼叫；在已有迴圈的環境（如 Jupyter）中請用 `await` 而非 `asyncio.run()`。
3. **加上背壓**：佇列與併發數一定要設上限，否則負載尖峰時會耗盡記憶體。
4. **free-threaded 不是免費午餐**：GIL 移除後，過去偶然安全的程式碼可能開始出錯。
5. **先量測再優化**：多數「效能問題」其實是單一慢查詢或 N+1 問題，改用非同步並不會解決。

#### 📝 小測驗

1. `await asyncio.sleep(1)` 與 `time.sleep(1)` 在協程中的差別是什麼？
2. `asyncio.gather()` 與 `asyncio.TaskGroup` 在某個子任務失敗時的行為有何不同？
3. 為什麼 `asyncio.create_task()` 的回傳值需要保留參考？
4. CPU 密集的工作應該選哪種併發模型？為什麼不是 `asyncio`？
5. 在協程中捕捉 `asyncio.CancelledError` 後，為什麼必須重新拋出？

**參考答案：**

1. `asyncio.sleep()` 讓出控制權給事件迴圈，其他任務可繼續執行；`time.sleep()` 阻塞整個執行緒，事件迴圈完全停擺。
2. `TaskGroup` 會取消其餘所有子任務並以 `ExceptionGroup` 一次回報；`gather()` 預設讓其他任務繼續執行完畢。
3. 事件迴圈只持有任務的弱參考，沒有強參考時任務可能在執行途中被垃圾回收而消失。
4. `multiprocessing` 或 free-threaded 建置。`asyncio` 是單執行緒協作式排程，CPU 密集工作不會讓出控制權，無法取得任何平行加速。
5. 不重新拋出等於「拒絕被取消」，會讓 `TaskGroup` 與 `asyncio.timeout()` 的取消機制失效，導致程式掛住。

#### 🏷️ 認證考試對應

- **PCAP**: 模組 5 - Miscellaneous（生成器、迭代器與進階函式概念）
- **企業實務**：非同步與併發非 PCEP／PCAP 考試範圍，但屬於企業級 Python 開發的核心能力

---

## 3. 專案實務應用

### 3.1 程式碼風格與規範

#### 🎯 學習目標

- 掌握 PEP 8 程式碼風格規範
- 學習撰寫乾淨且可維護的程式碼
- 了解程式碼檢查工具的使用
- 建立良好的開發習慣

#### 3.1.1 PEP 8 風格指南

##### 命名慣例

```python
# 正確的命名方式

# 變數和函式：小寫字母 + 底線
user_name = "John"
total_amount = 1000

def calculate_total_price():
    pass

def get_user_info():
    pass

# 常數：大寫字母 + 底線
MAX_RETRY_COUNT = 3
DEFAULT_TIMEOUT = 30
API_BASE_URL = "https://api.example.com"

# 類別：PascalCase
class UserAccount:
    pass

class PaymentProcessor:
    pass

# 私有屬性/方法：單底線開頭
class BankAccount:
    def __init__(self):
        self._balance = 0          # 受保護屬性
        self.__account_id = None   # 私有屬性
    
    def _validate_amount(self, amount):  # 受保護方法
        return amount > 0

# 模組名稱：小寫字母，可用底線
# user_utils.py, data_processor.py

# 套件名稱：小寫字母，不建議使用底線
# myproject, userauth
```

##### 程式碼佈局

```python
# 匯入順序
import os           # 標準庫
import sys
from pathlib import Path

import requests     # 第三方庫
import numpy as np
from flask import Flask

from myproject import utils    # 本地模組
from myproject.models import User

# 每組匯入之間空一行

# 函式定義
def short_function():
    return "simple"

# 兩空行分隔頂層函式和類別
def another_function():
    pass


class MyClass:
    """類別說明文件"""
    
    def __init__(self):
        self.value = 0
    
    # 類別內方法間一空行
    def method_one(self):
        pass
    
    def method_two(self):
        pass


# 運算子周圍的空格
x = 1
y = 2
z = x + y

# 函式參數
def function(param1, param2, param3=None):
    pass

# 串列、字典
my_list = [1, 2, 3, 4]
my_dict = {'key1': 'value1', 'key2': 'value2'}

# 切片不需要空格
text = "Hello World"
first_part = text[0:5]
last_part = text[6:]
```

##### 行長度與換行

```python
# 每行最多 79 字元（程式碼）或 72 字元（註解）

# 長函式呼叫的換行
result = some_function_with_long_name(
    parameter_one,
    parameter_two,
    parameter_three,
    parameter_four
)

# 或者
result = some_function_with_long_name(parameter_one, parameter_two,
                                     parameter_three, parameter_four)

# 長字典
config = {
    'database_host': 'localhost',
    'database_port': 5432,
    'database_name': 'myapp',
    'database_user': 'admin',
    'database_password': 'secret123'
}

# 長條件判斷
if (user.is_authenticated() and 
    user.has_permission('read') and 
    not user.is_suspended()):
    allow_access()

# 使用括號進行邏輯分組
if ((user.is_authenticated() and user.has_permission('read')) and
    not (user.is_suspended() or user.is_expired())):
    allow_access()
```

#### 3.1.2 文件字串與註解

##### 文件字串 (Docstrings)

```python
def calculate_discount(price, discount_rate, member_type="regular"):
    """
    計算商品折扣後的價格
    
    Args:
        price (float): 商品原價
        discount_rate (float): 折扣率 (0.0 ~ 1.0)
        member_type (str, optional): 會員類型. Defaults to "regular".
    
    Returns:
        float: 折扣後的價格
    
    Raises:
        ValueError: 當價格為負數或折扣率超出範圍時
    
    Example:
        >>> calculate_discount(100, 0.1)
        90.0
        >>> calculate_discount(100, 0.2, "premium")
        80.0
    """
    if price < 0:
        raise ValueError("價格不能為負數")
    
    if not 0 <= discount_rate <= 1:
        raise ValueError("折扣率必須在 0 到 1 之間")
    
    multiplier = {"regular": 1.0, "premium": 1.2, "vip": 1.5}
    final_discount = discount_rate * multiplier.get(member_type, 1.0)
    
    return price * (1 - min(final_discount, 1.0))


class UserManager:
    """
    使用者管理類別
    
    負責使用者的建立、驗證、更新等操作。
    支援不同類型的使用者帳戶管理。
    
    Attributes:
        users (dict): 儲存使用者資料的字典
        max_users (int): 系統支援的最大使用者數量
    """
    
    def __init__(self, max_users=1000):
        """
        初始化使用者管理器
        
        Args:
            max_users (int, optional): 最大使用者數量. Defaults to 1000.
        """
        self.users = {}
        self.max_users = max_users
    
    def create_user(self, username, email, password):
        """
        建立新使用者
        
        Args:
            username (str): 使用者名稱
            email (str): 電子郵件地址
            password (str): 密碼
        
        Returns:
            bool: 建立成功返回 True，否則返回 False
        """
        # 實現細節...
        pass
```

##### 註解最佳實務

```python
def process_payment(amount, payment_method):
    """處理付款"""
    
    # 驗證金額（必須為正數）
    if amount <= 0:
        raise ValueError("金額必須大於零")
    
    # TODO: 實現信用卡付款驗證
    # FIXME: 處理網路連線失敗的情況
    # NOTE: 此功能需要與銀行 API 整合
    
    # 計算手續費（不同付款方式有不同費率）
    fee_rates = {
        'credit_card': 0.03,    # 3% 手續費
        'debit_card': 0.01,     # 1% 手續費
        'bank_transfer': 0.005  # 0.5% 手續費
    }
    
    fee = amount * fee_rates.get(payment_method, 0.02)  # 預設 2%
    total_amount = amount + fee
    
    # 記錄交易（用於稽核）
    log_transaction(amount, fee, payment_method)
    
    return total_amount


# 避免無意義的註解
x = x + 1  # 不好：x 加一

# 解釋為什麼，而不是做什麼
x = x + 1  # 好：補償邊界條件造成的偏移
```

#### 3.1.3 程式碼檢查工具

Python 的程式碼品質工具可分為三類，缺一不可：

| 類別 | 作用 | 現代首選 | 傳統組合 |
| --- | --- | --- | --- |
| Linter | 找出錯誤與不良寫法 | **Ruff** | pylint、flake8 |
| Formatter | 統一排版 | **Ruff format** | black |
| 型別檢查 | 驗證型別一致性 | **mypy** 或 **pyright** | （無傳統對應） |

##### 使用 Ruff（建議首選）

Ruff 以 Rust 實作，在單一工具中重新實作了 flake8 及其數十個外掛、isort、pyupgrade、bandit 等規則，執行速度通常快上 10～100 倍。自 2025 年起已成為新專案的預設選擇。

```bash
# 安裝
uv add --dev ruff

# 檢查（取代 flake8 / pylint）
uv run ruff check .

# 自動修正可修復的問題
uv run ruff check --fix .

# 格式化（取代 black）
uv run ruff format .

# CI 模式：只檢查不修改，有問題即回傳非零結束碼
uv run ruff check --no-fix .
uv run ruff format --check .
```

設定集中在 `pyproject.toml`，不需要額外的 `.flake8`、`.isort.cfg`：

```toml
[tool.ruff]
line-length = 88
target-version = "py314"
exclude = [".git", "__pycache__", ".venv", "build", "dist"]

[tool.ruff.lint]
# 選用規則集：每個字母前綴對應一組原本獨立的工具
select = [
    "E", "W",   # pycodestyle：PEP 8 排版
    "F",        # Pyflakes：未使用的匯入、未定義的名稱
    "I",        # isort：匯入排序
    "UP",       # pyupgrade：自動採用新版語法
    "B",        # flake8-bugbear：常見的邏輯陷阱
    "SIM",      # flake8-simplify：可簡化的寫法
    "S",        # flake8-bandit：安全性問題（見 3.4.2）
    "ANN",      # flake8-annotations：要求型別標註
]
ignore = [
    "E501",     # 行長度交由 formatter 處理
    "ANN101",   # 不要求標註 self
]

[tool.ruff.lint.per-file-ignores]
# 測試檔案允許 assert 與缺少標註
"tests/**/*.py" = ["S101", "ANN"]

[tool.ruff.lint.isort]
known-first-party = ["myproject"]
```

**從舊工具遷移的對應關係：**

| 舊工具 | Ruff 對應規則集 | 說明 |
| --- | --- | --- |
| flake8 | `E`, `W`, `F` | 核心規則完全覆蓋 |
| isort | `I` | `ruff check --select I --fix` 即可排序 |
| black | `ruff format` | 格式化結果與 black 高度相容 |
| pyupgrade | `UP` | 自動升級語法至 `target-version` |
| bandit | `S` | 安全性檢查 |
| pylint | 部分（`PL` 前綴） | pylint 的跨檔案分析與設計類警告尚未完全覆蓋，對品質要求極高的專案可兩者並用 |

##### 型別檢查工具

型別檢查與 linter 是互補的，Ruff 不做型別推斷。詳見 [1.2.5 型別提示](#125-型別提示-type-hints)。

```bash
uv run mypy src/          # 規則最貼近 PEP 定義
uv run pyright src/       # 速度快、推斷積極，Pylance 的底層引擎
```

##### 傳統工具組合（維護既有專案時仍會遇到）

以下四項在新專案中已可由 Ruff 單一工具取代，但既有專案的維護、以及認證考試的名詞辨識仍需了解。

##### 使用 pylint

```bash
# 安裝 pylint
pip install pylint

# 檢查單一檔案
pylint my_script.py

# 檢查整個專案
pylint my_project/

# 產生設定檔
pylint --generate-rcfile > .pylintrc

# 忽略特定警告
pylint --disable=C0103,R0903 my_script.py
```

##### 使用 flake8

```bash
# 安裝 flake8
pip install flake8

# 檢查程式碼
flake8 my_script.py

# 設定檔 (.flake8 或 setup.cfg)
[flake8]
max-line-length = 88
ignore = E203, W503
exclude = 
    .git,
    __pycache__,
    .venv
```

##### 使用 black (程式碼格式化)

```bash
# 安裝 black
pip install black

# 格式化檔案
black my_script.py

# 格式化整個專案
black .

# 檢查但不修改
black --check .

# 顯示差異
black --diff my_script.py
```

##### 使用 isort (匯入排序)

```bash
# 安裝 isort
pip install isort

# 排序匯入
isort my_script.py

# 檢查但不修改
isort --check-only my_script.py

# 設定檔 (.isort.cfg)
[settings]
profile = black
line_length = 88
multi_line_output = 3
```

#### 3.1.4 程式碼品質實務

##### 函式設計原則

```python
# 單一職責原則 - 每個函式只做一件事
def calculate_tax(income):
    """只計算稅額"""
    return income * 0.2

def format_currency(amount):
    """只格式化貨幣顯示"""
    return f"${amount:,.2f}"

def send_notification(message, recipient):
    """只發送通知"""
    # 發送邏輯
    pass

# 不好的設計 - 一個函式做太多事
def process_order_bad(order_data):
    # 驗證資料
    # 計算價格
    # 更新庫存
    # 發送確認郵件
    # 記錄日誌
    pass

# 好的設計 - 職責分離
def validate_order(order_data):
    """驗證訂單資料"""
    pass

def calculate_order_total(order_items):
    """計算訂單總額"""
    pass

def update_inventory(order_items):
    """更新庫存"""
    pass

def send_confirmation_email(order_id, customer_email):
    """發送確認郵件"""
    pass

def process_order(order_data):
    """協調訂單處理流程"""
    if not validate_order(order_data):
        return False
    
    total = calculate_order_total(order_data['items'])
    update_inventory(order_data['items'])
    send_confirmation_email(order_data['id'], order_data['customer_email'])
    
    return True
```

##### 錯誤處理最佳實務

```python
import logging
from typing import Any

# 設定日誌
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Python 3.9+ 可直接使用內建型別作為泛型（list[int]、dict[str, Any]）
# Python 3.10+ 可用 X | None 取代 Optional[X]
# typing.List / typing.Dict / typing.Optional 已不建議在新程式碼中使用
def safe_divide(a: float, b: float) -> float | None:
    """
    安全除法，處理除零錯誤
    
    Args:
        a: 被除數
        b: 除數
    
    Returns:
        除法結果，如果除零則返回 None
    """
    try:
        if b == 0:
            logger.warning("嘗試除零運算")
            return None
        return a / b
    except TypeError as e:
        logger.error(f"型別錯誤: {e}")
        return None

def process_user_data(user_data: dict[str, Any]) -> bool:
    """
    處理使用者資料，包含完整的錯誤處理
    
    Args:
        user_data: 使用者資料字典
    
    Returns:
        處理成功返回 True
    """
    required_fields = ['name', 'email', 'age']
    
    try:
        # 驗證必需欄位
        for field in required_fields:
            if field not in user_data:
                raise ValueError(f"缺少必需欄位: {field}")
        
        # 驗證資料型態
        if not isinstance(user_data['age'], int) or user_data['age'] < 0:
            raise ValueError("年齡必須是非負整數")
        
        # 驗證電子郵件格式
        if '@' not in user_data['email']:
            raise ValueError("無效的電子郵件格式")
        
        # 處理資料...
        logger.info(f"成功處理使用者: {user_data['name']}")
        return True
        
    except ValueError as e:
        logger.error(f"資料驗證錯誤: {e}")
        return False
    except Exception as e:
        logger.error(f"未預期的錯誤: {e}")
        return False

# 自定義例外類別
class ValidationError(Exception):
    """驗證錯誤"""
    pass

class BusinessLogicError(Exception):
    """業務邏輯錯誤"""
    pass

def validate_business_rules(data):
    """驗證業務規則"""
    if data.get('amount', 0) > 10000:
        raise BusinessLogicError("單筆交易金額不能超過 10000")
    
    if not data.get('verified', False):
        raise ValidationError("帳戶未通過驗證")
```

#### 💡 實務案例

**專案結構範例：**

```text
my_python_project/
│
├── src/                    # 原始碼目錄
│   ├── __init__.py
│   ├── main.py            # 主程式入口
│   ├── config/            # 設定相關
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   └── database.py
│   ├── models/            # 資料模型
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── order.py
│   ├── services/          # 業務邏輯
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   └── order_service.py
│   └── utils/             # 工具函式
│       ├── __init__.py
│       ├── validators.py
│       └── helpers.py
│
├── tests/                 # 測試檔案
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_services.py
│   └── test_utils.py
│
├── docs/                  # 文件
│   ├── README.md
│   └── api_reference.md
│
├── requirements.txt       # 依賴清單
├── requirements-dev.txt   # 開發依賴
├── .gitignore            # Git 忽略檔案
├── .pylintrc             # Pylint 設定
├── setup.py              # 套件設定
└── README.md             # 專案說明
```

#### ⚠️ 注意事項

1. **一致性**：在整個專案中保持一致的程式碼風格
2. **可讀性優先**：程式碼是寫給人看的，機器只是恰好能執行
3. **適度註解**：註解應該解釋「為什麼」而不是「做什麼」
4. **重構習慣**：定期重構程式碼，保持程式碼品質

#### 📝 小測驗

1. PEP 8 建議的每行最大字元數是多少？
2. 類別名稱應該使用什麼命名慣例？
3. 私有屬性應該如何命名？
4. `black` 工具的主要用途是什麼？
5. 什麼是單一職責原則？

**參考答案：**

1. 79 字元（程式碼）或 72 字元（註解）
2. PascalCase（每個單字首字母大寫）
3. 以雙底線開頭（如 `__private_attr`）
4. 自動格式化 Python 程式碼
5. 一個函式或類別應該只有一個改變的理由，專注於單一功能

#### 🏷️ 認證考試對應

- **PCEP**: 模組 4 - 函式、元組、字典、例外處理（部分）
- **PCAP**: 模組 2 - 模組和套件（部分）

---

### 3.2 專案開發實務

#### 🎯 學習目標

- 掌握專案結構設計原則
- 學習版本控制的最佳實務
- 了解持續整合與部署概念
- 建立專案文件撰寫習慣

#### 3.2.1 專案結構設計

##### 標準專案結構

採用 **src-layout**（原始碼放在 `src/` 下）是目前的建議做法：測試時必須先安裝套件才能匯入，可及早發現封裝設定錯誤，避免「本機能跑、安裝後卻缺檔案」的問題。

```text
my_python_project/
│
├── README.md                 # 專案說明文件
├── pyproject.toml            # 專案設定：中繼資料、依賴、工具設定（PEP 621／735）
├── uv.lock                   # 鎖檔：確保可重現建置（須提交進版控）
├── pylock.toml               # PEP 751 標準鎖檔（可由 uv export 產生）
├── .gitignore               # Git 忽略檔案
├── .env.example             # 環境變數範例（絕不提交 .env 本身）
├── .pre-commit-config.yaml  # 提交前自動檢查
├── Makefile                 # 自動化腳本
├── LICENSE                  # 授權檔案
│
├── src/                     # 源碼目錄
│   └── myproject/
│       ├── __init__.py
│       ├── main.py
│       ├── config.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── user.py
│       ├── services/
│       │   ├── __init__.py
│       │   └── user_service.py
│       └── utils/
│           ├── __init__.py
│           └── helpers.py
│
├── tests/                   # 測試目錄
│   ├── __init__.py
│   ├── conftest.py         # pytest 配置
│   ├── unit/
│   ├── integration/
│   └── fixtures/
│
├── docs/                    # 文件目錄
│   ├── index.md
│   ├── api.md
│   └── user_guide.md
│
├── scripts/                 # 腳本目錄
│   ├── deploy.sh
│   └── backup.py
│
└── data/                    # 資料目錄
    ├── raw/
    ├── processed/
    └── external/
```

##### 套件化專案結構（現代 pyproject.toml 方式）

> ℹ️ **說明**：Python 專案現在推薦使用 `pyproject.toml`（PEP 621）來管理專案設定，取代傳統的 `setup.py`。

```toml
# pyproject.toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my-python-project"
version = "0.1.0"
description = "A sample Python project"
readme = "README.md"
license = "MIT"
requires-python = ">=3.13"
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
]
dependencies = [
    "httpx>=0.28",
]

# 選用功能：使用者以 pip install my-python-project[redis] 取得
[project.optional-dependencies]
redis = ["redis>=5.2"]

# PEP 735 依賴群組：開發期專用，不會發布也不會被下游安裝
[dependency-groups]
dev = [
    "pytest>=8.3",
    "pytest-cov>=6.0",
    "ruff>=0.8",
    "mypy>=1.14",
    "pip-audit>=2.7",
]
docs = [
    "sphinx>=8.1",
    "sphinx-rtd-theme>=3.0",
]

[project.scripts]
myproject = "myproject.main:main"

[project.urls]
Homepage = "https://github.com/yourusername/my-python-project"
Repository = "https://github.com/yourusername/my-python-project"

[tool.uv]
# 預設同步哪些依賴群組
default-groups = ["dev"]

[tool.ruff]
line-length = 88
target-version = "py314"

[tool.ruff.lint]
select = ["E", "W", "F", "I", "UP", "B", "SIM", "S"]

[tool.ruff.lint.per-file-ignores]
"tests/**/*.py" = ["S101"]

[tool.mypy]
python_version = "3.14"
strict = true

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "--cov=src --cov-report=term-missing --strict-markers"
```

**為什麼是 hatchling 而非 setuptools？**
`setuptools` 仍可正常使用，但 `hatchling` 對 src-layout 零設定、不需要 `[tool.setuptools.packages.find]`，且是 PyPA 官方教學採用的建置後端。既有使用 `setuptools` 的專案不需要為此遷移。

> 📝 **傳統 setup.py 方式**（舊專案參考）：
> 若需支援較舊的建置工具，仍可保留 `setup.py`，但新專案應一律採用 `pyproject.toml`。
> 注意 `setup.py install` 已被移除，安裝一律改用 `pip install .`。

##### 配置管理

```python
# src/myproject/config.py
import os
from dataclasses import dataclass, field

@dataclass
class DatabaseConfig:
    host: str = "localhost"
    port: int = 5432
    username: str = "user"
    password: str = "password"
    database: str = "mydb"

@dataclass
class AppConfig:
    debug: bool = False
    secret_key: str = "default-secret-key"
    log_level: str = "INFO"
    # 必須用 default_factory；直接寫 DatabaseConfig() 會拋出
    # ValueError: mutable default ... for field database is not allowed
    database: DatabaseConfig = field(default_factory=DatabaseConfig)

def load_config() -> AppConfig:
    """從環境變數載入配置"""
    config = AppConfig()
    
    # 基本設定
    config.debug = os.getenv("DEBUG", "False").lower() == "true"
    config.secret_key = os.getenv("SECRET_KEY", config.secret_key)
    config.log_level = os.getenv("LOG_LEVEL", config.log_level)
    
    # 資料庫設定
    config.database.host = os.getenv("DB_HOST", config.database.host)
    config.database.port = int(os.getenv("DB_PORT", config.database.port))
    config.database.username = os.getenv("DB_USERNAME", config.database.username)
    config.database.password = os.getenv("DB_PASSWORD", config.database.password)
    config.database.database = os.getenv("DB_DATABASE", config.database.database)
    
    return config

# 使用範例
config = load_config()
```

#### 3.2.2 版本控制最佳實務

##### Git 工作流程

```bash
# 專案初始化
git init
git remote add origin https://github.com/username/project.git

# 分支策略
git checkout -b develop          # 開發分支
git checkout -b feature/user-auth # 功能分支
git checkout -b hotfix/bug-fix   # 修復分支

# 提交訊息規範
git commit -m "feat: 新增用戶認證功能"
git commit -m "fix: 修復密碼驗證錯誤"
git commit -m "docs: 更新 API 文件"
git commit -m "test: 新增用戶服務測試"
git commit -m "refactor: 重構資料庫連接邏輯"
```

##### .gitignore 檔案

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual Environment
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Database
*.db
*.sqlite3

# Environment Variables
.env
.env.local
.env.production

# Logs
logs/
*.log

# Cache
.cache/
.pytest_cache/

# Coverage
htmlcov/
.coverage
.coverage.*
coverage.xml

# OS
.DS_Store
Thumbs.db
```

##### Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-merge-conflict
      - id: check-yaml
      - id: check-json
      - id: check-added-large-files

  # Ruff 一次取代 black + flake8 + isort
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.8.6
    hooks:
      - id: ruff              # 檢查
        args: [--fix]
      - id: ruff-format       # 格式化

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.14.1
    hooks:
      - id: mypy
        additional_dependencies: [types-requests]

  # 阻擋密鑰意外提交，見 3.4.3
  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.5.0
    hooks:
      - id: detect-secrets
```

```bash
# 安裝 hooks（只需執行一次）
uv run pre-commit install

# 對既有程式碼全面套用
uv run pre-commit run --all-files

# 定期更新 hook 版本
uv run pre-commit autoupdate
```

#### 3.2.3 持續整合與部署

##### GitHub Actions 配置

```yaml
# .github/workflows/ci.yml
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
      fail-fast: false
      matrix:
        # 只保留仍在支援期內的版本；3.15 先行驗證相容性
        python-version: ['3.13', '3.14', '3.15']

    steps:
    - uses: actions/checkout@v4

    - name: Install uv
      uses: astral-sh/setup-uv@v5
      with:
        enable-cache: true

    - name: Set up Python ${{ matrix.python-version }}
      run: uv python install ${{ matrix.python-version }}

    - name: Install dependencies
      # --frozen 確保完全依照鎖檔安裝，CI 不會意外升級依賴
      run: uv sync --frozen --group dev

    - name: Lint with Ruff
      run: |
        uv run ruff check --output-format=github .
        uv run ruff format --check .

    - name: Type check with mypy
      run: uv run mypy src

    - name: Test with pytest
      run: uv run pytest tests/ --cov=src --cov-report=xml

    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v5
      with:
        files: ./coverage.xml

  security:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: astral-sh/setup-uv@v5

    # 掃描相依套件的已知弱點，見 3.4.1
    - name: Audit dependencies
      run: uvx pip-audit --strict

    # Ruff 的 S 規則集（bandit），見 3.4.2
    - name: Static security analysis
      run: uvx ruff check --select S .

  deploy:
    needs: [test, security]
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'

    steps:
    - uses: actions/checkout@v4

    - name: Deploy to production
      run: |
        echo "部署到生產環境"
        # 這裡添加實際的部署步驟
```

##### Docker 容器化

以 uv 進行多階段建置：建置階段安裝依賴，執行階段只複製結果，映像更小且不含建置工具。

```dockerfile
# Dockerfile
# ---------- 建置階段 ----------
FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim AS builder

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

# 先只複製依賴宣告，讓 Docker 層快取在原始碼變動時仍可重用
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

# 再複製原始碼並安裝專案本身
COPY src/ ./src/
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# ---------- 執行階段 ----------
FROM python:3.14-slim-bookworm

WORKDIR /app

# 建立非 root 用戶
RUN useradd --create-home --shell /bin/bash app

# 只複製建好的虛擬環境與原始碼，不帶入建置工具
COPY --from=builder --chown=app:app /app/.venv /app/.venv
COPY --from=builder --chown=app:app /app/src /app/src

USER app

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# 健康檢查（使用標準函式庫，不必為此多裝套件）
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"

CMD ["python", "-m", "myproject.main"]
```

```yaml
# docker-compose.yml
# 注意：Compose Specification 已不需要 version 欄位，新版會忽略並發出警告

services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
      - DB_HOST=db
      - DB_PORT=5432
      - DB_USERNAME=myuser
      - DB_PASSWORD=mypassword
      - DB_DATABASE=mydb
    depends_on:
      - db
    volumes:
      - ./logs:/app/logs

  db:
    image: postgres:13
    environment:
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
      POSTGRES_DB: mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  redis:
    image: redis:6-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

#### 3.2.4 專案文件撰寫

##### README.md 範本

````markdown
# My Python Project

[![CI/CD](https://github.com/username/project/workflows/CI/badge.svg)](https://github.com/username/project/actions)
[![codecov](https://codecov.io/gh/username/project/branch/main/graph/badge.svg)](https://codecov.io/gh/username/project)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

## 專案簡介

這是一個 Python 專案的說明...

## 功能特色

- ✨ 功能 1
- 🚀 功能 2
- 🔒 功能 3

## 安裝說明

### 環境需求

- Python 3.13+
- Git
- [uv](https://docs.astral.sh/uv/)（建議）

### 安裝步驟

1. 克隆專案
   ```bash
   git clone https://github.com/username/project.git
   cd project
   ```

2. 建立環境並安裝依賴
   ```bash
   # 使用 uv（推薦）：依鎖檔還原完全一致的環境
   uv sync

   # 或使用標準工具
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -e ".[dev]"
   ```

4. 設定環境變數
   ```bash
   cp .env.example .env
   # 編輯 .env 檔案
   ```

5. 執行專案
   ```bash
   python -m myproject.main
   ```

## 使用說明

### 基本用法

```python
from myproject import MyClass

instance = MyClass()
result = instance.do_something()
```

### API 參考

詳見 [API 文件](docs/api.md)

## 開發指南

### 開發環境設定

```bash
pip install -r requirements-dev.txt
pre-commit install
```

### 執行測試

```bash
pytest
```

### 程式碼檢查

```bash
flake8 src tests
mypy src
black src tests
```

## 貢獻指南

1. Fork 專案
2. 建立功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交變更 (`git commit -m 'Add amazing feature'`)
4. 推送分支 (`git push origin feature/amazing-feature`)
5. 開啟 Pull Request

## 授權

此專案採用 MIT 授權 - 詳見 [LICENSE](LICENSE) 檔案

## 聯絡資訊

- 作者：Your Name
- Email：your.email@example.com
- 專案連結：https://github.com/username/project
````

##### API 文件範例

````markdown
# API 文件

## 用戶模組

### 用戶類別

```python
class User:
    """用戶類別
    
    Attributes:
        id (int): 用戶ID
        username (str): 用戶名稱
        email (str): 電子郵件
    """
    
    def __init__(self, username: str, email: str):
        """初始化用戶
        
        Args:
            username: 用戶名稱
            email: 電子郵件
            
        Raises:
            ValueError: 當用戶名稱或郵件格式無效時
        """
```

### 函式說明

#### authenticate_user()

認證用戶身份

**參數：**
- `username` (str): 用戶名稱
- `password` (str): 密碼

**回傳值：**
- `User | None`: 認證成功回傳用戶物件，失敗回傳 None

**範例：**
```python
user = authenticate_user("john", "password123")
if user:
    print(f"歡迎 {user.username}")
```
````

#### 💡 實務案例

**完整專案範例：**

```python
# src/myproject/main.py
import logging
import sys
from pathlib import Path

from .config import load_config
from .services.user_service import UserService
from .utils.logger import setup_logging

def main():
    """主程式入口"""
    try:
        # 載入配置
        config = load_config()
        
        # 設定日誌
        setup_logging(config.log_level)
        logger = logging.getLogger(__name__)
        
        logger.info("應用程式啟動")
        
        # 初始化服務
        user_service = UserService(config.database)
        
        # 主要業務邏輯
        result = user_service.get_all_users()
        logger.info(f"找到 {len(result)} 個用戶")
        
    except Exception as e:
        logging.error(f"應用程式錯誤: {e}")
        sys.exit(1)
    
    logging.info("應用程式正常結束")

if __name__ == "__main__":
    main()
```

#### ⚠️ 注意事項

1. **版本控制**：遵循語義化版本規範 (Semantic Versioning)
2. **安全性**：不要在程式碼中硬編碼敏感資訊
3. **效能**：定期進行效能測試和優化
4. **相容性**：支援多個 Python 版本時要注意相容性

#### 📝 小測驗

1. 為什麼要使用虛擬環境？
2. 什麼是持續整合 (CI)？
3. Docker 的主要優點是什麼？
4. `.gitignore` 檔案的作用是什麼？
5. 如何撰寫好的提交訊息？

**參考答案：**

1. 隔離專案依賴，避免版本衝突
2. 自動執行測試和建置的過程，確保程式碼品質
3. 環境一致性、可移植性、資源隔離
4. 告訴 Git 哪些檔案不需要版本控制
5. 簡潔明確，使用動詞開頭，說明變更的目的

#### 🏷️ 認證考試對應

- **PCEP**: 不涉及（專案管理超出範圍）
- **PCAP**: 模組 2 - 模組和套件（部分相關）

---

### 3.3 團隊協作工具

#### 🎯 學習目標

- 掌握協作開發工具的使用
- 學習程式碼審查的最佳實務
- 了解專案管理工具的應用
- 建立有效的溝通協作機制

#### 3.3.1 程式碼審查 (Code Review)

##### Pull Request 流程

```markdown
## Pull Request 範本

### 變更說明
簡要描述此次變更的目的和內容

### 變更類型
- [ ] 新功能 (feature)
- [ ] 錯誤修復 (bugfix)
- [ ] 文件更新 (docs)
- [ ] 程式碼重構 (refactor)
- [ ] 效能優化 (performance)
- [ ] 測試更新 (test)

### 測試
- [ ] 已添加單元測試
- [ ] 已執行現有測試
- [ ] 手動測試已完成

### 檢查清單
- [ ] 程式碼符合專案風格指南
- [ ] 已更新相關文件
- [ ] 沒有破壞性變更
- [ ] 已考慮向後相容性

### 相關議題
關閉 #123, #456

### 截圖 (如適用)
<!-- 添加截圖或 GIF 展示變更效果 -->

### 額外資訊
<!-- 任何審查者需要知道的額外資訊 -->
```

##### 程式碼審查指南

```python
# 良好的程式碼審查實務

class CodeReviewGuidelines:
    """程式碼審查指導原則"""
    
    def review_checklist(self):
        """審查檢查清單"""
        return [
            "程式碼邏輯是否正確？",
            "是否有潛在的錯誤或安全問題？",
            "程式碼是否易於理解和維護？",
            "變數命名是否有意義？",
            "函式是否單一職責？",
            "是否有足夠的測試覆蓋？",
            "效能是否有問題？",
            "是否遵循專案風格指南？"
        ]
    
    def comment_examples(self):
        """審查評論範例"""
        return {
            "建設性建議": [
                "考慮使用 `dict.get()` 來避免 KeyError",
                "這個函式有點長，可以考慮拆分",
                "建議添加類型提示以提高可讀性"
            ],
            "讚美回饋": [
                "很好的錯誤處理實作！",
                "這個測試案例很全面",
                "程式碼結構很清晰"
            ],
            "問題詢問": [
                "這裡為什麼選擇使用遞迴？",
                "這個快取策略的依據是什麼？",
                "能否解釋一下這個演算法的時間複雜度？"
            ]
        }

# 範例：審查意見回應
def handle_review_feedback():
    """處理審查回饋的方法"""
    steps = [
        "仔細閱讀所有評論",
        "對於問題給出清楚解釋",
        "根據建議修改程式碼",
        "感謝審查者的時間和建議",
        "推送更新並通知審查者"
    ]
    return steps
```

#### 3.3.2 專案管理工具

##### GitHub Issues 管理

```markdown
<!-- Issue 範本 -->

## 錯誤報告

### 問題描述
清楚簡潔地描述遇到的問題

### 重現步驟
1. 前往 '...'
2. 點擊 '...'
3. 向下滾動到 '...'
4. 看到錯誤

### 預期行為
描述您預期應該發生什麼

### 實際行為
描述實際發生了什麼

### 環境資訊
- OS: [例如 Windows 10]
- Python 版本: [例如 3.9.0]
- 專案版本: [例如 1.2.3]

### 額外內容
添加任何其他有助於解釋問題的內容，如截圖、日誌等
```

##### 專案看板管理

```python
# 使用 GitHub Projects API 自動化專案管理

import requests
from datetime import datetime, timedelta

class ProjectManager:
    """專案管理工具"""
    
    def __init__(self, token, repo_owner, repo_name):
        self.token = token
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }
    
    def create_issue(self, title, body, labels=None, assignee=None):
        """建立新議題"""
        url = f'https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/issues'
        data = {
            'title': title,
            'body': body,
            'labels': labels or [],
            'assignee': assignee
        }
        
        response = requests.post(url, json=data, headers=self.headers)
        return response.json() if response.status_code == 201 else None
    
    def get_sprint_issues(self, sprint_label='sprint-current'):
        """取得當前衝刺的議題"""
        url = f'https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/issues'
        params = {
            'labels': sprint_label,
            'state': 'all',
            'per_page': 100
        }
        
        response = requests.get(url, params=params, headers=self.headers)
        return response.json() if response.status_code == 200 else []
    
    def generate_sprint_report(self):
        """產生衝刺報告"""
        issues = self.get_sprint_issues()
        
        completed = [i for i in issues if i['state'] == 'closed']
        in_progress = [i for i in issues if i['state'] == 'open' and 'in-progress' in [l['name'] for l in i['labels']]]
        backlog = [i for i in issues if i['state'] == 'open' and 'in-progress' not in [l['name'] for l in i['labels']]]
        
        report = f"""
# 衝刺報告 ({datetime.now().strftime('%Y-%m-%d')})

## 統計資訊
- 總議題數: {len(issues)}
- 已完成: {len(completed)} ({len(completed)/len(issues)*100:.1f}%)
- 進行中: {len(in_progress)}
- 待處理: {len(backlog)}

## 已完成議題
{chr(10).join([f"- #{i['number']} {i['title']}" for i in completed])}

## 進行中議題
{chr(10).join([f"- #{i['number']} {i['title']}" for i in in_progress])}
        """
        
        return report
```

#### 3.3.3 溝通協作工具

##### 文件協作

```python
# 使用 Sphinx 自動產生文件

# docs/conf.py
import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------
project = 'My Python Project'
copyright = '2024, Your Name'
author = 'Your Name'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
language = 'zh_TW'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------
# autodoc
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# napoleon
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
```

```restructuredtext
.. docs/index.rst

Welcome to My Python Project's documentation!
=============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   quickstart
   api/modules
   contributing
   changelog

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

##### 團隊溝通規範

```markdown
# 團隊溝通指南

## 會議規範

### 每日站會 (Daily Standup)
- **時間**: 每工作日上午 9:00
- **時長**: 15 分鐘
- **形式**: 線上會議
- **內容**:
  - 昨天完成了什麼？
  - 今天計劃做什麼？
  - 遇到什麼阻礙？

### 衝刺規劃會議 (Sprint Planning)
- **時間**: 每兩週一次
- **時長**: 2 小時
- **參與者**: 全體開發團隊
- **目標**: 規劃下個衝刺的工作內容

### 回顧會議 (Retrospective)
- **時間**: 每個衝刺結束後
- **時長**: 1 小時
- **目標**: 改善團隊工作流程

## 通訊工具使用

### Slack / Discord 頻道分工
- `#general`: 一般討論
- `#development`: 技術討論
- `#code-review`: 程式碼審查通知
- `#deployment`: 部署相關
- `#random`: 非工作相關聊天

### 訊息撰寫原則
- 使用明確的主旨
- 重要訊息使用 @here 或 @channel
- 程式碼片段使用代碼塊格式
- 長篇討論移至專用頻道

## 知識分享

### 技術分享會
- **頻率**: 每月一次
- **時長**: 30-45 分鐘
- **形式**: 團隊成員輪流分享
- **主題**: 新技術、最佳實務、專案經驗

### 文件撰寫標準
- 使用 Markdown 格式
- 包含目錄和索引
- 添加程式碼範例
- 定期更新內容
```

#### 3.3.4 自動化工具

##### GitHub Actions 工作流程

```yaml
# .github/workflows/auto-assign.yml
name: Auto Assign

on:
  pull_request:
    types: [opened]

jobs:
  assign-author:
    runs-on: ubuntu-latest
    steps:
      - name: Assign PR to author
        uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.addAssignees({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number,
              assignees: [context.payload.pull_request.user.login]
            });

      - name: Add labels
        uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.addLabels({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number,
              labels: ['needs-review']
            });
```

##### 自動化腳本

```python
#!/usr/bin/env python3
# scripts/daily_report.py

import os
import sys
import requests
from datetime import datetime, timedelta
from collections import defaultdict

def generate_daily_report():
    """產生每日開發報告"""
    
    # 獲取昨天的提交
    yesterday = datetime.now() - timedelta(days=1)
    commits = get_commits_since(yesterday)
    
    # 獲取已關閉的 Issues
    closed_issues = get_closed_issues_since(yesterday)
    
    # 獲取新的 Pull Requests
    new_prs = get_new_pull_requests_since(yesterday)
    
    # 產生報告
    report = f"""
# 每日開發報告 ({yesterday.strftime('%Y-%m-%d')})

## 程式碼提交
總提交數: {len(commits)}

{format_commits(commits)}

## 已解決議題
總議題數: {len(closed_issues)}

{format_issues(closed_issues)}

## 新的 Pull Requests
總 PR 數: {len(new_prs)}

{format_pull_requests(new_prs)}

## 下一步行動
- 審查待處理的 PR
- 跟進阻塞的議題
- 準備下週衝刺規劃
    """
    
    # 發送到 Slack
    send_to_slack(report)
    
    return report

def send_to_slack(message):
    """發送訊息到 Slack"""
    webhook_url = os.getenv('SLACK_WEBHOOK_URL')
    if not webhook_url:
        print("未設定 Slack Webhook URL")
        return
    
    payload = {
        'text': message,
        'channel': '#development',
        'username': 'Daily Report Bot'
    }
    
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 200:
        print(f"發送 Slack 訊息失敗: {response.status_code}")

if __name__ == "__main__":
    report = generate_daily_report()
    print(report)
```

#### 💡 實務案例

**完整協作工作流程：**

```python
# 團隊協作工作流程自動化

class TeamCollaborationWorkflow:
    """團隊協作工作流程管理"""
    
    def __init__(self, config):
        self.config = config
        self.github_api = GitHubAPI(config.github_token)
        self.slack_api = SlackAPI(config.slack_token)
    
    def handle_pr_opened(self, pr_data):
        """處理新 PR 建立事件"""
        # 1. 自動指派審查者
        reviewers = self.select_reviewers(pr_data)
        self.github_api.assign_reviewers(pr_data['number'], reviewers)
        
        # 2. 添加標籤
        labels = self.determine_labels(pr_data)
        self.github_api.add_labels(pr_data['number'], labels)
        
        # 3. 通知 Slack
        message = f"新的 PR: {pr_data['title']} by {pr_data['user']['login']}"
        self.slack_api.send_message('#code-review', message)
    
    def handle_pr_approved(self, pr_data):
        """處理 PR 通過審查事件"""
        # 1. 檢查是否可以合併
        if self.can_auto_merge(pr_data):
            self.github_api.merge_pr(pr_data['number'])
            
        # 2. 更新專案看板
        self.update_project_board(pr_data, 'Done')
        
        # 3. 通知作者
        message = f"您的 PR #{pr_data['number']} 已通過審查並合併"
        self.slack_api.send_dm(pr_data['user']['login'], message)
    
    def generate_team_metrics(self):
        """產生團隊效能指標"""
        metrics = {
            'pr_merge_time': self.calculate_average_merge_time(),
            'code_review_turnaround': self.calculate_review_time(),
            'bug_resolution_time': self.calculate_bug_resolution_time(),
            'team_velocity': self.calculate_sprint_velocity()
        }
        
        return self.format_metrics_report(metrics)
```

#### ⚠️ 注意事項

1. **權限管理**：確保 API 金鑰和存取權限的安全性
2. **通知頻率**：避免過度通知造成資訊疲勞
3. **工具整合**：選擇適合團隊規模的工具組合
4. **流程標準化**：建立清楚的工作流程和規範

#### 📝 小測驗

1. 程式碼審查的主要目的是什麼？
2. Pull Request 應該包含哪些資訊？
3. 什麼是每日站會 (Daily Standup)？
4. GitHub Actions 的主要用途是什麼？
5. 如何選擇適合的團隊溝通工具？

**參考答案：**

1. 提高程式碼品質、知識分享、發現潛在問題
2. 變更說明、測試資訊、相關議題、檢查清單
3. 每日短時間會議，同步團隊進度和解決阻礙
4. 自動化 CI/CD 流程、測試、部署等任務
5. 考慮團隊規模、溝通需求、預算、整合能力

#### 🏷️ 認證考試對應

- **PCEP**: 不涉及（團隊協作超出範圍）
- **PCAP**: 不涉及（團隊協作超出範圍）

---

### 3.4 安全性與供應鏈管理

#### 🎯 學習目標

- 建立相依套件的弱點掃描機制
- 以靜態分析在提交前攔截安全問題
- 正確管理密鑰與敏感設定
- 透過鎖檔、SBOM 與 Trusted Publishing 確保供應鏈完整性
- 辨識並避免 Python 特有的安全陷阱

> 現代 Python 應用的攻擊面，多數不在自己寫的程式碼，而在**數百個遞移依賴**與**CI/CD 憑證**上。本節聚焦於這兩處。

#### 3.4.1 相依套件弱點掃描

一個典型的 Python 專案會間接引入數十至數百個套件，任何一個出現 CVE 都會影響整個應用。

##### pip-audit

PyPA 官方維護的弱點掃描工具，比對 PyPI Advisory Database 與 OSV 資料庫：

```bash
# 以 uvx 免安裝執行
uvx pip-audit

# 掃描目前環境
uv run pip-audit

# 掃描鎖檔而非已安裝環境（CI 建議做法，不需先建環境）
uvx pip-audit -r pylock.toml

# 發現任何弱點即失敗，用於 CI 閘門
uvx pip-audit --strict

# 嘗試自動升級到已修補的版本
uvx pip-audit --fix
```

##### 分層防護策略

| 層級 | 工具 | 時機 |
| --- | --- | --- |
| 開發者本機 | `pre-commit` + pip-audit | 提交前 |
| Pull Request | CI 中的 `pip-audit --strict` | 每次 PR |
| 持續監控 | GitHub Dependabot / Renovate | 每日自動掃描並開 PR |
| 定期稽核 | SBOM 比對 | 每季 |

```yaml
# .github/dependabot.yml — 讓 Dependabot 自動監控並提出升級 PR
version: 2
updates:
  - package-ecosystem: "uv"
    directory: "/"
    schedule:
      interval: "weekly"
    groups:
      # 把修補版更新合併成單一 PR，減少雜訊
      patch-updates:
        update-types: ["patch"]
```

> **實務建議**：不要對所有弱點一律阻擋。先依 CVSS 分數與「是否位於實際執行路徑上」分級，否則開發團隊會很快學會忽略警告。

#### 3.4.2 靜態安全分析

##### Ruff 的 S 規則集

Ruff 已內建 bandit 的規則（`S` 前綴），不需要額外安裝工具：

```bash
uvx ruff check --select S .
```

```toml
[tool.ruff.lint]
select = ["E", "F", "S"]

[tool.ruff.lint.per-file-ignores]
# 測試檔案中的 assert 是正常寫法，不應觸發 S101
"tests/**/*.py" = ["S101"]
```

常見的 `S` 規則：

| 規則 | 問題 |
| --- | --- |
| S101 | 使用 `assert`（最佳化模式 `-O` 下會被移除，不可用於安全檢查） |
| S105／S106 | 疑似硬編碼的密碼 |
| S301 | 使用 `pickle` 反序列化不可信資料 |
| S307 | 使用 `eval` |
| S324 | 使用不安全的雜湊演算法（MD5、SHA1） |
| S501 | 停用 TLS 憑證驗證（`verify=False`） |
| S602／S605 | 以 `shell=True` 執行子行程 |
| S608 | 以字串拼接組出 SQL |

##### Bandit（獨立工具）

需要更詳盡的報告格式或 Ruff 尚未覆蓋的規則時：

```bash
uvx bandit -r src/ -f json -o bandit-report.json

# 只回報中等以上嚴重度與信心度
uvx bandit -r src/ -ll -ii
```

#### 3.4.3 密鑰與設定管理

##### 基本原則

1. **密鑰絕不進入原始碼與版本控制**——包括註解、測試資料與 Jupyter notebook 的輸出。
2. **以環境變數注入**，不同環境使用不同的值。
3. **提交 `.env.example` 而非 `.env`**，讓新成員知道需要哪些變數，但不洩漏實際值。

```python
# src/myproject/settings.py
import os
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """以 pydantic-settings 讀取並驗證環境變數"""
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="forbid",       # 出現未宣告的變數即報錯，避免拼字錯誤被忽略
    )

    database_url: str
    secret_key: str = Field(min_length=32)
    debug: bool = False

settings = Settings()   # 缺少必填變數時，啟動即失敗而非執行到一半才爆
```

> **為什麼要在啟動時驗證？** 設定錯誤應該讓程式立刻無法啟動（fail fast），而不是在半夜的尖峰時段才因為某個沒設到的變數而出錯。

##### .gitignore 必備項目

```gitignore
# 密鑰與憑證，絕不可提交
.env
.env.*
!.env.example
*.pem
*.key
credentials.json
secrets.yaml
```

##### 提交前攔截

```yaml
# .pre-commit-config.yaml 片段
  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.5.0
    hooks:
      - id: detect-secrets
        args: ['--baseline', '.secrets.baseline']
```

```bash
# 建立基線：記錄已知的誤判，之後只對新出現的密鑰告警
uvx detect-secrets scan > .secrets.baseline
```

> **密鑰一旦外洩就視為已失效**。從 Git 歷史中移除並不足夠——歷史可能已被複製、被搜尋引擎索引。**正確的處置順序是：先輪換金鑰，再清理歷史。**

#### 3.4.4 供應鏈完整性

##### 以鎖檔與雜湊驗證防範套件被竄改

鎖檔記錄的不只是版本，還有每個發行檔的雜湊值。安裝時若雜湊不符即中止，可防範套件在傳輸途中或於 registry 上被替換：

```bash
# uv 預設驗證鎖檔中的雜湊
uv sync --frozen

# pip 的對應做法
pip install --require-hashes -r requirements.txt
```

##### 依賴混淆與惡意套件

| 攻擊手法 | 說明 | 防範 |
| --- | --- | --- |
| Typosquatting | 註冊 `reqeusts`、`python-dateutil` 等近似名稱 | 從官方文件複製套件名，不要手打 |
| 依賴混淆 | 在公開 PyPI 註冊與內部私有套件同名的套件，讓解析器優先取得公開版本 | 為內部套件加上組織前綴；設定 `--index-strategy unsafe-best-match` 以外的嚴格來源策略 |
| 帳號接管 | 維護者帳號被入侵後發布惡意版本 | 鎖檔 + 升級前檢視 changelog；啟用 Dependabot 的升級 PR 審查 |

```toml
# 明確指定索引來源，避免內部套件被公開同名套件取代
[[tool.uv.index]]
name = "internal"
url = "https://pypi.internal.example.com/simple"
explicit = true            # 只有明確指定的套件才從此來源取得

[tool.uv.sources]
my-internal-lib = { index = "internal" }
```

##### SBOM（軟體物料清單）

企業採購與資安稽核日益要求提供 SBOM，列出軟體的完整成分：

```bash
# 產生 CycloneDX 格式的 SBOM
uvx cyclonedx-py environment -o sbom.json

# 由鎖檔產生（不需建立環境）
uvx cyclonedx-py requirements pylock.toml -o sbom.json
```

##### Trusted Publishing

發布套件時不使用長期 API token，改以 GitHub Actions 的 OIDC 身分向 PyPI 驗證。token 不存在，就不會外洩。設定方式見 [1.4.3 套件管理](#143-套件管理)。

| 做法 | 風險 |
| --- | --- |
| 在 CI Secrets 存放 PyPI API token | token 長期有效，一旦外洩可持續發布惡意版本 |
| **Trusted Publishing（OIDC）** | 憑證在單次工作流程中產生且短時效，無長期機密可竊取 |

#### 3.4.5 常見 Python 安全陷阱

##### 反序列化

```python
import pickle
import json

# 危險：pickle 可在反序列化時執行任意程式碼
data = pickle.loads(untrusted_bytes)        # 等同執行對方提供的程式

# 安全：對不可信來源使用 JSON
data = json.loads(untrusted_string)
```

```python
import yaml

# 危險：yaml.load 預設可具現化任意 Python 物件
config = yaml.load(user_input, Loader=yaml.Loader)

# 安全：safe_load 只處理基本型別
config = yaml.safe_load(user_input)
```

##### 動態執行

```python
# 危險：即使有過濾，eval 的沙箱化實務上無法做對
result = eval(user_expression)

# 安全：對數學運算使用 ast.literal_eval，或專用的運算式解析器
import ast
result = ast.literal_eval(user_expression)   # 只接受字面值，不執行程式
```

##### 子行程注入

```python
import subprocess

# 危險：shell=True 加上字串拼接 → 命令注入
subprocess.run(f"ping {user_host}", shell=True)
# user_host = "example.com; rm -rf /" 會被一併執行

# 安全：以引數串列傳遞，不經過 shell
subprocess.run(["ping", "-c", "4", user_host], check=True)
```

##### SQL 注入

```python
# 危險：字串拼接
cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")

# 安全：參數化查詢，由驅動程式負責跳脫
cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
```

Python 3.14 的 t-string（PEP 750）讓「安全的字串組裝」有了語言層級的支援——模板保留了「哪些是靜態文字、哪些是使用者輸入」的結構資訊，處理函式因此能對插值部分強制跳脫，而 f-string 在求值當下就已經失去這項資訊：

```python
from string.templatelib import Template, Interpolation

def safe_sql(template: Template) -> tuple[str, list]:
    """把 t-string 轉為參數化查詢，插值一律變成佔位符"""
    query, params = [], []
    for item in template:
        if isinstance(item, str):
            query.append(item)
        elif isinstance(item, Interpolation):
            query.append("?")
            params.append(item.value)
    return "".join(query), params

# 使用者輸入不可能變成 SQL 語法的一部分
sql, params = safe_sql(t"SELECT * FROM users WHERE name = {name}")
cursor.execute(sql, params)
```

同樣的模式可用於 HTML 跳脫以防範 XSS，範例見 [2.5.4 Python 3.14 新特性](#254-python-314-新特性2025-年-10-月發布)。

##### 路徑穿越

```python
from pathlib import Path

UPLOAD_DIR = Path("/var/app/uploads").resolve()

def save_upload(filename: str, content: bytes) -> None:
    # 危險：filename = "../../etc/passwd" 可寫到任意位置
    # target = UPLOAD_DIR / filename

    # 安全：解析後確認仍在允許的目錄之內
    target = (UPLOAD_DIR / filename).resolve()
    if not target.is_relative_to(UPLOAD_DIR):
        raise ValueError(f"非法的檔案路徑: {filename}")
    target.write_bytes(content)
```

##### 其他重點

| 陷阱 | 正確做法 |
| --- | --- |
| `assert` 用於安全檢查 | `python -O` 會移除所有 assert；安全檢查一律用 `if ... raise` |
| `random` 產生 token | 改用 `secrets.token_urlsafe()` |
| 以 `==` 比對密碼雜湊 | 改用 `secrets.compare_digest()`，避免時序攻擊 |
| `requests.get(url, verify=False)` | 絕不停用 TLS 驗證；憑證有問題應修正憑證 |
| 記錄日誌時輸出完整請求 | 過濾 Authorization 標頭、密碼與個資欄位 |
| MD5／SHA1 儲存密碼 | 改用 `argon2` 或 `bcrypt` 等專為密碼設計的演算法 |

#### 💡 實務案例

**完整的安全檢查 CI 工作流程：**

```yaml
# .github/workflows/security.yml
name: Security

on:
  pull_request:
  schedule:
    - cron: '0 2 * * 1'      # 每週一凌晨全面掃描，捕捉新公布的 CVE

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v5

      - name: 相依套件弱點掃描
        run: uvx pip-audit -r pylock.toml --strict

      - name: 靜態安全分析
        run: uvx ruff check --select S --output-format=github .

      - name: 密鑰掃描（含完整歷史）
        run: |
          uvx detect-secrets scan --baseline .secrets.baseline
          uvx detect-secrets audit --report --fail-on-unaudited .secrets.baseline

      - name: 產生 SBOM
        run: uvx cyclonedx-py requirements pylock.toml -o sbom.json

      - uses: actions/upload-artifact@v4
        with:
          name: sbom
          path: sbom.json
```

#### ⚠️ 注意事項

1. **掃描不等於安全**：工具只能找出已知問題，無法替代威脅建模與程式碼審查。
2. **控制誤報量**：誤報過多會讓團隊養成忽略警告的習慣，比沒有掃描更危險。設好基線並定期整理。
3. **外洩優先輪換**：密鑰外洩時，先輪換再清理歷史，順序不能顛倒。
4. **升級也有風險**：為修補 CVE 而升級可能引入破壞性變更；務必有鎖檔與測試套件才敢升。
5. **供應鏈防護要涵蓋 CI**：CI 憑證與 runner 本身也是攻擊目標，GitHub Actions 建議以完整 SHA 而非標籤釘選第三方 action。

#### 📝 小測驗

1. 為什麼不應該用 `assert` 做安全性檢查？
2. `pickle.loads()` 處理不可信資料有什麼風險？
3. Trusted Publishing 相較於 API token 的安全優勢是什麼？
4. 鎖檔中的雜湊值有什麼安全作用？
5. 比對密碼雜湊時，為什麼要用 `secrets.compare_digest()` 而不是 `==`？

**參考答案：**

1. 以 `-O` 旗標執行時，所有 `assert` 會被編譯器移除，安全檢查將完全失效。
2. `pickle` 在反序列化過程中可具現化任意物件並執行程式碼，等同讓對方在你的程序中執行任意指令。
3. OIDC 憑證僅在單次工作流程中有效且短時效，不存在可被竊取或長期濫用的靜態機密。
4. 安裝時會驗證下載內容的雜湊，若套件在傳輸途中或於 registry 上遭替換即會中止安裝。
5. `==` 在第一個不同的位元組就回傳，比對耗時會洩漏正確前綴的長度，可被時序攻擊利用；`compare_digest()` 為常數時間比對。

#### 🏷️ 認證考試對應

- **PCEP／PCAP**: 不涉及（安全性超出認證範圍）
- **企業實務**：安全與供應鏈管理為企業級交付的必要條件，亦是資安稽核的檢核重點

---

## 4. Python 認證考試指引

### 4.1 PCEP 認證指引

#### 🎯 考試概述

**Python Institute Certified Entry-Level Python Programmer（PCEP-30-02）**

| 項目 | 內容 |
| --- | --- |
| 考試代碼 | PCEP-30-02（官方狀態：ACTIVE） |
| 題目數量 | 30 題 |
| 通過分數 | 各區塊加權後總平均 ≥ 70% |
| 題型 | 單選、複選、程式碼題、情境題、互動題 |
| 考試語言 | 英語 |
| 考試方式 | OpenEDG 線上監考或授權測試中心 |
| 先修條件 | 無 |
| 有效期限 | 終身有效，不需重新認證 |

##### 官方考試配分（Exam Blocks）

| Block | 主題 | 題數 | 配分 |
| --- | --- | --- | --- |
| 1 | Computer Programming and Python Fundamentals | 7 | 18% |
| 2 | Control Flow – Conditional Blocks and Loops | 8 | 29% |
| 3 | Data Collections – Tuples, Dictionaries, Lists, and Strings | 7 | 25% |
| 4 | Functions and Exceptions | 8 | 28% |
| **合計** | | **30** | **100%** |

> **備讀重點**：Block 2 與 Block 4 合計佔 57%，流程控制與函式／例外是分數最集中之處，應優先掌握。
> 資料來源：[PCEP-30-0x Exam Syllabus](https://pythoninstitute.org/pcep-exam-syllabus)（查核日期：2026-09-21）
>
> ⚠️ Python Institute 已將 PCEP-30-02 的改版排程於 2026 年第三季。這屬於例行版本更新而非退場，報考前請至官網確認當下的有效版本代碼與大綱。

#### 4.1.1 考試範圍與重點

##### 模組 1：Python 基礎概念 (18%)

```python
# 重點主題：
# - Python 的特性和應用
# - 解釋器 vs 編譯器
# - Python 語法基礎

# 常見考題範例：
print("Hello", "World")  # 輸出: Hello World
print("Hello" + "World") # 輸出: HelloWorld

# 理解 print() 函式的不同用法
print("A", "B", "C", sep="-")      # A-B-C
print("Line1", end="")
print("Line2")                     # Line1Line2
```

##### 模組 2：資料型態、變數、基本 I/O、運算子 (29%)

```python
# 重點：數值型態轉換
x = "123"
y = int(x)      # 字串轉整數
z = float(x)    # 字串轉浮點數

# 常見陷阱：
print(2 ** 3 ** 2)  # 512 (右結合)
print((2 ** 3) ** 2)  # 64

# 字串操作
text = "Python"
print(text[0])      # P
print(text[-1])     # n
print(text[1:4])    # yth
print(text[::-1])   # nohtyP

# 串列基礎
numbers = [1, 2, 3]
numbers.append(4)   # [1, 2, 3, 4]
numbers.extend([5, 6])  # [1, 2, 3, 4, 5, 6]
```

##### 模組 3：布林值、條件執行、迴圈、串列處理 (29%)

```python
# 布林運算重點
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# 短路評估
def test():
    print("Function called")
    return True

result = False and test()  # test() 不會被呼叫

# 迴圈與 else
for i in range(3):
    print(i)
else:
    print("Loop completed")  # 會執行

for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("Loop completed")  # 不會執行（有 break）

# 串列推導式基礎
squares = [x**2 for x in range(5)]      # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

##### 模組 4：函式、元組、字典、例外處理 (24%)

```python
# 函式參數
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))           # Hello, Alice!
print(greet("Bob", "Hi"))       # Hi, Bob!

# 元組特性
coordinates = (10, 20)
x, y = coordinates  # 解包
# coordinates[0] = 5  # TypeError: 元組不可變

# 字典操作
student = {"name": "John", "age": 20}
print(student.get("grade", "N/A"))  # N/A (預設值)

# 例外處理
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero")
except Exception as e:
    print(f"Other error: {e}")
finally:
    print("Cleanup")
```

#### 4.1.2 PCEP 考試技巧

##### 時間管理

```text
- 平均每題 2.2 分鐘
- 快速回答確定的題目
- 標記不確定的題目，最後回來檢查
- 留 10-15 分鐘檢查
```

##### 常見陷阱

```python
# 1. 變數作用域
def func():
    print(x)  # UnboundLocalError
    x = 10

x = 5
func()

# 正確寫法
def func():
    global x
    print(x)
    x = 10

# 2. 可變預設參數
def add_to_list(item, target=[]):  # 危險！
    target.append(item)
    return target

# 3. 遲評估
funcs = []
for i in range(3):
    funcs.append(lambda: i)  # 都會返回 2

for f in funcs:
    print(f())  # 2 2 2

# 4. 整數除法 vs 浮點除法
print(5 / 2)   # 2.5
print(5 // 2)  # 2
```

### 4.2 PCAP 認證指引

#### 🎯 考試概述

**Python Institute Certified Associate in Python Programming（PCAP-31-03）**

| 項目 | 內容 |
| --- | --- |
| 考試代碼 | PCAP-31-03（官方狀態：ACTIVE） |
| 題目數量 | 40 題 |
| 通過分數 | 各區塊加權後總平均 ≥ 70% |
| 題型 | 單選、複選、程式碼題、情境題、互動題 |
| 計分方式 | 每題最高 40 分，原始分數正規化後以百分比呈現 |
| 先決條件 | 無強制要求，但建議先取得 PCEP |
| 能力定位 | 設計、撰寫、除錯多模組 Python 程式，並運用核心 OOP 技術 |

##### 官方考試配分（Exam Blocks）

| Block | 主題 | 題數 | 配分 |
| --- | --- | --- | --- |
| 1 | Modules and Packages | 6 | 12% |
| 2 | Exceptions | 5 | 14% |
| 3 | Strings | 8 | 18% |
| 4 | Object-Oriented Programming | 12 | 34% |
| 5 | Miscellaneous（List Comprehensions, Lambdas, Closures, I/O） | 9 | 22% |
| **合計** | | **40** | **100%** |

> **備讀重點**：OOP 單獨佔 34%，是 PCAP 的決勝區塊，務必熟練繼承、MRO、特殊方法與封裝。
> 資料來源：[PCAP-31-0x Exam Syllabus](https://pythoninstitute.org/pcap-exam-syllabus)（查核日期：2026-09-21）

#### 4.2.1 考試範圍重點

##### 模組 1：控制和評估、資料聚合 (25%)

```python
# 進階迴圈控制
matrix = [[1, 2], [3, 4], [5, 6]]
for i, row in enumerate(matrix):
    for j, val in enumerate(row):
        print(f"[{i}][{j}] = {val}")

# 生成器表達式
squares_gen = (x**2 for x in range(1000000))  # 記憶體效率高
squares_list = [x**2 for x in range(1000000)]  # 記憶體使用量大

# 字典和集合推導式
word_lengths = {word: len(word) for word in ["hello", "world"]}
unique_chars = {char for char in "hello world" if char.isalpha()}
```

##### 模組 2：模組和套件 (25%)

```python
# 模組匯入方式
import math
from math import pi, sqrt
from math import *  # 匯入所有公開名稱（不建議在正式程式中使用）

# 套件結構理解
# mypackage/
#   __init__.py
#   module1.py
#   subpackage/
#     __init__.py
#     module2.py

# 模組搜尋路徑
import sys
print(sys.path)

# __name__ 的使用
if __name__ == "__main__":
    main()
```

##### 模組 3：物件導向程式設計 (25%)

```python
# 類別和繼承
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} started")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

# 特殊方法
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

# 多重繼承和 MRO
class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")
        super().method()

class C(A):
    def method(self):
        print("C")
        super().method()

class D(B, C):
    def method(self):
        print("D")
        super().method()

# D().method() 的輸出順序？
```

##### 模組 4：雜項 (25%)

```python
# 生成器和迭代器
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib))

# 檔案處理
with open("file.txt", "r") as f:
    content = f.read()

# 上下文管理器
class MyContext:
    def __enter__(self):
        print("Entering")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting")

with MyContext() as ctx:
    print("In context")

# Lambda 和高階函式
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

from functools import reduce
total = reduce(lambda x, y: x + y, numbers)
```

### 4.3 考試準備與技巧

#### 4.3.1 學習路線規劃

##### PCEP 準備時程（8-12 週）

```text
週次 1-2：Python 基礎
- 安裝和環境設置
- 基本語法和資料型態
- 變數和運算子

週次 3-4：控制結構
- 條件判斷
- 迴圈結構
- 例外處理基礎

週次 5-6：資料結構
- 串列操作
- 字典和元組
- 字串處理

週次 7-8：函式
- 函式定義和呼叫
- 參數處理
- 作用域

週次 9-10：綜合練習
- 模擬考試
- 弱點加強

週次 11-12：考前衝刺
- 最後複習
- 考試技巧練習
```

##### PCAP 準備時程（12-16 週）

```text
週次 1-4：PCEP 基礎鞏固
- 確保 PCEP 知識點熟練

週次 5-8：進階主題
- 物件導向程式設計
- 模組和套件
- 生成器和迭代器

週次 9-12：實務應用
- 檔案處理
- 例外處理進階
- 設計模式基礎

週次 13-16：考前準備
- 模擬考試
- 重點複習
- 考試策略
```

#### 4.3.2 練習資源

##### 官方資源

```text
1. Python Institute 官網
   - 考試說明書
   - 樣本題目
   - 學習材料

2. Python.org 官方文檔
   - Tutorial
   - Library Reference
   - Language Reference

3. 模擬考試平台
   - Testprep-Online
   - MeasureUp
   - Whizlabs
```

##### 實作練習

```python
# PCEP 練習題範例

# 1. 字串操作
def reverse_words(text):
    """反轉句子中的每個單字"""
    words = text.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

# 測試
print(reverse_words("Hello World"))  # olleH dlroW

# 2. 數學計算
def is_prime(n):
    """檢查是否為質數"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 3. 串列處理
def find_common_elements(list1, list2):
    """找出兩個串列的共同元素"""
    return list(set(list1) & set(list2))

# PCAP 練習題範例

# 1. 物件導向設計
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
        self._transactions = []
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transactions.append(f"Deposit: +{amount}")
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._transactions.append(f"Withdraw: -{amount}")
            return True
        return False
    
    @property
    def balance(self):
        return self._balance

# 2. 模組設計練習
# math_utils.py
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
```

#### 4.3.3 考試當天技巧

##### 考前準備

```text
1. 環境檢查
   - 網路連線穩定
   - 攝影機和麥克風正常
   - 身分證件準備

2. 心理準備
   - 充足睡眠
   - 適度運動
   - 避免考前熬夜

3. 物理準備
   - 安靜的考試環境
   - 舒適的座椅
   - 清理桌面
```

##### 答題策略

```text
1. 時間分配
   - PCEP: 30題/65分鐘 ≈ 2分鐘/題
   - PCAP: 40題/65分鐘 ≈ 1.6分鐘/題

2. 答題順序
   - 先答確定的題目
   - 標記困難題目
   - 最後回來檢查

3. 檢查技巧
   - 仔細閱讀題目
   - 注意關鍵字
   - 驗證答案邏輯
```

#### 4.3.4 完整認證階梯

Python Institute（OpenEDG）的認證分為通用程式設計主線與兩條專業旁支。

##### 主線：通用 Python 程式設計

| 層級 | 認證 | 代碼 | 題數 | 能力定位 |
| --- | --- | --- | --- | --- |
| 入門 | PCEP – Certified Entry-Level Python Programmer | PCEP-30-02 | 30 | 語法基礎、流程控制、資料集合、函式與例外 |
| 準專業 | PCAP – Certified Associate in Python Programming | PCAP-31-03 | 40 | 模組與套件、OOP、字串處理、推導式與閉包 |
| 專業 I | PCPP1 – Certified Professional in Python Programming 1 | PCPP-32-1xx | — | 進階 OOP、GUI（tkinter）、檔案處理、PEP 規範、math／os／datetime |
| 專業 II | PCPP2 – Certified Professional in Python Programming 2 | PCPP-32-2xx | — | 程序間通訊、網路程式設計、SQL 資料庫、設計模式、套件製作與測試 |

##### 旁支：領域專業認證

| 認證 | 定位 |
| --- | --- |
| PCED – Certified Entry-Level Data Analyst with Python | 資料分析入門：資料清理、統計基礎、視覺化 |
| PCAD – Certified Associate Data Analyst with Python | 資料分析進階：pandas／NumPy、探索式分析、建模基礎 |

##### 學習路徑建議

```text
                     ┌──────────────────────────────┐
  完全新手 ────────▶ │ PCEP（本手冊第 1 章）        │
                     └──────────────┬───────────────┘
                                    ▼
                     ┌──────────────────────────────┐
  有基礎者起點 ────▶ │ PCAP（本手冊第 2 章）        │
                     └──────────────┬───────────────┘
                                    ▼
                  ┌─────────────────┴─────────────────┐
                  ▼                                   ▼
        ┌───────────────────┐              ┌────────────────────┐
        │ PCPP1 → PCPP2     │              │ PCED → PCAD        │
        │ 通用軟體工程方向  │              │ 資料分析方向       │
        └───────────────────┘              └────────────────────┘
```

> **對企業工程師的務實建議**：PCEP／PCAP 對建立語言基礎與求職履歷有實質幫助；但本手冊第 3 章的工具鏈、測試、CI/CD 與安全供應鏈實務**不在任何認證範圍內**，卻是實際工作中權重最高的能力。認證與實務應並行累積，不要因為「不考」就略過第 3 章。

---

## 5. 檢查清單

### 5.1 環境設置檢查清單

#### Python 環境

- [ ] Python 3.13+ 已安裝（3.12 已進入 security-only、3.9 已 EOL）
- [ ] pip 工具可正常使用
- [ ] 已設定 PATH 環境變數
- [ ] 虛擬環境工具已準備（`venv` 或 uv）
- [ ] 已確認目標版本仍在官方支援期內

#### 開發工具

- [ ] VS Code 或 PyCharm 已安裝
- [ ] Python 與 Pylance 擴充套件已安裝
- [ ] 檢查與格式化工具已就緒（Ruff；舊專案可為 black + flake8）
- [ ] 型別檢查工具已就緒（mypy 或 pyright）
- [ ] 版本控制工具（Git）

#### 套件管理

- [ ] 依賴宣告於 `pyproject.toml`（而非僅有 `requirements.txt`）
- [ ] 開發依賴以 PEP 735 `[dependency-groups]` 區分
- [ ] 鎖檔已產生並提交版控（`uv.lock` 或 `pylock.toml`）
- [ ] 虛擬環境已啟動
- [ ] 必要套件已安裝

### 5.2 程式碼品質檢查清單

#### 程式碼風格

- [ ] 遵循 PEP 8 命名慣例
- [ ] 適當的縮排（4個空格）
- [ ] 行長度不超過 79 字元
- [ ] 匯入語句按標準排序

#### 文件和註解

- [ ] 所有函式都有 docstring
- [ ] 複雜邏輯有適當註解
- [ ] README.md 檔案完整
- [ ] API 文件已建立

#### 錯誤處理

- [ ] 適當的例外處理
- [ ] 輸入驗證完整
- [ ] 錯誤訊息有意義
- [ ] 日誌記錄已實現

### 5.3 專案結構檢查清單

#### 目錄結構

- [ ] 源碼目錄（src/）
- [ ] 測試目錄（tests/）
- [ ] 文件目錄（docs/）
- [ ] 設定檔案分離

#### 檔案組織

- [ ] 模組職責清晰
- [ ] 避免循環匯入
- [ ] `__init__.py` 檔案適當
- [ ] 設定檔案分環境

### 5.4 測試檢查清單

#### 測試覆蓋

- [ ] 單元測試已撰寫
- [ ] 測試覆蓋率 > 80%
- [ ] 邊界條件已測試
- [ ] 錯誤情況已測試

#### 測試品質

- [ ] 測試名稱有意義
- [ ] 測試獨立性
- [ ] 測試資料清理
- [ ] 模擬外部依賴

### 5.5 部署準備檢查清單

#### 環境配置

- [ ] 生產環境設定
- [ ] 敏感資訊加密
- [ ] 環境變數設定
- [ ] 依賴版本鎖定

#### 安全性

- [ ] 輸入驗證完整
- [ ] SQL 注入防護
- [ ] 權限控制實現
- [ ] 日誌不包含敏感資訊

### 5.6 認證考試檢查清單

#### PCEP 準備

- [ ] Python 基礎語法熟練
- [ ] 資料型態操作熟悉
- [ ] 控制結構理解
- [ ] 函式使用熟練
- [ ] 基本 I/O 操作

#### PCAP 準備

- [ ] 物件導向概念理解
- [ ] 模組和套件使用
- [ ] 進階資料結構
- [ ] 例外處理進階
- [ ] 生成器和迭代器

#### 考試技巧

- [ ] 時間管理策略
- [ ] 模擬考試練習
- [ ] 弱點分析改進
- [ ] 考試環境準備

### 5.7 持續學習檢查清單

#### 技能提升

- [ ] 定期練習編程
- [ ] 閱讀他人程式碼
- [ ] 參與開源專案
- [ ] 學習新的函式庫

#### 社群參與

- [ ] 加入 Python 社群
- [ ] 參加技術聚會
- [ ] 分享學習心得
- [ ] 幫助其他學習者

#### 版本追蹤

- [ ] 已訂閱 [Python Insider](https://blog.python.org/) 掌握發布動態
- [ ] 每年 10 月新版發布後，檢視 What's New 並評估升級
- [ ] CI 中已納入下一個版本的矩陣測試
- [ ] 已確認專案使用的版本尚未接近 EOL

### 5.8 安全與供應鏈檢查清單

#### 相依套件

- [ ] CI 中已加入 `pip-audit --strict` 閘門
- [ ] 已啟用 Dependabot 或 Renovate 自動監控
- [ ] 鎖檔含雜湊值，安裝時以 `uv sync --frozen` 驗證
- [ ] 內部套件已設定明確的索引來源，可防依賴混淆

#### 程式碼

- [ ] Ruff 已啟用 `S` 規則集（bandit）
- [ ] 無 `pickle`／`yaml.load`／`eval` 處理不可信輸入
- [ ] 子行程呼叫一律使用引數串列，未使用 `shell=True` 拼接
- [ ] SQL 全面採用參數化查詢
- [ ] 檔案路徑已做 `is_relative_to()` 邊界檢查
- [ ] 安全檢查未使用 `assert`（`-O` 下會被移除）

#### 密鑰

- [ ] `.env` 已列入 `.gitignore`，僅提交 `.env.example`
- [ ] pre-commit 已啟用 detect-secrets
- [ ] 設定於應用啟動時驗證，缺漏即 fail fast
- [ ] 日誌輸出已過濾憑證與個資欄位
- [ ] 密碼雜湊使用 argon2／bcrypt，比對使用 `secrets.compare_digest()`

#### 發布與稽核

- [ ] PyPI 發布已改用 Trusted Publishing（OIDC），CI 中無長期 token
- [ ] 可依需求產生 CycloneDX 格式 SBOM
- [ ] 第三方 GitHub Action 已以完整 SHA 釘選
- [ ] 已建立密鑰外洩的輪換程序（先輪換、再清歷史）

---

## 結語

這份 Python 程式語言教學手冊涵蓋了從基礎入門到認證考試的完整學習路徑。記住，程式設計是一門實務技能，需要持續的練習和應用。

**學習建議：**

1. **循序漸進**：按照手冊章節順序學習，確保基礎紮實
2. **動手實作**：每個範例都要親自練習，理論與實務並重
3. **專案實務**：將所學應用到實際專案中
4. **持續改進**：定期檢視和重構自己的程式碼
5. **社群學習**：與其他開發者交流，分享經驗

**下一步行動：**

- 設定開發環境並開始第一個 Python 程式
- 制定個人學習計畫和時程
- 加入 Python 學習社群
- 規劃認證考試時間表

Python 的學習之路沒有終點，只有不斷的成長和進步。祝您在 Python 程式設計的道路上取得成功！

### 官方參考資源

| 資源 | 用途 |
| --- | --- |
| [Python 官方文件](https://www.python.org/doc/) | 語言參考、標準函式庫、教學 |
| [Getting Started](https://www.python.org/about/gettingstarted/) | 初學者入門指引與資源彙整 |
| [What's New in Python](https://docs.python.org/3/whatsnew/) | 各版本新特性與不相容變更 |
| [Status of Python versions](https://devguide.python.org/versions/) | 版本生命週期與 EOL 時程 |
| [PEP Index](https://peps.python.org/) | 所有語言提案的權威來源 |
| [Python Packaging User Guide](https://packaging.python.org/) | 打包、發布與依賴管理的官方指南 |
| [PyPI](https://pypi.org/) | 套件索引與搜尋 |
| [Python Institute](https://pythoninstitute.org/) | PCEP／PCAP／PCPP 認證大綱與報考 |

---

*本教學手冊由專業講師團隊編撰，定期更新以確保內容的準確性和實用性。如有建議或問題，歡迎回饋討論。*
*版本 2.0 — 最後更新 2026 年 9 月，內容查核基準日 2026-09-21。*
