# Rangalipi

![Theme Preview](https://raw.githubusercontent.com/harish2222/Rangalipi/main/gallery/shot-1.png)

# USE JetBrainsMono Nerd Font AND FiraCode Nerd Font Mono (Retina)

Without them every icon renders as tofu boxes. Get both from `scoop`
(`nerd-fonts/JetBrainsMono-NF`, `nerd-fonts/FiraCode-NF`,
`nerd-fonts/FiraCode-NF-Mono`) or nerdfonts.com, then set them as the
four `--*-font` vars at the top of `styles.css` (preset block included).

Original Rangalipi palette: 22 hand-built themes (11 dark + 11 light),
each with its own folk-motif artwork, bar runner, and full hue set.
Komorebi workspaces, system stats, media with full controls, and one
suckless palette picker for all 22 palettes (Lights are for bright wallpapers).

## Gallery

![Bar](https://raw.githubusercontent.com/harish2222/Rangalipi/main/gallery/shot-1.png)
![Bar collapsed](https://raw.githubusercontent.com/harish2222/Rangalipi/main/gallery/shot-2.png)
![Stats expanded](https://raw.githubusercontent.com/harish2222/Rangalipi/main/gallery/shot-3.png)

## Desktop

![Clean](https://raw.githubusercontent.com/harish2222/Rangalipi/main/gallery/desktop-clean.png)
![Stats](https://raw.githubusercontent.com/harish2222/Rangalipi/main/gallery/desktop-stats.png)
![Control center](https://raw.githubusercontent.com/harish2222/Rangalipi/main/gallery/desktop-control.png)
![Media](https://raw.githubusercontent.com/harish2222/Rangalipi/main/gallery/desktop-media.png)
![Home menu](https://raw.githubusercontent.com/harish2222/Rangalipi/main/gallery/desktop-home.png)
![Layout menu](https://raw.githubusercontent.com/harish2222/Rangalipi/main/gallery/desktop-layout.png)
![Wallpaper gallery](https://raw.githubusercontent.com/harish2222/Rangalipi/main/gallery/desktop-gallery.png)
![Crimson](https://raw.githubusercontent.com/harish2222/Rangalipi/main/gallery/desktop-crimson.png)

## Features

- **Opaque islands**: solid theme-tinted bar and popups, readable on light and dark wallpapers (bar blur stays off)
- **Palette browser**: flexbox switcher for the 22 Rangalipi palettes, live search
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

Full guide with fonts, tools, switching, and troubleshooting:
[`docs/INSTALL.md`](docs/INSTALL.md)

1. **Fonts**: install `JetBrainsMono Nerd Font` and
   `FiraCode Nerd Font Mono` (Retina), plus `Segoe Fluent Icons`.
2. Run the replicator — it backs up live files, deploys the bar + artwork +
   WM configs, builds the tools and verifies everything:
   `powershell -ExecutionPolicy Bypass -File tools\setup\yasb-setup.ps1`
   Tested on YASB v2.0.7, Komorebi 0.1.41, GlazeWM 3.10.1.
3. Companion tools ship as source only (no binaries) under `tools\`
   (theme CLI, palette picker) and `yasb-theme\` (Rust source).
   Without the built exes the bar still works; only the palette button
   needs rebinding. WM configs live in `configs\` (deployed by the script).

### Companion scripts

All runnable from PowerShell (`-ExecutionPolicy Bypass` for `.ps1`):

- `tools\setup\yasb-setup.ps1` — one-shot replicator: backs up live files,
  deploys bar + artwork + WM configs, builds the exes, verifies the chain.
  Idempotent, safe to re-run.
- `tools\theme\yasb-theme-build.ps1` — rebuilds `yasb-theme.exe`
  (`list|current|set|next|prev`) and deploys `silent-run.exe`.
- `tools\theme\yasb-theme-shell.ps1` — dot-source for the `yt` shortcut.
- `tools\picker\palette-picker-build.ps1` — rebuilds `palette-picker.exe`
  (palette browser) from the only Python source left.
