# 根據目錄路徑更新 Hugo Front Matter 的 tags

$postsPath = "d:\developer\repos\Blog\content\posts"

# 獲取所有 markdown 檔案
$files = Get-ChildItem -Path $postsPath -Recurse -Filter "*.md" | Where-Object { 
    $_.Name -ne "_index.md" 
}

$count = 0
foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8 -ErrorAction SilentlyContinue
    
    if ($content -and $content -match '^(\+\+\+)') {
        # 從檔案路徑中提取所有目錄名稱作為標籤（相對於 posts 目錄）
        $fullPath = $file.Directory.FullName
        
        # 檢查路徑是否在 postsPath 下
        if (-not $fullPath.StartsWith($postsPath)) {
            continue
        }
        
        # 移除 postsPath，保留相對路徑
        $relativePath = $fullPath.Substring($postsPath.Length).TrimStart("\")
        
        # 如果檔案直接在 posts 目錄下，跳過
        if ([string]::IsNullOrEmpty($relativePath)) {
            continue
        }
        
        # 將所有路徑部分作為標籤
        $pathParts = @($relativePath -split "\\" | Where-Object { $_ -ne "" -and $_ -ne "" })
        
        if ($pathParts.Count -eq 0) {
            continue
        }
        
        $tags = $pathParts
        
        # 讀取現有的 Front Matter
        if ($content -match '(?s)^\+\+\+\s*\n(.*?)\n\+\+\+') {
            $frontMatterBlock = $matches[1]
            
            # 提取現有的 title
            $title = ""
            if ($frontMatterBlock -match "title\s*=\s*'([^']*)'") {
                $title = $matches[1]
            }
            
            # 提取現有的 categories
            $categories = ""
            if ($frontMatterBlock -match "categories\s*=\s*\[([^\]]*)\]") {
                $categories = $matches[1]
            }
            
            # 提取現有的 date
            $date = ""
            if ($frontMatterBlock -match "date\s*=\s*'([^']*)'") {
                $date = $matches[1]
            }
            
            # 提取現有的 draft
            $draft = "false"
            if ($frontMatterBlock -match "draft\s*=\s*(true|false)") {
                $draft = $matches[1]
            }
            
            # 生成新的標籤字串
            $tagsStr = "'" + ($tags -join "', '") + "'"
            
            # 建立新的 Front Matter
            $newFrontMatter = @"
+++
date = '$date'
draft = $draft
title = '$title'
tags = [$tagsStr]
categories = [$categories]
+++
"@
            
            # 替換 Front Matter
            $newContent = $content -replace '(?s)^\+\+\+\s*\n.*?\n\+\+\+', $newFrontMatter
            
            # 寫回檔案
            Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8
            
            $count++
            Write-Host "已更新: $($file.FullName)" -ForegroundColor Green
            Write-Host "  標籤: $tagsStr" -ForegroundColor Yellow
        }
    }
}

Write-Host "`n總共更新了 $count 個檔案的標籤" -ForegroundColor Cyan
