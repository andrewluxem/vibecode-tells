#!/usr/bin/env python3
"""Heuristic scanner for vibecoded-design tells in HTML/CSS/JS/JSX/TSX/Vue/Svelte/MD files.

Usage: python scan.py <file-or-directory> [--json] [--strict]
--strict exits with code 1 when any tell is flagged (for CI).
Hits are leads for review, not verdicts.
"""
import colorsys, json, os, re, sys

EXTS = {".html", ".htm", ".css", ".scss", ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte", ".md", ".mdx", ".astro"}
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", ".vercel", "out", "coverage", ".svelte-kit"}

I = re.IGNORECASE
CHECKS = [
    (1, "Harsh gradients", re.compile(r"linear-gradient\(|conic-gradient\(|bg-gradient-to-[a-z]+", I)),
    (2, "Lucide icons", re.compile(r"lucide", I)),
    (3, "Pure white background", re.compile(r"background(-color)?\s*:\s*(#fff\b|#ffffff\b|white\b|rgb\(\s*255\s*,\s*255\s*,\s*255\s*\))|\bbg-white\b", I)),
    (4, "Rainbow coloring", re.compile(r"background-clip\s*:\s*text|bg-clip-text|text-transparent", I)),
    (5, "Drop shadows", re.compile(r"box-shadow\s*:(?!\s*none)|\bshadow-(sm|md|lg|xl|2xl)\b|drop-shadow", I)),
    (6, "3 feature cards in a row", re.compile(r"grid-cols-3\b|md:grid-cols-3|lg:grid-cols-3|repeat\(\s*3\s*,", I)),
    (8, "Liquid glass", re.compile(r"backdrop-filter|backdrop-blur", I)),
    (9, "Em dashes", re.compile(r"\u2014|&mdash;|&#8212;")),
    (10, "Inter/Geist/Space Grotesk", re.compile(r"\b(Inter|Geist|Space[ _+]Grotesk)\b")),
    (11, "Colored left stripe", re.compile(r"border-left\s*:\s*([3-9]|\d\d)px|\bborder-l-(4|8)\b", I)),
    (12, "Testimonials (verify real)", re.compile(r"testimonial", I)),
    (13, "Bento grid", re.compile(r"bento|(col-span-2|row-span-2)", I)),
    (14, "Terminal window", re.compile(r"#ff5f56|#ffbd2e|#27c93f|#ff5f57|#febc2e|#28c840|terminal-window|TerminalWindow", I)),
    (15, "\"It's not X, it's Y\" copy", re.compile(r"(it'?s|this is|we'?re)\s+not\s+(just\s+)?(a|an|the)?\s*[\w\- ]{1,40}[.,;:]\s*(it'?s|this is|we'?re)\b|not just [\w\- ]{1,40},\s*(but|it)", I)),
    (16, "Checkmark bullets", re.compile(r"[\u2713\u2714\u2705]|\bCheck(Circle|Circle2|Icon)?\b(?=[\s/>])", 0)),
    (17, "Pricing tiers", re.compile(r"most popular|/\s*mo(nth)?\b|per month", I)),
    (19, "Soft corner radius", re.compile(r"border-radius\s*:\s*(1[2-9]|[2-9]\d)px|\brounded-(xl|2xl|3xl)\b", I)),
    (20, "Purple (check purple-and-black)", re.compile(r"\b(bg|text|from|to|via|border)-(purple|violet|indigo|fuchsia)-\d{2,3}\b", I)),
    (22, "Radial orbs", re.compile(r"radial-gradient\(|\bblur-(2xl|3xl)\b|filter\s*:\s*blur\(\s*([4-9]\d|\d{3})px", I)),
    (23, "Dot grids", re.compile(r"radial-gradient\([^)]*1px|dot-grid|bg-dot|dotted-bg", I)),
    (24, "Sparkle icons", re.compile(r"sparkle|\u2728", I)),
    (25, "Animated arrows", re.compile(r"group-hover:translate-x|ArrowRight|\u2192", 0)),
    (28, "Hover animations", re.compile(r"hover:(scale|-?translate-y|shadow)|:hover[^{]*\{[^}]*(transform|translate|scale)", I)),
]
EMOJI = re.compile("[\U0001F300-\U0001FAFF\U00002600-\U000026FF\U00002700-\U000027BF\U0001F1E6-\U0001F1FF]")
HEX = re.compile(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b")
NAMES = {1: "Harsh gradients", 7: "Emojis", 21: "No skeleton loaders", 26: "No TOS", 27: "No privacy policy", 29: "Neon colors", 30: "Basic pastel colors"}


def files(root):
    if os.path.isfile(root):
        yield root
        return
    for d, dirs, fs in os.walk(root):
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
        for f in fs:
            if os.path.splitext(f)[1].lower() in EXTS:
                yield os.path.join(d, f)


def hls(h):
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    return colorsys.rgb_to_hls(r, g, b)


def scan(root):
    hits = {}
    blob = []
    neon, pastel = [], []

    def add(n, name, where, text):
        hits.setdefault(n, {"name": name, "hits": []})["hits"].append({"where": where, "text": text.strip()[:120]})

    for path in files(root):
        try:
            with open(path, encoding="utf-8", errors="ignore") as fh:
                content = fh.read()
        except OSError:
            continue
        blob.append(content)
        rel = os.path.relpath(path, root) if os.path.isdir(root) else os.path.basename(path)
        for i, line in enumerate(content.splitlines(), 1):
            where = f"{rel}:{i}"
            for n, name, rx in CHECKS:
                if rx.search(line):
                    add(n, name, where, line)
            if EMOJI.search(line):
                add(7, NAMES[7], where, line)
            for m in HEX.finditer(line):
                l, s = hls(m.group(1))[1:]
                if s > 0.85 and 0.45 <= l <= 0.65:
                    neon.append((where, m.group(0)))
                elif l >= 0.82 and 0.35 <= s <= 1.0:
                    pastel.append((where, m.group(0)))

    all_text = "\n".join(blob)
    if neon:
        for w, c in neon[:15]:
            add(29, NAMES[29], w, c)
    if len({c.lower() for _, c in pastel}) >= 3:
        for w, c in pastel[:15]:
            add(30, NAMES[30], w, c)
    if re.search(r"\bfetch\(|useQuery|useSWR|axios|isLoading|loading", all_text) and not re.search(r"skeleton", all_text, I):
        add(21, NAMES[21], "(project)", "Async data/loading states found but no skeleton components")
    if not re.search(r"terms(-of-service|-and-conditions)?\b|/tos\b|terms of (service|use)", all_text, I):
        add(26, NAMES[26], "(project)", "No terms of service page or link found")
    if not re.search(r"privacy", all_text, I):
        add(27, NAMES[27], "(project)", "No privacy policy page or link found")
    return hits


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(1)
    hits = scan(args[0])
    if "--json" in sys.argv:
        print(json.dumps(hits, indent=2))
        sys.exit(1 if hits and "--strict" in sys.argv else 0)
    manual = "Manual checks always needed: #12 are testimonials real, #18 are there real product demos, #15 copy framing beyond regex."
    if not hits:
        print("No mechanical tells found.\n" + manual)
        return
    print(f"Vibecode scan: {args[0]}\n{len(hits)} of 30 tells flagged (heuristic, verify each)\n")
    for n in sorted(hits):
        h = hits[n]
        print(f"#{n} {h['name']}  ({len(h['hits'])} hits)")
        for x in h["hits"][:8]:
            print(f"    {x['where']}  {x['text']}")
        if len(h["hits"]) > 8:
            print(f"    ... {len(h['hits']) - 8} more")
    print("\n" + manual)
    if "--strict" in sys.argv:
        sys.exit(1)


if __name__ == "__main__":
    main()
