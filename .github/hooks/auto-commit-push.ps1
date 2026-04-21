# Auto commit and push on agent session Stop.
# Only runs when the gate file .github/hooks/.auto-push-enabled exists.
# To enable:  New-Item .github/hooks/.auto-push-enabled
# To disable: Remove-Item .github/hooks/.auto-push-enabled

$ErrorActionPreference = "Continue"

# Read hook input (optional, for future use)
try {
    $hookInput = [Console]::In.ReadToEnd() | ConvertFrom-Json
} catch {
    # Proceed even if no input
}

Set-Location -Path $PSScriptRoot\..\..

# Gate: only proceed if the enable flag file exists
$gateFile = Join-Path $PSScriptRoot ".auto-push-enabled"
if (-not (Test-Path $gateFile)) {
    @{ continue = $true } | ConvertTo-Json
    exit 0
}

# Check if there are any changes to commit
$status = git status --porcelain 2>&1
if (-not $status) {
    # No changes, nothing to do
    @{ continue = $true } | ConvertTo-Json
    exit 0
}

# Stage all changes
git add -A 2>&1

# Commit with a timestamped message
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$commitMsg = "auto-commit: agent session ended at $timestamp"
$commitResult = git commit -m $commitMsg 2>&1

if ($LASTEXITCODE -ne 0) {
    Write-Error "Commit failed: $commitResult"
    @{ continue = $true } | ConvertTo-Json
    exit 0
}

# Push to remote
$pushResult = git push 2>&1

if ($LASTEXITCODE -ne 0) {
    Write-Error "Push failed: $pushResult"
    @{ continue = $true } | ConvertTo-Json
    exit 0
}

@{ continue = $true } | ConvertTo-Json
exit 0
