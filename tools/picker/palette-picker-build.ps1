# Rebuilds palette-picker.exe from palette-picker.py (onefile, windowed).
# Windowed = GUI subsystem = it can never own a console, so no terminal
# flash on launch, ever. Re-run after any picker source change.
$ErrorActionPreference = 'Stop'
$dir = $PSScriptRoot
python3 -c "import PyInstaller" 2>$null
if ($LASTEXITCODE -ne 0) {
    python3 -m pip install pyinstaller
}
Push-Location $dir
try {
    python3 -m PyInstaller --noconfirm --clean --onefile --windowed `
        --name palette-picker `
        --distpath "$dir\dist" --workpath "$dir\build" --specpath "$dir" `
        "$dir\palette-picker.py"
    Copy-Item "$dir\dist\palette-picker.exe" "$dir\palette-picker.exe" -Force
    $size = [math]::Round((Get-Item "$dir\palette-picker.exe").Length / 1MB, 1)
    Write-Output ("deployed palette-picker.exe ({0} MB)" -f $size)
} finally {
    Pop-Location
}
