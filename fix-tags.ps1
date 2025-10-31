# 批量修正 tags - 只保留相對路徑的目錄名稱

$postsPath = "d:\developer\repos\Blog\content\posts"

$files = Get-ChildItem -Path $postsPath -Recurse -Filter "*.md" | Where-Object { 
    $_.Name -ne "_index.md" 
}

$count = 0
foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    
    if ($content -match '(?s)^\+\+\+(.*?)\+\+\+') {
        $fullPath = $file.Directory.FullName
        
        # 取得相對路徑
        if ($fullPath.StartsWith($postsPath)) {
            $relativePath = $fullPath.Substring($postsPath.Length).TrimStart("\")
            
            if ([string]::IsNullOrEmpty($relativePath)) {
                continue
            }
            
            # 取得目錄名稱作為標籤
            $pathParts = @($relativePath -split "\\" | Where-Object { $_ -ne "" })
            
            if ($pathParts.Count -eq 0) {
                continue
            }
            
            # 建立新的標籤字串
            $newTags = "'" + ($pathParts -join "', '") + "'"
            
            # 檢查是否有錯誤的標籤（包含 'D:' 的）
            if ($content -match "'D:'") {
                # 替換 tags
                $newContent = $content -replace "tags\s*=\s*\[[^\]]+\]", "tags = [$newTags]"
                
                # 同時修正 categories
                $category = $pathParts[0]
                $newContent = $newContent -replace "categories\s*=\s*\[[^\]]+\]", "categories = ['$category']"
                
                Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8 -NoNewline
                $count++
                Write-Host "Fixed: $($file.Name)" -ForegroundColor Green
                Write-Host "  Tags: $newTags" -ForegroundColor Yellow
                Write-Host "  Category: $category" -ForegroundColor Cyan
            }
        }
    }
}

Write-Host "Total fixed: $count files" -ForegroundColor Cyan
