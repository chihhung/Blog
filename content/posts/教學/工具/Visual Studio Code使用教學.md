+++
date = '2025-10-31T00:00:00+08:00'
draft = false
title = 'Visual Studio Code使用教學'
tags = ['教學', '工具']
categories = ['教學']
+++
# Visual Studio Code 使用教學手冊

> **完整的 VS Code 開發環境設定與實戰指南**  
> 涵蓋前端 (Vue 3 + TypeScript) 與後端 (Spring Boot) 開發，適用於團隊協作與企業級專案開發

## 📋 目錄

### 1. VS Code 安裝與環境設定
- [1.1 安裝步驟](#11-安裝步驟)
- [1.2 推薦字型與主題](#12-推薦字型與主題)
- [1.3 專案必要的 Extensions 清單](#13-專案必要的-extensions-清單)
- [1.4 設定同步功能](#14-設定同步功能)
- [1.5 實務案例與注意事項](#15-實務案例與注意事項)

### 2. 專案開發環境配置
- [2.1 如何開啟專案](#21-如何開啟專案)
- [2.2 前端、後端工作區設定](#22-前端後端工作區設定-workspace-settings)
- [2.3 編碼規範設定](#23-編碼規範設定)
  - [2.3.1 前端編碼規範 (ESLint + Prettier)](#231-前端編碼規範-eslint--prettier)
  - [2.3.2 後端編碼規範 (Checkstyle)](#232-後端編碼規範-checkstyle)
  - [2.3.3 Maven 獨立安裝設定](#233-maven-獨立安裝設定)
- [2.4 容器化開發環境 (Dev Containers)](#24-容器化開發環境-dev-containers)
- [2.5 實務案例與注意事項](#25-實務案例與注意事項)

### 3. 日常開發操作
- [3.1 Git 與 GitHub/GitLab 整合](#31-git-與-githubgitlab-整合)
- [3.2 常用快捷鍵](#32-常用快捷鍵)
- [3.3 偵錯與斷點設定](#33-偵錯-debugging-與斷點設定)
- [3.4 終端機與多工作區使用](#34-終端機與多工作區使用)
- [3.5 程式碼片段 (Snippets) 使用](#35-程式碼片段-snippets-使用)
- [3.6 實務案例與注意事項](#36-實務案例與注意事項)

### 4. 專案特定開發流程指引
- [4.1 前端開發流程](#41-前端開發流程-vue-3--typescript)
- [4.2 後端開發流程](#42-後端開發流程-spring-boot)
- [4.3 全端開發工作流程](#43-全端開發工作流程)
- [4.4 程式碼品質檢查](#44-程式碼品質檢查)
- [4.5 Python 開發環境設定](#45-python-開發環境設定)
  - [4.5.1 Python 專案結構](#451-python-專案結構)
  - [4.5.2 Python 環境設定](#452-python-環境設定)
  - [4.5.3 Python 開發工具設定](#453-python-開發工具設定)
  - [4.5.4 Python 偵錯設定](#454-python-偵錯設定)
  - [4.5.5 Python 任務設定](#455-python-任務設定)
  - [4.5.6 Python 專案範例](#456-python-專案範例)
  - [4.5.7 Python 開發最佳實務](#457-python-開發最佳實務)
- [4.6 效能監控與分析](#46-效能監控與分析)
- [4.7 實務案例與注意事項](#47-實務案例與注意事項)

### 5. 協作開發功能
- [5.1 Live Share 即時協作](#51-live-share-即時協作)
- [5.2 多人開發設定](#52-多人開發設定)
- [5.3 程式碼審查工具](#53-程式碼審查工具)
  - [5.3.1 GitHub Pull Request 整合](#531-github-pull-request-整合)
  - [5.3.2 GitLab Merge Request 整合](#532-gitlab-merge-request-整合)
  - [5.3.3 程式碼審查檢查清單](#533-程式碼審查檢查清單)
- [5.4 團隊協作最佳實務](#54-團隊協作最佳實務)

### 6. 進階功能與擴充
- [6.1 自訂程式碼片段](#61-自訂程式碼片段)
- [6.2 擴充功能開發入門](#62-擴充功能開發入門)
- [6.3 工作流程自動化](#63-工作流程自動化)
  - [6.3.1 Task 自動化](#631-task-自動化)
  - [6.3.2 GitHub Actions 整合](#632-github-actions-整合)
  - [6.3.3 GitLab CI/CD 整合](#633-gitlab-cicd-整合)
- [6.4 效能優化進階技巧](#64-效能優化進階技巧)
- [6.5 遠端開發與 SSH](#65-遠端開發與-ssh)
- [6.6 工作區管理進階技巧](#66-工作區管理進階技巧)

### 7. 最佳實務
- [7.1 常見問題 (FAQ) 與解決方式](#71-常見問題-faq-與解決方式)
- [7.2 建議的工作習慣](#72-建議的工作習慣)
- [7.3 效能最佳化](#73-效能最佳化)
- [7.4 安全性最佳實務](#74-安全性最佳實務)
- [7.5 團隊協作規範](#75-團隊協作規範)

### 8. 檢查清單
- [8.1 新進成員快速上手檢查清單](#81-新進成員快速上手檢查清單)
- [8.2 日常開發檢查清單](#82-日常開發檢查清單)
- [8.3 部署前檢查清單](#83-部署前檢查清單)
- [8.4 故障排除檢查清單](#84-故障排除檢查清單)

### 9. 附錄
- [9.1 參考資源](#91-參考資源)
- [9.2 聯絡支援](#92-聯絡支援)

---

## 1. VS Code 安裝與環境設定

### 1.1 安裝步驟

#### 1.1.1 下載與安裝
1. 前往 [Visual Studio Code 官方網站](https://code.visualstudio.com/)
2. 點擊 "Download for Windows" 下載安裝檔
3. 執行安裝檔，建議勾選以下選項：
   - ✅ 新增至 PATH (在重新啟動後可用)
   - ✅ 在檔案總管中的檔案上顯示「使用 Code 開啟」動作
   - ✅ 在檔案總管中的目錄上顯示「使用 Code 開啟」動作
   - ✅ 將 Code 註冊為支援的檔案類型的編輯器

#### 1.1.2 首次啟動設定
1. 啟動 VS Code
2. 選擇適合的色彩主題
3. 登入 Microsoft 帳戶（可選，用於同步設定）

### 1.2 推薦字型與主題

#### 1.2.1 推薦字型
建議安裝並使用以下等寬字型：

**主要推薦：**
- **JetBrains Mono** - 專為程式設計設計，支援連字符
- **Fira Code** - 支援程式設計連字符，提升程式碼可讀性
- **Cascadia Code** - Microsoft 開發的程式設計字型

**安裝步驟：**
1. 下載字型檔案（.ttf 或 .otf）
2. 右鍵點擊字型檔案 → 選擇「安裝」
3. 在 VS Code 中設定字型

**VS Code 字型設定：**
```json
{
    "editor.fontFamily": "'JetBrains Mono', 'Fira Code', Consolas, monospace",
    "editor.fontLigatures": true,
    "editor.fontSize": 14,
    "editor.fontWeight": "400"
}
```

#### 1.2.2 推薦主題
根據不同喜好推薦以下主題：

**暗色主題：**
- **One Dark Pro** - 基於 Atom 的流行暗色主題
- **Material Theme** - Google Material Design 風格
- **Dracula Official** - 高對比度暗色主題

**亮色主題：**
- **Light+ (default light)** - VS Code 預設亮色主題
- **Material Theme Lighter** - Material Design 亮色版本

**安裝主題步驟：**
1. 按 `Ctrl + Shift + X` 開啟擴充功能面板
2. 搜尋主題名稱
3. 點擊「Install」安裝
4. 按 `Ctrl + K, Ctrl + T` 選擇主題

### 1.3 專案必要的 Extensions 清單

#### 1.3.1 基礎開發工具

**必裝擴充功能：**

| 擴充功能名稱 | 用途 | 安裝指令 |
|------------|------|---------|
| **Chinese (Traditional) Language Pack** | 繁體中文語言包 | `ext install MS-CEINTL.vscode-language-pack-zh-hant` |
| **GitLens** | Git 進階功能增強 | `ext install eamodio.gitlens` |
| **GitHub Pull Requests and Issues** | GitHub 整合 | `ext install GitHub.vscode-pull-request-github` |
| **GitLab Workflow** | GitLab 整合 | `ext install gitlab.gitlab-workflow` |
| **Auto Rename Tag** | HTML/XML 標籤自動重新命名 | `ext install formulahendry.auto-rename-tag` |
| **Bracket Pair Colorizer 2** | 括號配對色彩化 | `ext install CoenraadS.bracket-pair-colorizer-2` |
| **indent-rainbow** | 縮排色彩化 | `ext install oderwat.indent-rainbow` |
| **Path Intellisense** | 路徑自動完成 | `ext install christian-kohler.path-intellisense` |

#### 1.3.2 前端開發 (Vue 3 + TypeScript)

| 擴充功能名稱 | 用途 | 安裝指令 |
|------------|------|---------|
| **Vetur** 或 **Volar** | Vue.js 語言支援 | `ext install Vue.volar` |
| **TypeScript Importer** | TypeScript 自動匯入 | `ext install pmneo.tsimporter` |
| **ESLint** | JavaScript/TypeScript 程式碼檢查 | `ext install dbaeumer.vscode-eslint` |
| **Prettier** | 程式碼格式化工具 | `ext install esbenp.prettier-vscode` |
| **Tailwind CSS IntelliSense** | Tailwind CSS 自動完成 | `ext install bradlc.vscode-tailwindcss` |
| **Auto Close Tag** | HTML 標籤自動閉合 | `ext install formulahendry.auto-close-tag` |
| **HTML CSS Support** | HTML 中的 CSS 支援 | `ext install ecmel.vscode-html-css` |

#### 1.3.3 後端開發 (Java + Spring Boot)

| 擴充功能名稱 | 用途 | 安裝指令 |
|------------|------|---------|
| **Extension Pack for Java** | Java 開發工具包 | `ext install vscjava.vscode-java-pack` |
| **Spring Boot Extension Pack** | Spring Boot 開發工具包 | `ext install Pivotal.vscode-boot-dev-pack` |
| **Maven for Java** | Maven 專案管理 | `ext install vscjava.vscode-maven` |
| **Checkstyle for Java** | Java 程式碼風格檢查 | `ext install shengchen.vscode-checkstyle` |
| **SonarLint** | 程式碼品質分析 | `ext install SonarSource.sonarlint-vscode` |

#### 1.3.4 Python 開發

| 擴充功能名稱 | 用途 | 安裝指令 |
|------------|------|---------|
| **Python** | Python 官方開發工具 | `ext install ms-python.python` |
| **Pylint** | Python 程式碼檢查 | `ext install ms-python.flake8` |
| **Python Docstring Generator** | 自動產生文檔字串 | `ext install njpwerner.autodocstring` |
| **Jupyter** | Jupyter Notebook 支援 | `ext install ms-toolsai.jupyter` |
| **Python Type Hint** | 型別提示支援 | `ext install ms-python.vscode-pylance` |
| **autoDocstring** | 自動文檔生成 | `ext install njpwerner.autodocstring` |
| **Python Test Explorer** | 測試執行器 | `ext install LittleFoxTeam.vscode-python-test-adapter` |

#### 1.3.5 一鍵安裝指令
在 VS Code 終端機中執行以下指令快速安裝所有推薦擴充功能：

```powershell
# 基礎工具
code --install-extension MS-CEINTL.vscode-language-pack-zh-hant
code --install-extension eamodio.gitlens
code --install-extension GitHub.vscode-pull-request-github
code --install-extension gitlab.gitlab-workflow
code --install-extension formulahendry.auto-rename-tag
code --install-extension CoenraadS.bracket-pair-colorizer-2
code --install-extension oderwat.indent-rainbow
code --install-extension christian-kohler.path-intellisense

# 前端開發
code --install-extension Vue.volar
code --install-extension pmneo.tsimporter
code --install-extension dbaeumer.vscode-eslint
code --install-extension esbenp.prettier-vscode
code --install-extension bradlc.vscode-tailwindcss
code --install-extension formulahendry.auto-close-tag
code --install-extension ecmel.vscode-html-css

# 後端開發
code --install-extension vscjava.vscode-java-pack
code --install-extension Pivotal.vscode-boot-dev-pack
code --install-extension vscjava.vscode-maven
code --install-extension shengchen.vscode-checkstyle
code --install-extension SonarSource.sonarlint-vscode

# Python 開發
code --install-extension ms-python.python
code --install-extension ms-python.flake8
code --install-extension njpwerner.autodocstring
code --install-extension ms-toolsai.jupyter
code --install-extension ms-python.vscode-pylance
code --install-extension LittleFoxTeam.vscode-python-test-adapter
```

### 1.4 設定同步功能

#### 1.4.1 啟用設定同步

VS Code 提供設定同步功能，讓您在不同設備間保持一致的開發環境。

**啟用步驟：**
1. 按 `Ctrl + Shift + P` 開啟命令面板
2. 輸入 `Settings Sync: Turn On`
3. 選擇要同步的項目：
   - ✅ 設定 (Settings)
   - ✅ 快捷鍵綁定 (Keybindings)
   - ✅ 擴充功能 (Extensions)
   - ✅ 使用者程式碼片段 (User Snippets)
   - ✅ UI 狀態 (UI State)
4. 使用 Microsoft 或 GitHub 帳戶登入

#### 1.4.2 同步項目說明

**同步的內容包括：**
- **設定檔** - editor、theme、font 等個人偏好設定
- **擴充功能** - 已安裝的擴充功能清單
- **快捷鍵** - 自訂的快捷鍵綁定
- **程式碼片段** - 自訂的程式碼片段
- **UI 狀態** - 面板配置、視窗大小等

**不會同步的內容：**
- 工作區特定設定
- 本地檔案路徑
- 敏感資訊（如 tokens、密碼）

#### 1.4.3 管理同步設定

**查看同步狀態：**
- 點擊狀態列的同步圖示
- 或按 `Ctrl + Shift + P` → `Settings Sync: Show Settings`

**手動同步：**
```
Ctrl + Shift + P：
- Settings Sync: Sync Now
- Settings Sync: Download Settings
- Settings Sync: Upload Settings
```

**關閉同步：**
- `Ctrl + Shift + P` → `Settings Sync: Turn Off`

### 1.5 實務案例與注意事項

#### ⚠️ 注意事項
1. **效能考量**：不要安裝過多不必要的擴充功能，會影響 VS Code 啟動速度
2. **版本相容性**：定期更新擴充功能，確保與 VS Code 版本相容
3. **工作區設定**：某些擴充功能設定建議在工作區層級配置，避免影響其他專案

#### 💡 實務建議
- 使用 `Ctrl + Shift + P` 開啟命令面板，輸入 `Extensions: Show Recommended Extensions` 查看工作區推薦的擴充功能
- 定期執行 `Extensions: Update All Extensions` 更新所有擴充功能
- 使用設定同步功能，在不同設備間保持一致的開發環境

---

## 2. 專案開發環境配置

### 2.1 如何開啟專案

#### 2.1.1 開啟專案的方式

**方式一：透過檔案總管**
1. 在專案根目錄右鍵點擊
2. 選擇「使用 Code 開啟」

**方式二：透過 VS Code**
1. 啟動 VS Code
2. 按 `Ctrl + K, Ctrl + O` 或選擇 `File > Open Folder`
3. 選擇專案根目錄

**方式三：透過命令列**
```powershell
# 在專案根目錄執行
cd d:\developer\repos\your-project
code .
```

#### 2.1.2 專案結構確認
正確開啟專案後，應該看到以下結構：

```
your-project/
├── frontend/          # Vue 3 前端專案
│   ├── src/
│   ├── package.json
│   └── vite.config.ts
├── backend/           # Spring Boot 後端專案
│   ├── src/
│   ├── pom.xml
│   └── application.yml
├── .vscode/           # VS Code 工作區設定
├── README.md
└── .gitignore
```

### 2.2 前端、後端工作區設定 (Workspace Settings)

#### 2.2.1 建立工作區設定檔

在專案根目錄建立 `.vscode` 資料夾，並創建以下設定檔：

**`.vscode/settings.json`** - 工作區設定
```json
{
  // 編輯器設定
  "editor.tabSize": 2,
  "editor.insertSpaces": true,
  "editor.formatOnSave": true,
  "editor.formatOnPaste": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true,
    "source.organizeImports": true
  },
  
  // 檔案設定
  "files.autoSave": "onFocusChange",
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true,
  "files.exclude": {
    "**/node_modules": true,
    "**/target": true,
    "**/.git": true,
    "**/.DS_Store": true
  },
  
  // 前端專案設定
  "[vue]": {
    "editor.defaultFormatter": "Vue.volar"
  },
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[json]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[html]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[css]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  
  // 後端專案設定
  "[java]": {
    "editor.defaultFormatter": "redhat.java",
    "editor.tabSize": 4
  },
  "[xml]": {
    "editor.defaultFormatter": "redhat.vscode-xml"
  },
  "[yaml]": {
    "editor.defaultFormatter": "redhat.vscode-yaml"
  },
  
  // Java 相關設定
  "java.configuration.updateBuildConfiguration": "automatic",
  "java.compile.nullAnalysis.mode": "automatic",
  "java.format.settings.url": ".vscode/eclipse-formatter.xml",
  "java.checkstyle.configuration": ".vscode/checkstyle.xml",
  
  // Maven 相關設定 (獨立安裝)
  "maven.executable.path": "D:\\apache-maven-3.9.4\\bin\\mvn.cmd",
  "maven.terminal.useJavaHome": true,
  "maven.terminal.customEnv": [
    {
      "environmentVariable": "JAVA_HOME",
      "value": "C:\\Program Files\\Java\\jdk-17"
    },
    {
      "environmentVariable": "M2_HOME", 
      "value": "D:\\apache-maven-3.9.4"
    }
  ],
  "maven.view": "hierarchical",
  "maven.pomfile.autoUpdateEffectivePOM": true,
  "maven.pomfile.globalSettings": "D:\\apache-maven-3.9.4\\conf\\settings.xml",
  "maven.pomfile.userSettings": "${env:USERPROFILE}\\.m2\\settings.xml",
  "maven.offline": false,
  "maven.updateSnapshots": false,
  "maven.showDependencies": "all",
  
  // Python 相關設定
  "python.defaultInterpreterPath": "python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.linting.flake8Enabled": true,
  "python.linting.lintOnSave": true,
  "python.formatting.provider": "black",
  "python.formatting.blackArgs": ["--line-length", "88"],
  "python.sortImports.args": ["--profile", "black"],
  "python.analysis.typeCheckingMode": "basic",
  "python.analysis.autoImportCompletions": true,
  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": false,
  "python.testing.nosetestsEnabled": false,
  "jupyter.askForKernelRestart": false,
  "jupyter.alwaysTrustNotebooks": true,
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    },
    "editor.tabSize": 4
  },
  
  // ESLint 設定
  "eslint.workingDirectories": ["frontend"],
  "eslint.validate": [
    "javascript",
    "typescript",
    "vue"
  ],
  
  // Prettier 設定
  "prettier.configPath": "frontend/.prettierrc",
  
  // 搜尋設定
  "search.exclude": {
    "**/node_modules": true,
    "**/target": true,
    "**/dist": true,
    "**/.git": true
  }
}
```

**`.vscode/extensions.json`** - 推薦擴充功能
```json
{
  "recommendations": [
    // 基礎工具
    "ms-ceintl.vscode-language-pack-zh-hant",
    "eamodio.gitlens",
    "formulahendry.auto-rename-tag",
    "coenraads.bracket-pair-colorizer-2",
    "oderwat.indent-rainbow",
    "christian-kohler.path-intellisense",
    
    // 前端開發
    "vue.volar",
    "pmneo.tsimporter",
    "dbaeumer.vscode-eslint",
    "esbenp.prettier-vscode",
    "bradlc.vscode-tailwindcss",
    "formulahendry.auto-close-tag",
    "ecmel.vscode-html-css",
    
    // 後端開發
    "vscjava.vscode-java-pack",
    "pivotal.vscode-boot-dev-pack",
    "vscjava.vscode-maven",
    "shengchen.vscode-checkstyle",
    "sonarsource.sonarlint-vscode"
  ]
}
```

**`.vscode/launch.json`** - 偵錯設定
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Launch Vue App",
      "type": "node",
      "request": "launch",
      "cwd": "${workspaceFolder}/frontend",
      "runtimeExecutable": "npm",
      "runtimeArgs": ["run", "dev"]
    },
    {
      "name": "Launch Spring Boot",
      "type": "java",
      "request": "launch",
      "mainClass": "com.yourcompany.Application",
      "projectName": "your-backend-project",
      "args": "--spring.profiles.active=dev"
    },
    {
      "name": "Debug Vue Tests",
      "type": "node",
      "request": "launch",
      "cwd": "${workspaceFolder}/frontend",
      "runtimeExecutable": "npm",
      "runtimeArgs": ["run", "test:debug"]
    },
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": true
    },
    {
      "name": "Python: FastAPI",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/src/main.py",
      "console": "integratedTerminal",
      "args": ["--reload"]
    },
    {
      "name": "Python: Flask",
      "type": "python",
      "request": "launch",
      "module": "flask",
      "env": {
        "FLASK_APP": "app.py",
        "FLASK_ENV": "development"
      },
      "args": ["run", "--host=0.0.0.0", "--port=5000"],
      "jinja": true,
      "justMyCode": true
    },
    {
      "name": "Python: Django",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/manage.py",
      "args": ["runserver"],
      "console": "integratedTerminal",
      "justMyCode": true
    }
  ]
}
```

**`.vscode/tasks.json`** - 任務設定
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Frontend: Install Dependencies",
      "type": "shell",
      "command": "npm",
      "args": ["install"],
      "options": {
        "cwd": "${workspaceFolder}/frontend"
      },
      "group": "build",
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared"
      }
    },
    {
      "label": "Frontend: Dev Server",
      "type": "shell",
      "command": "npm",
      "args": ["run", "dev"],
      "options": {
        "cwd": "${workspaceFolder}/frontend"
      },
      "group": "build",
      "isBackground": true,
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "new"
      }
    },
    {
      "label": "Frontend: Build",
      "type": "shell",
      "command": "npm",
      "args": ["run", "build"],
      "options": {
        "cwd": "${workspaceFolder}/frontend"
      },
      "group": "build"
    },
    {
      "label": "Frontend: Test",
      "type": "shell",
      "command": "npm",
      "args": ["run", "test"],
      "options": {
        "cwd": "${workspaceFolder}/frontend"
      },
      "group": "test"
    },
    {
      "label": "Backend: Maven Clean Install",
      "type": "shell",
      "command": "mvn",
      "args": ["clean", "install"],
      "options": {
        "cwd": "${workspaceFolder}/backend"
      },
      "group": "build"
    },
    {
      "label": "Backend: Maven Spring Boot Run",
      "type": "shell",
      "command": "mvn",
      "args": ["spring-boot:run"],
      "options": {
        "cwd": "${workspaceFolder}/backend"
      },
      "group": "build",
      "isBackground": true
    },
    {
      "label": "Backend: Maven Test",
      "type": "shell",
      "command": "mvn",
      "args": ["test"],
      "options": {
        "cwd": "${workspaceFolder}/backend"
      },
      "group": "test"
    }
  ]
}
```

### 2.3 編碼規範設定

#### 2.3.1 前端編碼規範 (ESLint + Prettier)

**frontend/.eslintrc.js**
```javascript
module.exports = {
  env: {
    browser: true,
    es2021: true,
    node: true
  },
  extends: [
    'eslint:recommended',
    '@typescript-eslint/recommended',
    '@vue/typescript/recommended',
    'prettier'
  ],
  parser: 'vue-eslint-parser',
  parserOptions: {
    ecmaVersion: 2021,
    parser: '@typescript-eslint/parser',
    sourceType: 'module'
  },
  plugins: [
    '@typescript-eslint',
    'vue'
  ],
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    '@typescript-eslint/no-unused-vars': 'error',
    'vue/multi-word-component-names': 'off',
    'vue/no-v-html': 'warn'
  }
}
```

**frontend/.prettierrc**
```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 80,
  "tabWidth": 2,
  "useTabs": false,
  "endOfLine": "lf"
}
```

#### 2.3.2 後端編碼規範 (Checkstyle)

**backend/.vscode/checkstyle.xml**
```xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
    "https://checkstyle.org/dtds/configuration_1_3.dtd">
<module name="Checker">
  <property name="charset" value="UTF-8"/>
  <property name="severity" value="warning"/>
  
  <module name="TreeWalker">
    <!-- 命名規則 -->
    <module name="TypeName"/>
    <module name="MethodName"/>
    <module name="PackageName"/>
    <module name="ParameterName"/>
    <module name="LocalVariableName"/>
    
    <!-- 程式碼風格 -->
    <module name="LineLength">
      <property name="max" value="120"/>
    </module>
    <module name="Indentation">
      <property name="basicOffset" value="4"/>
    </module>
    
    <!-- 匯入規則 -->
    <module name="UnusedImports"/>
    <module name="RedundantImport"/>
    <module name="IllegalImport"/>
    
    <!-- 空白規則 -->
    <module name="WhitespaceAfter"/>
    <module name="WhitespaceAround"/>
  </module>
</module>
```

#### 2.3.3 Maven 獨立安裝設定

**安裝 Maven：**
1. 從 [Apache Maven 官網](https://maven.apache.org/download.cgi) 下載最新版本
2. 解壓縮到指定目錄，例如：`D:\apache-maven-3.9.4`
3. 設定系統環境變數：
   ```bash
   MAVEN_HOME=D:\apache-maven-3.9.4
   M2_HOME=D:\apache-maven-3.9.4
   PATH=%PATH%;%MAVEN_HOME%\bin
   ```

**VS Code Maven 設定：**
```json
// .vscode/settings.json
{
  // Maven 執行檔路徑設定
  "maven.executable.path": "D:\\apache-maven-3.9.4\\bin\\mvn.cmd",
  
  // 使用 JAVA_HOME 環境變數
  "maven.terminal.useJavaHome": true,
  
  // 自訂環境變數
  "maven.terminal.customEnv": [
    {
      "environmentVariable": "JAVA_HOME",
      "value": "C:\\Program Files\\Java\\jdk-17"
    },
    {
      "environmentVariable": "M2_HOME", 
      "value": "D:\\apache-maven-3.9.4"
    },
    {
      "environmentVariable": "MAVEN_OPTS",
      "value": "-Xmx1024m -XX:MaxPermSize=256m"
    }
  ],
  
  // Maven 檢視設定
  "maven.view": "hierarchical",
  "maven.pomfile.autoUpdateEffectivePOM": true,
  
  // Maven 設定檔路徑
  "maven.pomfile.globalSettings": "D:\\apache-maven-3.9.4\\conf\\settings.xml",
  "maven.pomfile.userSettings": "${env:USERPROFILE}\\.m2\\settings.xml",
  
  // Maven 操作設定
  "maven.offline": false,
  "maven.updateSnapshots": false,
  "maven.showDependencies": "all",
  "maven.excludedFolders": [
    "**/.*",
    "**/node_modules",
    "**/target",
    "**/bin",
    "**/archetype-resources"
  ],
  
  // Maven 編譯設定
  "maven.runtime.settings": "${env:USERPROFILE}\\.m2\\settings.xml",
  "maven.multiModuleProjectDirectory": "${workspaceFolder}",
  "maven.projectOpenBehavior": "Interactive"
}
```

**Maven 專案任務設定：**
```json
// .vscode/tasks.json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Maven: Clean",
      "type": "shell",
      "command": "${config:maven.executable.path}",
      "args": ["clean"],
      "group": "build",
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared"
      },
      "problemMatcher": []
    },
    {
      "label": "Maven: Compile",
      "type": "shell",
      "command": "${config:maven.executable.path}",
      "args": ["compile"],
      "group": "build",
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared"
      },
      "problemMatcher": ["$maven-compiler-java"]
    },
    {
      "label": "Maven: Test",
      "type": "shell",
      "command": "${config:maven.executable.path}",
      "args": ["test"],
      "group": "test",
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared"
      },
      "problemMatcher": ["$maven-compiler-java"]
    },
    {
      "label": "Maven: Package",
      "type": "shell",
      "command": "${config:maven.executable.path}",
      "args": ["package", "-DskipTests"],
      "group": "build",
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared"
      },
      "problemMatcher": ["$maven-compiler-java"]
    },
    {
      "label": "Maven: Install",
      "type": "shell",
      "command": "${config:maven.executable.path}",
      "args": ["install"],
      "group": "build",
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared"
      },
      "problemMatcher": ["$maven-compiler-java"]
    },
    {
      "label": "Maven: Spring Boot Run",
      "type": "shell",
      "command": "${config:maven.executable.path}",
      "args": ["spring-boot:run"],
      "group": "build",
      "isBackground": true,
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared"
      },
      "problemMatcher": [
        {
          "pattern": [
            {
              "regexp": "\\b\\B",
              "file": 1,
              "location": 2,
              "message": 3
            }
          ],
          "background": {
            "activeOnStart": true,
            "beginsPattern": "^.*Restarting due to",
            "endsPattern": "^.*Started .* in .* seconds.*"
          }
        }
      ]
    }
  ]
}
```

**Maven Wrapper 設定 (推薦)：**
如果專案使用 Maven Wrapper，可以使用以下設定：
```json
// .vscode/settings.json
{
  "maven.executable.path": "${workspaceFolder}/mvnw.cmd",
  "maven.executable.preferMavenWrapper": true
}
```

**驗證 Maven 設定：**
1. 開啟 VS Code 命令面板：`Ctrl + Shift + P`
2. 執行：`Java: Reload Projects`
3. 檢查 Maven 擴充功能是否正常載入專案
4. 在終端執行：`mvn -version` 確認版本正確

### 2.4 容器化開發環境 (Dev Containers)

#### 2.4.1 Dev Containers 簡介

Dev Containers 讓團隊在一致的容器化環境中開發，確保 "在我的機器上可以運行" 的問題不再發生。

**優勢：**
- 統一的開發環境
- 快速環境建置
- 隔離的依賴管理
- 支援不同的技術堆疊

#### 2.4.2 設定 Dev Container

**1. 安裝必要擴充功能：**
```bash
code --install-extension ms-vscode-remote.remote-containers
```

**2. 建立 `.devcontainer` 資料夾：**
```
.devcontainer/
├── devcontainer.json
├── Dockerfile
└── docker-compose.yml
```

**3. 配置 `devcontainer.json`：**
```json
{
  "name": "Full Stack Development",
  "dockerComposeFile": "docker-compose.yml",
  "service": "app",
  "workspaceFolder": "/workspace",
  "shutdownAction": "stopCompose",
  
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-vscode.vscode-typescript-next",
        "vue.volar",
        "vscjava.vscode-java-pack",
        "pivotal.vscode-boot-dev-pack"
      ],
      "settings": {
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
          "source.fixAll.eslint": true
        }
      }
    }
  },
  
  "forwardPorts": [3000, 8080, 3306],
  "postCreateCommand": "npm install && mvn install"
}
```

**4. Docker Compose 設定：**
```yaml
version: '3.8'
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - ..:/workspace:cached
      - /var/run/docker.sock:/var/run/docker.sock
    ports:
      - "3000:3000"
      - "8080:8080"
    environment:
      - NODE_ENV=development
    depends_on:
      - database
  
  database:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: devdb
      MYSQL_USER: devuser
      MYSQL_PASSWORD: devpassword
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql

volumes:
  mysql_data:
```

#### 2.4.3 使用 Dev Container

**啟動 Dev Container：**
1. 按 `Ctrl + Shift + P`
2. 輸入 `Dev Containers: Reopen in Container`
3. 等待容器建置完成

**常用 Dev Container 指令：**
```
Ctrl + Shift + P：
- Dev Containers: Rebuild Container
- Dev Containers: Reopen Locally
- Dev Containers: Show Container Log
```

### 2.5 實務案例與注意事項

#### ⚠️ 注意事項
1. **設定檔版本控制**：將 `.vscode` 資料夾加入版本控制，確保團隊成員使用相同設定
2. **路徑設定**：確保所有路徑設定符合專案實際結構
3. **效能最佳化**：定期清理不必要的設定，避免影響 VS Code 效能

#### 💡 實務建議
- 使用 `Ctrl + Shift + P` 執行 `Developer: Reload Window` 重新載入設定
- 定期執行 `Preferences: Workspace Settings` 檢查設定是否正確
- 建議將常用任務加入 VS Code 的任務面板快速存取

---

## 3. 日常開發操作

### 3.1 Git 與 GitHub/GitLab 整合

#### 3.1.1 Git 基本操作

**透過 VS Code Git 面板操作：**

1. **查看變更檔案**
   - 按 `Ctrl + Shift + G` 開啟 Git 面板
   - 檢視 "Changes" 區段的修改檔案

2. **暫存變更**
   - 點擊檔案旁的 `+` 號暫存單一檔案
   - 點擊 "Changes" 旁的 `+` 暫存所有變更

3. **提交變更**
   - 在訊息框輸入提交訊息
   - 按 `Ctrl + Enter` 或點擊 ✓ 提交

4. **推送到遠端**
   - 點擊狀態列的同步按鈕
   - 或按 `Ctrl + Shift + P` → `Git: Push`

#### 3.1.2 GitLens 擴充功能使用

**主要功能：**

- **檔案歷史檢視**：點擊編輯器中的 GitLens 註解
- **比較變更**：右鍵檔案 → `Compare with Previous`
- **Blame 檢視**：查看每行程式碼的修改者和時間
- **分支檢視**：在側邊欄檢視所有分支和提交歷史

**常用 GitLens 指令：**
```
Ctrl + Shift + P：
- GitLens: Show File History
- GitLens: Compare with Previous
- GitLens: Show Line History
- GitLens: Toggle File Blame
```

#### 3.1.3 GitHub/GitLab 整合設定

**GitHub 整合：**
1. 安裝 "GitHub Pull Requests and Issues" 擴充功能
2. 按 `Ctrl + Shift + P` → `GitHub: Sign In`
3. 完成授權後即可在 VS Code 中：
   - 檢視和建立 Pull Request
   - 管理 Issues
   - 進行 Code Review

**常用 GitHub 操作：**
- `Ctrl + Shift + P` → `GitHub: Create Pull Request`
- 在 Explorer 面板中直接檢視 PR 狀態
- 在編輯器中直接回覆 PR 評論

**GitLab 整合：**
1. 安裝 "GitLab Workflow" 擴充功能：
   ```bash
   code --install-extension gitlab.gitlab-workflow
   ```

2. 設定 GitLab 存取權杖：
   - 前往 GitLab → User Settings → Access Tokens
   - 建立 Personal Access Token，權限包含：
     - `api` - 完整 API 存取
     - `read_user` - 讀取使用者資訊
     - `read_repository` - 讀取倉庫資訊

3. 在 VS Code 中設定 GitLab：
   ```json
   // settings.json
   {
     "gitlab.instanceUrl": "https://gitlab.yourcompany.com",
     "gitlab.personalAccessToken": "your-access-token",
     "gitlab.showPipelineUpdateNotifications": true,
     "gitlab.enableExperimentalFeatures": true
   }
   ```

**GitLab 主要功能：**
- **Merge Request 管理**：檢視、建立和審查 MR
- **Pipeline 狀態**：即時檢視 CI/CD Pipeline 狀態
- **Issue 追蹤**：管理 GitLab Issues
- **程式碼審查**：在 VS Code 中進行 MR 審查
- **分支管理**：建立和切換 GitLab 分支

**常用 GitLab 操作：**
```
Ctrl + Shift + P：
- GitLab: Create Merge Request
- GitLab: Show Issues
- GitLab: Show Merge Requests
- GitLab: Open in GitLab
- GitLab: Compare with Base
```

**GitLab CI/CD 整合：**
1. 檢視 Pipeline 狀態：
   - 在狀態列顯示目前分支的 Pipeline 狀態
   - 點擊可直接開啟 GitLab Pipeline 頁面

2. 建立 `.gitlab-ci.yml` 檔案支援：
   - 語法高亮和自動完成
   - 即時語法檢查
   - 範本片段支援

**GitLab 與 GitHub 比較：**

| 功能 | GitHub | GitLab |
|------|--------|--------|
| Pull/Merge Request | Pull Request | Merge Request |
| CI/CD | GitHub Actions | GitLab CI/CD |
| 專案管理 | Projects, Issues | Issues, Milestones, Boards |
| 容器註冊表 | GitHub Packages | GitLab Container Registry |
| 安全掃描 | GitHub Security | GitLab Security Dashboard |

### 3.2 常用快捷鍵

#### 3.2.1 檔案操作

| 快捷鍵 | 功能 | 說明 |
|--------|------|------|
| `Ctrl + N` | 新增檔案 | 建立新的未命名檔案 |
| `Ctrl + O` | 開啟檔案 | 開啟檔案對話框 |
| `Ctrl + S` | 儲存檔案 | 儲存目前檔案 |
| `Ctrl + Shift + S` | 另存新檔 | 另存新檔對話框 |
| `Ctrl + W` | 關閉分頁 | 關閉目前編輯器分頁 |
| `Ctrl + Shift + T` | 重開分頁 | 重新開啟最近關閉的分頁 |
| `Ctrl + Tab` | 切換分頁 | 在開啟的分頁間切換 |
| `Ctrl + P` | 快速開啟 | 快速搜尋並開啟檔案 |

#### 3.2.2 編輯操作

| 快捷鍵 | 功能 | 說明 |
|--------|------|------|
| `Ctrl + Z` | 復原 | 復原上一個動作 |
| `Ctrl + Y` | 重做 | 重做被復原的動作 |
| `Ctrl + X` | 剪下 | 剪下選取的文字 |
| `Ctrl + C` | 複製 | 複製選取的文字 |
| `Ctrl + V` | 貼上 | 貼上剪貼簿內容 |
| `Ctrl + A` | 全選 | 選取所有內容 |
| `Ctrl + F` | 搜尋 | 在目前檔案中搜尋 |
| `Ctrl + H` | 取代 | 搜尋並取代 |
| `Ctrl + Shift + F` | 全域搜尋 | 在整個專案中搜尋 |

#### 3.2.3 程式碼編輯

| 快捷鍵 | 功能 | 說明 |
|--------|------|------|
| `Ctrl + /` | 切換註解 | 註解/取消註解選取的行 |
| `Shift + Alt + A` | 區塊註解 | 切換區塊註解 |
| `Alt + Up/Down` | 移動行 | 向上/向下移動目前行 |
| `Shift + Alt + Up/Down` | 複製行 | 向上/向下複製目前行 |
| `Ctrl + Shift + K` | 刪除行 | 刪除目前行 |
| `Ctrl + Enter` | 插入新行 | 在下方插入新行 |
| `Ctrl + Shift + Enter` | 插入新行 | 在上方插入新行 |
| `Ctrl + ]` | 增加縮排 | 增加選取內容的縮排 |
| `Ctrl + [` | 減少縮排 | 減少選取內容的縮排 |

#### 3.2.4 進階操作

| 快捷鍵 | 功能 | 說明 |
|--------|------|------|
| `Ctrl + Shift + P` | 命令面板 | 開啟命令面板 |
| `Ctrl + Shift + E` | 檔案總管 | 切換到檔案總管 |
| `Ctrl + Shift + G` | Git 面板 | 切換到 Git 面板 |
| `Ctrl + Shift + X` | 擴充功能 | 切換到擴充功能面板 |
| `Ctrl + Shift + D` | 偵錯面板 | 切換到偵錯面板 |
| `Ctrl + ` ` (反引號) | 終端機 | 切換終端機面板 |
| `F11` | 全螢幕 | 切換全螢幕模式 |
| `Ctrl + K, Z` | 禪模式 | 進入專注模式 |

### 3.3 偵錯 (Debugging) 與斷點設定

#### 3.3.1 設定斷點

**基本斷點操作：**
1. **新增斷點**：在行號左側點擊，或按 `F9`
2. **條件斷點**：右鍵點擊斷點 → "Edit Breakpoint" → 設定條件
3. **日誌斷點**：在斷點不暫停的情況下輸出訊息
4. **移除斷點**：再次點擊斷點，或按 `F9`

**斷點類型：**
- **一般斷點**：程式執行到此處會暫停
- **條件斷點**：只有滿足條件時才暫停
- **日誌斷點**：輸出訊息但不暫停執行
- **函式斷點**：在特定函式被呼叫時暫停

#### 3.3.2 前端偵錯 (Vue 3 + TypeScript)

**Chrome DevTools 整合：**
1. 安裝 "Debugger for Chrome" 擴充功能
2. 在 `launch.json` 中配置：

```json
{
  "name": "Vue App Debug",
  "type": "chrome",
  "request": "launch",
  "url": "http://localhost:3000",
  "webRoot": "${workspaceFolder}/frontend/src",
  "sourceMaps": true
}
```

**偵錯步驟：**
1. 啟動開發伺服器：`npm run dev`
2. 在程式碼中設定斷點
3. 按 `F5` 啟動偵錯
4. 在瀏覽器中觸發相關功能

#### 3.3.3 後端偵錯 (Spring Boot)

**Java 偵錯設定：**
在 `launch.json` 中配置：

```json
{
  "name": "Spring Boot Debug",
  "type": "java",
  "request": "launch",
  "mainClass": "com.yourcompany.Application",
  "projectName": "your-backend-project",
  "args": "--spring.profiles.active=dev",
  "vmArgs": "-Dspring.profiles.active=dev"
}
```

**偵錯步驟：**
1. 在 Java 程式碼中設定斷點
2. 按 `F5` 啟動偵錯模式
3. 透過 API 測試工具觸發相關端點
4. 程式會在斷點處暫停

#### 3.3.4 偵錯控制快捷鍵

| 快捷鍵 | 功能 | 說明 |
|--------|------|------|
| `F5` | 開始偵錯 | 啟動偵錯或繼續執行 |
| `Shift + F5` | 停止偵錯 | 停止偵錯工作階段 |
| `Ctrl + Shift + F5` | 重新啟動 | 重新啟動偵錯工作階段 |
| `F10` | 逐步執行 | 執行下一行（不進入函式） |
| `F11` | 逐步進入 | 執行下一行（進入函式） |
| `Shift + F11` | 逐步離開 | 離開目前函式 |
| `F9` | 切換斷點 | 在目前行新增/移除斷點 |

### 3.4 終端機與多工作區使用

#### 3.4.1 終端機基本操作

**開啟終端機：**
- 按 `Ctrl + ` ` (反引號)
- 或選擇 `Terminal > New Terminal`

**終端機管理：**
- **新增終端機**：點擊終端機面板的 `+` 號
- **切換終端機**：點擊終端機標籤
- **分割終端機**：點擊分割按鈕或按 `Ctrl + Shift + 5`
- **關閉終端機**：點擊垃圾桶圖示或按 `Ctrl + Shift + ` `

#### 3.4.2 多工作區管理

**開啟多個工作區：**
1. **新視窗**：`File > New Window` 或 `Ctrl + Shift + N`
2. **多資料夾工作區**：`File > Add Folder to Workspace`
3. **工作區檔案**：儲存為 `.code-workspace` 檔案

**工作區切換：**
- 使用 `Ctrl + Tab` 在不同視窗間切換
- 使用 `Ctrl + 1, 2, 3...` 切換編輯器群組

#### 3.4.3 實用終端機指令

**前端開發常用指令：**
```powershell
# 進入前端目錄
cd frontend

# 安裝相依套件
npm install

# 啟動開發伺服器
npm run dev

# 執行測試
npm run test

# 建置專案
npm run build

# 檢查程式碼
npm run lint
```

**後端開發常用指令：**
```powershell
# 進入後端目錄
cd backend

# Maven 編譯
mvn compile

# 執行應用程式
mvn spring-boot:run

# 執行測試
mvn test

# 打包專案
mvn package

# 清理專案
mvn clean
```

### 3.5 程式碼片段 (Snippets) 使用

#### 3.5.1 使用內建程式碼片段

VS Code 提供豐富的內建程式碼片段，加速程式碼撰寫效率。

**常用 JavaScript/TypeScript 片段：**
```typescript
// 輸入 "for" 然後按 Tab
for (let index = 0; index < array.length; index++) {
    const element = array[index];
}

// 輸入 "fof" 然後按 Tab
for (const iterator of object) {
}

// 輸入 "func" 然後按 Tab
function name(params: type) {
    
}

// 輸入 "cl" 然後按 Tab
console.log();
```

**常用 Java 片段：**
```java
// 輸入 "main" 然後按 Tab
public static void main(String[] args) {
    
}

// 輸入 "sysout" 然後按 Tab
System.out.println();

// 輸入 "for" 然後按 Tab
for (int i = 0; i < args.length; i++) {
    
}

// 輸入 "try" 然後按 Tab
try {
    
} catch (Exception e) {
    // TODO: handle exception
}
```

#### 3.5.2 自訂程式碼片段

**建立全域程式碼片段：**
1. 按 `Ctrl + Shift + P`
2. 輸入 `Preferences: Configure User Snippets`
3. 選擇語言或建立新的全域片段檔案

**Vue 3 Composition API 片段範例：**
```json
{
  "Vue 3 Composition API Component": {
    "prefix": "vue3-comp",
    "body": [
      "<template>",
      "  <div class=\"${1:component-name}\">",
      "    ${2:<!-- Component content -->}",
      "  </div>",
      "</template>",
      "",
      "<script setup lang=\"ts\">",
      "import { ref, reactive, computed, onMounted } from 'vue'",
      "",
      "// Reactive data",
      "const ${3:data} = ref(${4:''})",
      "",
      "// Computed properties",
      "const ${5:computedValue} = computed(() => {",
      "  return ${6:// computation}",
      "})",
      "",
      "// Lifecycle hooks",
      "onMounted(() => {",
      "  ${7:// mounted logic}",
      "})",
      "</script>",
      "",
      "<style scoped>",
      ".${1:component-name} {",
      "  ${8:/* styles */}",
      "}",
      "</style>"
    ],
    "description": "Vue 3 Composition API component template"
  }
}
```

**Spring Boot Controller 片段範例：**
```json
{
  "Spring Boot REST Controller": {
    "prefix": "spring-controller",
    "body": [
      "@RestController",
      "@RequestMapping(\"/api/${1:resource}\")",
      "@Validated",
      "public class ${2:Resource}Controller {",
      "",
      "    private final ${2:Resource}Service ${3:service};",
      "",
      "    public ${2:Resource}Controller(${2:Resource}Service ${3:service}) {",
      "        this.${3:service} = ${3:service};",
      "    }",
      "",
      "    @GetMapping",
      "    public ResponseEntity<List<${2:Resource}>> getAll() {",
      "        List<${2:Resource}> ${4:resources} = ${3:service}.findAll();",
      "        return ResponseEntity.ok(${4:resources});",
      "    }",
      "",
      "    @GetMapping(\"/{id}\")",
      "    public ResponseEntity<${2:Resource}> getById(@PathVariable Long id) {",
      "        ${2:Resource} ${5:resource} = ${3:service}.findById(id);",
      "        return ResponseEntity.ok(${5:resource});",
      "    }",
      "",
      "    @PostMapping",
      "    public ResponseEntity<${2:Resource}> create(@Valid @RequestBody ${2:Resource} ${5:resource}) {",
      "        ${2:Resource} created = ${3:service}.create(${5:resource});",
      "        return ResponseEntity.status(HttpStatus.CREATED).body(created);",
      "    }",
      "}"
    ],
    "description": "Spring Boot REST Controller template"
  }
}
```

#### 3.5.3 專案特定程式碼片段

在專案根目錄建立 `.vscode/snippets.code-snippets`：

```json
{
  "Project API Response": {
    "prefix": "api-response",
    "body": [
      "interface ${1:ResponseName} {",
      "  success: boolean;",
      "  message: string;",
      "  data?: ${2:any};",
      "  errors?: string[];",
      "  timestamp: string;",
      "}"
    ],
    "description": "Standard API response interface"
  },
  
  "Project Test Case": {
    "prefix": "test-case",
    "body": [
      "describe('${1:Test Suite}', () => {",
      "  beforeEach(() => {",
      "    ${2:// Setup}",
      "  });",
      "",
      "  it('should ${3:test description}', () => {",
      "    // Arrange",
      "    ${4:// Setup test data}",
      "",
      "    // Act",
      "    ${5:// Execute test action}",
      "",
      "    // Assert",
      "    ${6:// Verify results}",
      "  });",
      "});"
    ],
    "description": "Standard test case template"
  }
}
```

#### 3.5.4 程式碼片段最佳實務

**設計原則：**
1. **簡潔的前綴**：使用容易記憶的簡短前綴
2. **合理的佔位符**：使用有意義的變數名稱
3. **適當的預設值**：提供常用的預設值
4. **清楚的描述**：撰寫描述性的說明

**管理技巧：**
- 定期檢視和更新程式碼片段
- 團隊共享常用片段
- 使用版本控制管理專案片段
- 避免過於複雜的片段

### 3.6 實務案例與注意事項

#### ⚠️ 開發注意事項
1. **版本控制**：經常提交變更，避免遺失程式碼
2. **分支管理**：使用功能分支進行開發，避免直接在主分支修改
3. **程式碼格式化**：設定自動格式化，保持程式碼風格一致

#### 💡 開發最佳實務
- 使用 Git 工作流程：Feature Branch → Pull Request → Code Review → Merge
- 定期同步遠端分支，避免合併衝突
- 善用 VS Code 的多游標編輯功能提升效率（`Ctrl + Alt + Up/Down`）
- 使用程式碼片段（Snippets）加速常用程式碼撰寫

---

## 4. 專案特定開發流程指引

### 4.1 前端開發流程 (Vue 3 + TypeScript)

#### 4.1.1 專案啟動與設定

**初始化專案環境：**

1. **開啟專案**
   ```powershell
   cd d:\your-project\frontend
   code .
   ```

2. **安裝相依套件**
   ```powershell
   npm install
   # 或使用 yarn
   yarn install
   ```

3. **檢查 Node.js 版本**
   ```powershell
   node --version  # 建議使用 Node.js 16+
   npm --version   # 建議使用 npm 8+
   ```

#### 4.1.2 開發伺服器啟動

**方式一：透過 VS Code 任務**
1. 按 `Ctrl + Shift + P`
2. 輸入 `Tasks: Run Task`
3. 選擇 `Frontend: Dev Server`

**方式二：透過終端機**
```powershell
cd frontend
npm run dev
# 或
yarn dev
```

**開發伺服器資訊：**
- 預設連接埠：`http://localhost:3000`
- 自動重新載入：檔案異動時自動更新
- 開發工具：Vue DevTools 整合

#### 4.1.3 前端偵錯設定

**配置 launch.json：**
```json
{
  "name": "Debug Vue App",
  "type": "chrome",
  "request": "launch",
  "url": "http://localhost:3000",
  "webRoot": "${workspaceFolder}/frontend/src",
  "breakOnLoad": true,
  "sourceMapPathOverrides": {
    "webpack:///src/*": "${webRoot}/*"
  }
}
```

**偵錯步驟：**
1. 啟動開發伺服器
2. 在 `.vue` 或 `.ts` 檔案中設定斷點
3. 按 `F5` 啟動偵錯
4. 在瀏覽器中操作觸發斷點

#### 4.1.4 前端測試執行

**單元測試 (Vitest)：**
```powershell
# 執行所有測試
npm run test

# 監視模式執行測試
npm run test:watch

# 產生測試覆蓋率報告
npm run test:coverage
```

**E2E 測試 (Cypress)：**
```powershell
# 開啟 Cypress 測試介面
npm run test:e2e

# 無介面執行 E2E 測試
npm run test:e2e:headless
```

#### 4.1.5 前端建置流程

**開發建置：**
```powershell
npm run build:dev
```

**生產建置：**
```powershell
npm run build
```

**預覽建置結果：**
```powershell
npm run preview
```

### 4.2 後端開發流程 (Spring Boot)

#### 4.2.1 Java 環境設定

**檢查 Java 環境：**
```powershell
java -version     # 建議使用 Java 17+
mvn -version      # 檢查 Maven 版本
```

**VS Code Java 設定：**
確保已安裝以下擴充功能：
- Extension Pack for Java
- Spring Boot Extension Pack
- Maven for Java

#### 4.2.2 Spring Boot 應用程式啟動

**方式一：透過 VS Code 偵錯**
1. 開啟主要應用程式類別（通常是 `Application.java`）
2. 點擊類別上方的 "Run" 或 "Debug" 連結
3. 或按 `F5` 啟動偵錯模式

**方式二：透過 Maven 任務**
```powershell
cd backend
mvn spring-boot:run
```

**方式三：透過 VS Code 任務**
1. 按 `Ctrl + Shift + P`
2. 選擇 `Tasks: Run Task`
3. 選擇 `Backend: Maven Spring Boot Run`

#### 4.2.3 後端偵錯設定

**偵錯配置範例：**
```json
{
  "name": "Debug Spring Boot",
  "type": "java",
  "request": "launch",
  "mainClass": "com.yourcompany.YourApplication",
  "projectName": "your-backend-project",
  "args": "--spring.profiles.active=dev",
  "vmArgs": [
    "-Dspring.profiles.active=dev",
    "-Dserver.port=8080"
  ],
  "console": "internalConsole",
  "stopOnEntry": false
}
```

**設定斷點與偵錯：**
1. 在 Java 程式碼中點擊行號左側設定斷點
2. 啟動偵錯模式
3. 使用 Postman 或前端應用程式觸發 API
4. 程式會在斷點處暫停

#### 4.2.4 API 測試

**使用 REST Client 擴充功能：**

建立 `api-test.http` 檔案：
```http
### 測試用戶登入
POST http://localhost:8080/api/auth/login
Content-Type: application/json

{
  "username": "admin",
  "password": "password123"
}

### 取得用戶清單
GET http://localhost:8080/api/users
Authorization: Bearer {{token}}

### 建立新用戶
POST http://localhost:8080/api/users
Content-Type: application/json
Authorization: Bearer {{token}}

{
  "username": "newuser",
  "email": "newuser@example.com",
  "role": "USER"
}
```

#### 4.2.5 後端測試執行

**單元測試：**
```powershell
# 執行所有單元測試
mvn test

# 執行特定測試類別
mvn test -Dtest=UserServiceTest

# 執行特定測試方法
mvn test -Dtest=UserServiceTest#testCreateUser
```

**整合測試：**
```powershell
# 執行整合測試
mvn verify

# 包含測試覆蓋率報告
mvn clean verify jacoco:report
```

### 4.3 全端開發工作流程

#### 4.3.1 同時啟動前後端

**使用 VS Code 複合任務：**

在 `tasks.json` 中新增：
```json
{
  "label": "Start Full Stack",
  "dependsOn": [
    "Backend: Maven Spring Boot Run",
    "Frontend: Dev Server"
  ],
  "dependsOrder": "parallel"
}
```

**手動啟動步驟：**
1. 開啟兩個終端機視窗
2. 終端機 1：
   ```powershell
   cd backend
   mvn spring-boot:run
   ```
3. 終端機 2：
   ```powershell
   cd frontend
   npm run dev
   ```

#### 4.3.2 API 介接開發

**前端 API 設定：**

在 `frontend/src/config/api.ts` 中：
```typescript
const API_BASE_URL = process.env.NODE_ENV === 'production' 
  ? 'https://api.yourcompany.com' 
  : 'http://localhost:8080';

export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});
```

**CORS 設定 (後端)：**
```java
@Configuration
@EnableWebMvc
public class WebConfig implements WebMvcConfigurer {
    
    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/api/**")
                .allowedOrigins("http://localhost:3000")
                .allowedMethods("GET", "POST", "PUT", "DELETE")
                .allowedHeaders("*")
                .allowCredentials(true);
    }
}
```

#### 4.3.3 資料庫開發

**H2 資料庫 (開發環境)：**
```yaml
# application-dev.yml
spring:
  datasource:
    url: jdbc:h2:mem:testdb
    driver-class-name: org.h2.Driver
    username: sa
    password: 
  h2:
    console:
      enabled: true
      path: /h2-console
```

**MySQL 資料庫 (生產環境)：**
```yaml
# application-prod.yml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/yourdb
    username: ${DB_USERNAME}
    password: ${DB_PASSWORD}
    driver-class-name: com.mysql.cj.jdbc.Driver
```

### 4.4 程式碼品質檢查

#### 4.4.1 前端程式碼檢查

**ESLint 執行：**
```powershell
# 檢查所有檔案
npm run lint

# 自動修正可修正的問題
npm run lint:fix

# 檢查特定檔案
npx eslint src/components/UserForm.vue
```

**Prettier 格式化：**
```powershell
# 格式化所有檔案
npm run format

# 檢查格式化狀態
npm run format:check
```

#### 4.4.2 後端程式碼檢查

**Checkstyle 檢查：**
```powershell
# 執行 Checkstyle 檢查
mvn checkstyle:check

# 產生 Checkstyle 報告
mvn checkstyle:checkstyle
```

**SpotBugs 靜態分析：**
```powershell
# 執行 SpotBugs 分析
mvn spotbugs:check

# 產生 SpotBugs 報告
mvn spotbugs:spotbugs
```

### 4.6 效能監控與分析

#### 4.6.1 前端效能監控

**使用 Lighthouse 擴充功能：**
1. 安裝 "Lighthouse" 擴充功能
2. 在開發者工具中執行 Lighthouse 分析
3. 檢視效能報告和建議

**Vue DevTools 效能分析：**
```typescript
// 在 main.ts 中啟用效能追蹤
import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)

// 開發環境啟用效能追蹤
if (process.env.NODE_ENV === 'development') {
  app.config.performance = true
}

app.mount('#app')
```

**前端效能檢查清單：**
- Bundle 大小分析：`npm run build -- --report`
- Core Web Vitals 監控
- 記憶體使用量檢查
- 網路請求最佳化

#### 4.6.2 後端效能監控

**Spring Boot Actuator 設定：**
```yaml
# application.yml
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,prometheus
  endpoint:
    health:
      show-details: always
    metrics:
      enabled: true
```

**效能指標監控：**
```java
@RestController
public class MetricsController {
    
    @Autowired
    private MeterRegistry meterRegistry;
    
    @GetMapping("/api/metrics/custom")
    public Map<String, Double> getCustomMetrics() {
        Map<String, Double> metrics = new HashMap<>();
        
        // JVM 記憶體使用量
        metrics.put("jvm.memory.used", 
            meterRegistry.get("jvm.memory.used").gauge().value());
        
        // HTTP 請求計數
        metrics.put("http.requests.total", 
            meterRegistry.get("http.server.requests").counter().count());
        
        return metrics;
    }
}
```

**後端效能檢查清單：**
- 資料庫查詢最佳化
- API 回應時間監控
- JVM 記憶體使用分析
- 執行緒池狀態檢查

#### 4.6.3 VS Code 效能診斷

**啟用效能監控：**
1. 按 `Ctrl + Shift + P`
2. 輸入 `Developer: Startup Performance`
3. 檢視啟動效能報告

**常用效能診斷指令：**
```
Ctrl + Shift + P：
- Developer: Show Running Extensions
- Developer: Restart Extension Host
- Developer: Toggle Developer Tools
- Performance: Startup Performance
```

**擴充功能效能分析：**
```typescript
// 在 VS Code 開發者工具 Console 中執行
// 查看擴充功能啟動時間
console.table(
  vscode.extensions.all
    .filter(ext => ext.isActive)
    .map(ext => ({
      id: ext.id,
      activationTime: ext.activationTime || 'Unknown'
    }))
    .sort((a, b) => (b.activationTime || 0) - (a.activationTime || 0))
)
```

### 4.7 實務案例與注意事項

#### ⚠️ 開發流程注意事項
1. **連接埠衝突**：確保前後端使用不同連接埠
2. **環境變數**：正確設定開發和生產環境變數
3. **API 版本控制**：使用 API 版本控制避免相容性問題
4. **錯誤處理**：前後端都要有適當的錯誤處理機制

#### 💡 開發最佳實務
- 使用功能分支進行開發，避免直接在主分支修改
- 定期執行測試，確保程式碼品質
- 使用 API 文件工具（如 Swagger）記錄 API 規格
- 實施 Code Review 流程，提升程式碼品質

## 4.5 Python 開發環境設定

### 4.5.1 Python 專案結構

**標準 Python 專案結構：**
```
my-python-project/
├── .vscode/                 # VS Code 設定檔
│   ├── settings.json
│   ├── launch.json
│   └── tasks.json
├── src/                     # 原始碼目錄
│   ├── __init__.py
│   └── main.py
├── tests/                   # 測試目錄
│   ├── __init__.py
│   └── test_main.py
├── docs/                    # 文件目錄
├── requirements.txt         # 套件依賴
├── setup.py                # 安裝設定
├── README.md               # 專案說明
├── .gitignore              # Git 忽略檔案
├── .pylintrc               # Pylint 設定
└── pyproject.toml          # 專案設定（Python 3.6+）
```

### 4.5.2 Python 環境設定

#### 虛擬環境設定

**建立虛擬環境：**
```powershell
# 使用 venv（Python 3.3+）
python -m venv venv

# 啟動虛擬環境（Windows）
.\venv\Scripts\Activate.ps1

# 啟動虛擬環境（Linux/macOS）
source venv/bin/activate

# 安裝套件
pip install -r requirements.txt

# 凍結當前套件版本
pip freeze > requirements.txt
```

**使用 conda：**
```powershell
# 建立新環境
conda create -n myproject python=3.11

# 啟動環境
conda activate myproject

# 安裝套件
conda install pandas numpy matplotlib

# 匯出環境
conda env export > environment.yml
```

#### VS Code Python 解譯器設定

**設定 Python 解譯器：**
1. 按 `Ctrl + Shift + P`
2. 輸入 "Python: Select Interpreter"
3. 選擇虛擬環境中的 Python

**`.vscode/settings.json` Python 設定：**
```json
{
  "python.defaultInterpreterPath": "./venv/Scripts/python.exe",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.linting.flake8Enabled": true,
  "python.linting.mypyEnabled": true,
  "python.formatting.provider": "black",
  "python.formatting.blackArgs": ["--line-length", "88"],
  "python.sortImports.args": ["--profile", "black"],
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": [
    "tests",
    "--verbose"
  ],
  "python.testing.unittestEnabled": false,
  "python.testing.nosetestsEnabled": false,
  "python.analysis.autoImportCompletions": true,
  "python.analysis.typeCheckingMode": "basic"
}
```

### 4.5.3 Python 開發工具設定

#### Linting 和格式化

**Pylint 設定（.pylintrc）：**
```ini
[MASTER]
disable=
    C0114, # missing-module-docstring
    C0115, # missing-class-docstring
    C0116, # missing-function-docstring
    R0903, # too-few-public-methods

[FORMAT]
max-line-length=88

[VARIABLES]
good-names=i,j,k,ex,Run,_,x,y,z
```

**Black 格式化設定（pyproject.toml）：**
```toml
[tool.black]
line-length = 88
target-version = ['py311']
include = '\.pyi?$'
exclude = '''
/(
    \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | _build
  | buck-out
  | build
  | dist
)/
'''
```

#### 測試設定

**pytest 設定（pytest.ini）：**
```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    --verbose
    --tb=short
    --strict-markers
    --disable-warnings
    --cov=src
    --cov-report=html
    --cov-report=term-missing
```

**單元測試範例：**
```python
# tests/test_main.py
import unittest
from src.main import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        """測試加法功能"""
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
    
    def test_divide_by_zero(self):
        """測試除零例外"""
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

if __name__ == '__main__':
    unittest.main()
```

### 4.5.4 Python 偵錯設定

**`.vscode/launch.json` Python 設定：**
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": true
    },
    {
      "name": "Python: FastAPI",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/src/main.py",
      "console": "integratedTerminal",
      "args": ["--reload"],
      "env": {
        "PYTHONPATH": "${workspaceFolder}"
      }
    },
    {
      "name": "Python: Flask",
      "type": "python",
      "request": "launch",
      "module": "flask",
      "env": {
        "FLASK_APP": "src/app.py",
        "FLASK_ENV": "development",
        "PYTHONPATH": "${workspaceFolder}"
      },
      "args": ["run", "--host=0.0.0.0", "--port=5000"],
      "jinja": true
    },
    {
      "name": "Python: Django",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/manage.py",
      "args": ["runserver"],
      "django": true,
      "justMyCode": true
    },
    {
      "name": "Python: Pytest",
      "type": "python",
      "request": "launch",
      "module": "pytest",
      "args": ["tests", "-v"],
      "console": "integratedTerminal",
      "justMyCode": false
    }
  ]
}
```

### 4.5.5 Python 任務設定

**`.vscode/tasks.json` Python 任務：**
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Python: Install Dependencies",
      "type": "shell",
      "command": "pip",
      "args": ["install", "-r", "requirements.txt"],
      "group": "build",
      "presentation": {
        "echo": true,
        "reveal": "always"
      }
    },
    {
      "label": "Python: Run Tests",
      "type": "shell",
      "command": "python",
      "args": ["-m", "pytest", "tests", "-v"],
      "group": "test",
      "presentation": {
        "echo": true,
        "reveal": "always"
      }
    },
    {
      "label": "Python: Format Code",
      "type": "shell",
      "command": "black",
      "args": ["src", "tests"],
      "group": "build",
      "presentation": {
        "echo": true,
        "reveal": "always"
      }
    },
    {
      "label": "Python: Lint Code",
      "type": "shell",
      "command": "pylint",
      "args": ["src"],
      "group": "build",
      "presentation": {
        "echo": true,
        "reveal": "always"
      }
    },
    {
      "label": "Python: Generate Documentation",
      "type": "shell",
      "command": "sphinx-build",
      "args": ["-b", "html", "docs", "docs/_build/html"],
      "group": "build"
    }
  ]
}
```

### 4.5.6 Python 專案範例

#### FastAPI 專案範例

**主應用程式（src/main.py）：**
```python
"""
FastAPI 應用程式主檔案
提供 RESTful API 服務
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(
    title="Python Tutorial API",
    description="Python 開發教學 API",
    version="1.0.0"
)

class Item(BaseModel):
    """項目模型"""
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float

# 模擬資料庫
items_db: List[Item] = []

@app.get("/")
async def root():
    """根路徑"""
    return {"message": "Hello Python World!"}

@app.get("/items/", response_model=List[Item])
async def get_items():
    """取得所有項目"""
    return items_db

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    """建立新項目"""
    item.id = len(items_db) + 1
    items_db.append(item)
    return item

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """取得特定項目"""
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
```

**需求檔案（requirements.txt）：**
```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
pytest==7.4.3
pytest-cov==4.1.0
black==23.11.0
pylint==3.0.3
mypy==1.7.1
```

### 4.5.7 Python 開發最佳實務

#### 程式碼品質檢查

**自動化品質檢查流程：**
```powershell
# 格式化程式碼
black src tests

# 靜態分析
pylint src
mypy src

# 執行測試
pytest tests --cov=src --cov-report=html

# 安全性檢查
bandit -r src
```

#### 依賴管理

**使用 pip-tools 管理依賴：**
```powershell
# 安裝 pip-tools
pip install pip-tools

# 編譯需求檔案
pip-compile requirements.in

# 同步環境
pip-sync requirements.txt
```

**requirements.in 範例：**
```txt
# Web 框架
fastapi
uvicorn[standard]

# 資料處理
pandas
numpy

# 開發工具
pytest
black
pylint
```

## 5. 協作開發功能

### 5.1 Live Share 即時協作

#### 5.1.1 Live Share 設定

Live Share 讓團隊成員可以即時協作編輯程式碼，無需複雜的環境設定。

**安裝 Live Share：**
```bash
code --install-extension ms-vsliveshare.vsliveshare
```

**啟動協作工作階段：**
1. 按 `Ctrl + Shift + P`
2. 輸入 `Live Share: Start Collaboration Session`
3. 選擇分享範圍（唯讀或可編輯）
4. 複製並分享邀請連結

#### 5.1.2 Live Share 功能

**主要功能：**
- **即時程式碼編輯**：多人同時編輯同一檔案
- **共享終端機**：分享終端機操作權限
- **共享伺服器**：自動轉發本地伺服器連接埠
- **語音通話**：整合語音溝通功能
- **追蹤游標**：查看其他參與者的游標位置

**協作工作流程：**
1. **主持人**：啟動 Live Share 工作階段
2. **參與者**：點擊邀請連結加入
3. **協作編輯**：即時查看和編輯程式碼
4. **除錯協作**：共享除錯工作階段
5. **結束工作階段**：主持人結束協作

#### 5.1.3 Live Share 最佳實務

**權限管理：**
```json
// .vscode/settings.json
{
  "liveshare.guestApprovalRequired": true,
  "liveshare.shareExternalFiles": false,
  "liveshare.shareTerminal": false
}
```

**安全考量：**
- 謹慎分享敏感程式碼
- 使用唯讀模式進行程式碼展示
- 定期檢視參與者清單

### 5.2 多人開發設定

#### 5.2.1 團隊設定標準化

**建立團隊設定檔案：**
```json
// .vscode/settings.json (專案層級)
{
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true,
    "source.organizeImports": true
  },
  "files.eol": "\n",
  "files.insertFinalNewline": true,
  "files.trimTrailingWhitespace": true,
  
  // 統一擴充功能設定
  "eslint.workingDirectories": ["frontend"],
  "prettier.configPath": "frontend/.prettierrc",
  
  // Git 設定
  "git.autofetch": true,
  "git.confirmSync": false,
  "git.enableSmartCommit": true
}
```

**強制擴充功能：**
```json
// .vscode/extensions.json
{
  "recommendations": [
    "ms-ceintl.vscode-language-pack-zh-hant",
    "eamodio.gitlens",
    "esbenp.prettier-vscode",
    "dbaeumer.vscode-eslint"
  ],
  "unwantedRecommendations": [
    "ms-vscode.vscode-typescript"
  ]
}
```

#### 5.2.2 工作流程標準化

**Git 工作流程設定：**
```json
// .vscode/tasks.json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Git: Sync with Main",
      "type": "shell",
      "command": "git",
      "args": ["pull", "origin", "main"],
      "group": "build"
    },
    {
      "label": "Git: Create Feature Branch",
      "type": "shell",
      "command": "git",
      "args": ["checkout", "-b", "feature/${input:featureName}"],
      "group": "build"
    }
  ],
  "inputs": [
    {
      "id": "featureName",
      "description": "Feature branch name",
      "default": "new-feature",
      "type": "promptString"
    }
  ]
}
```

### 5.3 程式碼審查工具

#### 5.3.1 GitHub Pull Request 整合

**設定 GitHub PR 擴充功能：**
```bash
code --install-extension github.vscode-pull-request-github
```

**PR 審查工作流程：**
1. **建立 PR**：`Ctrl + Shift + P` → `GitHub: Create Pull Request`
2. **查看變更**：在 GitHub Pull Requests 面板檢視差異
3. **新增評論**：直接在程式碼行上新增審查評論
4. **回應評論**：在 VS Code 中直接回覆討論
5. **核准合併**：完成審查後核准 PR

#### 5.3.2 GitLab Merge Request 整合

**設定 GitLab MR 擴充功能：**
```bash
code --install-extension gitlab.gitlab-workflow
```

**MR 審查工作流程：**
1. **建立 MR**：`Ctrl + Shift + P` → `GitLab: Create Merge Request`
2. **查看管道狀態**：在狀態列查看 CI/CD 管道執行狀態
3. **審查變更**：在 GitLab 面板檢視檔案差異
4. **新增評論**：在程式碼行上新增審查建議
5. **追蹤問題**：整合 GitLab Issues 進行追蹤
6. **合併請求**：審查完成後執行合併

**GitLab 與 GitHub 比較：**

| 功能 | GitHub | GitLab |
|------|--------|--------|
| 程式碼審查 | Pull Request | Merge Request |
| CI/CD 整合 | GitHub Actions | GitLab CI/CD |
| 問題追蹤 | GitHub Issues | GitLab Issues |
| 專案管理 | GitHub Projects | GitLab Boards |
| 安全性掃描 | GitHub Security | GitLab Security |

#### 5.3.3 程式碼審查檢查清單

**前端程式碼審查要點：**
- [ ] 元件結構是否合理
- [ ] TypeScript 類型定義是否完整
- [ ] 是否遵循 Vue 3 最佳實務
- [ ] CSS 樣式是否符合 Tailwind 規範
- [ ] 是否有適當的錯誤處理
- [ ] 效能是否最佳化

**後端程式碼審查要點：**
- [ ] API 設計是否 RESTful
- [ ] 例外處理是否完整
- [ ] 資料庫操作是否最佳化
- [ ] 安全性考量是否足夠
- [ ] 測試覆蓋率是否充足
- [ ] 文件是否完整

### 5.4 團隊協作最佳實務

#### 5.4.1 溝通協調

**每日站會檢查：**
- 昨天完成的工作
- 今天計劃的工作
- 遇到的阻礙或問題
- 需要其他人協助的事項

**程式碼評論準則：**
- 建設性的意見回饋
- 明確的改善建議
- 尊重團隊成員
- 關注程式碼品質而非個人

#### 5.4.2 知識分享

**團隊學習機制：**
- 定期技術分享會
- 程式碼最佳實務分享
- 新技術評估與討論
- 問題解決經驗分享

**文件協作：**
- 使用 Markdown 撰寫文件
- 版本控制文件變更
- 定期更新開發指南
- 建立 FAQ 知識庫

---

## 6. 進階功能與擴充

### 6.1 自訂程式碼片段

#### 6.1.1 進階程式碼片段語法

**變數替換：**
```json
{
  "Current Date": {
    "prefix": "date",
    "body": [
      "// Created on: $CURRENT_YEAR-$CURRENT_MONTH-$CURRENT_DATE",
      "// Author: $1",
      "$0"
    ],
    "description": "Insert current date and author"
  }
}
```

**條件邏輯：**
```json
{
  "React Component": {
    "prefix": "rfc",
    "body": [
      "import React${1:, { useState \\}} from 'react';",
      "",
      "interface ${2:ComponentName}Props {",
      "  ${3:// props}",
      "}",
      "",
      "const ${2:ComponentName}: React.FC<${2:ComponentName}Props> = (${4:props}) => {",
      "  ${5:const [state, setState] = useState();}",
      "",
      "  return (",
      "    <div>",
      "      ${0:// Component content}",
      "    </div>",
      "  );",
      "};",
      "",
      "export default ${2:ComponentName};"
    ],
    "description": "React functional component with TypeScript"
  }
}
```

### 6.2 擴充功能開發入門

#### 6.2.1 建立基本擴充功能

**初始化擴充功能專案：**
```bash
npm install -g yo generator-code
yo code
```

**選擇擴充功能類型：**
- New Extension (TypeScript)
- New Color Theme
- New Language Support
- New Code Snippets
- New Keymap

### 6.3 工作流程自動化

#### 6.3.1 Task 自動化

**VS Code 任務系統概述：**

VS Code 任務系統讓您可以自動化常見的開發工作流程，如建置、測試、部署等。

**基本任務配置：**
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Build Project",
      "type": "shell",
      "command": "mvn",
      "args": ["clean", "compile"],
      "group": "build",
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared"
      },
      "problemMatcher": ["$maven-compiler-java"]
    }
  ]
}
```

**複合任務範例：**
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Frontend: Install Dependencies",
      "type": "shell",
      "command": "npm",
      "args": ["install"],
      "options": {
        "cwd": "${workspaceFolder}/frontend"
      },
      "group": "build"
    },
    {
      "label": "Frontend: Build",
      "type": "shell",
      "command": "npm",
      "args": ["run", "build"],
      "options": {
        "cwd": "${workspaceFolder}/frontend"
      },
      "group": "build",
      "dependsOn": "Frontend: Install Dependencies"
    },
    {
      "label": "Backend: Test",
      "type": "shell",
      "command": "mvn",
      "args": ["test"],
      "options": {
        "cwd": "${workspaceFolder}/backend"
      },
      "group": "test"
    },
    {
      "label": "Full Build Pipeline",
      "dependsOrder": "sequence",
      "dependsOn": [
        "Frontend: Build",
        "Backend: Test"
      ],
      "group": {
        "kind": "build",
        "isDefault": true
      }
    }
  ]
}
```

**任務變數使用：**
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Deploy to Environment",
      "type": "shell",
      "command": "deploy",
      "args": ["--env", "${input:environment}"],
      "group": "build"
    }
  ],
  "inputs": [
    {
      "id": "environment",
      "description": "Select deployment environment",
      "type": "pickString",
      "options": [
        "development",
        "staging", 
        "production"
      ],
      "default": "development"
    }
  ]
}
```

**背景任務設定：**
```json
{
  "label": "Watch Mode",
  "type": "shell",
  "command": "npm",
  "args": ["run", "watch"],
  "isBackground": true,
  "group": "build",
  "presentation": {
    "echo": true,
    "reveal": "always",
    "focus": false,
    "panel": "new"
  },
  "problemMatcher": {
    "pattern": [
      {
        "regexp": "\\b\\B",
        "file": 1,
        "location": 2,
        "message": 3
      }
    ],
    "background": {
      "activeOnStart": true,
      "beginsPattern": "^.*webpack.*",
      "endsPattern": "^.*compiled.*"
    }
  }
}
```

**任務執行快捷鍵：**
```json
// keybindings.json
[
  {
    "key": "ctrl+shift+b",
    "command": "workbench.action.tasks.build"
  },
  {
    "key": "ctrl+shift+t", 
    "command": "workbench.action.tasks.test"
  },
  {
    "key": "ctrl+shift+r",
    "command": "workbench.action.tasks.runTask",
    "args": "Full Build Pipeline"
  }
]
```

**常用任務指令：**
- `Ctrl + Shift + P` → `Tasks: Run Task` - 執行任務
- `Ctrl + Shift + P` → `Tasks: Configure Task` - 配置任務
- `Ctrl + Shift + P` → `Tasks: Restart Running Task` - 重新啟動任務
- `Ctrl + Shift + B` - 執行建置任務

#### 6.3.2 GitHub Actions 整合

**設定 GitHub Actions：**
```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline
on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Setup Java
      uses: actions/setup-java@v3
      with:
        java-version: '11'
        distribution: 'temurin'
    - name: Build with Maven
      run: mvn clean compile test
```

#### 6.3.3 GitLab CI/CD 整合

**設定 GitLab CI/CD：**
```yaml
# .gitlab-ci.yml
stages:
  - build
  - test
  - deploy

variables:
  MAVEN_OPTS: "-Dmaven.repo.local=$CI_PROJECT_DIR/.m2/repository"

cache:
  paths:
    - .m2/repository/
    - node_modules/

build:
  stage: build
  image: maven:3.8.1-openjdk-11
  script:
    - mvn clean compile
  artifacts:
    paths:
      - target/

test:
  stage: test
  image: maven:3.8.1-openjdk-11
  script:
    - mvn test
  coverage: '/Total.*?([0-9]{1,3})%/'
  artifacts:
    reports:
      junit:
        - target/surefire-reports/TEST-*.xml
      coverage_report:
        coverage_format: cobertura
        path: target/site/cobertura/coverage.xml

deploy:
  stage: deploy
  script:
    - echo "Deploying application..."
  only:
    - main
```

**VS Code 中的 CI/CD 監控：**
- **GitHub Actions**：使用 GitHub Actions 擴充功能查看工作流程狀態
- **GitLab CI/CD**：使用 GitLab Workflow 擴充功能監控 Pipeline 狀態
- **即時通知**：CI/CD 狀態變更時接收通知
```

### 6.4 效能優化進階技巧

**記憶體使用優化：**
```json
{
  "files.watcherExclude": {
    "**/.git/objects/**": true,
    "**/node_modules/**": true,
    "**/target/**": true
  },
  "search.followSymlinks": false
}
```

### 6.5 遠端開發與 SSH

#### 6.5.1 Remote SSH 設定

**安裝 Remote SSH 擴充功能：**
```bash
code --install-extension ms-vscode-remote.remote-ssh
```

**SSH 設定檔配置：**
```bash
# ~/.ssh/config
Host dev-server
    HostName 192.168.1.100
    User developer
    Port 22
    IdentityFile ~/.ssh/id_rsa
    ForwardAgent yes
```

**連線到遠端伺服器：**
1. `Ctrl + Shift + P` → `Remote-SSH: Connect to Host`
2. 選擇預設的主機或輸入新的連線
3. VS Code 會在遠端建立伺服器並同步擴充功能

#### 6.5.2 遠端開發最佳實務

**檔案同步策略：**
- 使用 Git 進行版本控制
- 避免直接編輯生產環境檔案
- 設定適當的檔案排除規則

**效能優化：**
```json
{
  "remote.SSH.enableDynamicForwarding": false,
  "remote.SSH.maxReconnectionAttempts": 3,
  "remote.SSH.enableRemoteCommand": true
}
```

### 6.6 工作區管理進階技巧

#### 6.6.1 多根工作區 (Multi-root Workspace)

**建立多根工作區：**
```json
// myproject.code-workspace
{
  "folders": [
    {
      "name": "Frontend",
      "path": "./frontend"
    },
    {
      "name": "Backend",
      "path": "./backend"
    },
    {
      "name": "Documentation",
      "path": "./docs"
    }
  ],
  "settings": {
    "files.exclude": {
      "**/node_modules": true,
      "**/target": true
    }
  },
  "extensions": {
    "recommendations": [
      "ms-vscode.vscode-typescript-next",
      "vscjava.vscode-java-pack"
    ]
  }
}
```

#### 6.6.2 工作區範本

**建立專案範本：**
```bash
# 建立專案範本資料夾
mkdir project-template
cd project-template

# 建立基本結構
mkdir .vscode
touch .vscode/settings.json
touch .vscode/tasks.json
touch .vscode/launch.json
```

**範本設定檔：**
```json
// .vscode/settings.json 範本
{
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll": true
  },
  "java.configuration.updateBuildConfiguration": "automatic",
  "spring.boot.java.mainClass": "com.example.Application"
}
```

---

## 7. 最佳實務

### 7.1 常見問題 (FAQ) 與解決方式

#### 5.1.1 安裝與設定問題

**Q1: VS Code 啟動速度很慢**

**解決方案：**
1. 檢查安裝的擴充功能數量，移除不必要的擴充功能
2. 清理 VS Code 快取：
   ```powershell
   # 關閉 VS Code 後執行
   Remove-Item -Recurse -Force "$env:APPDATA\Code\User\workspaceStorage"
   Remove-Item -Recurse -Force "$env:APPDATA\Code\CachedExtensions"
   ```
3. 使用 `Developer: Reload Window` 重新載入視窗

**Q2: 擴充功能無法正常運作**

**解決方案：**
1. 檢查擴充功能是否為最新版本
2. 重新安裝問題擴充功能
3. 檢查工作區設定是否正確
4. 查看 `Output` 面板的錯誤訊息

**Q3: Java 專案無法正確識別**

**解決方案：**
1. 確認已安裝 "Extension Pack for Java"
2. 檢查 Java 版本：`java -version`
3. 重新匯入專案：`Ctrl + Shift + P` → `Java: Reload Projects`
4. 檢查 `.vscode/settings.json` 中的 Java 路徑設定

#### 5.1.2 開發環境問題

**Q4: 前端熱重載不工作**

**解決方案：**
1. 檢查開發伺服器是否正常啟動
2. 確認檔案監視功能正常：
   ```powershell
   # 增加檔案監視限制
   echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf
   ```
3. 檢查防火牆設定是否阻擋連接埠

**Q5: Git 整合顯示錯誤**

**解決方案：**
1. 檢查 Git 是否正確安裝：`git --version`
2. 設定 Git 使用者資訊：
   ```powershell
   git config --global user.name "Your Name"
   git config --global user.email "your.email@company.com"
   ```
3. 重新初始化 Git 倉庫

**Q6: 偵錯無法啟動**

**解決方案：**
1. 檢查 `launch.json` 設定是否正確
2. 確認專案已正確編譯
3. 檢查連接埠是否被佔用
4. 查看 `Debug Console` 的錯誤訊息

#### 5.1.3 效能最佳化問題

**Q7: 編輯器回應緩慢**

**解決方案：**
1. 關閉不必要的檔案分頁
2. 排除大型檔案和資料夾：
   ```json
   {
     "files.exclude": {
       "**/node_modules": true,
       "**/target": true,
       "**/.git": true,
       "**/dist": true
     }
   }
   ```
3. 調整 TypeScript 服務設定：
   ```json
   {
     "typescript.suggest.enabled": false,
     "typescript.validate.enable": false
   }
   ```

### 7.2 建議的工作習慣

#### 5.2.1 自動化設定

**自動儲存設定：**
```json
{
  "files.autoSave": "onFocusChange",
  "files.autoSaveDelay": 1000
}
```

**自動格式化設定：**
```json
{
  "editor.formatOnSave": true,
  "editor.formatOnPaste": true,
  "editor.formatOnType": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true,
    "source.organizeImports": true,
    "source.removeUnusedImports": true
  }
}
```

**自動完成設定：**
```json
{
  "editor.quickSuggestions": {
    "other": true,
    "comments": false,
    "strings": true
  },
  "editor.suggestOnTriggerCharacters": true,
  "editor.acceptSuggestionOnEnter": "on"
}
```

#### 5.2.2 程式碼品質習慣

**1. 定期 Commit 習慣**
- 每完成一個小功能就提交
- 使用有意義的提交訊息
- 遵循團隊的提交訊息格式

**範例提交訊息格式：**
```
feat: 新增用戶註冊功能
fix: 修正登入驗證問題
docs: 更新 API 文件
style: 調整程式碼格式
refactor: 重構用戶服務層
test: 新增用戶服務測試
```

**2. 程式碼審查習慣**
- 建立 Pull Request 進行程式碼審查
- 使用 GitHub/GitLab 的審查功能
- 遵循團隊的審查標準

**3. 測試習慣**
- 撰寫單元測試
- 執行自動化測試
- 維持高測試覆蓋率

#### 5.2.3 工作區管理習慣

**檔案組織習慣：**
1. 使用一致的檔案命名規則
2. 適當使用資料夾結構
3. 定期清理不需要的檔案

**設定同步習慣：**
1. 使用 VS Code 設定同步功能
2. 備份重要的設定檔案
3. 定期更新擴充功能

### 7.3 效能最佳化

#### 5.3.1 編輯器效能優化

**記憶體使用優化：**
```json
{
  "files.watcherExclude": {
    "**/.git/objects/**": true,
    "**/.git/subtree-cache/**": true,
    "**/node_modules/*/**": true,
    "**/target/**": true
  },
  "search.exclude": {
    "**/node_modules": true,
    "**/target": true,
    "**/dist": true
  }
}
```

**CPU 使用優化：**
```json
{
  "editor.minimap.enabled": false,
  "editor.semanticHighlighting.enabled": false,
  "breadcrumbs.enabled": false,
  "editor.hover.enabled": false
}
```

#### 5.3.2 專案載入優化

**大型專案設定：**
```json
{
  "typescript.preferences.includePackageJsonAutoImports": "off",
  "typescript.suggest.autoImports": false,
  "typescript.surveys.enabled": false,
  "files.exclude": {
    "**/node_modules": true,
    "**/target": true,
    "**/.git": true
  }
}
```

### 7.4 安全性最佳實務

#### 7.4.1 敏感資訊保護

**環境變數使用：**
```javascript
// 正確做法：使用環境變數
const API_KEY = process.env.REACT_APP_API_KEY;
const DB_PASSWORD = process.env.DB_PASSWORD;

// 錯誤做法：直接寫在程式碼中
const API_KEY = "sk-1234567890abcdef"; // 不要這樣做！
```

**VS Code 設定檔案保護：**
```json
// .vscode/settings.json - 不要提交敏感設定
{
  "java.configuration.runtimes": [
    {
      "name": "JavaSE-17",
      "path": "${env:JAVA_HOME}"  // 使用環境變數
    }
  ],
  "spring.datasource.password": "${env:DB_PASSWORD}"
}
```

**設定檔案保護最佳實務：**
1. 將敏感設定加入 `.gitignore`：
   ```gitignore
   # 敏感設定檔
   .env
   .env.local
   .env.production
   application-prod.properties
   
   # VS Code 敏感設定
   .vscode/settings.json
   ```
2. 使用 `.env.example` 提供範本
3. 定期檢查是否有敏感資訊被提交：
   ```powershell
   # 掃描歷史提交中的敏感資訊
   git log --all --full-history -- **/*.env
   ```

#### 7.4.2 憑證與金鑰管理

**GitHub/GitLab 存取權杖安全：**
```json
// 設定檔範例
{
  "github.gitAuthentication": true,
  "gitlab.instanceUrl": "${env:GITLAB_URL}",
  "gitlab.personalAccessToken": "${env:GITLAB_TOKEN}"
}
```

**安全存儲建議：**
- 使用 Windows 憑證管理員
- 定期輪換存取權杖
- 設定權杖到期時間
- 只授予必要的權限範圍

#### 7.4.3 依賴套件安全

**定期更新依賴：**
```powershell
# 前端依賴更新
npm audit
npm audit fix --force

# 檢查過時套件
npm outdated

# 後端依賴檢查
mvn dependency-check:check
mvn versions:display-dependency-updates
```

**使用安全掃描工具：**
- **SonarLint** 擴充功能：即時程式碼品質檢查
- **GitHub Dependabot** alerts：自動依賴安全警告
- **GitLab Dependency Scanning**：CI/CD 整合掃描
- **OWASP Dependency Check**：開源依賴漏洞檢查

**擴充功能安全設定：**
```json
{
  "extensions.autoCheckUpdates": true,
  "extensions.autoUpdate": false,  // 手動審查更新
  "telemetry.telemetryLevel": "off",  // 關閉遙測
  "update.showReleaseNotes": false
}
```

#### 7.4.4 程式碼掃描與分析

**SonarQube 整合：**
```json
// .vscode/settings.json
{
  "sonarlint.connectedMode.project": {
    "connectionId": "your-sonarqube-server",
    "projectKey": "your-project-key"
  }
}
```

**安全編碼檢查清單：**
- [ ] 輸入驗證與 SQL 注入防護
- [ ] XSS 防護
- [ ] CSRF 權杖驗證
- [ ] 敏感資料加密
- [ ] 適當的錯誤處理
- [ ] 安全的認證與授權

#### 7.4.5 開發環境隔離

**容器化開發環境：**
```dockerfile
# .devcontainer/Dockerfile
FROM mcr.microsoft.com/vscode/devcontainers/java:17

# 安全設定
RUN useradd -m -s /bin/bash developer && \
    usermod -aG sudo developer

USER developer
WORKDIR /workspace

# 安裝安全工具
RUN npm install -g audit-ci
```

**網路安全設定：**
```json
// .devcontainer/devcontainer.json
{
  "forwardPorts": [3000, 8080],
  "portsAttributes": {
    "3000": {
      "label": "Frontend Dev Server",
      "requireLocalPort": true
    }
  }
}
```

### 7.5 團隊協作規範

#### 7.5.1 編碼標準統一

**團隊設定同步：**
```json
// 團隊共用 settings.json
{
  "editor.tabSize": 2,
  "editor.insertSpaces": true,
  "editor.formatOnSave": true,
  "editor.formatOnPaste": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true,
    "source.organizeImports": true
  },
  "files.encoding": "utf8",
  "files.eol": "\n",
  "java.format.settings.url": "https://raw.githubusercontent.com/google/styleguide/gh-pages/eclipse-java-google-style.xml"
}
```

**強制格式化規則：**
```json
// .vscode/settings.json (專案層級)
{
  "eslint.workingDirectories": ["frontend"],
  "java.checkstyle.configuration": "/path/to/checkstyle.xml",
  "prettier.configPath": "./.prettierrc",
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "[java]": {
    "editor.defaultFormatter": "redhat.java"
  }
}
```

#### 7.5.2 程式碼審查流程

**審查前自動檢查：**
```json
// .vscode/tasks.json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Pre-commit Check",
      "type": "shell",
      "command": "npm run lint && npm run test && mvn checkstyle:check",
      "group": "build",
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared"
      }
    }
  ]
}
```

**程式碼審查檢查點：**
- [ ] **架構設計**：是否符合專案架構原則
- [ ] **程式碼品質**：可讀性、維護性、複用性
- [ ] **效能考量**：演算法效率、資源使用
- [ ] **安全性**：輸入驗證、權限檢查、敏感資料處理
- [ ] **測試覆蓋**：單元測試、整合測試
- [ ] **文件完整性**：註解、README、API 文件

#### 7.5.3 版本控制協作

**分支命名規範：**
```bash
# 功能開發
feature/user-authentication
feature/payment-integration

# 修復問題
bugfix/login-error
hotfix/security-patch

# 版本發佈
release/v2.1.0
```

**Commit 訊息規範：**
```bash
# 格式：<type>(<scope>): <description>
feat(auth): add JWT token validation
fix(payment): resolve currency conversion bug
docs(readme): update installation instructions
test(user): add unit tests for user service
refactor(api): simplify error handling logic
```

**合併策略設定：**
```json
// .vscode/settings.json
{
  "git.enableSmartCommit": true,
  "git.confirmSync": false,
  "git.autofetch": true,
  "git.pullTags": true,
  "gitlens.codeLens.enabled": true,
  "gitlens.blame.compact": false
}
```
```

---

## 8. 檢查清單

### 8.1 新進成員快速上手檢查清單

#### ✅ 環境安裝檢查

**基本環境：**
- [ ] 安裝 Visual Studio Code
- [ ] 安裝 Git
- [ ] 安裝 Node.js (版本 16+)
- [ ] 安裝 Java (版本 17+)
- [ ] 安裝 Maven (獨立安裝或使用內建版本)
- [ ] 設定 Git 使用者資訊
- [ ] 設定 JAVA_HOME 環境變數
- [ ] 設定 MAVEN_HOME 環境變數 (獨立安裝時)

**Maven 設定檢查：**
- [ ] 設定 `maven.executable.path` 指向正確的 Maven 執行檔
- [ ] 設定 `maven.terminal.customEnv` 環境變數
- [ ] 設定 Maven settings.xml 路徑
- [ ] 驗證 Maven 版本：`mvn -version`
- [ ] 測試 Maven 專案載入功能

**字型與主題：**
- [ ] 安裝推薦字型 (JetBrains Mono 或 Fira Code)
- [ ] 選擇適合的佈景主題
- [ ] 設定字型大小和行高

#### ✅ 擴充功能安裝檢查

**基礎工具：**
- [ ] Chinese (Traditional) Language Pack
- [ ] GitLens
- [ ] Auto Rename Tag
- [ ] Bracket Pair Colorizer 2
- [ ] indent-rainbow
- [ ] Path Intellisense

**前端開發：**
- [ ] Volar (Vue Language Features)
- [ ] TypeScript Importer
- [ ] ESLint
- [ ] Prettier
- [ ] Tailwind CSS IntelliSense
- [ ] Auto Close Tag

**後端開發：**
- [ ] Extension Pack for Java
- [ ] Spring Boot Extension Pack
- [ ] Maven for Java
- [ ] Checkstyle for Java
- [ ] SonarLint

#### ✅ 專案設定檢查

**工作區設定：**
- [ ] 建立 `.vscode/settings.json`
- [ ] 建立 `.vscode/extensions.json`
- [ ] 建立 `.vscode/launch.json`
- [ ] 建立 `.vscode/tasks.json`
- [ ] 設定專案特定的程式碼格式化規則

**Git 整合：**
- [ ] 連結 GitHub/GitLab 帳號
- [ ] 設定 SSH 金鑰
- [ ] 測試 Git 操作功能
- [ ] 設定 `.gitignore` 檔案

### 8.2 日常開發檢查清單

#### ✅ 開發前檢查

**環境準備：**
- [ ] 更新到最新的 VS Code 版本
- [ ] 檢查擴充功能更新
- [ ] 拉取最新的程式碼變更
- [ ] 確認開發分支正確

**專案狀態：**
- [ ] 檢查依賴套件更新
- [ ] 執行單元測試
- [ ] 檢查程式碼品質掃描結果
- [ ] 確認開發伺服器正常運作

#### ✅ 開發中檢查

**程式碼品質：**
- [ ] 遵循專案編碼規範
- [ ] 執行格式化檢查
- [ ] 處理 Linting 警告
- [ ] 撰寫適當的註解

**功能開發：**
- [ ] 撰寫單元測試
- [ ] 執行功能測試
- [ ] 檢查錯誤處理機制
- [ ] 驗證效能影響

#### ✅ 提交前檢查

**程式碼審查：**
- [ ] 自我程式碼審查
- [ ] 檢查是否有調試程式碼殘留
- [ ] 確認敏感資訊已移除
- [ ] 檢查 import 和依賴項

**測試驗證：**
- [ ] 執行完整測試套件
- [ ] 檢查測試覆蓋率
- [ ] 執行整合測試
- [ ] 驗證 CI/CD Pipeline 通過

### 8.3 部署前檢查清單

#### ✅ 生產環境準備

**環境設定：**
- [ ] 檢查環境變數設定
- [ ] 確認資料庫連線設定
- [ ] 檢查 API 端點配置
- [ ] 驗證 CORS 設定

**安全性檢查：**
- [ ] 移除開發用的 debug 模式
- [ ] 檢查 API 金鑰和密碼保護
- [ ] 確認 HTTPS 設定
- [ ] 執行安全性掃描

**效能檢查：**
- [ ] 執行效能測試
- [ ] 檢查資源使用情況
- [ ] 優化圖片和靜態資源
- [ ] 檢查快取設定

**CI/CD 檢查：**
- [ ] GitHub Actions 或 GitLab CI/CD Pipeline 成功執行
- [ ] 所有測試通過
- [ ] 程式碼審查已完成
- [ ] 部署腳本已驗證
- [ ] 回滾計劃已準備

### 8.4 故障排除檢查清單

#### ✅ 常見問題診斷

**VS Code 問題：**
- [ ] 重新啟動 VS Code
- [ ] 重新載入視窗 (`Developer: Reload Window`)
- [ ] 檢查擴充功能狀態
- [ ] 查看輸出和問題面板

**專案問題：**
- [ ] 清理並重新建置專案
- [ ] 重新安裝依賴套件
- [ ] 檢查 Node.js/Java 版本
- [ ] 確認路徑和檔案權限

**Git 問題：**
- [ ] 檢查 Git 狀態：`git status`
- [ ] 解決合併衝突
- [ ] 檢查遠端分支連線
- [ ] 重新設定 Git 認證

**效能問題：**
- [ ] 檢查 CPU 和記憶體使用率
- [ ] 關閉不必要的擴充功能
- [ ] 清理工作區快取
- [ ] 優化檔案監視設定

---

## 9. 附錄

### 9.1 參考資源

**官方文件：**
- [Visual Studio Code 官方文件](https://code.visualstudio.com/docs)
- [Vue.js 官方文件](https://vuejs.org/)
- [Spring Boot 官方文件](https://spring.io/projects/spring-boot)
- [TypeScript 官方文件](https://www.typescriptlang.org/docs/)

**學習資源：**
- [VS Code Tips and Tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)
- [Java 在 VS Code 中的使用](https://code.visualstudio.com/docs/languages/java)
- [TypeScript 開發指南](https://code.visualstudio.com/docs/languages/typescript)
- [Remote Development 指南](https://code.visualstudio.com/docs/remote/remote-overview)

**社群資源：**
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/)
- [GitHub VS Code Repository](https://github.com/microsoft/vscode)
- [VS Code YouTube Channel](https://www.youtube.com/channel/UCs5Y5_7XK8HLDX0SLNwkd3w)

**工具與擴充功能：**
- [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)
- [SonarLint](https://marketplace.visualstudio.com/items?itemName=SonarSource.sonarlint-vscode)
- [Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

### 9.2 聯絡支援

**技術支援管道：**
- 技術支援：`tech-support@yourcompany.com`
- 開發團隊：`dev-team@yourcompany.com`
- 專案經理：`pm@yourcompany.com`

**內部資源：**
- 內部技術文件庫：`https://docs.yourcompany.com`
- 開發團隊 Slack：`#dev-team`
- VS Code 討論群組：`#vscode-help`

**緊急支援：**
- 24/7 技術熱線：`+886-xxx-xxx-xxx`
- 緊急事件通報：`emergency@yourcompany.com`

### 9.3 版本歷程

| 版本 | 日期 | 更新內容 | 作者 |
|------|------|----------|------|
| 2.0 | 2025-08-29 | 新增 GitLab 整合、安全性最佳實務、遠端開發 | 開發團隊 |
| 1.5 | 2025-08-01 | 新增 CI/CD 整合、容器化開發環境 | 開發團隊 |
| 1.0 | 2025-07-01 | 初版發佈，基本功能教學 | 開發團隊 |

---

*文件版本：2.0*  
*最後更新：2025年8月29日*  
*維護團隊：開發部技術團隊*

**程式碼品質：**
- [ ] 定期執行 Lint 檢查
- [ ] 修正所有 Lint 警告和錯誤
- [ ] 確保程式碼格式化正確
- [ ] 撰寫適當的註解和文件

**測試覆蓋：**
- [ ] 撰寫單元測試
- [ ] 執行所有測試並確保通過
- [ ] 檢查測試覆蓋率
- [ ] 進行手動測試

#### ✅ 提交前檢查

**程式碼審查：**
- [ ] 檢查所有變更檔案
- [ ] 移除 console.log 和 debug 程式碼
- [ ] 確認沒有提交敏感資訊
- [ ] 檢查 .gitignore 是否正確

**測試執行：**
- [ ] 執行完整測試套件
- [ ] 檢查建置是否成功
- [ ] 進行跨瀏覽器測試（前端）
- [ ] 測試 API 端點（後端）

### 8.3 部署前檢查清單

#### ✅ 生產環境準備

**環境設定：**
- [ ] 檢查環境變數設定
- [ ] 確認資料庫連線設定
- [ ] 檢查 API 端點配置
- [ ] 驗證 CORS 設定

**安全性檢查：**
- [ ] 移除開發用的 debug 模式
- [ ] 檢查 API 金鑰和密碼保護
- [ ] 確認 HTTPS 設定
- [ ] 執行安全性掃描

**效能檢查：**
- [ ] 執行效能測試
- [ ] 檢查資源使用情況
- [ ] 優化圖片和靜態資源
- [ ] 檢查快取設定

**CI/CD 檢查：**
- [ ] GitHub Actions 或 GitLab CI/CD Pipeline 成功執行
- [ ] 所有測試通過
- [ ] 程式碼審查已完成
- [ ] 部署腳本已驗證
- [ ] 回滾計劃已準備

### 8.4 故障排除檢查清單

#### ✅ 常見問題診斷

**VS Code 問題：**
- [ ] 重新啟動 VS Code
- [ ] 重新載入視窗 (`Developer: Reload Window`)
- [ ] 檢查擴充功能狀態
- [ ] 查看輸出和問題面板

**專案問題：**
- [ ] 清理並重新建置專案
- [ ] 重新安裝依賴套件
- [ ] 檢查 Node.js/Java 版本
- [ ] 確認路徑和檔案權限

**Git 問題：**
- [ ] 檢查 Git 狀態：`git status`
- [ ] 解決合併衝突
- [ ] 檢查遠端分支連線
- [ ] 重新設定 Git 認證

---

## 9. 附錄

### 9.1 參考資源

**官方文件：**
- [Visual Studio Code 官方文件](https://code.visualstudio.com/docs)
- [Vue.js 官方文件](https://vuejs.org/)
- [Spring Boot 官方文件](https://spring.io/projects/spring-boot)

**學習資源：**
- [VS Code Tips and Tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)
- [Java 在 VS Code 中的使用](https://code.visualstudio.com/docs/languages/java)
- [TypeScript 開發指南](https://code.visualstudio.com/docs/languages/typescript)

### 9.2 聯絡支援

如有任何問題或建議，請聯絡：
- 技術支援：`tech-support@yourcompany.com`
- 開發團隊：`dev-team@yourcompany.com`

---

*文件版本：2.0*  
*最後更新：2025年8月*  
*維護者：開發團隊*
