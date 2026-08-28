param(
    [Parameter(Mandatory = $true)][string]$Path
)

$lines = Get-Content -LiteralPath $Path -Encoding UTF8
$n = $lines.Count
$issues = @()

$inCode = $false
$fenceLangMissing = @()
for ($i = 0; $i -lt $n; $i++) {
    $l = $lines[$i]
    $ln = $i + 1

    if ($l -match '^\s*```') {
        if (-not $inCode) {
            $inCode = $true
            if ($l -match '^\s*```\s*$') { $fenceLangMissing += $ln }
        }
        else { $inCode = $false }
        continue
    }
    if ($inCode) { continue }

    if ($l -match '\s+$') { $issues += "MD009 行尾空白           L$ln" }
    if ($l -match "`t") { $issues += "MD010 內含 Tab          L$ln" }

    if ($l -match '^#{1,6}\s') {
        if ($i -gt 0 -and $lines[$i - 1].Trim() -ne '') { $issues += "MD022 標題前缺空行       L$ln  $l" }
        if ($i -lt $n - 1 -and $lines[$i + 1].Trim() -ne '') { $issues += "MD022 標題後缺空行       L$ln  $l" }
        if ($l -match '\s+$') { $issues += "MD023 標題行尾空白       L$ln" }
    }

    # 表格：第一列前需空行
    if ($l -match '^\s*\|' -and $i -gt 0 -and $lines[$i - 1] -notmatch '^\s*\|' -and $lines[$i - 1].Trim() -ne '') {
        $issues += "MD058 表格前缺空行       L$ln"
    }
    if ($l -match '^\s*\|' -and $i -lt $n - 1 -and $lines[$i + 1] -notmatch '^\s*\|' -and $lines[$i + 1].Trim() -ne '') {
        $issues += "MD058 表格後缺空行       L$ln"
    }

    # 清單前需空行
    if ($l -match '^\s*([-*+]|\d+\.)\s' -and $i -gt 0) {
        $prev = $lines[$i - 1]
        if ($prev.Trim() -ne '' -and $prev -notmatch '^\s*([-*+]|\d+\.)\s' -and $prev -notmatch '^\s{2,}\S') {
            $issues += "MD032 清單前缺空行       L$ln  $l"
        }
    }
}

if ($inCode) { $issues += "MD040 程式碼區塊未關閉（檔尾）" }

Write-Output "=== 未標語言的程式碼區塊 (MD040) ==="
if ($fenceLangMissing.Count -eq 0) { Write-Output "  (無)" } else { $fenceLangMissing | ForEach-Object { Write-Output "  L$_" } }

Write-Output ""
Write-Output "=== 其他格式問題 (共 $($issues.Count) 筆) ==="
$issues | Group-Object { ($_ -split '\s+')[0] } | Sort-Object Name | ForEach-Object {
    Write-Output ("  {0} : {1} 筆" -f $_.Name, $_.Count)
}
Write-Output ""
Write-Output "--- 明細（前 80 筆）---"
$issues | Select-Object -First 80 | ForEach-Object { Write-Output "  $_" }
