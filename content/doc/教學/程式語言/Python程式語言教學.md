# Python 程式語言教學手冊

## 目錄

1. [Python 基礎入門](#1-python-基礎入門)
   - 1.1 [Python 安裝與環境設置](#11-python-安裝與環境設置)
   - 1.2 [語法基礎](#12-語法基礎)
   - 1.3 [流程控制](#13-流程控制)
   - 1.4 [函式、模組與套件管理](#14-函式模組與套件管理)

2. [進階應用](#2-進階應用)
   - 2.1 [面向物件程式設計](#21-面向物件程式設計)
   - 2.2 [檔案處理與例外處理](#22-檔案處理與例外處理)
   - 2.3 [常用標準函式庫](#23-常用標準函式庫)
   - 2.4 [測試與除錯](#24-測試與除錯)

3. [專案實務應用](#3-專案實務應用)
   - 3.1 [程式碼風格與規範](#31-程式碼風格與規範)
   - 3.2 [專案開發實務](#32-專案開發實務)
   - 3.3 [團隊協作工具](#33-團隊協作工具)

4. [Python 認證考試指引](#4-python-認證考試指引)
   - 4.1 [PCEP 認證指引](#41-pcep-認證指引)
   - 4.2 [PCAP 認證指引](#42-pcap-認證指引)
   - 4.3 [考試準備與技巧](#43-考試準備與技巧)

5. [檢查清單](#5-檢查清單)

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

#### 1.1.2 Windows 系統安裝

##### 步驟 1：下載 Python
1. 前往 [Python 官網](https://www.python.org/downloads/)
2. 下載最新的穩定版本（建議 Python 3.9 以上）
3. 選擇 Windows x86-64 executable installer

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

1. **Visual Studio Code**
   ```bash
   # 推薦擴充套件
   - Python (Microsoft)
   - Python Docstring Generator
   - Python Indent
   - Pylance
   ```

2. **PyCharm Community Edition**
   - 功能完整的 Python IDE
   - 內建除錯器和測試工具

#### 1.1.5 虛擬環境管理

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

#### 💡 實務案例

**專案目錄結構範例：**
```
my_python_project/
│
├── venv/                   # 虛擬環境
├── src/                    # 原始碼
│   ├── __init__.py
│   ├── main.py
│   └── utils/
├── tests/                  # 測試檔案
├── docs/                   # 文件
├── requirements.txt        # 依賴清單
├── README.md              # 專案說明
└── .gitignore             # Git 忽略檔案
```

#### ⚠️ 注意事項

1. **版本相容性**：建議使用 Python 3.9 以上版本
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

# 搜尋套件
pip search keyword
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
requests==2.28.1
numpy>=1.21.0
pandas==1.5.2
matplotlib==3.6.2
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
from typing import Optional, List, Dict, Any

# 設定日誌
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def safe_divide(a: float, b: float) -> Optional[float]:
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

def process_user_data(user_data: Dict[str, Any]) -> bool:
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
```
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
```
my_python_project/
│
├── README.md                 # 專案說明文件
├── requirements.txt          # 依賴清單
├── setup.py                  # 安裝腳本
├── .gitignore               # Git 忽略檔案
├── .env.example             # 環境變數範例
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

##### 套件化專案結構
```python
# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip()]

setup(
    name="my-python-project",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A sample Python project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my-python-project",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.910",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=0.5",
        ],
    },
    entry_points={
        "console_scripts": [
            "myproject=myproject.main:main",
        ],
    },
)
```

##### 配置管理
```python
# src/myproject/config.py
import os
from dataclasses import dataclass
from typing import Optional

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
    database: DatabaseConfig = DatabaseConfig()

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
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-merge-conflict
      - id: check-yaml
      - id: check-json

  - repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
      - id: black
        language_version: python3

  - repo: https://github.com/pycqa/flake8
    rev: 5.0.4
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v0.991
    hooks:
      - id: mypy
        additional_dependencies: [types-requests]
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
      matrix:
        python-version: [3.8, 3.9, '3.10']

    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-dev.txt
    
    - name: Lint with flake8
      run: |
        flake8 src tests --count --select=E9,F63,F7,F82 --show-source --statistics
        flake8 src tests --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    
    - name: Type check with mypy
      run: mypy src
    
    - name: Test with pytest
      run: |
        pytest tests/ --cov=src --cov-report=xml
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Deploy to production
      run: |
        echo "部署到生產環境"
        # 這裡添加實際的部署步驟
```

##### Docker 容器化
```dockerfile
# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# 安裝系統依賴
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 複製依賴檔案
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製源碼
COPY src/ ./src/
COPY tests/ ./tests/

# 建立非 root 用戶
RUN useradd --create-home --shell /bin/bash app
USER app

# 設定環境變數
ENV PYTHONPATH=/app/src
ENV PYTHONUNBUFFERED=1

# 健康檢查
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/health')"

# 啟動命令
CMD ["python", "-m", "myproject.main"]
```

```yaml
# docker-compose.yml
version: '3.8'

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
```markdown
# My Python Project

[![CI/CD](https://github.com/username/project/workflows/CI/badge.svg)](https://github.com/username/project/actions)
[![codecov](https://codecov.io/gh/username/project/branch/main/graph/badge.svg)](https://codecov.io/gh/username/project)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## 專案簡介

這是一個 Python 專案的說明...

## 功能特色

- ✨ 功能 1
- 🚀 功能 2
- 🔒 功能 3

## 安裝說明

### 環境需求

- Python 3.8+
- Git

### 安裝步驟

1. 克隆專案
   ```bash
   git clone https://github.com/username/project.git
   cd project
   ```

2. 建立虛擬環境
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. 安裝依賴
   ```bash
   pip install -r requirements.txt
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
```

##### API 文件範例
```markdown
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
```

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

## 4. Python 認證考試指引

### 4.1 PCEP 認證指引

#### 🎯 考試概述
**Python Institute Certified Entry-Level Python Programmer (PCEP)**
- 考試時間：65 分鐘
- 題目數量：30 題
- 通過分數：70%
- 考試語言：英語
- 考試方式：線上監考或測試中心

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
```
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
**Python Institute Certified Associate in Python Programming (PCAP)**
- 考試時間：65 分鐘
- 題目數量：40 題
- 通過分數：70%
- 先決條件：建議先取得 PCEP

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
from math import * as math_all

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
```
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
```
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
```
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
```
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
```
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

---

## 5. 檢查清單

### 5.1 環境設置檢查清單

#### Python 環境
- [ ] Python 3.9+ 已安裝
- [ ] pip 工具可正常使用
- [ ] 已設定 PATH 環境變數
- [ ] 虛擬環境工具已準備

#### 開發工具
- [ ] VS Code 或 PyCharm 已安裝
- [ ] Python 擴充套件已安裝
- [ ] 程式碼格式化工具（black, flake8）
- [ ] 版本控制工具（Git）

#### 套件管理
- [ ] requirements.txt 檔案建立
- [ ] 虛擬環境已啟動
- [ ] 必要套件已安裝
- [ ] 開發依賴已區分

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

---

*本教學手冊由專業講師團隊編撰，定期更新以確保內容的準確性和實用性。如有建議或問題，歡迎回饋討論。*
