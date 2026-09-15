#!/usr/bin/env python3
"""Suckless dmenu-style picker for the YASB bar: themes (default) or
system Nerd Fonts (--fonts). One slim frameless bar: filter line on top,
flexbox flow below. Type to narrow, arrows to move, Enter to apply.
Reads themes/fonts catalogs, paints with the ACTIVE theme's vars.
"""
import json
import os
import re
import subprocess
import sys

from PyQt6.QtCore import QMargins, QPoint, QRect, QSize, Qt
from PyQt6.QtGui import QCursor, QKeySequence, QShortcut
from PyQt6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLayout,
    QLineEdit,
    QScrollArea,
    QVBoxLayout,
    QWidget,
    QWidgetItem,
)

BASE = os.path.dirname(os.path.abspath(__file__))
FALLBACK = os.path.join(os.path.expanduser("~"), ".config", "yasb")
FONTS_MODE = "--fonts" in sys.argv


def resolve(name):
    tried = [os.path.join(BASE, name)]
    if name == "yasb-theme.exe":
        # lives with the theme tool, not the picker
        tried.append(os.path.join(FALLBACK, "tools", "theme", name))
    tried.append(os.path.join(FALLBACK, "tools", "picker", name))
    tried.append(os.path.join(FALLBACK, name))
    for q in tried:
        if os.path.exists(q):
            return q
    return tried[0]


DATA_JSON = resolve("palette-themes.json")
STYLES_CSS = resolve("styles.css")
EXE = resolve("yasb-theme.exe")
FONT_SCRIPT = resolve("yasb-font.py")
FONT_EXE = resolve("yasb-font.exe")

DEFAULT_VARS = {
    "background": "#181825",
    "surface": "#313244",
    "text": "#cdd6f4",
    "subtext": "#a6adc8",
    "accent": "#b4befe",
    "border": "#45475a",
}


def python_cmd():
    exe = sys.executable or ""
    if exe.lower().endswith("python.exe") or exe.lower().endswith("pythonw.exe"):
        return exe
    return "python3"


def font_bin():
    if os.path.exists(FONT_EXE):
        return [FONT_EXE]
    return [python_cmd(), FONT_SCRIPT]


def load_items():
    if FONTS_MODE:
        # single source of truth: live discovery inside the font tool
        try:
            out = subprocess.run(font_bin() + ["list"], capture_output=True,
                                 timeout=15)
            names = []
            for line in out.stdout.decode("utf-8", "replace").splitlines():
                s = line.strip()
                if s.startswith("* "):
                    s = s[2:]
                elif s.startswith("  "):
                    s = s.strip()
                if s:
                    names.append(s)
            return [{"name": n, "colors": [], "section": "all"} for n in names]
        except Exception:
            return []
    return json.load(open(DATA_JSON, encoding="utf-8"))


def active_name():
    try:
        if FONTS_MODE:
            css = open(STYLES_CSS, encoding="utf-8").read()
            m = re.search(r'--system-font:\s*"([^"]+)"', css)
            return m.group(1) if m else ""
        out = subprocess.run([EXE, "current"], capture_output=True, timeout=10)
        return out.stdout.decode("utf-8", "replace").strip()
    except Exception:
        return ""


def theme_vars(wanted):
    """Vars of the ACTIVE theme section (/* NAME - active */ + bare vars)."""
    vars_ = dict(DEFAULT_VARS)
    try:
        css = open(STYLES_CSS, encoding="utf-8").read()
        m = re.search(
            r"/\*\s*" + re.escape(wanted) + r"\s*- active\s*\*/(.*?)(?=/\*|\Z)",
            css, re.S,
        )
        if m:
            body = m.group(1)
            for k in list(vars_):
                mm = re.search(r"--" + k + r"\s*:\s*([^;]+);", body)
                if mm:
                    vars_[k] = mm.group(1).strip()
            s0 = re.search(r"--surface0\s*:\s*([^;]+);", body)
            if s0:
                vars_["surface"] = s0.group(1).strip()
    except Exception:
        pass
    return vars_


class FlowLayout(QLayout):
    """Wrapping flexbox-style layout: items flow left-to-right, wrap rows."""

    def __init__(self, parent=None, spacing=6):
        super().__init__(parent)
        self._items = []
        self.setSpacing(spacing)
        self.setContentsMargins(0, 0, 0, 0)

    def addItem(self, item):
        self._items.append(item)

    def count(self):
        return len(self._items)

    def itemAt(self, i):
        return self._items[i] if 0 <= i < len(self._items) else None

    def takeAt(self, i):
        return self._items.pop(i) if 0 <= i < len(self._items) else None

    def expandingDirections(self):
        return Qt.Orientation(0)

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, w):
        return self._do_layout(QRect(0, 0, w, 0), True)

    def setGeometry(self, rect):
        super().setGeometry(rect)
        self._do_layout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        s = QSize()
        for it in self._items:
            s = s.expandedTo(it.minimumSize())
        m = self.contentsMargins()
        return s + QSize(m.left() + m.right(), m.top() + m.bottom())

    def _do_layout(self, rect, test):
        m = self.contentsMargins()
        area = rect.adjusted(m.left(), m.top(), -m.right(), -m.bottom())
        x, y, line_h = area.x(), area.y(), 0
        sp = self.spacing()
        for it in self._items:
            w = it.widget()
            hint = it.sizeHint()
            cell_w = w.property("flow_w") or hint.width()
            next_x = x + cell_w + sp
            if next_x - sp > area.right() and line_h > 0:
                x, y = area.x(), y + line_h + sp
                line_h = 0
            if not test:
                it.setGeometry(QRect(QPoint(x, y), QSize(cell_w, hint.height())))
            x += cell_w + sp
            line_h = max(line_h, hint.height())
        return y + line_h - rect.y()


