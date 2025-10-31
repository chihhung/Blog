+++
date = '2025-10-31T00:00:00+08:00'
draft = false
title = 'UIUX指引'
tags = ['指引', '設計開發']
categories = ['指引']
+++
# UI/UX 開發指引

## 目錄

1. [文件概述](#文件概述)
2. [設計原則](#1-設計原則)
   - 1.1 [銀行系統的安全性與一致性要求](#11-銀行系統的安全性與一致性要求)
   - 1.2 [清晰的資訊層次與導航設計](#12-清晰的資訊層次與導航設計)
   - 1.3 [金融資料顯示與重點突顯規範](#13-金融資料顯示與重點突顯規範)
   - 1.4 [無障礙設計（WCAG 2.1 AA 級）](#14-無障礙設計wcag-21-aa-級)
   - 1.5 [多語系支援](#15-多語系支援)
3. [UI 元件規範](#2-ui-元件規範)
   - 2.1 [樣式系統 (Design System)](#21-樣式系統-design-system)
   - 2.2 [響應式設計規範](#22-響應式設計規範)
   - 2.3 [常用元件設計](#23-常用元件設計)
4. [UX 流程規範](#3-ux-流程規範)
   - 3.1 [表單驗證與錯誤回饋](#31-表單驗證與錯誤回饋)
   - 3.2 [使用者引導 (Onboarding)](#32-使用者引導-onboarding)
   - 3.3 [搜尋、篩選與排序互動設計](#33-搜尋篩選與排序互動設計)
   - 3.4 [資料載入與狀態設計](#34-資料載入與狀態設計)
5. [設計資產與交付](#4-設計資產與交付)
   - 4.1 [設計 Token 系統](#41-設計-token-系統)
   - 4.2 [元件庫架構](#42-元件庫架構)
6. [Vue 3 + Tailwind CSS 最佳實踐](#5-vue-3--tailwind-css-最佳實踐)
   - 5.1 [元件命名與結構規範](#51-元件命名與結構規範)
   - 5.2 [Tailwind CSS 自定義配置](#52-tailwind-css-自定義配置)
7. [檢測與驗證](#6-檢測與驗證)
   - 6.1 [視覺回歸測試](#61-視覺回歸測試)
   - 6.2 [無障礙檢測](#62-無障礙檢測)
   - 6.3 [使用性測試清單](#63-使用性測試清單)
7. [性能優化指引](#性能優化指引)
8. [設計協作流程](#設計協作流程)
9. [維護與版本控制](#維護與版本控制)
10. [附錄](#附錄)

---

## 文件概述

本指引適用於大型金融共用平台的前端 UI/UX 開發，涵蓋設計原則、UI 元件規範、UX 流程、設計資產交付等完整內容。

### 專案技術堆疊

- **前端架構**: 微前端 + SPA (Single-Page App---

**第一部分完成**，接下來我將繼續撰寫第二部分：無障礙設計和多語系支援。

### 1.4 無障礙設計（WCAG 2.1 AA 級）

#### 色彩對比度要求

- **正常文字**: 對比度至少 4.5:1
- **大文字** (18pt 以上): 對比度至少 3:1
- **互動元件**: 對比度至少 3:1

```css
/* Tailwind CSS 無障礙色彩配置 */
.text-primary {
  @apply text-gray-900; /* 對比度 21:1 */
}

.text-secondary {
  @apply text-gray-700; /* 對比度 9.2:1 */
}

.bg-interactive {
  @apply bg-blue-600 hover:bg-blue-700 focus:bg-blue-700;
}

.bg-interactive:focus {
  @apply ring-2 ring-blue-500 ring-offset-2;
}
```

#### 鍵盤操作支援

- **Tab 順序**: 邏輯性的焦點移動順序
- **快捷鍵**: 主要功能提供鍵盤快捷鍵
- **焦點指示**: 清晰的焦點視覺回饋

```vue
<template>
  <!-- 無障礙表單範例 -->
  <form @submit.prevent="handleSubmit" class="space-y-6">
    <div>
      <label for="account-number" class="block text-sm font-medium text-gray-700">
        帳戶號碼 <span class="text-red-500" aria-label="必填欄位">*</span>
      </label>
      <input
        id="account-number"
        v-model="accountNumber"
        type="text"
        required
        aria-describedby="account-help account-error"
        class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
        :aria-invalid="hasError"
      />
      <p id="account-help" class="mt-2 text-sm text-gray-500">
        請輸入 12 位數字帳戶號碼
      </p>
      <p id="account-error" v-if="errorMessage" class="mt-2 text-sm text-red-600" role="alert">
        {{ errorMessage }}
      </p>
    </div>
  </form>
</template>
```

#### 螢幕閱讀器支援

- **語義化 HTML**: 使用適當的 HTML 語義標籤
- **ARIA 標籤**: 補充無障礙資訊
- **替代文字**: 圖片提供有意義的 alt 文字

```vue
<template>
  <!-- 無障礙數據表格 -->
  <table role="table" aria-label="帳戶交易記錄">
    <caption class="sr-only">
      最近 10 筆交易記錄，包含日期、摘要、金額和餘額
    </caption>
    <thead>
      <tr>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
          交易日期
        </th>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
          摘要
        </th>
        <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
          金額
        </th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="transaction in transactions" :key="transaction.id">
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
          {{ formatDate(transaction.date) }}
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
          {{ transaction.description }}
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-right">
          <span :class="transaction.amount >= 0 ? 'text-green-600' : 'text-red-600'">
            {{ formatCurrency(transaction.amount) }}
          </span>
        </td>
      </tr>
    </tbody>
  </table>
</template>
```

### 1.5 多語系支援

#### 語言切換機制

```typescript
// i18n 配置
import { createI18n } from 'vue-i18n';

interface Messages {
  'zh-TW': Record<string, any>;
  'en-US': Record<string, any>;
  'ja-JP': Record<string, any>;
}

const messages: Messages = {
  'zh-TW': {
    common: {
      confirm: '確認',
      cancel: '取消',
      save: '儲存',
      delete: '刪除',
      loading: '載入中...'
    },
    account: {
      balance: '帳戶餘額',
      transfer: '轉帳',
      history: '交易記錄'
    }
  },
  'en-US': {
    common: {
      confirm: 'Confirm',
      cancel: 'Cancel',
      save: 'Save',
      delete: 'Delete',
      loading: 'Loading...'
    },
    account: {
      balance: 'Account Balance',
      transfer: 'Transfer',
      history: 'Transaction History'
    }
  }
};

export const i18n = createI18n({
  locale: 'zh-TW',
  fallbackLocale: 'en-US',
  messages
});
```

#### 文字方向支援 (RTL/LTR)

```vue
<template>
  <div :dir="currentLocale.dir" class="app-container">
    <!-- 語言切換器 -->
    <div class="language-selector">
      <select 
        v-model="currentLanguage" 
        @change="changeLanguage"
        class="block w-32 rounded-md border-gray-300"
        :aria-label="$t('common.selectLanguage')"
      >
        <option value="zh-TW">繁體中文</option>
        <option value="en-US">English</option>
        <option value="ar-SA">العربية</option>
      </select>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { useI18n } from 'vue-i18n';

const { locale, t } = useI18n();

const localeConfig = {
  'zh-TW': { dir: 'ltr', name: '繁體中文' },
  'en-US': { dir: 'ltr', name: 'English' },
  'ar-SA': { dir: 'rtl', name: 'العربية' }
};

const currentLocale = computed(() => localeConfig[locale.value]);
</script>

<style>
/* RTL 支援樣式 */
[dir="rtl"] .text-left {
  text-align: right;
}

[dir="rtl"] .text-right {
  text-align: left;
}

[dir="rtl"] .ml-4 {
  margin-left: 0;
  margin-right: 1rem;
}
</style>
```

#### 數字與日期本地化

```typescript
// 本地化格式化工具
export class LocaleFormatter {
  private locale: string;
  
  constructor(locale: string) {
    this.locale = locale;
  }
  
  // 金額格式化
  formatCurrency(amount: number, currency: string = 'TWD'): string {
    const currencyMap = {
      'zh-TW': 'TWD',
      'en-US': 'USD',
      'ja-JP': 'JPY',
      'ko-KR': 'KRW'
    };
    
    return new Intl.NumberFormat(this.locale, {
      style: 'currency',
      currency: currencyMap[this.locale] || currency,
      minimumFractionDigits: currency === 'JPY' ? 0 : 2
    }).format(amount);
  }
  
  // 日期格式化
  formatDate(date: Date, options?: Intl.DateTimeFormatOptions): string {
    const defaultOptions: Intl.DateTimeFormatOptions = {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    };
    
    return new Intl.DateTimeFormat(this.locale, options || defaultOptions).format(date);
  }
  
  // 時間格式化
  formatTime(date: Date): string {
    return new Intl.DateTimeFormat(this.locale, {
      hour: '2-digit',
      minute: '2-digit',
      hour12: this.locale === 'en-US'
    }).format(date);
  }
  
  // 百分比格式化
  formatPercentage(value: number): string {
    return new Intl.NumberFormat(this.locale, {
      style: 'percent',
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    }).format(value);
  }
}
```

#### 進階無障礙設計實作

```vue
<template>
  <!-- 高對比模式切換 -->
  <div class="accessibility-controls fixed top-4 right-4 z-50">
    <button
      @click="toggleHighContrast"
      :aria-pressed="isHighContrast"
      class="p-2 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
      :class="isHighContrast ? 'bg-yellow-400 text-black' : 'bg-white text-gray-700 shadow-md'"
      aria-label="切換高對比模式"
    >
      <EyeIcon class="h-5 w-5" />
    </button>
    
    <!-- 字體大小調整 -->
    <div class="mt-2 flex flex-col space-y-1">
      <button
        @click="increaseFontSize"
        class="p-1 text-xs bg-white rounded shadow-md hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-500"
        aria-label="增大字體"
      >
        A+
      </button>
      <button
        @click="decreaseFontSize"
        class="p-1 text-xs bg-white rounded shadow-md hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-500"
        aria-label="縮小字體"
      >
        A-
      </button>
      <button
        @click="resetFontSize"
        class="p-1 text-xs bg-white rounded shadow-md hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-500"
        aria-label="重設字體大小"
      >
        A
      </button>
    </div>
  </div>
  
  <!-- 跳至主要內容連結 -->
  <a
    href="#main-content"
    class="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 bg-blue-600 text-white px-4 py-2 rounded-md z-50"
  >
    跳至主要內容
  </a>
  
  <!-- 焦點陷阱對話框範例 -->
  <div
    v-if="showModal"
    class="fixed inset-0 z-10 overflow-y-auto"
    role="dialog"
    aria-modal="true"
    :aria-labelledby="modalTitleId"
    @keydown.esc="closeModal"
  >
    <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
      <!-- 背景遮罩 -->
      <div
        class="fixed inset-0 transition-opacity"
        aria-hidden="true"
        @click="closeModal"
      >
        <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
      </div>
      
      <!-- 對話框內容 -->
      <div
        ref="modalContent"
        class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full"
        @keydown="handleModalKeydown"
      >
        <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
          <h3 :id="modalTitleId" class="text-lg leading-6 font-medium text-gray-900 mb-4">
            確認操作
          </h3>
          <p class="text-sm text-gray-500 mb-4">
            您確定要執行此操作嗎？此動作無法復原。
          </p>
          
          <!-- 焦點陷阱內的可互動元素 -->
          <div class="flex justify-end space-x-3">
            <button
              ref="cancelButton"
              @click="closeModal"
              class="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              取消
            </button>
            <button
              ref="confirmButton"
              @click="handleConfirm"
              class="px-4 py-2 text-sm font-medium text-white bg-red-600 border border-transparent rounded-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500"
            >
              確認
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, nextTick, onMounted, onUnmounted } from 'vue';
import { EyeIcon } from '@heroicons/vue/24/outline';

// 無障礙狀態管理
const isHighContrast = ref(false);
const fontSize = ref(16);
const showModal = ref(false);
const modalTitleId = ref(`modal-title-${Math.random().toString(36).substr(2, 9)}`);

// 高對比模式
const toggleHighContrast = () => {
  isHighContrast.value = !isHighContrast.value;
  document.documentElement.classList.toggle('high-contrast', isHighContrast.value);
  
  // 儲存使用者偏好
  localStorage.setItem('high-contrast', isHighContrast.value.toString());
  
  // 通知螢幕閱讀器
  announceToScreenReader(
    isHighContrast.value ? '已開啟高對比模式' : '已關閉高對比模式'
  );
};

// 字體大小調整
const increaseFontSize = () => {
  if (fontSize.value < 24) {
    fontSize.value += 2;
    updateFontSize();
  }
};

const decreaseFontSize = () => {
  if (fontSize.value > 12) {
    fontSize.value -= 2;
    updateFontSize();
  }
};

const resetFontSize = () => {
  fontSize.value = 16;
  updateFontSize();
};

const updateFontSize = () => {
  document.documentElement.style.fontSize = `${fontSize.value}px`;
  localStorage.setItem('font-size', fontSize.value.toString());
  announceToScreenReader(`字體大小已調整為 ${fontSize.value} 像素`);
};

// 螢幕閱讀器公告
const announceToScreenReader = (message: string) => {
  const announcement = document.createElement('div');
  announcement.setAttribute('aria-live', 'polite');
  announcement.setAttribute('aria-atomic', 'true');
  announcement.className = 'sr-only';
  announcement.textContent = message;
  
  document.body.appendChild(announcement);
  
  setTimeout(() => {
    document.body.removeChild(announcement);
  }, 1000);
};

// 焦點陷阱管理
const modalContent = ref<HTMLElement>();
const cancelButton = ref<HTMLButtonElement>();
const confirmButton = ref<HTMLButtonElement>();
const focusableElements: HTMLElement[] = [];
let previousFocusedElement: HTMLElement | null = null;

const openModal = async () => {
  previousFocusedElement = document.activeElement as HTMLElement;
  showModal.value = true;
  
  await nextTick();
  
  // 收集可聚焦元素
  const selector = 'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])';
  focusableElements.splice(0);
  focusableElements.push(
    ...Array.from(modalContent.value?.querySelectorAll(selector) || [])
  );
  
  // 聚焦第一個元素
  if (focusableElements.length > 0) {
    focusableElements[0].focus();
  }
};

const closeModal = () => {
  showModal.value = false;
  // 恢復之前的焦點
  if (previousFocusedElement) {
    previousFocusedElement.focus();
  }
};

const handleModalKeydown = (event: KeyboardEvent) => {
  if (event.key === 'Tab') {
    const currentIndex = focusableElements.indexOf(event.target as HTMLElement);
    
    if (event.shiftKey) {
      // Shift + Tab (向後)
      if (currentIndex <= 0) {
        event.preventDefault();
        focusableElements[focusableElements.length - 1].focus();
      }
    } else {
      // Tab (向前)
      if (currentIndex >= focusableElements.length - 1) {
        event.preventDefault();
        focusableElements[0].focus();
      }
    }
  }
};

const handleConfirm = () => {
  // 處理確認邏輯
  announceToScreenReader('操作已確認');
  closeModal();
};

// 鍵盤快捷鍵
const handleGlobalKeydown = (event: KeyboardEvent) => {
  // Alt + H: 開啟高對比模式
  if (event.altKey && event.key === 'h') {
    event.preventDefault();
    toggleHighContrast();
  }
  
  // Alt + +: 增大字體
  if (event.altKey && event.key === '+') {
    event.preventDefault();
    increaseFontSize();
  }
  
  // Alt + -: 縮小字體
  if (event.altKey && event.key === '-') {
    event.preventDefault();
    decreaseFontSize();
  }
};

// 初始化無障礙設定
onMounted(() => {
  // 載入儲存的偏好設定
  const savedHighContrast = localStorage.getItem('high-contrast');
  if (savedHighContrast === 'true') {
    isHighContrast.value = true;
    document.documentElement.classList.add('high-contrast');
  }
  
  const savedFontSize = localStorage.getItem('font-size');
  if (savedFontSize) {
    fontSize.value = parseInt(savedFontSize);
    document.documentElement.style.fontSize = `${fontSize.value}px`;
  }
  
  // 監聽全域鍵盤事件
  document.addEventListener('keydown', handleGlobalKeydown);
  
  // 檢測用戶偏好的配色方案
  if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    document.documentElement.classList.add('dark-mode');
  }
  
  // 檢測用戶偏好的動畫設定
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.documentElement.classList.add('reduce-motion');
  }
});

onUnmounted(() => {
  document.removeEventListener('keydown', handleGlobalKeydown);
});
</script>

<style>
/* 高對比模式樣式 */
.high-contrast {
  filter: contrast(150%) saturate(200%);
}

.high-contrast button {
  border: 2px solid currentColor !important;
}

.high-contrast a {
  text-decoration: underline !important;
}

/* 減少動畫模式 */
.reduce-motion *,
.reduce-motion *::before,
.reduce-motion *::after {
  animation-duration: 0.01ms !important;
  animation-iteration-count: 1 !important;
  transition-duration: 0.01ms !important;
}

/* 深色模式支援 */
.dark-mode {
  color-scheme: dark;
}

/* 螢幕閱讀器專用隱藏 */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

.sr-only.focus:focus {
  position: static;
  width: auto;
  height: auto;
  padding: inherit;
  margin: inherit;
  overflow: visible;
  clip: auto;
  white-space: normal;
}
</style>
```

#### 多語系內容管理策略

```typescript
// 多語系內容管理
interface TranslationKey {
  key: string;
  context?: string;
  pluralization?: boolean;
  interpolation?: string[];
}

interface TranslationContent {
  [locale: string]: {
    [namespace: string]: {
      [key: string]: string | object;
    };
  };
}

// 翻譯內容結構化管理
export const translationStructure: TranslationContent = {
  'zh-TW': {
    common: {
      // 通用操作
      actions: {
        save: '儲存',
        cancel: '取消',
        confirm: '確認',
        delete: '刪除',
        edit: '編輯',
        add: '新增',
        search: '搜尋',
        filter: '篩選',
        sort: '排序',
        refresh: '重新整理',
        loading: '載入中...',
        noData: '無資料',
        error: '發生錯誤'
      },
      
      // 表單相關
      form: {
        required: '此欄位為必填',
        invalid: '格式不正確',
        tooShort: '長度不足',
        tooLong: '長度過長',
        emailInvalid: '請輸入有效的電子郵件地址',
        phoneInvalid: '請輸入有效的手機號碼',
        passwordMismatch: '密碼不一致'
      },
      
      // 時間相關
      time: {
        just_now: '剛剛',
        minutes_ago: '{count} 分鐘前',
        hours_ago: '{count} 小時前',
        days_ago: '{count} 天前',
        weeks_ago: '{count} 週前',
        months_ago: '{count} 個月前',
        years_ago: '{count} 年前'
      }
    },
    
    // 金融業務相關
    banking: {
      account: {
        balance: '帳戶餘額',
        available: '可用餘額',
        accountNumber: '帳戶號碼',
        accountType: '帳戶類型',
        status: '狀態',
        openDate: '開戶日期',
        lastTransaction: '最近交易'
      },
      
      transaction: {
        transfer: '轉帳',
        deposit: '存款',
        withdrawal: '提款',
        payment: '付款',
        refund: '退款',
        fee: '手續費',
        amount: '金額',
        recipient: '收款人',
        description: '摘要',
        reference: '參考號碼',
        date: '交易日期',
        status: '交易狀態'
      },
      
      status: {
        active: '啟用',
        inactive: '停用',
        pending: '處理中',
        completed: '已完成',
        failed: '失敗',
        cancelled: '已取消',
        expired: '已過期'
      }
    }
  },
  
  'en-US': {
    common: {
      actions: {
        save: 'Save',
        cancel: 'Cancel',
        confirm: 'Confirm',
        delete: 'Delete',
        edit: 'Edit',
        add: 'Add',
        search: 'Search',
        filter: 'Filter',
        sort: 'Sort',
        refresh: 'Refresh',
        loading: 'Loading...',
        noData: 'No Data',
        error: 'Error Occurred'
      },
      
      form: {
        required: 'This field is required',
        invalid: 'Invalid format',
        tooShort: 'Too short',
        tooLong: 'Too long',
        emailInvalid: 'Please enter a valid email address',
        phoneInvalid: 'Please enter a valid phone number',
        passwordMismatch: 'Passwords do not match'
      },
      
      time: {
        just_now: 'Just now',
        minutes_ago: '{count} minutes ago',
        hours_ago: '{count} hours ago',
        days_ago: '{count} days ago',
        weeks_ago: '{count} weeks ago',
        months_ago: '{count} months ago',
        years_ago: '{count} years ago'
      }
    },
    
    banking: {
      account: {
        balance: 'Account Balance',
        available: 'Available Balance',
        accountNumber: 'Account Number',
        accountType: 'Account Type',
        status: 'Status',
        openDate: 'Open Date',
        lastTransaction: 'Last Transaction'
      },
      
      transaction: {
        transfer: 'Transfer',
        deposit: 'Deposit',
        withdrawal: 'Withdrawal',
        payment: 'Payment',
        refund: 'Refund',
        fee: 'Fee',
        amount: 'Amount',
        recipient: 'Recipient',
        description: 'Description',
        reference: 'Reference Number',
        date: 'Transaction Date',
        status: 'Transaction Status'
      },
      
      status: {
        active: 'Active',
        inactive: 'Inactive',
        pending: 'Pending',
        completed: 'Completed',
        failed: 'Failed',
        cancelled: 'Cancelled',
        expired: 'Expired'
      }
    }
  }
};

// 進階翻譯函數
export class I18nManager {
  private currentLocale: string = 'zh-TW';
  private fallbackLocale: string = 'en-US';
  
  // 設定當前語言
  setLocale(locale: string) {
    this.currentLocale = locale;
    document.documentElement.setAttribute('lang', locale);
    
    // 更新頁面方向
    const direction = this.getTextDirection(locale);
    document.documentElement.setAttribute('dir', direction);
    
    // 觸發語言變更事件
    window.dispatchEvent(new CustomEvent('localeChanged', { 
      detail: { locale, direction } 
    }));
  }
  
  // 取得文字方向
  private getTextDirection(locale: string): 'ltr' | 'rtl' {
    const rtlLocales = ['ar', 'he', 'fa', 'ur'];
    return rtlLocales.some(rtl => locale.startsWith(rtl)) ? 'rtl' : 'ltr';
  }
  
  // 翻譯函數
  translate(key: string, options?: {
    interpolation?: Record<string, any>;
    count?: number;
    defaultValue?: string;
  }): string {
    const keys = key.split('.');
    let value = this.getNestedValue(translationStructure[this.currentLocale], keys);
    
    // 如果找不到翻譯，嘗試備用語言
    if (!value) {
      value = this.getNestedValue(translationStructure[this.fallbackLocale], keys);
    }
    
    // 如果還是找不到，返回預設值或 key
    if (!value) {
      return options?.defaultValue || key;
    }
    
    // 處理插值
    if (options?.interpolation) {
      Object.entries(options.interpolation).forEach(([placeholder, replacement]) => {
        value = value.replace(new RegExp(`{${placeholder}}`, 'g'), replacement);
      });
    }
    
    // 處理複數形式
    if (options?.count !== undefined) {
      value = this.handlePluralization(value, options.count);
    }
    
    return value;
  }
  
  // 取得巢狀物件值
  private getNestedValue(obj: any, keys: string[]): string | null {
    return keys.reduce((current, key) => current?.[key], obj) || null;
  }
  
  // 處理複數形式
  private handlePluralization(value: string, count: number): string {
    // 簡化的複數處理，實際應用中可能需要更複雜的邏輯
    if (this.currentLocale === 'en-US') {
      if (count === 1) {
        return value.replace(/\{count\}/, count.toString());
      } else {
        // 處理英文複數規則
        return value.replace(/\{count\}/, count.toString());
      }
    }
    
    return value.replace(/\{count\}/, count.toString());
  }
  
  // 格式化相對時間
  formatRelativeTime(date: Date): string {
    const now = new Date();
    const diffInSeconds = Math.floor((now.getTime() - date.getTime()) / 1000);
    
    if (diffInSeconds < 60) {
      return this.translate('common.time.just_now');
    } else if (diffInSeconds < 3600) {
      const minutes = Math.floor(diffInSeconds / 60);
      return this.translate('common.time.minutes_ago', { 
        interpolation: { count: minutes.toString() } 
      });
    } else if (diffInSeconds < 86400) {
      const hours = Math.floor(diffInSeconds / 3600);
      return this.translate('common.time.hours_ago', { 
        interpolation: { count: hours.toString() } 
      });
    } else if (diffInSeconds < 604800) {
      const days = Math.floor(diffInSeconds / 86400);
      return this.translate('common.time.days_ago', { 
        interpolation: { count: days.toString() } 
      });
    } else if (diffInSeconds < 2419200) {
      const weeks = Math.floor(diffInSeconds / 604800);
      return this.translate('common.time.weeks_ago', { 
        interpolation: { count: weeks.toString() } 
      });
    } else if (diffInSeconds < 29030400) {
      const months = Math.floor(diffInSeconds / 2419200);
      return this.translate('common.time.months_ago', { 
        interpolation: { count: months.toString() } 
      });
    } else {
      const years = Math.floor(diffInSeconds / 29030400);
      return this.translate('common.time.years_ago', { 
        interpolation: { count: years.toString() } 
      });
    }
  }
}

// 全域 i18n 實例
export const i18nManager = new I18nManager();

// Vue 組合函數
export function useI18n() {
  const t = (key: string, options?: any) => i18nManager.translate(key, options);
  const setLocale = (locale: string) => i18nManager.setLocale(locale);
  const formatRelativeTime = (date: Date) => i18nManager.formatRelativeTime(date);
  
  return {
    t,
    setLocale,
    formatRelativeTime
  };
}
```

---

**無障礙設計和多語系支援擴充完成**，接下來我將繼續撰寫第三部分：UI 元件規範。

## 2. UI 元件規範

### 2.1 樣式系統 (Design System)

#### 字體系統

```css
/* 字體階層定義 */
:root {
  /* Primary Font Family */
  --font-primary: 'Noto Sans TC', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', Consolas, monospace;
  
  /* Font Sizes */
  --text-xs: 0.75rem;    /* 12px */
  --text-sm: 0.875rem;   /* 14px */
  --text-base: 1rem;     /* 16px */
  --text-lg: 1.125rem;   /* 18px */
  --text-xl: 1.25rem;    /* 20px */
  --text-2xl: 1.5rem;    /* 24px */
  --text-3xl: 1.875rem;  /* 30px */
  --text-4xl: 2.25rem;   /* 36px */
  
  /* Line Heights */
  --leading-tight: 1.25;
  --leading-normal: 1.5;
  --leading-relaxed: 1.75;
}
```

```typescript
// Tailwind CSS 字體配置
export const fontConfig = {
  fontFamily: {
    'sans': ['Noto Sans TC', 'system-ui', 'sans-serif'],
    'mono': ['JetBrains Mono', 'Fira Code', 'monospace']
  },
  fontSize: {
    'xs': ['0.75rem', { lineHeight: '1rem' }],
    'sm': ['0.875rem', { lineHeight: '1.25rem' }],
    'base': ['1rem', { lineHeight: '1.5rem' }],
    'lg': ['1.125rem', { lineHeight: '1.75rem' }],
    'xl': ['1.25rem', { lineHeight: '1.75rem' }],
    '2xl': ['1.5rem', { lineHeight: '2rem' }],
    '3xl': ['1.875rem', { lineHeight: '2.25rem' }],
    '4xl': ['2.25rem', { lineHeight: '2.5rem' }]
  }
};
```

#### 色彩系統

```css
/* 色彩標記系統 */
:root {
  /* Primary Colors - 主品牌色 */
  --color-primary-50: #eff6ff;
  --color-primary-100: #dbeafe;
  --color-primary-500: #3b82f6;
  --color-primary-600: #2563eb;
  --color-primary-700: #1d4ed8;
  --color-primary-900: #1e3a8a;
  
  /* Semantic Colors - 語義色彩 */
  --color-success: #10b981;
  --color-warning: #f59e0b;
  --color-danger: #ef4444;
  --color-info: #3b82f6;
  
  /* Neutral Colors - 中性色 */
  --color-gray-50: #f9fafb;
  --color-gray-100: #f3f4f6;
  --color-gray-500: #6b7280;
  --color-gray-700: #374151;
  --color-gray-900: #111827;
  
  /* Financial Colors - 金融專用色 */
  --color-profit: #10b981;      /* 獲利綠 */
  --color-loss: #ef4444;        /* 虧損紅 */
  --color-neutral: #6b7280;     /* 中性灰 */
  --color-pending: #f59e0b;     /* 待處理橙 */
}
```

#### 間距系統

```css
/* 間距標記系統 */
:root {
  --spacing-0: 0;
  --spacing-1: 0.25rem;   /* 4px */
  --spacing-2: 0.5rem;    /* 8px */
  --spacing-3: 0.75rem;   /* 12px */
  --spacing-4: 1rem;      /* 16px */
  --spacing-5: 1.25rem;   /* 20px */
  --spacing-6: 1.5rem;    /* 24px */
  --spacing-8: 2rem;      /* 32px */
  --spacing-12: 3rem;     /* 48px */
  --spacing-16: 4rem;     /* 64px */
  --spacing-20: 5rem;     /* 80px */
}
```

### 2.2 響應式設計規範

#### 斷點系統

```typescript
// 響應式斷點定義
export const breakpoints = {
  'sm': '640px',    // 手機橫向
  'md': '768px',    // 平板直向
  'lg': '1024px',   // 平板橫向/小筆電
  'xl': '1280px',   // 桌上型電腦
  '2xl': '1536px'   // 大型螢幕
} as const;

// Tailwind CSS 斷點配置
export const screens = breakpoints;
```

#### 響應式元件範例

```vue
<template>
  <!-- 響應式卡片佈局 -->
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-6">
    <div v-for="account in accounts" :key="account.id" 
         class="bg-white rounded-lg shadow-md p-4 md:p-6 hover:shadow-lg transition-shadow">
      
      <!-- 帳戶資訊區塊 -->
      <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-4">
        <h3 class="text-lg font-semibold text-gray-900 mb-2 sm:mb-0">
          {{ account.name }}
        </h3>
        <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium"
              :class="getAccountStatusClass(account.status)">
          {{ account.status }}
        </span>
      </div>
      
      <!-- 餘額顯示 - 響應式字體大小 */
      <div class="mb-4">
        <p class="text-sm text-gray-500 mb-1">可用餘額</p>
        <p class="text-2xl md:text-3xl font-bold text-gray-900">
          {{ formatCurrency(account.balance) }}
        </p>
      </div>
      
      <!-- 操作按鈕 - 響應式排列 -->
      <div class="flex flex-col sm:flex-row gap-2 sm:gap-3">
        <button class="flex-1 bg-blue-600 text-white py-2 px-4 rounded-md text-sm font-medium hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
          轉帳
        </button>
        <button class="flex-1 bg-gray-100 text-gray-700 py-2 px-4 rounded-md text-sm font-medium hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-2">
          查詢
        </button>
      </div>
    </div>
  </div>
</template>
```

### 2.3 常用元件設計

#### 按鈕元件

```vue
<template>
  <!-- 按鈕元件 -->
  <component
    :is="tag"
    :class="buttonClasses"
    :disabled="disabled || loading"
    v-bind="$attrs"
    @click="handleClick"
  >
    <!-- 載入圖示 -->
    <svg v-if="loading" class="animate-spin -ml-1 mr-3 h-5 w-5" fill="none" viewBox="0 0 24 24">
      <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
      <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
    </svg>
    
    <!-- 前置圖示 -->
    <component v-if="iconLeft && !loading" :is="iconLeft" class="w-5 h-5 mr-2" />
    
    <!-- 按鈕文字 -->
    <span>{{ loading ? loadingText : text }}</span>
    
    <!-- 後置圖示 -->
    <component v-if="iconRight && !loading" :is="iconRight" class="w-5 h-5 ml-2" />
  </component>
</template>

<script setup lang="ts">
import { computed } from 'vue';

interface Props {
  variant?: 'primary' | 'secondary' | 'danger' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  text: string;
  loading?: boolean;
  loadingText?: string;
  disabled?: boolean;
  iconLeft?: any;
  iconRight?: any;
  tag?: 'button' | 'a';
}

const props = withDefaults(defineProps<Props>(), {
  variant: 'primary',
  size: 'md',
  loading: false,
  loadingText: '處理中...',
  disabled: false,
  tag: 'button'
});

const emit = defineEmits<{
  click: [event: Event];
}>();

const buttonClasses = computed(() => {
  const base = 'inline-flex items-center justify-center font-medium rounded-md focus:outline-none focus:ring-2 focus:ring-offset-2 transition-colors duration-200 disabled:opacity-50 disabled:cursor-not-allowed';
  
  const variants = {
    primary: 'bg-blue-600 text-white hover:bg-blue-700 focus:ring-blue-500',
    secondary: 'bg-gray-100 text-gray-900 hover:bg-gray-200 focus:ring-gray-500',
    danger: 'bg-red-600 text-white hover:bg-red-700 focus:ring-red-500',
    ghost: 'text-blue-600 hover:bg-blue-50 focus:ring-blue-500'
  };
  
  const sizes = {
    sm: 'px-3 py-2 text-sm',
    md: 'px-4 py-2 text-sm',
    lg: 'px-6 py-3 text-base'
  };
  
  return `${base} ${variants[props.variant]} ${sizes[props.size]}`;
});

const handleClick = (event: Event) => {
  if (!props.disabled && !props.loading) {
    emit('click', event);
  }
};
</script>
```

#### 表單輸入元件

```vue
<template>
  <div class="form-field">
    <!-- 標籤 -->
    <label v-if="label" :for="inputId" class="block text-sm font-medium text-gray-700 mb-1">
      {{ label }}
      <span v-if="required" class="text-red-500 ml-1" aria-label="必填欄位">*</span>
    </label>
    
    <!-- 輸入框容器 -->
    <div class="relative">
      <!-- 前置圖示 -->
      <div v-if="iconLeft" class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
        <component :is="iconLeft" class="h-5 w-5 text-gray-400" />
      </div>
      
      <!-- 輸入框 -->
      <input
        :id="inputId"
        :type="inputType"
        :value="modelValue"
        :placeholder="placeholder"
        :required="required"
        :disabled="disabled"
        :readonly="readonly"
        :maxlength="maxlength"
        :aria-invalid="hasError"
        :aria-describedby="helpTextId"
        :class="inputClasses"
        @input="handleInput"
        @blur="handleBlur"
        @focus="handleFocus"
      />
      
      <!-- 後置圖示或清除按鈕 -->
      <div v-if="iconRight || clearable" class="absolute inset-y-0 right-0 pr-3 flex items-center">
        <button
          v-if="clearable && modelValue"
          @click="clearInput"
          class="text-gray-400 hover:text-gray-600 focus:outline-none"
          type="button"
        >
          <XMarkIcon class="h-5 w-5" />
        </button>
        <component v-else-if="iconRight" :is="iconRight" class="h-5 w-5 text-gray-400" />
      </div>
    </div>
    
    <!-- 說明文字 -->
    <p v-if="helpText" :id="helpTextId" class="mt-2 text-sm text-gray-500">
      {{ helpText }}
    </p>
    
    <!-- 錯誤訊息 -->
    <p v-if="errorMessage" class="mt-2 text-sm text-red-600" role="alert">
      {{ errorMessage }}
    </p>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue';
import { XMarkIcon } from '@heroicons/vue/24/outline';

interface Props {
  modelValue: string | number;
  label?: string;
  placeholder?: string;
  type?: 'text' | 'email' | 'password' | 'number' | 'tel';
  required?: boolean;
  disabled?: boolean;
  readonly?: boolean;
  maxlength?: number;
  helpText?: string;
  errorMessage?: string;
  iconLeft?: any;
  iconRight?: any;
  clearable?: boolean;
}

const props = withDefaults(defineProps<Props>(), {
  type: 'text',
  required: false,
  disabled: false,
  readonly: false,
  clearable: false
});

const emit = defineEmits<{
  'update:modelValue': [value: string | number];
  blur: [event: FocusEvent];
  focus: [event: FocusEvent];
}>();

const inputId = ref(`input-${Math.random().toString(36).substr(2, 9)}`);
const helpTextId = computed(() => `${inputId.value}-help`);
const hasError = computed(() => !!props.errorMessage);

const inputType = computed(() => {
  if (props.type === 'password') {
    return showPassword.value ? 'text' : 'password';
  }
  return props.type;
});

const inputClasses = computed(() => {
  const base = 'block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm disabled:bg-gray-50 disabled:text-gray-500';
  const withIcon = props.iconLeft ? 'pl-10' : '';
  const withRightIcon = (props.iconRight || props.clearable) ? 'pr-10' : '';
  const errorState = hasError.value ? 'border-red-300 text-red-900 placeholder-red-300 focus:border-red-500 focus:ring-red-500' : '';
  
  return `${base} ${withIcon} ${withRightIcon} ${errorState}`;
});

const showPassword = ref(false);

const handleInput = (event: Event) => {
  const target = event.target as HTMLInputElement;
  emit('update:modelValue', target.value);
};

const handleBlur = (event: FocusEvent) => {
  emit('blur', event);
};

const handleFocus = (event: FocusEvent) => {
  emit('focus', event);
};

const clearInput = () => {
  emit('update:modelValue', '');
};
</script>
```

---

**第三部分完成**，接下來我將繼續撰寫第四部分：UX 流程規範。

## 3. UX 流程規範

### 3.1 表單驗證與錯誤回饋

#### 驗證時機

- **即時驗證**: 使用者離開欄位時進行驗證
- **提交驗證**: 表單提交時進行完整驗證
- **格式驗證**: 輸入過程中的格式提示

```typescript
// 表單驗證規則定義
interface ValidationRule {
  required?: boolean;
  pattern?: RegExp;
  min?: number;
  max?: number;
  custom?: (value: any) => string | null;
  message: string;
}

interface FieldValidation {
  rules: ValidationRule[];
  validateOn: 'blur' | 'input' | 'submit';
}

// 金融表單驗證規則
export const bankingValidationRules = {
  accountNumber: {
    rules: [
      { required: true, message: '請輸入帳戶號碼' },
      { pattern: /^\d{12}$/, message: '帳戶號碼必須為 12 位數字' }
    ],
    validateOn: 'blur'
  },
  
  transferAmount: {
    rules: [
      { required: true, message: '請輸入轉帳金額' },
      { min: 1, message: '轉帳金額必須大於 0' },
      { max: 1000000, message: '單筆轉帳金額不得超過 100 萬' },
      { 
        custom: (value: number) => {
          return value % 1 !== 0 ? '轉帳金額必須為整數' : null;
        },
        message: ''
      }
    ],
    validateOn: 'blur'
  },
  
  phone: {
    rules: [
      { required: true, message: '請輸入手機號碼' },
      { pattern: /^09\d{8}$/, message: '請輸入正確的手機號碼格式' }
    ],
    validateOn: 'blur'
  }
};
```

#### 錯誤訊息設計

```vue
<template>
  <!-- 表單驗證範例 -->
  <form @submit.prevent="handleSubmit" class="space-y-6">
    <!-- 轉帳金額欄位 -->
    <div class="form-group">
      <label for="amount" class="block text-sm font-medium text-gray-700">
        轉帳金額 <span class="text-red-500">*</span>
      </label>
      
      <div class="mt-1 relative">
        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
          <span class="text-gray-500 sm:text-sm">NT$</span>
        </div>
        
        <input
          id="amount"
          v-model="form.amount"
          type="number"
          step="1"
          min="1"
          :class="[
            'block w-full pl-12 pr-3 py-2 border rounded-md shadow-sm focus:outline-none focus:ring-1 sm:text-sm',
            errors.amount
              ? 'border-red-300 text-red-900 placeholder-red-300 focus:border-red-500 focus:ring-red-500'
              : 'border-gray-300 focus:border-blue-500 focus:ring-blue-500'
          ]"
          placeholder="0"
          @blur="validateField('amount')"
          @input="clearFieldError('amount')"
        />
      </div>
      
      <!-- 錯誤訊息 -->
      <div v-if="errors.amount" class="mt-2 flex items-center">
        <ExclamationCircleIcon class="h-5 w-5 text-red-500 mr-2" />
        <p class="text-sm text-red-600">{{ errors.amount }}</p>
      </div>
      
      <!-- 說明文字 -->
      <p v-else class="mt-2 text-sm text-gray-500">
        單筆轉帳限額 NT$ 1,000,000
      </p>
    </div>
    
    <!-- 收款帳號欄位 -->
    <div class="form-group">
      <label for="recipient" class="block text-sm font-medium text-gray-700">
        收款帳號 <span class="text-red-500">*</span>
      </label>
      
      <div class="mt-1">
        <input
          id="recipient"
          v-model="form.recipientAccount"
          type="text"
          maxlength="12"
          :class="[
            'block w-full px-3 py-2 border rounded-md shadow-sm focus:outline-none focus:ring-1 sm:text-sm',
            errors.recipientAccount
              ? 'border-red-300 text-red-900 focus:border-red-500 focus:ring-red-500'
              : 'border-gray-300 focus:border-blue-500 focus:ring-blue-500'
          ]"
          placeholder="請輸入 12 位數帳號"
          @blur="validateField('recipientAccount')"
          @input="formatAccountNumber"
        />
      </div>
      
      <!-- 動態驗證狀態 -->
      <div class="mt-2 flex items-center" v-if="validationStatus.recipientAccount">
        <CheckCircleIcon v-if="validationStatus.recipientAccount === 'valid'" 
                        class="h-5 w-5 text-green-500 mr-2" />
        <ExclamationCircleIcon v-else-if="validationStatus.recipientAccount === 'invalid'" 
                              class="h-5 w-5 text-red-500 mr-2" />
        <div v-else class="animate-spin h-5 w-5 border-2 border-blue-500 border-t-transparent rounded-full mr-2"></div>
        
        <p :class="[
          'text-sm',
          validationStatus.recipientAccount === 'valid' ? 'text-green-600' : 
          validationStatus.recipientAccount === 'invalid' ? 'text-red-600' : 'text-gray-500'
        ]">
          {{ getValidationMessage('recipientAccount') }}
        </p>
      </div>
    </div>
    
    <!-- 提交按鈕 -->
    <div class="flex justify-end space-x-3">
      <button
        type="button"
        class="px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
        @click="resetForm"
      >
        重設
      </button>
      
      <button
        type="submit"
        :disabled="!isFormValid || loading"
        class="px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed"
      >
        <div v-if="loading" class="flex items-center">
          <div class="animate-spin -ml-1 mr-3 h-5 w-5 border-2 border-white border-t-transparent rounded-full"></div>
          處理中...
        </div>
        <span v-else>確認轉帳</span>
      </button>
    </div>
  </form>
</template>
```

### 3.2 使用者引導 (Onboarding)

#### 首次使用引導

```vue
<template>
  <!-- 使用者引導元件 -->
  <div v-if="showOnboarding" class="fixed inset-0 z-50 overflow-hidden">
    <!-- 遮罩 -->
    <div class="absolute inset-0 bg-black bg-opacity-50"></div>
    
    <!-- 引導內容 -->
    <div class="relative h-full flex items-center justify-center p-4">
      <div class="bg-white rounded-lg shadow-xl max-w-md w-full p-6">
        <!-- 步驟指示器 -->
        <div class="flex justify-center mb-6">
          <div class="flex space-x-2">
            <div v-for="(step, index) in onboardingSteps" 
                 :key="index"
                 :class="[
                   'w-3 h-3 rounded-full',
                   index <= currentStep ? 'bg-blue-500' : 'bg-gray-300'
                 ]">
            </div>
          </div>
        </div>
        
        <!-- 當前步驟內容 -->
        <div class="text-center">
          <div class="mb-4">
            <component :is="currentStepData.icon" class="w-16 h-16 mx-auto text-blue-500" />
          </div>
          
          <h3 class="text-lg font-semibold text-gray-900 mb-2">
            {{ currentStepData.title }}
          </h3>
          
          <p class="text-gray-600 mb-6">
            {{ currentStepData.description }}
          </p>
          
          <!-- 操作按鈕 -->
          <div class="flex justify-between">
            <button
              v-if="currentStep > 0"
              @click="previousStep"
              class="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 rounded-md hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-gray-500"
            >
              上一步
            </button>
            
            <div v-else></div>
            
            <button
              @click="nextStep"
              class="px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              {{ isLastStep ? '開始使用' : '下一步' }}
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { 
  ShieldCheckIcon, 
  CreditCardIcon, 
  ChartBarIcon, 
  BellIcon 
} from '@heroicons/vue/24/outline';

interface OnboardingStep {
  icon: any;
  title: string;
  description: string;
}

const onboardingSteps: OnboardingStep[] = [
  {
    icon: ShieldCheckIcon,
    title: '安全保護',
    description: '我們使用銀行級加密技術保護您的資料安全，請放心使用。'
  },
  {
    icon: CreditCardIcon,
    title: '多元服務',
    description: '提供轉帳、查詢、投資等完整金融服務，滿足您的需求。'
  },
  {
    icon: ChartBarIcon,
    title: '智能分析',
    description: '個人化財務分析，幫助您更好地管理資產配置。'
  },
  {
    icon: BellIcon,
    title: '即時通知',
    description: '重要交易即時推播通知，掌握帳戶動態。'
  }
];

const showOnboarding = ref(true);
const currentStep = ref(0);

const currentStepData = computed(() => onboardingSteps[currentStep.value]);
const isLastStep = computed(() => currentStep.value === onboardingSteps.length - 1);

const nextStep = () => {
  if (isLastStep.value) {
    finishOnboarding();
  } else {
    currentStep.value++;
  }
};

const previousStep = () => {
  if (currentStep.value > 0) {
    currentStep.value--;
  }
};

const finishOnboarding = () => {
  showOnboarding.value = false;
  // 儲存使用者已完成引導的狀態
  localStorage.setItem('onboarding-completed', 'true');
};
</script>
```

### 3.3 搜尋、篩選與排序互動設計

#### 智能搜尋元件

```vue
<template>
  <div class="search-container">
    <!-- 搜尋輸入框 -->
    <div class="relative">
      <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
        <MagnifyingGlassIcon class="h-5 w-5 text-gray-400" />
      </div>
      
      <input
        v-model="searchQuery"
        type="text"
        class="block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-md leading-5 bg-white placeholder-gray-500 focus:outline-none focus:placeholder-gray-400 focus:ring-1 focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
        placeholder="搜尋交易記錄、收款人..."
        @input="handleSearch"
        @keydown.enter="performSearch"
      />
      
      <!-- 清除搜尋 -->
      <button
        v-if="searchQuery"
        @click="clearSearch"
        class="absolute inset-y-0 right-0 pr-3 flex items-center"
      >
        <XMarkIcon class="h-5 w-5 text-gray-400 hover:text-gray-600" />
      </button>
    </div>
    
    <!-- 搜尋建議 -->
    <div v-if="showSuggestions && suggestions.length > 0" 
         class="absolute z-10 mt-1 w-full bg-white shadow-lg max-h-60 rounded-md py-1 text-base ring-1 ring-black ring-opacity-5 overflow-auto focus:outline-none sm:text-sm">
      
      <div
        v-for="(suggestion, index) in suggestions"
        :key="index"
        @click="selectSuggestion(suggestion)"
        class="cursor-pointer select-none relative py-2 pl-3 pr-9 hover:bg-gray-50"
      >
        <div class="flex items-center">
          <ClockIcon class="h-4 w-4 text-gray-400 mr-2" />
          <span class="font-normal block truncate">{{ suggestion.text }}</span>
        </div>
      </div>
    </div>
    
    <!-- 篩選器 -->
    <div class="mt-4 flex flex-wrap gap-2">
      <!-- 日期範圍篩選 -->
      <div class="relative">
        <button
          @click="toggleDateFilter"
          class="inline-flex items-center px-3 py-2 border border-gray-300 shadow-sm text-sm leading-4 font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          <CalendarIcon class="h-4 w-4 mr-2" />
          日期範圍
          <ChevronDownIcon class="ml-2 h-4 w-4" />
        </button>
        
        <!-- 日期篩選下拉選單 -->
        <div v-if="showDateFilter" class="absolute z-10 mt-2 w-64 bg-white rounded-md shadow-lg ring-1 ring-black ring-opacity-5">
          <div class="p-4">
            <div class="space-y-4">
              <div>
                <label class="block text-sm font-medium text-gray-700">開始日期</label>
                <input
                  v-model="dateRange.start"
                  type="date"
                  class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">結束日期</label>
                <input
                  v-model="dateRange.end"
                  type="date"
                  class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                />
              </div>
              <div class="flex justify-end space-x-2">
                <button
                  @click="clearDateFilter"
                  class="px-3 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50"
                >
                  清除
                </button>
                <button
                  @click="applyDateFilter"
                  class="px-3 py-2 text-sm font-medium text-white bg-blue-600 border border-transparent rounded-md hover:bg-blue-700"
                >
                  套用
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- 金額範圍篩選 -->
      <div class="relative">
        <button
          @click="toggleAmountFilter"
          class="inline-flex items-center px-3 py-2 border border-gray-300 shadow-sm text-sm leading-4 font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          <CurrencyDollarIcon class="h-4 w-4 mr-2" />
          金額範圍
          <ChevronDownIcon class="ml-2 h-4 w-4" />
        </button>
      </div>
      
      <!-- 交易類型篩選 -->
      <div class="relative">
        <select
          v-model="selectedTransactionType"
          class="appearance-none bg-white border border-gray-300 rounded-md px-3 py-2 pr-8 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
        >
          <option value="">所有類型</option>
          <option value="transfer">轉帳</option>
          <option value="deposit">存款</option>
          <option value="withdrawal">提款</option>
          <option value="payment">付款</option>
        </select>
      </div>
    </div>
    
    <!-- 排序選項 -->
    <div class="mt-4 flex justify-between items-center">
      <div class="text-sm text-gray-700">
        找到 {{ totalResults }} 筆結果
      </div>
      
      <div class="flex items-center space-x-2">
        <span class="text-sm text-gray-700">排序:</span>
        <select
          v-model="sortBy"
          class="text-sm border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
        >
          <option value="date-desc">日期 (新到舊)</option>
          <option value="date-asc">日期 (舊到新)</option>
          <option value="amount-desc">金額 (高到低)</option>
          <option value="amount-asc">金額 (低到高)</option>
        </select>
      </div>
    </div>
  </div>
</template>
```

---

**第四部分完成**，現在讓我繼續撰寫最後幾個部分。

### 3.4 資料載入與狀態設計

#### Loading 狀態設計

```vue
<template>
  <!-- 全頁載入狀態 -->
  <div v-if="isFullPageLoading" class="fixed inset-0 bg-white bg-opacity-90 flex items-center justify-center z-50">
    <div class="text-center">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mb-4"></div>
      <p class="text-gray-600">載入中，請稍候...</p>
    </div>
  </div>
  
  <!-- 區塊載入狀態 -->
  <div class="space-y-6">
    <!-- 帳戶卡片載入骨架 -->
    <div v-if="isLoadingAccounts" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="n in 6" :key="n" class="bg-white rounded-lg border border-gray-200 p-6">
        <div class="animate-pulse">
          <div class="flex justify-between items-start mb-4">
            <div class="h-4 bg-gray-200 rounded w-24"></div>
            <div class="h-6 bg-gray-200 rounded-full w-16"></div>
          </div>
          <div class="space-y-2">
            <div class="h-3 bg-gray-200 rounded w-20"></div>
            <div class="h-8 bg-gray-200 rounded w-32"></div>
          </div>
          <div class="flex gap-2 mt-4">
            <div class="h-8 bg-gray-200 rounded flex-1"></div>
            <div class="h-8 bg-gray-200 rounded flex-1"></div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- 表格載入狀態 -->
    <div v-else-if="isLoadingTransactions" class="bg-white shadow overflow-hidden sm:rounded-md">
      <div class="animate-pulse">
        <div class="px-4 py-5 sm:p-6">
          <div class="space-y-4">
            <div v-for="n in 8" :key="n" class="flex items-center space-x-4">
              <div class="h-4 bg-gray-200 rounded w-20"></div>
              <div class="h-4 bg-gray-200 rounded flex-1"></div>
              <div class="h-4 bg-gray-200 rounded w-24"></div>
              <div class="h-4 bg-gray-200 rounded w-20"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
```

#### Empty 狀態設計

```vue
<template>
  <!-- 無資料狀態 -->
  <div class="text-center py-12">
    <component :is="emptyState.icon" class="mx-auto h-24 w-24 text-gray-400 mb-4" />
    <h3 class="text-lg font-medium text-gray-900 mb-2">{{ emptyState.title }}</h3>
    <p class="text-gray-500 mb-6 max-w-sm mx-auto">{{ emptyState.description }}</p>
    
    <div class="flex justify-center space-x-3">
      <button
        v-if="emptyState.primaryAction"
        @click="emptyState.primaryAction.handler"
        class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
      >
        <component :is="emptyState.primaryAction.icon" class="mr-2 h-4 w-4" />
        {{ emptyState.primaryAction.text }}
      </button>
      
      <button
        v-if="emptyState.secondaryAction"
        @click="emptyState.secondaryAction.handler"
        class="inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
      >
        {{ emptyState.secondaryAction.text }}
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { 
  CreditCardIcon, 
  PlusIcon, 
  ArrowPathIcon,
  MagnifyingGlassIcon,
  ExclamationTriangleIcon 
} from '@heroicons/vue/24/outline';

// 不同情境的空狀態配置
const emptyStates = {
  noAccounts: {
    icon: CreditCardIcon,
    title: '尚無帳戶資料',
    description: '您目前沒有任何帳戶，請新增帳戶後再試。',
    primaryAction: {
      icon: PlusIcon,
      text: '新增帳戶',
      handler: () => router.push('/accounts/add')
    }
  },
  
  noTransactions: {
    icon: MagnifyingGlassIcon,
    title: '查無交易記錄',
    description: '在指定的時間範圍內沒有找到任何交易記錄。',
    secondaryAction: {
      text: '調整搜尋條件',
      handler: () => resetSearchFilters()
    }
  },
  
  networkError: {
    icon: ExclamationTriangleIcon,
    title: '載入失敗',
    description: '網路連線發生問題，請檢查網路狀態後重試。',
    primaryAction: {
      icon: ArrowPathIcon,
      text: '重新載入',
      handler: () => retryRequest()
    }
  }
};
</script>
```

#### Error 狀態設計

```vue
<template>
  <!-- 錯誤狀態元件 -->
  <div class="rounded-md p-4" :class="errorClasses">
    <div class="flex">
      <div class="flex-shrink-0">
        <component :is="errorIcon" class="h-5 w-5" :class="iconClasses" />
      </div>
      
      <div class="ml-3 flex-1">
        <h3 class="text-sm font-medium" :class="titleClasses">
          {{ errorTitle }}
        </h3>
        
        <div class="mt-2 text-sm" :class="messageClasses">
          <p>{{ errorMessage }}</p>
          
          <!-- 詳細錯誤資訊 (開發模式) -->
          <details v-if="isDevelopment && errorDetails" class="mt-3">
            <summary class="cursor-pointer font-medium">技術詳情</summary>
            <pre class="mt-2 text-xs bg-gray-50 p-2 rounded overflow-auto">{{ errorDetails }}</pre>
          </details>
        </div>
        
        <!-- 錯誤操作按鈕 -->
        <div class="mt-4 flex space-x-3">
          <button
            v-if="showRetry"
            @click="handleRetry"
            type="button"
            class="text-sm font-medium underline hover:no-underline focus:outline-none"
            :class="actionClasses"
          >
            重新嘗試
          </button>
          
          <button
            v-if="showReport"
            @click="reportError"
            type="button"
            class="text-sm font-medium underline hover:no-underline focus:outline-none"
            :class="actionClasses"
          >
            回報問題
          </button>
          
          <button
            v-if="showDismiss"
            @click="dismissError"
            type="button"
            class="text-sm font-medium underline hover:no-underline focus:outline-none"
            :class="actionClasses"
          >
            忽略
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { 
  ExclamationTriangleIcon, 
  XCircleIcon, 
  InformationCircleIcon 
} from '@heroicons/vue/20/solid';

interface Props {
  type?: 'error' | 'warning' | 'info';
  title?: string;
  message: string;
  details?: string;
  showRetry?: boolean;
  showReport?: boolean;
  showDismiss?: boolean;
}

const props = withDefaults(defineProps<Props>(), {
  type: 'error',
  showRetry: true,
  showReport: false,
  showDismiss: true
});

const emit = defineEmits<{
  retry: [];
  report: [];
  dismiss: [];
}>();

const errorConfig = {
  error: {
    icon: XCircleIcon,
    bgClass: 'bg-red-50',
    iconClass: 'text-red-400',
    titleClass: 'text-red-800',
    messageClass: 'text-red-700',
    actionClass: 'text-red-600 hover:text-red-500'
  },
  warning: {
    icon: ExclamationTriangleIcon,
    bgClass: 'bg-yellow-50',
    iconClass: 'text-yellow-400',
    titleClass: 'text-yellow-800',
    messageClass: 'text-yellow-700',
    actionClass: 'text-yellow-600 hover:text-yellow-500'
  },
  info: {
    icon: InformationCircleIcon,
    bgClass: 'bg-blue-50',
    iconClass: 'text-blue-400',
    titleClass: 'text-blue-800',
    messageClass: 'text-blue-700',
    actionClass: 'text-blue-600 hover:text-blue-500'
  }
};

const config = computed(() => errorConfig[props.type]);
const errorClasses = computed(() => config.value.bgClass);
const errorIcon = computed(() => config.value.icon);
const iconClasses = computed(() => config.value.iconClass);
const titleClasses = computed(() => config.value.titleClass);
const messageClasses = computed(() => config.value.messageClass);
const actionClasses = computed(() => config.value.actionClass);

const errorTitle = computed(() => {
  if (props.title) return props.title;
  
  const defaultTitles = {
    error: '發生錯誤',
    warning: '注意事項',
    info: '資訊通知'
  };
  
  return defaultTitles[props.type];
});

const errorMessage = computed(() => props.message);
const errorDetails = computed(() => props.details);
const isDevelopment = computed(() => process.env.NODE_ENV === 'development');

const handleRetry = () => emit('retry');
const reportError = () => emit('report');
const dismissError = () => emit('dismiss');
</script>
```

---

現在讓我完成最後的章節。

## 4. 設計資產與交付

### 4.1 設計 Token 系統

```javascript
// design-tokens.js - 設計標記定義
export const designTokens = {
  // 色彩標記
  colors: {
    primary: {
      50: '#eff6ff',
      100: '#dbeafe',
      500: '#3b82f6',
      600: '#2563eb',
      700: '#1d4ed8',
      900: '#1e3a8a'
    },
    semantic: {
      success: '#10b981',
      warning: '#f59e0b',
      danger: '#ef4444',
      info: '#3b82f6'
    },
    financial: {
      profit: '#10b981',
      loss: '#ef4444',
      neutral: '#6b7280',
      pending: '#f59e0b'
    }
  },
  
  // 字體標記
  typography: {
    fontFamily: {
      sans: ['Noto Sans TC', 'system-ui', 'sans-serif'],
      mono: ['JetBrains Mono', 'monospace']
    },
    fontSize: {
      xs: '0.75rem',
      sm: '0.875rem',
      base: '1rem',
      lg: '1.125rem',
      xl: '1.25rem',
      '2xl': '1.5rem',
      '3xl': '1.875rem'
    },
    fontWeight: {
      normal: '400',
      medium: '500',
      semibold: '600',
      bold: '700'
    }
  },
  
  // 間距標記
  spacing: {
    0: '0',
    1: '0.25rem',
    2: '0.5rem',
    3: '0.75rem',
    4: '1rem',
    5: '1.25rem',
    6: '1.5rem',
    8: '2rem',
    12: '3rem',
    16: '4rem'
  },
  
  // 圓角標記
  borderRadius: {
    none: '0',
    sm: '0.125rem',
    md: '0.375rem',
    lg: '0.5rem',
    xl: '0.75rem',
    full: '9999px'
  },
  
  // 陰影標記
  boxShadow: {
    sm: '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
    md: '0 4px 6px -1px rgba(0, 0, 0, 0.1)',
    lg: '0 10px 15px -3px rgba(0, 0, 0, 0.1)',
    xl: '0 20px 25px -5px rgba(0, 0, 0, 0.1)'
  }
};
```

### 4.2 元件庫架構

```typescript
// components/index.ts - 元件庫導出
export { default as Button } from './Button/Button.vue';
export { default as Input } from './Input/Input.vue';
export { default as Modal } from './Modal/Modal.vue';
export { default as Table } from './Table/Table.vue';
export { default as Card } from './Card/Card.vue';
export { default as Toast } from './Toast/Toast.vue';

// 金融特殊元件
export { default as AccountCard } from './Financial/AccountCard.vue';
export { default as TransactionTable } from './Financial/TransactionTable.vue';
export { default as AmountDisplay } from './Financial/AmountDisplay.vue';
export { default as CurrencyInput } from './Financial/CurrencyInput.vue';

// 佈局元件
export { default as Header } from './Layout/Header.vue';
export { default as Sidebar } from './Layout/Sidebar.vue';
export { default as Footer } from './Layout/Footer.vue';
export { default as Container } from './Layout/Container.vue';
```

## 5. Vue 3 + Tailwind CSS 最佳實踐

### 5.1 元件命名與結構規範

```vue
<!-- 標準 Vue 3 元件結構 -->
<template>
  <div class="component-name">
    <!-- 元件內容 -->
  </div>
</template>

<script setup lang="ts">
// 導入依賴
import { ref, computed, onMounted } from 'vue';
import type { PropType } from 'vue';

// 類型定義
interface ComponentProps {
  // 屬性定義
}

// Props 定義
const props = defineProps<ComponentProps>();

// Emits 定義
const emit = defineEmits<{
  change: [value: string];
  submit: [data: any];
}>();

// 響應式狀態
const state = ref('');

// 計算屬性
const computedValue = computed(() => {
  return state.value.toUpperCase();
});

// 生命週期
onMounted(() => {
  // 初始化邏輯
});

// 方法
const handleSubmit = () => {
  emit('submit', state.value);
};
</script>

<style scoped>
/* 僅在必要時使用 scoped 樣式 */
/* 優先使用 Tailwind CSS 類別 */
</style>
```

### 5.2 Tailwind CSS 自定義配置

```javascript
// tailwind.config.js
const { designTokens } = require('./design-tokens');

module.exports = {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}'
  ],
  theme: {
    extend: {
      colors: designTokens.colors,
      fontFamily: designTokens.typography.fontFamily,
      fontSize: designTokens.typography.fontSize,
      spacing: designTokens.spacing,
      borderRadius: designTokens.borderRadius,
      boxShadow: designTokens.boxShadow,
      
      // 自定義動畫
      animation: {
        'fade-in': 'fadeIn 0.3s ease-in-out',
        'slide-up': 'slideUp 0.3s ease-out',
        'pulse-slow': 'pulse 2s infinite'
      },
      
      // 自定義關鍵影格
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' }
        },
        slideUp: {
          '0%': { transform: 'translateY(10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' }
        }
      }
    }
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio'),
    
    // 自定義外掛
    function({ addUtilities }) {
      const newUtilities = {
        '.safe-area-inset': {
          paddingTop: 'env(safe-area-inset-top)',
          paddingBottom: 'env(safe-area-inset-bottom)',
          paddingLeft: 'env(safe-area-inset-left)',
          paddingRight: 'env(safe-area-inset-right)'
        }
      };
      addUtilities(newUtilities);
    }
  ]
};
```

## 6. 檢測與驗證

### 6.1 視覺回歸測試

```javascript
// tests/visual-regression.spec.js
import { test, expect } from '@playwright/test';

test.describe('視覺回歸測試', () => {
  test('首頁載入正確', async ({ page }) => {
    await page.goto('/');
    await page.waitForLoadState('networkidle');
    await expect(page).toHaveScreenshot('homepage.png');
  });

  test('登入表單顯示正確', async ({ page }) => {
    await page.goto('/login');
    await expect(page.locator('.login-form')).toHaveScreenshot('login-form.png');
  });

  test('帳戶列表 RWD 測試', async ({ page }) => {
    // 桌面版
    await page.setViewportSize({ width: 1280, height: 720 });
    await page.goto('/accounts');
    await expect(page).toHaveScreenshot('accounts-desktop.png');

    // 平板版
    await page.setViewportSize({ width: 768, height: 1024 });
    await expect(page).toHaveScreenshot('accounts-tablet.png');

    // 手機版
    await page.setViewportSize({ width: 375, height: 667 });
    await expect(page).toHaveScreenshot('accounts-mobile.png');
  });
});
```

### 6.2 無障礙檢測

```javascript
// tests/accessibility.spec.js
import { test } from '@playwright/test';
import { injectAxe, checkA11y } from 'axe-playwright';

test.describe('無障礙檢測', () => {
  test.beforeEach(async ({ page }) => {
    await injectAxe(page);
  });

  test('首頁無障礙檢測', async ({ page }) => {
    await page.goto('/');
    await checkA11y(page, null, {
      detailedReport: true,
      detailedReportOptions: { html: true }
    });
  });

  test('表單無障礙檢測', async ({ page }) => {
    await page.goto('/transfer');
    await checkA11y(page, '.transfer-form', {
      rules: {
        'color-contrast': { enabled: true },
        'keyboard-navigation': { enabled: true },
        'aria-labels': { enabled: true }
      }
    });
  });
});
```

### 6.3 使用性測試清單

```markdown
# 使用性測試檢查清單

## 導航測試
- [ ] 主導航清晰可見
- [ ] 麵包屑導航正確顯示
- [ ] 返回按鈕功能正常
- [ ] 搜尋功能易於使用

## 表單測試
- [ ] 必填欄位明確標示
- [ ] 錯誤訊息清楚易懂
- [ ] 驗證即時回饋
- [ ] 提交成功提示

## 回應式設計測試
- [ ] 手機版佈局適當
- [ ] 平板版互動順暢
- [ ] 桌面版充分利用空間
- [ ] 觸控操作友善

## 性能測試
- [ ] 頁面載入時間 < 3 秒
- [ ] 圖片最佳化載入
- [ ] 無不必要的網路請求
- [ ] 離線提示機制

## 安全性測試
- [ ] 敏感資訊適當遮蔽
- [ ] HTTPS 連線確認
- [ ] 會話逾時提醒
- [ ] 重要操作二次確認
```

---

## 結論

本 UI/UX 開發指引涵蓋了金融大型平台前端開發的完整規範，從設計原則到技術實作，從無障礙設計到性能優化。開發團隊應：

1. **嚴格遵循設計規範**: 確保產品一致性與專業性
2. **重視使用者體驗**: 以使用者為中心進行設計決策
3. **持續改進優化**: 根據使用者回饋不斷完善產品
4. **保持技術更新**: 跟上 Vue 3 與 Tailwind CSS 最新發展

---

## 7. 性能優化指引

### 7.1 前端載入性能優化

#### 程式碼分割與懶載入

```typescript
// 路由層級的懶載入
import { createRouter, createWebHistory } from 'vue-router';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'Dashboard',
      component: () => import('@/views/Dashboard.vue')
    },
    {
      path: '/accounts',
      name: 'Accounts',
      component: () => import('@/views/Accounts.vue'),
      children: [
        {
          path: 'transfer',
          component: () => import('@/views/accounts/Transfer.vue')
        }
      ]
    }
  ]
});

// 元件層級的懶載入
import { defineAsyncComponent } from 'vue';

export const LazyModal = defineAsyncComponent(() =>
  import('@/components/Modal.vue')
);
```

#### 圖片優化策略

```vue
<template>
  <!-- 響應式圖片 -->
  <picture>
    <source 
      media="(min-width: 768px)" 
      srcset="/images/hero-desktop.webp"
      type="image/webp"
    />
    <source 
      media="(min-width: 768px)" 
      srcset="/images/hero-desktop.jpg"
    />
    <source 
      srcset="/images/hero-mobile.webp"
      type="image/webp"
    />
    <img 
      src="/images/hero-mobile.jpg" 
      alt="銀行服務展示"
      loading="lazy"
      class="w-full h-auto"
    />
  </picture>
  
  <!-- 延遲載入頭像 -->
  <img 
    v-if="userAvatar"
    :src="userAvatar"
    alt="使用者頭像"
    loading="lazy"
    class="w-10 h-10 rounded-full"
    @error="handleImageError"
  />
</template>

<script setup lang="ts">
const handleImageError = (event: Event) => {
  const img = event.target as HTMLImageElement;
  img.src = '/images/default-avatar.png';
};
</script>
```

#### 快取策略

```typescript
// Service Worker 快取策略
import { precacheAndRoute, cleanupOutdatedCaches } from 'workbox-precaching';
import { registerRoute } from 'workbox-routing';
import { StaleWhileRevalidate, CacheFirst } from 'workbox-strategies';

// 清理過期快取
cleanupOutdatedCaches();

// 預快取靜態資源
precacheAndRoute(self.__WB_MANIFEST);

// API 回應快取策略
registerRoute(
  ({ url }) => url.pathname.startsWith('/api/'),
  new StaleWhileRevalidate({
    cacheName: 'api-cache',
    plugins: [
      {
        cacheWillUpdate: async ({ response }) => {
          return response.status === 200 ? response : null;
        }
      }
    ]
  })
);

// 靜態資源快取策略
registerRoute(
  ({ request }) => request.destination === 'image',
  new CacheFirst({
    cacheName: 'images-cache',
    plugins: [
      {
        cacheWillUpdate: async ({ response }) => {
          return response.status === 200 ? response : null;
        }
      }
    ]
  })
);
```

### 7.2 執行時性能優化

#### Vue 3 性能最佳化

```vue
<template>
  <!-- 使用 v-memo 優化大型列表 -->
  <div 
    v-for="transaction in transactions" 
    :key="transaction.id"
    v-memo="[transaction.amount, transaction.status]"
    class="transaction-item"
  >
    {{ transaction.description }}
  </div>
  
  <!-- 虛擬滾動優化超長列表 -->
  <VirtualList
    :items="longTransactionList"
    :item-height="60"
    :container-height="400"
    v-slot="{ item, index }"
  >
    <TransactionItem :transaction="item" :index="index" />
  </VirtualList>
</template>

<script setup lang="ts">
import { computed, shallowRef } from 'vue';

// 使用 shallowRef 減少深度響應式開銷
const transactions = shallowRef([]);

// 使用 computed 快取複雜計算
const totalAmount = computed(() => {
  return transactions.value.reduce((sum, t) => sum + t.amount, 0);
});

// 防抖搜尋
import { debounce } from 'lodash-es';

const searchTransactions = debounce((query: string) => {
  // 搜尋邏輯
}, 300);
</script>
```

#### 網路請求優化

```typescript
// API 請求去重與快取
class APIManager {
  private requestCache = new Map();
  private pendingRequests = new Map();

  async get<T>(url: string, options?: RequestInit): Promise<T> {
    const cacheKey = `${url}${JSON.stringify(options)}`;
    
    // 檢查快取
    if (this.requestCache.has(cacheKey)) {
      const cached = this.requestCache.get(cacheKey);
      if (Date.now() - cached.timestamp < 5 * 60 * 1000) { // 5分鐘快取
        return cached.data;
      }
    }
    
    // 檢查進行中的請求
    if (this.pendingRequests.has(cacheKey)) {
      return this.pendingRequests.get(cacheKey);
    }
    
    // 發起新請求
    const request = fetch(url, options)
      .then(response => response.json())
      .then(data => {
        this.requestCache.set(cacheKey, {
          data,
          timestamp: Date.now()
        });
        this.pendingRequests.delete(cacheKey);
        return data;
      })
      .catch(error => {
        this.pendingRequests.delete(cacheKey);
        throw error;
      });
    
    this.pendingRequests.set(cacheKey, request);
    return request;
  }
}

// 使用 AbortController 取消無用請求
const controller = new AbortController();

const fetchAccountData = async (accountId: string) => {
  try {
    const response = await fetch(`/api/accounts/${accountId}`, {
      signal: controller.signal
    });
    return await response.json();
  } catch (error) {
    if (error.name === 'AbortError') {
      console.log('請求已取消');
    }
  }
};

// 在組件卸載時取消請求
onUnmounted(() => {
  controller.abort();
});
```

---

## 8. 設計協作流程

### 8.1 設計師與開發者協作規範

#### 設計交付規範

```typescript
// 設計稿命名規範
interface DesignFile {
  name: string; // 格式: [頁面]-[狀態]-[裝置]
  // 範例: "transfer-form-error-mobile.fig"
  page: string; // 頁面名稱
  state: 'default' | 'loading' | 'error' | 'success' | 'empty';
  device: 'desktop' | 'tablet' | 'mobile';
  version: string; // 版本號 v1.0.0
}

// 設計標記 (Design Tokens) 交付格式
interface DesignTokens {
  colors: Record<string, string>;
  typography: {
    fontFamily: Record<string, string[]>;
    fontSize: Record<string, string>;
    fontWeight: Record<string, number>;
    lineHeight: Record<string, number>;
  };
  spacing: Record<string, string>;
  borderRadius: Record<string, string>;
  boxShadow: Record<string, string>;
}
```

#### 協作工具與流程

```markdown
## 設計協作檢查清單

### 設計階段
- [ ] UI 規格書完整包含所有狀態
- [ ] 設計稿包含響應式斷點設計
- [ ] 互動動效規格文件
- [ ] 設計標記 (Design Tokens) 檔案
- [ ] 無障礙設計考量說明

### 開發階段
- [ ] 設計稿審查會議記錄
- [ ] 技術可行性評估報告
- [ ] 元件實作進度追蹤
- [ ] 設計還原度檢查

### 交付階段
- [ ] 跨瀏覽器相容性測試
- [ ] 響應式設計驗證
- [ ] 無障礙檢測通過
- [ ] 性能指標達標
```

### 8.2 設計系統維護

#### 版本控制策略

```json
{
  "name": "@company/design-system",
  "version": "2.1.0",
  "description": "金融平台設計系統",
  "exports": {
    "./tokens": "./dist/tokens.json",
    "./components": "./dist/components/index.js",
    "./styles": "./dist/styles.css"
  },
  "peerDependencies": {
    "vue": "^3.0.0",
    "tailwindcss": "^3.0.0"
  },
  "changelog": {
    "2.1.0": [
      "新增: 深色模式支援",
      "修正: 表單元件無障礙問題",
      "更新: 色彩對比度符合 WCAG 2.1 AA"
    ]
  }
}
```

#### 元件庫文件系統

```vue
<!-- ComponentDoc.vue - 元件文件模板 -->
<template>
  <div class="component-doc">
    <!-- 元件展示 -->
    <section class="demo-section">
      <h2>基本用法</h2>
      <div class="demo-container">
        <Button variant="primary">主要按鈕</Button>
      </div>
      <CodeBlock language="vue" :code="basicUsageCode" />
    </section>
    
    <!-- 所有變體展示 -->
    <section class="variants-section">
      <h2>所有變體</h2>
      <div class="variants-grid">
        <div v-for="variant in variants" :key="variant.name">
          <h3>{{ variant.name }}</h3>
          <component :is="variant.component" v-bind="variant.props" />
        </div>
      </div>
    </section>
    
    <!-- API 文件 -->
    <section class="api-section">
      <h2>API 參考</h2>
      <ApiTable :props="componentProps" :events="componentEvents" />
    </section>
  </div>
</template>
```

---

## 9. 維護與版本控制

### 9.1 設計系統演進策略

#### 語義化版本控制

```typescript
// 版本更新規則
interface VersionUpdate {
  major: 'BREAKING_CHANGE'; // 重大變更，不向後相容
  minor: 'FEATURE'; // 新功能，向後相容
  patch: 'BUGFIX'; // 錯誤修正，向後相容
}

// 變更日誌格式
interface Changelog {
  version: string;
  date: string;
  type: 'added' | 'changed' | 'deprecated' | 'removed' | 'fixed' | 'security';
  description: string;
  impact: 'low' | 'medium' | 'high';
  migration?: string; // 升級指南
}
```

#### 廢棄功能管理

```typescript
// 廢棄警告系統
export function deprecateComponent(
  componentName: string, 
  version: string, 
  alternative?: string
) {
  if (process.env.NODE_ENV === 'development') {
    console.warn(
      `[DEPRECATED] ${componentName} 將在 ${version} 版本中移除。` +
      (alternative ? `請使用 ${alternative} 替代。` : '')
    );
  }
}

// 在元件中使用
export default defineComponent({
  name: 'OldButton',
  setup() {
    deprecateComponent('OldButton', 'v3.0.0', 'NewButton');
    // 元件邏輯
  }
});
```

### 9.2 效能監控與改進

#### 核心指標追蹤

```typescript
// Web Vitals 監控
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';

interface PerformanceMetrics {
  FCP: number; // First Contentful Paint
  LCP: number; // Largest Contentful Paint
  FID: number; // First Input Delay
  CLS: number; // Cumulative Layout Shift
  TTFB: number; // Time to First Byte
}

class PerformanceMonitor {
  private metrics: Partial<PerformanceMetrics> = {};
  
  init() {
    getCLS(metric => {
      this.metrics.CLS = metric.value;
      this.reportMetric('CLS', metric);
    });
    
    getFID(metric => {
      this.metrics.FID = metric.value;
      this.reportMetric('FID', metric);
    });
    
    // 其他指標...
  }
  
  private reportMetric(name: string, metric: any) {
    // 發送到分析服務
    analytics.track('performance_metric', {
      name,
      value: metric.value,
      rating: metric.rating,
      url: window.location.pathname
    });
  }
}
```

#### 持續改進流程

```markdown
## 效能優化檢查清單

### 每月檢查項目
- [ ] Core Web Vitals 指標檢查
- [ ] 頁面載入時間分析
- [ ] 使用者體驗問題收集
- [ ] 第三方套件版本更新

### 季度改進項目
- [ ] 程式碼分割策略檢討
- [ ] 圖片資源優化
- [ ] 快取策略調整
- [ ] CDN 效能分析

### 年度重大檢討
- [ ] 技術棧升級評估
- [ ] 設計系統重構規劃
- [ ] 使用者研究成果整合
- [ ] 競品分析與改進
```

---

## 10. 附錄

### 10.1 常見問題解答

#### Q: 如何處理不同瀏覽器的相容性問題？

A: 使用以下策略確保跨瀏覽器相容：

```typescript
// 特性檢測而非瀏覽器檢測
const supportsWebP = () => {
  const canvas = document.createElement('canvas');
  canvas.width = 1;
  canvas.height = 1;
  return canvas.toDataURL('image/webp').indexOf('data:image/webp') === 0;
};

// 漸進式增強
if ('IntersectionObserver' in window) {
  // 使用 Intersection Observer
} else {
  // 降級方案
}
```

#### Q: 如何確保設計系統的一致性？

A: 透過以下機制維護一致性：

1. **自動化測試**: 視覺回歸測試
2. **程式碼檢查**: ESLint + Stylelint 規則
3. **設計審查**: 定期設計系統審查會議
4. **文件維護**: 保持文件與實作同步

### 10.2 資源連結

#### 設計資源
- [Material Design Guidelines](https://material.io/design)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)

#### 開發工具
- [Vue 3 官方文件](https://vuejs.org/guide/)
- [Tailwind CSS 文件](https://tailwindcss.com/docs)
- [TypeScript 文件](https://www.typescriptlang.org/docs/)

#### 測試工具
- [Playwright](https://playwright.dev/) - E2E 測試
- [axe-core](https://github.com/dequelabs/axe-core) - 無障礙檢測
- [Lighthouse](https://developers.google.com/web/tools/lighthouse) - 效能檢測

### 10.3 版本記錄

| 版本 | 日期 | 變更內容 |
|------|------|----------|
| v2.1.0 | 2024-08-29 | 新增性能優化指引、設計協作流程 |
| v2.0.0 | 2024-07-15 | 重大更新：Vue 3 + Tailwind CSS 架構 |
| v1.5.0 | 2024-06-01 | 新增無障礙設計規範 |
| v1.0.0 | 2024-01-01 | 初始版本發布 |

---

此指引將隨著專案發展持續更新，確保始終符合最佳實踐與業界標準。如有疑問或建議，請聯繫 UI/UX 團隊。

