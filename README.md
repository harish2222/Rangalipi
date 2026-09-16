# Rangalipi

![Theme Preview](https://raw.githubusercontent.com/harish2222/Rangalipi/main/gallery/shot-1.png)

# USE JetBrainsMono Nerd Font AND FiraCode Nerd Font Mono (Retina)

Without them every icon renders as tofu boxes. Get both from `scoop`
(`nerd-fonts/JetBrainsMono-NF`, `nerd-fonts/FiraCode-NF`,
`nerd-fonts/FiraCode-NF-Mono`) or nerdfonts.com, then set them as the
four `--*-font` vars at the top of `styles.css` (preset block included).

Original Rangalipi palette: ink-indigo islands with marigold borders. Komorebi
workspaces, system stats, media with full controls, and two suckless pickers:
one for 82 color palettes, one for installed Nerd Fonts.

## Gallery

![Shot 1](https://raw.githubusercontent.com/harish2222/Rangalipi/main/gallery/shot-1.png)
![Shot 2](https://raw.githubusercontent.com/harish2222/Rangalipi/main/gallery/shot-2.png)
![Shot 3](https://raw.githubusercontent.com/harish2222/Rangalipi/main/gallery/shot-3.png)
![Shot 4](https://raw.githubusercontent.com/harish2222/Rangalipi/main/gallery/shot-4.png)
![Shot 5](https://raw.githubusercontent.com/harish2222/Rangalipi/main/gallery/shot-5.png)
![Shot 6](https://raw.githubusercontent.com/harish2222/Rangalipi/main/gallery/shot-6.png)
![Shot 7](https://raw.githubusercontent.com/harish2222/Rangalipi/main/gallery/shot-7.png)
![Shot 8](https://raw.githubusercontent.com/harish2222/Rangalipi/main/gallery/shot-8.png)

## Features

- **Liquid glass**: theme-tinted blur on islands and all popups
- **Palette browser**: flexbox switcher for 82 palettes, live search
- **Font browser**: any installed Nerd Font, previewed in its own face
- **Komorebi set**: workspaces, layout, control, stack widgets
- **Full media**: thumbnail, controls, bounce titles, progress, volume
- **Monitors**: CPU, GPU, memory, disk, traffic, integer readouts, statuses
- **Zero flash**: launchers run through a hidden runner process
- **RDP-proof**: remote windows ignored by class, exe and title
- **Boot-proof**: ordered login chain plus a verifying one-shot setup script

## Bar layout

Left: home menu, Komorebi layout, workspaces, stack. Center: clock, cava
spectrum (theme-synced gradient), media. Right: systray, system-stats
group, control group (bluetooth, audio, power, wallpapers, palette,
alerts), control center.

## Installation

1. **Fonts**: install `JetBrainsMono Nerd Font` and
   `FiraCode Nerd Font Mono` (Retina), plus `Segoe Fluent Icons`.
2. Copy `config.yaml` and `styles.css` into `%USERPROFILE%\.config\yasb`.
   Tested on YASB v2.0.7, Komorebi 0.1.41, GlazeWM 3.10.1.
3. Companion tools ship as source only (no binaries) under `tools\`
   (theme CLI, palette and font pickers) and `yasb-theme\` (Rust source).
   Build every exe with `tools\setup\yasb-setup.ps1` — Rust, Qt6 and
   PyInstaller are installed automatically when missing. Without them the
   bar still works; only the palette button needs rebinding. WM configs
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