class ThemeCell(QFrame):
    def __init__(self, theme, state, on_pick, on_hover):
        super().__init__()
        self._name = theme["name"]
        self._pick = on_pick
        self._hover = on_hover
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setProperty("class", f"cell {state}".strip())
        self.setProperty("flow_w", 178)
        self.setMinimumWidth(178)
        self.setFixedHeight(28)
        lay = QHBoxLayout(self)
        lay.setContentsMargins(8, 0, 8, 0)
        lay.setSpacing(3)
        for c in theme["colors"][:3]:
            chip = QFrame()
            chip.setFixedSize(11, 11)
            chip.setStyleSheet(f"background: {c}; border-radius: 2px;")
            lay.addWidget(chip)
        lab = QLabel(theme["name"])
        lab.setProperty("class", "cell-label")
        if FONTS_MODE:
            # live preview: render the name in the candidate font itself
            lab.setStyleSheet(f'font-family: "{theme["name"]}";')
        lay.addWidget(lab, 1)

    def set_state(self, state):
        self.setProperty("class", f"cell {state}".strip())
        self.style().unpolish(self)
        self.style().polish(self)

    def mousePressEvent(self, ev):
        if ev.button() == Qt.MouseButton.LeftButton:
            self._pick(self._name)

    def enterEvent(self, ev):
        super().enterEvent(ev)
        self._hover(self._name)


