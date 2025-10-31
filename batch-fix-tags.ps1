$postsPath = "d:\developer\repos\Blog\content\posts"
$files = Get-ChildItem -Path $postsPath -Recurse -Filter "*.md" | Where-Object { $_.Name -ne "_index.md" }
$count = 0

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    
    if ($content -match "'D:'") {
        $fullPath = $file.Directory.FullName
        
        if ($fullPath.StartsWith($postsPath)) {
            $relativePath = $fullPath.Substring($postsPath.Length).TrimStart("\")
            
            if (-not [string]::IsNullOrEmpty($relativePath)) {
                $pathParts = @($relativePath -split "\\" | Where-Object { $_ -ne "" })
                
                if ($pathParts.Count -gt 0) {
                    $newTags = "'" + ($pathParts -join "', '") + "'"
                    $category = $pathParts[0]
                    
                    $newContent = $content -replace "tags\s*=\s*\[[^\]]+\]", "tags = [$newTags]"
                    $newContent = $newContent -replace "categories\s*=\s*\[[^\]]+\]", "categories = ['$category']"
                    
                    Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8 -NoNewline
                    $count++
                    Write-Host "Fixed: $($file.Name)"
                }
            }
        }
    }
}

Write-Host "Total fixed: $count files" -ForegroundColor Green
