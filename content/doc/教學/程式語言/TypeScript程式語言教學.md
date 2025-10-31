# TypeScript 程式語言教學手冊

> **適用對象**：新進前端開發同仁  
> **目標**：快速掌握 TypeScript 在專案中的使用方法與最佳實踐  
> **更新日期**：2025年8月31日

## 📋 目錄

1. [TypeScript 基礎](#1-typescript-基礎)
   - 1.1 [TypeScript 與 JavaScript 的差異](#11-typescript-與-javascript-的差異)
   - 1.2 [型別系統](#12-型別系統)
   - 1.3 [介面與型別別名](#13-介面-interface-與型別別名-type-alias)
2. [專案規範](#2-專案規範)
   - 2.1 [TypeScript 版本與設定](#21-typescript-版本與設定)
   - 2.2 [檔案命名規則與專案目錄結構](#22-檔案命名規則與專案目錄結構)
   - 2.3 [型別宣告的最佳實踐](#23-型別宣告的最佳實踐)
   - 2.4 [使用 any 的限制與替代方法](#24-使用-any-的限制與替代方法)
3. [程式開發指引](#3-程式開發指引)
   - 3.1 [撰寫可讀性與可維護性的程式碼](#31-撰寫可讀性與可維護性的程式碼)
   - 3.2 [常見錯誤與最佳解法](#32-常見錯誤與最佳解法)
   - 3.3 [與第三方套件整合](#33-與第三方套件整合)
4. [範例程式碼](#4-範例程式碼)
   - 4.1 [Class 類別實作範例](#41-class-類別實作範例)
   - 4.2 [Interface 介面範例](#42-interface-介面範例)
   - 4.3 [泛型實作範例](#43-泛型實作範例)
   - 4.4 [模組化範例](#44-模組化範例)
5. [實務建議](#5-實務建議)
   - 5.1 [善用 TypeScript 的型別檢查](#51-善用-typescript-的型別檢查)
   - 5.2 [除錯與測試](#52-除錯與測試)
   - 5.3 [團隊協作與程式風格統一](#53-團隊協作與程式風格統一)
6. [檢查清單](#6-檢查清單)
   - 6.1 [專案建立檢查清單](#61-專案建立檢查清單)
   - 6.2 [開發期間檢查清單](#62-開發期間檢查清單)
   - 6.3 [程式碼審查檢查清單](#63-程式碼審查檢查清單)
   - 6.4 [部署前檢查清單](#64-部署前檢查清單)
   - 6.5 [常見問題快速檢查](#65-常見問題快速檢查)
7. [進階主題](#7-進階主題)
   - 7.1 [條件型別 (Conditional Types)](#71-條件型別-conditional-types)
   - 7.2 [映射型別 (Mapped Types)](#72-映射型別-mapped-types)
   - 7.3 [模板字面型別 (Template Literal Types)](#73-模板字面型別-template-literal-types)
   - 7.4 [裝飾器 (Decorators)](#74-裝飾器-decorators)
8. [效能優化與最佳實踐](#8-效能優化與最佳實踐)
   - 8.1 [編譯效能優化](#81-編譯效能優化)
   - 8.2 [型別檢查效能](#82-型別檢查效能)
   - 8.3 [打包優化](#83-打包優化)
9. [TypeScript 生態系統](#9-typescript-生態系統)
   - 9.1 [開發工具](#91-開發工具)
   - 9.2 [測試框架](#92-測試框架)
   - 9.3 [建置工具](#93-建置工具)
   - 9.4 [型別定義管理](#94-型別定義管理)
10. [常見問題與解決方案](#10-常見問題與解決方案)
    - 10.1 [編譯錯誤](#101-編譯錯誤)
    - 10.2 [型別推斷問題](#102-型別推斷問題)
    - 10.3 [執行時期問題](#103-執行時期問題)
    - 10.4 [最佳實踐檢查清單](#104-最佳實踐檢查清單)

---

## 1. TypeScript 基礎

### 1.1 TypeScript 與 JavaScript 的差異

#### 什麼是 TypeScript？
TypeScript 是 Microsoft 開發的 JavaScript 超集（superset），為 JavaScript 添加了靜態型別檢查功能。

#### 主要差異比較

| 特性 | JavaScript | TypeScript |
|------|------------|------------|
| 型別檢查 | 動態型別（執行時期） | 靜態型別（編譯時期） |
| 語法 | ES5/ES6+ | ES5/ES6+ + 型別註解 |
| 編譯 | 直接執行 | 需編譯為 JavaScript |
| 錯誤偵測 | 執行時期 | 開發時期 |
| IDE 支援 | 基本 | 強大的自動完成與錯誤提示 |

#### 為什麼使用 TypeScript？

**優點：**
- 🔍 **編譯時期錯誤檢查**：在開發階段就能發現錯誤
- 🎯 **更好的 IDE 支援**：自動完成、重構、導航
- 📚 **自我文件化**：型別即文件，提升程式可讀性
- 🛡️ **重構安全性**：大型專案重構時更安全
- 👥 **團隊協作**：明確的介面定義，降低溝通成本

**範例比較：**

```javascript
// JavaScript - 執行時期才發現錯誤
function calculateTotal(items) {
    return items.reduce((sum, item) => sum + item.price, 0);
}

// 傳入錯誤的資料結構，執行時期才會報錯
calculateTotal([{ name: "商品", cost: 100 }]); // Error: Cannot read property 'price'
```

```typescript
// TypeScript - 開發時期就能發現錯誤
interface Item {
    name: string;
    price: number;
}

function calculateTotal(items: Item[]): number {
    return items.reduce((sum, item) => sum + item.price, 0);
}

// 編譯時期就會提示錯誤
calculateTotal([{ name: "商品", cost: 100 }]); // 編譯錯誤：缺少 'price' 屬性
```

### 1.2 型別系統

#### 基本型別

TypeScript 提供了多種基本型別來描述資料：

```typescript
// 基本型別
let isDone: boolean = false;
let decimal: number = 6;
let color: string = "blue";
let list: number[] = [1, 2, 3];
let tuple: [string, number] = ["hello", 10];

// null 和 undefined
let u: undefined = undefined;
let n: null = null;

// void - 通常用於沒有回傳值的函數
function warnUser(): void {
    console.log("This is my warning message");
}

// never - 永遠不會回傳的函數
function error(message: string): never {
    throw new Error(message);
}
```

#### 物件型別

```typescript
// 物件型別定義
let user: {
    name: string;
    age: number;
    email?: string; // 可選屬性
} = {
    name: "王小明",
    age: 25
};

// 使用 interface 定義物件型別（推薦）
interface User {
    readonly id: number;     // 唯讀屬性
    name: string;
    age: number;
    email?: string;          // 可選屬性
    [propName: string]: any; // 索引簽名，允許額外屬性
}

const userData: User = {
    id: 1,
    name: "李小華",
    age: 30,
    email: "lee@example.com",
    department: "IT" // 額外屬性
};
```

#### 陣列型別

```typescript
// 陣列型別的兩種寫法
let numbers1: number[] = [1, 2, 3, 4, 5];
let numbers2: Array<number> = [1, 2, 3, 4, 5];

// 物件陣列
interface Product {
    id: number;
    name: string;
    price: number;
}

let products: Product[] = [
    { id: 1, name: "筆電", price: 30000 },
    { id: 2, name: "滑鼠", price: 800 }
];

// 多維陣列
let matrix: number[][] = [[1, 2], [3, 4]];
```

#### 泛型 (Generics)

泛型讓我們能撰寫可重用的程式碼，同時保持型別安全：

```typescript
// 基本泛型函數
function identity<T>(arg: T): T {
    return arg;
}

let output1 = identity<string>("myString");
let output2 = identity<number>(100);

// 泛型介面
interface GenericIdentityFn<T> {
    (arg: T): T;
}

// 泛型類別
class GenericRepository<T> {
    private items: T[] = [];

    add(item: T): void {
        this.items.push(item);
    }

    findById(id: number): T | undefined {
        return this.items[id];
    }

    getAll(): T[] {
        return this.items;
    }
}

// 使用泛型類別
const userRepository = new GenericRepository<User>();
userRepository.add({ id: 1, name: "測試用戶", age: 25 });
```

**實務注意事項：**
- 優先使用具體型別，只有在需要重用時才使用泛型
- 為泛型參數選擇有意義的名稱（如 `TUser` 而非 `T`）
- 適當使用泛型約束來限制泛型型別

### 1.3 介面 (Interface) 與型別別名 (Type Alias)

#### Interface 介面

介面定義物件的結構，是 TypeScript 中定義型別的主要方式：

```typescript
// 基本介面定義
interface Person {
    name: string;
    age: number;
}

// 介面繼承
interface Employee extends Person {
    employeeId: string;
    department: string;
    salary?: number; // 可選屬性
}

// 實作介面
class Developer implements Employee {
    name: string;
    age: number;
    employeeId: string;
    department: string;
    
    constructor(name: string, age: number, employeeId: string) {
        this.name = name;
        this.age = age;
        this.employeeId = employeeId;
        this.department = "開發部";
    }
}

// 函數介面
interface SearchFunc {
    (source: string, subString: string): boolean;
}

let mySearch: SearchFunc = function(source: string, subString: string): boolean {
    return source.search(subString) > -1;
};
```

#### Type Alias 型別別名

型別別名為現有型別建立新名稱：

```typescript
// 基本型別別名
type ID = string | number;
type UserStatus = "active" | "inactive" | "pending";

// 物件型別別名
type Point = {
    x: number;
    y: number;
};

// 函數型別別名
type EventHandler = (event: Event) => void;

// 泛型型別別名
type ApiResponse<T> = {
    data: T;
    success: boolean;
    message: string;
};

// 使用範例
type UserResponse = ApiResponse<User>;
```

#### Interface vs Type Alias 選擇指南

| 使用情境 | 推薦 | 原因 |
|----------|------|------|
| 定義物件結構 | Interface | 更清晰的語法，支援聲明合併 |
| 定義函數型別 | Type Alias | 更簡潔 |
| Union/Intersection 型別 | Type Alias | Interface 不支援 |
| 需要繼承 | Interface | 語法更直觀 |
| 計算屬性名 | Type Alias | Interface 不支援 |

```typescript
// 推薦：使用 Interface 定義物件
interface UserConfig {
    apiUrl: string;
    timeout: number;
}

// 推薦：使用 Type 定義 Union 型別
type Theme = "light" | "dark" | "auto";

// 推薦：使用 Type 定義複雜型別
type EventMap = {
    click: MouseEvent;
    keypress: KeyboardEvent;
    focus: FocusEvent;
};
```

---

**本章重點回顧：**

- TypeScript 提供編譯時期的型別檢查，大幅提升開發效率
- 掌握基本型別系統是使用 TypeScript 的基礎
- Interface 適合定義物件結構，Type Alias 適合複雜型別操作
- 泛型讓程式碼更具重用性，但要適度使用

**下一章預告：** 我們將學習專案中的 TypeScript 配置與開發規範。

---

## 2. 專案規範

### 2.1 TypeScript 版本與設定

#### 建議的 TypeScript 版本

```json
{
  "devDependencies": {
    "typescript": "^5.1.0",
    "@types/node": "^20.0.0"
  }
}
```

**版本選擇原則：**

- 使用 LTS（長期支援）版本確保穩定性
- 定期更新但避免使用最新的 Beta 版本
- 團隊統一使用相同的 TypeScript 版本

#### tsconfig.json 專案配置

專案中的 `tsconfig.json` 是 TypeScript 編譯器的配置檔案：

```json
{
  "compilerOptions": {
    // 編譯目標
    "target": "ES2020",
    "module": "ESNext",
    "moduleResolution": "bundler",
    
    // 輸出設定
    "outDir": "./dist",
    "rootDir": "./src",
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    
    // 型別檢查設定
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedIndexedAccess": true,
    
    // 模組解析
    "baseUrl": "./",
    "paths": {
      "@/*": ["src/*"],
      "@/components/*": ["src/components/*"],
      "@/utils/*": ["src/utils/*"],
      "@/types/*": ["src/types/*"]
    },
    
    // 其他設定
    "allowSyntheticDefaultImports": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true
  },
  "include": [
    "src/**/*",
    "types/**/*"
  ],
  "exclude": [
    "node_modules",
    "dist",
    "build",
    "**/*.test.ts",
    "**/*.spec.ts"
  ]
}
```

#### 重要配置說明

| 配置項目 | 說明 | 建議值 |
|----------|------|--------|
| `strict` | 啟用所有嚴格型別檢查 | `true` |
| `noImplicitAny` | 禁止隱式 any 型別 | `true` |
| `strictNullChecks` | 嚴格檢查 null/undefined | `true` |
| `noUnusedLocals` | 檢查未使用的變數 | `true` |
| `noUnusedParameters` | 檢查未使用的參數 | `true` |
| `exactOptionalPropertyTypes` | 精確檢查可選屬性 | `true` |

### 2.2 檔案命名規則與專案目錄結構

#### 檔案命名規則

```
專案根目錄/
├── src/
│   ├── components/          # React/Vue 元件
│   │   ├── common/         # 共用元件
│   │   │   ├── Button.tsx
│   │   │   ├── Modal.tsx
│   │   │   └── index.ts    # 統一匯出
│   │   └── pages/          # 頁面元件
│   │       ├── HomePage.tsx
│   │       └── UserProfile.tsx
│   ├── hooks/              # 自定義 hooks (React)
│   │   ├── useAuth.ts
│   │   └── useLocalStorage.ts
│   ├── services/           # API 服務層
│   │   ├── api.ts
│   │   ├── authService.ts
│   │   └── userService.ts
│   ├── store/              # 狀態管理
│   │   ├── index.ts
│   │   ├── authStore.ts
│   │   └── userStore.ts
│   ├── types/              # 型別定義
│   │   ├── api.types.ts
│   │   ├── user.types.ts
│   │   └── common.types.ts
│   ├── utils/              # 工具函數
│   │   ├── helpers.ts
│   │   ├── constants.ts
│   │   └── formatters.ts
│   ├── styles/             # 樣式檔案
│   └── assets/             # 靜態資源
├── types/                  # 全域型別定義
│   └── global.d.ts
├── tests/                  # 測試檔案
└── docs/                   # 說明文件
```

#### 命名慣例

**檔案命名：**

```typescript
// ✅ 好的命名
UserProfile.tsx        // 元件：PascalCase
userService.ts         // 服務：camelCase
auth.types.ts          // 型別定義：camelCase + .types
constants.ts           // 常數：camelCase
api-client.ts          // 連字符號可接受

// ❌ 避免的命名
user_profile.tsx       // 避免底線
UserProfile.ts         // 元件檔案使用 .tsx
AUTH_SERVICE.ts        // 避免全大寫
```

**變數與函數命名：**

```typescript
// ✅ 好的命名
const userName = "王小明";                    // camelCase
const API_BASE_URL = "https://api.example.com"; // 常數：UPPER_SNAKE_CASE
const MAX_RETRY_COUNT = 3;

function getUserById(id: string): User { ... }   // 函數：camelCase，動詞開頭
function calculateTotalPrice(items: Item[]): number { ... }

// ✅ 類別和介面命名
class UserManager { ... }                       // 類別：PascalCase
interface ApiResponse<T> { ... }                // 介面：PascalCase
type UserStatus = "active" | "inactive";        // 型別：PascalCase
```

### 2.3 型別宣告的最佳實踐

#### 型別定義組織

```typescript
// types/user.types.ts - 用戶相關型別
export interface User {
  id: string;
  name: string;
  email: string;
  role: UserRole;
  createdAt: Date;
  updatedAt: Date;
}

export type UserRole = "admin" | "user" | "guest";

export interface CreateUserRequest {
  name: string;
  email: string;
  password: string;
}

export interface UpdateUserRequest extends Partial<Omit<User, "id" | "createdAt">> {}

// types/api.types.ts - API 相關型別
export interface ApiResponse<T = any> {
  data: T;
  success: boolean;
  message: string;
  errors?: string[];
}

export interface PaginatedResponse<T> extends ApiResponse<T[]> {
  pagination: {
    page: number;
    limit: number;
    total: number;
    totalPages: number;
  };
}

// types/common.types.ts - 通用型別
export type Status = "loading" | "success" | "error" | "idle";

export interface SelectOption<T = string> {
  label: string;
  value: T;
  disabled?: boolean;
}
```

#### 型別導入與導出規範

```typescript
// ✅ 明確的型別導入
import type { User, UserRole } from "@/types/user.types";
import type { ApiResponse } from "@/types/api.types";

// ✅ 命名空間組織（大型專案）
declare namespace API {
  interface Response<T> {
    data: T;
    success: boolean;
  }
  
  namespace User {
    interface Detail {
      id: string;
      name: string;
    }
    
    interface CreateRequest {
      name: string;
      email: string;
    }
  }
}

// 使用命名空間
function handleResponse(response: API.Response<API.User.Detail>) {
  // ...
}
```

### 2.4 使用 any 的限制與替代方法

#### any 的問題

```typescript
// ❌ 問題：失去型別安全性
let data: any = fetchUserData();
data.nonExistentMethod(); // 編譯時不會報錯，執行時會出錯
```

#### 替代方案

**1. 使用 unknown 型別**

```typescript
// ✅ 使用 unknown 替代 any
function processApiResponse(response: unknown): User | null {
  // 需要型別守衛
  if (isUser(response)) {
    return response;
  }
  return null;
}

// 型別守衛函數
function isUser(obj: unknown): obj is User {
  return (
    typeof obj === "object" &&
    obj !== null &&
    typeof (obj as User).id === "string" &&
    typeof (obj as User).name === "string"
  );
}
```

**2. 使用泛型**

```typescript
// ✅ 使用泛型保持型別安全
interface Repository<T> {
  findById(id: string): Promise<T | null>;
  create(entity: Omit<T, "id">): Promise<T>;
  update(id: string, entity: Partial<T>): Promise<T>;
  delete(id: string): Promise<boolean>;
}

class UserRepository implements Repository<User> {
  async findById(id: string): Promise<User | null> {
    // 實作...
  }
  
  // 其他方法實作...
}
```

**3. 使用 Union 型別**

```typescript
// ✅ 明確定義可能的型別
type ApiData = User | Product | Order | null;

function handleApiData(data: ApiData) {
  if (!data) return;
  
  // 使用 discriminated union
  switch (data.type) {
    case "user":
      // TypeScript 知道這是 User 型別
      console.log(data.name);
      break;
    case "product":
      // TypeScript 知道這是 Product 型別
      console.log(data.price);
      break;
  }
}
```

**4. 使用型別斷言（謹慎使用）**

```typescript
// ✅ 適當的型別斷言
interface LegacyApiResponse {
  [key: string]: any;
}

function migrateLegacyData(legacy: LegacyApiResponse): User {
  // 明確的型別轉換
  return {
    id: legacy.user_id as string,
    name: legacy.user_name as string,
    email: legacy.email_address as string,
    role: (legacy.role as string) || "user"
  } as User;
}
```

#### any 使用準則

**允許使用 any 的情況：**

- 遷移現有 JavaScript 程式碼時的漸進式轉換
- 整合沒有型別定義的第三方函式庫
- 動態內容處理（如 JSON 解析）

**使用 any 時的注意事項：**

```typescript
// ✅ 加上註解說明原因
// eslint-disable-next-line @typescript-eslint/no-explicit-any
const legacyData: any = JSON.parse(legacyJsonString); // 舊系統資料格式未定義

// ✅ 儘快轉換為具體型別
const userData = validateAndTransformUser(legacyData);
```

---

**本章重點回顧：**

- 正確配置 `tsconfig.json` 是專案成功的基礎
- 統一的命名規則提升程式碼可讀性
- 良好的目錄結構有助於專案維護
- 避免使用 `any`，優先考慮 `unknown`、泛型、Union 型別等替代方案

**下一章預告：** 我們將深入探討如何撰寫高品質的 TypeScript 程式碼。

---

## 3. 程式開發指引

### 3.1 撰寫可讀性與可維護性的程式碼

#### 函數設計原則

**單一職責原則**

```typescript
// ❌ 職責混雜的函數
function processUserData(userData: any): any {
  // 驗證資料
  if (!userData.email || !userData.name) {
    throw new Error("資料不完整");
  }
  
  // 格式化資料
  userData.email = userData.email.toLowerCase();
  userData.name = userData.name.trim();
  
  // 儲存到資料庫
  database.save(userData);
  
  // 發送歡迎信件
  emailService.sendWelcomeEmail(userData.email);
  
  return userData;
}

// ✅ 拆分為多個單一職責函數
interface UserInput {
  name: string;
  email: string;
}

interface ValidatedUser {
  name: string;
  email: string;
}

function validateUserInput(input: UserInput): ValidatedUser {
  if (!input.email || !input.name) {
    throw new Error("使用者姓名和電子信箱為必填欄位");
  }
  
  return {
    name: input.name.trim(),
    email: input.email.toLowerCase()
  };
}

function formatUserData(user: ValidatedUser): ValidatedUser {
  return {
    name: user.name.trim(),
    email: user.email.toLowerCase()
  };
}

async function createUser(input: UserInput): Promise<User> {
  const validatedUser = validateUserInput(input);
  const formattedUser = formatUserData(validatedUser);
  
  const savedUser = await userRepository.create(formattedUser);
  await emailService.sendWelcomeEmail(savedUser.email);
  
  return savedUser;
}
```

#### 型別優先的程式設計

```typescript
// ✅ 先定義型別，再實作功能
interface PaymentMethod {
  id: string;
  type: "credit_card" | "paypal" | "bank_transfer";
  isDefault: boolean;
}

interface PaymentRequest {
  amount: number;
  currency: string;
  paymentMethodId: string;
  orderId: string;
}

interface PaymentResult {
  success: boolean;
  transactionId?: string;
  errorMessage?: string;
}

class PaymentService {
  async processPayment(request: PaymentRequest): Promise<PaymentResult> {
    try {
      const paymentMethod = await this.getPaymentMethod(request.paymentMethodId);
      const transaction = await this.createTransaction(request, paymentMethod);
      
      return {
        success: true,
        transactionId: transaction.id
      };
    } catch (error) {
      return {
        success: false,
        errorMessage: error instanceof Error ? error.message : "付款處理失敗"
      };
    }
  }
  
  private async getPaymentMethod(id: string): Promise<PaymentMethod> {
    // 實作取得付款方式邏輯
    throw new Error("Method not implemented");
  }
  
  private async createTransaction(
    request: PaymentRequest, 
    method: PaymentMethod
  ): Promise<{ id: string }> {
    // 實作建立交易邏輯
    throw new Error("Method not implemented");
  }
}
```

#### 錯誤處理策略

```typescript
// ✅ 使用 Result 模式進行錯誤處理
type Result<T, E = Error> = 
  | { success: true; data: T }
  | { success: false; error: E };

class UserService {
  async getUser(id: string): Promise<Result<User, string>> {
    try {
      if (!id) {
        return { success: false, error: "使用者 ID 不能為空" };
      }
      
      const user = await userRepository.findById(id);
      if (!user) {
        return { success: false, error: "找不到指定的使用者" };
      }
      
      return { success: true, data: user };
    } catch (error) {
      logger.error("取得使用者資料失敗", { id, error });
      return { 
        success: false, 
        error: "系統錯誤，請稍後再試" 
      };
    }
  }
}

// 使用 Result 模式
async function displayUser(userId: string): Promise<void> {
  const result = await userService.getUser(userId);
  
  if (result.success) {
    console.log(`使用者姓名: ${result.data.name}`);
  } else {
    console.error(`錯誤: ${result.error}`);
  }
}
```

### 3.2 常見錯誤與最佳解法

#### 錯誤 1：型別斷言濫用

```typescript
// ❌ 危險的型別斷言
function processApiResponse(response: any): User {
  return response as User; // 沒有驗證，可能導致執行時錯誤
}

// ✅ 使用型別守衛
function isValidUser(obj: unknown): obj is User {
  return (
    typeof obj === "object" &&
    obj !== null &&
    typeof (obj as User).id === "string" &&
    typeof (obj as User).name === "string" &&
    typeof (obj as User).email === "string"
  );
}

function processApiResponse(response: unknown): User | null {
  if (isValidUser(response)) {
    return response;
  }
  logger.warn("API 回應格式不正確", response);
  return null;
}
```

#### 錯誤 2：忽略 null/undefined 檢查

```typescript
// ❌ 沒有處理 null/undefined
function getUserName(user: User | null): string {
  return user.name; // 可能拋出錯誤
}

// ✅ 適當的 null 檢查
function getUserName(user: User | null): string {
  return user?.name ?? "未知使用者";
}

// ✅ 使用型別縮小
function getUserName(user: User | null): string {
  if (!user) {
    return "未知使用者";
  }
  return user.name; // TypeScript 知道 user 不是 null
}
```

#### 錯誤 3：Promise 型別處理不當

```typescript
// ❌ 未正確處理 Promise 型別
async function fetchUsers(): Promise<User[]> {
  const response = fetch("/api/users");
  return response.json(); // 型別不匹配
}

// ✅ 正確的 Promise 處理
async function fetchUsers(): Promise<User[]> {
  try {
    const response = await fetch("/api/users");
    
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    
    const data: unknown = await response.json();
    
    if (!Array.isArray(data)) {
      throw new Error("API 回應格式不正確");
    }
    
    return data.filter(isValidUser);
  } catch (error) {
    logger.error("取得使用者列表失敗", error);
    throw new Error("無法載入使用者資料");
  }
}
```

### 3.3 與第三方套件整合

#### React 專案整合

```typescript
// types/react.types.ts
import { ReactNode } from "react";

export interface BaseProps {
  children?: ReactNode;
  className?: string;
  testId?: string;
}

export interface ButtonProps extends BaseProps {
  variant?: "primary" | "secondary" | "danger";
  size?: "small" | "medium" | "large";
  disabled?: boolean;
  loading?: boolean;
  onClick?: (event: React.MouseEvent<HTMLButtonElement>) => void;
}

// components/Button.tsx
import React from "react";
import { ButtonProps } from "@/types/react.types";

export const Button: React.FC<ButtonProps> = ({
  children,
  variant = "primary",
  size = "medium",
  disabled = false,
  loading = false,
  onClick,
  className = "",
  testId
}) => {
  const handleClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    if (!disabled && !loading && onClick) {
      onClick(event);
    }
  };

  return (
    <button
      type="button"
      className={`btn btn--${variant} btn--${size} ${className}`}
      disabled={disabled || loading}
      onClick={handleClick}
      data-testid={testId}
    >
      {loading ? "載入中..." : children}
    </button>
  );
};

// hooks/useApi.ts
import { useState, useEffect } from "react";

interface UseApiState<T> {
  data: T | null;
  loading: boolean;
  error: string | null;
}

export function useApi<T>(
  fetcher: () => Promise<T>,
  dependencies: any[] = []
): UseApiState<T> {
  const [state, setState] = useState<UseApiState<T>>({
    data: null,
    loading: true,
    error: null
  });

  useEffect(() => {
    let cancelled = false;
    
    const fetchData = async () => {
      try {
        setState(prev => ({ ...prev, loading: true, error: null }));
        const result = await fetcher();
        
        if (!cancelled) {
          setState({ data: result, loading: false, error: null });
        }
      } catch (error) {
        if (!cancelled) {
          setState({
            data: null,
            loading: false,
            error: error instanceof Error ? error.message : "未知錯誤"
          });
        }
      }
    };

    fetchData();
    
    return () => {
      cancelled = true;
    };
  }, dependencies);

  return state;
}
```

#### Vue 3 專案整合

```typescript
// types/vue.types.ts
export interface ComponentProps {
  [key: string]: any;
}

export interface EmitEvents {
  [key: string]: (...args: any[]) => void;
}

// composables/useCounter.ts
import { ref, computed, Ref } from "vue";

interface UseCounterReturn {
  count: Ref<number>;
  doubleCount: Ref<number>;
  increment: () => void;
  decrement: () => void;
  reset: () => void;
}

export function useCounter(initialValue: number = 0): UseCounterReturn {
  const count = ref(initialValue);
  
  const doubleCount = computed(() => count.value * 2);
  
  const increment = () => {
    count.value++;
  };
  
  const decrement = () => {
    count.value--;
  };
  
  const reset = () => {
    count.value = initialValue;
  };
  
  return {
    count,
    doubleCount,
    increment,
    decrement,
    reset
  };
}

// components/UserCard.vue
<template>
  <div class="user-card">
    <h3>{{ user.name }}</h3>
    <p>{{ user.email }}</p>
    <button @click="handleEdit">編輯</button>
  </div>
</template>

<script setup lang="ts">
interface Props {
  user: User;
}

interface Emits {
  (e: "edit", user: User): void;
}

const props = defineProps<Props>();
const emit = defineEmits<Emits>();

const handleEdit = () => {
  emit("edit", props.user);
};
</script>
```

#### Node.js 專案整合

```typescript
// types/express.types.ts
import { Request, Response, NextFunction } from "express";

export interface AuthenticatedRequest extends Request {
  user?: User;
}

export interface ApiResponse<T = any> {
  success: boolean;
  data?: T;
  message: string;
  errors?: string[];
}

export type AsyncHandler = (
  req: Request,
  res: Response,
  next: NextFunction
) => Promise<void>;

// middleware/auth.ts
import { Response, NextFunction } from "express";
import { AuthenticatedRequest } from "@/types/express.types";

export const authMiddleware = async (
  req: AuthenticatedRequest,
  res: Response,
  next: NextFunction
): Promise<void> => {
  try {
    const token = req.headers.authorization?.replace("Bearer ", "");
    
    if (!token) {
      res.status(401).json({
        success: false,
        message: "需要驗證令牌"
      });
      return;
    }
    
    const user = await verifyToken(token);
    req.user = user;
    next();
  } catch (error) {
    res.status(401).json({
      success: false,
      message: "無效的驗證令牌"
    });
  }
};

// controllers/userController.ts
import { Response } from "express";
import { AuthenticatedRequest, ApiResponse } from "@/types/express.types";

export const getProfile = async (
  req: AuthenticatedRequest,
  res: Response<ApiResponse<User>>
): Promise<void> => {
  try {
    if (!req.user) {
      res.status(401).json({
        success: false,
        message: "未授權的請求"
      });
      return;
    }
    
    res.json({
      success: true,
      data: req.user,
      message: "成功取得使用者資料"
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: "伺服器錯誤"
    });
  }
};
```

---

**本章重點回顧：**

- 遵循單一職責原則，讓函數功能明確且易於測試
- 先定義型別再實作功能，確保型別安全
- 使用 Result 模式和型別守衛處理錯誤
- 不同框架有其特定的 TypeScript 整合模式
- 適當的錯誤處理和 null 檢查是必要的

**下一章預告：** 我們將通過具體的程式碼範例，展示 TypeScript 的實際應用。

---

## 4. 範例程式碼

### 4.1 Class 類別實作範例

#### 基礎類別設計

```typescript
// models/User.ts
export class User {
  private _id: string;
  private _name: string;
  private _email: string;
  private _createdAt: Date;
  private _lastLoginAt: Date | null = null;

  constructor(id: string, name: string, email: string) {
    this._id = id;
    this._name = this.validateName(name);
    this._email = this.validateEmail(email);
    this._createdAt = new Date();
  }

  // Getter 方法
  get id(): string {
    return this._id;
  }

  get name(): string {
    return this._name;
  }

  get email(): string {
    return this._email;
  }

  get createdAt(): Date {
    return new Date(this._createdAt);
  }

  get lastLoginAt(): Date | null {
    return this._lastLoginAt ? new Date(this._lastLoginAt) : null;
  }

  get isNewUser(): boolean {
    return this._lastLoginAt === null;
  }

  // Setter 方法
  set name(newName: string) {
    this._name = this.validateName(newName);
  }

  set email(newEmail: string) {
    this._email = this.validateEmail(newEmail);
  }

  // 公開方法
  updateLastLogin(): void {
    this._lastLoginAt = new Date();
  }

  getDaysSinceCreation(): number {
    const now = new Date();
    const diffTime = Math.abs(now.getTime() - this._createdAt.getTime());
    return Math.ceil(diffTime / (1000 * 60 * 60 * 24));
  }

  toJSON(): UserJSON {
    return {
      id: this._id,
      name: this._name,
      email: this._email,
      createdAt: this._createdAt.toISOString(),
      lastLoginAt: this._lastLoginAt?.toISOString() || null,
      isNewUser: this.isNewUser
    };
  }

  // 私有驗證方法
  private validateName(name: string): string {
    if (!name || name.trim().length === 0) {
      throw new Error("使用者姓名不能為空");
    }
    if (name.length > 50) {
      throw new Error("使用者姓名不能超過 50 個字元");
    }
    return name.trim();
  }

  private validateEmail(email: string): string {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      throw new Error("電子郵件格式不正確");
    }
    return email.toLowerCase();
  }

  // 靜態工廠方法
  static fromJSON(json: UserJSON): User {
    const user = new User(json.id, json.name, json.email);
    user._createdAt = new Date(json.createdAt);
    if (json.lastLoginAt) {
      user._lastLoginAt = new Date(json.lastLoginAt);
    }
    return user;
  }
}

// 相關型別定義
interface UserJSON {
  id: string;
  name: string;
  email: string;
  createdAt: string;
  lastLoginAt: string | null;
  isNewUser: boolean;
}
```

#### 繼承與多型範例

```typescript
// models/BaseEntity.ts
export abstract class BaseEntity {
  protected _id: string;
  protected _createdAt: Date;
  protected _updatedAt: Date;

  constructor(id: string) {
    this._id = id;
    this._createdAt = new Date();
    this._updatedAt = new Date();
  }

  get id(): string {
    return this._id;
  }

  get createdAt(): Date {
    return new Date(this._createdAt);
  }

  get updatedAt(): Date {
    return new Date(this._updatedAt);
  }

  protected updateTimestamp(): void {
    this._updatedAt = new Date();
  }

  // 抽象方法，子類必須實作
  abstract validate(): boolean;
  abstract toJSON(): Record<string, any>;
}

// models/Product.ts
export class Product extends BaseEntity {
  private _name: string;
  private _price: number;
  private _category: ProductCategory;
  private _isActive: boolean = true;

  constructor(
    id: string,
    name: string,
    price: number,
    category: ProductCategory
  ) {
    super(id);
    this._name = name;
    this._price = price;
    this._category = category;
  }

  get name(): string {
    return this._name;
  }

  get price(): number {
    return this._price;
  }

  get category(): ProductCategory {
    return this._category;
  }

  get isActive(): boolean {
    return this._isActive;
  }

  updatePrice(newPrice: number): void {
    if (newPrice <= 0) {
      throw new Error("商品價格必須大於 0");
    }
    this._price = newPrice;
    this.updateTimestamp();
  }

  deactivate(): void {
    this._isActive = false;
    this.updateTimestamp();
  }

  activate(): void {
    this._isActive = true;
    this.updateTimestamp();
  }

  // 實作抽象方法
  validate(): boolean {
    return (
      this._name.length > 0 &&
      this._price > 0 &&
      Object.values(ProductCategory).includes(this._category)
    );
  }

  toJSON(): ProductJSON {
    return {
      id: this._id,
      name: this._name,
      price: this._price,
      category: this._category,
      isActive: this._isActive,
      createdAt: this._createdAt.toISOString(),
      updatedAt: this._updatedAt.toISOString()
    };
  }
}

enum ProductCategory {
  ELECTRONICS = "electronics",
  CLOTHING = "clothing",
  BOOKS = "books",
  HOME = "home",
  SPORTS = "sports"
}

interface ProductJSON {
  id: string;
  name: string;
  price: number;
  category: ProductCategory;
  isActive: boolean;
  createdAt: string;
  updatedAt: string;
}
```

### 4.2 Interface 介面範例

#### 複雜介面設計

```typescript
// interfaces/Repository.ts
export interface Repository<T, TKey = string> {
  findById(id: TKey): Promise<T | null>;
  findAll(filter?: RepositoryFilter<T>): Promise<T[]>;
  create(entity: Omit<T, "id" | "createdAt" | "updatedAt">): Promise<T>;
  update(id: TKey, updates: Partial<T>): Promise<T | null>;
  delete(id: TKey): Promise<boolean>;
  count(filter?: RepositoryFilter<T>): Promise<number>;
}

export interface RepositoryFilter<T> {
  where?: Partial<T>;
  orderBy?: {
    field: keyof T;
    direction: "asc" | "desc";
  }[];
  limit?: number;
  offset?: number;
}

// interfaces/Service.ts
export interface CacheService {
  get<T>(key: string): Promise<T | null>;
  set<T>(key: string, value: T, ttl?: number): Promise<void>;
  delete(key: string): Promise<boolean>;
  clear(): Promise<void>;
  exists(key: string): Promise<boolean>;
}

export interface EmailService {
  sendWelcomeEmail(to: string, userName: string): Promise<EmailResult>;
  sendResetPasswordEmail(to: string, resetToken: string): Promise<EmailResult>;
  sendNotificationEmail(
    to: string,
    subject: string,
    content: string
  ): Promise<EmailResult>;
}

export interface EmailResult {
  success: boolean;
  messageId?: string;
  error?: string;
}

// interfaces/Events.ts
export interface DomainEvent {
  eventId: string;
  eventType: string;
  aggregateId: string;
  timestamp: Date;
  version: number;
  data: Record<string, any>;
}

export interface EventHandler<T extends DomainEvent = DomainEvent> {
  eventType: string;
  handle(event: T): Promise<void>;
}

export interface EventBus {
  publish<T extends DomainEvent>(event: T): Promise<void>;
  subscribe<T extends DomainEvent>(handler: EventHandler<T>): void;
  unsubscribe<T extends DomainEvent>(handler: EventHandler<T>): void;
}
```

#### 條件型別與映射型別

```typescript
// types/Utility.ts

// 條件型別範例
type NonNullable<T> = T extends null | undefined ? never : T;

type ApiEndpoint<T> = T extends "users" 
  ? "/api/users"
  : T extends "products"
  ? "/api/products"
  : T extends "orders"
  ? "/api/orders"
  : never;

// 映射型別範例
type ReadOnly<T> = {
  readonly [P in keyof T]: T[P];
};

type Optional<T> = {
  [P in keyof T]?: T[P];
};

type PartialExcept<T, K extends keyof T> = Partial<T> & Pick<T, K>;

// 實用工具型別
type DeepPartial<T> = {
  [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P];
};

type KeysOfType<T, U> = {
  [K in keyof T]: T[K] extends U ? K : never;
}[keyof T];

type RequiredKeys<T> = {
  [K in keyof T]-?: {} extends Pick<T, K> ? never : K;
}[keyof T];

// 使用範例
interface UserProfile {
  id: string;
  name: string;
  email: string;
  avatar?: string;
  settings: {
    theme: "light" | "dark";
    notifications: boolean;
  };
}

type ReadOnlyUserProfile = ReadOnly<UserProfile>;
type PartialUserProfile = DeepPartial<UserProfile>;
type UserWithRequiredId = PartialExcept<UserProfile, "id">;
type StringKeys = KeysOfType<UserProfile, string>; // "id" | "name" | "email" | "avatar"
type RequiredUserKeys = RequiredKeys<UserProfile>; // "id" | "name" | "email" | "settings"
```

### 4.3 泛型實作範例

#### 泛型類別完整實作

```typescript
// utils/Result.ts
export class Result<T, E = Error> {
  private constructor(
    private readonly _isSuccess: boolean,
    private readonly _value?: T,
    private readonly _error?: E
  ) {}

  get isSuccess(): boolean {
    return this._isSuccess;
  }

  get isFailure(): boolean {
    return !this._isSuccess;
  }

  get value(): T {
    if (!this._isSuccess) {
      throw new Error("Cannot get value from failed result");
    }
    return this._value as T;
  }

  get error(): E {
    if (this._isSuccess) {
      throw new Error("Cannot get error from successful result");
    }
    return this._error as E;
  }

  // 靜態工廠方法
  static success<T, E = Error>(value: T): Result<T, E> {
    return new Result<T, E>(true, value);
  }

  static failure<T, E = Error>(error: E): Result<T, E> {
    return new Result<T, E>(false, undefined, error);
  }

  // 函數式方法
  map<U>(fn: (value: T) => U): Result<U, E> {
    if (this._isSuccess) {
      try {
        return Result.success(fn(this._value as T));
      } catch (error) {
        return Result.failure(error as E);
      }
    }
    return Result.failure(this._error as E);
  }

  flatMap<U>(fn: (value: T) => Result<U, E>): Result<U, E> {
    if (this._isSuccess) {
      return fn(this._value as T);
    }
    return Result.failure(this._error as E);
  }

  mapError<F>(fn: (error: E) => F): Result<T, F> {
    if (this._isSuccess) {
      return Result.success(this._value as T);
    }
    return Result.failure(fn(this._error as E));
  }

  // 條件檢查
  match<U>(
    onSuccess: (value: T) => U,
    onFailure: (error: E) => U
  ): U {
    if (this._isSuccess) {
      return onSuccess(this._value as T);
    }
    return onFailure(this._error as E);
  }
}

// 使用範例
async function fetchUser(id: string): Promise<Result<User, string>> {
  try {
    if (!id) {
      return Result.failure("使用者 ID 不能為空");
    }

    const response = await fetch(`/api/users/${id}`);
    
    if (!response.ok) {
      return Result.failure(`HTTP ${response.status}: ${response.statusText}`);
    }

    const userData = await response.json();
    
    if (!isValidUser(userData)) {
      return Result.failure("使用者資料格式不正確");
    }

    return Result.success(userData);
  } catch (error) {
    return Result.failure("網路請求失敗");
  }
}

// 使用 Result
async function displayUserProfile(userId: string): Promise<void> {
  const result = await fetchUser(userId);
  
  result.match(
    (user) => {
      console.log(`歡迎，${user.name}！`);
      updateUI(user);
    },
    (error) => {
      console.error(`錯誤：${error}`);
      showErrorMessage(error);
    }
  );
}
```

#### 進階泛型模式

```typescript
// utils/EventEmitter.ts
export class TypedEventEmitter<TEvents extends Record<string, any[]>> {
  private listeners: {
    [K in keyof TEvents]?: Array<(...args: TEvents[K]) => void>;
  } = {};

  on<K extends keyof TEvents>(
    event: K,
    listener: (...args: TEvents[K]) => void
  ): this {
    if (!this.listeners[event]) {
      this.listeners[event] = [];
    }
    this.listeners[event]!.push(listener);
    return this;
  }

  off<K extends keyof TEvents>(
    event: K,
    listener: (...args: TEvents[K]) => void
  ): this {
    const eventListeners = this.listeners[event];
    if (eventListeners) {
      const index = eventListeners.indexOf(listener);
      if (index > -1) {
        eventListeners.splice(index, 1);
      }
    }
    return this;
  }

  emit<K extends keyof TEvents>(event: K, ...args: TEvents[K]): boolean {
    const eventListeners = this.listeners[event];
    if (eventListeners && eventListeners.length > 0) {
      eventListeners.forEach(listener => {
        try {
          listener(...args);
        } catch (error) {
          console.error(`Event listener error for ${String(event)}:`, error);
        }
      });
      return true;
    }
    return false;
  }

  removeAllListeners<K extends keyof TEvents>(event?: K): this {
    if (event) {
      delete this.listeners[event];
    } else {
      this.listeners = {};
    }
    return this;
  }

  listenerCount<K extends keyof TEvents>(event: K): number {
    return this.listeners[event]?.length ?? 0;
  }
}

// 定義事件型別
interface AppEvents {
  userLogin: [user: User];
  userLogout: [userId: string];
  productAdded: [product: Product];
  error: [error: Error, context?: string];
  statusChange: [status: "loading" | "ready" | "error"];
}

// 使用型別化事件發射器
const eventBus = new TypedEventEmitter<AppEvents>();

// 型別安全的事件監聽
eventBus.on("userLogin", (user) => {
  // TypeScript 知道 user 的型別是 User
  console.log(`使用者 ${user.name} 已登入`);
});

eventBus.on("error", (error, context) => {
  // TypeScript 知道參數型別
  console.error(`錯誤發生 [${context}]:`, error.message);
});

// 型別安全的事件發射
eventBus.emit("userLogin", currentUser);
eventBus.emit("statusChange", "loading");
```

### 4.4 模組化範例

#### ES 模組系統

```typescript
// utils/validators.ts
export interface ValidationRule<T> {
  validate(value: T): boolean;
  message: string;
}

export class RequiredRule implements ValidationRule<any> {
  message = "此欄位為必填";

  validate(value: any): boolean {
    return value !== null && value !== undefined && value !== "";
  }
}

export class EmailRule implements ValidationRule<string> {
  message = "請輸入有效的電子郵件地址";

  validate(value: string): boolean {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(value);
  }
}

export class MinLengthRule implements ValidationRule<string> {
  constructor(private minLength: number) {
    this.message = `長度不能少於 ${minLength} 個字元`;
  }

  message: string;

  validate(value: string): boolean {
    return value.length >= this.minLength;
  }
}

// utils/validator.ts
import { ValidationRule } from "./validators";

export interface ValidationResult {
  isValid: boolean;
  errors: string[];
}

export class Validator<T> {
  private rules: Map<keyof T, ValidationRule<any>[]> = new Map();

  addRule<K extends keyof T>(
    field: K,
    rule: ValidationRule<T[K]>
  ): this {
    if (!this.rules.has(field)) {
      this.rules.set(field, []);
    }
    this.rules.get(field)!.push(rule);
    return this;
  }

  validate(data: T): ValidationResult {
    const errors: string[] = [];

    for (const [field, rules] of this.rules.entries()) {
      const value = data[field];
      for (const rule of rules) {
        if (!rule.validate(value)) {
          errors.push(`${String(field)}: ${rule.message}`);
        }
      }
    }

    return {
      isValid: errors.length === 0,
      errors
    };
  }
}

// services/UserService.ts
import { Validator } from "@/utils/validator";
import { RequiredRule, EmailRule, MinLengthRule } from "@/utils/validators";
import { Repository } from "@/interfaces/Repository";
import { Result } from "@/utils/Result";

export class UserService {
  private validator: Validator<CreateUserRequest>;

  constructor(
    private userRepository: Repository<User>,
    private emailService: EmailService
  ) {
    this.setupValidator();
  }

  private setupValidator(): void {
    this.validator = new Validator<CreateUserRequest>()
      .addRule("name", new RequiredRule())
      .addRule("name", new MinLengthRule(2))
      .addRule("email", new RequiredRule())
      .addRule("email", new EmailRule())
      .addRule("password", new RequiredRule())
      .addRule("password", new MinLengthRule(8));
  }

  async createUser(request: CreateUserRequest): Promise<Result<User, string>> {
    // 驗證輸入資料
    const validationResult = this.validator.validate(request);
    if (!validationResult.isValid) {
      return Result.failure(validationResult.errors.join(", "));
    }

    try {
      // 檢查電子郵件是否已存在
      const existingUser = await this.userRepository.findAll({
        where: { email: request.email }
      });

      if (existingUser.length > 0) {
        return Result.failure("此電子郵件已被註冊");
      }

      // 建立新使用者
      const newUser = await this.userRepository.create({
        name: request.name,
        email: request.email,
        password: await this.hashPassword(request.password)
      });

      // 發送歡迎信件
      await this.emailService.sendWelcomeEmail(newUser.email, newUser.name);

      return Result.success(newUser);
    } catch (error) {
      return Result.failure("建立使用者失敗");
    }
  }

  private async hashPassword(password: string): Promise<string> {
    // 實作密碼雜湊邏輯
    return `hashed_${password}`;
  }
}

interface CreateUserRequest {
  name: string;
  email: string;
  password: string;
}
```

---

**本章重點回顧：**

- 類別設計應遵循封裝原則，適當使用 private、protected、public
- 介面設計要考慮擴展性和重用性
- 泛型讓程式碼更加靈活，但要保持型別安全
- 模組化設計有助於程式碼組織和測試
- 實用工具型別能大幅提升開發效率

**下一章預告：** 我們將探討 TypeScript 的實務應用建議和團隊協作最佳實踐。

---

## 5. 實務建議

### 5.1 善用 TypeScript 的型別檢查

#### 編譯器嚴格模式設定

啟用嚴格模式能幫助捕捉更多潛在錯誤：

```json
// tsconfig.json 嚴格設定
{
  "compilerOptions": {
    "strict": true,                              // 啟用所有嚴格檢查
    "noImplicitAny": true,                       // 禁止隱式 any
    "strictNullChecks": true,                    // 嚴格 null 檢查
    "strictFunctionTypes": true,                 // 嚴格函數型別檢查
    "strictBindCallApply": true,                 // 嚴格檢查 bind/call/apply
    "strictPropertyInitialization": true,       // 嚴格屬性初始化檢查
    "noImplicitThis": true,                     // 禁止隱式 this
    "noImplicitReturns": true,                  // 檢查函數所有路徑都有回傳值
    "noFallthroughCasesInSwitch": true,         // 檢查 switch case 是否遺漏 break
    "noUncheckedIndexedAccess": true,           // 檢查索引存取
    "exactOptionalPropertyTypes": true,         // 精確可選屬性型別
    "noImplicitOverride": true,                 // 需要明確標記 override
    "noPropertyAccessFromIndexSignature": true, // 禁止從索引簽名存取屬性
    "noUnusedLocals": true,                     // 檢查未使用的區域變數
    "noUnusedParameters": true                  // 檢查未使用的參數
  }
}
```

#### 使用型別斷言的最佳實踐

```typescript
// ❌ 避免不安全的型別斷言
function processData(data: unknown): User {
  return data as User; // 危險：沒有驗證
}

// ✅ 使用型別守衛
function isUser(data: unknown): data is User {
  return (
    typeof data === "object" &&
    data !== null &&
    typeof (data as User).id === "string" &&
    typeof (data as User).name === "string" &&
    typeof (data as User).email === "string"
  );
}

function processData(data: unknown): User | null {
  if (isUser(data)) {
    return data; // TypeScript 知道這是 User 型別
  }
  return null;
}

// ✅ 使用 zod 等函式庫進行執行時驗證
import { z } from "zod";

const UserSchema = z.object({
  id: z.string(),
  name: z.string(),
  email: z.string().email(),
  age: z.number().min(0).max(150)
});

type User = z.infer<typeof UserSchema>;

function validateAndParseUser(data: unknown): User {
  return UserSchema.parse(data); // 會拋出錯誤如果驗證失敗
}

function safeParseUser(data: unknown): { success: true; data: User } | { success: false; error: string } {
  const result = UserSchema.safeParse(data);
  if (result.success) {
    return { success: true, data: result.data };
  }
  return { success: false, error: result.error.message };
}
```

#### 利用編譯時檢查防止錯誤

```typescript
// 使用品牌型別防止混用相似型別
type UserId = string & { readonly brand: unique symbol };
type ProductId = string & { readonly brand: unique symbol };

function createUserId(id: string): UserId {
  return id as UserId;
}

function createProductId(id: string): ProductId {
  return id as ProductId;
}

function getUserById(id: UserId): Promise<User> {
  // 實作...
}

function getProductById(id: ProductId): Promise<Product> {
  // 實作...
}

// 編譯時防止錯誤
const userId = createUserId("user-123");
const productId = createProductId("product-456");

getUserById(userId);     // ✅ 正確
getUserById(productId);  // ❌ 編譯錯誤

// 使用常數斷言和映射型別
const THEMES = ["light", "dark", "auto"] as const;
type Theme = typeof THEMES[number]; // "light" | "dark" | "auto"

const STATUS_CODES = {
  OK: 200,
  NOT_FOUND: 404,
  INTERNAL_ERROR: 500
} as const;

type StatusCode = typeof STATUS_CODES[keyof typeof STATUS_CODES]; // 200 | 404 | 500
```

### 5.2 除錯與測試

#### TypeScript 除錯設定

```json
// .vscode/launch.json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug TypeScript",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/src/index.ts",
      "preLaunchTask": "tsc: build - tsconfig.json",
      "outFiles": ["${workspaceFolder}/dist/**/*.js"],
      "sourceMaps": true,
      "skipFiles": ["<node_internals>/**"],
      "env": {
        "NODE_ENV": "development"
      }
    },
    {
      "name": "Debug Jest Tests",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/node_modules/.bin/jest",
      "args": ["--runInBand", "--no-cache"],
      "console": "integratedTerminal",
      "internalConsoleOptions": "neverOpen",
      "disableOptimisticBPs": true,
      "windows": {
        "program": "${workspaceFolder}/node_modules/jest/bin/jest"
      }
    }
  ]
}
```

#### 單元測試最佳實踐

```typescript
// tests/UserService.test.ts
import { UserService } from "../src/services/UserService";
import { MockUserRepository } from "./mocks/MockUserRepository";
import { MockEmailService } from "./mocks/MockEmailService";

describe("UserService", () => {
  let userService: UserService;
  let mockUserRepository: MockUserRepository;
  let mockEmailService: MockEmailService;

  beforeEach(() => {
    mockUserRepository = new MockUserRepository();
    mockEmailService = new MockEmailService();
    userService = new UserService(mockUserRepository, mockEmailService);
  });

  describe("createUser", () => {
    it("should create user successfully with valid data", async () => {
      // Arrange
      const validRequest = {
        name: "王小明",
        email: "wang@example.com",
        password: "password123"
      };

      mockUserRepository.findAll.mockResolvedValue([]);
      mockUserRepository.create.mockResolvedValue({
        id: "user-1",
        ...validRequest,
        createdAt: new Date()
      });

      // Act
      const result = await userService.createUser(validRequest);

      // Assert
      expect(result.isSuccess).toBe(true);
      if (result.isSuccess) {
        expect(result.value.name).toBe(validRequest.name);
        expect(result.value.email).toBe(validRequest.email);
      }
      expect(mockEmailService.sendWelcomeEmail).toHaveBeenCalledWith(
        validRequest.email,
        validRequest.name
      );
    });

    it("should fail with invalid email", async () => {
      // Arrange
      const invalidRequest = {
        name: "王小明",
        email: "invalid-email",
        password: "password123"
      };

      // Act
      const result = await userService.createUser(invalidRequest);

      // Assert
      expect(result.isFailure).toBe(true);
      if (result.isFailure) {
        expect(result.error).toContain("請輸入有效的電子郵件地址");
      }
    });

    it("should fail when email already exists", async () => {
      // Arrange
      const existingUserRequest = {
        name: "李小華",
        email: "existing@example.com",
        password: "password123"
      };

      mockUserRepository.findAll.mockResolvedValue([
        { id: "existing-user", name: "現有用戶", email: "existing@example.com" }
      ]);

      // Act
      const result = await userService.createUser(existingUserRequest);

      // Assert
      expect(result.isFailure).toBe(true);
      if (result.isFailure) {
        expect(result.error).toBe("此電子郵件已被註冊");
      }
    });
  });
});

// tests/mocks/MockUserRepository.ts
import { Repository, RepositoryFilter } from "../../src/interfaces/Repository";
import { User } from "../../src/models/User";

export class MockUserRepository implements Repository<User> {
  findById = jest.fn<Promise<User | null>, [string]>();
  findAll = jest.fn<Promise<User[]>, [RepositoryFilter<User>?]>();
  create = jest.fn<Promise<User>, [Omit<User, "id" | "createdAt" | "updatedAt">]>();
  update = jest.fn<Promise<User | null>, [string, Partial<User>]>();
  delete = jest.fn<Promise<boolean>, [string]>();
  count = jest.fn<Promise<number>, [RepositoryFilter<User>?]>();
}
```

#### 型別測試

```typescript
// tests/types.test.ts
import { expectType, expectAssignable, expectNotAssignable } from "tsd";
import { User, CreateUserRequest } from "../src/types/user";
import { Result } from "../src/utils/Result";

// 測試型別正確性
expectType<string>(new User("1", "Test", "test@example.com").id);
expectType<Date>(new User("1", "Test", "test@example.com").createdAt);

// 測試型別相容性
expectAssignable<CreateUserRequest>({
  name: "Test User",
  email: "test@example.com",
  password: "password123"
});

// 測試型別不相容
expectNotAssignable<CreateUserRequest>({
  name: "Test User",
  // 缺少 email 和 password
});

// 測試 Result 型別
expectType<Result<User, string>>(Result.success(new User("1", "Test", "test@example.com")));
expectType<Result<User, string>>(Result.failure("Error message"));
```

### 5.3 團隊協作與程式風格統一

#### ESLint 與 Prettier 設定

```json
// .eslintrc.json
{
  "extends": [
    "@typescript-eslint/recommended",
    "@typescript-eslint/recommended-requiring-type-checking",
    "prettier"
  ],
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaVersion": 2020,
    "sourceType": "module",
    "project": "./tsconfig.json"
  },
  "plugins": ["@typescript-eslint", "import"],
  "rules": {
    "@typescript-eslint/no-unused-vars": "error",
    "@typescript-eslint/no-explicit-any": "warn",
    "@typescript-eslint/explicit-function-return-type": "warn",
    "@typescript-eslint/no-non-null-assertion": "error",
    "@typescript-eslint/prefer-nullish-coalescing": "error",
    "@typescript-eslint/prefer-optional-chain": "error",
    "@typescript-eslint/no-floating-promises": "error",
    "@typescript-eslint/await-thenable": "error",
    "import/order": [
      "error",
      {
        "groups": [
          "builtin",
          "external",
          "internal",
          "parent",
          "sibling",
          "index"
        ],
        "newlines-between": "always",
        "alphabetize": {
          "order": "asc",
          "caseInsensitive": true
        }
      }
    ]
  }
}
```

```json
// .prettierrc
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": false,
  "printWidth": 80,
  "tabWidth": 2,
  "useTabs": false,
  "bracketSpacing": true,
  "arrowParens": "avoid",
  "endOfLine": "lf"
}
```

#### Git Hooks 設定

```json
// package.json
{
  "scripts": {
    "lint": "eslint src/**/*.ts",
    "lint:fix": "eslint src/**/*.ts --fix",
    "type-check": "tsc --noEmit",
    "format": "prettier --write src/**/*.ts",
    "pre-commit": "lint-staged"
  },
  "lint-staged": {
    "*.{ts,tsx}": [
      "eslint --fix",
      "prettier --write",
      "git add"
    ]
  },
  "husky": {
    "hooks": {
      "pre-commit": "npm run pre-commit",
      "pre-push": "npm run type-check && npm test"
    }
  }
}
```

#### 程式碼審查檢查清單

**型別安全性檢查：**

- [ ] 避免使用 `any` 型別，使用具體型別或 `unknown`
- [ ] 適當處理 `null` 和 `undefined`
- [ ] 使用型別守衛而非型別斷言
- [ ] 泛型使用是否合理且有型別約束

**程式碼品質檢查：**

- [ ] 函數職責是否單一且明確
- [ ] 變數和函數命名是否清楚描述其用途
- [ ] 是否有適當的錯誤處理
- [ ] 程式碼是否遵循 SOLID 原則

**效能考量：**

- [ ] 避免不必要的型別計算
- [ ] 合理使用 `readonly` 和 `const assertions`
- [ ] 避免深層嵌套的條件型別

**測試覆蓋：**

- [ ] 關鍵功能是否有單元測試
- [ ] 邊界條件是否有測試案例
- [ ] 型別定義是否有對應的型別測試

#### 文件化最佳實踐

```typescript
/**
 * 使用者服務類別，負責處理使用者相關的業務邏輯
 * 
 * @example
 * ```typescript
 * const userService = new UserService(userRepository, emailService);
 * const result = await userService.createUser({
 *   name: "王小明",
 *   email: "wang@example.com",
 *   password: "securePassword123"
 * });
 * 
 * if (result.isSuccess) {
 *   console.log("使用者建立成功:", result.value.name);
 * }
 * ```
 */
export class UserService {
  /**
   * 建立新使用者
   * 
   * @param request - 建立使用者的請求資料
   * @returns Promise<Result<User, string>> - 包含建立結果的 Promise
   * 
   * @throws 不會拋出例外，所有錯誤都包裝在 Result 中
   * 
   * @example
   * ```typescript
   * const result = await userService.createUser({
   *   name: "李小華",
   *   email: "lee@example.com", 
   *   password: "password123"
   * });
   * ```
   */
  async createUser(request: CreateUserRequest): Promise<Result<User, string>> {
    // 實作...
  }
}

/**
 * 建立使用者的請求介面
 * 
 * @interface CreateUserRequest
 */
interface CreateUserRequest {
  /** 使用者姓名，長度必須在 2-50 字元之間 */
  name: string;
  
  /** 電子郵件地址，必須符合有效的電子郵件格式 */
  email: string;
  
  /** 密碼，長度必須至少 8 個字元 */
  password: string;
}
```

---

**本章重點回顧：**

- 啟用 TypeScript 嚴格模式以獲得最大的型別安全性
- 使用型別守衛和執行時驗證替代不安全的型別斷言
- 建立完整的測試策略，包括單元測試和型別測試
- 使用 ESLint、Prettier 和 Git Hooks 統一程式碼風格
- 良好的文件化有助於團隊協作和程式碼維護

---

## 6. 檢查清單

### 6.1 專案建立檢查清單

#### 初始設定

- [ ] **安裝 TypeScript**
  ```bash
  npm install -D typescript @types/node
  ```

- [ ] **建立 tsconfig.json**
  ```bash
  npx tsc --init
  ```

- [ ] **設定專案目錄結構**
  ```
  src/
  ├── components/
  ├── services/
  ├── types/
  ├── utils/
  └── index.ts
  ```

- [ ] **安裝開發工具**
  ```bash
  npm install -D eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin
  npm install -D prettier eslint-config-prettier
  npm install -D husky lint-staged
  ```

#### 設定檔配置

- [ ] **tsconfig.json 嚴格模式**
  - [ ] `"strict": true`
  - [ ] `"noImplicitAny": true`
  - [ ] `"strictNullChecks": true`
  - [ ] `"noImplicitReturns": true`

- [ ] **ESLint 設定**
  - [ ] TypeScript 專用規則
  - [ ] Import 排序規則
  - [ ] 禁用 `any` 型別警告

- [ ] **Git Hooks 設定**
  - [ ] pre-commit: 程式碼格式化和檢查
  - [ ] pre-push: 型別檢查和測試

### 6.2 開發期間檢查清單

#### 型別定義

- [ ] **介面和型別**
  - [ ] 所有公開介面都有完整的型別定義
  - [ ] 使用 `interface` 定義物件結構
  - [ ] 使用 `type` 定義聯合型別和複雜型別
  - [ ] 適當使用泛型增加重用性

- [ ] **函數定義**
  - [ ] 明確指定參數型別
  - [ ] 明確指定回傳型別
  - [ ] 處理可能的 `null` 和 `undefined`
  - [ ] 使用 Result 模式處理錯誤

#### 程式碼品質

- [ ] **命名規範**
  - [ ] 變數使用 camelCase
  - [ ] 類別使用 PascalCase
  - [ ] 常數使用 UPPER_SNAKE_CASE
  - [ ] 檔案命名一致性

- [ ] **函數設計**
  - [ ] 單一職責原則
  - [ ] 函數長度適中（< 20 行）
  - [ ] 避免深層嵌套（< 3 層）
  - [ ] 有意義的函數名稱

#### 錯誤處理

- [ ] **防禦性程式設計**
  - [ ] 輸入驗證
  - [ ] 邊界條件檢查
  - [ ] 適當的例外處理
  - [ ] 有意義的錯誤訊息

### 6.3 程式碼審查檢查清單

#### 型別安全性

- [ ] **型別檢查**
  - [ ] 沒有使用 `any` 型別
  - [ ] 正確處理 `null` 和 `undefined`
  - [ ] 使用型別守衛而非型別斷言
  - [ ] 泛型使用合理且有約束

- [ ] **API 整合**
  - [ ] 外部 API 資料有型別驗證
  - [ ] 使用 unknown 處理未知資料
  - [ ] 適當的錯誤處理機制

#### 效能和維護性

- [ ] **程式碼組織**
  - [ ] 模組化設計
  - [ ] 循環相依檢查
  - [ ] 合理的檔案大小
  - [ ] 清楚的目錄結構

- [ ] **測試覆蓋**
  - [ ] 關鍵功能有單元測試
  - [ ] 邊界條件測試
  - [ ] Mock 使用適當
  - [ ] 測試案例命名清楚

### 6.4 部署前檢查清單

#### 建置和測試

- [ ] **編譯檢查**
  ```bash
  npm run type-check    # TypeScript 編譯檢查
  npm run lint         # ESLint 檢查
  npm run test         # 單元測試
  npm run build        # 建置檢查
  ```

- [ ] **程式碼品質**
  - [ ] 所有 ESLint 警告已解決
  - [ ] 程式碼格式化一致
  - [ ] 沒有 TODO 或 FIXME 註解
  - [ ] 移除 console.log 和除錯程式碼

#### 文件和註解

- [ ] **文件化**
  - [ ] API 文件已更新
  - [ ] README 包含最新的安裝和使用說明
  - [ ] 重要函數有 JSDoc 註解
  - [ ] 型別定義有適當的註解

- [ ] **版本控制**
  - [ ] 提交訊息清楚描述變更
  - [ ] 沒有敏感資訊在程式碼中
  - [ ] 分支命名符合規範
  - [ ] Pull Request 描述完整

### 6.5 常見問題快速檢查

#### 編譯錯誤

- [ ] **型別錯誤排查**
  - [ ] 檢查變數型別定義
  - [ ] 確認函數參數和回傳型別
  - [ ] 檢查 null/undefined 處理
  - [ ] 確認模組 import/export

- [ ] **設定問題**
  - [ ] tsconfig.json 路徑設定
  - [ ] 模組解析設定
  - [ ] 編譯目標版本
  - [ ] include/exclude 設定

#### 執行時錯誤

- [ ] **資料驗證**
  - [ ] API 回應格式檢查
  - [ ] 輸入資料驗證
  - [ ] 型別守衛實作
  - [ ] 錯誤處理邏輯

---

**總結**

這份檢查清單涵蓋了 TypeScript 專案從建立到部署的完整流程。建議將此清單加入到團隊的開發流程中，確保程式碼品質和型別安全性。

定期檢視和更新這些檢查項目，隨著專案成長和團隊經驗累積，持續改善開發流程和程式碼品質。

---

## 7. 進階主題

### 7.1 條件型別 (Conditional Types)

條件型別允許我們根據型別條件來選擇不同的型別，類似於程式中的三元運算子：

```typescript
// 基本條件型別語法
type ConditionalType<T> = T extends string ? string[] : number[];

type Example1 = ConditionalType<string>;  // string[]
type Example2 = ConditionalType<number>;  // number[]

// 實用的條件型別範例
type NonNullable<T> = T extends null | undefined ? never : T;

type ApiResponse<T> = T extends string 
  ? { message: T }
  : T extends number 
  ? { code: T }
  : { data: T };

// 分散式條件型別
type ToArray<T> = T extends any ? T[] : never;
type StrArrOrNumArr = ToArray<string | number>; // string[] | number[]
```

#### 高級條件型別模式

```typescript
// 提取型別資訊
type GetReturnType<T> = T extends (...args: any[]) => infer R ? R : never;
type GetFirstParameter<T> = T extends (first: infer P, ...args: any[]) => any ? P : never;

// 使用範例
function processUser(user: User): Promise<User> {
  return Promise.resolve(user);
}

type ReturnType = GetReturnType<typeof processUser>; // Promise<User>
type FirstParam = GetFirstParameter<typeof processUser>; // User

// 遞迴條件型別
type Flatten<T> = T extends readonly (infer U)[] 
  ? Flatten<U> 
  : T;

type DeepArray = number[][][];
type Flattened = Flatten<DeepArray>; // number

// 字串操作型別
type Capitalize<S extends string> = S extends `${infer F}${infer R}`
  ? `${Uppercase<F>}${R}`
  : S;

type CamelCase<S extends string> = S extends `${infer P1}_${infer P2}${infer P3}`
  ? `${P1}${Capitalize<CamelCase<`${P2}${P3}`>>}`
  : S;

type Example = CamelCase<"user_profile_data">; // "userProfileData"
```

### 7.2 映射型別 (Mapped Types)

映射型別讓我們能基於現有型別創建新的型別：

```typescript
// 基本映射型別
type ReadOnly<T> = {
  readonly [P in keyof T]: T[P];
};

type Optional<T> = {
  [P in keyof T]?: T[P];
};

// 進階映射型別
type Getters<T> = {
  [P in keyof T as `get${Capitalize<string & P>}`]: () => T[P];
};

interface User {
  name: string;
  age: number;
  email: string;
}

type UserGetters = Getters<User>;
// {
//   getName: () => string;
//   getAge: () => number;
//   getEmail: () => string;
// }

// 條件映射型別
type PickByType<T, U> = {
  [P in keyof T as T[P] extends U ? P : never]: T[P];
};

type StringFields = PickByType<User, string>; // { name: string; email: string; }

// 模板字面量型別映射
type EventHandlers<T> = {
  [K in keyof T as `on${Capitalize<string & K>}`]: (value: T[K]) => void;
};

type UserEventHandlers = EventHandlers<User>;
// {
//   onName: (value: string) => void;
//   onAge: (value: number) => void;
//   onEmail: (value: string) => void;
// }
```

### 7.3 模板字面型別 (Template Literal Types)

模板字面量型別允許我們使用模板字面量語法來操作字串型別：

```typescript
// 基本模板字面量型別
type Greeting = `Hello, ${string}!`;
type ApiEndpoint = `/api/${string}`;

// 結合聯合型別
type HttpMethod = "GET" | "POST" | "PUT" | "DELETE";
type ApiRoute = "users" | "products" | "orders";
type ApiCall = `${HttpMethod} /api/${ApiRoute}`;

// 實際使用範例
interface ApiConfig {
  [K in ApiCall]: {
    url: string;
    handler: Function;
  };
}

// 動態屬性名稱
type EventType = "click" | "hover" | "focus";
type ElementId = "button" | "input" | "form";

type EventHandler = {
  [K in `${ElementId}_${EventType}`]: (event: Event) => void;
};

// CSS 樣式型別
type CSSUnit = "px" | "em" | "rem" | "%";
type CSSProperty = "margin" | "padding" | "width" | "height";
type CSSValue = `${number}${CSSUnit}`;

type CSSStyles = {
  [K in CSSProperty]: CSSValue;
};

// 路由型別系統
type RouteParams<T extends string> = T extends `${string}:${infer Param}/${infer Rest}`
  ? { [K in Param]: string } & RouteParams<Rest>
  : T extends `${string}:${infer Param}`
  ? { [K in Param]: string }
  : {};

type UserRouteParams = RouteParams<"/users/:id/posts/:postId">; 
// { id: string; postId: string; }
```

### 7.4 裝飾器 (Decorators)

裝飾器是一種特殊的聲明，可以附加到類別、方法、存取器、屬性或參數上。裝飾器使用 `@expression` 語法：

```typescript
// 啟用裝飾器（在 tsconfig.json 中設定）
{
  "compilerOptions": {
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true
  }
}

// 類別裝飾器
function Component(target: any) {
  // 為類別添加額外的功能
  target.prototype.render = function() {
    return `<div>${this.name}</div>`;
  };
}

@Component
class MyComponent {
  name = "Hello World";
}

// 方法裝飾器
function Log(target: any, propertyName: string, descriptor: PropertyDescriptor) {
  const method = descriptor.value;
  
  descriptor.value = function (...args: any[]) {
    console.log(`呼叫方法 ${propertyName}，參數:`, args);
    const result = method.apply(this, args);
    console.log(`方法 ${propertyName} 回傳:`, result);
    return result;
  };
}

class Calculator {
  @Log
  add(a: number, b: number): number {
    return a + b;
  }
}

// 屬性裝飾器
function Required(target: any, propertyName: string) {
  // 標記必填欄位
  const requiredFields = target.constructor.requiredFields || [];
  requiredFields.push(propertyName);
  target.constructor.requiredFields = requiredFields;
}

class User {
  @Required
  name: string;
  
  @Required
  email: string;
  
  age?: number;
}

// 參數裝飾器
function Validate(target: any, propertyName: string, parameterIndex: number) {
  // 記錄需要驗證的參數
  console.log(`參數 ${parameterIndex} 在方法 ${propertyName} 中需要驗證`);
}

class UserService {
  createUser(@Validate name: string, @Validate email: string) {
    // 建立使用者邏輯
  }
}
```

#### 實際應用範例

```typescript
// 快取裝飾器
function Cache(ttl: number = 60000) { // 預設快取 1 分鐘
  return function (target: any, propertyName: string, descriptor: PropertyDescriptor) {
    const originalMethod = descriptor.value;
    const cache = new Map();
    
    descriptor.value = function (...args: any[]) {
      const key = JSON.stringify(args);
      const now = Date.now();
      
      if (cache.has(key)) {
        const { data, timestamp } = cache.get(key);
        if (now - timestamp < ttl) {
          return data;
        }
      }
      
      const result = originalMethod.apply(this, args);
      cache.set(key, { data: result, timestamp: now });
      return result;
    };
  };
}

// 使用快取裝飾器
class ApiService {
  @Cache(30000) // 快取 30 秒
  async fetchUserData(userId: string): Promise<User> {
    // 實際的 API 呼叫
    const response = await fetch(`/api/users/${userId}`);
    return response.json();
  }
}
```

---

## 8. 效能優化與最佳實踐

### 8.1 編譯效能優化

#### 專案組態最佳化

```json
// tsconfig.json 效能設定
{
  "compilerOptions": {
    // 跳過型別定義檔案檢查以提升速度
    "skipLibCheck": true,
    
    // 只檢查實際使用的檔案
    "skipDefaultLibCheck": true,
    
    // 增量編譯
    "incremental": true,
    "tsBuildInfoFile": ".tsbuildinfo",
    
    // 專案參考（大型專案）
    "composite": true,
    "declaration": true,
    "declarationMap": true,
    
    // 模組解析優化
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true,
    "esModuleInterop": true,
    
    // 減少型別檢查負擔
    "isolatedModules": true,
    "noEmit": true
  },
  "include": ["src/**/*"],
  "exclude": [
    "node_modules",
    "dist",
    "**/*.test.ts",
    "**/*.spec.ts"
  ]
}
```

#### 專案參考 (Project References)

```json
// 根目錄 tsconfig.json
{
  "files": [],
  "references": [
    { "path": "./packages/core" },
    { "path": "./packages/ui" },
    { "path": "./packages/utils" }
  ]
}

// packages/core/tsconfig.json
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "composite": true,
    "rootDir": "./src",
    "outDir": "./dist"
  },
  "include": ["src/**/*"],
  "references": [
    { "path": "../utils" }
  ]
}
```

### 8.2 型別檢查效能

#### 避免複雜的型別運算

```typescript
// ❌ 複雜的遞迴型別（可能導致編譯緩慢）
type DeepFlatten<T> = T extends readonly (infer U)[]
  ? U extends readonly (infer V)[]
    ? V extends readonly (infer W)[]
      ? W extends readonly (infer X)[]
        ? X extends readonly (infer Y)[]
          ? Y
          : X
        : W
      : V
    : U
  : T;

// ✅ 簡化或使用適當的深度限制
type Flatten<T, Depth extends number = 5> = 
  Depth extends 0 
    ? T
    : T extends readonly (infer U)[]
    ? Flatten<U, Prev<Depth>>
    : T;

type Prev<T extends number> = T extends 0 ? 0 : T extends 1 ? 0 : T extends 2 ? 1 : T extends 3 ? 2 : T extends 4 ? 3 : T extends 5 ? 4 : number;
```

#### 使用型別快取

```typescript
// 使用 type alias 快取複雜型別
type CachedComplexType<T> = {
  [K in keyof T]: T[K] extends Function 
    ? T[K] 
    : T[K] extends object 
    ? CachedComplexType<T[K]> 
    : T[K];
};

// 一次計算，多次使用
type ProcessedUser = CachedComplexType<User>;
type ProcessedProduct = CachedComplexType<Product>;
```

### 8.3 打包優化

#### 型別守衛最佳化

```typescript
// ✅ 使用高效的型別守衛
function isUser(obj: unknown): obj is User {
  return (
    typeof obj === "object" &&
    obj !== null &&
    "id" in obj &&
    "name" in obj &&
    "email" in obj
  );
}

// ✅ 使用 discriminated unions 提升效能
interface LoadingState {
  status: "loading";
}

interface SuccessState {
  status: "success";
  data: any;
}

interface ErrorState {
  status: "error";
  error: string;
}

type AsyncState = LoadingState | SuccessState | ErrorState;

function handleState(state: AsyncState) {
  // TypeScript 能有效地進行型別縮小
  switch (state.status) {
    case "loading":
      // 只有 LoadingState 的屬性可用
      break;
    case "success":
      // 只有 SuccessState 的屬性可用
      console.log(state.data);
      break;
    case "error":
      // 只有 ErrorState 的屬性可用
      console.error(state.error);
      break;
  }
}
```

#### 避免過度的型別運算

```typescript
// ❌ 每次都重新計算型別
function processData<T>(data: T): Omit<T, "id"> & { processedAt: Date } {
  // 這會在每次調用時重新計算型別
  const { id, ...rest } = data as any;
  return { ...rest, processedAt: new Date() };
}

// ✅ 預先定義好型別
type ProcessedData<T> = Omit<T, "id"> & { processedAt: Date };

function processData<T>(data: T): ProcessedData<T> {
  const { id, ...rest } = data as any;
  return { ...rest, processedAt: new Date() };
}
```

### 8.4 記憶體使用優化

#### 適當使用 readonly

```typescript
// 使用 readonly 減少不必要的防禦性複製
interface ReadOnlyConfig {
  readonly apiUrl: string;
  readonly timeout: number;
  readonly retryCount: number;
  readonly endpoints: readonly string[];
}

// 使用 const assertions
const themes = ["light", "dark", "auto"] as const;
const config = {
  theme: "light",
  version: "1.0.0"
} as const;
```

#### 型別收窄策略

```typescript
// ✅ 使用聯合型別而非泛型（當適合時）
type ApiResult = 
  | { success: true; data: any }
  | { success: false; error: string };

// ✅ 而非過度泛型化
interface ApiResult<T, E = string> {
  success: boolean;
  data?: T;
  error?: E;
}
```

---

## 9. TypeScript 生態系統

### 9.1 開發工具

#### VS Code 設定優化

```json
// .vscode/settings.json
{
  "typescript.preferences.quoteStyle": "double",
  "typescript.preferences.semicolons": "insert",
  "typescript.suggest.autoImports": true,
  "typescript.suggest.paths": true,
  "typescript.preferences.organizeImports": true,
  "typescript.inlayHints.parameterNames.enabled": "all",
  "typescript.inlayHints.variableTypes.enabled": true,
  "typescript.inlayHints.functionLikeReturnTypes.enabled": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true,
    "source.fixAll.eslint": true
  },
  "typescript.updateImportsOnFileMove.enabled": "always"
}
```

#### 推薦的 VS Code 擴充功能

```json
// .vscode/extensions.json
{
  "recommendations": [
    "ms-vscode.vscode-typescript-next",
    "esbenp.prettier-vscode",
    "dbaeumer.vscode-eslint",
    "bradlc.vscode-tailwindcss",
    "ms-vscode.vscode-json",
    "christian-kohler.path-intellisense",
    "ms-vscode.vscode-typescript-tslint-plugin"
  ]
}
```

### 9.2 測試框架

#### Webpack 整合

```typescript
// webpack.config.ts
import { Configuration } from "webpack";
import path from "path";

const config: Configuration = {
  mode: "development",
  entry: "./src/index.ts",
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: {
          loader: "ts-loader",
          options: {
            configFile: path.resolve(__dirname, "tsconfig.json"),
            transpileOnly: true, // 只轉譯，型別檢查交給 fork-ts-checker-webpack-plugin
          },
        },
        exclude: /node_modules/,
      },
    ],
  },
  resolve: {
    extensions: [".tsx", ".ts", ".js"],
    alias: {
      "@": path.resolve(__dirname, "src"),
    },
  },
  plugins: [
    new (require("fork-ts-checker-webpack-plugin"))({
      typescript: {
        configFile: path.resolve(__dirname, "tsconfig.json"),
      },
    }),
  ],
};

export default config;
```

#### Vite 整合

```typescript
// vite.config.ts
import { defineConfig } from "vite";
import { resolve } from "path";

export default defineConfig({
  resolve: {
    alias: {
      "@": resolve(__dirname, "src"),
    },
  },
  build: {
    lib: {
      entry: resolve(__dirname, "src/index.ts"),
      name: "MyLibrary",
      fileName: (format) => `my-library.${format}.js`,
    },
    rollupOptions: {
      external: ["vue", "react"],
      output: {
        globals: {
          vue: "Vue",
          react: "React",
        },
      },
    },
  },
  esbuild: {
    target: "esnext",
  },
});
```

### 9.3 建置工具

#### Jest 設定

```typescript
// jest.config.ts
import type { Config } from "@jest/types";

const config: Config.InitialOptions = {
  preset: "ts-jest",
  testEnvironment: "node",
  roots: ["<rootDir>/src"],
  testMatch: ["**/__tests__/**/*.ts", "**/?(*.)+(spec|test).ts"],
  transform: {
    "^.+\\.ts$": "ts-jest",
  },
  collectCoverageFrom: [
    "src/**/*.ts",
    "!src/**/*.d.ts",
    "!src/**/*.test.ts",
    "!src/**/*.spec.ts",
  ],
  moduleNameMapping: {
    "^@/(.*)$": "<rootDir>/src/$1",
  },
  setupFilesAfterEnv: ["<rootDir>/src/test/setup.ts"],
};

export default config;
```

#### Vitest 設定

```typescript
// vitest.config.ts
import { defineConfig } from "vitest/config";
import { resolve } from "path";

export default defineConfig({
  test: {
    environment: "node",
    globals: true,
    setupFiles: ["./src/test/setup.ts"],
  },
  resolve: {
    alias: {
      "@": resolve(__dirname, "src"),
    },
  },
});
```

### 9.4 型別定義管理

#### 自訂型別定義

```typescript
// types/global.d.ts
declare global {
  interface Window {
    gtag: (command: string, targetId: string, config?: any) => void;
    dataLayer: any[];
  }

  namespace NodeJS {
    interface ProcessEnv {
      NODE_ENV: "development" | "production" | "test";
      API_BASE_URL: string;
      DATABASE_URL: string;
    }
  }
}

// 模組擴展
declare module "*.vue" {
  import { DefineComponent } from "vue";
  const component: DefineComponent<{}, {}, any>;
  export default component;
}

declare module "*.svg" {
  const content: string;
  export default content;
}

// 第三方套件型別擴展
declare module "lodash" {
  interface LoDashStatic {
    customMethod(value: any): any;
  }
}
```

#### 套件型別管理

```typescript
// types/api.d.ts - API 回應型別統一管理
declare namespace API {
  interface BaseResponse {
    success: boolean;
    message: string;
    timestamp: string;
  }

  interface PaginatedResponse<T> extends BaseResponse {
    data: T[];
    pagination: {
      page: number;
      limit: number;
      total: number;
      hasNext: boolean;
      hasPrev: boolean;
    };
  }

  namespace User {
    interface Detail {
      id: string;
      name: string;
      email: string;
      avatar?: string;
      createdAt: string;
      updatedAt: string;
    }

    interface CreateRequest {
      name: string;
      email: string;
      password: string;
    }

    interface UpdateRequest {
      name?: string;
      avatar?: string;
    }

    interface ListResponse extends PaginatedResponse<Detail> {}
  }
}
```

---

## 10. 常見問題與解決方案

### 10.1 編譯錯誤

#### 模組解析問題

```typescript
// 問題：Cannot find module '@/components/Button' or its corresponding type declarations

// 解決方案 1：檢查 tsconfig.json 路徑設定
{
  "compilerOptions": {
    "baseUrl": "./",
    "paths": {
      "@/*": ["src/*"],
      "@/components/*": ["src/components/*"]
    }
  }
}

// 解決方案 2：確認檔案結構
src/
├── components/
│   ├── Button.tsx
│   └── index.ts  // 統一匯出

// 解決方案 3：明確的副檔名
import { Button } from "@/components/Button"; // ✅
// 或
import { Button } from "@/components/Button.js"; // ✅ (在某些配置下)
```

#### 型別定義衝突

```typescript
// 問題：Type 'string' is not assignable to type 'never'

// 原因：聯合型別縮小失敗
function processValue(value: string | number) {
  if (typeof value === "string") {
    // 在某些複雜情況下，TypeScript 可能無法正確縮小型別
    return value.toUpperCase(); // 錯誤：value 被推斷為 never
  }
}

// 解決方案：明確的型別斷言或重構
function processValue(value: string | number): string {
  if (typeof value === "string") {
    return (value as string).toUpperCase(); // 明確斷言
  }
  return value.toString().toUpperCase();
}

// 更好的解決方案：使用函數多載
function processValue(value: string): string;
function processValue(value: number): string;
function processValue(value: string | number): string {
  return typeof value === "string" ? value.toUpperCase() : value.toString().toUpperCase();
}
```

### 10.2 型別推斷問題

#### 編譯速度緩慢

```bash
# 問題診斷
npx tsc --listFiles > compilation-files.txt
npx tsc --traceResolution > trace.txt
npx tsc --generateTrace trace-output

# 解決方案
## 1. 啟用增量編譯
{
  "compilerOptions": {
    "incremental": true,
    "tsBuildInfoFile": ".tsbuildinfo"
  }
}

## 2. 排除不必要的檔案
{
  "exclude": [
    "node_modules",
    "dist",
    "coverage",
    "**/*.test.ts",
    "**/*.spec.ts",
    "**/temp/**"
  ]
}

## 3. 使用專案參考
{
  "extends": "./tsconfig.base.json",
  "compilerOptions": {
    "composite": true
  },
  "references": [
    { "path": "./shared" }
  ]
}
```

#### 記憶體使用過高

```typescript
// 問題：複雜的型別運算導致記憶體使用過高

// ❌ 避免過度複雜的遞迴型別
type DeepReadonly<T> = {
  readonly [P in keyof T]: T[P] extends object 
    ? DeepReadonly<T[P]> 
    : T[P];
};

// ✅ 限制遞迴深度
type DeepReadonly<T, Depth extends number = 3> = Depth extends 0
  ? T
  : {
      readonly [P in keyof T]: T[P] extends object
        ? DeepReadonly<T[P], Prev<Depth>>
        : T[P];
    };

// ✅ 或使用更簡單的替代方案
type SimpleReadonly<T> = {
  readonly [P in keyof T]: T[P];
};
```

### 10.3 執行時期問題

#### 型別與執行時期資料不匹配

```typescript
// 問題：API 回應與型別定義不匹配

// ❌ 危險的直接型別斷言
async function fetchUser(id: string): Promise<User> {
  const response = await fetch(`/api/users/${id}`);
  const data = await response.json();
  return data as User; // 沒有驗證
}

// ✅ 使用執行時期驗證
import { z } from "zod";

const UserSchema = z.object({
  id: z.string(),
  name: z.string(),
  email: z.string().email(),
  age: z.number().min(0).max(150)
});

type User = z.infer<typeof UserSchema>;

async function fetchUser(id: string): Promise<Result<User, string>> {
  try {
    const response = await fetch(`/api/users/${id}`);
    
    if (!response.ok) {
      return Result.failure(`HTTP ${response.status}: ${response.statusText}`);
    }
    
    const data = await response.json();
    const validatedUser = UserSchema.parse(data);
    
    return Result.success(validatedUser);
  } catch (error) {
    if (error instanceof z.ZodError) {
      return Result.failure(`資料驗證失敗: ${error.message}`);
    }
    return Result.failure("網路請求失敗");
  }
}
```

#### 第三方套件型別問題

```typescript
// 問題：第三方套件沒有型別定義或型別不完整

// 解決方案 1：自訂型別定義
// types/vendor.d.ts
declare module "some-package" {
  interface SomePackageOptions {
    option1: string;
    option2?: number;
  }
  
  export function someFunction(options: SomePackageOptions): Promise<any>;
  export default someFunction;
}

// 解決方案 2：模組擴展
declare module "existing-package" {
  interface ExistingInterface {
    newProperty: string;
  }
}

// 解決方案 3：使用 DefinitelyTyped
npm install --save-dev @types/package-name
```

### 10.4 最佳實踐檢查清單

#### 程式碼品質檢查

- [ ] **型別安全性**
  - [ ] 避免使用 `any` 型別
  - [ ] 適當處理 `null` 和 `undefined`
  - [ ] 使用型別守衛進行執行時期驗證
  - [ ] 明確定義函數回傳型別

- [ ] **效能考量**
  - [ ] 避免過度複雜的型別運算
  - [ ] 使用適當的型別快取策略
  - [ ] 啟用增量編譯
  - [ ] 排除不必要的檔案

- [ ] **可維護性**
  - [ ] 一致的命名慣例
  - [ ] 適當的程式碼組織
  - [ ] 完整的型別定義
  - [ ] 清楚的介面設計

#### 團隊協作檢查

- [ ] **工具設定**
  - [ ] ESLint 和 Prettier 配置
  - [ ] Git hooks 設定
  - [ ] VS Code 設定同步
  - [ ] 統一的 tsconfig.json

- [ ] **文件化**
  - [ ] API 文件更新
  - [ ] 型別定義註解
  - [ ] 範例程式碼
  - [ ] 最佳實踐指南

---

## 總結

這份完整的 TypeScript 教學手冊涵蓋了從基礎概念到進階應用的所有重要主題。透過系統性的學習和實踐，開發者能夠充分掌握 TypeScript 的強大功能，提升程式碼品質和開發效率。

記住，TypeScript 的核心價值在於型別安全性和開發體驗的提升。持續學習新特性，關注社群最佳實踐，並在專案中逐步應用這些知識，將有助於成為一名優秀的 TypeScript 開發者。

---

## 📚 延伸學習資源

### 官方文件

- [TypeScript 官方手冊](https://www.typescriptlang.org/docs/)
- [TypeScript 遊樂場](https://www.typescriptlang.org/play/)

### 社群資源

- [TypeScript Deep Dive](https://basarat.gitbook.io/typescript/)
- [Type Challenges](https://github.com/type-challenges/type-challenges)

### 工具和函式庫

- [zod](https://zod.dev/) - 執行時型別驗證
- [io-ts](https://gcanti.github.io/io-ts/) - 函數式型別驗證
- [tRPC](https://trpc.io/) - 端到端型別安全的 API

---

> **文件資訊**  
> 版本：v2.0  
> 最後更新：2025年8月31日  
> 作者：開發團隊