class Picker(QWidget):
    SYMBOL = "β" if FONTS_MODE else "वर्ण"
    KIND = "fonts" if FONTS_MODE else "palette"

    def __init__(self, items, current, vars_):
        super().__init__(
            None,
            Qt.WindowType.Tool
            | Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.NoDropShadowWindowHint,
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.items = items
        self.current = current
        self.cells = []
        self.filtered = []
        self.sel = 0
        self.resize(680, 300)

        frame = QFrame(self)
        frame.setProperty("class", "frame")
        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.addWidget(frame)
        self.setStyleSheet(self._css(vars_))

        root = QVBoxLayout(frame)
        root.setContentsMargins(12, 8, 12, 10)
        root.setSpacing(0)

        self.search = QLineEdit()
        self.search.setPlaceholderText(f"{self.KIND} — type, ↑↓, enter")
        self.search.setProperty("class", "search")
        self.search.setFrame(False)
        self.search.textChanged.connect(self._refilter)
        self.search.returnPressed.connect(self._confirm)
        root.addWidget(self.search)

        sep = QFrame()
        sep.setProperty("class", "sep")
        sep.setFixedHeight(1)
        root.addWidget(sep)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setProperty("class", "scroll")
        self.scroll.setFrameShape(QFrame.Shape.NoFrame)
        root.addWidget(self.scroll, 1)

        self.body = QWidget()
        self.flow_root = QVBoxLayout(self.body)
        self.flow_root.setContentsMargins(0, 0, 0, 0)
        self.flow_root.setSpacing(6)
        self.scroll.setWidget(self.body)

        QShortcut(QKeySequence(Qt.Key.Key_Escape), self, self.close)
        self._refilter()

    def _css(self, v):
        return f"""
        Picker {{ background: transparent; }}
        .frame {{ background: {v['background']};
            border: 1px solid {v['border']}; border-radius: 12px; }}
        .search {{ background: transparent; border: none;
            color: {v['text']}; font-size: 15px; padding: 6px 2px; }}
        .sep {{ background: {v['border']}; margin: 2px 0 8px 0; }}
        .scroll {{ border: none; background: transparent; }}
        .cell {{ background: transparent; border: 1px solid transparent;
            border-radius: 7px; }}
        .cell:hover {{ border: 1px solid {v['border']}; }}
        .cell.selected {{ background: {v['surface']};
            border: 1px solid {v['accent']}; }}
        .cell.active .cell-label {{ color: {v['accent']}; }}
        .cell-label {{ color: {v['text']}; font-size: 12px;
            background: transparent; }}
        """

    def _sections(self):
        if FONTS_MODE:
            return (("all", None),)
        return (("dark", "Dark"), ("light", "Light"))

    def _refilter(self):
        q = self.search.text().strip().lower()
        self.filtered = [t for t in self.items if not q or q in t["name"].lower()]
        while self.flow_root.count():
            ch = self.flow_root.takeAt(0)
            if ch.widget():
                ch.widget().deleteLater()
        self.cells = []
        self._wraps = []
        for section, label in self._sections():
            items = [t for t in self.filtered
                     if section == "all" or t["section"] == section]
            if not items:
                continue
            if label:
                head = QLabel(label)
                head.setProperty("class", "section")
                self.flow_root.addWidget(head)
            wrap = QWidget()
            self._wraps.append(wrap)
            self.flow_root.addWidget(wrap)
            flow = FlowLayout(wrap, spacing=6)
            for t in items:
                state = "selected" if not self.cells else ""
                if t["name"] == self.current:
                    state = (state + " active").strip()
                cell = ThemeCell(t, state, self._pick, self._hover)
                flow.addWidget(cell)
                self.cells.append(cell)
        self.sel = 0
        self.flow_root.addStretch(1)
        self._sync_sel()

    def _sync_sel(self):
        for i, cell in enumerate(self.cells):
            base = "selected" if i == self.sel else ""
            if self.filtered[i]["name"] == self.current:
                base = (base + " active").strip()
            cell.set_state(base)
        if self.cells:
            self.scroll.ensureWidgetVisible(self.cells[self.sel])

    def _hover(self, name):
        for i, t in enumerate(self.filtered):
            if t["name"] == name and i != self.sel:
                self.sel = i
                self._sync_sel()
                break

    def _move(self, delta):
        if not self.cells:
            return
        self.sel = (self.sel + delta) % len(self.cells)
        self._sync_sel()

    def _cols(self):
        vw = self.scroll.viewport().width() or 1
        return max(1, vw // 184)

    def keyPressEvent(self, ev):
        k = ev.key()
        if k == Qt.Key.Key_Down:
            self._move(self._cols())
        elif k == Qt.Key.Key_Up:
            self._move(-self._cols())
        elif k in (Qt.Key.Key_Right, Qt.Key.Key_Tab):
            self._move(1)
        elif k in (Qt.Key.Key_Left, Qt.Key.Key_Backtab):
            self._move(-1)
        elif k in (Qt.Key.Key_PageDown,):
            self._move(8)
        elif k in (Qt.Key.Key_PageUp,):
            self._move(-8)
        else:
            super().keyPressEvent(ev)

    def focusOutEvent(self, ev):
        super().focusOutEvent(ev)
        self.close()

    def _confirm(self):
        if self.filtered:
            self._pick(self.filtered[self.sel]["name"])

    def apply_item(self, name):
        if FONTS_MODE:
            subprocess.run(
                font_bin() + ["set", name],
                capture_output=True,
                creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
            )
        else:
            subprocess.run(
                [EXE, "set", name],
                capture_output=True,
                creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
            )

    def _pick(self, name):
        self.apply_item(name)
        self.close()


def selftest(app, items, current, vars_):
    """Offscreen end-to-end: build, filter, keyboard-pick (no real apply)."""
    w = Picker(items, current, vars_)
    cells = w.findChildren(ThemeCell)
    print(f"items={len(items)} cells={len(cells)} current={current!r}")
    assert len(cells) == len(items), "cell count mismatch"
    picked = []
    w.apply_item = picked.append
    probe = "hack" if FONTS_MODE else "nord"
    w.search.setText(probe)
    assert w.filtered, "filter found nothing"
    w._move(1)
    w._confirm()
    expect = w.filtered[1]["name"] if len(w.filtered) > 1 else w.filtered[0]["name"]
    print(f"filter={probe} picked={picked}")
    assert picked == [expect], "keyboard pick path broken"
    w.search.setText("")
    assert len(w.cells) == len(items), "clear-filter restore broken"
    print("smoke: flexbox + keyboard path OK")
    return 0


def main():
    smoke = "--smoke" in sys.argv
    if smoke:
        os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication(sys.argv if not smoke else [sys.argv[0]])
    items = load_items()
    current = active_name()
    # chrome follows the bar theme: in fonts mode re-resolve via theme tool
    theme_now = current
    if FONTS_MODE:
        try:
            out = subprocess.run([EXE, "current"], capture_output=True, timeout=10)
            theme_now = out.stdout.decode("utf-8", "replace").strip()
        except Exception:
            theme_now = ""
    vars_ = theme_vars(theme_now)
    w = Picker(items, current, vars_)
    if smoke:
        return selftest(app, items, current, vars_)
    screen = QApplication.screenAt(QCursor.pos()) or app.primaryScreen()
    if screen:
        geo = screen.availableGeometry()
        x = geo.center().x() - w.width() // 2
        w.move(x, geo.top() + 48)
    w.show()
    w.raise_()
    w.activateWindow()
    w.search.setFocus()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
