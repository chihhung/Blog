# 測試 Mermaid 語法腳本
param(
    [Parameter(Mandatory=$true)]
    [string]$FilePath
)

# 讀取文件內容
$content = Get-Content -Path $FilePath -Raw -Encoding UTF8

# 檢查潛在的語法問題
$issues = @()

# 1. 檢查 timeline 語法
if ($content -match '```mermaid[\s\S]*?timeline[\s\S]*?```') {
    $issues += "發現 timeline 圖表 - Mermaid v11 可能不完全支援"
}

# 2. 檢查 note 語法
if ($content -match 'note (for|over|left of|right of)') {
    $issues += "發現 note 語法 - Mermaid v11 已移除此功能"
}

# 3. 檢查類圖中的註解
if ($content -match '```mermaid[\s\S]*?classDiagram[\s\S]*?%%[\s\S]*?```') {
    $issues += "發現 classDiagram 中的註解 - 請確認格式正確"
}

# 4. 提取所有 mermaid 區塊
$pattern = '```mermaid([\s\S]*?)```'
$matches = [regex]::Matches($content, $pattern)

Write-Host "檔案: $FilePath" -ForegroundColor Cyan
Write-Host "找到 $($matches.Count) 個 Mermaid 圖表" -ForegroundColor Green
Write-Host ""

$blockNum = 1
foreach ($match in $matches) {
    $mermaidCode = $match.Groups[1].Value.Trim()
    $firstLine = ($mermaidCode -split "`n")[0]
    
    Write-Host "圖表 $blockNum`: $firstLine" -ForegroundColor Yellow
    
    # 檢查特定語法
    if ($mermaidCode -match 'timeline') {
        Write-Host "  ⚠ 包含 timeline" -ForegroundColor Red
    }
    if ($mermaidCode -match 'note (for|over|left of|right of)') {
        Write-Host "  ⚠ 包含 note 語法" -ForegroundColor Red
    }
    if ($mermaidCode -match 'classDiagram' -and $mermaidCode -match '<<interface>>') {
        Write-Host "  ✓ 包含 interface 標記" -ForegroundColor Green
    }
    
    $blockNum++
}

Write-Host ""
if ($issues.Count -eq 0) {
    Write-Host "✓ 未發現明顯的語法問題" -ForegroundColor Green
} else {
    Write-Host "發現以下潛在問題:" -ForegroundColor Red
    $issues | ForEach-Object { Write-Host "  - $_" -ForegroundColor Red }
}
