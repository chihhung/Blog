# 修正 TDD 教學手冊的 Markdown 格式問題
$filePath = "d:\developer\repos\Blog\content\doc\教學\分析與設計\TDD(Test-Driven Development)測試驅動開發教學手冊使用教學.md"

Write-Host "讀取檔案..." -ForegroundColor Cyan
$content = Get-Content $filePath -Raw -Encoding UTF8

Write-Host "修正格式問題..." -ForegroundColor Cyan

# 1. 修正列表前後的空行 (MD032)
# 在數字列表前添加空行 (如果前面不是空行或標題)
$content = $content -replace '(?<!\n\n)(\n\d+\.\s)', "`n`n`$1"
# 在項目列表前添加空行
$content = $content -replace '(?<!\n\n)(\n[-*]\s)', "`n`n`$1"
# 在列表後添加空行 (如果後面是段落文字)
$content = $content -replace '(\n[-*]\s[^\n]+\n)(?!\n|[-*]|\d+\.)', "`$1`n"

# 2. 修正程式碼區塊前後的空行 (MD031)
# 在程式碼區塊前添加空行
$content = $content -replace '(?<!\n\n)(\n```)', "`n`n`$1"
# 在程式碼區塊後添加空行  
$content = $content -replace '(```\n)(?!\n)', "`$1`n"

# 3. 修正沒有語言標記的程式碼區塊 (MD040)
# 尋找空的程式碼標記並添加 text
$content = $content -replace '```(\r?\n)(?!java|python|javascript|typescript|xml|yaml|yml|json|groovy|gherkin|markdown|bash|shell|powershell|sql|text|mermaid)', '```text$1'

# 4. 修正 MD036 (強調作為標題) - 將 **數字.** 格式改為 #### 標題
$content = $content -replace '\n\*\*(\d+\.\s+[^\*]+)\*\*\n', "`n#### $1`n`n"

# 5. 處理重複的空行 (超過2個空行合併為2個)
$content = $content -replace '\n\n\n+', "`n`n"

Write-Host "寫入修正後的檔案..." -ForegroundColor Cyan
$content | Set-Content $filePath -Encoding UTF8 -NoNewline

Write-Host "完成!" -ForegroundColor Green
Write-Host "已修正以下格式問題:" -ForegroundColor Yellow
Write-Host "  - MD032: 列表前後的空行" -ForegroundColor Yellow
Write-Host "  - MD031: 程式碼區塊前後的空行" -ForegroundColor Yellow
Write-Host "  - MD040: 程式碼區塊語言標記" -ForegroundColor Yellow
Write-Host "  - MD036: 強調作為標題" -ForegroundColor Yellow
Write-Host "  - 清理多餘的空行" -ForegroundColor Yellow
