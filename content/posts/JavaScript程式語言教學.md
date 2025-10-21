+++
date = '2025-10-21T16:17:51+08:00'
draft = false
title = 'JavaScript程式語言教學'
tags = ['教學','程式語言' ,'JavaScript']
categories = ['技術']
author = 'Eric Cheng'
summary = '提供完整JavaScript程式語言教學'
+++



# JavaScript 程式語言教學手冊

## 文件資訊

- **版本**: 1.0
- **更新日期**: 2025年8月29日
- **適用對象**: 新進前端開發同仁
- **專案架構**: 前後端分離 (Vue 3.x / React / Angular)

---

## 目錄

1. [JavaScript 基本概念](#1-javascript-基本概念)
   - 1.1 [語言特性](#11-語言特性)
   - 1.2 [基礎資料型別與運算子](#12-基礎資料型別與運算子)
   - 1.3 [變數與作用域](#13-變數與作用域)
   - 1.4 [函式與閉包](#14-函式與閉包)
   - 1.5 [物件與原型鏈](#15-物件與原型鏈)
   - 1.6 [ES6+ 常用語法](#16-es6-常用語法)
   - 1.7 [實務注意事項](#17-實務注意事項)

2. [程式開發規範](#2-程式開發規範)
   - 2.1 [程式碼風格指南](#21-程式碼風格指南)
   - 2.2 [ESLint 和 Prettier 設定](#22-eslint-和-prettier-設定)
   - 2.3 [專案中常用的 Utility Functions](#23-專案中常用的-utility-functions)

3. [專案中常見應用範例](#3-專案中常見應用範例)
   - 3.1 [DOM 操作與事件處理](#31-dom-操作與事件處理)
   - 3.2 [非同步處理](#32-非同步處理-promise-asyncawait-fetch-api)
   - 3.3 [與後端 API 溝通](#33-與後端-api-溝通-restful-api-呼叫範例)
   - 3.4 [錯誤處理與例外狀況處理](#34-錯誤處理與例外狀況處理)
   - 3.5 [Web APIs 應用](#35-web-apis-應用)
   - 3.6 [專案最佳實務](#36-專案最佳實務)
   - 3.7 [測試與除錯](#37-測試與除錯)

4. [現代開發工具與 TypeScript](#4-現代開發工具與-typescript)
   - 4.1 [TypeScript 基礎](#41-typescript-基礎)
   - 4.2 [建置工具](#42-建置工具)

5. [學習資源與進階閱讀](#5-學習資源與進階閱讀)
   - 5.1 [官方文件與標準](#51-官方文件與標準)
   - 5.2 [推薦學習資源](#52-推薦學習資源)
   - 5.3 [實務工具與框架](#53-實務工具與框架)
   - 5.4 [社群與資源](#54-社群與資源)
   - 5.5 [持續學習建議](#55-持續學習建議)

6. [開發檢查清單](#6-開發檢查清單)
   - 6.1 [程式碼品質檢查](#61-程式碼品質檢查)
   - 6.2 [安全性檢查](#62-安全性檢查)
   - 6.3 [API 整合檢查](#63-api-整合檢查)
   - 6.4 [使用者體驗檢查](#64-使用者體驗檢查)
   - 6.5 [測試檢查](#65-測試檢查)
   - 6.6 [部署前檢查](#66-部署前檢查)
   - 6.7 [維護檢查](#67-維護檢查)

---

## 1. JavaScript 基本概念

### 1.1 語言特性

JavaScript 是一種動態、弱型別的直譯式程式語言，具有以下核心特性：

#### 1.1.1 動態型別

- 變數型別在執行時期決定
- 同一變數可存放不同型別的值
- 不需要明確宣告變數型別

```javascript
// 動態型別範例
let value = 42;        // number
value = "Hello";       // string
value = true;          // boolean
value = { name: "John" }; // object
```

#### 1.1.2 事件驅動

- 程式執行基於事件觸發
- 支援非同步事件處理
- 常用於使用者互動回應

```javascript
// 事件驅動範例
document.getElementById('submitBtn').addEventListener('click', function(event) {
    console.log('按鈕被點擊了');
    // 處理點擊事件的邏輯
});

// 自定義事件
const customEvent = new CustomEvent('dataLoaded', {
    detail: { message: '資料載入完成' }
});
```

#### 1.1.3 非同步處理

- 支援非阻塞式程式執行
- 使用 Promise、async/await 處理非同步操作
- 避免介面凍結問題

```javascript
// 非同步處理範例
async function fetchUserData(userId) {
    try {
        const response = await fetch(`/api/users/${userId}`);
        const userData = await response.json();
        return userData;
    } catch (error) {
        console.error('取得使用者資料失敗:', error);
        throw error;
    }
}
```

### 1.2 基礎資料型別與運算子

JavaScript 有八種基本資料型別，分為原始型別（Primitive Types）和物件型別（Object Types）。

#### 1.2.1 原始資料型別

```javascript
// ✅ 原始資料型別範例

// 1. Number - 數字型別
let age = 25;
let price = 99.99;
let infinity = Infinity;
let notANumber = NaN;

console.log(typeof age);        // "number"
console.log(Number.isNaN(notANumber)); // true
console.log(Number.isFinite(infinity)); // false

// 2. String - 字串型別
let name = "Alice";
let greeting = 'Hello World';
let template = `Hello, ${name}!`;

console.log(typeof name);       // "string"
console.log(template);          // "Hello, Alice!"

// 3. Boolean - 布林型別
let isActive = true;
let isComplete = false;

console.log(typeof isActive);   // "boolean"

// 4. undefined - 未定義
let uninitializedVar;
console.log(uninitializedVar);  // undefined
console.log(typeof uninitializedVar); // "undefined"

// 5. null - 空值
let emptyValue = null;
console.log(emptyValue);        // null
console.log(typeof emptyValue); // "object" (這是 JavaScript 的已知 bug)

// 6. Symbol - 符號型別 (ES6+)
let symbol1 = Symbol('id');
let symbol2 = Symbol('id');
console.log(symbol1 === symbol2); // false (每個 Symbol 都是唯一的)

// 7. BigInt - 大整數型別 (ES2020+)
let bigNumber = 9007199254740991n;
let anotherBig = BigInt(9007199254740991);
console.log(typeof bigNumber);  // "bigint"
```

#### 1.2.2 物件型別

```javascript
// ✅ 物件型別範例

// 1. Object - 物件
let person = {
    name: "John",
    age: 30,
    isStudent: false
};

// 2. Array - 陣列
let numbers = [1, 2, 3, 4, 5];
let mixedArray = [1, "hello", true, null];

// 3. Function - 函式
function greet(name) {
    return `Hello, ${name}!`;
}

// 4. Date - 日期
let now = new Date();
let specificDate = new Date('2024-01-01');

console.log(typeof person);     // "object"
console.log(typeof numbers);    // "object"
console.log(typeof greet);      // "function"
console.log(typeof now);        // "object"

// 檢查陣列
console.log(Array.isArray(numbers)); // true
console.log(Array.isArray(person));  // false
```

#### 1.2.3 型別轉換

```javascript
// ✅ 隱式型別轉換
console.log("5" + 3);       // "53" (字串拼接)
console.log("5" - 3);       // 2 (數字運算)
console.log("5" * "2");     // 10 (數字運算)
console.log(true + 1);      // 2 (布林轉數字)
console.log(false + 1);     // 1

// ✅ 明式型別轉換
// 轉為字串
let num = 123;
let str1 = String(num);        // "123"
let str2 = num.toString();     // "123"
let str3 = `${num}`;          // "123"

// 轉為數字
let str = "123";
let num1 = Number(str);        // 123
let num2 = parseInt(str);      // 123
let num3 = parseFloat("123.45"); // 123.45
let num4 = +str;              // 123 (一元運算子)

// 轉為布林
let bool1 = Boolean(1);        // true
let bool2 = Boolean(0);        // false
let bool3 = Boolean("");       // false
let bool4 = Boolean("hello");  // true
let bool5 = !!str;            // true (雙重否定)

// ✅ 假值 (Falsy Values)
const falsyValues = [
    false,
    0,
    -0,
    0n,
    "",
    null,
    undefined,
    NaN
];

falsyValues.forEach(value => {
    console.log(`${value} 是假值:`, !value);
});
```

#### 1.2.4 運算子

```javascript
// ✅ 算術運算子
let a = 10, b = 3;

console.log(a + b);    // 13 (加法)
console.log(a - b);    // 7 (減法)
console.log(a * b);    // 30 (乘法)
console.log(a / b);    // 3.333... (除法)
console.log(a % b);    // 1 (餘數)
console.log(a ** b);   // 1000 (指數運算，ES2016+)

// 遞增遞減
let count = 5;
console.log(++count);  // 6 (前置遞增)
console.log(count++);  // 6 (後置遞增，先回傳再遞增)
console.log(count);    // 7

// ✅ 比較運算子
console.log(5 == "5");   // true (寬鬆相等，會型別轉換)
console.log(5 === "5");  // false (嚴格相等，不會型別轉換)
console.log(5 != "5");   // false
console.log(5 !== "5");  // true

console.log(10 > 5);     // true
console.log(10 >= 10);   // true
console.log(5 < 3);      // false

// ✅ 邏輯運算子
let x = true, y = false;

console.log(x && y);     // false (邏輯 AND)
console.log(x || y);     // true (邏輯 OR)
console.log(!x);         // false (邏輯 NOT)

// 短路求值
let result1 = true || console.log("不會執行"); // true
let result2 = false && console.log("不會執行"); // false

// ✅ 賦值運算子
let num = 10;
num += 5;  // num = num + 5; (15)
num -= 3;  // num = num - 3; (12)
num *= 2;  // num = num * 2; (24)
num /= 4;  // num = num / 4; (6)
num %= 4;  // num = num % 4; (2)

// ✅ ES2020+ 新運算子
// 空值合併運算子 (Nullish Coalescing)
let config = {
    theme: null,
    language: "zh-TW"
};

let theme = config.theme ?? "light";        // "light"
let language = config.language ?? "en-US";  // "zh-TW"

// 可選鏈運算子 (Optional Chaining)
let user = {
    profile: {
        name: "Alice"
    }
};

console.log(user.profile?.name);        // "Alice"
console.log(user.profile?.email);       // undefined
console.log(user.settings?.theme);      // undefined (不會報錯)

// 邏輯賦值運算子 (ES2021+)
let settings = {};
settings.theme ||= "dark";               // 如果為假值才賦值
settings.notifications ??= true;        // 如果為 null/undefined 才賦值
settings.debug &&= false;               // 如果為真值才賦值
```

#### 1.2.5 資料型別檢查最佳實務

```javascript
// ✅ 型別檢查工具函式
const TypeChecker = {
    // 精確的型別檢查
    getType(value) {
        return Object.prototype.toString.call(value).slice(8, -1).toLowerCase();
    },
    
    // 檢查是否為指定型別
    isType(value, type) {
        return this.getType(value) === type.toLowerCase();
    },
    
    // 常用型別檢查
    isString(value) { return typeof value === 'string'; },
    isNumber(value) { return typeof value === 'number' && !isNaN(value); },
    isBoolean(value) { return typeof value === 'boolean'; },
    isFunction(value) { return typeof value === 'function'; },
    isObject(value) { return value !== null && typeof value === 'object' && !Array.isArray(value); },
    isArray(value) { return Array.isArray(value); },
    isNull(value) { return value === null; },
    isUndefined(value) { return value === undefined; },
    isNullOrUndefined(value) { return value == null; },
    
    // 檢查是否為空
    isEmpty(value) {
        if (value == null) return true;
        if (typeof value === 'string') return value.length === 0;
        if (Array.isArray(value)) return value.length === 0;
        if (typeof value === 'object') return Object.keys(value).length === 0;
        return false;
    }
};

// 使用範例
console.log(TypeChecker.getType([]));           // "array"
console.log(TypeChecker.getType(new Date()));   // "date"
console.log(TypeChecker.isString("hello"));     // true
console.log(TypeChecker.isEmpty({}));           // true
console.log(TypeChecker.isEmpty([]));           // true
console.log(TypeChecker.isEmpty(""));           // true
```

### 1.3 變數與作用域

#### 1.3.1 變數宣告方式

```javascript
// ✅ var、let、const 的差異

// 1. var - 函式作用域，可以重複宣告，有提升特性
function varExample() {
    console.log(x); // undefined (不是錯誤，因為提升)
    
    if (true) {
        var x = 1;
        var x = 2; // 可以重複宣告
    }
    
    console.log(x); // 2 (函式作用域，不受區塊限制)
}

// 2. let - 區塊作用域，不可重複宣告，有暫時性死區
function letExample() {
    // console.log(y); // ReferenceError: 暫時性死區
    
    if (true) {
        let y = 1;
        // let y = 2; // SyntaxError: 不可重複宣告
        y = 3; // 可以重新賦值
    }
    
    // console.log(y); // ReferenceError: 區塊作用域
}

// 3. const - 區塊作用域，不可重複宣告，不可重新賦值
function constExample() {
    const z = 1;
    // z = 2; // TypeError: 不可重新賦值
    
    // 但物件內容可以修改
    const obj = { name: "Alice" };
    obj.name = "Bob"; // 可以修改物件屬性
    obj.age = 30;     // 可以新增屬性
    
    // obj = {}; // TypeError: 不可重新賦值整個物件
}
```

#### 1.3.2 作用域類型

```javascript
// ✅ 全域作用域
var globalVar = "我是全域變數";
let globalLet = "我也是全域變數";

function showGlobal() {
    console.log(globalVar); // 可以存取
    console.log(globalLet); // 可以存取
}

// ✅ 函式作用域
function functionScope() {
    var functionVar = "函式作用域變數";
    let functionLet = "函式作用域變數";
    
    function innerFunction() {
        console.log(functionVar); // 可以存取外層函式變數
        console.log(functionLet); // 可以存取外層函式變數
    }
    
    innerFunction();
}

// console.log(functionVar); // ReferenceError: 函式外無法存取

// ✅ 區塊作用域
function blockScope() {
    if (true) {
        var blockVar = "var 沒有區塊作用域";
        let blockLet = "let 有區塊作用域";
        const blockConst = "const 有區塊作用域";
    }
    
    console.log(blockVar);    // "var 沒有區塊作用域"
    // console.log(blockLet);    // ReferenceError
    // console.log(blockConst);  // ReferenceError
}

// ✅ 模組作用域 (ES6 Modules)
// moduleA.js
export const moduleVar = "模組變數";
export function moduleFunction() {
    const privateVar = "私有變數"; // 只在此模組內可見
    return privateVar;
}

// moduleB.js
// import { moduleVar } from './moduleA.js';
// console.log(moduleVar); // 可以存取匯出的變數
```

#### 1.3.3 變數提升 (Hoisting)

```javascript
// ✅ var 提升範例
console.log(hoistedVar); // undefined (不是錯誤)
var hoistedVar = "我被提升了";

// 實際執行等同於：
/*
var hoistedVar; // 宣告被提升
console.log(hoistedVar); // undefined
hoistedVar = "我被提升了"; // 賦值留在原位
*/

// ✅ 函式提升
console.log(hoistedFunction()); // "我是被提升的函式"

function hoistedFunction() {
    return "我是被提升的函式";
}

// 函式表達式不會被提升
// console.log(notHoisted()); // TypeError: notHoisted is not a function
var notHoisted = function() {
    return "我不會被提升";
};

// ✅ let 和 const 的暫時性死區
function temporalDeadZone() {
    // console.log(letVar); // ReferenceError: 暫時性死區
    // console.log(constVar); // ReferenceError: 暫時性死區
    
    let letVar = "let 變數";
    const constVar = "const 變數";
    
    console.log(letVar);   // "let 變數"
    console.log(constVar); // "const 變數"
}
```

### 1.4 函式與閉包

#### 1.4.1 函式定義方式

```javascript
// ✅ 函式宣告 (Function Declaration)
function declarationFunction(param) {
    return `宣告函式: ${param}`;
}

// ✅ 函式表達式 (Function Expression)
const expressionFunction = function(param) {
    return `表達式函式: ${param}`;
};

// ✅ 箭頭函式 (Arrow Function)
const arrowFunction = (param) => `箭頭函式: ${param}`;

// 簡化寫法
const simpleArrow = param => param * 2;
const multipleParams = (a, b) => a + b;
const noParams = () => "沒有參數";

// ✅ 建構函式
function ConstructorFunction(name) {
    this.name = name;
    this.greet = function() {
        return `Hello, ${this.name}`;
    };
}

const instance = new ConstructorFunction("Alice");

// ✅ 方法定義 (ES6+)
const obj = {
    // 傳統方法
    traditionalMethod: function() {
        return "傳統方法";
    },
    
    // ES6 簡化語法
    modernMethod() {
        return "現代方法";
    },
    
    // 箭頭函式方法 (注意 this 綁定)
    arrowMethod: () => "箭頭方法"
};
```

#### 1.4.2 函式參數

```javascript
// ✅ 預設參數 (ES6+)
function greet(name = "World", greeting = "Hello") {
    return `${greeting}, ${name}!`;
}

console.log(greet());                    // "Hello, World!"
console.log(greet("Alice"));             // "Hello, Alice!"
console.log(greet("Bob", "Hi"));         // "Hi, Bob!"

// ✅ 其餘參數 (Rest Parameters)
function sum(...numbers) {
    return numbers.reduce((total, num) => total + num, 0);
}

console.log(sum(1, 2, 3, 4, 5)); // 15

function processUser(name, age, ...hobbies) {
    return {
        name,
        age,
        hobbies
    };
}

console.log(processUser("Alice", 25, "reading", "coding", "gaming"));

// ✅ 展開語法 (Spread Syntax)
const numbers = [1, 2, 3];
console.log(Math.max(...numbers)); // 等同於 Math.max(1, 2, 3)

function multiply(a, b, c) {
    return a * b * c;
}

console.log(multiply(...numbers)); // 6

// ✅ 解構參數
function createUser({ name, email, age = 18 }) {
    return {
        id: Date.now(),
        name,
        email,
        age,
        createdAt: new Date()
    };
}

const userData = createUser({
    name: "Alice",
    email: "alice@example.com"
});
```

#### 1.4.3 閉包 (Closures)

```javascript
// ✅ 基本閉包範例
function outerFunction(x) {
    // 外層函式的變數
    
    function innerFunction(y) {
        // 內層函式可以存取外層函式的變數
        return x + y;
    }
    
    return innerFunction;
}

const addFive = outerFunction(5);
console.log(addFive(3)); // 8

// ✅ 實用的閉包應用 - 私有變數
function createCounter() {
    let count = 0; // 私有變數
    
    return {
        increment() {
            count++;
            return count;
        },
        
        decrement() {
            count--;
            return count;
        },
        
        getCount() {
            return count;
        },
        
        reset() {
            count = 0;
            return count;
        }
    };
}

const counter = createCounter();
console.log(counter.increment()); // 1
console.log(counter.increment()); // 2
console.log(counter.getCount());  // 2
console.log(counter.reset());     // 0

// ✅ 閉包與迴圈的常見陷阱
// 錯誤範例
function createFunctionsWrong() {
    const functions = [];
    
    for (var i = 0; i < 3; i++) {
        functions.push(function() {
            return i; // 所有函式都會回傳 3
        });
    }
    
    return functions;
}

// 正確範例 1: 使用 let
function createFunctionsCorrect1() {
    const functions = [];
    
    for (let i = 0; i < 3; i++) {
        functions.push(function() {
            return i; // 每個函式都會回傳正確的值
        });
    }
    
    return functions;
}

// 正確範例 2: 使用 IIFE
function createFunctionsCorrect2() {
    const functions = [];
    
    for (var i = 0; i < 3; i++) {
        functions.push((function(index) {
            return function() {
                return index;
            };
        })(i));
    }
    
    return functions;
}

// ✅ 模組模式 (Module Pattern)
const UserModule = (function() {
    // 私有變數和函式
    const users = [];
    let nextId = 1;
    
    function generateId() {
        return nextId++;
    }
    
    function validateUser(user) {
        return user.name && user.email;
    }
    
    // 公開的 API
    return {
        addUser(user) {
            if (validateUser(user)) {
                user.id = generateId();
                users.push(user);
                return user;
            }
            throw new Error("無效的使用者資料");
        },
        
        getUser(id) {
            return users.find(user => user.id === id);
        },
        
        getAllUsers() {
            return [...users]; // 回傳複本，防止外部修改
        },
        
        getUserCount() {
            return users.length;
        }
    };
})();

// 使用模組
const user1 = UserModule.addUser({ name: "Alice", email: "alice@example.com" });
console.log(UserModule.getUserCount()); // 1
```

### 1.5 物件與原型鏈

#### 1.5.1 物件建立方式

```javascript
// ✅ 物件字面值 (Object Literal)
const person1 = {
    name: "Alice",
    age: 30,
    greet() {
        return `Hello, I'm ${this.name}`;
    }
};

// ✅ Object.create()
const personPrototype = {
    greet() {
        return `Hello, I'm ${this.name}`;
    }
};

const person2 = Object.create(personPrototype);
person2.name = "Bob";
person2.age = 25;

// ✅ 建構函式
function Person(name, age) {
    this.name = name;
    this.age = age;
}

Person.prototype.greet = function() {
    return `Hello, I'm ${this.name}`;
};

const person3 = new Person("Charlie", 35);

// ✅ ES6 類別語法
class PersonClass {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    
    greet() {
        return `Hello, I'm ${this.name}`;
    }
    
    static getSpecies() {
        return "Homo sapiens";
    }
}

const person4 = new PersonClass("Diana", 28);
```

#### 1.5.2 原型鏈 (Prototype Chain)

```javascript
// ✅ 理解原型鏈
function Animal(name) {
    this.name = name;
}

Animal.prototype.speak = function() {
    return `${this.name} makes a sound`;
};

function Dog(name, breed) {
    Animal.call(this, name); // 呼叫父建構函式
    this.breed = breed;
}

// 設定原型鏈
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

Dog.prototype.bark = function() {
    return `${this.name} barks!`;
};

Dog.prototype.speak = function() {
    return `${this.name} barks loudly!`;
};

const dog = new Dog("Buddy", "Golden Retriever");

console.log(dog.speak());    // "Buddy barks loudly!"
console.log(dog.bark());     // "Buddy barks!"
console.log(dog.name);       // "Buddy"

// 檢查原型鏈
console.log(dog instanceof Dog);     // true
console.log(dog instanceof Animal);  // true
console.log(dog instanceof Object);  // true

// ✅ ES6 類別繼承
class AnimalClass {
    constructor(name) {
        this.name = name;
    }
    
    speak() {
        return `${this.name} makes a sound`;
    }
}

class DogClass extends AnimalClass {
    constructor(name, breed) {
        super(name); // 呼叫父類別建構函式
        this.breed = breed;
    }
    
    speak() {
        return `${this.name} barks loudly!`;
    }
    
    bark() {
        return `${this.name} barks!`;
    }
}

const dogClass = new DogClass("Max", "Labrador");
```

#### 1.5.3 物件屬性與方法

```javascript
// ✅ 屬性描述符
const obj = {};

Object.defineProperty(obj, 'name', {
    value: 'Alice',
    writable: true,      // 可以修改值
    enumerable: true,    // 可以被列舉
    configurable: true   // 可以被刪除或修改描述符
});

Object.defineProperty(obj, 'secret', {
    value: 'top secret',
    writable: false,     // 不可修改
    enumerable: false,   // 不會出現在 for...in 中
    configurable: false  // 不可刪除
});

// ✅ Getter 和 Setter
const user = {
    _age: 0,
    
    get age() {
        return this._age;
    },
    
    set age(value) {
        if (value < 0 || value > 150) {
            throw new Error("年齡必須在 0-150 之間");
        }
        this._age = value;
    },
    
    get isAdult() {
        return this._age >= 18;
    }
};

user.age = 25;
console.log(user.age);      // 25
console.log(user.isAdult);  // true

// ✅ 物件方法
const userManager = {
    users: [],
    
    addUser(user) {
        this.users.push(user);
    },
    
    findUser(id) {
        return this.users.find(user => user.id === id);
    },
    
    removeUser(id) {
        const index = this.users.findIndex(user => user.id === id);
        if (index !== -1) {
            return this.users.splice(index, 1)[0];
        }
        return null;
    }
};

// ✅ 物件解構和展開
const original = {
    name: "Alice",
    age: 30,
    city: "Taipei",
    hobbies: ["reading", "coding"]
};

// 解構
const { name, age, ...rest } = original;

// 展開
const updated = {
    ...original,
    age: 31,
    country: "Taiwan"
};

// 深拷貝 vs 淺拷貝
const shallowCopy = { ...original };
const deepCopy = JSON.parse(JSON.stringify(original));

// 修改原始物件的陣列
original.hobbies.push("gaming");

console.log(shallowCopy.hobbies); // ["reading", "coding", "gaming"]
console.log(deepCopy.hobbies);    // ["reading", "coding"]
```

### 1.6 ES6+ 常用語法

#### 1.2.1 變數宣告 (let/const)

**使用原則:**

- 優先使用 `const` 宣告常數
- 需要重新賦值時使用 `let`
- 避免使用 `var`（具有提升特性且作用域複雜）

```javascript
// ✅ 良好實務
const API_BASE_URL = 'https://api.example.com';
const userConfig = {
    theme: 'dark',
    language: 'zh-TW'
};

let currentPage = 1;
let isLoading = false;

// ❌ 避免使用
var globalVar = 'avoid using var';
```

#### 1.2.2 箭頭函式 (Arrow Functions)

**使用時機:**

- 簡短的函式表達式
- 不需要 `this` 綁定的情況
- 陣列方法的回調函式

```javascript
// ✅ 適合使用箭頭函式
const add = (a, b) => a + b;
const multiply = (a, b) => a * b;

// 陣列處理
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(num => num * 2);
const evens = numbers.filter(num => num % 2 === 0);

// ✅ 多行箭頭函式
const processUser = (user) => {
    const processedUser = {
        ...user,
        fullName: `${user.firstName} ${user.lastName}`,
        isActive: user.status === 'active'
    };
    return processedUser;
};

// ❌ 不適合使用箭頭函式的情況
const userObject = {
    name: 'John',
    // 避免在物件方法中使用箭頭函式
    greet() {
        return `Hello, ${this.name}`;
    }
};
```

#### 1.2.3 模板字串 (Template Literals)

**使用優勢:**

- 支援多行字串
- 變數插值更直觀
- 支援表達式計算

```javascript
// ✅ 模板字串範例
const user = {
    name: 'Alice',
    age: 30,
    department: '前端開發部'
};

// 變數插值
const greeting = `你好，${user.name}！歡迎加入${user.department}。`;

// 多行字串
const emailTemplate = `
親愛的 ${user.name}：

感謝您加入我們的團隊。
您的帳號資訊如下：
- 姓名：${user.name}
- 年齡：${user.age}
- 部門：${user.department}

祝工作順利！
`;

// 表達式計算
const orderSummary = `
訂單總計：${user.age >= 65 ? '優惠價格' : '原價'}
預計送達：${new Date().toLocaleDateString()}
`;
```

#### 1.2.4 解構賦值 (Destructuring)

**物件解構:**

```javascript
// ✅ 物件解構範例
const apiResponse = {
    data: {
        user: {
            id: 1,
            name: 'John Doe',
            email: 'john@example.com',
            profile: {
                avatar: 'avatar.jpg',
                bio: 'Frontend Developer'
            }
        }
    },
    status: 'success',
    message: '資料取得成功'
};

// 基本解構
const { status, message } = apiResponse;

// 嵌套解構
const { data: { user: { name, email } } } = apiResponse;

// 重新命名
const { data: { user: { name: userName } } } = apiResponse;

// 預設值
const { data: { user: { phone = '未提供' } } } = apiResponse;
```

**陣列解構:**

```javascript
// ✅ 陣列解構範例
const coordinates = [120.9738819, 23.9739374];
const [longitude, latitude] = coordinates;

// 跳過元素
const colors = ['red', 'green', 'blue', 'yellow'];
const [primary, , tertiary] = colors; // primary='red', tertiary='blue'

// 其餘元素
const [first, ...rest] = colors; // first='red', rest=['green', 'blue', 'yellow']
```

**函式參數解構:**

```javascript
// ✅ 函式參數解構
function createUser({ name, email, age = 18, department = '未分配' }) {
    return {
        id: Date.now(),
        name,
        email,
        age,
        department,
        createdAt: new Date().toISOString()
    };
}

// 使用方式
const newUser = createUser({
    name: 'Jane Smith',
    email: 'jane@example.com'
});
```

### 1.7 實務注意事項

#### 1.3.1 型別檢查最佳實務

```javascript
// ✅ 型別檢查範例
function processUserInput(input) {
    // 檢查是否為字串
    if (typeof input !== 'string') {
        throw new Error('輸入必須為字串');
    }
    
    // 檢查是否為空字串
    if (input.trim().length === 0) {
        throw new Error('輸入不能為空');
    }
    
    return input.trim().toLowerCase();
}

// 檢查物件屬性
function validateUser(user) {
    const requiredFields = ['name', 'email'];
    
    for (const field of requiredFields) {
        if (!(field in user) || !user[field]) {
            throw new Error(`缺少必要欄位: ${field}`);
        }
    }
    
    return true;
}
```

#### 1.3.2 效能考量

```javascript
// ✅ 避免在迴圈中重複計算
function processItems(items) {
    const itemCount = items.length; // 快取長度
    const results = [];
    
    for (let i = 0; i < itemCount; i++) {
        results.push(processItem(items[i]));
    }
    
    return results;
}

// ✅ 使用適當的資料結構
const userMap = new Map(); // 大量查找操作時比物件更高效
const uniqueValues = new Set(); // 去重操作
```

---

## 2. 程式開發規範

### 2.1 程式碼風格指南

#### 2.1.1 命名規則

**變數和函式命名:**

```javascript
// ✅ 良好的命名範例
const MAX_RETRY_COUNT = 3;           // 常數：大寫蛇形命名
const userAccountBalance = 1000;     // 變數：駝峰命名
let currentPageIndex = 0;           // 變數：駝峰命名

// 函式命名：動詞開頭，描述行為
function calculateTotalPrice(items) { }
function validateEmailFormat(email) { }
function getUserById(id) { }
function updateUserProfile(userId, profile) { }

// 布林值：is/has/can 開頭
const isAuthenticated = true;
const hasPermission = false;
const canEdit = true;

// 事件處理函式：handle 開頭
function handleSubmitClick(event) { }
function handleInputChange(event) { }
```

**類別和建構函式:**

```javascript
// ✅ 類別命名：大寫駝峰命名
class UserManager {
    constructor(apiClient) {
        this.apiClient = apiClient;
        this.cache = new Map();
    }
    
    async fetchUser(userId) {
        // 實作邏輯
    }
}

// 建構函式
function ApiClient(baseUrl) {
    this.baseUrl = baseUrl;
    this.timeout = 5000;
}
```

#### 2.1.2 縮排和格式化

**縮排規則:**

```javascript
// ✅ 使用 2 個空格縮排
if (condition) {
  if (nestedCondition) {
    doSomething();
  }
}

// ✅ 物件和陣列格式化
const userConfig = {
  theme: 'dark',
  language: 'zh-TW',
  notifications: {
    email: true,
    push: false
  }
};

const menuItems = [
  { id: 1, label: '首頁', path: '/' },
  { id: 2, label: '產品', path: '/products' },
  { id: 3, label: '關於我們', path: '/about' }
];
```

**函式格式化:**

```javascript
// ✅ 函式參數換行
function createUserAccount(
  username,
  email,
  password,
  profileData = {},
  options = {}
) {
  // 函式實作
}

// ✅ 鏈式呼叫換行
const processedData = rawData
  .filter(item => item.isActive)
  .map(item => transformItem(item))
  .sort((a, b) => a.priority - b.priority);
```

#### 2.1.3 註解規範

**JSDoc 註解:**

```javascript
/**
 * 計算商品總價格，包含稅金和折扣
 * @param {Array<Object>} items - 商品清單
 * @param {number} items[].price - 商品價格
 * @param {number} items[].quantity - 商品數量
 * @param {number} [taxRate=0.05] - 稅率（預設 5%）
 * @param {number} [discountPercent=0] - 折扣百分比
 * @returns {Object} 計算結果
 * @returns {number} returns.subtotal - 小計
 * @returns {number} returns.tax - 稅金
 * @returns {number} returns.total - 總計
 * @example
 * const items = [
 *   { price: 100, quantity: 2 },
 *   { price: 50, quantity: 1 }
 * ];
 * const result = calculateTotalPrice(items, 0.05, 10);
 * console.log(result.total); // 236.25
 */
function calculateTotalPrice(items, taxRate = 0.05, discountPercent = 0) {
  const subtotal = items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
  const discountAmount = subtotal * (discountPercent / 100);
  const discountedSubtotal = subtotal - discountAmount;
  const tax = discountedSubtotal * taxRate;
  const total = discountedSubtotal + tax;
  
  return {
    subtotal,
    discountAmount,
    tax,
    total
  };
}
```

**一般註解:**

```javascript
// ✅ 解釋複雜邏輯的註解
// 使用防抖機制避免頻繁 API 呼叫
const debouncedSearch = debounce((query) => {
  searchUsers(query);
}, 300);

// TODO: 需要加入快取機制以提升效能
function expensiveCalculation(data) {
  // 實作邏輯
}

// FIXME: 這個函式在某些邊緣情況下會失敗
function problematicFunction() {
  // 需要修正的邏輯
}
```

### 2.2 ESLint 和 Prettier 設定

#### 2.2.1 ESLint 設定範例

```json
// .eslintrc.json
{
  "env": {
    "browser": true,
    "es2021": true,
    "node": true
  },
  "extends": [
    "eslint:recommended"
  ],
  "parserOptions": {
    "ecmaVersion": 2022,
    "sourceType": "module"
  },
  "rules": {
    "indent": ["error", 2],
    "quotes": ["error", "single"],
    "semi": ["error", "always"],
    "no-unused-vars": ["error", { "argsIgnorePattern": "^_" }],
    "no-console": ["warn"],
    "prefer-const": ["error"],
    "no-var": ["error"]
  }
}
```

#### 2.2.2 Prettier 設定範例

```json
// .prettierrc
{
  "singleQuote": true,
  "trailingComma": "es5",
  "tabWidth": 2,
  "semi": true,
  "printWidth": 80,
  "bracketSpacing": true,
  "arrowParens": "avoid"
}
```

### 2.3 專案中常用的 Utility Functions

#### 2.3.1 資料處理工具函式

```javascript
// ✅ 深拷貝函式
function deepClone(obj) {
  if (obj === null || typeof obj !== 'object') {
    return obj;
  }
  
  if (obj instanceof Date) {
    return new Date(obj.getTime());
  }
  
  if (obj instanceof Array) {
    return obj.map(item => deepClone(item));
  }
  
  if (typeof obj === 'object') {
    const clonedObj = {};
    Object.keys(obj).forEach(key => {
      clonedObj[key] = deepClone(obj[key]);
    });
    return clonedObj;
  }
}

// ✅ 陣列去重
function uniqueArray(array, key = null) {
  if (key) {
    // 物件陣列去重
    const seen = new Set();
    return array.filter(item => {
      const value = item[key];
      if (seen.has(value)) {
        return false;
      }
      seen.add(value);
      return true;
    });
  }
  
  // 基本型別陣列去重
  return [...new Set(array)];
}

// ✅ 物件屬性安全存取
function safeGet(obj, path, defaultValue = undefined) {
  const keys = path.split('.');
  let result = obj;
  
  for (const key of keys) {
    if (result == null || typeof result !== 'object') {
      return defaultValue;
    }
    result = result[key];
  }
  
  return result !== undefined ? result : defaultValue;
}

// 使用範例
const user = {
  profile: {
    contact: {
      email: 'user@example.com'
    }
  }
};

const email = safeGet(user, 'profile.contact.email', '未提供');
const phone = safeGet(user, 'profile.contact.phone', '未提供');
```

#### 2.3.2 字串處理工具函式

```javascript
// ✅ 字串格式化
function formatString(template, params) {
  return template.replace(/\{(\w+)\}/g, (match, key) => {
    return params[key] !== undefined ? params[key] : match;
  });
}

// 使用範例
const message = formatString('歡迎 {name}，您的積分為 {points}', {
  name: 'Alice',
  points: 1500
});

// ✅ 字串轉換函式
const stringUtils = {
  // 轉換為駝峰命名
  toCamelCase: (str) => {
    return str.replace(/[-_](.)/g, (_, char) => char.toUpperCase());
  },
  
  // 轉換為蛇形命名
  toSnakeCase: (str) => {
    return str.replace(/([A-Z])/g, '_$1').toLowerCase().replace(/^_/, '');
  },
  
  // 首字母大寫
  capitalize: (str) => {
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
  },
  
  // 截斷字串
  truncate: (str, length, suffix = '...') => {
    return str.length > length ? str.substring(0, length) + suffix : str;
  }
};
```

#### 2.3.3 日期處理工具函式

```javascript
// ✅ 日期格式化函式
const dateUtils = {
  // 格式化日期
  format: (date, format = 'YYYY-MM-DD') => {
    const d = new Date(date);
    const year = d.getFullYear();
    const month = String(d.getMonth() + 1).padStart(2, '0');
    const day = String(d.getDate()).padStart(2, '0');
    const hours = String(d.getHours()).padStart(2, '0');
    const minutes = String(d.getMinutes()).padStart(2, '0');
    const seconds = String(d.getSeconds()).padStart(2, '0');
    
    return format
      .replace('YYYY', year)
      .replace('MM', month)
      .replace('DD', day)
      .replace('HH', hours)
      .replace('mm', minutes)
      .replace('ss', seconds);
  },
  
  // 計算日期差異
  daysBetween: (date1, date2) => {
    const oneDay = 24 * 60 * 60 * 1000;
    const firstDate = new Date(date1);
    const secondDate = new Date(date2);
    return Math.round(Math.abs((firstDate - secondDate) / oneDay));
  },
  
  // 相對時間顯示
  timeAgo: (date) => {
    const now = new Date();
    const past = new Date(date);
    const diffInSeconds = Math.floor((now - past) / 1000);
    
    if (diffInSeconds < 60) return '剛剛';
    if (diffInSeconds < 3600) return `${Math.floor(diffInSeconds / 60)} 分鐘前`;
    if (diffInSeconds < 86400) return `${Math.floor(diffInSeconds / 3600)} 小時前`;
    if (diffInSeconds < 2592000) return `${Math.floor(diffInSeconds / 86400)} 天前`;
    
    return dateUtils.format(date, 'YYYY-MM-DD');
  }
};
```

---

## 3. 專案中常見應用範例

### 3.1 DOM 操作與事件處理

#### 3.1.1 現代 DOM 選取和操作

```javascript
// ✅ DOM 選取器最佳實務
class DomHelper {
  // 單一元素選取
  static select(selector, parent = document) {
    return parent.querySelector(selector);
  }
  
  // 多元素選取
  static selectAll(selector, parent = document) {
    return Array.from(parent.querySelectorAll(selector));
  }
  
  // 建立元素
  static createElement(tag, attributes = {}, children = []) {
    const element = document.createElement(tag);
    
    // 設定屬性
    Object.keys(attributes).forEach(key => {
      if (key === 'className') {
        element.className = attributes[key];
      } else if (key === 'dataset') {
        Object.assign(element.dataset, attributes[key]);
      } else {
        element.setAttribute(key, attributes[key]);
      }
    });
    
    // 加入子元素
    children.forEach(child => {
      if (typeof child === 'string') {
        element.appendChild(document.createTextNode(child));
      } else {
        element.appendChild(child);
      }
    });
    
    return element;
  }
}

// 使用範例
const button = DomHelper.createElement('button', {
  className: 'btn btn-primary',
  dataset: { action: 'submit' },
  id: 'submitBtn'
}, ['提交表單']);
```

#### 3.1.2 事件處理最佳實務

```javascript
// ✅ 事件委派模式
class EventManager {
  constructor() {
    this.listeners = new Map();
  }
  
  // 事件委派
  delegate(parent, eventType, selector, handler) {
    const wrappedHandler = (event) => {
      const target = event.target.closest(selector);
      if (target && parent.contains(target)) {
        handler.call(target, event);
      }
    };
    
    parent.addEventListener(eventType, wrappedHandler);
    
    // 儲存參考以便移除
    const key = `${eventType}-${selector}`;
    this.listeners.set(key, { parent, handler: wrappedHandler });
  }
  
  // 移除事件監聽
  removeDelegate(parent, eventType, selector) {
    const key = `${eventType}-${selector}`;
    const listener = this.listeners.get(key);
    
    if (listener) {
      listener.parent.removeEventListener(eventType, listener.handler);
      this.listeners.delete(key);
    }
  }
}

// 使用範例
const eventManager = new EventManager();

// 為所有按鈕加入點擊事件（包含動態新增的按鈕）
eventManager.delegate(document.body, 'click', '.btn', function(event) {
  console.log('按鈕被點擊:', this.textContent);
  
  // 防止重複點擊
  this.disabled = true;
  setTimeout(() => {
    this.disabled = false;
  }, 1000);
});
```

#### 3.1.3 表單處理

```javascript
// ✅ 表單驗證和提交
class FormHandler {
  constructor(formSelector) {
    this.form = document.querySelector(formSelector);
    this.validators = new Map();
    this.init();
  }
  
  // 初始化
  init() {
    if (!this.form) return;
    
    this.form.addEventListener('submit', this.handleSubmit.bind(this));
    this.form.addEventListener('input', this.handleInput.bind(this));
  }
  
  // 加入驗證規則
  addValidator(fieldName, validator) {
    this.validators.set(fieldName, validator);
  }
  
  // 處理輸入事件
  handleInput(event) {
    const field = event.target;
    if (this.validators.has(field.name)) {
      this.validateField(field);
    }
  }
  
  // 驗證單一欄位
  validateField(field) {
    const validator = this.validators.get(field.name);
    const result = validator(field.value);
    
    this.updateFieldUI(field, result);
    return result.isValid;
  }
  
  // 更新欄位 UI
  updateFieldUI(field, validationResult) {
    const errorElement = field.parentNode.querySelector('.error-message');
    
    if (validationResult.isValid) {
      field.classList.remove('invalid');
      field.classList.add('valid');
      if (errorElement) {
        errorElement.textContent = '';
      }
    } else {
      field.classList.remove('valid');
      field.classList.add('invalid');
      if (errorElement) {
        errorElement.textContent = validationResult.message;
      }
    }
  }
  
  // 處理表單提交
  async handleSubmit(event) {
    event.preventDefault();
    
    // 驗證所有欄位
    const isFormValid = this.validateForm();
    if (!isFormValid) {
      return;
    }
    
    // 取得表單資料
    const formData = this.getFormData();
    
    try {
      // 提交表單
      await this.submitForm(formData);
      this.onSubmitSuccess();
    } catch (error) {
      this.onSubmitError(error);
    }
  }
  
  // 驗證整個表單
  validateForm() {
    let isValid = true;
    
    this.validators.forEach((validator, fieldName) => {
      const field = this.form.querySelector(`[name="${fieldName}"]`);
      if (field && !this.validateField(field)) {
        isValid = false;
      }
    });
    
    return isValid;
  }
  
  // 取得表單資料
  getFormData() {
    const formData = new FormData(this.form);
    const data = {};
    
    for (const [key, value] of formData.entries()) {
      data[key] = value;
    }
    
    return data;
  }
  
  // 提交表單
  async submitForm(data) {
    const response = await fetch(this.form.action, {
      method: this.form.method || 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data)
    });
    
    if (!response.ok) {
      throw new Error(`提交失敗: ${response.statusText}`);
    }
    
    return response.json();
  }
  
  // 提交成功處理
  onSubmitSuccess() {
    this.form.reset();
    this.showMessage('表單提交成功！', 'success');
  }
  
  // 提交錯誤處理
  onSubmitError(error) {
    console.error('表單提交錯誤:', error);
    this.showMessage('提交失敗，請稍後再試', 'error');
  }
  
  // 顯示訊息
  showMessage(message, type) {
    // 實作訊息顯示邏輯
    console.log(`${type.toUpperCase()}: ${message}`);
  }
}

// 使用範例
const userForm = new FormHandler('#userForm');

// 加入驗證規則
userForm.addValidator('email', (value) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return {
    isValid: emailRegex.test(value),
    message: emailRegex.test(value) ? '' : '請輸入有效的電子郵件地址'
  };
});

userForm.addValidator('password', (value) => {
  const isValid = value.length >= 8;
  return {
    isValid,
    message: isValid ? '' : '密碼至少需要 8 個字元'
  };
});
```

### 3.2 非同步處理 (Promise, async/await, fetch API)

#### 3.2.1 Promise 最佳實務

```javascript
// ✅ Promise 串連和錯誤處理
function processUserRegistration(userData) {
  return validateUserData(userData)
    .then(validatedData => createUser(validatedData))
    .then(user => sendWelcomeEmail(user.email))
    .then(() => ({
      success: true,
      message: '用戶註冊成功'
    }))
    .catch(error => {
      console.error('用戶註冊失敗:', error);
      return {
        success: false,
        message: error.message || '註冊過程發生錯誤'
      };
    });
}

// ✅ Promise.all 並行處理
async function loadDashboardData(userId) {
  try {
    const [userProfile, notifications, statistics] = await Promise.all([
      fetchUserProfile(userId),
      fetchNotifications(userId),
      fetchUserStatistics(userId)
    ]);
    
    return {
      profile: userProfile,
      notifications,
      stats: statistics
    };
  } catch (error) {
    console.error('載入儀表板資料失敗:', error);
    throw new Error('無法載入儀表板資料');
  }
}

// ✅ Promise.allSettled 處理部分失敗
async function loadOptionalData() {
  const promises = [
    fetchCriticalData(),
    fetchOptionalData1(),
    fetchOptionalData2()
  ];
  
  const results = await Promise.allSettled(promises);
  
  const [criticalResult, optional1Result, optional2Result] = results;
  
  // 關鍵資料必須成功
  if (criticalResult.status === 'rejected') {
    throw new Error('無法載入關鍵資料');
  }
  
  return {
    critical: criticalResult.value,
    optional1: optional1Result.status === 'fulfilled' ? optional1Result.value : null,
    optional2: optional2Result.status === 'fulfilled' ? optional2Result.value : null
  };
}
```

#### 3.2.2 async/await 進階應用

```javascript
// ✅ 錯誤處理和重試機制
async function fetchWithRetry(url, options = {}, maxRetries = 3) {
  const { retryDelay = 1000, ...fetchOptions } = options;
  
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const response = await fetch(url, fetchOptions);
      
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }
      
      return await response.json();
    } catch (error) {
      console.warn(`第 ${attempt} 次嘗試失敗:`, error.message);
      
      if (attempt === maxRetries) {
        throw new Error(`在 ${maxRetries} 次嘗試後仍然失敗: ${error.message}`);
      }
      
      // 等待後重試
      await new Promise(resolve => setTimeout(resolve, retryDelay * attempt));
    }
  }
}

// ✅ 序列化處理
async function processItemsSequentially(items, processor) {
  const results = [];
  
  for (const item of items) {
    try {
      const result = await processor(item);
      results.push({ success: true, data: result });
    } catch (error) {
      console.error(`處理項目失敗:`, item, error);
      results.push({ success: false, error: error.message });
    }
  }
  
  return results;
}

// ✅ 並行處理與限流
async function processItemsConcurrently(items, processor, concurrency = 5) {
  const results = [];
  
  for (let i = 0; i < items.length; i += concurrency) {
    const batch = items.slice(i, i + concurrency);
    const batchPromises = batch.map(async (item, index) => {
      try {
        const result = await processor(item);
        return { index: i + index, success: true, data: result };
      } catch (error) {
        return { index: i + index, success: false, error: error.message };
      }
    });
    
    const batchResults = await Promise.all(batchPromises);
    results.push(...batchResults);
  }
  
  return results.sort((a, b) => a.index - b.index);
}
```

### 3.3 與後端 API 溝通 (RESTful API 呼叫範例)

#### 3.3.1 API 客戶端類別設計

```javascript
// ✅ API 客戶端封裝
class ApiClient {
  constructor(baseUrl, options = {}) {
    this.baseUrl = baseUrl.replace(/\/$/, '');
    this.defaultHeaders = {
      'Content-Type': 'application/json',
      ...options.headers
    };
    this.timeout = options.timeout || 10000;
    this.interceptors = {
      request: [],
      response: []
    };
  }
  
  // 加入請求攔截器
  addRequestInterceptor(interceptor) {
    this.interceptors.request.push(interceptor);
  }
  
  // 加入回應攔截器
  addResponseInterceptor(interceptor) {
    this.interceptors.response.push(interceptor);
  }
  
  // 執行請求攔截器
  async applyRequestInterceptors(config) {
    let processedConfig = { ...config };
    
    for (const interceptor of this.interceptors.request) {
      processedConfig = await interceptor(processedConfig);
    }
    
    return processedConfig;
  }
  
  // 執行回應攔截器
  async applyResponseInterceptors(response) {
    let processedResponse = response;
    
    for (const interceptor of this.interceptors.response) {
      processedResponse = await interceptor(processedResponse);
    }
    
    return processedResponse;
  }
  
  // 基礎請求方法
  async request(endpoint, options = {}) {
    const url = `${this.baseUrl}${endpoint}`;
    
    // 準備請求配置
    let config = {
      method: 'GET',
      headers: { ...this.defaultHeaders },
      ...options
    };
    
    // 套用請求攔截器
    config = await this.applyRequestInterceptors(config);
    
    // 建立 AbortController 用於超時控制
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), this.timeout);
    
    try {
      config.signal = controller.signal;
      const response = await fetch(url, config);
      clearTimeout(timeoutId);
      
      // 套用回應攔截器
      const processedResponse = await this.applyResponseInterceptors(response);
      
      if (!processedResponse.ok) {
        throw new Error(`HTTP ${processedResponse.status}: ${processedResponse.statusText}`);
      }
      
      return await processedResponse.json();
    } catch (error) {
      clearTimeout(timeoutId);
      
      if (error.name === 'AbortError') {
        throw new Error('請求超時');
      }
      
      throw error;
    }
  }
  
  // GET 請求
  get(endpoint, params = {}) {
    const queryString = new URLSearchParams(params).toString();
    const url = queryString ? `${endpoint}?${queryString}` : endpoint;
    return this.request(url);
  }
  
  // POST 請求
  post(endpoint, data = {}) {
    return this.request(endpoint, {
      method: 'POST',
      body: JSON.stringify(data)
    });
  }
  
  // PUT 請求
  put(endpoint, data = {}) {
    return this.request(endpoint, {
      method: 'PUT',
      body: JSON.stringify(data)
    });
  }
  
  // PATCH 請求
  patch(endpoint, data = {}) {
    return this.request(endpoint, {
      method: 'PATCH',
      body: JSON.stringify(data)
    });
  }
  
  // DELETE 請求
  delete(endpoint) {
    return this.request(endpoint, {
      method: 'DELETE'
    });
  }
}

// 建立 API 客戶端實例
const apiClient = new ApiClient('https://api.example.com', {
  timeout: 15000,
  headers: {
    'X-App-Version': '1.0.0'
  }
});

// 加入認證攔截器
apiClient.addRequestInterceptor(async (config) => {
  const token = localStorage.getItem('authToken');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// 加入錯誤處理攔截器
apiClient.addResponseInterceptor(async (response) => {
  if (response.status === 401) {
    // 處理認證過期
    localStorage.removeItem('authToken');
    window.location.href = '/login';
  }
  return response;
});
```

#### 3.3.2 具體 API 呼叫範例

```javascript
// ✅ 用戶管理 API
class UserService {
  // 取得用戶列表
  static async getUsers(page = 1, limit = 10, filters = {}) {
    try {
      const params = {
        page,
        limit,
        ...filters
      };
      
      const response = await apiClient.get('/users', params);
      return response;
    } catch (error) {
      console.error('取得用戶列表失敗:', error);
      throw new Error('無法載入用戶列表');
    }
  }
  
  // 取得單一用戶
  static async getUserById(userId) {
    try {
      const response = await apiClient.get(`/users/${userId}`);
      return response.data;
    } catch (error) {
      console.error('取得用戶資料失敗:', error);
      throw new Error('無法載入用戶資料');
    }
  }
  
  // 建立用戶
  static async createUser(userData) {
    try {
      // 資料驗證
      if (!userData.email || !userData.name) {
        throw new Error('電子郵件和姓名為必填欄位');
      }
      
      const response = await apiClient.post('/users', userData);
      return response.data;
    } catch (error) {
      console.error('建立用戶失敗:', error);
      throw new Error('無法建立用戶');
    }
  }
  
  // 更新用戶
  static async updateUser(userId, userData) {
    try {
      const response = await apiClient.put(`/users/${userId}`, userData);
      return response.data;
    } catch (error) {
      console.error('更新用戶失敗:', error);
      throw new Error('無法更新用戶資料');
    }
  }
  
  // 刪除用戶
  static async deleteUser(userId) {
    try {
      await apiClient.delete(`/users/${userId}`);
      return true;
    } catch (error) {
      console.error('刪除用戶失敗:', error);
      throw new Error('無法刪除用戶');
    }
  }
  
  // 批次操作
  static async batchUpdateUsers(updates) {
    try {
      const response = await apiClient.patch('/users/batch', { updates });
      return response.data;
    } catch (error) {
      console.error('批次更新失敗:', error);
      throw new Error('無法執行批次更新');
    }
  }
}

// ✅ 檔案上傳 API
class FileService {
  static async uploadFile(file, onProgress = null) {
    try {
      const formData = new FormData();
      formData.append('file', file);
      
      // 使用 XMLHttpRequest 支援進度追蹤
      return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        
        // 進度事件
        if (onProgress) {
          xhr.upload.addEventListener('progress', (event) => {
            if (event.lengthComputable) {
              const percentComplete = (event.loaded / event.total) * 100;
              onProgress(Math.round(percentComplete));
            }
          });
        }
        
        // 完成事件
        xhr.addEventListener('load', () => {
          if (xhr.status >= 200 && xhr.status < 300) {
            resolve(JSON.parse(xhr.responseText));
          } else {
            reject(new Error(`上傳失敗: ${xhr.statusText}`));
          }
        });
        
        // 錯誤事件
        xhr.addEventListener('error', () => {
          reject(new Error('上傳過程發生錯誤'));
        });
        
        // 發送請求
        xhr.open('POST', `${apiClient.baseUrl}/files/upload`);
        
        // 加入認證標頭
        const token = localStorage.getItem('authToken');
        if (token) {
          xhr.setRequestHeader('Authorization', `Bearer ${token}`);
        }
        
        xhr.send(formData);
      });
    } catch (error) {
      console.error('檔案上傳失敗:', error);
      throw new Error('無法上傳檔案');
    }
  }
  
  static async downloadFile(fileId, filename) {
    try {
      const response = await fetch(`${apiClient.baseUrl}/files/${fileId}/download`, {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('authToken')}`
        }
      });
      
      if (!response.ok) {
        throw new Error('下載失敗');
      }
      
      const blob = await response.blob();
      
      // 建立下載連結
      const url = window.URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = filename || `file_${fileId}`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      window.URL.revokeObjectURL(url);
    } catch (error) {
      console.error('檔案下載失敗:', error);
      throw new Error('無法下載檔案');
    }
  }
}
```

#### 3.3.3 API 呼叫的實際應用範例

```javascript
// ✅ 用戶管理介面
class UserManagement {
  constructor() {
    this.currentPage = 1;
    this.usersPerPage = 10;
    this.filters = {};
    this.init();
  }
  
  async init() {
    await this.loadUsers();
    this.setupEventListeners();
  }
  
  // 載入用戶列表
  async loadUsers() {
    try {
      this.showLoading(true);
      
      const response = await UserService.getUsers(
        this.currentPage,
        this.usersPerPage,
        this.filters
      );
      
      this.renderUserTable(response.data);
      this.renderPagination(response.pagination);
    } catch (error) {
      this.showError('載入用戶列表失敗: ' + error.message);
    } finally {
      this.showLoading(false);
    }
  }
  
  // 建立新用戶
  async createUser(userData) {
    try {
      this.showLoading(true);
      
      const newUser = await UserService.createUser(userData);
      await this.loadUsers(); // 重新載入列表
      this.showSuccess('用戶建立成功');
      
      return newUser;
    } catch (error) {
      this.showError('建立用戶失敗: ' + error.message);
      throw error;
    } finally {
      this.showLoading(false);
    }
  }
  
  // 設定事件監聽器
  setupEventListeners() {
    // 搜尋功能
    const searchInput = document.getElementById('userSearch');
    if (searchInput) {
      let searchTimeout;
      searchInput.addEventListener('input', (event) => {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
          this.filters.search = event.target.value;
          this.currentPage = 1;
          this.loadUsers();
        }, 500); // 防抖處理
      });
    }
    
    // 新增用戶按鈕
    const addUserBtn = document.getElementById('addUserBtn');
    if (addUserBtn) {
      addUserBtn.addEventListener('click', () => {
        this.showUserModal();
      });
    }
  }
  
  // 顯示用戶表格
  renderUserTable(users) {
    const tbody = document.querySelector('#userTable tbody');
    if (!tbody) return;
    
    tbody.innerHTML = users.map(user => `
      <tr data-user-id="${user.id}">
        <td>${user.name}</td>
        <td>${user.email}</td>
        <td>${user.department || '未指定'}</td>
        <td>${dateUtils.format(user.createdAt, 'YYYY-MM-DD')}</td>
        <td>
          <button class="btn btn-sm btn-primary" onclick="userManagement.editUser(${user.id})">
            編輯
          </button>
          <button class="btn btn-sm btn-danger" onclick="userManagement.deleteUser(${user.id})">
            刪除
          </button>
        </td>
      </tr>
    `).join('');
  }
  
  // UI 輔助方法
  showLoading(show) {
    const loadingElement = document.getElementById('loading');
    if (loadingElement) {
      loadingElement.style.display = show ? 'block' : 'none';
    }
  }
  
  showError(message) {
    // 實作錯誤訊息顯示
    console.error(message);
  }
  
  showSuccess(message) {
    // 實作成功訊息顯示
    console.log(message);
  }
}

// 初始化用戶管理
const userManagement = new UserManagement();
```

### 3.4 錯誤處理與例外狀況處理

#### 3.4.1 錯誤分類和處理策略

```javascript
// ✅ 自定義錯誤類別
class AppError extends Error {
  constructor(message, code, statusCode = 500) {
    super(message);
    this.name = this.constructor.name;
    this.code = code;
    this.statusCode = statusCode;
    this.timestamp = new Date().toISOString();
    
    // 保持堆疊追蹤
    if (Error.captureStackTrace) {
      Error.captureStackTrace(this, this.constructor);
    }
  }
}

class ValidationError extends AppError {
  constructor(message, field = null) {
    super(message, 'VALIDATION_ERROR', 400);
    this.field = field;
  }
}

class NetworkError extends AppError {
  constructor(message, originalError = null) {
    super(message, 'NETWORK_ERROR', 0);
    this.originalError = originalError;
  }
}

class AuthenticationError extends AppError {
  constructor(message = '認證失敗') {
    super(message, 'AUTH_ERROR', 401);
  }
}

class AuthorizationError extends AppError {
  constructor(message = '權限不足') {
    super(message, 'PERMISSION_ERROR', 403);
  }
}
```

#### 3.4.2 全域錯誤處理器

```javascript
// ✅ 錯誤處理管理器
class ErrorHandler {
  constructor() {
    this.errorLoggers = [];
    this.userNotifiers = [];
    this.setupGlobalHandlers();
  }
  
  // 設定全域錯誤處理
  setupGlobalHandlers() {
    // 處理未捕捉的 Promise 拒絕
    window.addEventListener('unhandledrejection', (event) => {
      console.error('未處理的 Promise 拒絕:', event.reason);
      this.handleError(event.reason);
      event.preventDefault(); // 防止預設的錯誤顯示
    });
    
    // 處理一般 JavaScript 錯誤
    window.addEventListener('error', (event) => {
      console.error('JavaScript 錯誤:', event.error);
      this.handleError(event.error);
    });
  }
  
  // 加入錯誤記錄器
  addLogger(logger) {
    this.errorLoggers.push(logger);
  }
  
  // 加入用戶通知器
  addNotifier(notifier) {
    this.userNotifiers.push(notifier);
  }
  
  // 處理錯誤
  async handleError(error) {
    // 標準化錯誤物件
    const standardError = this.standardizeError(error);
    
    // 記錄錯誤
    await this.logError(standardError);
    
    // 通知用戶
    await this.notifyUser(standardError);
  }
  
  // 標準化錯誤物件
  standardizeError(error) {
    if (error instanceof AppError) {
      return error;
    }
    
    if (error instanceof TypeError) {
      return new AppError(error.message, 'TYPE_ERROR', 500);
    }
    
    if (error instanceof ReferenceError) {
      return new AppError(error.message, 'REFERENCE_ERROR', 500);
    }
    
    // 網路錯誤
    if (error.name === 'NetworkError' || error.message.includes('fetch')) {
      return new NetworkError('網路連線錯誤', error);
    }
    
    // 預設錯誤
    return new AppError(
      error.message || '發生未知錯誤',
      'UNKNOWN_ERROR',
      500
    );
  }
  
  // 記錄錯誤
  async logError(error) {
    const errorInfo = {
      message: error.message,
      code: error.code,
      statusCode: error.statusCode,
      timestamp: error.timestamp,
      stack: error.stack,
      userAgent: navigator.userAgent,
      url: window.location.href,
      userId: this.getCurrentUserId()
    };
    
    // 執行所有錯誤記錄器
    for (const logger of this.errorLoggers) {
      try {
        await logger(errorInfo);
      } catch (logError) {
        console.error('錯誤記錄失敗:', logError);
      }
    }
  }
  
  // 通知用戶
  async notifyUser(error) {
    // 根據錯誤類型決定是否顯示給用戶
    if (this.shouldNotifyUser(error)) {
      const userMessage = this.getUserMessage(error);
      
      // 執行所有用戶通知器
      for (const notifier of this.userNotifiers) {
        try {
          await notifier(userMessage, error.code);
        } catch (notifyError) {
          console.error('用戶通知失敗:', notifyError);
        }
      }
    }
  }
  
  // 判斷是否應該通知用戶
  shouldNotifyUser(error) {
    // 系統內部錯誤通常不直接顯示給用戶
    const internalErrors = ['REFERENCE_ERROR', 'TYPE_ERROR', 'UNKNOWN_ERROR'];
    return !internalErrors.includes(error.code);
  }
  
  // 取得用戶友善的錯誤訊息
  getUserMessage(error) {
    const userMessages = {
      'VALIDATION_ERROR': error.message,
      'NETWORK_ERROR': '網路連線不穩定，請稍後再試',
      'AUTH_ERROR': '請重新登入',
      'PERMISSION_ERROR': '您沒有執行此操作的權限',
      'SERVER_ERROR': '伺服器暫時無法處理請求，請稍後再試'
    };
    
    return userMessages[error.code] || '操作失敗，請稍後再試';
  }
  
  getCurrentUserId() {
    // 從認證狀態取得當前用戶 ID
    try {
      const token = localStorage.getItem('authToken');
      if (token) {
        const payload = JSON.parse(atob(token.split('.')[1]));
        return payload.userId;
      }
    } catch (e) {
      // 忽略解析錯誤
    }
    return null;
  }
}

// 建立全域錯誤處理器
const errorHandler = new ErrorHandler();

// 加入錯誤記錄器
errorHandler.addLogger(async (errorInfo) => {
  // 發送到錯誤監控服務
  try {
    await fetch('/api/errors', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(errorInfo)
    });
  } catch (e) {
    console.error('無法發送錯誤日誌:', e);
  }
});

// 加入用戶通知器
errorHandler.addNotifier(async (message, errorCode) => {
  // 顯示用戶友善的錯誤訊息
  showToast(message, 'error');
});
```

#### 3.4.3 具體錯誤處理範例

```javascript
// ✅ API 呼叫錯誤處理
async function safeApiCall(apiFunction, ...args) {
  try {
    const result = await apiFunction(...args);
    return { success: true, data: result };
  } catch (error) {
    // 根據錯誤類型進行不同處理
    if (error.name === 'AbortError') {
      return { success: false, error: '操作已取消' };
    }
    
    if (error.message.includes('401')) {
      // 認證失敗，重新導向到登入頁
      window.location.href = '/login';
      return { success: false, error: '請重新登入' };
    }
    
    if (error.message.includes('403')) {
      return { success: false, error: '權限不足' };
    }
    
    if (error.message.includes('404')) {
      return { success: false, error: '找不到請求的資源' };
    }
    
    if (error.message.includes('500')) {
      return { success: false, error: '伺服器錯誤，請稍後再試' };
    }
    
    // 預設錯誤處理
    return { success: false, error: '操作失敗，請稍後再試' };
  }
}

// 使用範例
async function loadUserData(userId) {
  const result = await safeApiCall(UserService.getUserById, userId);
  
  if (result.success) {
    displayUserData(result.data);
  } else {
    showErrorMessage(result.error);
  }
}

// ✅ 表單驗證錯誤處理
function validateForm(formData) {
  const errors = [];
  
  try {
    // 驗證電子郵件
    if (!formData.email) {
      errors.push(new ValidationError('電子郵件為必填欄位', 'email'));
    } else if (!isValidEmail(formData.email)) {
      errors.push(new ValidationError('請輸入有效的電子郵件地址', 'email'));
    }
    
    // 驗證密碼
    if (!formData.password) {
      errors.push(new ValidationError('密碼為必填欄位', 'password'));
    } else if (formData.password.length < 8) {
      errors.push(new ValidationError('密碼長度至少需要 8 個字元', 'password'));
    }
    
    if (errors.length > 0) {
      throw errors;
    }
    
    return { isValid: true, errors: [] };
  } catch (validationErrors) {
    return { isValid: false, errors: validationErrors };
  }
}

// ✅ 重試機制的錯誤處理
async function retryOperation(operation, maxRetries = 3, delay = 1000) {
  let lastError;
  
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      return await operation();
    } catch (error) {
      lastError = error;
      
      // 某些錯誤不應該重試
      if (error instanceof ValidationError || 
          error instanceof AuthenticationError || 
          error instanceof AuthorizationError) {
        throw error;
      }
      
      if (attempt === maxRetries) {
        throw new AppError(
          `操作在 ${maxRetries} 次嘗試後仍然失敗: ${error.message}`,
          'MAX_RETRIES_EXCEEDED'
        );
      }
      
      // 等待後重試
      await new Promise(resolve => setTimeout(resolve, delay * attempt));
    }
  }
}
```

### 3.5 Web APIs 應用

#### 3.5.1 本地儲存 (Local Storage & Session Storage)

```javascript
// ✅ Local Storage - 持久性儲存
class LocalStorageManager {
  // 儲存資料
  static set(key, value) {
    try {
      const serializedValue = JSON.stringify(value);
      localStorage.setItem(key, serializedValue);
      return true;
    } catch (error) {
      console.error('Local Storage 儲存失敗:', error);
      return false;
    }
  }
  
  // 讀取資料
  static get(key, defaultValue = null) {
    try {
      const serializedValue = localStorage.getItem(key);
      return serializedValue ? JSON.parse(serializedValue) : defaultValue;
    } catch (error) {
      console.error('Local Storage 讀取失敗:', error);
      return defaultValue;
    }
  }
  
  // 移除資料
  static remove(key) {
    try {
      localStorage.removeItem(key);
      return true;
    } catch (error) {
      console.error('Local Storage 移除失敗:', error);
      return false;
    }
  }
  
  // 清空所有資料
  static clear() {
    try {
      localStorage.clear();
      return true;
    } catch (error) {
      console.error('Local Storage 清空失敗:', error);
      return false;
    }
  }
  
  // 取得所有鍵名
  static getAllKeys() {
    return Object.keys(localStorage);
  }
  
  // 檢查容量
  static checkCapacity() {
    try {
      const testKey = '__test__';
      const testValue = new Array(1024 * 1024).join('a'); // 1MB
      localStorage.setItem(testKey, testValue);
      localStorage.removeItem(testKey);
      return true;
    } catch (error) {
      return false;
    }
  }
}

// ✅ Session Storage - 會話期間儲存
class SessionStorageManager {
  static set(key, value) {
    try {
      sessionStorage.setItem(key, JSON.stringify(value));
      return true;
    } catch (error) {
      console.error('Session Storage 儲存失敗:', error);
      return false;
    }
  }
  
  static get(key, defaultValue = null) {
    try {
      const value = sessionStorage.getItem(key);
      return value ? JSON.parse(value) : defaultValue;
    } catch (error) {
      console.error('Session Storage 讀取失敗:', error);
      return defaultValue;
    }
  }
  
  static remove(key) {
    sessionStorage.removeItem(key);
  }
  
  static clear() {
    sessionStorage.clear();
  }
}

// 使用範例
// 儲存使用者偏好設定
LocalStorageManager.set('userPreferences', {
  theme: 'dark',
  language: 'zh-TW',
  fontSize: 16
});

// 儲存暫時的表單資料
SessionStorageManager.set('formData', {
  name: 'Alice',
  email: 'alice@example.com'
});
```

#### 3.5.2 Fetch API 進階應用

```javascript
// ✅ 進階 Fetch 封裝
class HttpClient {
  constructor(baseURL = '', defaultOptions = {}) {
    this.baseURL = baseURL;
    this.defaultOptions = {
      headers: {
        'Content-Type': 'application/json',
      },
      ...defaultOptions
    };
    this.interceptors = {
      request: [],
      response: []
    };
  }
  
  // 加入請求攔截器
  addRequestInterceptor(interceptor) {
    this.interceptors.request.push(interceptor);
  }
  
  // 加入回應攔截器
  addResponseInterceptor(interceptor) {
    this.interceptors.response.push(interceptor);
  }
  
  // 處理請求攔截器
  async processRequestInterceptors(url, options) {
    let processedOptions = { ...options };
    
    for (const interceptor of this.interceptors.request) {
      processedOptions = await interceptor(url, processedOptions);
    }
    
    return processedOptions;
  }
  
  // 處理回應攔截器
  async processResponseInterceptors(response) {
    let processedResponse = response;
    
    for (const interceptor of this.interceptors.response) {
      processedResponse = await interceptor(processedResponse);
    }
    
    return processedResponse;
  }
  
  // 基礎請求方法
  async request(url, options = {}) {
    const fullURL = this.baseURL + url;
    
    // 合併預設選項
    let mergedOptions = {
      ...this.defaultOptions,
      ...options,
      headers: {
        ...this.defaultOptions.headers,
        ...options.headers
      }
    };
    
    // 處理請求攔截器
    mergedOptions = await this.processRequestInterceptors(fullURL, mergedOptions);
    
    try {
      let response = await fetch(fullURL, mergedOptions);
      
      // 處理回應攔截器
      response = await this.processResponseInterceptors(response);
      
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }
      
      return response;
    } catch (error) {
      console.error('HTTP 請求失敗:', error);
      throw error;
    }
  }
  
  // GET 請求
  async get(url, params = {}) {
    const queryString = new URLSearchParams(params).toString();
    const finalURL = queryString ? `${url}?${queryString}` : url;
    
    const response = await this.request(finalURL, { method: 'GET' });
    return response.json();
  }
  
  // POST 請求
  async post(url, data = {}) {
    const response = await this.request(url, {
      method: 'POST',
      body: JSON.stringify(data)
    });
    return response.json();
  }
  
  // PUT 請求
  async put(url, data = {}) {
    const response = await this.request(url, {
      method: 'PUT',
      body: JSON.stringify(data)
    });
    return response.json();
  }
  
  // DELETE 請求
  async delete(url) {
    const response = await this.request(url, { method: 'DELETE' });
    return response.status === 204 ? null : response.json();
  }
  
  // 上傳檔案
  async uploadFile(url, file, onProgress = null) {
    const formData = new FormData();
    formData.append('file', file);
    
    const options = {
      method: 'POST',
      body: formData,
      headers: {} // 讓瀏覽器自動設定 Content-Type
    };
    
    // 如果需要進度追蹤，使用 XMLHttpRequest
    if (onProgress) {
      return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        
        xhr.upload.addEventListener('progress', (event) => {
          if (event.lengthComputable) {
            const percentComplete = (event.loaded / event.total) * 100;
            onProgress(Math.round(percentComplete));
          }
        });
        
        xhr.addEventListener('load', () => {
          if (xhr.status >= 200 && xhr.status < 300) {
            resolve(JSON.parse(xhr.responseText));
          } else {
            reject(new Error(`Upload failed: ${xhr.statusText}`));
          }
        });
        
        xhr.addEventListener('error', () => {
          reject(new Error('Upload failed'));
        });
        
        xhr.open('POST', this.baseURL + url);
        xhr.send(formData);
      });
    }
    
    const response = await this.request(url, options);
    return response.json();
  }
}

// 建立 HTTP 客戶端實例
const httpClient = new HttpClient('https://api.example.com');

// 加入認證攔截器
httpClient.addRequestInterceptor(async (url, options) => {
  const token = LocalStorageManager.get('authToken');
  if (token) {
    options.headers.Authorization = `Bearer ${token}`;
  }
  return options;
});

// 加入錯誤處理攔截器
httpClient.addResponseInterceptor(async (response) => {
  if (response.status === 401) {
    LocalStorageManager.remove('authToken');
    window.location.href = '/login';
  }
  return response;
});
```

#### 3.5.3 Web Workers

```javascript
// ✅ Web Worker 應用
// worker.js (獨立檔案)
/*
self.addEventListener('message', function(event) {
  const { type, data } = event.data;
  
  switch (type) {
    case 'HEAVY_CALCULATION':
      const result = performHeavyCalculation(data);
      self.postMessage({ type: 'CALCULATION_COMPLETE', result });
      break;
      
    case 'PROCESS_DATA':
      const processedData = processLargeDataSet(data);
      self.postMessage({ type: 'DATA_PROCESSED', result: processedData });
      break;
      
    default:
      self.postMessage({ type: 'ERROR', message: 'Unknown command' });
  }
});

function performHeavyCalculation(numbers) {
  return numbers.map(num => {
    let result = 0;
    for (let i = 0; i < 1000000; i++) {
      result += Math.sqrt(num * i);
    }
    return result;
  });
}

function processLargeDataSet(data) {
  return data
    .filter(item => item.active)
    .map(item => ({
      ...item,
      processed: true,
      timestamp: Date.now()
    }))
    .sort((a, b) => a.priority - b.priority);
}
*/

// 主執行緒 Web Worker 管理器
class WorkerManager {
  constructor(workerScript) {
    this.worker = null;
    this.workerScript = workerScript;
    this.messageHandlers = new Map();
    this.messageId = 0;
  }
  
  // 初始化 Worker
  init() {
    if (!this.worker) {
      this.worker = new Worker(this.workerScript);
      this.worker.addEventListener('message', this.handleMessage.bind(this));
      this.worker.addEventListener('error', this.handleError.bind(this));
    }
  }
  
  // 處理來自 Worker 的訊息
  handleMessage(event) {
    const { type, result, messageId } = event.data;
    
    const handler = this.messageHandlers.get(messageId);
    if (handler) {
      handler.resolve(result);
      this.messageHandlers.delete(messageId);
    }
  }
  
  // 處理 Worker 錯誤
  handleError(error) {
    console.error('Worker 錯誤:', error);
    
    // 拒絕所有等待中的 Promise
    this.messageHandlers.forEach(handler => {
      handler.reject(new Error('Worker 執行錯誤'));
    });
    this.messageHandlers.clear();
  }
  
  // 發送訊息到 Worker
  sendMessage(type, data) {
    return new Promise((resolve, reject) => {
      this.init();
      
      const messageId = ++this.messageId;
      this.messageHandlers.set(messageId, { resolve, reject });
      
      this.worker.postMessage({
        type,
        data,
        messageId
      });
      
      // 設定超時
      setTimeout(() => {
        if (this.messageHandlers.has(messageId)) {
          this.messageHandlers.delete(messageId);
          reject(new Error('Worker 訊息超時'));
        }
      }, 30000); // 30 秒超時
    });
  }
  
  // 執行大量計算
  async performHeavyCalculation(numbers) {
    return this.sendMessage('HEAVY_CALCULATION', numbers);
  }
  
  // 處理大型資料集
  async processData(data) {
    return this.sendMessage('PROCESS_DATA', data);
  }
  
  // 終止 Worker
  terminate() {
    if (this.worker) {
      this.worker.terminate();
      this.worker = null;
      this.messageHandlers.clear();
    }
  }
}

// 使用範例
const workerManager = new WorkerManager('/js/worker.js');

// 在背景執行大量計算
async function handleHeavyTask() {
  const numbers = Array.from({ length: 1000 }, (_, i) => i);
  
  try {
    console.log('開始大量計算...');
    const result = await workerManager.performHeavyCalculation(numbers);
    console.log('計算完成:', result);
  } catch (error) {
    console.error('計算失敗:', error);
  }
}
```

#### 3.5.4 地理位置 API

```javascript
// ✅ 地理位置 API 封裝
class GeolocationManager {
  constructor() {
    this.watchId = null;
    this.isSupported = 'geolocation' in navigator;
  }
  
  // 檢查支援度
  isGeolocationSupported() {
    return this.isSupported;
  }
  
  // 取得目前位置
  async getCurrentPosition(options = {}) {
    if (!this.isSupported) {
      throw new Error('瀏覽器不支援地理位置 API');
    }
    
    const defaultOptions = {
      enableHighAccuracy: true,
      timeout: 10000,
      maximumAge: 60000
    };
    
    const mergedOptions = { ...defaultOptions, ...options };
    
    return new Promise((resolve, reject) => {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          resolve({
            latitude: position.coords.latitude,
            longitude: position.coords.longitude,
            accuracy: position.coords.accuracy,
            altitude: position.coords.altitude,
            heading: position.coords.heading,
            speed: position.coords.speed,
            timestamp: position.timestamp
          });
        },
        (error) => {
          let errorMessage;
          switch (error.code) {
            case error.PERMISSION_DENIED:
              errorMessage = "使用者拒絕地理位置存取";
              break;
            case error.POSITION_UNAVAILABLE:
              errorMessage = "無法取得地理位置";
              break;
            case error.TIMEOUT:
              errorMessage = "地理位置請求超時";
              break;
            default:
              errorMessage = "未知的地理位置錯誤";
              break;
          }
          reject(new Error(errorMessage));
        },
        mergedOptions
      );
    });
  }
  
  // 監控位置變化
  watchPosition(onSuccess, onError, options = {}) {
    if (!this.isSupported) {
      throw new Error('瀏覽器不支援地理位置 API');
    }
    
    const defaultOptions = {
      enableHighAccuracy: true,
      timeout: 10000,
      maximumAge: 60000
    };
    
    const mergedOptions = { ...defaultOptions, ...options };
    
    this.watchId = navigator.geolocation.watchPosition(
      onSuccess,
      onError,
      mergedOptions
    );
    
    return this.watchId;
  }
  
  // 停止監控
  clearWatch() {
    if (this.watchId !== null) {
      navigator.geolocation.clearWatch(this.watchId);
      this.watchId = null;
    }
  }
  
  // 計算兩點間距離 (公里)
  static calculateDistance(lat1, lng1, lat2, lng2) {
    const R = 6371; // 地球半徑（公里）
    const dLat = this.toRadians(lat2 - lat1);
    const dLng = this.toRadians(lng2 - lng1);
    
    const a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
              Math.cos(this.toRadians(lat1)) * Math.cos(this.toRadians(lat2)) *
              Math.sin(dLng / 2) * Math.sin(dLng / 2);
    
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    return R * c;
  }
  
  static toRadians(degrees) {
    return degrees * (Math.PI / 180);
  }
}

// 使用範例
const geoManager = new GeolocationManager();

async function getLocation() {
  try {
    const position = await geoManager.getCurrentPosition();
    console.log('目前位置:', position);
    
    // 計算與台北101的距離
    const taipei101 = { lat: 25.0340, lng: 121.5645 };
    const distance = GeolocationManager.calculateDistance(
      position.latitude,
      position.longitude,
      taipei101.lat,
      taipei101.lng
    );
    
    console.log(`距離台北101: ${distance.toFixed(2)} 公里`);
  } catch (error) {
    console.error('取得位置失敗:', error);
  }
}
```

#### 3.5.5 通知 API

```javascript
// ✅ 通知 API 封裝
class NotificationManager {
  constructor() {
    this.isSupported = 'Notification' in window;
    this.permission = this.isSupported ? Notification.permission : 'denied';
  }
  
  // 檢查支援度
  isNotificationSupported() {
    return this.isSupported;
  }
  
  // 請求通知權限
  async requestPermission() {
    if (!this.isSupported) {
      throw new Error('瀏覽器不支援通知 API');
    }
    
    if (this.permission === 'granted') {
      return 'granted';
    }
    
    if (this.permission === 'denied') {
      throw new Error('通知權限已被拒絕');
    }
    
    this.permission = await Notification.requestPermission();
    return this.permission;
  }
  
  // 顯示通知
  async showNotification(title, options = {}) {
    if (!this.isSupported) {
      throw new Error('瀏覽器不支援通知 API');
    }
    
    if (this.permission !== 'granted') {
      await this.requestPermission();
    }
    
    if (this.permission !== 'granted') {
      throw new Error('沒有通知權限');
    }
    
    const defaultOptions = {
      icon: '/favicon.ico',
      badge: '/badge.png',
      image: null,
      body: '',
      tag: 'default',
      requireInteraction: false,
      silent: false,
      vibrate: [200, 100, 200]
    };
    
    const mergedOptions = { ...defaultOptions, ...options };
    
    const notification = new Notification(title, mergedOptions);
    
    // 設定事件處理器
    notification.onclick = options.onClick || function() {
      window.focus();
      notification.close();
    };
    
    notification.onclose = options.onClose || function() {
      console.log('通知已關閉');
    };
    
    notification.onerror = options.onError || function(error) {
      console.error('通知錯誤:', error);
    };
    
    // 自動關閉
    if (options.autoClose && options.autoClose > 0) {
      setTimeout(() => {
        notification.close();
      }, options.autoClose);
    }
    
    return notification;
  }
  
  // 顯示帶按鈕的通知 (需要 Service Worker)
  async showActionNotification(title, options = {}) {
    if (!('serviceWorker' in navigator)) {
      throw new Error('需要 Service Worker 支援');
    }
    
    const registration = await navigator.serviceWorker.ready;
    
    const defaultOptions = {
      body: '',
      icon: '/favicon.ico',
      badge: '/badge.png',
      tag: 'action-notification',
      actions: []
    };
    
    const mergedOptions = { ...defaultOptions, ...options };
    
    return registration.showNotification(title, mergedOptions);
  }
}

// 使用範例
const notificationManager = new NotificationManager();

// 顯示簡單通知
async function showSimpleNotification() {
  try {
    await notificationManager.showNotification('新訊息', {
      body: '您有一則新的訊息',
      icon: '/message-icon.png',
      autoClose: 5000,
      onClick: () => {
        window.open('/messages');
      }
    });
  } catch (error) {
    console.error('顯示通知失敗:', error);
  }
}

// 顯示帶按鈕的通知
async function showActionNotification() {
  try {
    await notificationManager.showActionNotification('會議提醒', {
      body: '您的會議即將在 5 分鐘後開始',
      actions: [
        { action: 'join', title: '加入會議' },
        { action: 'dismiss', title: '稍後提醒' }
      ]
    });
  } catch (error) {
    console.error('顯示通知失敗:', error);
  }
}
```

---

### 3.6 專案最佳實務

#### 3.6.1 模組化程式設計

##### ES6 模組系統

```javascript
// ✅ userService.js - 用戶服務模組
export class UserService {
  constructor(apiClient) {
    this.apiClient = apiClient;
    this.cache = new Map();
  }
  
  async getUser(id) {
    // 先檢查快取
    if (this.cache.has(id)) {
      return this.cache.get(id);
    }
    
    const user = await this.apiClient.get(`/users/${id}`);
    this.cache.set(id, user);
    return user;
  }
  
  clearCache() {
    this.cache.clear();
  }
}

// 命名匯出
export const USER_ROLES = {
  ADMIN: 'admin',
  USER: 'user',
  MODERATOR: 'moderator'
};

export function validateUserRole(role) {
  return Object.values(USER_ROLES).includes(role);
}

// 預設匯出
export default UserService;
```

```javascript
// ✅ utils/dateUtils.js - 日期工具模組
/**
 * 日期格式化工具
 */
export const formatDate = (date, format = 'YYYY-MM-DD') => {
  const d = new Date(date);
  const formatMap = {
    'YYYY': d.getFullYear(),
    'MM': String(d.getMonth() + 1).padStart(2, '0'),
    'DD': String(d.getDate()).padStart(2, '0'),
    'HH': String(d.getHours()).padStart(2, '0'),
    'mm': String(d.getMinutes()).padStart(2, '0'),
    'ss': String(d.getSeconds()).padStart(2, '0')
  };
  
  return Object.keys(formatMap).reduce((result, key) => {
    return result.replace(key, formatMap[key]);
  }, format);
};

/**
 * 計算兩個日期之間的天數差
 */
export const daysBetween = (date1, date2) => {
  const oneDay = 24 * 60 * 60 * 1000;
  const firstDate = new Date(date1);
  const secondDate = new Date(date2);
  return Math.round(Math.abs((firstDate - secondDate) / oneDay));
};

/**
 * 檢查日期是否有效
 */
export const isValidDate = (date) => {
  return date instanceof Date && !isNaN(date);
};

// 預設匯出所有工具
export default {
  formatDate,
  daysBetween,
  isValidDate
};
```

```javascript
// ✅ main.js - 主要應用程式檔案
import UserService, { USER_ROLES, validateUserRole } from './userService.js';
import dateUtils, { formatDate } from './utils/dateUtils.js';
import { ApiClient } from './apiClient.js';

// 初始化服務
const apiClient = new ApiClient('https://api.example.com');
const userService = new UserService(apiClient);

// 使用模組
async function initApp() {
  try {
    const user = await userService.getUser(1);
    
    if (validateUserRole(user.role)) {
      console.log(`用戶角色驗證通過: ${user.role}`);
    }
    
    const formattedDate = formatDate(user.createdAt, 'YYYY-MM-DD HH:mm');
    console.log(`用戶建立時間: ${formattedDate}`);
    
  } catch (error) {
    console.error('應用程式初始化失敗:', error);
  }
}

initApp();
```

##### 模組組織結構

```
src/
├── components/          # UI 元件
│   ├── Button/
│   │   ├── Button.js
│   │   ├── Button.css
│   │   └── index.js
│   └── Modal/
│       ├── Modal.js
│       ├── Modal.css
│       └── index.js
├── services/           # 業務邏輯服務
│   ├── userService.js
│   ├── authService.js
│   └── dataService.js
├── utils/              # 工具函式
│   ├── dateUtils.js
│   ├── stringUtils.js
│   └── validationUtils.js
├── config/             # 設定檔
│   ├── api.js
│   └── constants.js
├── stores/             # 狀態管理
│   ├── userStore.js
│   └── appStore.js
└── main.js             # 主要入口點
```

#### 3.6.2 重複程式碼抽取共用方法

##### 高階函式 (Higher-Order Functions)

```javascript
// ✅ 防抖函式
function debounce(func, delay) {
  let timeoutId;
  
  return function debounced(...args) {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func.apply(this, args), delay);
  };
}

// ✅ 節流函式
function throttle(func, limit) {
  let inThrottle;
  
  return function throttled(...args) {
    if (!inThrottle) {
      func.apply(this, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
}

// ✅ 記憶化函式
function memoize(func) {
  const cache = new Map();
  
  return function memoized(...args) {
    const key = JSON.stringify(args);
    
    if (cache.has(key)) {
      return cache.get(key);
    }
    
    const result = func.apply(this, args);
    cache.set(key, result);
    return result;
  };
}

// ✅ 重試函式
function withRetry(func, maxRetries = 3, delay = 1000) {
  return async function(...args) {
    let lastError;
    
    for (let attempt = 1; attempt <= maxRetries; attempt++) {
      try {
        return await func.apply(this, args);
      } catch (error) {
        lastError = error;
        
        if (attempt === maxRetries) {
          throw error;
        }
        
        await new Promise(resolve => setTimeout(resolve, delay * attempt));
      }
    }
  };
}

// 使用範例
const debouncedSearch = debounce((query) => {
  console.log('搜尋:', query);
}, 300);

const throttledScroll = throttle(() => {
  console.log('滾動事件');
}, 100);

const memoizedExpensiveFunction = memoize((x, y) => {
  console.log('執行昂貴計算');
  return x * y * Math.random();
});

const retryableApiCall = withRetry(async (url) => {
  const response = await fetch(url);
  if (!response.ok) throw new Error('API 呼叫失敗');
  return response.json();
});
```

##### 設計模式應用

```javascript
// ✅ 工廠模式
class ComponentFactory {
  static createComponent(type, props = {}) {
    const components = {
      button: () => new Button(props),
      modal: () => new Modal(props),
      form: () => new Form(props),
      table: () => new Table(props)
    };
    
    const componentCreator = components[type.toLowerCase()];
    
    if (!componentCreator) {
      throw new Error(`未知的元件類型: ${type}`);
    }
    
    return componentCreator();
  }
}

// ✅ 觀察者模式
class EventEmitter {
  constructor() {
    this.events = new Map();
  }
  
  on(event, listener) {
    if (!this.events.has(event)) {
      this.events.set(event, []);
    }
    
    this.events.get(event).push(listener);
    
    // 返回移除監聽器的函式
    return () => this.off(event, listener);
  }
  
  off(event, listener) {
    if (!this.events.has(event)) return;
    
    const listeners = this.events.get(event);
    const index = listeners.indexOf(listener);
    
    if (index > -1) {
      listeners.splice(index, 1);
    }
  }
  
  emit(event, ...args) {
    if (!this.events.has(event)) return;
    
    const listeners = this.events.get(event);
    listeners.forEach(listener => {
      try {
        listener(...args);
      } catch (error) {
        console.error('事件監聽器執行錯誤:', error);
      }
    });
  }
  
  once(event, listener) {
    const removeListener = this.on(event, (...args) => {
      removeListener();
      listener(...args);
    });
    
    return removeListener;
  }
}

// ✅ 單例模式
class ConfigManager {
  constructor() {
    if (ConfigManager.instance) {
      return ConfigManager.instance;
    }
    
    this.config = new Map();
    ConfigManager.instance = this;
  }
  
  set(key, value) {
    this.config.set(key, value);
  }
  
  get(key, defaultValue = null) {
    return this.config.get(key) || defaultValue;
  }
  
  has(key) {
    return this.config.has(key);
  }
  
  static getInstance() {
    if (!ConfigManager.instance) {
      ConfigManager.instance = new ConfigManager();
    }
    return ConfigManager.instance;
  }
}

// 使用範例
const config = ConfigManager.getInstance();
config.set('apiUrl', 'https://api.example.com');

const eventBus = new EventEmitter();
const button = ComponentFactory.createComponent('button', { text: '點擊我' });
```

#### 3.6.3 安全性注意事項

##### XSS 防護

```javascript
// ✅ HTML 編碼函式
function escapeHtml(unsafe) {
  const entityMap = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#39;',
    '/': '&#x2F;',
    '`': '&#x60;',
    '=': '&#x3D;'
  };
  
  return String(unsafe).replace(/[&<>"'`=\/]/g, (char) => entityMap[char]);
}

// ✅ 安全的 DOM 插入
function safeSetContent(element, content, allowHtml = false) {
  if (!element) {
    throw new Error('DOM 元素不存在');
  }
  
  if (allowHtml) {
    // 如果允許 HTML，使用 DOMPurify 等庫進行清理
    element.innerHTML = content; // 注意：這裡應該使用 DOMPurify.sanitize(content)
  } else {
    // 安全的純文字插入
    element.textContent = content;
  }
}

// ✅ 安全的動態腳本載入
function loadScript(src, integrity = null) {
  return new Promise((resolve, reject) => {
    const script = document.createElement('script');
    script.src = src;
    
    // 加入完整性檢查
    if (integrity) {
      script.integrity = integrity;
      script.crossOrigin = 'anonymous';
    }
    
    script.onload = resolve;
    script.onerror = reject;
    
    document.head.appendChild(script);
  });
}

// ✅ URL 驗證
function isValidUrl(url, allowedDomains = []) {
  try {
    const urlObj = new URL(url);
    
    // 檢查協議
    if (!['http:', 'https:'].includes(urlObj.protocol)) {
      return false;
    }
    
    // 檢查允許的域名
    if (allowedDomains.length > 0) {
      return allowedDomains.some(domain => 
        urlObj.hostname === domain || 
        urlObj.hostname.endsWith(`.${domain}`)
      );
    }
    
    return true;
  } catch {
    return false;
  }
}
```

##### 輸入驗證

```javascript
// ✅ 輸入驗證工具
const ValidationUtils = {
  // 電子郵件驗證
  isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email) && email.length <= 254;
  },
  
  // 電話號碼驗證（台灣）
  isValidPhone(phone) {
    const phoneRegex = /^09\d{8}$/;
    return phoneRegex.test(phone.replace(/[\s-]/g, ''));
  },
  
  // 密碼強度驗證
  isStrongPassword(password) {
    const minLength = 8;
    const hasUpperCase = /[A-Z]/.test(password);
    const hasLowerCase = /[a-z]/.test(password);
    const hasNumbers = /\d/.test(password);
    const hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/.test(password);
    
    return password.length >= minLength && 
           hasUpperCase && 
           hasLowerCase && 
           hasNumbers && 
           hasSpecialChar;
  },
  
  // 身分證字號驗證（台灣）
  isValidTaiwanId(id) {
    if (!/^[A-Z][12]\d{8}$/.test(id)) return false;
    
    const letterMap = {
      A: 10, B: 11, C: 12, D: 13, E: 14, F: 15, G: 16,
      H: 17, I: 34, J: 18, K: 19, L: 20, M: 21, N: 22,
      O: 35, P: 23, Q: 24, R: 25, S: 26, T: 27, U: 28,
      V: 29, W: 32, X: 30, Y: 31, Z: 33
    };
    
    const firstLetter = letterMap[id[0]];
    const checksum = Math.floor(firstLetter / 10) + 
                    (firstLetter % 10) * 9 +
                    Array.from(id.slice(1, 9))
                         .reduce((sum, digit, index) => sum + parseInt(digit) * (8 - index), 0);
    
    return (10 - (checksum % 10)) % 10 === parseInt(id[9]);
  },
  
  // 清理輸入（移除潛在危險字元）
  sanitizeInput(input, options = {}) {
    const {
      allowHtml = false,
      maxLength = 1000,
      trimWhitespace = true
    } = options;
    
    let cleaned = String(input);
    
    if (trimWhitespace) {
      cleaned = cleaned.trim();
    }
    
    if (!allowHtml) {
      cleaned = escapeHtml(cleaned);
    }
    
    if (cleaned.length > maxLength) {
      cleaned = cleaned.substring(0, maxLength);
    }
    
    return cleaned;
  }
};

// ✅ 表單驗證範例
class FormValidator {
  constructor(form) {
    this.form = form;
    this.rules = new Map();
    this.errors = new Map();
  }
  
  addRule(fieldName, validator, errorMessage) {
    if (!this.rules.has(fieldName)) {
      this.rules.set(fieldName, []);
    }
    
    this.rules.get(fieldName).push({ validator, errorMessage });
  }
  
  validate() {
    this.errors.clear();
    let isValid = true;
    
    for (const [fieldName, rules] of this.rules) {
      const field = this.form.querySelector(`[name="${fieldName}"]`);
      
      if (!field) continue;
      
      const value = ValidationUtils.sanitizeInput(field.value);
      
      for (const rule of rules) {
        if (!rule.validator(value)) {
          this.errors.set(fieldName, rule.errorMessage);
          isValid = false;
          break;
        }
      }
    }
    
    this.updateUI();
    return isValid;
  }
  
  updateUI() {
    // 清除所有錯誤狀態
    this.form.querySelectorAll('.error').forEach(el => {
      el.classList.remove('error');
    });
    
    this.form.querySelectorAll('.error-message').forEach(el => {
      el.remove();
    });
    
    // 顯示新的錯誤
    for (const [fieldName, errorMessage] of this.errors) {
      const field = this.form.querySelector(`[name="${fieldName}"]`);
      
      if (field) {
        field.classList.add('error');
        
        const errorEl = document.createElement('div');
        errorEl.className = 'error-message';
        errorEl.textContent = errorMessage;
        field.parentNode.insertBefore(errorEl, field.nextSibling);
      }
    }
  }
}
```

##### 資料傳輸安全

```javascript
// ✅ 安全的資料儲存
class SecureStorage {
  constructor(prefix = 'app_') {
    this.prefix = prefix;
  }
  
  // 加密儲存（簡化版本）
  setSecure(key, value) {
    try {
      const data = JSON.stringify(value);
      const encrypted = btoa(data); // 實際應用應使用更強的加密
      localStorage.setItem(this.prefix + key, encrypted);
    } catch (error) {
      console.error('儲存資料失敗:', error);
    }
  }
  
  // 解密讀取
  getSecure(key, defaultValue = null) {
    try {
      const encrypted = localStorage.getItem(this.prefix + key);
      if (!encrypted) return defaultValue;
      
      const data = atob(encrypted);
      return JSON.parse(data);
    } catch (error) {
      console.error('讀取資料失敗:', error);
      return defaultValue;
    }
  }
  
  // 移除資料
  remove(key) {
    localStorage.removeItem(this.prefix + key);
  }
  
  // 清除所有應用資料
  clear() {
    const keys = Object.keys(localStorage);
    keys.forEach(key => {
      if (key.startsWith(this.prefix)) {
        localStorage.removeItem(key);
      }
    });
  }
}

// ✅ 安全的 API 呼叫
class SecureApiClient {
  constructor(baseUrl) {
    this.baseUrl = baseUrl;
    this.storage = new SecureStorage();
  }
  
  async request(endpoint, options = {}) {
    const token = this.storage.getSecure('authToken');
    
    const config = {
      ...options,
      headers: {
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest', // CSRF 保護
        ...options.headers
      }
    };
    
    // 加入認證標頭
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    
    // 加入 CSRF Token
    const csrfToken = document.querySelector('meta[name="csrf-token"]')?.content;
    if (csrfToken) {
      config.headers['X-CSRF-Token'] = csrfToken;
    }
    
    try {
      const response = await fetch(`${this.baseUrl}${endpoint}`, config);
      
      // 檢查回應狀態
      if (response.status === 401) {
        this.handleAuthError();
        throw new Error('認證過期');
      }
      
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }
      
      return await response.json();
    } catch (error) {
      console.error('API 請求失敗:', error);
      throw error;
    }
  }
  
  handleAuthError() {
    this.storage.remove('authToken');
    this.storage.remove('userInfo');
    
    // 重新導向到登入頁面
    if (typeof window !== 'undefined') {
      window.location.href = '/login';
    }
  }
}
```

#### 3.6.4 效能優化建議

##### Debounce/Throttle 應用

```javascript
// ✅ 搜尋輸入防抖
class SearchComponent {
  constructor(searchInput, onSearch) {
    this.searchInput = searchInput;
    this.onSearch = onSearch;
    this.debouncedSearch = this.debounce(this.handleSearch.bind(this), 300);
    
    this.init();
  }
  
  init() {
    this.searchInput.addEventListener('input', this.debouncedSearch);
  }
  
  debounce(func, delay) {
    let timeoutId;
    return function(...args) {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(() => func.apply(this, args), delay);
    };
  }
  
  handleSearch(event) {
    const query = event.target.value.trim();
    
    if (query.length >= 2) {
      this.onSearch(query);
    }
  }
}

// ✅ 滾動事件節流
class ScrollHandler {
  constructor() {
    this.isScrolling = false;
    this.scrollPosition = 0;
    this.throttledScroll = this.throttle(this.handleScroll.bind(this), 16); // 60fps
    
    window.addEventListener('scroll', this.throttledScroll);
  }
  
  throttle(func, limit) {
    let inThrottle;
    return function(...args) {
      if (!inThrottle) {
        func.apply(this, args);
        inThrottle = true;
        setTimeout(() => inThrottle = false, limit);
      }
    };
  }
  
  handleScroll() {
    this.scrollPosition = window.pageYOffset;
    
    // 執行滾動相關邏輯
    this.updateScrollProgress();
    this.handleStickyElements();
  }
  
  updateScrollProgress() {
    const windowHeight = window.innerHeight;
    const documentHeight = document.documentElement.scrollHeight;
    const progress = (this.scrollPosition / (documentHeight - windowHeight)) * 100;
    
    // 更新進度條
    const progressBar = document.querySelector('.scroll-progress');
    if (progressBar) {
      progressBar.style.width = `${Math.min(progress, 100)}%`;
    }
  }
  
  handleStickyElements() {
    const stickyElements = document.querySelectorAll('[data-sticky]');
    
    stickyElements.forEach(element => {
      const rect = element.getBoundingClientRect();
      const isVisible = rect.top <= 0;
      
      element.classList.toggle('sticky-active', isVisible);
    });
  }
}
```

##### Lazy Loading 實作

```javascript
// ✅ 圖片延遲載入
class LazyImageLoader {
  constructor() {
    this.imageObserver = null;
    this.init();
  }
  
  init() {
    // 檢查瀏覽器支援
    if ('IntersectionObserver' in window) {
      this.setupIntersectionObserver();
    } else {
      // 降級處理：立即載入所有圖片
      this.loadAllImages();
    }
  }
  
  setupIntersectionObserver() {
    const options = {
      root: null,
      rootMargin: '50px', // 提前 50px 載入
      threshold: 0.1
    };
    
    this.imageObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          this.loadImage(entry.target);
          this.imageObserver.unobserve(entry.target);
        }
      });
    }, options);
    
    // 觀察所有延遲載入圖片
    this.observeImages();
  }
  
  observeImages() {
    const lazyImages = document.querySelectorAll('img[data-src]');
    lazyImages.forEach(img => {
      this.imageObserver.observe(img);
    });
  }
  
  loadImage(img) {
    const src = img.dataset.src;
    const srcset = img.dataset.srcset;
    
    if (src) {
      img.src = src;
    }
    
    if (srcset) {
      img.srcset = srcset;
    }
    
    img.classList.add('loaded');
    
    // 移除 data 屬性
    delete img.dataset.src;
    delete img.dataset.srcset;
  }
  
  loadAllImages() {
    const lazyImages = document.querySelectorAll('img[data-src]');
    lazyImages.forEach(img => this.loadImage(img));
  }
}

// ✅ 元件延遲載入
class LazyComponentLoader {
  constructor() {
    this.componentObserver = null;
    this.loadedComponents = new Set();
    this.init();
  }
  
  init() {
    if ('IntersectionObserver' in window) {
      this.setupComponentObserver();
    }
  }
  
  setupComponentObserver() {
    const options = {
      root: null,
      rootMargin: '100px',
      threshold: 0
    };
    
    this.componentObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !this.loadedComponents.has(entry.target)) {
          this.loadComponent(entry.target);
          this.componentObserver.unobserve(entry.target);
        }
      });
    }, options);
    
    this.observeComponents();
  }
  
  observeComponents() {
    const lazyComponents = document.querySelectorAll('[data-lazy-component]');
    lazyComponents.forEach(element => {
      this.componentObserver.observe(element);
    });
  }
  
  async loadComponent(element) {
    const componentName = element.dataset.lazyComponent;
    
    if (this.loadedComponents.has(element)) {
      return;
    }
    
    this.loadedComponents.add(element);
    
    try {
      // 顯示載入狀態
      element.innerHTML = '<div class="loading">載入中...</div>';
      
      // 動態載入元件
      const componentModule = await import(`./components/${componentName}.js`);
      const Component = componentModule.default;
      
      // 初始化元件
      const component = new Component(element);
      await component.render();
      
    } catch (error) {
      console.error(`載入元件失敗: ${componentName}`, error);
      element.innerHTML = '<div class="error">載入失敗</div>';
    }
  }
}
```

##### 記憶體管理

```javascript
// ✅ 事件監聽器管理
class EventManager {
  constructor() {
    this.listeners = new Map();
    this.abortController = new AbortController();
  }
  
  addEventListener(element, event, handler, options = {}) {
    const key = `${element.id || 'element'}-${event}`;
    
    // 使用 AbortController 統一管理
    const eventOptions = {
      ...options,
      signal: this.abortController.signal
    };
    
    element.addEventListener(event, handler, eventOptions);
    
    // 記錄監聽器
    this.listeners.set(key, { element, event, handler });
  }
  
  removeEventListener(element, event, handler) {
    element.removeEventListener(event, handler);
    
    const key = `${element.id || 'element'}-${event}`;
    this.listeners.delete(key);
  }
  
  removeAllListeners() {
    // 使用 AbortController 一次移除所有監聽器
    this.abortController.abort();
    this.listeners.clear();
    
    // 建立新的 AbortController
    this.abortController = new AbortController();
  }
  
  destroy() {
    this.removeAllListeners();
  }
}

// ✅ 快取管理
class CacheManager {
  constructor(maxSize = 100, ttl = 5 * 60 * 1000) { // 5分鐘 TTL
    this.cache = new Map();
    this.maxSize = maxSize;
    this.ttl = ttl;
    this.accessOrder = [];
  }
  
  set(key, value) {
    const now = Date.now();
    
    // 如果已存在，更新存取順序
    if (this.cache.has(key)) {
      this.updateAccessOrder(key);
    } else {
      // 檢查大小限制
      if (this.cache.size >= this.maxSize) {
        this.evictLRU();
      }
      
      this.accessOrder.push(key);
    }
    
    this.cache.set(key, {
      value,
      timestamp: now,
      accessCount: 1
    });
  }
  
  get(key) {
    const item = this.cache.get(key);
    
    if (!item) {
      return null;
    }
    
    // 檢查是否過期
    if (Date.now() - item.timestamp > this.ttl) {
      this.delete(key);
      return null;
    }
    
    // 更新存取記錄
    item.accessCount++;
    this.updateAccessOrder(key);
    
    return item.value;
  }
  
  delete(key) {
    this.cache.delete(key);
    const index = this.accessOrder.indexOf(key);
    if (index > -1) {
      this.accessOrder.splice(index, 1);
    }
  }
  
  updateAccessOrder(key) {
    const index = this.accessOrder.indexOf(key);
    if (index > -1) {
      this.accessOrder.splice(index, 1);
    }
    this.accessOrder.push(key);
  }
  
  evictLRU() {
    if (this.accessOrder.length > 0) {
      const lruKey = this.accessOrder.shift();
      this.cache.delete(lruKey);
    }
  }
  
  clear() {
    this.cache.clear();
    this.accessOrder = [];
  }
  
  // 清理過期項目
  cleanup() {
    const now = Date.now();
    const expiredKeys = [];
    
    for (const [key, item] of this.cache) {
      if (now - item.timestamp > this.ttl) {
        expiredKeys.push(key);
      }
    }
    
    expiredKeys.forEach(key => this.delete(key));
  }
}

// ✅ 資源清理工具
class ResourceCleaner {
  constructor() {
    this.resources = new Set();
    this.intervals = new Set();
    this.timeouts = new Set();
    
    // 頁面卸載時自動清理
    window.addEventListener('beforeunload', () => this.cleanup());
  }
  
  addResource(resource) {
    this.resources.add(resource);
  }
  
  addInterval(intervalId) {
    this.intervals.add(intervalId);
  }
  
  addTimeout(timeoutId) {
    this.timeouts.add(timeoutId);
  }
  
  cleanup() {
    // 清理定時器
    this.intervals.forEach(id => clearInterval(id));
    this.timeouts.forEach(id => clearTimeout(id));
    
    // 清理其他資源
    this.resources.forEach(resource => {
      if (typeof resource.destroy === 'function') {
        resource.destroy();
      } else if (typeof resource.disconnect === 'function') {
        resource.disconnect();
      } else if (typeof resource.abort === 'function') {
        resource.abort();
      }
    });
    
    // 清空集合
    this.resources.clear();
    this.intervals.clear();
    this.timeouts.clear();
  }
}
```

---

### 3.7 測試與除錯

#### 3.7.1 使用瀏覽器 DevTools 進行除錯

##### Console 除錯技巧

```javascript
// ✅ 進階 console 用法
class DebugUtils {
  static log(message, data = null, level = 'info') {
    const timestamp = new Date().toISOString();
    const styles = {
      info: 'color: #2196F3',
      warn: 'color: #FF9800',
      error: 'color: #F44336',
      success: 'color: #4CAF50'
    };
    
    console.log(
      `%c[${timestamp}] ${message}`,
      styles[level] || styles.info,
      data || ''
    );
  }
  
  static group(title, callback) {
    console.group(title);
    try {
      callback();
    } finally {
      console.groupEnd();
    }
  }
  
  static table(data, columns = null) {
    if (Array.isArray(data) || typeof data === 'object') {
      console.table(data, columns);
    } else {
      console.log('table() 需要陣列或物件格式的資料');
    }
  }
  
  static time(label = 'default') {
    console.time(label);
  }
  
  static timeEnd(label = 'default') {
    console.timeEnd(label);
  }
  
  static trace(message = '') {
    console.trace(message);
  }
  
  static assert(condition, message) {
    console.assert(condition, message);
  }
}

// 使用範例
DebugUtils.log('使用者登入', { userId: 123, email: 'user@example.com' }, 'info');

DebugUtils.group('API 呼叫詳情', () => {
  DebugUtils.log('請求 URL', '/api/users');
  DebugUtils.log('請求方法', 'GET');
  DebugUtils.log('回應狀態', '200 OK');
});

DebugUtils.time('資料處理');
// ... 處理資料的程式碼
DebugUtils.timeEnd('資料處理');
```

##### 效能監控

```javascript
// ✅ 效能監控工具
class PerformanceMonitor {
  constructor() {
    this.metrics = new Map();
    this.observers = [];
    this.init();
  }
  
  init() {
    // 監控頁面載入效能
    this.observePageLoad();
    
    // 監控長任務
    this.observeLongTasks();
    
    // 監控視覺穩定性
    this.observeLayoutShift();
  }
  
  observePageLoad() {
    window.addEventListener('load', () => {
      const navigation = performance.getEntriesByType('navigation')[0];
      
      this.metrics.set('頁面載入', {
        DNS解析: navigation.domainLookupEnd - navigation.domainLookupStart,
        TCP連接: navigation.connectEnd - navigation.connectStart,
        請求時間: navigation.responseStart - navigation.requestStart,
        回應時間: navigation.responseEnd - navigation.responseStart,
        DOM解析: navigation.domContentLoadedEventEnd - navigation.domContentLoadedEventStart,
        完整載入: navigation.loadEventEnd - navigation.navigationStart
      });
      
      console.table(this.metrics.get('頁面載入'));
    });
  }
  
  observeLongTasks() {
    if ('PerformanceObserver' in window) {
      const observer = new PerformanceObserver((list) => {
        const longTasks = list.getEntries();
        
        longTasks.forEach(task => {
          console.warn(`檢測到長任務: ${task.duration.toFixed(2)}ms`, task);
          
          if (task.duration > 100) {
            this.reportPerformanceIssue('長任務', {
              duration: task.duration,
              startTime: task.startTime
            });
          }
        });
      });
      
      observer.observe({ entryTypes: ['longtask'] });
      this.observers.push(observer);
    }
  }
  
  observeLayoutShift() {
    if ('PerformanceObserver' in window) {
      let cumulativeLayoutShift = 0;
      
      const observer = new PerformanceObserver((list) => {
        const shifts = list.getEntries();
        
        shifts.forEach(shift => {
          if (!shift.hadRecentInput) {
            cumulativeLayoutShift += shift.value;
          }
        });
        
        this.metrics.set('版面偏移', cumulativeLayoutShift);
        
        if (cumulativeLayoutShift > 0.1) {
          console.warn(`累積版面偏移過高: ${cumulativeLayoutShift.toFixed(4)}`);
        }
      });
      
      observer.observe({ entryTypes: ['layout-shift'] });
      this.observers.push(observer);
    }
  }
  
  measureFunction(func, label) {
    const start = performance.now();
    const result = func();
    const end = performance.now();
    
    console.log(`${label} 執行時間: ${(end - start).toFixed(2)}ms`);
    return result;
  }
  
  async measureAsync(asyncFunc, label) {
    const start = performance.now();
    const result = await asyncFunc();
    const end = performance.now();
    
    console.log(`${label} 執行時間: ${(end - start).toFixed(2)}ms`);
    return result;
  }
  
  reportPerformanceIssue(type, data) {
    // 發送效能問題報告到監控系統
    console.warn(`效能問題 - ${type}:`, data);
  }
  
  getMetrics() {
    return Object.fromEntries(this.metrics);
  }
  
  destroy() {
    this.observers.forEach(observer => observer.disconnect());
    this.observers = [];
    this.metrics.clear();
  }
}

// 使用範例
const perfMonitor = new PerformanceMonitor();

// 測量函式效能
const result = perfMonitor.measureFunction(() => {
  return Array.from({ length: 100000 }, (_, i) => i * 2);
}, '陣列運算');

// 測量非同步函式效能
perfMonitor.measureAsync(async () => {
  const response = await fetch('/api/data');
  return response.json();
}, 'API 呼叫');
```

#### 3.7.2 基本單元測試 (Jest/Vitest)

##### 基本測試結構

```javascript
// ✅ utils.test.js
import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest';
import { formatDate, validateEmail, debounce } from '../src/utils';

describe('工具函式測試', () => {
  describe('formatDate', () => {
    it('應該正確格式化日期', () => {
      const date = new Date('2024-01-15T10:30:00Z');
      const result = formatDate(date, 'YYYY-MM-DD');
      expect(result).toBe('2024-01-15');
    });
    
    it('應該處理無效日期', () => {
      const result = formatDate(null);
      expect(result).toBe('Invalid Date');
    });
    
    it('應該使用預設格式', () => {
      const date = new Date('2024-01-15T10:30:00Z');
      const result = formatDate(date);
      expect(result).toMatch(/^\d{4}-\d{2}-\d{2}$/);
    });
  });
  
  describe('validateEmail', () => {
    it('應該驗證有效的電子郵件', () => {
      expect(validateEmail('user@example.com')).toBe(true);
      expect(validateEmail('test.email+tag@domain.co.uk')).toBe(true);
    });
    
    it('應該拒絕無效的電子郵件', () => {
      expect(validateEmail('invalid')).toBe(false);
      expect(validateEmail('user@')).toBe(false);
      expect(validateEmail('@domain.com')).toBe(false);
      expect(validateEmail('')).toBe(false);
    });
  });
  
  describe('debounce', () => {
    beforeEach(() => {
      vi.useFakeTimers();
    });
    
    afterEach(() => {
      vi.useRealTimers();
    });
    
    it('應該延遲函式執行', () => {
      const mockFn = vi.fn();
      const debouncedFn = debounce(mockFn, 100);
      
      debouncedFn();
      expect(mockFn).not.toHaveBeenCalled();
      
      vi.advanceTimersByTime(100);
      expect(mockFn).toHaveBeenCalledTimes(1);
    });
    
    it('應該在新呼叫時重置計時器', () => {
      const mockFn = vi.fn();
      const debouncedFn = debounce(mockFn, 100);
      
      debouncedFn();
      vi.advanceTimersByTime(50);
      debouncedFn(); // 重置計時器
      
      vi.advanceTimersByTime(50);
      expect(mockFn).not.toHaveBeenCalled();
      
      vi.advanceTimersByTime(50);
      expect(mockFn).toHaveBeenCalledTimes(1);
    });
  });
});
```

##### API 測試

```javascript
// ✅ apiClient.test.js
import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest';
import { ApiClient } from '../src/services/apiClient';

// Mock fetch
global.fetch = vi.fn();

describe('ApiClient', () => {
  let apiClient;
  
  beforeEach(() => {
    apiClient = new ApiClient('https://api.example.com');
    fetch.mockClear();
  });
  
  afterEach(() => {
    vi.restoreAllMocks();
  });
  
  describe('GET 請求', () => {
    it('應該發送正確的 GET 請求', async () => {
      const mockResponse = { data: { id: 1, name: 'Test User' } };
      
      fetch.mockResolvedValueOnce({
        ok: true,
        json: async () => mockResponse
      });
      
      const result = await apiClient.get('/users/1');
      
      expect(fetch).toHaveBeenCalledWith(
        'https://api.example.com/users/1',
        expect.objectContaining({
          method: 'GET',
          headers: expect.objectContaining({
            'Content-Type': 'application/json'
          })
        })
      );
      
      expect(result).toEqual(mockResponse);
    });
    
    it('應該處理查詢參數', async () => {
      fetch.mockResolvedValueOnce({
        ok: true,
        json: async () => ({ data: [] })
      });
      
      await apiClient.get('/users', { page: 1, limit: 10 });
      
      expect(fetch).toHaveBeenCalledWith(
        'https://api.example.com/users?page=1&limit=10',
        expect.any(Object)
      );
    });
  });
  
  describe('POST 請求', () => {
    it('應該發送正確的 POST 請求', async () => {
      const userData = { name: 'New User', email: 'user@example.com' };
      const mockResponse = { data: { id: 1, ...userData } };
      
      fetch.mockResolvedValueOnce({
        ok: true,
        json: async () => mockResponse
      });
      
      const result = await apiClient.post('/users', userData);
      
      expect(fetch).toHaveBeenCalledWith(
        'https://api.example.com/users',
        expect.objectContaining({
          method: 'POST',
          headers: expect.objectContaining({
            'Content-Type': 'application/json'
          }),
          body: JSON.stringify(userData)
        })
      );
      
      expect(result).toEqual(mockResponse);
    });
  });
  
  describe('錯誤處理', () => {
    it('應該處理網路錯誤', async () => {
      fetch.mockRejectedValueOnce(new Error('Network Error'));
      
      await expect(apiClient.get('/users')).rejects.toThrow('Network Error');
    });
    
    it('應該處理 HTTP 錯誤狀態', async () => {
      fetch.mockResolvedValueOnce({
        ok: false,
        status: 404,
        statusText: 'Not Found'
      });
      
      await expect(apiClient.get('/users/999')).rejects.toThrow('HTTP 404: Not Found');
    });
    
    it('應該處理超時', async () => {
      const mockAbortError = new Error('超時');
      mockAbortError.name = 'AbortError';
      
      fetch.mockRejectedValueOnce(mockAbortError);
      
      await expect(apiClient.get('/users')).rejects.toThrow('請求超時');
    });
  });
});
```

##### 元件測試

```javascript
// ✅ userForm.test.js
import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest';
import { JSDOM } from 'jsdom';
import { UserForm } from '../src/components/UserForm';

describe('UserForm 元件', () => {
  let dom;
  let document;
  let userForm;
  
  beforeEach(() => {
    dom = new JSDOM(`
      <form id="userForm">
        <input name="name" type="text" />
        <input name="email" type="email" />
        <input name="password" type="password" />
        <button type="submit">提交</button>
      </form>
    `);
    
    global.document = dom.window.document;
    global.window = dom.window;
    
    userForm = new UserForm('#userForm');
  });
  
  afterEach(() => {
    userForm.destroy();
  });
  
  it('應該正確初始化表單', () => {
    expect(userForm.form).toBeTruthy();
    expect(userForm.validators.size).toBeGreaterThan(0);
  });
  
  it('應該驗證必填欄位', () => {
    const nameField = document.querySelector('[name="name"]');
    nameField.value = '';
    
    const isValid = userForm.validateField(nameField);
    expect(isValid).toBe(false);
    expect(nameField.classList.contains('invalid')).toBe(true);
  });
  
  it('應該驗證電子郵件格式', () => {
    const emailField = document.querySelector('[name="email"]');
    
    // 無效的電子郵件
    emailField.value = 'invalid-email';
    expect(userForm.validateField(emailField)).toBe(false);
    
    // 有效的電子郵件
    emailField.value = 'user@example.com';
    expect(userForm.validateField(emailField)).toBe(true);
  });
  
  it('應該阻止無效表單提交', async () => {
    const submitHandler = vi.fn();
    userForm.onSubmit = submitHandler;
    
    const form = document.querySelector('#userForm');
    const submitEvent = new dom.window.Event('submit');
    
    form.dispatchEvent(submitEvent);
    
    expect(submitHandler).not.toHaveBeenCalled();
  });
  
  it('應該提交有效表單', async () => {
    // 填入有效資料
    document.querySelector('[name="name"]').value = 'Test User';
    document.querySelector('[name="email"]').value = 'test@example.com';
    document.querySelector('[name="password"]').value = 'password123';
    
    const submitHandler = vi.fn().mockResolvedValue({ success: true });
    userForm.onSubmit = submitHandler;
    
    const form = document.querySelector('#userForm');
    const submitEvent = new dom.window.Event('submit');
    
    await form.dispatchEvent(submitEvent);
    
    expect(submitHandler).toHaveBeenCalledWith({
      name: 'Test User',
      email: 'test@example.com',
      password: 'password123'
    });
  });
});
```

---

## 4. 現代開發工具與 TypeScript

### 4.1 TypeScript 基礎

#### 4.1.1 TypeScript 簡介

TypeScript 是 Microsoft 開發的 JavaScript 超集合，加入了靜態型別檢查功能，可以在編譯時期發現錯誤，提升程式碼品質和開發效率。

**TypeScript 的優勢：**

```typescript
// ✅ 型別安全
interface User {
  id: number;
  name: string;
  email: string;
  isActive?: boolean; // 可選屬性
}

function getUserInfo(user: User): string {
  return `${user.name} (${user.email})`;
}

// 編譯時期就會檢查型別錯誤
const user: User = {
  id: 1,
  name: "Alice",
  email: "alice@example.com"
};

console.log(getUserInfo(user)); // ✅ 正確
// console.log(getUserInfo("invalid")); // ❌ 編譯錯誤
```

#### 4.1.2 基本型別系統

```typescript
// ✅ 基本型別
let isDone: boolean = false;
let count: number = 42;
let userName: string = "Alice";
let list: number[] = [1, 2, 3];
let tuple: [string, number] = ["hello", 10];

// ✅ 聯合型別
type Status = "pending" | "approved" | "rejected";
let currentStatus: Status = "pending";

// ✅ 字面量型別
type ButtonSize = "small" | "medium" | "large";
interface ButtonProps {
  size: ButtonSize;
  variant: "primary" | "secondary";
  disabled?: boolean;
}

// ✅ 泛型
function identity<T>(arg: T): T {
  return arg;
}

const stringResult = identity<string>("hello");
const numberResult = identity<number>(42);

// ✅ 陣列和物件型別
interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}

type UserList = ApiResponse<User[]>;
type UserDetail = ApiResponse<User>;
```

#### 4.1.3 類別和介面

```typescript
// ✅ 介面定義
interface Drawable {
  draw(): void;
}

interface Movable {
  move(x: number, y: number): void;
}

// ✅ 類別實作介面
class Circle implements Drawable, Movable {
  constructor(
    private radius: number,
    private x: number = 0,
    private y: number = 0
  ) {}
  
  draw(): void {
    console.log(`Drawing circle with radius ${this.radius}`);
  }
  
  move(x: number, y: number): void {
    this.x = x;
    this.y = y;
  }
  
  // Getter 和 Setter
  get area(): number {
    return Math.PI * this.radius ** 2;
  }
  
  set radiusValue(value: number) {
    if (value > 0) {
      this.radius = value;
    }
  }
}

// ✅ 抽象類別
abstract class Shape {
  abstract area(): number;
  
  describe(): string {
    return `This shape has an area of ${this.area()}`;
  }
}

class Rectangle extends Shape {
  constructor(
    private width: number,
    private height: number
  ) {
    super();
  }
  
  area(): number {
    return this.width * this.height;
  }
}
```

#### 4.1.4 進階型別

```typescript
// ✅ 條件型別
type NonNullable<T> = T extends null | undefined ? never : T;

// ✅ 映射型別
type Partial<T> = {
  [P in keyof T]?: T[P];
};

type Required<T> = {
  [P in keyof T]-?: T[P];
};

// ✅ 工具型別使用
interface UserForm {
  name: string;
  email: string;
  password: string;
  confirmPassword: string;
}

type UserCreateData = Omit<UserForm, 'confirmPassword'>;
type UserUpdateData = Partial<UserCreateData>;

// ✅ 函式型別
type EventHandler<T = any> = (event: T) => void;
type AsyncFunction<T, R> = (args: T) => Promise<R>;

const handleClick: EventHandler<MouseEvent> = (event) => {
  console.log('Button clicked', event.target);
};

const fetchUser: AsyncFunction<number, User> = async (userId) => {
  const response = await fetch(`/api/users/${userId}`);
  return response.json();
};
```

#### 4.1.5 TypeScript 設定

```json
// tsconfig.json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "preserve",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": [
    "src/**/*"
  ],
  "exclude": [
    "node_modules",
    "dist"
  ]
}
```

### 4.2 建置工具

#### 4.2.1 Vite 開發環境

Vite 是新一代的前端建置工具，提供極快的開發伺服器和最佳化的生產建置。

```javascript
// vite.config.js
import { defineConfig } from 'vite';

export default defineConfig({
  root: './src',
  server: {
    port: 3000,
    open: true,
    cors: true
  },
  build: {
    outDir: '../dist',
    sourcemap: true,
    minify: 'terser',
    rollupOptions: {
      input: {
        main: './src/index.html',
        about: './src/about.html'
      }
    }
  },
  resolve: {
    alias: {
      '@': new URL('./src', import.meta.url).pathname
    }
  }
});
```

#### 4.2.2 Webpack 設定範例

```javascript
// webpack.config.js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: '[name].[contenthash].js',
    path: path.resolve(__dirname, 'dist'),
    clean: true
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env']
          }
        }
      },
      {
        test: /\.css$/,
        use: [MiniCssExtractPlugin.loader, 'css-loader']
      },
      {
        test: /\.(png|svg|jpg|jpeg|gif)$/i,
        type: 'asset/resource'
      }
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html'
    }),
    new MiniCssExtractPlugin({
      filename: '[name].[contenthash].css'
    })
  ],
  optimization: {
    splitChunks: {
      chunks: 'all'
    }
  }
};
```

#### 4.2.3 ESLint 和 Prettier 整合

```json
// .eslintrc.json
{
  "env": {
    "browser": true,
    "es2021": true,
    "node": true
  },
  "extends": [
    "eslint:recommended",
    "@typescript-eslint/recommended",
    "prettier"
  ],
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaVersion": "latest",
    "sourceType": "module"
  },
  "plugins": [
    "@typescript-eslint"
  ],
  "rules": {
    "indent": ["error", 2],
    "quotes": ["error", "single"],
    "semi": ["error", "always"],
    "@typescript-eslint/no-unused-vars": "error",
    "@typescript-eslint/explicit-function-return-type": "warn"
  }
}
```

```json
// .prettierrc
{
  "singleQuote": true,
  "trailingComma": "es5",
  "tabWidth": 2,
  "semi": true,
  "printWidth": 80,
  "bracketSpacing": true,
  "arrowParens": "avoid",
  "endOfLine": "lf"
}
```

#### 4.2.4 Package.json 腳本

```json
{
  "name": "modern-web-project",
  "version": "1.0.0",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview",
    "lint": "eslint src --ext .js,.ts,.tsx",
    "lint:fix": "eslint src --ext .js,.ts,.tsx --fix",
    "format": "prettier --write src/**/*.{js,ts,tsx,css,json}",
    "type-check": "tsc --noEmit",
    "test": "vitest",
    "test:ui": "vitest --ui",
    "test:coverage": "vitest --coverage"
  },
  "devDependencies": {
    "@typescript-eslint/eslint-plugin": "^6.0.0",
    "@typescript-eslint/parser": "^6.0.0",
    "eslint": "^8.0.0",
    "prettier": "^3.0.0",
    "typescript": "^5.0.0",
    "vite": "^4.0.0",
    "vitest": "^0.34.0"
  }
}
```

---

## 5. 學習資源與進階閱讀

### 5.1 官方文件與標準

#### 5.1.1 核心文件

- **MDN Web Docs**: <https://developer.mozilla.org/zh-TW/docs/Web/JavaScript>
  - 最權威的 JavaScript 文件
  - 包含完整的 API 參考和範例
  - 定期更新，涵蓋最新標準

- **ECMAScript 規範**: <https://tc39.es/ecma262/>
  - JavaScript 語言的正式規範
  - 了解語言特性的官方定義
  - 追蹤新功能的提案進度

- **TC39 提案**: <https://github.com/tc39/proposals>
  - JavaScript 新功能的提案狀態
  - 了解未來語言發展方向

#### 5.1.2 瀏覽器相容性

- **Can I Use**: <https://caniuse.com/>
  - 檢查 Web API 和 JavaScript 功能的瀏覽器支援度
  - 規劃功能實作的重要參考

- **MDN 相容性表**: 每個 API 頁面都有詳細的瀏覽器支援資訊

### 5.2 推薦學習資源

#### 5.2.1 線上教學平台

- **JavaScript.info**: <https://javascript.info/>
  - 系統性的 JavaScript 教學
  - 從基礎到進階的完整課程
  - 豐富的範例和練習

- **FreeCodeCamp**: <https://www.freecodecamp.org/>
  - 免費的程式設計課程
  - 實作導向的學習方式
  - 包含認證和專案

- **Codecademy**: <https://www.codecademy.com/learn/introduction-to-javascript>
  - 互動式學習平台
  - 結構化的課程設計

#### 5.2.2 書籍推薦

- **《JavaScript: The Good Parts》** by Douglas Crockford
  - 經典的 JavaScript 入門書
  - 重點介紹語言的精華部分

- **《Eloquent JavaScript》** by Marijn Haverbeke
  - 免費線上閱讀：<https://eloquentjavascript.net/>
  - 深入淺出的程式設計思維

- **《You Don't Know JS》** by Kyle Simpson
  - 免費 GitHub 系列：<https://github.com/getify/You-Dont-Know-JS>
  - 深度探討 JavaScript 核心概念

### 5.3 實務工具與框架

#### 5.3.1 開發工具

- **VS Code 擴充功能**:
  - ESLint: 程式碼品質檢查
  - Prettier: 程式碼格式化
  - JavaScript (ES6) code snippets: 程式碼片段
  - Bracket Pair Colorizer: 括號配對
  - Live Server: 本地開發伺服器

- **瀏覽器開發者工具**:
  - Chrome DevTools
  - Firefox Developer Tools
  - Performance profiling
  - Network monitoring

#### 5.3.2 測試工具

- **單元測試**:
  - Jest: <https://jestjs.io/>
  - Vitest: <https://vitest.dev/>
  - Mocha: <https://mochajs.org/>

- **端對端測試**:
  - Cypress: <https://www.cypress.io/>
  - Playwright: <https://playwright.dev/>

#### 5.3.3 建置工具

- **模組打包器**:
  - Vite: <https://vitejs.dev/>
  - Webpack: <https://webpack.js.org/>
  - Rollup: <https://rollupjs.org/>

- **任務執行器**:
  - npm scripts
  - Gulp: <https://gulpjs.com/>

### 5.4 社群與資源

#### 5.4.1 技術社群

- **Stack Overflow**: <https://stackoverflow.com/questions/tagged/javascript>
  - 程式設計問題解答
  - 搜尋常見問題的解決方案

- **GitHub**: <https://github.com/topics/javascript>
  - 開源專案學習
  - 閱讀優質程式碼

- **Reddit**: <https://www.reddit.com/r/javascript/>
  - 技術討論和新聞

#### 5.4.2 技術部落格與資源

- **CSS-Tricks**: <https://css-tricks.com/>
  - 前端開發技術文章

- **Smashing Magazine**: <https://www.smashingmagazine.com/>
  - Web 開發最佳實務

- **Dev.to**: <https://dev.to/t/javascript>
  - 開發者社群文章分享

### 5.5 持續學習建議

#### 5.5.1 學習路徑

1. **基礎階段**:
   - 掌握語言基本語法
   - 理解 DOM 操作
   - 學習事件處理

2. **進階階段**:
   - 非同步程式設計
   - 模組化開發
   - 測試驅動開發

3. **專精階段**:
   - 效能優化
   - 架構設計
   - 開源貢獻

#### 5.5.2 實作專案建議

- **入門專案**:
  - 計算機應用程式
  - 待辦事項清單
  - 簡易部落格

- **進階專案**:
  - 單頁應用程式 (SPA)
  - 即時聊天應用
  - 資料視覺化儀表板

- **挑戰專案**:
  - 建立自己的框架
  - 貢獻開源專案
  - 效能優化案例研究

---

## 6. 開發檢查清單

### 6.1 程式碼品質檢查

#### 6.1.1 語法與風格

- [ ] 使用 `const` 和 `let`，避免 `var`
- [ ] 箭頭函式使用適當（避免在物件方法中使用）
- [ ] 模板字串用於字串拼接
- [ ] 解構賦值簡化程式碼
- [ ] 函式和變數使用有意義的命名
- [ ] 程式碼縮排一致（建議 2 個空格）
- [ ] 行尾統一使用分號
- [ ] 單引號或雙引號使用一致

#### 6.1.2 函式設計

- [ ] 函式職責單一，功能明確
- [ ] 函式參數數量合理（建議不超過 3 個）
- [ ] 使用純函式減少副作用
- [ ] 函式有適當的 JSDoc 註解
- [ ] 錯誤處理完整
- [ ] 回傳值類型一致

#### 6.1.3 效能考量

- [ ] 避免在迴圈中進行 DOM 操作
- [ ] 使用事件委派處理大量元素
- [ ] 快取頻繁使用的 DOM 元素
- [ ] 長任務使用 Web Workers
- [ ] 圖片和資源使用延遲載入
- [ ] 防抖和節流應用於適當場景

### 6.2 安全性檢查

#### 6.2.1 輸入驗證

- [ ] 所有使用者輸入都經過驗證
- [ ] 使用 HTML 編碼防止 XSS
- [ ] URL 驗證防止開放重新導向
- [ ] 檔案上傳類型和大小限制
- [ ] SQL 注入防護（如果直接處理資料庫）

#### 6.2.2 資料保護

- [ ] 敏感資料不儲存在客戶端
- [ ] 使用 HTTPS 傳輸敏感資料
- [ ] JWT Token 安全儲存和驗證
- [ ] CSRF Token 保護表單提交
- [ ] 適當的 CORS 設定

### 6.3 API 整合檢查

#### 6.3.1 請求處理

- [ ] 所有 API 呼叫都有錯誤處理
- [ ] 超時設定合理
- [ ] 重試機制適當實作
- [ ] 載入狀態正確顯示
- [ ] 認證 Token 自動更新

#### 6.3.2 資料處理

- [ ] API 回應資料驗證
- [ ] 空資料狀態處理
- [ ] 分頁功能正常運作
- [ ] 快取策略合理
- [ ] 資料同步機制可靠

### 6.4 使用者體驗檢查

#### 6.4.1 互動回饋

- [ ] 載入狀態視覺回饋
- [ ] 操作成功/失敗訊息
- [ ] 表單驗證即時回饋
- [ ] 按鈕點擊回饋
- [ ] 鍵盤導航支援

#### 6.4.2 響應式設計

- [ ] 行動裝置適配
- [ ] 觸控操作友善
- [ ] 視窗大小調整適應
- [ ] 文字大小合適
- [ ] 圖片自適應載入

### 6.5 測試檢查

#### 6.5.1 單元測試

- [ ] 關鍵業務邏輯有單元測試
- [ ] 測試覆蓋率達到要求（建議 > 80%）
- [ ] 邊界條件和錯誤情況有測試
- [ ] Mock 和 Stub 使用適當
- [ ] 測試案例易讀易懂

#### 6.5.2 整合測試

- [ ] API 整合測試完整
- [ ] 元件互動測試通過
- [ ] 端到端關鍵流程測試
- [ ] 瀏覽器相容性測試
- [ ] 效能測試符合需求

### 6.6 部署前檢查

#### 6.6.1 建置和打包

- [ ] 程式碼成功建置無錯誤
- [ ] 靜態資源路徑正確
- [ ] 生產環境設定檔正確
- [ ] 第三方依賴版本穩定
- [ ] 檔案大小優化

#### 6.6.2 環境配置

- [ ] 環境變數設定正確
- [ ] 資料庫連線設定驗證
- [ ] 外部服務 API 金鑰配置
- [ ] 快取設定適當
- [ ] 日誌級別設定正確

### 6.7 維護檢查

#### 6.7.1 程式碼維護

- [ ] 程式碼有適當註解
- [ ] 依賴套件定期更新
- [ ] 漏洞掃描和修復
- [ ] 效能監控和優化
- [ ] 錯誤監控和回報

#### 6.7.2 文件維護

- [ ] API 文件保持最新
- [ ] 部署說明文件完整
- [ ] 故障排除指南更新
- [ ] 開發環境設定文件
- [ ] 變更日誌維護

### 6.8 檢查清單使用範例

```javascript
// ✅ 自動化檢查清單工具
class DevelopmentChecklist {
  constructor() {
    this.checks = new Map();
    this.results = new Map();
    this.init();
  }
  
  init() {
    // 註冊檢查項目
    this.registerChecks();
  }
  
  registerChecks() {
    // 程式碼品質檢查
    this.addCheck('code-style', '程式碼風格檢查', this.checkCodeStyle);
    this.addCheck('eslint', 'ESLint 檢查', this.checkESLint);
    this.addCheck('performance', '效能檢查', this.checkPerformance);
    
    // 安全性檢查
    this.addCheck('xss-protection', 'XSS 防護檢查', this.checkXSSProtection);
    this.addCheck('input-validation', '輸入驗證檢查', this.checkInputValidation);
    
    // 測試檢查
    this.addCheck('unit-tests', '單元測試', this.checkUnitTests);
    this.addCheck('coverage', '測試覆蓋率', this.checkTestCoverage);
  }
  
  addCheck(id, name, checkFunction) {
    this.checks.set(id, { name, check: checkFunction });
  }
  
  async runAllChecks() {
    console.log('🔍 開始執行開發檢查清單...\n');
    
    for (const [id, { name, check }] of this.checks) {
      try {
        console.log(`⏳ 執行檢查: ${name}`);
        const result = await check();
        this.results.set(id, { passed: result.passed, message: result.message });
        
        if (result.passed) {
          console.log(`✅ ${name}: 通過`);
        } else {
          console.log(`❌ ${name}: ${result.message}`);
        }
      } catch (error) {
        console.log(`💥 ${name}: 檢查失敗 - ${error.message}`);
        this.results.set(id, { passed: false, message: error.message });
      }
    }
    
    this.generateReport();
  }
  
  // 程式碼風格檢查
  async checkCodeStyle() {
    const issues = [];
    
    // 檢查是否使用 const/let
    const codeFiles = await this.getJavaScriptFiles();
    for (const file of codeFiles) {
      const content = await this.readFile(file);
      if (content.includes('var ') && !content.includes('// allow-var')) {
        issues.push(`${file}: 發現使用 var 關鍵字`);
      }
    }
    
    return {
      passed: issues.length === 0,
      message: issues.length > 0 ? issues.join('\n') : '程式碼風格符合規範'
    };
  }
  
  // ESLint 檢查
  async checkESLint() {
    try {
      const result = await this.runCommand('npx eslint src/ --format json');
      const lintResults = JSON.parse(result);
      
      const errorCount = lintResults.reduce((sum, file) => sum + file.errorCount, 0);
      const warningCount = lintResults.reduce((sum, file) => sum + file.warningCount, 0);
      
      return {
        passed: errorCount === 0,
        message: errorCount > 0 
          ? `發現 ${errorCount} 個錯誤, ${warningCount} 個警告` 
          : 'ESLint 檢查通過'
      };
    } catch (error) {
      return { passed: false, message: 'ESLint 執行失敗' };
    }
  }
  
  // 效能檢查
  async checkPerformance() {
    const issues = [];
    
    // 檢查是否有大型 bundle
    const bundleSize = await this.getBundleSize();
    if (bundleSize > 1024 * 1024) { // 1MB
      issues.push(`Bundle 大小過大: ${(bundleSize / 1024 / 1024).toFixed(2)}MB`);
    }
    
    // 檢查是否有未使用的依賴
    const unusedDeps = await this.getUnusedDependencies();
    if (unusedDeps.length > 0) {
      issues.push(`發現未使用的依賴: ${unusedDeps.join(', ')}`);
    }
    
    return {
      passed: issues.length === 0,
      message: issues.length > 0 ? issues.join('\n') : '效能檢查通過'
    };
  }
  
  // XSS 防護檢查
  async checkXSSProtection() {
    const issues = [];
    const codeFiles = await this.getJavaScriptFiles();
    
    for (const file of codeFiles) {
      const content = await this.readFile(file);
      
      // 檢查是否有不安全的 innerHTML 使用
      if (content.match(/\.innerHTML\s*=\s*[^'"`]/)) {
        issues.push(`${file}: 發現可能不安全的 innerHTML 使用`);
      }
      
      // 檢查是否有 eval 使用
      if (content.includes('eval(')) {
        issues.push(`${file}: 發現 eval() 使用，存在安全風險`);
      }
    }
    
    return {
      passed: issues.length === 0,
      message: issues.length > 0 ? issues.join('\n') : 'XSS 防護檢查通過'
    };
  }
  
  // 輸入驗證檢查
  async checkInputValidation() {
    const issues = [];
    const codeFiles = await this.getJavaScriptFiles();
    
    for (const file of codeFiles) {
      const content = await this.readFile(file);
      
      // 檢查表單處理是否有驗證
      if (content.includes('addEventListener("submit"') && 
          !content.includes('validate')) {
        issues.push(`${file}: 表單提交缺少驗證`);
      }
    }
    
    return {
      passed: issues.length === 0,
      message: issues.length > 0 ? issues.join('\n') : '輸入驗證檢查通過'
    };
  }
  
  // 單元測試檢查
  async checkUnitTests() {
    try {
      const testResult = await this.runCommand('npm test -- --passWithNoTests');
      return {
        passed: !testResult.includes('FAIL'),
        message: testResult.includes('FAIL') ? '單元測試失敗' : '單元測試通過'
      };
    } catch (error) {
      return { passed: false, message: '單元測試執行失敗' };
    }
  }
  
  // 測試覆蓋率檢查
  async checkTestCoverage() {
    try {
      const coverageResult = await this.runCommand('npm run test:coverage');
      const coverage = this.parseCoverage(coverageResult);
      
      return {
        passed: coverage >= 80,
        message: `測試覆蓋率: ${coverage}% ${coverage >= 80 ? '(通過)' : '(未達標準 80%)'}`
      };
    } catch (error) {
      return { passed: false, message: '測試覆蓋率檢查失敗' };
    }
  }
  
  // 生成檢查報告
  generateReport() {
    console.log('\n📊 檢查清單報告\n');
    console.log('================\n');
    
    let passedCount = 0;
    let totalCount = this.results.size;
    
    for (const [id, result] of this.results) {
      const check = this.checks.get(id);
      const status = result.passed ? '✅' : '❌';
      console.log(`${status} ${check.name}`);
      
      if (!result.passed) {
        console.log(`   ${result.message}`);
      }
      
      if (result.passed) passedCount++;
    }
    
    console.log(`\n📈 總結: ${passedCount}/${totalCount} 項檢查通過`);
    
    if (passedCount === totalCount) {
      console.log('🎉 所有檢查都通過！可以進行部署。');
    } else {
      console.log('⚠️  部分檢查未通過，請修正後再重新檢查。');
    }
  }
  
  // 輔助方法
  async getJavaScriptFiles() {
    // 實作取得 JavaScript 檔案清單
    return ['src/main.js', 'src/utils.js']; // 示例
  }
  
  async readFile(filePath) {
    // 實作檔案讀取
    return ''; // 示例
  }
  
  async runCommand(command) {
    // 實作命令執行
    return ''; // 示例
  }
  
  async getBundleSize() {
    // 實作 bundle 大小檢查
    return 500 * 1024; // 示例：500KB
  }
  
  async getUnusedDependencies() {
    // 實作未使用依賴檢查
    return []; // 示例
  }
  
  parseCoverage(output) {
    // 解析測試覆蓋率
    const match = output.match(/All files.*?(\d+(?:\.\d+)?)/);
    return match ? parseFloat(match[1]) : 0;
  }
}

// 使用範例
const checklist = new DevelopmentChecklist();
checklist.runAllChecks().then(() => {
  console.log('✨ 檢查清單執行完成');
});
```

---

## 結語

本手冊涵蓋了前端 JavaScript 開發的核心知識和最佳實務。請務必：

1. **循序漸進學習**：從基礎概念開始，逐步深入進階主題
2. **實作導向**：透過實際專案鞏固所學知識
3. **持續更新**：JavaScript 生態系統快速發展，保持學習熱忱
4. **代碼品質**：始終堅持編寫乾淨、可維護的程式碼
5. **安全意識**：將安全性考量融入開發流程的每個環節

記住，成為優秀的 JavaScript 開發者不僅需要技術能力，更需要良好的問題解決思維和持續學習的態度。

**祝您在 JavaScript 開發路上順利前行！** 🚀

---

*本文件最後更新：2025年8月29日*  
*如有問題或建議，請聯繫前端開發團隊*
