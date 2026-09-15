# Rangalipi

![Theme Preview](https://raw.githubusercontent.com/harish2222/Rangalipi/main/preview.png)

Kanagawa-wave dark bar on floating glass islands with gold borders. Komorebi
workspaces, system stats, media with full controls, and two suckless pickers:
one for 82 color palettes, one for installed Nerd Fonts.

## Features

- **Liquid glass**: theme-tinted blur on bar islands and every popup
- **Palette browser (वर्ण)**: scrollable flexbox switcher for 82 palettes,
  live search, arrows + Enter, chrome follows the active theme
- **Font browser (β)**: switch any installed Nerd Font live, names previewed
  in their own typeface
- **Komorebi first**: workspaces, active layout, control, stack widgets
- **Full media**: thumbnail, inline controls, bounce titles, progress line,
  volume slider, play/pause + open-player mouse actions
- **System monitors**: CPU, GPU, memory, disk, traffic in one collapsible
  group with integer readouts and load-status colors
- **Zero flash**: every launcher routed through a hidden runner process
- **RDP-proof**: remote windows ignored by class, exe and title so sessions
  never disturb tiling or focus
- **Boot-proof**: ordered login chain (Komorebi, GlazeWM keys, bar) with a
  one-shot setup script that rebuilds and verifies everything

## Bar layout

Left: home menu, Komorebi layout + control, workspaces, active-window icon,
stack. Center: clock, cava spectrum (theme-synced gradient), media. Right:
systray, system-stats group (α), control group (Ω: network, audio, power,
wallpapers, palette, fonts, alerts), control center (Θ).

## Installation

1. **Fonts**: install `Hack Nerd Font` (or any Nerd Font), `Segoe UI Variable`,
   `Segoe Fluent Icons`. The bar falls back gracefully without them.
2. Copy `config.yaml` and `styles.css` into `%USERPROFILE%\.config\yasb`.
   Tested on YASB v2.0.7, Komorebi 0.1.41, GlazeWM 3.10.1.
3. Companion tools ship as source only (no binaries) under `tools\`
   (theme CLI, palette and font pickers) and `yasb-theme\` (Rust source).
   Build every exe with `tools\setup\yasb-setup.ps1` — Rust, Qt6 and
   PyInstaller are installed automatically when missing. Without them the
   bar still works; only the वर्ण/β buttons need rebinding. WM configs
   live in `configs\`.

### Companion scripts

All runnable from PowerShell (`-ExecutionPolicy Bypass` for `.ps1`):

- `tools\setup\yasb-setup.ps1` — one-shot setup: checks toolchains
  (Rust, Python Qt6), rebuilds every binary, verifies the chain, snapshots
  the WM configs. Idempotent, safe to re-run.
- `tools\theme\yasb-theme-build.ps1` — rebuilds `yasb-theme.exe`
  (`list|current|set|next|prev`) and deploys `silent-run.exe`.
- `tools\theme\yasb-theme-shell.ps1` — dot-source for the `yt` shortcut.
- `tools\picker\palette-picker-build.ps1` — rebuilds `palette-picker.exe`.
- `tools\picker\yasb-font-build.ps1` — rebuilds `yasb-font.exe`
  (`list|current|set|next|prev` over installed Nerd Fonts).
- `tools\setup\export-theme.py` — regenerates this submission pack
  (single-theme CSS, clean config, redaction, screenshots).

## Author

[![GitHub](https://img.shields.io/badge/GitHub-harish2222-181717?logo=github&style=flat-square)](https://github.com/harish2222)
