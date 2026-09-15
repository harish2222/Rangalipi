@echo off
rem Launch the bundled font picker (suckless grid, Nerd Fonts only).
rem Windowed-subsystem exe: can never own a console, so zero terminal flash.
set "QT_PLUGIN_PATH="
set "QT_QPA_PLATFORM_PLUGIN_PATH="
set "QML2_IMPORT_PATH="
set "QT_QPA_PLATFORM="
set "PYTHONPATH="
set "PYTHONHOME="
set "CONDA_PREFIX="
set "CONDA_SHLVL="
set "CONDA_PROMPT_MODIFIER="
start "" "C:/Users/YourName\.config\yasb\tools\picker\palette-picker.exe" --fonts
