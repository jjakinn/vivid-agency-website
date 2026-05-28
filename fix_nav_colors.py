#!/usr/bin/env python3
"""
Fix nav text color on all rize-clone pages:
- Deduplicate CSS blocks if present
- Add light mode override (black text)
"""

import re
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

OLD_BLOCK = """\t\t\t/* Nav menu text white for dark header */
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

NEW_BLOCK = """\t\t\t/* Nav menu text white for dark header */
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
\t\t\t}"""

for rel_path in FILES:
    path = BASE / rel_path
    if not path.exists():
        print(f"Skip: {rel_path} (not found)")
        continue

    content = path.read_text()
    original = content

    # Deduplicate: replace double block with single block
    content = content.replace(OLD_BLOCK + "\n" + OLD_BLOCK, OLD_BLOCK)

    # Replace single block with new block
    if OLD_BLOCK in content:
        content = content.replace(OLD_BLOCK, NEW_BLOCK)
    else:
        # If no block found, maybe the formatting is different — try inserting before </style>
        pass

    if content != original:
        path.write_text(content)
        print(f"Updated: {rel_path}")
    else:
        print(f"No changes: {rel_path}")

print("Done.")
