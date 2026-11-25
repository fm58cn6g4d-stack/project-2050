#!/usr/bin/env python3
"""Role: checks every text and color pair in tokens.json against WCAG 2.2 AA (stage H step H9).
Status: draft, November 25, 2026. Prints the table; exits 1 if any required pair fails.
Usage: python3 models/tools/public-product/design/check_tokens.py [--markdown]
"""
import json, pathlib, sys

PAIRS = [  # (foreground, background, use, minimum ratio)
    ("text", "bg", "body text", 4.5),
    ("text", "surface", "body text on panels", 4.5),
    ("muted", "bg", "secondary text", 4.5),
    ("muted", "surface", "secondary text on panels", 4.5),
    ("accent", "bg", "links, labels in the accent color", 4.5),
    ("accent", "surface", "links on panels", 4.5),
    ("accent-ink", "accent", "button label", 4.5),
    ("accent-2", "bg", "flagship label", 4.5),
    ("tag-fg", "tag-bg", "the imagined-scene tag", 4.5),
    ("focus", "bg", "focus ring (non-text, 1.4.11)", 3.0),
]


def luminance(hex_color):
    h = hex_color.lstrip("#")
    out = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        out.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * out[0] + 0.7152 * out[1] + 0.0722 * out[2]


def ratio(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def main():
    tokens = json.loads((pathlib.Path(__file__).with_name("tokens.json")).read_text())
    rows, failed = [], 0
    for key, d in tokens["directions"].items():
        for mode in ("light", "dark"):
            c = d["color"][mode]
            for fg, bg, use, minimum in PAIRS:
                r = ratio(c[fg], c[bg])
                ok = r >= minimum
                failed += not ok
                rows.append((f"{key} {d['name']}", mode, f"{fg} on {bg}", c[fg], c[bg], f"{r:.2f}", minimum, "pass" if ok else "FAIL", use))
    if "--markdown" in sys.argv:
        print("| Direction | Mode | Pair | Colors | Ratio | AA needs | Result | Use |")
        print("| --- | --- | --- | --- | --- | --- | --- | --- |")
        for r in rows:
            print(f"| {r[0]} | {r[1]} | {r[2]} | `{r[3]}` on `{r[4]}` | {r[5]}:1 | {r[6]}:1 | {r[7]} | {r[8]} |")
    else:
        for r in rows:
            print(" ".join(str(x) for x in r[:8]))
        print(f"{len(rows)} pairs, {failed} failing")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
