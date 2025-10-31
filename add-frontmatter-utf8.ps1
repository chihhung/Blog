# 正確處理 UTF-8 編碼的腳本
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$postsPath = "d:\developer\repos\Blog\content\posts"

# 第一步：為所有檔案添加 Front Matter
$files = Get-ChildItem -Path $postsPath -Recurse -Filter "*.md" | Where-Object { $_.Name -ne "_index.md" }

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    
    # 檢查是否已有 Front Matter
    if ($content -notmatch '^(\+\+\+|---)') {
        # 從路徑提取分類和標籤
        $fullPath = $file.Directory.FullName
        $relativePath = $fullPath.Substring($postsPath.Length).TrimStart("\")
        
        if ([string]::IsNullOrEmpty($relativePath)) {
            continue
        }
        
        $pathParts = @($relativePath -split "\\" | Where-Object { $_ -ne "" })
        
        if ($pathParts.Count -eq 0) {
            continue
        }
        
        # 建立標籤和分類
        $tags = "'" + ($pathParts -join "', '") + "'"
        $category = $pathParts[0]
        $title = $file.BaseName
        
        # 建立 Front Matter
        $frontMatter = @"
+++
date = '2025-10-31T00:00:00+08:00'
draft = false
title = '$title'
tags = [$tags]
categories = ['$category']
+++

"@
        
        # 添加到檔案開頭
        $newContent = $frontMatter + $content
        
        # 使用正確的編碼寫入
        [System.IO.File]::WriteAllText($file.FullName, $newContent, [System.Text.Encoding]::UTF8)
        
        Write-Host "已處理: $($file.Name)" -ForegroundColor Green
    }
}

Write-Host "Complete!" -ForegroundColor Cyan
