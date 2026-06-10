import re, sys, os, glob

paths = sys.argv[1:] if len(sys.argv) > 1 else ['index.html']

for path in paths:
    if not os.path.exists(path):
        print(f"Skip missing: {path}")
        continue
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Replace visible text content only, not URLs
    replacements = [
        # Titles & meta
        ("Rize - Creator Management Agency", "Vivid - Creator Management Agency"),
        ("Rize%20-%20Creator%20Management%20Agency", "Vivid%20-%20Creator%20Management%20Agency"),
        ("Rize - OnlyFans Management Agency", "Vivid - OnlyFans Management Agency"),
        ("Rize%20-%20OnlyFans%20Management%20Agency", "Vivid%20-%20OnlyFans%20Management%20Agency"),
        # Brand name
        ("Rize Agency", "Vivid Agency"),
        # Hashtag
        ("#TogetherWeRize", "#TogetherWeVivid"),
        # CTAs - case variations
        ("Apply to rize", "Apply to vivid"),
        ("Apply to Rize", "Apply to Vivid"),
        # Description text
        ("Rize is the UK", "Vivid is the UK"),
        ("Rize is the UK's leading", "Vivid is the UK's leading"),
        ("Rize is a movement", "Vivid is a movement"),
        ("Rize isn't just", "Vivid isn't just"),
        # About section
        ("About Rize", "About Vivid"),
        # Standalone "Rize" in text content (careful)
        ('"Rize"', '"Vivid"'),
        ("'Rize'", "'Vivid'"),
        # JSON schema specific
        ('"name":"Rize', '"name":"Vivid'),
        ('"name":"Rize Agency"', '"name":"Vivid Agency"'),
        # RSS / feed titles
        ('title="Rize Agency', 'title="Vivid Agency'),
        # File references
        ('href="Rizeagency.html"', 'href="Vividagency.html"'),
        ('href="Rizeagency-2.html"', 'href="Vividagency-2.html"'),
        ('href="Rizeagency-3.html"', 'href="Vividagency-3.html"'),
        # Wordplay: "rize to their full potential" -> "rise to their full potential"
        ("wants to rize to their full potential", "wants to rise to their full potential"),
        # Standalone brand references that slipped through
        (">Rize ", ">Vivid "),
        ("Rize isn't just", "Vivid isn't just"),
        ("Rize is a", "Vivid is a"),
        # Referral page specific
        ("Rize profits", "Vivid profits"),
        ("Rize can help", "Vivid can help"),
        ("Rize movement", "Vivid movement"),
        ("Rize makes", "Vivid makes"),
        ("Rize Partner", "Vivid Partner"),
        ("the Rize", "the Vivid"),
        ("into Rize", "into Vivid"),
        ("with Rize", "with Vivid"),
        ("for Rize", "for Vivid"),
        ("about Rize", "about Vivid"),
        ("by Rize", "by Vivid"),
        ("to Rize", "to Vivid"),
        # External domain links in hrefs (should point to vivid now)
        ('href="Rizeagency.co"', 'href="https://vividagency.co"'),
    ]

    for old, new in replacements:
        text = text.replace(old, new)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Done: {path}")
