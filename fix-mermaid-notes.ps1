# 修正 Mermaid classDiagram 中的 note 語法
# Mermaid v11+ 不支援 note for 語法，需要移除或改為註解

$files = @(
    "d:\developer\repos\Blog\content\posts\教學\分析與設計\統一建模語言(UML)教學.md"
)

foreach ($filePath in $files) {
    Write-Host "`n處理檔案: $filePath" -ForegroundColor Cyan
    
    if (-not (Test-Path $filePath)) {
        Write-Host "  檔案不存在，跳過" -ForegroundColor Yellow
        continue
    }
    
    # 讀取檔案內容
    $content = Get-Content -Path $filePath -Raw -Encoding UTF8
    
    # 備份原檔案
    $backupPath = $filePath + ".backup_notes"
    Copy-Item -Path $filePath -Destination $backupPath -Force
    Write-Host "  已備份原檔案" -ForegroundColor Green
    
    # 處理內容
    $lines = $content -split "`r?`n"
    $inMermaidBlock = $false
    $inClassDiagram = $false
    $result = @()
    $notesRemoved = 0
    
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
        
        # 如果在 classDiagram 中，移除 note for/over/left/right 語法
        if ($inMermaidBlock -and $inClassDiagram) {
            # 檢查是否為 note 語句
            if ($line -match '^\s*note\s+(for|over|left of|right of)\s+') {
                Write-Host "  移除: $($line.Trim())" -ForegroundColor Yellow
                $notesRemoved++
                # 不加入結果（移除此行）
                continue
            }
        }
        
        # 保留其他行
        $result += $line
    }
    
    # 寫回檔案
    $newContent = $result -join "`r`n"
    [System.IO.File]::WriteAllText($filePath, $newContent, [System.Text.Encoding]::UTF8)
    
    Write-Host "  完成！移除了 $notesRemoved 個 note 語句" -ForegroundColor Green
}

Write-Host "`n所有檔案處理完成！" -ForegroundColor Green
Write-Host "請檢查修改後的檔案，如有問題可從 .backup_notes 檔案還原" -ForegroundColor Cyan
