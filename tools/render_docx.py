"""Render minimalQMS Markdown documents (SOPs, templates) to a Word review pack.

Usage:
    python tools/render_docx.py OUTPUT.docx FILE.md [FILE.md ...] [--source "branch@commit"]

Handles the Markdown subset minimalQMS documents use: YAML front matter, headings,
paragraphs, bullet and numbered lists, tables, code blocks, **bold**, *italic*,
`code` and [links](url). Each document starts on a new page with a header block taken
from its front matter. Output is a review copy and is marked as uncontrolled.

Requires: python-docx (pip install python-docx), PyYAML.
"""
import os
import re
import sys
from datetime import date

import yaml
from docx import Document
from docx.enum.text import WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

INLINE = re.compile(r"(\*\*[^*]+\*\*|\*[^*\s][^*]*\*|`[^`]+`|\[[^\]]+\]\([^)]+\))")


def add_inline(par, text):
    """Add text to a paragraph, applying bold / italic / code / link formatting."""
    for part in INLINE.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            add_inline_run(par, part[2:-2], bold=True)
        elif part.startswith("`") and part.endswith("`"):
            run = par.add_run(part[1:-1])
            run.font.name = "Consolas"
            run.font.size = Pt(9.5)
        elif part.startswith("[") and "](" in part:
            label, url = re.match(r"\[([^\]]+)\]\(([^)]+)\)", part).groups()
            run = par.add_run(label)
            run.font.color.rgb = RGBColor(0x1F, 0x4E, 0x99)
            run.underline = True
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            add_inline_run(par, part[1:-1], italic=True)
        else:
            par.add_run(part)


def add_inline_run(par, text, bold=False, italic=False):
    # nested formatting inside bold/italic (e.g. **`code`**) is flattened to the outer style
    text = re.sub(r"`([^`]+)`", r"\1", text)
    run = par.add_run(text)
    run.bold = bold
    run.italic = italic


def shade(cell, hex_fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_fill)
    tc_pr.append(shd)


def header_block(doc, meta, path, source):
    title = f"{meta.get('id', '')} {meta.get('title', '')}".strip() or path
    doc.add_heading(title, level=0)
    rows = [
        ("Document", meta.get("id", path)),
        ("Revision", str(meta.get("rev", "-"))),
        ("Status", str(meta.get("status", "-")).upper()),
        ("Owner", str(meta.get("owner", "-"))),
        ("Standard", str(meta.get("standard", "-"))),
        ("Source", f"{path}  ({source})" if source else path),
        ("Rendered", date.today().isoformat()),
    ]
    table = doc.add_table(rows=len(rows), cols=2)
    table.style = "Table Grid"
    for i, (k, v) in enumerate(rows):
        table.cell(i, 0).text = k
        table.cell(i, 1).text = v
        shade(table.cell(i, 0), "E8EEF7")
        table.cell(i, 0).paragraphs[0].runs[0].bold = True
    note = doc.add_paragraph()
    run = note.add_run(
        "REVIEW COPY: uncontrolled. The controlled version is the file on the main branch. "
        "Comment in this document; changes are made in the source file."
    )
    run.italic = True
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(0xA0, 0x30, 0x30)


def render_table(doc, lines):
    rows = [
        [c.strip() for c in ln.strip().strip("|").split("|")]
        for ln in lines
        if not re.match(r"^\s*\|?\s*:?-{3,}", ln)
    ]
    width = max(len(r) for r in rows)
    table = doc.add_table(rows=len(rows), cols=width)
    table.style = "Table Grid"
    for i, row in enumerate(rows):
        for j in range(width):
            cell = table.cell(i, j)
            cell.text = ""
            add_inline(cell.paragraphs[0], row[j] if j < len(row) else "")
            if i == 0:
                shade(cell, "E8EEF7")
                for r in cell.paragraphs[0].runs:
                    r.bold = True
    doc.add_paragraph()


def render(doc, text, path, source, file_path=None):
    file_path = file_path or path
    meta = {}
    if text.startswith("---"):
        _, fm, text = text.split("---", 2)
        meta = yaml.safe_load(fm) or {}
    header_block(doc, meta, path, source)

    lines = text.splitlines()
    i = 0
    skipped_title = False
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue
        if stripped.startswith("```"):
            block = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                block.append(lines[i])
                i += 1
            par = doc.add_paragraph()
            run = par.add_run("\n".join(block))
            run.font.name = "Consolas"
            run.font.size = Pt(9)
            i += 1
            continue
        m = re.match(r"^(#{1,6})\s+(.*)", stripped)
        if m:
            level = len(m.group(1))
            if level == 1 and not skipped_title:
                skipped_title = True  # the header block already shows the title
            else:
                doc.add_heading(m.group(2), level=min(level - 1, 3) or 1)
            i += 1
            continue
        if stripped.startswith("|"):
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(lines[i])
                i += 1
            render_table(doc, block)
            continue
        m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)", line)
        if m:
            indent = len(m.group(1)) // 2
            numbered = m.group(2)[0].isdigit()
            item = m.group(3)
            i += 1
            # continuation lines (indented, not a new list item)
            while (
                i < len(lines)
                and lines[i].strip()
                and lines[i].startswith(" ")
                and not re.match(r"^\s*([-*]|\d+\.)\s+", lines[i])
            ):
                item += " " + lines[i].strip()
                i += 1
            if numbered:
                # keep the source numbering; Word's auto-numbering would run on across documents
                par = doc.add_paragraph()
                par.paragraph_format.left_indent = Pt(18 * (indent + 1))
                par.paragraph_format.first_line_indent = Pt(-14)
                par.paragraph_format.space_after = Pt(2)
                par.add_run(m.group(2) + " ")
                add_inline(par, item)
            else:
                style = "List Bullet 2" if indent else "List Bullet"
                add_inline(doc.add_paragraph(style=style), item)
            continue
        m = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)", stripped)
        if m:
            img = os.path.normpath(os.path.join(os.path.dirname(file_path), m.group(2)))
            if os.path.exists(img) and img.lower().endswith((".png", ".jpg", ".jpeg")):
                doc.add_picture(img, width=Inches(6.3))
            else:
                doc.add_paragraph(f"[figure: {m.group(1)} ({m.group(2)})]")
            i += 1
            continue
        if stripped.startswith(">"):
            par = doc.add_paragraph(style="Intense Quote")
            add_inline(par, stripped.lstrip("> "))
            i += 1
            continue
        # paragraph: join until blank line or a block element
        para = [stripped]
        i += 1
        while (
            i < len(lines)
            and lines[i].strip()
            and not re.match(r"^\s*(#|\||```|>|[-*]\s|\d+\.\s)", lines[i])
        ):
            para.append(lines[i].strip())
            i += 1
        add_inline(doc.add_paragraph(), " ".join(para))


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 1
    source = ""
    if "--source" in argv:
        k = argv.index("--source")
        source = argv[k + 1]
        argv = argv[:k] + argv[k + 2 :]
    out, files = argv[1], argv[2:]
    doc = Document()
    doc.styles["Normal"].font.name = "Calibri"
    doc.styles["Normal"].font.size = Pt(10.5)
    for n, path in enumerate(files):
        if n:
            doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
        with open(path, encoding="utf-8") as f:
            render(doc, f.read(), path.replace("\\", "/").split("/review-src/")[-1], source, path)
    doc.save(out)
    print(f"wrote {out} ({len(files)} documents)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
