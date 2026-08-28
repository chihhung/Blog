param(
    [Parameter(Mandatory = $true)][string]$Path
)

$lines = Get-Content -LiteralPath $Path -Encoding UTF8

function Get-Anchor([string]$text) {
    # 模擬 Hugo/GoldMark（GitHub 風格）的 heading ID 產生規則
    $t = $text.Trim()
    $t = $t.ToLowerInvariant()
    # 移除除了 中日韓/字母/數字/空白/連字號/底線 以外的字元
    $sb = New-Object System.Text.StringBuilder
    foreach ($ch in $t.ToCharArray()) {
        if ([char]::IsLetterOrDigit($ch) -or $ch -eq ' ' -or $ch -eq '-' -or $ch -eq '_') {
            [void]$sb.Append($ch)
        }
    }
    # GitHub/GoldMark 規則：空白逐一換成連字號，不做連續合併
    $t = $sb.ToString().Replace(' ', '-')
    return $t
}

# 收集內文標題（排除程式碼區塊內的 #）
$inCode = $false
$headings = @()
for ($i = 0; $i -lt $lines.Count; $i++) {
    $l = $lines[$i]
    if ($l -match '^\s*```') { $inCode = -not $inCode; continue }
    if ($inCode) { continue }
    if ($l -match '^(#{2,4})\s+(.*)$') {
        $headings += [pscustomobject]@{
            Line   = $i + 1
            Text   = $Matches[2].Trim()
            Anchor = Get-Anchor $Matches[2]
        }
    }
}

# 收集 TOC 連結
$tocLinks = @()
$tocActive = $false
for ($i = 0; $i -lt $lines.Count; $i++) {
    $l = $lines[$i]
    if ($l -match 'TOC-AUTO-BEGIN') { $tocActive = $true; continue }
    if ($l -match 'TOC-AUTO-END') { $tocActive = $false; continue }
    if (-not $tocActive) { continue }
    foreach ($m in [regex]::Matches($l, '\[([^\]]+)\]\(#([^)]+)\)')) {
        $tocLinks += [pscustomobject]@{
            Line   = $i + 1
            Label  = $m.Groups[1].Value
            Anchor = $m.Groups[2].Value
        }
    }
}

$anchorSet = @{}
foreach ($h in $headings) { $anchorSet[$h.Anchor] = $h.Line }

Write-Output "=== 標題總數: $($headings.Count) / TOC 連結總數: $($tocLinks.Count) ==="

Write-Output ""
Write-Output "=== [A] TOC 連結找不到對應標題 ==="
$bad = 0
foreach ($t in $tocLinks) {
    if (-not $anchorSet.ContainsKey($t.Anchor)) {
        Write-Output ("  L{0}  {1}  ->  #{2}" -f $t.Line, $t.Label, $t.Anchor)
        $bad++
    }
}
if ($bad -eq 0) { Write-Output "  (無)" }

Write-Output ""
Write-Output "=== [B] 有編號的標題但 TOC 未收錄 ==="
$tocAnchorSet = @{}
foreach ($t in $tocLinks) { $tocAnchorSet[$t.Anchor] = $true }
$missing = 0
foreach ($h in $headings) {
    if ($h.Text -match '^\d+(\.\d+)*\s' -or $h.Text -match '^\d+(\.\d+)*\.?\s') {
        if (-not $tocAnchorSet.ContainsKey($h.Anchor)) {
            Write-Output ("  L{0}  {1}  (anchor: #{2})" -f $h.Line, $h.Text, $h.Anchor)
            $missing++
        }
    }
}
if ($missing -eq 0) { Write-Output "  (無)" }

Write-Output ""
Write-Output "=== [C] 重複錨點 ==="
$dupe = $headings | Group-Object Anchor | Where-Object { $_.Count -gt 1 }
if ($dupe) {
    foreach ($d in $dupe) { Write-Output ("  #{0}  x{1}" -f $d.Name, $d.Count) }
}
else { Write-Output "  (無)" }
