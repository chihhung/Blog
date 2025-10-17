# Google Analytics 設定指南

## 📊 如何追蹤網站訪客

這個文件說明如何在您的 Hugo 部落格中設定 Google Analytics 4。

## 步驟 1: 建立 Google Analytics 帳戶

### 1.1 前往 Google Analytics
1. 訪問 https://analytics.google.com/
2. 使用您的 Google 帳戶登入
3. 點選 "開始測量" 或 "管理" → "建立帳戶"

### 1.2 設定帳戶資訊
- **帳戶名稱**: 我的部落格 (或任何您喜歡的名稱)
- **資源名稱**: chihhung.github.io/Blog
- **時區**: 台灣 (GMT+8)
- **貨幣**: 新台幣 (TWD)

### 1.3 選擇平台
- 選擇 **"網站"**
- 輸入網站 URL: `https://chihhung.github.io/Blog/`
- 輸入串流名稱: 我的部落格

### 1.4 取得測量 ID
完成設定後,您會看到一個測量 ID,格式類似:
```
G-XXXXXXXXXX
```
請複製這個 ID。

## 步驟 2: 在 Hugo 中設定

### 2.1 更新 hugo.toml
已經為您添加了設定,只需要更新測量 ID:

```toml
# 將 G-XXXXXXXXXX 替換為您實際的測量 ID
googleAnalytics = "G-XXXXXXXXXX"
```

### 2.2 範例設定
```toml
baseURL = 'https://chihhung.github.io/Blog/'
languageCode = 'zh-TW'
title = '我的個人部落格'
theme = 'PaperMod'

# Google Analytics 設定
googleAnalytics = "G-ABC123XYZ4"  # ← 替換成您的 ID
```

## 步驟 3: 部署並測試

### 3.1 提交變更
```bash
git add hugo.toml
git commit -m "feat: 添加 Google Analytics 追蹤"
git push
```

### 3.2 測試追蹤是否正常
1. 等待 GitHub Actions 部署完成 (約 1-3 分鐘)
2. 訪問您的網站: https://chihhung.github.io/Blog/
3. 開啟瀏覽器開發者工具 (F12)
4. 切換到 "Network" 標籤
5. 重新整理頁面
6. 搜尋 "google-analytics" 或 "analytics.js"
7. 如果看到相關請求,表示設定成功

### 3.3 在 Google Analytics 中確認
1. 回到 Google Analytics 控制台
2. 選擇 "即時" → "總覽"
3. 開啟您的網站
4. 幾秒鐘後應該會看到您的訪問記錄

## 📈 可以追蹤的數據

設定完成後,您可以在 Google Analytics 中看到:

### 即時數據
- 📍 目前有多少人在線上
- 🌍 訪客來自哪些國家/城市
- 📱 使用什麼裝置 (電腦/手機/平板)
- 📄 正在瀏覽哪些頁面

### 歷史數據
- 📊 每日/每週/每月訪客數
- 📈 頁面瀏覽量
- ⏱️ 平均停留時間
- 🔄 跳出率
- 🎯 最受歡迎的文章
- 🔍 訪客從哪裡來 (搜尋引擎、社群媒體、直接訪問)

### 使用者行為
- 🖱️ 點擊行為
- 📱 裝置類型分布
- 🌐 瀏覽器類型
- 🗺️ 地理位置分布

## 🎯 進階功能

### 設定事件追蹤
您可以追蹤特定的使用者互動,例如:
- 點擊外部連結
- 下載檔案
- 觀看影片
- 提交表單

### 設定轉換目標
定義重要的使用者行為,例如:
- 閱讀特定文章
- 瀏覽超過 3 頁
- 停留超過 2 分鐘

### 建立自訂報表
根據您的需求建立專屬報表。

## 🔒 隱私權注意事項

### 遵守 GDPR/個資法
如果您的網站有歐盟訪客,建議:
1. 添加 Cookie 同意橫幅
2. 在隱私權政策中說明使用 Google Analytics
3. 啟用 IP 匿名化 (GA4 預設已啟用)

### 建議添加隱私權政策
在 `content/privacy.md` 建立隱私權政策頁面。

## 📚 其他分析工具選項

除了 Google Analytics,您也可以考慮:

### 1. Plausible Analytics
- 開源、注重隱私
- 不使用 Cookie
- 簡單易用
- 付費服務

### 2. Umami
- 開源、自架
- 注重隱私
- 簡潔的介面
- 免費 (需自己架設)

### 3. GoatCounter
- 開源
- 注重隱私
- 簡單輕量
- 免費選項

### 4. Cloudflare Web Analytics
- 免費
- 注重隱私
- 整合 Cloudflare CDN

## 🆘 常見問題

### Q: 為什麼看不到數據?
A: 
- 確認測量 ID 正確
- 等待 24-48 小時讓數據累積
- 檢查瀏覽器是否封鎖追蹤器
- 確認網站已部署最新版本

### Q: 數據會立即顯示嗎?
A: 
- 即時報表會在幾秒內顯示
- 標準報表可能需要 24-48 小時

### Q: 會影響網站速度嗎?
A: 
- Google Analytics 是異步載入的
- 對速度影響很小
- 如果擔心,可以考慮其他輕量級方案

### Q: 需要付費嗎?
A: 
- Google Analytics 4 完全免費
- 適合個人部落格和中小型網站

## 📞 需要協助?

如果您在設定過程中遇到問題,可以:
1. 查看 Google Analytics 說明中心
2. 參考 Hugo 官方文檔
3. 在 GitHub 上開 Issue

---

**最後更新**: 2025年10月17日
