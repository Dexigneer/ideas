#!/usr/bin/env python3
"""Build van/web/index.html – a single-file viewer with copy buttons for every prompt."""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import render as R  # noqa: E402

ROOT = R.ROOT


def sheets(md_path, head_re):
    """Parse a sheet markdown file into sections with their code blocks."""
    text = md_path.read_text(encoding="utf-8")
    parts = re.split(r"^## ", text, flags=re.M)[1:]
    out = []
    for p in parts:
        title, _, body = p.partition("\n")
        if not re.match(head_re, title):
            continue
        blocks = []
        label = ""
        intro = []
        in_code = False
        buf = []
        for line in body.splitlines():
            if line.startswith("```"):
                if in_code:
                    blocks.append({"label": label or "Prompt", "text": "\n".join(buf).strip()})
                    buf, label, in_code = [], "", False
                else:
                    in_code = True
                continue
            if in_code:
                buf.append(line)
                continue
            m = re.match(r"^\*\*(.+?)\*\*\s*$", line.strip())
            if m:
                label = m.group(1).rstrip(":")
            elif line.startswith("|") and not line.startswith("|---") and "**" in line:
                cells = [c.strip() for c in line.strip("|").split("|")]
                if len(cells) >= 2 and cells[0]:
                    intro.append([re.sub(r"\*\*", "", cells[0]), re.sub(r"[*`]", "", cells[1])])
            elif line.strip() and not line.startswith("|") and not line.startswith("---") and not line.startswith(">"):
                intro.append(["", re.sub(r"[*`]", "", line.strip())])
        if blocks:
            out.append({"title": title.strip(), "rows": intro, "blocks": blocks})
    return out


def main():
    eps = []
    for p in sorted((ROOT / "data").glob("*.txt")):
        eps += R.parse(p)
    eps.sort(key=lambda e: e["num"])
    data = []
    for ep in eps:
        code, sname = R.season_of(ep["num"])
        durs = [R.auto_dur(s) for s in ep["scenes"]]
        t = 0.0
        scenes, srt, hud = [], [], []
        for i, (s, d) in enumerate(zip(ep["scenes"], durs), 1):
            a, b = t, t + d
            t = b
            if s["text"]:
                srt.append(f"{len(srt) + 1}\n{R.srt_t(a)} --> {R.srt_t(b)}\n{s['text']}\n")
            for c in s["cues"]:
                if c.startswith("HUD:"):
                    hud.append(f"{len(hud) + 1}\n{R.srt_t(a)} --> {R.srt_t(b)}\n{c[4:].strip()}\n")
            scenes.append({
                "n": i, "a": round(a, 1), "b": round(b, 1), "shot": s["shot"],
                "shotName": R.SHOTS[s["shot"]][0].split(",")[0], "loc": s["loc"],
                "who": s["speaker"].replace("(VO)", " (VO)"), "line": s["text"],
                "cues": s["cues"], "refs": [c for c in s["chars"] if R.CHARS[c][1]] + [s["loc"]],
                "prompt": R.scene_prompt(ep, s, d),
            })
        chars = []
        for s in ep["scenes"]:
            for c in s["chars"]:
                if R.CHARS[c][1] and c not in chars:
                    chars.append(c)
        locs = list(dict.fromkeys(s["loc"] for s in ep["scenes"]))
        data.append({
            "num": ep["num"], "title": ep["title"], "type": ep["type"], "season": code, "seasonName": sname,
            "dur": round(t), "premise": ep.get("premise", ""), "emo": ep.get("emo", ""), "edu": ep.get("edu", ""),
            "clue": ep.get("clue", ""), "loop": ep.get("loop", ""), "cta": ep.get("cta") == "yes",
            "chars": chars, "locs": locs, "scenes": scenes,
            "srt": "\n".join(srt).strip(), "hud": "\n".join(hud).strip(),
            "caption": f"{ep['caption']}\n\n{R.HASHTAGS[ep['type']]} #vanexit",
        })
    payload = {
        "episodes": data,
        "locNames": {k: v[0] for k, v in R.LOCS.items()},
        "charNames": {k: v[0] for k, v in R.CHARS.items() if v[1]},
        "characters": sheets(ROOT / "01-character-sheets.md", r"^[1-9]\d*\. "),
        "locations": sheets(ROOT / "02-location-sheets.md", r"^L\d\d "),
        "style": sheets(ROOT / "01-character-sheets.md", r"^0\. "),
    }
    js = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    tpl = (ROOT / "tools" / "web_template.html").read_text(encoding="utf-8")
    out = ROOT / "web" / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(tpl.replace("/*__DATA__*/null", js), encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size // 1024} KB), {len(data)} episodes, "
          f"{sum(len(e['scenes']) for e in data)} scenes, {len(payload['characters'])} characters, "
          f"{len(payload['locations'])} locations")


if __name__ == "__main__":
    main()
