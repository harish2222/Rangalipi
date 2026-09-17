# Rangalipi one-shot replication script — turns a fresh machine into this bar.
#   powershell -NoProfile -ExecutionPolicy Bypass -File tools\setup\yasb-setup.ps1
# Run from a clone of the Rangalipi repo. It deploys the bar files
# (config.yaml, styles.css, motif/runner artwork), the GlazeWM + Komorebi
# configs, builds the companion tools (Rust theme CLI, Qt palette picker),
# deploys them into the live YASB dir, and verifies the whole chain.
# Idempotent: safe to re-run any time. Existing live files are backed up
# with a timestamp suffix before any overwrite, never deleted.
$repoRoot = Split-Path (Split-Path $PSScriptRoot)
$yasbDir = Join-Path $HOME '.config\yasb'
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$results = @()
function Step($name, [scriptblock]$body) {
    Write-Output ""
    Write-Output ("=== {0} ===" -f $name)
    try {
        & $body
        $script:results += [pscustomobject]@{ Step = $name; Result = 'PASS' }
        Write-Output ("[ok] {0}" -f $name)
    } catch {
        $script:results += [pscustomobject]@{ Step = $name; Result = 'FAIL: ' + $_.Exception.Message }
        Write-Output ("[FAIL] {0}: {1}" -f $name, $_.Exception.Message)
    }
}
function Refresh-Path {
    $m = [Environment]::GetEnvironmentVariable('Path', 'Machine')
    $u = [Environment]::GetEnvironmentVariable('Path', 'User')
    $env:Path = "$m;$u"
}
function Has-Cmd($name) {
    $null -ne (Get-Command $name -ErrorAction SilentlyContinue)
}
function Backup-File($path) {
    if (Test-Path -LiteralPath $path) {
        $bak = "$path.bak-$stamp"
        Copy-Item -LiteralPath $path -Destination $bak -Force
        Write-Output ("  backed up: {0} -> {1}" -f $path, $bak)
    }
}
function Deploy-File($src, $dst) {
    $d = Split-Path $dst
    if ($d -and -not (Test-Path -LiteralPath $d)) {
        New-Item $d -ItemType Directory -Force | Out-Null
    }
    Copy-Item -LiteralPath $src -Destination $dst -Force
}

Step 'paths' {
    foreach ($d in @($yasbDir,
            (Join-Path $HOME '.glzr\glazewm'),
            (Join-Path $HOME '.config\komorebi'))) {
        if (-not (Test-Path -LiteralPath $d)) {
            New-Item $d -ItemType Directory -Force | Out-Null
        }
    }
    foreach ($f in @('config.yaml', 'styles.css')) {
        if (-not (Test-Path -LiteralPath (Join-Path $repoRoot $f))) {
            throw ("repo file missing: {0}" -f $f)
        }
    }
    Write-Output ("  repo : {0}" -f $repoRoot)
    Write-Output ("  yasb : {0}" -f $yasbDir)
}

Step 'external apps (warn-only)' {
    $need = @(
        @('yasb', 'scoop install yasb'),
        @('komorebic', 'scoop install komorebi'),
        @('glazewm', 'scoop install glazewm'),
        @('cava', 'cava installer from github.com/karlstav/cava/releases')
    )
    foreach ($n in $need) {
        if (Has-Cmd $n[0]) { Write-Output ("  {0}: present" -f $n[0]) }
        else { Write-Output ("  {0}: MISSING -> {1}" -f $n[0], $n[1]) }
    }
    $faces = @()
    foreach ($h in @('HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts',
            'HKCU:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts')) {
        if (Test-Path $h) {
            $faces += @(Get-ItemProperty $h -ErrorAction SilentlyContinue |
                Get-Member -MemberType NoteProperty | Where-Object { $_.Name -match 'nerd' })
        }
    }
    $nf = $faces.Count
    Write-Output ("  nerd faces installed: {0}" -f $nf)
    if ($nf -eq 0) { throw 'no Nerd Fonts installed (bar icons need at least one: scoop install nerd-fonts/JetBrainsMono-NF nerd-fonts/FiraCode-NF-Mono)' }
}

Step 'back up live files' {
    Backup-File (Join-Path $yasbDir 'config.yaml')
    Backup-File (Join-Path $yasbDir 'styles.css')
    Backup-File (Join-Path $HOME '.glzr\glazewm\config.yaml')
    Backup-File (Join-Path $HOME 'komorebi.json')
    Backup-File (Join-Path $HOME '.config\komorebi\komorebi-startup.ps1')
}

Step 'deploy bar files' {
    Deploy-File (Join-Path $repoRoot 'config.yaml') (Join-Path $yasbDir 'config.yaml')
    Deploy-File (Join-Path $repoRoot 'styles.css') (Join-Path $yasbDir 'styles.css')
    $art = @(Get-ChildItem -LiteralPath $repoRoot -File |
        Where-Object { $_.Name -match '^(motif|runner)-.*\.svg$|^media-rangoli\.svg$' })
    if ($art.Count -eq 0) { throw 'no motif/runner artwork found in repo root' }
    foreach ($a in $art) { Deploy-File $a.FullName (Join-Path $yasbDir $a.Name) }
    Write-Output ("  bar + {0} artwork files deployed (YASB hot-reloads them)" -f $art.Count)
}

