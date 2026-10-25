# Rangalipi — Complete Installation & Replication Guide

This guide walks you through replicating the complete Rangalipi desktop environment: Komorebi tiling window manager + GlazeWM hotkey layer + YASB bar with 22 hand-crafted themes and native Apple HIG Win32 companion widgets.

Tested on Windows 11 / Windows 10, PowerShell 7, YASB v2.0.7, Komorebi 0.1.41, GlazeWM 3.10.1.

---

## 1. Prerequisites

### A. Recommended Package Manager (Scoop)

If you do not have Scoop installed:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex
```

### B. Core Window Managers & Bar

Install the core binaries:

```powershell
scoop install yasb komorebi glazewm
```

Optional spectrum visualizer: install `cava` from [github.com/karlstav/cava/releases](https://github.com/karlstav/cava/releases).

### C. Required Fonts

Without Nerd Fonts, bar icons and widget glyphs will render as empty boxes:

```powershell
scoop bucket add nerd-fonts
scoop install nerd-fonts/JetBrainsMono-NF nerd-fonts/FiraCode-NF nerd-fonts/FiraCode-NF-Mono
```

> **Note**: Close and reopen your terminal after installing fonts so Windows registers them.

---

## 2. One-Shot Turnkey Replication

All companion tools (`yasb-theme`, `silent-run`, `palette-picker`, `saka`, `saka-popup`, `keybind`, `pomodoro`, `komorebi-sync`, `screen-shot`) are written in **pure Rust** with zero Python runtime or build dependencies.

1. Clone the Rangalipi repository:

```powershell
git clone https://github.com/harish2222/Rangalipi.git C:\Users\$env:USERNAME\Rangalipi
cd C:\Users\$env:USERNAME\Rangalipi
```

2. Run the one-shot setup script:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools\setup\yasb-setup.ps1
```

### What `yasb-setup.ps1` Does Automatically:
1. **Backs up** existing files in `~/.config/yasb`, `~/.glzr/glazewm`, and `~/.config/komorebi` with timestamped `.bak` extensions (never overwrites destructively).
2. **Installs Rust** via winget if `cargo` is not yet on your system.
3. **Compiles all companion tools** using `cargo build --workspace --release` in a single pass.
4. **Deploys the `silent-run.exe` shim** to eliminate console window flashing during hotkey execution.
5. **Adapts configuration paths** dynamically to match your current Windows user profile (`config.yaml`, `styles.css` mandala URLs, and Komorebi/GlazeWM configs).
6. **Deploys high-resolution mandala artwork** and theme styles.
7. **Verifies the entire chain** with automated headless smoke tests.
8. **Registers the `yt` shell helper** inside your PowerShell profile.

---

## 3. Launching the Environment

1. **Start the Bar**:
   Run `yasb` or launch it from the Start Menu / Startup folder.
2. **Start the Window Managers**:
   Start Komorebi and GlazeWM. Hotkeys and window tiling will be immediately active.
3. **Verify Theme CLI**:
   Open a new PowerShell terminal and run:
   ```powershell
   yt list
   yt current
   yt set "Rangalipi Dune Dark"
   ```

---

## 4. Desktop Controls & Keybindings

| Keybinding | Action |
|---|---|
| **Win + K** | Open Apple HIG Keybindings Cheatsheet |
| **Alt + h/j/k/l** | Focus left / down / up / right window |
| **Alt + Shift + h/j/k/l** | Move window left / down / up / right |
| **Alt + Enter** | Launch terminal |
| **Alt + Shift + b** / **Alt + z** | Launch browser |
| **Alt + o** | Launch editor |
| **Alt + q** | Close focused window |
| **Alt + f** | Toggle maximize |
| **Alt + Shift + f** | Toggle monocle layout |
| **Alt + r** | Enter resize mode |
| **Alt + Shift + r** | Reload GlazeWM & Komorebi configurations |

---

## 5. Companion Widgets Guide

### 🌸 Vedic Panchangam (`saka` & `saka-popup`)
- **Trigger**: Left-click the Saka widget in the bar.
- **Hero Moons**: Displays both a 3D rotating planetary moon and an authentic telescopic night sky moon with real selenographic maria (*Mare Imbrium*, *Procellarum*, *Serenitatis*) and ray craters (*Tycho*, *Copernicus*).
- **Controls**:
  - `Tab`: Toggle between English and Telugu scripts.
  - `M`: Cycle layout modes (**Portrait** $\rightarrow$ **Landscape** $\rightarrow$ **Compact glance**).
  - `Esc`: Close panel.

### 🎨 Palette Browser (`palette-picker`)
- **Trigger**: Left-click the Palette icon in the bar control group.
- **Controls**: Type to fuzzy-filter themes across 22 options, use Arrow keys or mouse to navigate, `Enter` to apply instantly with zero restart.

### ⌨️ Keybindings Cheatsheet (`keybind`)
- **Trigger**: `Win + K` or left-click keyboard icon in the bar control group.
- **Controls**: Filter hotkeys by category chips (Focus, Move, Layout, Workspaces, Apps, System) or live search.

### ⏳ Focus Timer (`pomodoro`)
- **Trigger**: Click pomodoro widget in bar to start, pause, or reset focus sessions.

---

## 6. Troubleshooting

| Symptom | Cause | Solution |
|---|---|---|
| Glyphs appear as squares | Missing Nerd Fonts | Install JetBrainsMono NF: `scoop install nerd-fonts/JetBrainsMono-NF` and restart terminal |
| Hotkeys flash black windows | `silent-run.exe` not on PATH | Ensure `~/scoop/shims` or `~/.local/bin` is in your User PATH |
| Custom popups don't appear | Single-instance lock or missing build | Run `tools\setup\yasb-setup.ps1` to rebuild and run `--smoke` tests |
| Wallpapers don't change | Directory path missing | Configure `image_path` in `~/.config/yasb/config.yaml` to point to your wallpaper folder |
