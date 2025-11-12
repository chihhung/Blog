# 修復 Mermaid ClassDiagram 中的 interface 語法
param(
    [Parameter(Mandatory=$false)]
    [string]$FilePath
)

$encoding = New-Object System.Text.UTF8Encoding $false

if ($FilePath) {
    $files = @($FilePath)
} else {
    # 預設處理所有 Design Pattern 教學文件
    $files = @(
        "content\posts\教學\分析與設計\Design Pattern教學.md",
        "content\posts\教學\分析與設計\Design Pattern教學(二).md"
    )
}

foreach ($file in $files) {
    if (-not (Test-Path $file)) {
        Write-Host "檔案不存在: $file" -ForegroundColor Red
        continue
    }
    
    Write-Host "處理檔案: $file" -ForegroundColor Cyan
    
    # 建立備份
    $backupFile = "$file.backup_interface"
    Copy-Item -Path $file -Destination $backupFile -Force
    Write-Host "已建立備份: $backupFile" -ForegroundColor Green
    
    # 讀取檔案內容
    $content = [System.IO.File]::ReadAllText($file, $encoding)
    $originalContent = $content
    
    # 替換 <<interface>> 為 <<Interface>> (Mermaid v11 要求首字母大寫)
    # 在 mermaid 程式碼區塊中
    $content = $content -replace '(\s+)<<interface>>', '$1<<Interface>>'
    
    # 計算變更次數
    $changes = ($originalContent.Length - $content.Length) / ('<<interface>>'.Length - '<<Interface>>'.Length)
    
    if ($content -ne $originalContent) {
        # 寫回檔案
        [System.IO.File]::WriteAllText($file, $content, $encoding)
        Write-Host "已修復 $([int]$changes) 處 interface 語法" -ForegroundColor Green
    } else {
        Write-Host "未發現需要修復的內容" -ForegroundColor Yellow
    }
    
    Write-Host ""
}

Write-Host "處理完成！" -ForegroundColor Green
Write-Host "請執行 hugo 重新生成網站" -ForegroundColor Yellow
