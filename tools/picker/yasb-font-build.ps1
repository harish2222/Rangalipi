# Builds yasb-font.exe (console subsystem: it prints names; callers hide the
# window via CREATE_NO_WINDOW / silent-run, so still zero flash).
# Re-run after any yasb-font.py change.
$ErrorActionPreference = 'Stop'
$dir = $PSScriptRoot
Push-Location $dir
try {
    python3 -m PyInstaller --noconfirm --clean --onefile `
        --name yasb-font `
        --distpath "$dir\dist" --workpath "$dir\build" --specpath "$dir" `
        "$dir\yasb-font.py"
    Copy-Item "$dir\dist\yasb-font.exe" "$dir\yasb-font.exe" -Force
    $size = [math]::Round((Get-Item "$dir\yasb-font.exe").Length / 1KB, 0)
    Write-Output ("deployed yasb-font.exe ({0} KB)" -f $size)
} finally {
    Pop-Location
}
