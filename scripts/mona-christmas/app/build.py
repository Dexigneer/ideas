#!/usr/bin/env python3
"""Build the Mona Prompt Studio web app from the markdown scripts.

Usage:  python3 scripts/mona-christmas/app/build.py
Output: scripts/mona-christmas/app/index.html  (single self-contained page)

Reads:
  ../00-sheets-characters-locations.md   reference-image prompts
  ../A|B|C-test-*.md                      30 test scripts
  ../A|B|C-full/*.md                      270 expanded scripts
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

SLOGANS = {
    "A": "You met me at a very Christmas time of the year",
    "B": "Santa works for me",
    "C": "Oh my reindeer!",
}

SHOT_FULL = re.compile(r"^\*\*(S\d+)\s*·\s*(.+?)\*\*\s*(.*)$")
SHOT_TEST = re.compile(r"^\*\*(S\d+)\*\*\s*·\s*(.*)$")
NOTE = re.compile(r"^\*\*([^*]+?):\*\*\s*(.*)$")
TABLE_ROW = re.compile(r"^\|\s*(S\d+)\s*\|(.*)\|\s*$")


def clean(s: str) -> str:
    s = s.replace("`", "")
    s = re.sub(r"\*\*?", "", s)
    return s.strip()


def split_refs(rest: str):
    """'… · Refs: `@MONA-A` `LOC-05`' -> (line, [refs])"""
    refs = []
    m = re.search(r"Refs:\s*(.*)$", rest)
    if m:
        refs = re.findall(r"`([^`]+)`", m.group(1))
        rest = rest[: m.start()]
    rest = rest.strip().rstrip("·").strip()
    return rest, refs


def parse_scripts(path: Path, slogan: str, category: str, is_test: bool):
    text = path.read_text(encoding="utf-8")
    if not is_test:
        h1 = re.search(r"^# .*?·\s*(.+)$", text, re.M)
        if h1:
            category = h1.group(1).strip()
    sections = re.split(r"^## (?=[ABC]\d+\s·)", text, flags=re.M)[1:]
    out = []
    for sec in sections:
        lines = sec.split("\n")
        head = lines[0].strip()
        m = re.match(r"([ABC]\d+)\s*·\s*(.+)", head)
        if not m:
            continue
        sid, title = m.group(1), m.group(2).strip()
        meta_line = ""
        info = []
        notes = []
        shots = []
        table = {}
        i = 1
        while i < len(lines):
            line = lines[i].rstrip()
            if not meta_line and line.startswith("`F"):
                meta_line = clean(line)
            tr = TABLE_ROW.match(line)
            if tr:
                cells = [c.strip() for c in tr.group(2).split("|")]
                table[tr.group(1)] = cells
            sf = SHOT_FULL.match(line) if not is_test else None
            st = SHOT_TEST.match(line) if is_test else None
            if sf or st:
                if sf:
                    shot_id = sf.group(1)
                    head_txt = sf.group(2)
                    rest = sf.group(3)
                    # head_txt like "0,0–2,2 · KEV:" ; rest like „line“ · Refs: …
                    parts = [p.strip() for p in head_txt.split("·")]
                    time = parts[0] if parts else ""
                    who = " · ".join(parts[1:]).rstrip(":").strip()
                    line_txt, refs = split_refs(rest)
                    desc = clean((who + (": " if who and line_txt else "") + line_txt).strip())
                else:
                    shot_id = st.group(1)
                    _, refs = split_refs(st.group(2))
                    cells = table.get(shot_id, [])
                    time = cells[0] if cells else ""
                    desc = clean(" · ".join(c for c in cells[2:] if c and c not in ("—", "-")))
                # find prompt block
                j = i + 1
                while j < len(lines) and not lines[j].startswith("```"):
                    j += 1
                k = j + 1
                buf = []
                while k < len(lines) and not lines[k].startswith("```"):
                    buf.append(lines[k])
                    k += 1
                shots.append({
                    "id": shot_id,
                    "time": time.replace(",", "."),
                    "desc": desc,
                    "refs": refs,
                    "prompt": "\n".join(buf).strip(),
                })
                i = k + 1
                continue
            nm = NOTE.match(line)
            if nm:
                label = nm.group(1).strip()
                if label.startswith("Hook text"):
                    label = "Hook text"
                val = clean(nm.group(2))
                if label in ("Hook text", "Easter egg", "Prečo zaberie"):
                    info.append({"label": label, "text": val})
                else:
                    notes.append({"label": label, "text": val})
            i += 1
        fmt = re.search(r"\bF\d\b", meta_line)
        dur = re.search(r"(\d+)\s*s\b", meta_line)
        out.append({
            "id": sid,
            "slogan": slogan,
            "title": title,
            "category": category,
            "test": is_test,
            "format": fmt.group(0) if fmt else "",
            "duration": int(dur.group(1)) if dur else None,
            "meta": meta_line,
            "info": info,
            "shots": shots,
            "notes": notes,
        })
    return out


def parse_sheets(path: Path):
    lines = path.read_text(encoding="utf-8").split("\n")
    items = []
    current_group = ""
    last_title = ""
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("## "):
            current_group = clean(line[3:])
        elif line.startswith("### "):
            last_title = clean(line[4:])
        elif re.match(r"^\*\*LOC-\d+", line):
            last_title = clean(line)
        if line.startswith("```text"):
            k = i + 1
            buf = []
            while k < len(lines) and not lines[k].startswith("```"):
                buf.append(lines[k])
                k += 1
            items.append({"group": current_group, "title": last_title, "prompt": "\n".join(buf).strip()})
            i = k + 1
            continue
        i += 1
    return items


def main():
    videos = []
    tests = {"A": "A-test-you-met-me.md", "B": "B-test-santa-works-for-me.md", "C": "C-test-oh-my-reindeer.md"}
    for s, fname in tests.items():
        videos += parse_scripts(ROOT / fname, s, "Testovacie videá", True)
    for s in "ABC":
        for f in sorted((ROOT / f"{s}-full").glob("*.md")):
            videos += parse_scripts(f, s, "", False)
    sheets = parse_sheets(ROOT / "00-sheets-characters-locations.md")
    data = {"slogans": SLOGANS, "videos": videos, "sheets": sheets}
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    tpl = (HERE / "template.html").read_text(encoding="utf-8")
    html = tpl.replace("/*__DATA__*/null", payload)
    (HERE / "index.html").write_text(html, encoding="utf-8")
    n_shots = sum(len(v["shots"]) for v in videos)
    empty = [v["id"] + "/" + s["id"] for v in videos for s in v["shots"] if not s["prompt"]]
    print(f"videos={len(videos)} shots={n_shots} sheets={len(sheets)} empty_prompts={len(empty)} size={len(html)//1024}KB")
    if empty:
        print("EMPTY:", empty[:20])


if __name__ == "__main__":
    main()
