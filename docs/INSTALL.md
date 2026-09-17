# Rangalipi — Install & Run

Tested on YASB v2.0.7, Komorebi 0.1.41, GlazeWM 3.10.1, PowerShell 7.

## 1. Fonts (required)

Without these, every bar icon renders as tofu boxes:

```powershell
scoop bucket add nerd-fonts
scoop install nerd-fonts/JetBrainsMono-NF nerd-fonts/FiraCode-NF nerd-fonts/FiraCode-NF-Mono
```

`Segoe Fluent Icons` ships with Windows 11 — nothing to install.
Close and reopen Windows Terminal after installing so the fonts register.

## 2. Bar files

```powershell
Copy-Item config.yaml, styles.css "$env:USERPROFILE\.config\yasb\" -Force
```

Restart YASB (or wait for auto-reload). The four `--*-font` vars at the
top of `styles.css` already point at `FiraCode Nerd Font Mono`; swap the
comment block to JetBrainsMono if you prefer it.

## 3. Companion tools (optional)

The bar works without them. They power the shuffle (palette) button:

```powershell
powershell -ExecutionPolicy Bypass -File tools\setup\yasb-setup.ps1
```

This installs missing toolchains (Rust, Python Qt6, PyInstaller) and builds
`yasb-theme.exe` (12-theme engine, incl. Rangalipi Light), `palette-picker.exe`
(palette browser) and `silent-run.exe` (flash-free launcher).
Re-running is safe. Folk-motif SVGs (`motif-*.svg`, `runner-*.svg`)
must sit next to `styles.css` — copy them over too if you use the artwork.

## 4. Switching themes

- Left-click shuffle: visual browser (type to filter, arrows + Enter).
- Right-click shuffle: next theme. Middle-click: current theme name.
- Terminal: `yasb-theme.exe list|current|set <name>|next|prev`.

New terminals need the `yt` shortcut first:
`powershell -ExecutionPolicy Bypass -File tools\theme\yasb-theme-shell.ps1`
(dot-source it from your `$PROFILE` to keep it).

## 5. Troubleshooting

| Symptom | Fix |
|---|---|
| Boxes instead of icons | Fonts not installed/registered — redo step 1, restart terminal + YASB |
| Picker shows nothing | Rebuild: `tools\picker\palette-picker-build.ps1`, kill stuck `palette-picker` processes first |
| Theme won't switch | `yasb-theme.exe current` must print a name; if `unknown theme`, the styles.css header lost its `- active` suffix |
| Wallpaper gallery empty | Point `image_path` in `config.yaml` at a folder that exists |
| Bar screenshot | Right-click bar → Take Screenshot → `Pictures\YASB_Screenshots` |
