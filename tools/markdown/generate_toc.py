#!/usr/bin/env python3
"""Generate / verify a Markdown TOC whose anchors match Hugo (goldmark, autoHeadingIDType = "github").

Usage (run from the Blog repo root):

    # 預覽（輸出到 stdout）
    python tools/markdown/generate_toc.py "content/posts/.../xxx.md"

    # 改寫檔案中 <!-- TOC-AUTO-BEGIN --> ... <!-- TOC-AUTO-END --> 區塊
    python tools/markdown/generate_toc.py "content/posts/.../xxx.md" --write

    # 以 Hugo 實際輸出的 HTML 驗證所有目錄連結與標題 id
    hugo -d "%TEMP%/hugo-check"
    python tools/markdown/generate_toc.py "content/posts/.../xxx.md" --verify-html "%TEMP%/hugo-check/posts/.../index.html"

The TOC block format is:

    <!-- TOC-AUTO-BEGIN -->
    ## 目錄（Table of Contents）

    - [Heading](#anchor)
      - [Sub heading](#sub-anchor)

    <!-- TOC-AUTO-END -->
"""
from __future__ import annotations

import argparse
import html
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote

BEGIN = "<!-- TOC-AUTO-BEGIN -->"
END = "<!-- TOC-AUTO-END -->"
DEFAULT_TITLE = "## 目錄（Table of Contents）"

FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
ATX_RE = re.compile(r"^ {0,3}(#{1,6})[ \t]+(.*?)(?:[ \t]+#+)?[ \t]*$")
CUSTOM_ID_RE = re.compile(r"\s*\{#([^}]+)\}\s*$")


def heading_plain_text(raw: str) -> str:
    """Approximate goldmark's plain-text rendering of an inline heading."""
    text = raw
    text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", text)  # images -> alt
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)  # links -> text
    text = re.sub(r"`+([^`]*)`+", r"\1", text)  # inline code
    text = re.sub(r"<[^>]+>", "", text)  # raw inline HTML
    text = re.sub(r"(\*\*|__)(.+?)\1", r"\2", text)  # bold
    text = re.sub(r"(?<![\w*])([*_])(?!\s)(.+?)(?<!\s)\1(?![\w*])", r"\2", text)  # italic
    text = re.sub(r"~~(.+?)~~", r"\1", text)  # strikethrough
    text = re.sub(r"\\([\\`*_{}\[\]()#+\-.!|<>~])", r"\1", text)  # escapes
    return html.unescape(text).strip()


def github_slug(text: str) -> str:
    """Hugo/goldmark `github` anchor rule.

    Letters and digits are lower-cased and kept, spaces become '-', '-' and '_' are
    kept, every other rune (punctuation, symbols, emoji, full-width marks) is dropped.
    """
    out = []
    for ch in text:
        cat = unicodedata.category(ch)
        if cat[0] in ("L", "N"):  # combining marks such as U+FE0F are dropped, like Hugo
            out.append(ch.lower())
        elif ch in "-_":
            out.append(ch)
        elif ch == " ":
            out.append("-")
    return "".join(out)


class Heading:
    __slots__ = ("line", "level", "text", "anchor")

    def __init__(self, line: int, level: int, text: str, anchor: str):
        self.line, self.level, self.text, self.anchor = line, level, text, anchor


def parse_headings(lines: list[str]) -> list[Heading]:
    """Return every ATX heading (H1-H6) outside code fences and front matter, with unique ids."""
    headings: list[Heading] = []
    used: dict[str, int] = {}
    seen: set[str] = set()
    in_fence, fence = False, ""
    start = 0
    if lines and lines[0].strip() in ("+++", "---"):
        marker = lines[0].strip()
        for i in range(1, len(lines)):
            if lines[i].strip() == marker:
                start = i + 1
                break
    for idx in range(start, len(lines)):
        line = lines[idx]
        m = FENCE_RE.match(line)
        if m:
            if not in_fence:
                in_fence, fence = True, m.group(1)
            elif m.group(1).startswith(fence) and not m.group(2).strip():
                in_fence = False
            continue
        if in_fence:
            continue
        m = ATX_RE.match(line)
        if not m:
            continue
        raw = m.group(2)
        cm = CUSTOM_ID_RE.search(raw)
        if cm:
            raw = raw[: cm.start()]
            anchor = cm.group(1)
        else:
            base = github_slug(heading_plain_text(raw))
            anchor = base
            if anchor in seen:
                n = used.get(base, 0)
                while True:
                    n += 1
                    anchor = f"{base}-{n}"
                    if anchor not in seen:
                        break
                used[base] = n
        seen.add(anchor)
        headings.append(Heading(idx + 1, len(m.group(1)), heading_plain_text(raw), anchor))
    return headings


