#!/usr/bin/env python3
"""Bar font switcher: list / current / set / next / prev over the four
font vars in styles.css (:root preamble). Nerd-family names only; the
catalog (fonts.json) is registry-enumerated. YASB hot-reloads the sheet.
Usage: yasb-font.py list|current|set <family>|next|prev [--styles PATH]
"""
import re
import sys

VARS = ["--icons-font", "--icons-font-fallback", "--system-font", "--specialFont"]


def default_css():
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    q = os.path.normpath(os.path.join(here, "..", "..", "styles.css"))
    if os.path.exists(q):
        return q
    return os.path.join(os.path.expanduser("~"), ".config", "yasb", "styles.css")


def read_lines(path):
    data = open(path, encoding="utf-8").read().split("\n")
    return data


STRIP_TAIL = {'regular', 'bold', 'italic', 'bolditalic', 'light', 'extralight',
                'thin', 'medium', 'semibold', 'text', 'black', 'heavy', 'demibold'}


def discover():
    """Live system enumeration: any installed face whose name contains
    'nerd font' or 'NF' (regex, never hardcoded). Grouped to families."""
    import os
    names = set()
    if os.name == 'nt':
        import winreg
        for hive in (winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER):
            try:
                key = winreg.OpenKey(
                    hive, r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts')
            except OSError:
                continue
            i = 0
            while True:
                try:
                    n, _, _ = winreg.EnumValue(key, i)
                    i += 1
                except OSError:
                    break
                if re.search(r'nerd font|NF(M|P)?\b', n, re.I):
                    names.add(re.sub(r'\s*\(truetype\)\s*$', '', n,
                                     flags=re.I).strip())
    fams = {}
    for n in names:
        toks = n.split()
        while len(toks) > 2 and toks[-1].lower() in STRIP_TAIL:
            toks.pop()
        fams.setdefault(' '.join(toks), []).append(n)
    return sorted(fams)


def families(path):
    """Live discovery first; static catalog fallback; current value last."""
    live = discover()
    if live:
        return live
    cur = current(path)
    return [cur] if cur else []


def current(path):
    for l in read_lines(path)[:40]:
        m = re.search(r'--system-font:\s*"([^"]+)"', l)
        if m:
            return m.group(1)
    return ""


def set_family(path, fam):
    fams = families(path)
    hit = next((f for f in fams if f.lower() == fam.lower()), None)
    if hit is None:
        print(f"unknown font: {fam}")
        print("available:", ", ".join(fams))
        sys.exit(1)
    lines = read_lines(path)
    n = 0
    for i in range(min(40, len(lines))):
        for v in VARS:
            if re.match(r'\s*' + re.escape(v) + r'\s*:', lines[i]):
                lines[i] = re.sub(r':\s*.*;', f': "{hit}";', lines[i])
                n += 1
    open(path, "w", encoding="utf-8", newline="").write("\n".join(lines))
    print(hit)


def main(argv):
    args, path, skip = [], default_css(), False
    for a in argv:
        if skip:
            path, skip = a, False
        elif a == "--styles":
            skip = True
        else:
            args.append(a)
    if not args or args[0] == "list":
        cur = current(path)
        for f in families(path):
            print(("* " if f == cur else "  ") + f)
    elif args[0] == "current":
        sys.stdout.write(current(path))
    elif args[0] == "set" and len(args) > 1:
        set_family(path, " ".join(args[1:]))
    elif args[0] in ("next", "prev"):
        fams = families(path)
        cur = current(path)
        i = fams.index(cur) if cur in fams else -1
        set_family(path, fams[(i + (1 if args[0] == "next" else -1)) % len(fams)])
    else:
        print(__doc__)
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
