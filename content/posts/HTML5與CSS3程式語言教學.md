+++
date = '2025-10-21T16:17:19+08:00'
draft = false
title = 'HTML5與CSS3程式語言教學'
tags = ['教學','程式語言' ,'HTML5 & CSS3']
categories = ['技術']
author = 'Eric Cheng'
summary = '提供HTML5 & CSS3程式語言教學'
+++

# HTML5 與 CSS3 程式語言教學手冊

## 目錄

1. [前言](#1-前言)
2. [開發環境設定](#2-開發環境設定)
3. [HTML5 開發規範](#3-html5-開發規範)
4. [CSS3 開發規範](#4-css3-開發規範)
5. [專案中的命名規則與檔案結構](#5-專案中的命名規則與檔案結構)
6. [CSS 動畫與轉場效果](#6-css-動畫與轉場效果)
7. [HTML5 新特性與 API](#7-html5-新特性與-api)
8. [JavaScript 整合與互動](#8-javascript-整合與互動)
9. [網頁無障礙設計](#9-網頁無障礙設計)
10. [常見錯誤與解決方法](#10-常見錯誤與解決方法)
11. [開發最佳實務](#11-開發最佳實務)
12. [範例程式碼](#12-範例程式碼)
13. [結語](#13-結語)
14. [檢查清單](#14-檢查清單)

---

## 1. 前言

### 1.1 HTML5 與 CSS3 在專案中的角色

HTML5 和 CSS3 是現代網頁開發的基石，在我們的專案中扮演著至關重要的角色：

#### HTML5 的角色

- **結構定義者**：負責網頁內容的語意化結構
- **互動基礎**：提供表單、多媒體等互動元素
- **可及性保障**：確保網站對所有使用者都能順利存取
- **SEO 基礎**：良好的 HTML 結構有助於搜尋引擎優化

#### CSS3 的角色

- **視覺呈現**：控制網頁的外觀與佈局
- **使用者體驗**：創造流暢的動畫與互動效果
- **響應式設計**：確保在各種裝置上都有良好的顯示效果
- **效能優化**：減少不必要的圖片使用，提升載入速度

### 1.2 重要性

在現代網頁開發中，HTML5 和 CSS3 的重要性體現在：

1. **標準化**：遵循 W3C 標準，確保跨瀏覽器相容性
2. **可維護性**：良好的結構和命名規則讓程式碼易於維護
3. **效能**：正確使用能大幅提升網頁載入速度
4. **可及性**：符合無障礙設計標準，服務更多使用者
5. **SEO 優化**：語意化的 HTML 有助於搜尋引擎理解內容

---

## 2. 開發環境設定

### 2.1 必要工具

#### 2.1.1 程式碼編輯器

**推薦：Visual Studio Code**

安裝步驟：
1. 前往 [VS Code 官網](https://code.visualstudio.com/) 下載
2. 安裝完成後，建議安裝以下擴充套件：

```bash
# 必裝套件
- HTML CSS Support
- Auto Rename Tag
- Prettier - Code formatter
- Live Server
- IntelliSense for CSS class names in HTML

# 建議套件
- Emmet (內建)
- Bracket Pair Colorizer 2
- HTML Boilerplate
- CSS Peek
```

#### 2.1.2 瀏覽器開發工具

**主要瀏覽器**：

- Google Chrome（建議主要開發瀏覽器）
- Mozilla Firefox
- Microsoft Edge
- Safari（Mac 開發時）

**開發者工具快速鍵**：

- Chrome/Edge：`F12` 或 `Ctrl+Shift+I`
- Firefox：`F12` 或 `Ctrl+Shift+I`
- Safari：`Cmd+Option+I`

### 2.2 專案設定

#### 2.2.1 目錄結構範例

```
project-root/
├── index.html
├── assets/
│   ├── css/
│   │   ├── main.css
│   │   ├── components/
│   │   └── utilities/
│   ├── js/
│   ├── images/
│   └── fonts/
├── pages/
├── components/
└── docs/
```

---

## 3. HTML5 開發規範

### 3.1 基本文件結構

#### 3.1.1 標準 HTML5 文件結構

```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="頁面描述">
    <title>頁面標題</title>
    <link rel="stylesheet" href="assets/css/main.css">
</head>
<body>
    <header>
        <!-- 頁面標頭 -->
    </header>
    
    <nav>
        <!-- 導航選單 -->
    </nav>
    
    <main>
        <!-- 主要內容 -->
        <section>
            <!-- 內容區塊 -->
        </section>
    </main>
    
    <aside>
        <!-- 側邊欄 -->
    </aside>
    
    <footer>
        <!-- 頁尾 -->
    </footer>
    
    <script src="assets/js/main.js"></script>
</body>
</html>
```

### 3.2 語意化標籤使用規範

#### 3.2.1 結構性標籤

| 標籤 | 用途 | 使用時機 |
|------|------|----------|
| `<header>` | 頁面或區塊標頭 | 包含標題、Logo、導航 |
| `<nav>` | 導航選單 | 主要導航、麵包屑導航 |
| `<main>` | 主要內容 | 每頁只能有一個 |
| `<section>` | 內容區塊 | 有明確主題的內容群組 |
| `<article>` | 獨立文章 | 新聞、部落格文章、評論 |
| `<aside>` | 側邊內容 | 相關連結、廣告、側邊欄 |
| `<footer>` | 頁尾 | 版權、聯絡資訊、相關連結 |

### 3.3 表單開發規範

#### 3.3.1 基本表單結構

```html
<form action="/submit" method="post" novalidate>
    <fieldset>
        <legend>個人資訊</legend>
        
        <div class="form-group">
            <label for="username">使用者名稱 <span class="required">*</span></label>
            <input 
                type="text" 
                id="username" 
                name="username" 
                required 
                aria-describedby="username-help"
                autocomplete="username"
            >
            <small id="username-help" class="form-text">
                請輸入3-20個字元的使用者名稱
            </small>
        </div>
    </fieldset>
    
    <button type="submit" class="btn btn-primary">送出</button>
</form>
```

---

## 4. CSS3 開發規範

### 4.1 CSS 基礎結構與選擇器

#### 4.1.1 CSS 檔案組織結構

```css
/* ==========================================================================
   Variables
   ========================================================================== */
:root {
  --primary-color: #007bff;
  --secondary-color: #6c757d;
  --text-color: #212529;
  --bg-color: #ffffff;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
  --border-radius: 8px;
  --transition: all 0.3s ease;
}

/* ==========================================================================
   Base Styles
   ========================================================================== */
*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  line-height: 1.5;
  color: var(--text-color);
  background-color: var(--bg-color);
  margin: 0;
  padding: 0;
}
```

### 4.2 Flexbox 佈局規範

```css
/* Flexbox 基本使用 */
.flex-container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: var(--spacing-md);
}

/* 響應式 Flexbox */
.card-layout {
  display: flex;
  flex-wrap: wrap;
  gap: var(--spacing-md);
}

.card {
  flex: 1 1 300px; /* 最小寬度 300px */
}
```

### 4.3 CSS Grid 佈局規範

```css
/* Grid 基本使用 */
.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: var(--spacing-md);
}

/* 12欄系統 */
.grid-12 {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--spacing-md);
}

.col-6 { grid-column: span 6; }
.col-4 { grid-column: span 4; }
```

### 4.4 響應式設計規範

```css
/* Mobile First 設計 */
.container {
  width: 100%;
  padding: 0 var(--spacing-md);
}

@media (min-width: 768px) {
  .container {
    max-width: 750px;
    margin: 0 auto;
  }
}

@media (min-width: 1200px) {
  .container {
    max-width: 1170px;
  }
}
```

---

## 5. 專案中的命名規則與檔案結構

### 5.1 BEM 命名法

```css
/* Block（區塊） */
.card {
  border: 1px solid #ddd;
  border-radius: var(--border-radius);
  padding: var(--spacing-md);
}

/* Element（元素） */
.card__title {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: var(--spacing-sm);
}

.card__content {
  line-height: 1.6;
}

/* Modifier（修飾符） */
.card--large {
  padding: var(--spacing-lg);
}

.card--primary {
  border-color: var(--primary-color);
}
```

### 5.2 檔案結構組織

```
assets/css/
├── main.css
├── base/
│   ├── _reset.css
│   ├── _variables.css
│   └── _typography.css
├── components/
│   ├── _buttons.css
│   ├── _cards.css
│   └── _forms.css
├── layout/
│   ├── _header.css
│   ├── _footer.css
│   └── _grid.css
└── pages/
    ├── _home.css
    └── _about.css
```

---

## 6. CSS 動畫與轉場效果

### 6.1 CSS Transitions（轉場效果）

#### 6.1.1 基本轉場設定

```css
/* 基本轉場效果 */
.button {
  background-color: var(--primary-color);
  color: white;
  padding: var(--spacing-sm) var(--spacing-md);
  border: none;
  border-radius: var(--border-radius);
  cursor: pointer;
  transition: all 0.3s ease;
}

.button:hover {
  background-color: var(--primary-hover);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 123, 255, 0.3);
}

/* 分別設定不同屬性的轉場 */
.card {
  transition-property: transform, box-shadow;
  transition-duration: 0.3s, 0.2s;
  transition-timing-function: ease-out, ease;
}
```

#### 6.1.2 轉場函數與時機

```css
/* 各種轉場函數 */
.ease-linear { transition-timing-function: linear; }
.ease-in { transition-timing-function: ease-in; }
.ease-out { transition-timing-function: ease-out; }
.ease-in-out { transition-timing-function: ease-in-out; }

/* 使用 cubic-bezier 自訂轉場 */
.custom-easing {
  transition-timing-function: cubic-bezier(0.68, -0.55, 0.265, 1.55);
}
```

### 6.2 CSS Animations（動畫）

#### 6.2.1 @keyframes 規則

```css
/* 定義動畫 */
@keyframes fadeInUp {
  0% {
    opacity: 0;
    transform: translateY(30px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes pulse {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
}

@keyframes rotate {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
```

#### 6.2.2 動畫屬性設定

```css
/* 使用動畫 */
.fade-in {
  animation: fadeInUp 0.6s ease-out;
}

.loading-spinner {
  animation: rotate 1s linear infinite;
}

.heartbeat {
  animation: pulse 1.5s ease-in-out infinite;
}

/* 動畫延遲和重複 */
.stagger-1 { animation-delay: 0.1s; }
.stagger-2 { animation-delay: 0.2s; }
.stagger-3 { animation-delay: 0.3s; }

/* 動畫填充模式 */
.modal-enter {
  animation: fadeInUp 0.3s ease-out forwards;
}
```

### 6.3 效能優化動畫

#### 6.3.1 GPU 加速動畫

```css
/* 優化動畫效能 */
.optimized-animation {
  will-change: transform;
  transform: translateZ(0); /* 觸發硬體加速 */
}

/* 避免引起重排的屬性動畫 */
.good-animation {
  transition: transform 0.3s, opacity 0.3s;
}

/* 避免使用這些屬性進行動畫 */
.bad-animation {
  /* ❌ 會引起重排 */
  transition: width 0.3s, height 0.3s, top 0.3s, left 0.3s;
}
```

#### 6.3.2 減少動畫對可及性的影響

```css
/* 尊重使用者的動畫偏好設定 */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

### 6.4 常用動畫範例

#### 6.4.1 載入動畫

```css
/* 旋轉載入器 */
.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid var(--primary-color);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* 跳動點載入器 */
.dots-loader {
  display: flex;
  gap: 4px;
}

.dots-loader span {
  width: 8px;
  height: 8px;
  background: var(--primary-color);
  border-radius: 50%;
  animation: bounce 1.4s ease-in-out infinite both;
}

.dots-loader span:nth-child(1) { animation-delay: -0.32s; }
.dots-loader span:nth-child(2) { animation-delay: -0.16s; }

@keyframes bounce {
  0%, 80%, 100% {
    transform: scale(0);
  }
  40% {
    transform: scale(1);
  }
}
```

#### 6.4.2 頁面進入動畫

```css
/* 頁面載入動畫 */
.page-enter {
  animation: pageSlideIn 0.5s ease-out;
}

@keyframes pageSlideIn {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

/* 卡片序列動畫 */
.card-list .card {
  opacity: 0;
  animation: cardFadeIn 0.6s ease-out forwards;
}

.card-list .card:nth-child(1) { animation-delay: 0.1s; }
.card-list .card:nth-child(2) { animation-delay: 0.2s; }
.card-list .card:nth-child(3) { animation-delay: 0.3s; }

@keyframes cardFadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

---

## 7. HTML5 新特性與 API

### 7.1 語意化標籤

#### 7.1.1 內容區塊標籤

```html
<!-- 文章結構 -->
<article class="blog-post">
  <header>
    <h1>文章標題</h1>
    <p class="meta">
      <time datetime="2024-08-29">2024年8月29日</time>
      由 <span class="author">作者名稱</span> 發表
    </p>
  </header>
  
  <section class="content">
    <p>文章內容...</p>
  </section>
  
  <footer>
    <p>標籤：<span class="tags">HTML5, 教學</span></p>
  </footer>
</article>

<!-- 圖片與說明 -->
<figure>
  <img src="chart.png" alt="統計圖表">
  <figcaption>2024年網站訪問量統計圖</figcaption>
</figure>

<!-- 詳細資訊 -->
<details>
  <summary>更多資訊</summary>
  <p>這裡是詳細的說明內容...</p>
</details>
```

### 7.2 表單新功能

#### 7.2.1 新的輸入類型

```html
<!-- 新的 input 類型 -->
<form class="modern-form">
  <!-- 電子郵件 -->
  <div class="form-group">
    <label for="email">電子郵件</label>
    <input type="email" id="email" name="email" required>
  </div>
  
  <!-- 電話號碼 -->
  <div class="form-group">
    <label for="phone">電話號碼</label>
    <input type="tel" id="phone" name="phone">
  </div>
  
  <!-- 網址 -->
  <div class="form-group">
    <label for="website">網站</label>
    <input type="url" id="website" name="website">
  </div>
  
  <!-- 數字 -->
  <div class="form-group">
    <label for="age">年齡</label>
    <input type="number" id="age" name="age" min="18" max="100">
  </div>
  
  <!-- 日期 -->
  <div class="form-group">
    <label for="birthday">生日</label>
    <input type="date" id="birthday" name="birthday">
  </div>
  
  <!-- 範圍滑桿 -->
  <div class="form-group">
    <label for="volume">音量</label>
    <input type="range" id="volume" name="volume" min="0" max="100">
  </div>
  
  <!-- 顏色選擇器 -->
  <div class="form-group">
    <label for="color">選擇顏色</label>
    <input type="color" id="color" name="color">
  </div>
</form>
```

#### 7.2.2 表單驗證屬性

```html
<!-- HTML5 表單驗證 -->
<form novalidate>
  <div class="form-group">
    <label for="username">使用者名稱</label>
    <input 
      type="text" 
      id="username" 
      name="username"
      required
      minlength="3"
      maxlength="20"
      pattern="[a-zA-Z0-9_]+"
      title="只能包含字母、數字和底線"
    >
  </div>
  
  <div class="form-group">
    <label for="password">密碼</label>
    <input 
      type="password" 
      id="password" 
      name="password"
      required
      minlength="8"
      pattern="(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]"
      title="密碼必須包含大小寫字母、數字和特殊字元"
    >
  </div>
</form>
```

### 7.3 多媒體元素

#### 7.3.1 音訊和視訊

```html
<!-- 音訊播放器 -->
<audio controls>
  <source src="audio.mp3" type="audio/mpeg">
  <source src="audio.ogg" type="audio/ogg">
  您的瀏覽器不支援音訊播放。
</audio>

<!-- 視訊播放器 -->
<video controls width="640" height="360" poster="video-poster.jpg">
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
  <track kind="subtitles" src="subtitles.vtt" srclang="zh-TW" label="繁體中文">
  您的瀏覽器不支援視訊播放。
</video>
```

### 7.4 本地儲存 API

#### 7.4.1 localStorage 和 sessionStorage

```javascript
// localStorage 基本使用
localStorage.setItem('user-preference', JSON.stringify({
  theme: 'dark',
  language: 'zh-TW'
}));

const preference = JSON.parse(localStorage.getItem('user-preference'));

// sessionStorage 使用（會話結束後清除）
sessionStorage.setItem('current-form-data', JSON.stringify(formData));
```

---

## 8. JavaScript 整合與互動

### 8.1 DOM 操作最佳實務

#### 8.1.1 現代 JavaScript 選擇器

```javascript
// 現代 DOM 查詢方法
const element = document.querySelector('.my-class');
const elements = document.querySelectorAll('.item');

// 使用 optional chaining 避免錯誤
const text = element?.textContent;

// 事件委派
document.addEventListener('click', (e) => {
  if (e.target.matches('.button')) {
    handleButtonClick(e.target);
  }
});
```

#### 8.1.2 響應式互動

```javascript
// 響應式互動範例
class ResponsiveNavigation {
  constructor() {
    this.nav = document.querySelector('.navigation');
    this.toggle = document.querySelector('.nav-toggle');
    this.init();
  }
  
  init() {
    this.toggle.addEventListener('click', () => this.toggleNav());
    window.addEventListener('resize', () => this.handleResize());
  }
  
  toggleNav() {
    this.nav.classList.toggle('nav--open');
    this.toggle.setAttribute('aria-expanded', 
      this.nav.classList.contains('nav--open')
    );
  }
  
  handleResize() {
    if (window.innerWidth > 768) {
      this.nav.classList.remove('nav--open');
    }
  }
}

// 初始化導航
new ResponsiveNavigation();
```

### 8.2 Web API 整合

#### 8.2.1 Intersection Observer

```javascript
// 圖片延遲載入
const imageObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      img.classList.remove('lazy');
      imageObserver.unobserve(img);
    }
  });
});

document.querySelectorAll('img[data-src]').forEach(img => {
  imageObserver.observe(img);
});
```

#### 8.2.2 表單驗證增強

```javascript
// 自訂表單驗證
class FormValidator {
  constructor(form) {
    this.form = form;
    this.init();
  }
  
  init() {
    this.form.addEventListener('submit', (e) => this.handleSubmit(e));
    this.form.addEventListener('input', (e) => this.validateField(e.target));
  }
  
  validateField(field) {
    const isValid = field.checkValidity();
    const errorElement = field.nextElementSibling;
    
    if (!isValid) {
      field.classList.add('error');
      if (errorElement && errorElement.classList.contains('error-message')) {
        errorElement.textContent = field.validationMessage;
      }
    } else {
      field.classList.remove('error');
      if (errorElement && errorElement.classList.contains('error-message')) {
        errorElement.textContent = '';
      }
    }
    
    return isValid;
  }
  
  handleSubmit(e) {
    e.preventDefault();
    const isFormValid = Array.from(this.form.elements)
      .filter(field => field.type !== 'submit')
      .every(field => this.validateField(field));
    
    if (isFormValid) {
      this.submitForm();
    }
  }
  
  async submitForm() {
    try {
      const formData = new FormData(this.form);
      const response = await fetch(this.form.action, {
        method: 'POST',
        body: formData
      });
      
      if (response.ok) {
        this.showSuccess('表單提交成功！');
      } else {
        throw new Error('提交失敗');
      }
    } catch (error) {
      this.showError('提交時發生錯誤，請稍後再試。');
    }
  }
}
```

---

## 9. 網頁無障礙設計

### 9.1 ARIA 標籤使用

#### 9.1.1 基本 ARIA 屬性

```html
<!-- 角色定義 -->
<nav role="navigation" aria-label="主要導航">
  <ul>
    <li><a href="/" aria-current="page">首頁</a></li>
    <li><a href="/about">關於我們</a></li>
  </ul>
</nav>

<!-- 狀態描述 -->
<button aria-expanded="false" aria-controls="menu">選單</button>
<ul id="menu" aria-hidden="true">
  <!-- 選單項目 -->
</ul>

<!-- 表單標籤 -->
<label for="search">搜尋</label>
<input 
  type="search" 
  id="search" 
  aria-describedby="search-help"
  aria-required="true"
>
<div id="search-help">輸入關鍵字進行搜尋</div>
```

#### 9.1.2 複雜互動元件

```html
<!-- 標籤頁介面 -->
<div class="tabs" role="tablist" aria-label="內容分類">
  <button role="tab" aria-selected="true" aria-controls="panel1" id="tab1">
    標籤一
  </button>
  <button role="tab" aria-selected="false" aria-controls="panel2" id="tab2">
    標籤二
  </button>
</div>

<div role="tabpanel" id="panel1" aria-labelledby="tab1">
  <!-- 內容一 -->
</div>

<div role="tabpanel" id="panel2" aria-labelledby="tab2" hidden>
  <!-- 內容二 -->
</div>
```

### 9.2 鍵盤導航

#### 9.2.1 焦點管理

```css
/* 視覺焦點指示器 */
.btn:focus,
.form-control:focus {
  outline: 2px solid var(--focus-color);
  outline-offset: 2px;
}

/* 隱藏滑鼠焦點，保留鍵盤焦點 */
.btn:focus:not(:focus-visible) {
  outline: none;
}

.btn:focus-visible {
  outline: 2px solid var(--focus-color);
  outline-offset: 2px;
}
```

#### 9.2.2 跳過連結

```html
<!-- 跳過連結（輔助鍵盤使用者） -->
<a href="#main-content" class="skip-link">跳至主要內容</a>

<style>
.skip-link {
  position: absolute;
  top: -40px;
  left: 6px;
  background: var(--primary-color);
  color: white;
  padding: 8px;
  text-decoration: none;
  z-index: 1000;
}

.skip-link:focus {
  top: 6px;
}
</style>
```

### 9.3 色彩對比與文字

#### 9.3.1 色彩對比要求

```css
/* 確保充足的色彩對比 */
:root {
  --text-primary: #212529;    /* 對比比例 16.75:1 */
  --text-secondary: #6c757d;  /* 對比比例 7.04:1 */
  --bg-primary: #ffffff;
  
  /* 錯誤狀態不能只靠顏色表示 */
  --error-color: #dc3545;
  --error-bg: #f8d7da;
  --error-border: #f5c6cb;
}

.error-message {
  color: var(--error-color);
  background-color: var(--error-bg);
  border: 1px solid var(--error-border);
  padding: var(--spacing-sm);
  border-radius: var(--border-radius);
}

.error-message::before {
  content: "⚠ ";
  font-weight: bold;
}
```

---

## 10. 常見錯誤與解決方法

### 10.1 HTML 常見錯誤

#### 10.1.1 語意化錯誤

**❌ 錯誤做法**：
```html
<div class="header">
  <div class="title">網站標題</div>
</div>
```

**✅ 正確做法**：
```html
<header class="site-header">
  <h1 class="site-title">網站標題</h1>
</header>
```

#### 10.1.2 表單可及性錯誤

**❌ 錯誤做法**：
```html
<input type="text" placeholder="請輸入姓名">
```

**✅ 正確做法**：
```html
<label for="name">姓名</label>
<input type="text" id="name" name="name" required>
```

### 10.2 CSS 常見錯誤

#### 10.2.1 選擇器特異性問題

**❌ 錯誤做法**：
```css
#header .navigation ul li a.active {
  color: red;
}
```

**✅ 正確做法**：
```css
.nav-link--active {
  color: var(--primary-color);
}
```

#### 10.2.2 響應式設計錯誤

**❌ 錯誤做法**：
```css
.container {
  width: 1200px;
}
```

**✅ 正確做法**：
```css
.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--spacing-md);
}
```

---

## 11. 開發最佳實務

### 11.1 效能優化

#### 11.1.1 HTML 效能優化

```html
<!-- 關鍵資源預載入 -->
<link rel="preload" href="assets/fonts/main.woff2" as="font" type="font/woff2" crossorigin>

<!-- 響應式圖片 -->
<picture>
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="描述文字" loading="lazy">
</picture>

<!-- JavaScript 延遲載入 -->
<script src="script.js" defer></script>
```

#### 11.1.2 CSS 效能優化

```css
/* 使用 CSS 自訂屬性 */
:root {
  --primary-color: #007bff;
  --transition: all 0.3s ease;
}

/* 避免昂貴的選擇器 */
.button { /* ✅ 好 */ }
div > div > div > a { /* ❌ 避免 */ }

/* 優化動畫 */
.animate {
  will-change: transform;
  transform: translateZ(0);
}
```

### 11.2 可維護性

#### 11.2.1 模組化開發

```css
/* 組件化樣式 */
.btn {
  display: inline-block;
  padding: var(--spacing-sm) var(--spacing-md);
  border: none;
  border-radius: var(--border-radius);
  cursor: pointer;
  transition: var(--transition);
}

.btn--primary {
  background-color: var(--primary-color);
  color: white;
}

.btn--secondary {
  background-color: var(--secondary-color);
  color: white;
}
```

### 11.3 跨瀏覽器相容性

```css
/* 漸進增強 */
.grid-container {
  /* 回退：Flexbox */
  display: flex;
  flex-wrap: wrap;
}

@supports (display: grid) {
  .grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  }
}
```

---

## 12. 範例程式碼

### 12.1 完整的響應式卡片組件

#### HTML 結構

```html
<article class="product-card">
  <div class="product-card__image-container">
    <img src="product.jpg" alt="產品圖片" class="product-card__image">
    <span class="product-card__badge">新品</span>
  </div>
  
  <div class="product-card__content">
    <h3 class="product-card__title">產品標題</h3>
    <p class="product-card__description">產品描述文字</p>
    
    <div class="product-card__footer">
      <span class="product-card__price">NT$ 1,299</span>
      <button class="btn btn--primary">加入購物車</button>
    </div>
  </div>
</article>
```

#### CSS 樣式

```css
.product-card {
  display: flex;
  flex-direction: column;
  background: white;
  border-radius: var(--border-radius);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: var(--transition);
}

.product-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}

.product-card__image-container {
  position: relative;
}

.product-card__image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.product-card__badge {
  position: absolute;
  top: var(--spacing-sm);
  left: var(--spacing-sm);
  background: var(--primary-color);
  color: white;
  padding: var(--spacing-xs) var(--spacing-sm);
  border-radius: var(--border-radius);
  font-size: 0.875rem;
}

.product-card__content {
  padding: var(--spacing-md);
  flex: 1;
  display: flex;
  flex-direction: column;
}

.product-card__title {
  margin: 0 0 var(--spacing-sm) 0;
  font-size: 1.125rem;
  font-weight: 600;
}

.product-card__description {
  margin: 0 0 var(--spacing-md) 0;
  color: #666;
  line-height: 1.5;
  flex: 1;
}

.product-card__footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--spacing-sm);
}

.product-card__price {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--primary-color);
}

/* 響應式調整 */
@media (max-width: 767px) {
  .product-card__footer {
    flex-direction: column;
    gap: var(--spacing-sm);
  }
  
  .btn {
    width: 100%;
  }
}
```

### 12.2 響應式導航選單

#### HTML 結構

```html
<nav class="main-navigation" role="navigation" aria-label="主要導航">
  <div class="nav-container">
    <a href="/" class="nav-brand">
      <img src="logo.svg" alt="公司標誌" class="nav-logo">
    </a>
    
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav-menu">
      <span class="hamburger"></span>
      <span class="sr-only">開啟選單</span>
    </button>
    
    <ul class="nav-menu" id="nav-menu">
      <li class="nav-item">
        <a href="/" class="nav-link" aria-current="page">首頁</a>
      </li>
      <li class="nav-item">
        <a href="/products" class="nav-link">產品</a>
      </li>
      <li class="nav-item">
        <a href="/about" class="nav-link">關於我們</a>
      </li>
      <li class="nav-item">
        <a href="/contact" class="nav-link">聯絡我們</a>
      </li>
    </ul>
  </div>
</nav>
```

#### CSS 樣式

```css
.main-navigation {
  background: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--spacing-md);
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 60px;
}

.nav-brand {
  display: flex;
  align-items: center;
}

.nav-logo {
  height: 40px;
  width: auto;
}

.nav-toggle {
  display: none;
  flex-direction: column;
  background: none;
  border: none;
  cursor: pointer;
  padding: var(--spacing-sm);
}

.hamburger {
  width: 25px;
  height: 3px;
  background: var(--text-color);
  transition: var(--transition);
  position: relative;
}

.hamburger::before,
.hamburger::after {
  content: '';
  position: absolute;
  width: 25px;
  height: 3px;
  background: var(--text-color);
  transition: var(--transition);
}

.hamburger::before {
  top: -8px;
}

.hamburger::after {
  top: 8px;
}

.nav-menu {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
  gap: var(--spacing-lg);
}

.nav-link {
  text-decoration: none;
  color: var(--text-color);
  font-weight: 500;
  padding: var(--spacing-sm) 0;
  position: relative;
  transition: var(--transition);
}

.nav-link:hover,
.nav-link[aria-current="page"] {
  color: var(--primary-color);
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--primary-color);
  transition: width 0.3s ease;
}

.nav-link:hover::after,
.nav-link[aria-current="page"]::after {
  width: 100%;
}

/* 行動裝置樣式 */
@media (max-width: 768px) {
  .nav-toggle {
    display: flex;
  }
  
  .nav-menu {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: white;
    flex-direction: column;
    padding: var(--spacing-md);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transform: translateY(-10px);
    opacity: 0;
    visibility: hidden;
    transition: all 0.3s ease;
  }
  
  .nav-menu.nav-menu--open {
    transform: translateY(0);
    opacity: 1;
    visibility: visible;
  }
  
  .nav-item {
    padding: var(--spacing-sm) 0;
    border-bottom: 1px solid #eee;
  }
  
  .nav-item:last-child {
    border-bottom: none;
  }
  
  /* 漢堡選單動畫 */
  .nav-toggle[aria-expanded="true"] .hamburger {
    background: transparent;
  }
  
  .nav-toggle[aria-expanded="true"] .hamburger::before {
    transform: rotate(45deg);
    top: 0;
  }
  
  .nav-toggle[aria-expanded="true"] .hamburger::after {
    transform: rotate(-45deg);
    top: 0;
  }
}
```

#### JavaScript 互動

```javascript
class MobileNavigation {
  constructor() {
    this.nav = document.querySelector('.main-navigation');
    this.toggle = document.querySelector('.nav-toggle');
    this.menu = document.querySelector('.nav-menu');
    this.links = document.querySelectorAll('.nav-link');
    
    this.init();
  }
  
  init() {
    this.toggle.addEventListener('click', () => this.toggleMenu());
    this.links.forEach(link => {
      link.addEventListener('click', () => this.closeMenu());
    });
    
    // ESC 鍵關閉選單
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && this.isMenuOpen()) {
        this.closeMenu();
      }
    });
    
    // 點擊外部關閉選單
    document.addEventListener('click', (e) => {
      if (!this.nav.contains(e.target) && this.isMenuOpen()) {
        this.closeMenu();
      }
    });
  }
  
  toggleMenu() {
    const isOpen = this.isMenuOpen();
    
    if (isOpen) {
      this.closeMenu();
    } else {
      this.openMenu();
    }
  }
  
  openMenu() {
    this.menu.classList.add('nav-menu--open');
    this.toggle.setAttribute('aria-expanded', 'true');
    
    // 焦點管理
    const firstLink = this.menu.querySelector('.nav-link');
    if (firstLink) {
      firstLink.focus();
    }
  }
  
  closeMenu() {
    this.menu.classList.remove('nav-menu--open');
    this.toggle.setAttribute('aria-expanded', 'false');
  }
  
  isMenuOpen() {
    return this.menu.classList.contains('nav-menu--open');
  }
}

// 初始化導航
document.addEventListener('DOMContentLoaded', () => {
  new MobileNavigation();
});
```

### 12.3 進階表單範例

#### HTML 結構

```html
<form class="contact-form" novalidate>
  <h2>聯絡我們</h2>
  
  <div class="form-row">
    <div class="form-group">
      <label for="firstName">名字 <span class="required">*</span></label>
      <input 
        type="text" 
        id="firstName" 
        name="firstName" 
        required 
        aria-describedby="firstName-error"
        autocomplete="given-name"
      >
      <div id="firstName-error" class="error-message" aria-live="polite"></div>
    </div>
    
    <div class="form-group">
      <label for="lastName">姓氏 <span class="required">*</span></label>
      <input 
        type="text" 
        id="lastName" 
        name="lastName" 
        required 
        aria-describedby="lastName-error"
        autocomplete="family-name"
      >
      <div id="lastName-error" class="error-message" aria-live="polite"></div>
    </div>
  </div>
  
  <div class="form-group">
    <label for="email">電子郵件 <span class="required">*</span></label>
    <input 
      type="email" 
      id="email" 
      name="email" 
      required 
      aria-describedby="email-error email-help"
      autocomplete="email"
    >
    <div id="email-help" class="form-help">我們不會將您的郵件地址分享給第三方</div>
    <div id="email-error" class="error-message" aria-live="polite"></div>
  </div>
  
  <div class="form-group">
    <label for="subject">主旨 <span class="required">*</span></label>
    <select id="subject" name="subject" required aria-describedby="subject-error">
      <option value="">請選擇主旨</option>
      <option value="general">一般詢問</option>
      <option value="support">技術支援</option>
      <option value="sales">銷售諮詢</option>
      <option value="partnership">合作提案</option>
    </select>
    <div id="subject-error" class="error-message" aria-live="polite"></div>
  </div>
  
  <div class="form-group">
    <label for="message">訊息 <span class="required">*</span></label>
    <textarea 
      id="message" 
      name="message" 
      rows="5" 
      required 
      aria-describedby="message-error message-counter"
      maxlength="500"
    ></textarea>
    <div id="message-counter" class="character-counter">0/500 字元</div>
    <div id="message-error" class="error-message" aria-live="polite"></div>
  </div>
  
  <div class="form-group">
    <div class="checkbox-group">
      <input type="checkbox" id="newsletter" name="newsletter" value="yes">
      <label for="newsletter">我想訂閱電子報</label>
    </div>
  </div>
  
  <div class="form-actions">
    <button type="submit" class="btn btn--primary">
      <span class="btn-text">送出訊息</span>
      <span class="btn-loading" hidden>
        <span class="spinner"></span>
        處理中...
      </span>
    </button>
  </div>
  
  <div class="form-success" hidden>
    <h3>訊息發送成功！</h3>
    <p>感謝您的來信，我們會盡快回覆您。</p>
  </div>
</form>
```

---

## 13. 結語

### 13.1 專案標準的重要性

遵循本手冊中的規範和最佳實務，將為團隊帶來：

- **一致性**：統一的編碼風格讓團隊協作更順暢
- **可維護性**：良好的程式碼結構便於後續維護
- **效能**：正確的 HTML 和 CSS 提升網站效能
- **可及性**：語意化標籤讓網站對所有使用者友善
- **SEO 友好**：結構化內容有助於搜尋引擎優化

### 13.2 持續學習與改進

建議團隊成員：

1. 關注最新的 Web 標準和最佳實務
2. 在小型專案中嘗試新技術
3. 定期進行代碼審查和技術分享
4. 收集使用者回饋並持續改進

### 13.3 團隊協作

- 建立共同的樣式指南和組件庫
- 定期舉辦技術分享會議
- 維護和更新開發文件
- 使用自動化工具檢查代碼品質

---

## 14. 檢查清單

### 14.1 HTML 開發檢查清單

#### 基本結構
- [ ] 使用正確的 `<!DOCTYPE html>` 宣告
- [ ] 設定適當的 `lang` 屬性
- [ ] 包含必要的 meta 標籤
- [ ] 頁面標題具有描述性且獨特
- [ ] 正確使用語意化標籤

#### 內容品質
- [ ] 每頁只有一個 `<h1>` 標籤
- [ ] 標題階層合理且不跳級
- [ ] 所有圖片都有有意義的 `alt` 屬性
- [ ] 表單欄位都有對應的 `<label>`
- [ ] 連結文字具有描述性

#### 可及性
- [ ] 互動元素有適當的 focus 樣式
- [ ] 使用適當的 ARIA 標籤
- [ ] 顏色對比度符合標準
- [ ] 支援鍵盤導航

#### 效能
- [ ] 圖片使用適當格式
- [ ] 實施圖片延遲載入
- [ ] 使用 `preload` 載入關鍵資源
- [ ] JavaScript 使用 `defer` 或 `async`

### 14.2 CSS 開發檢查清單

#### 組織與結構
- [ ] 使用一致的命名規則（BEM）
- [ ] CSS 檔案組織良好
- [ ] 使用 CSS 自訂屬性
- [ ] 避免過度具體的選擇器

#### 響應式設計
- [ ] 採用 Mobile First 設計
- [ ] 使用相對單位
- [ ] 實施適當的斷點
- [ ] 測試各種螢幕尺寸

#### 現代 CSS
- [ ] 使用 Flexbox 或 Grid 佈局
- [ ] 使用現代選擇器
- [ ] 考慮容器查詢的使用

#### 效能優化
- [ ] 避免昂貴的選擇器
- [ ] 使用 `will-change` 優化動畫
- [ ] 壓縮 CSS 檔案
- [ ] 移除未使用的 CSS

### 14.3 跨瀏覽器相容性檢查清單

#### 測試環境
- [ ] Chrome（最新版本）
- [ ] Firefox（最新版本）
- [ ] Safari（最新版本）
- [ ] Edge（最新版本）
- [ ] 行動裝置瀏覽器

#### 功能測試
- [ ] 基本佈局正常顯示
- [ ] 互動功能正常運作
- [ ] 表單功能完整
- [ ] 媒體播放功能
- [ ] 動畫效果流暢

#### 回退方案
- [ ] 為新 CSS 特性提供回退
- [ ] 使用 `@supports` 檢測功能
- [ ] 漸進增強策略

### 14.4 部署前最終檢查

#### 代碼品質
- [ ] HTML 通過驗證器檢驗
- [ ] CSS 通過驗證器檢驗
- [ ] JavaScript 沒有控制台錯誤
- [ ] 所有連結正常運作

#### 內容檢查
- [ ] 文字內容正確無誤
- [ ] 圖片正常顯示且有 alt 屬性
- [ ] 聯絡資訊正確
- [ ] 版權資訊更新

#### SEO 優化
- [ ] 每頁都有唯一的 title 和 description
- [ ] 使用適當的標題結構
- [ ] 實施結構化資料
- [ ] 設定 robots.txt 和 sitemap

#### 安全性
- [ ] 實施 HTTPS
- [ ] 設定適當的 CSP 標頭
- [ ] 表單有適當的驗證
- [ ] 沒有敏感資料暴露

---

**記住**：這份檢查清單應該根據專案需求調整，並定期更新以反映最新的最佳實務。

---

*最後更新：2025年8月*  
*版本：2.0*  
*維護者：前端開發團隊*

### 附錄

#### A. 實用資源連結

- [W3C HTML5 規範](https://www.w3.org/TR/html52/)
- [W3C CSS3 規範](https://www.w3.org/Style/CSS/)
- [MDN Web 文件](https://developer.mozilla.org/)
- [Can I Use](https://caniuse.com/) - 瀏覽器支援查詢
- [HTML5 驗證器](https://validator.w3.org/)
- [CSS 驗證器](https://jigsaw.w3.org/css-validator/)
- [WebAIM](https://webaim.org/) - 無障礙資源
- [WCAG 指南](https://www.w3.org/WAI/WCAG21/quickref/)

#### B. 開發工具推薦

**線上工具**：
- CodePen - 線上程式碼測試
- Figma - UI/UX 設計
- Lighthouse - 效能分析
- PageSpeed Insights - 頁面速度測試

**瀏覽器擴充套件**：
- Web Developer - 開發者工具
- WAVE - 無障礙檢測
- ColorZilla - 顏色工具
- Responsive Viewer - 多螢幕預覽

#### C. 學習路徑建議

1. **基礎階段**（1-2個月）
   - HTML5 語意化標籤
   - CSS3 基本樣式
   - Flexbox 佈局
   - 響應式設計基礎

2. **進階階段**（2-3個月）
   - CSS Grid 佈局
   - CSS 動畫與轉場
   - JavaScript 整合
   - 效能優化技巧

3. **專精階段**（3-6個月）
   - 無障礙設計
   - 進階 CSS 技術
   - 前端自動化工具
   - 團隊協作流程