Step 'deploy window-manager configs' {
    Deploy-File (Join-Path $repoRoot 'configs\glazewm\config.yaml') (Join-Path $HOME '.glzr\glazewm\config.yaml')
    Deploy-File (Join-Path $repoRoot 'configs\komorebi\komorebi.json') (Join-Path $HOME 'komorebi.json')
    Deploy-File (Join-Path $repoRoot 'configs\komorebi\komorebi-startup.ps1') (Join-Path $HOME '.config\komorebi\komorebi-startup.ps1')
    Write-Output '  glazewm + komorebi configs deployed (restart the WMs to apply)'
}

Step 'rust toolchain' {
    if (-not (Has-Cmd 'cargo')) {
        Write-Output '  installing Rust via winget...'
        winget install --id Rustlang.Rustup -e --silent --accept-package-agreements --accept-source-agreements
        Refresh-Path
    }
    if (-not (Has-Cmd 'cargo')) { throw 'cargo still missing after install' }
    Write-Output ("  cargo: {0}" -f (Get-Command cargo).Source)
}

Step 'python Qt6 stack (build-only)' {
    # Build dependency only: the palette picker source is Python/PyInstaller.
    # Nothing Python runs at bar runtime.
    if (-not (Has-Cmd 'python3')) { throw 'python3 not found (install via winget: Python.Python.3.13)' }
    python3 -c "import PyQt6.QtCore as q; print('  PyQt6 Qt', q.qVersion())" 2>$null
    if ($LASTEXITCODE -ne 0) {
        Write-Output '  installing PyQt6 + PyInstaller...'
        python3 -m pip install --quiet PyQt6 PyInstaller
    }
    python3 -c "import PyQt6, PyInstaller; print('  modules ok')" 2>$null
    if ($LASTEXITCODE -ne 0) { throw 'PyQt6/PyInstaller import failed' }
}

Step 'build theme tool (rust)' {
    powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $repoRoot 'tools\theme\yasb-theme-build.ps1')
    if ($LASTEXITCODE -ne 0) { throw 'yasb-theme-build.ps1 failed' }
}

Step 'build palette picker (qt6)' {
    powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $repoRoot 'tools\picker\palette-picker-build.ps1')
    if ($LASTEXITCODE -ne 0) { throw 'palette-picker-build.ps1 failed' }
}

Step 'deploy tools to live yasb dir' {
    $map = @(
        @('tools\theme\yasb-theme.exe', 'tools\theme\yasb-theme.exe'),
        @('tools\theme\yasb-theme-shell.ps1', 'tools\theme\yasb-theme-shell.ps1'),
        @('tools\picker\palette-picker.exe', 'tools\picker\palette-picker.exe'),
        @('tools\picker\palette-themes.json', 'tools\picker\palette-themes.json'),
        @('tools\picker\palette-picker.bat', 'tools\picker\palette-picker.bat')
    )
    foreach ($m in $map) {
        $src = Join-Path $repoRoot $m[0]
        if (-not (Test-Path -LiteralPath $src)) { throw ("build output missing: {0}" -f $m[0]) }
        Deploy-File $src (Join-Path $yasbDir $m[1])
    }
    Write-Output '  theme CLI + palette picker deployed to live yasb dir'
}

Step 'verify chain' {
    $exe = Join-Path $yasbDir 'tools\theme\yasb-theme.exe'
    $cur = & $exe current
    if ($LASTEXITCODE -ne 0) { throw 'yasb-theme current failed' }
    $n = ((& $exe list) | Measure-Object -Line).Lines
    Write-Output ("  theme tool ok: {0} themes, active: {1}" -f $n, $cur)
    if ($n -lt 22) { throw ("expected 22 themes, got {0}" -f $n) }
    if (-not (Has-Cmd 'silent-run')) { throw 'silent-run not on PATH' }
    Write-Output '  silent-run on PATH'
    $pj = Join-Path $yasbDir 'tools\picker\palette-themes.json'
    if (-not (Test-Path $pj)) { throw 'palette-themes.json missing' }
    $p = Start-Process (Join-Path $yasbDir 'tools\picker\palette-picker.exe') -PassThru
    Start-Sleep -Seconds 8
    $alive = $null -ne (Get-Process -Id $p.Id -ErrorAction SilentlyContinue)
    Get-Process -Name palette-picker -ErrorAction SilentlyContinue | Stop-Process -Force
    if (-not $alive) { throw 'picker exe died on boot (bundled Qt broken)' }
    Write-Output '  picker exe boots bundled Qt6'
}

Step 'shell helper (yt)' {
    if (-not (Test-Path $PROFILE)) { New-Item $PROFILE -ItemType File -Force | Out-Null }
    $line = '. "{0}"' -f (Join-Path $yasbDir 'tools\theme\yasb-theme-shell.ps1')
    if (-not (Select-String -Path $PROFILE -Pattern 'yasb-theme-shell' -Quiet)) {
        Add-Content $PROFILE $line
        Write-Output '  yt helper added to profile'
    } else { Write-Output '  yt helper already in profile' }
}

Write-Output ""
Write-Output "================ SUMMARY ================"
$results | Format-Table -AutoSize | Out-String | Write-Output
if ($results.Result -match '^FAIL') { exit 1 }
Write-Output 'replication complete: restart the shell, then run: yt list'
Write-Output 'note: YASB hot-reloads the bar itself; restart GlazeWM + Komorebi to apply their configs'
