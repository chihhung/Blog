# 批量添加 Hugo Front Matter 的腳本

$postsPath = "d:\developer\repos\Blog\content\posts"

# 定義分類和標籤對應
$categoryMap = @{
    "prompts" = "prompts"
    "指引" = "指引"
    "教學" = "教學"
    "範本" = "範本"
    "專案管理" = "專案管理"
    "設計開發" = "設計開發"
    "需求分析" = "需求分析"
    "部署運維" = "部署運維"
    "測試驗收" = "測試驗收"
    "工具" = "工具"
    "分析與設計" = "分析與設計"
    "程式語言" = "程式語言"
    "framework" = "framework"
}

$tagMap = @{
    "專案管理" = @("專案管理", "指引")
    "設計開發" = @("設計開發", "指引", "開發指南")
    "需求分析" = @("需求分析", "指引")
    "部署運維" = @("部署", "運維", "DevOps")
    "測試驗收" = @("測試", "驗收", "品質保證")
    "prompts" = @("prompts", "AI工具")
    "工具" = @("工具", "教學")
    "分析與設計" = @("分析與設計", "教學")
    "程式語言" = @("程式語言", "教學")
    "framework" = @("framework", "教學")
}

# 獲取所有需要添加 Front Matter 的檔案
$files = Get-ChildItem -Path $postsPath -Recurse -Filter "*.md" | Where-Object { 
    $_.Name -ne "_index.md" 
}

$count = 0
foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw -ErrorAction SilentlyContinue
    
    # 檢查是否已有 Front Matter
    if ($content -and $content -notmatch '^(\+\+\+|---)') {
        # 從檔案路徑中提取分類
        $relativePath = $file.DirectoryName.Replace($postsPath, "").TrimStart("\")
        $pathParts = $relativePath -split "\\"
        
        $category = "技術"
        $tags = @()
        
        # 根據路徑確定分類和標籤
        if ($pathParts.Count -gt 0) {
            $firstLevel = $pathParts[0]
            if ($categoryMap.ContainsKey($firstLevel)) {
                $category = $categoryMap[$firstLevel]
            }
            
            if ($tagMap.ContainsKey($firstLevel)) {
                $tags = $tagMap[$firstLevel]
            }
            
            # 添加子分類作為標籤
            if ($pathParts.Count -gt 1) {
                $tags += $pathParts[1]
            }
        }
        
        # 從檔名生成標題（移除 .md 和數字前綴）
        $title = $file.BaseName -replace '^\d+[-_]', '' -replace '[-_]', ' '
        
        # 生成標籤字串
        $tagsStr = if ($tags.Count -gt 0) { 
            "'" + ($tags -join "', '") + "'" 
        } else { 
            "'文件'" 
        }
        
        # 建立 Front Matter
        $frontMatter = @"
+++
date = '2025-10-31T00:00:00+08:00'
draft = false
title = '$title'
tags = [$tagsStr]
categories = ['$category']
+++

"@
        
        # 添加 Front Matter 到檔案開頭
        $newContent = $frontMatter + $content
        Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8
        
        $count++
        Write-Host "已處理: $($file.FullName)" -ForegroundColor Green
    }
}

Write-Host "`n總共處理了 $count 個檔案" -ForegroundColor Cyan
