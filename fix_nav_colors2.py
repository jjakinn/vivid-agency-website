#!/usr/bin/env python3
"""
Fix nav text color: default black, dark mode white.
Replaces the old light-mode-detection CSS with flipped logic.
"""

from pathlib import Path

BASE = Path("/Users/Jakin/rize-clone/rizeagency.co")

FILES = [
    "index.html",
    "Our-Movement/index.html",
    "Our-Movement/index-2.html",
    "Our-Movement/index-3.html",
    "Our-Movement/Rizeagency.html",
    "Our-Movement/Rizeagency-2.html",
    "Our-Movement/Rizeagency-3.html",
    "our-referral-program/index.html",
    "our-referral-program/Rizeagency.html",
    "Rizeagency.html",
    "index18a1.html",
    "index67c7.html",
]

# Old blocks to replace (various forms that may exist)
OLD_BLOCKS = [
    """\t\t\t/* Nav menu text white for dark header */
\t\t\t.main-menu-link,
\t\t\t.item-title,
\t\t\t.menu-link span,
\t\t\t.branding nav a,
\t\t\t.branding .menu a {
\t\t\t\tcolor: #ffffff !important;
\t\t\t}
\t\t\t.branding .menu a:hover {
\t\t\t\tcolor: #cccccc !important;
\t\t\t}
\t\t\t/* Light mode: black text */
\t\t\tbody.light .main-menu-link,
\t\t\tbody.light .item-title,
\t\t\tbody.light .menu-link span,
\t\t\tbody.light .branding nav a,
\t\t\tbody.light .branding .menu a,
\t\t\thtml.light .main-menu-link,
\t\t\thtml.light .item-title,
\t\t\thtml.light .menu-link span,
\t\t\thtml.light .branding nav a,
\t\t\thtml.light .branding .menu a,
\t\t\tbody:not(.dark) .main-menu-link,
\t\t\tbody:not(.dark) .item-title,
\t\t\tbody:not(.dark) .menu-link span,
\t\t\tbody:not(.dark) .branding nav a,
\t\t\tbody:not(.dark) .branding .menu a {
\t\t\t\tcolor: #000000 !important;
\t\t\t}""",
]

NEW_BLOCK = """\t\t\t/* Default: black nav text for light backgrounds */
\t\t\t.main-menu-link,
\t\t\t.item-title,
\t\t\t.menu-link span,
\t\t\t.branding nav a,
\t\t\t.branding .menu a {
\t\t\t\tcolor: #000000 !important;
\t\t\t}
\t\t\t.branding .menu a:hover {
\t\t\t\tcolor: #333333 !important;
\t\t\t}
\t\t\t/* Dark mode: white text */
\t\t\tbody.dark .main-menu-link,
\t\t\tbody.dark .item-title,
\t\t\tbody.dark .menu-link span,
\t\t\tbody.dark .branding nav a,
\t\t\tbody.dark .branding .menu a,
\t\t\thtml.dark .main-menu-link,
\t\t\thtml.dark .item-title,
\t\t\thtml.dark .menu-link span,
\t\t\thtml.dark .branding nav a,
\t\t\thtml.dark .branding .menu a {
\t\t\t\tcolor: #ffffff !important;
\t\t\t}
\t\t\tbody.dark .branding .menu a:hover,
\t\t\thtml.dark .branding .menu a:hover {
\t\t\t\tcolor: #cccccc !important;
\t\t\t}"""

for rel_path in FILES:
    path = BASE / rel_path
    if not path.exists():
        print(f"Skip: {rel_path}")
        continue

    content = path.read_text()
    original = content

    for old in OLD_BLOCKS:
        content = content.replace(old, NEW_BLOCK)

    # Also handle case where only the white default exists (no light override)
    simple_old = """\t\t\t/* Nav menu text white for dark header */
\t\t\t.main-menu-link,
\t\t\t.item-title,
\t\t\t.menu-link span,
\t\t\t.branding nav a,
\t\t\t.branding .menu a {
\t\t\t\tcolor: #ffffff !important;
\t\t\t}
\t\t\t.branding .menu a:hover {
\t\t\t\tcolor: #cccccc !important;
\t\t\t}"""
    if simple_old in content:
        content = content.replace(simple_old, NEW_BLOCK)

    if content != original:
        path.write_text(content)
        print(f"Updated: {rel_path}")
    else:
        print(f"No changes: {rel_path}")

print("Done.")