def link_text(text: str) -> str:
    return text.replace("[", r"\[").replace("]", r"\]")


def build_toc(headings: list[Heading], title: str, min_level: int, max_level: int) -> list[str]:
    title_text = heading_plain_text(title.lstrip("#").strip())
    body = [h for h in headings if min_level <= h.level <= max_level and h.text != title_text]
    out = [BEGIN, title, ""]
    for h in body:
        out.append(f"{'  ' * (h.level - min_level)}- [{link_text(h.text)}](#{h.anchor})")
    out += ["", END]
    return out


def find_block(lines: list[str]) -> tuple[int, int]:
    try:
        b = next(i for i, l in enumerate(lines) if l.strip() == BEGIN)
        e = next(i for i in range(b + 1, len(lines)) if lines[i].strip() == END)
    except StopIteration:
        sys.exit(f"error: markers {BEGIN} / {END} not found")
    return b, e


def verify_html(md_lines: list[str], html_path: Path) -> int:
    page = html_path.read_text(encoding="utf-8")
    ids = {unquote(x) for x in re.findall(r'\bid="?([^"\s>]+)"?', page)}
    heading_ids = [unquote(x) for x in re.findall(r"<h[1-6][^>]*\bid=\"?([^\"\s>]+)", page)]
    b, e = find_block(md_lines)
    toc_targets = [unquote(t) for t in re.findall(r"\]\(#([^)]+)\)", "\n".join(md_lines[b:e]))]

    broken = [t for t in toc_targets if t not in ids]
    expected = [h.anchor for h in parse_headings(md_lines)]
    missing_in_html = [a for a in expected if a not in heading_ids]
    toc_set = set(toc_targets)
    not_in_toc = [a for a in heading_ids if a not in toc_set]
    dup_ids = sorted({a for a in heading_ids if heading_ids.count(a) > 1})

    print(f"HTML heading ids         : {len(heading_ids)}")
    print(f"TOC links                : {len(toc_targets)}")
    print(f"Broken TOC links         : {len(broken)}")
    print(f"Predicted ids not in HTML: {len(missing_in_html)}")
    print(f"Duplicate heading ids    : {len(dup_ids)}")
    print(f"HTML headings not in TOC : {len(not_in_toc)} (H1/H5/H6 and the TOC title are expected here)")
    for label, items in (("broken", broken), ("predicted-missing", missing_in_html), ("duplicate", dup_ids)):
        for item in items[:50]:
            print(f"  [{label}] {item}")
    for item in not_in_toc[:20]:
        print(f"  [not-in-toc] {item}")
    return 1 if (broken or missing_in_html or dup_ids) else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", type=Path)
    ap.add_argument("--write", action="store_true", help="rewrite the TOC block in place")
    ap.add_argument("--min-level", type=int, default=2)
    ap.add_argument("--max-level", type=int, default=4)
    ap.add_argument("--title", default=None, help=f"TOC heading line (default: keep existing or '{DEFAULT_TITLE}')")
    ap.add_argument("--verify-html", type=Path, help="Hugo output page to verify anchors against")
    args = ap.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    raw = args.file.read_bytes().decode("utf-8")
    newline = "\r\n" if "\r\n" in raw else "\n"
    lines = raw.split(newline)

    if args.verify_html:
        return verify_html(lines, args.verify_html)

    b, e = find_block(lines)
    title = args.title
    if title is None:
        title = next((l for l in lines[b + 1 : e] if l.startswith("#")), DEFAULT_TITLE)
    toc = build_toc(parse_headings(lines), title, args.min_level, args.max_level)

    if not args.write:
        print("\n".join(toc))
        return 0
    new_lines = lines[:b] + toc + lines[e + 1 :]
    args.file.write_bytes(newline.join(new_lines).encode("utf-8"))
    print(f"TOC updated: {sum(1 for l in toc if l.lstrip().startswith('- ['))} entries -> {args.file}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
