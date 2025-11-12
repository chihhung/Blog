# 修正 Mermaid classDiagram 語法
# 將 method(): Type 改為 method() Type
# 將 field: Type 改為 field Type
# 將 --> Class: label 改為 --> Class : label (冒號前後加空格)

$filePath = "d:\developer\repos\Blog\content\posts\教學\分析與設計\Design Pattern教學(二).md"

# 讀取檔案內容
$content = Get-Content -Path $filePath -Raw -Encoding UTF8

# 備份原檔案
$backupPath = $filePath + ".backup"
Copy-Item -Path $filePath -Destination $backupPath -Force
Write-Host "已備份原檔案至: $backupPath" -ForegroundColor Green

# 標記是否在 mermaid classDiagram 區塊中
$lines = $content -split "`r?`n"
$inMermaidBlock = $false
$inClassDiagram = $false
$result = @()

for ($i = 0; $i -lt $lines.Count; $i++) {
    $line = $lines[$i]
    
    # 檢查是否進入 mermaid 區塊
    if ($line -match '```mermaid') {
        $inMermaidBlock = $true
        $result += $line
        continue
    }
    
    # 檢查是否離開 mermaid 區塊
    if ($inMermaidBlock -and $line -match '```$') {
        $inMermaidBlock = $false
        $inClassDiagram = $false
        $result += $line
        continue
    }
    
    # 檢查是否是 classDiagram
    if ($inMermaidBlock -and $line -match '^\s*classDiagram\s*$') {
        $inClassDiagram = $true
        $result += $line
        continue
    }
    
    # 如果在 classDiagram 中，進行替換
    if ($inMermaidBlock -and $inClassDiagram) {
        $originalLine = $line
        
        # 修正方法返回類型: method(): Type -> method() Type
        # 匹配 +method(): Type 或 -method(): Type 等
        $line = $line -replace '(\+|-|#|~)([a-zA-Z_][a-zA-Z0-9_]*)\(\):\s*([a-zA-Z_][a-zA-Z0-9_<>,\[\]]*)', '$1$2() $3'
        
        # 修正方法參數返回類型: method(param): Type -> method(param) Type
        $line = $line -replace '(\+|-|#|~)([a-zA-Z_][a-zA-Z0-9_]*)\(([^)]*)\):\s*([a-zA-Z_][a-zA-Z0-9_<>,\[\]]*)', '$1$2($3) $4'
        
        # 修正 static 方法: +static method(): Type -> +static method() Type
        $line = $line -replace '(static\s+)([a-zA-Z_][a-zA-Z0-9_]*)\(\):\s*([a-zA-Z_][a-zA-Z0-9_<>,\[\]]*)', '$1$2() $3'
        $line = $line -replace '(static\s+)([a-zA-Z_][a-zA-Z0-9_]*)\(([^)]*)\):\s*([a-zA-Z_][a-zA-Z0-9_<>,\[\]]*)', '$1$2($3) $4'
        
        # 修正欄位類型: -field: Type -> -field Type
        $line = $line -replace '^(\s*)(\+|-|#|~)(static\s+)?([a-zA-Z_][a-zA-Z0-9_]*):\s*([a-zA-Z_][a-zA-Z0-9_<>,\[\]]*)', '$1$2$3$4 $5'
        
        # 修正關係中的標籤: --> Class: label -> --> Class : label
        $line = $line -replace '(-->|<--|\.\.>|<\.\.|--|\.\.|<\|--|\|>--)\s*([a-zA-Z_][a-zA-Z0-9_]*):(\S)', '$1 $2 : $3'
        
        if ($originalLine -ne $line) {
            Write-Host "修正第 $($i+1) 行:" -ForegroundColor Yellow
            Write-Host "  原始: $originalLine" -ForegroundColor Red
            Write-Host "  修正: $line" -ForegroundColor Green
        }
        
        $result += $line
    }
    else {
        $result += $line
    }
}

# 寫回檔案
$newContent = $result -join "`r`n"
Set-Content -Path $filePath -Value $newContent -Encoding UTF8 -NoNewline

Write-Host "`n修正完成!" -ForegroundColor Green
Write-Host "已處理檔案: $filePath" -ForegroundColor Cyan
Write-Host "如需還原,請執行: Copy-Item '$backupPath' '$filePath' -Force" -ForegroundColor Yellow
