# Rebuild + deploy yasb-theme.exe (run from anywhere; repo-relative, no hardcoded user).
#   pwsh -File tools\theme\yasb-theme-build.ps1
$ErrorActionPreference = 'Stop'
$yasbDir = Split-Path (Split-Path $PSScriptRoot)
$projectDir = Join-Path $yasbDir 'yasb-theme'
Push-Location $projectDir
try {
    cargo build --release
}
finally {
    Pop-Location
}
$built = Join-Path $projectDir 'target\release\yasb-theme.exe'
$dest = Join-Path $PSScriptRoot 'yasb-theme.exe'
Copy-Item -LiteralPath $built -Destination $dest -Force
$builtSilent = Join-Path $projectDir 'target\release\silent-run.exe'
$destSilent = Join-Path $HOME 'scoop\shims\silent-run.exe'
Copy-Item -LiteralPath $builtSilent -Destination $destSilent -Force
$current = & $dest current
if ($LASTEXITCODE -ne 0) { throw 'smoke test failed: yasb-theme.exe current' }
Write-Output "deployed : $dest"
Write-Output "active   : $current"
