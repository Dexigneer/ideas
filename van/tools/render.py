#!/usr/bin/env python3
"""Render VAN episode data files (van/data/*.txt) into copy-ready markdown.

Data format (one episode):

    #001 VISITOR
    type: A            # A = cutscene, B = tutorial level, C = idle/motivation
    emo: ...           # emotion the viewer should feel (Slovak)
    premise: ...       # one-sentence premise (Slovak)
    clue: ...          # visual clue / easter egg (Slovak)
    loop: ...          # how the ending loops (Slovak)
    edu: ...           # optional: what the viewer learns (Slovak)
    caption: ...       # TikTok / Reels caption (English)
    cta: yes           # optional: add SAVE GAME end card
    > SHOT | LOC | CHARS | SPEAKER: line | action | cues | @dur

Cues (comma separated): DROP, PING, OUT, LOOP, HUD:text, SFX:text, CARD:text
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STYLE = ("PS2-era video game cutscene (early 2000s console graphics), 4:3 frame, slightly low-poly 3D "
         "characters with smooth plastic-like skin shading, stylized hair with visible polygon edges, "
         "expressive Sims-like faces, cinematic game lighting")

CHARS = {
    "VAN": ("VAN", "man ~30, short dark slightly messy hair, light stubble, calm half-lidded eyes, black "
            "zip-up hoodie with small white monospace \"[ EXIT ]\" on the left chest, grey t-shirt, office "
            "lanyard with white badge reading \"VISITOR\", NO wristwatch, plain white ceramic mug",
            "calm, low, slow, dry deadpan voice, tiny pause before the last word"),
    "JUNE": ("JUNE", "woman ~27, copper-red hair in a messy side braid, round tortoiseshell glasses, freckles, "
             "oversized oatmeal-beige knit sweater, blue lanyard with photo badge \"EMPLOYEE\", paper coffee "
             "cup, cheap digital wristwatch",
             "fast, expressive young woman's voice, stressing the CAPS words"),
    "OLLIE": ("OLLIE", "heavyset man ~52, grey receding hair, grey moustache, reading glasses on a cord, "
              "short-sleeve pale blue dress shirt, brown knitted vest, gold wristwatch, kind tired eyes",
              "warm, gentle, slightly tired older man's voice"),
    "MGMT": ("MANAGEMENT", "office manager framed ONLY from the neck down - his head is ALWAYS out of frame or "
             "cut off by the top edge; beige short-sleeve dress shirt, wide brown tie, belly, clipboard, chunky "
             "steel wristwatch, \"#1 BOSS\" mug",
             "loud, clipped corporate voice, stressing CAPS words; his face is never shown"),
    "REX": ("REX", "flashy man ~35, bleached spiky hair, mirrored aviator sunglasses worn indoors, unbuttoned "
            "pastel pink silk shirt, oversized gold chain, huge gold watch, too-white teeth, holding a phone "
            "on a selfie stick",
            "over-hyped guru voice, shouting, fake laugh"),
    "MAE": ("MAE", "woman ~33, June's older sister, dark auburn hair in a messy bun, dark circles under the "
            "eyes, teal hospital scrubs, nurse badge clipped to pocket, stethoscope around neck, hospital "
            "vending-machine coffee",
            "soft, tired, raspy night-shift voice"),
    "NPC": ("NPC COWORKERS", "identical cloned office workers (same male 3D model repeated), side-parted brown "
            "hair, white shirt, grey tie, blank polite smile, cheap wristwatch",
            "flat, cheerful, robotic NPC voice with identical intonation"),
    "PIVOT": ("PIVOT", "June's chubby orange tabby cat with a white chest and a bent left ear", ""),
    "KID": ("NEW HIRE", "nervous young man ~22, curly black hair, oversized brand-new suit jacket, new blue "
            "lanyard \"EMPLOYEE\", clutching an onboarding folder",
            "nervous young voice"),
    "PA": ("PA SPEAKER", "", "distorted office loudspeaker announcement, speaker not visible"),
}

LOCS = {
    "L01": ("Open-plan office", "grey 2003 cubicle farm, buzzing fluorescent ceiling panels, beige CRT-era "
            "monitors, JUNE's cluttered cubicle next to VAN's old empty desk, rainy window wall, wall clock "
            "showing 4:59, a green running-man EXIT sign always visible somewhere",
            "cold flickering fluorescent light with a sickly green-grey cast",
            "rain streaks on windows, clone coworkers typing, copier spitting paper, second hand on the clock"),
    "L02": ("Break room", "small office kitchen, humming coffee machine, microwave with a queue, vending "
            "machine, fridge covered in passive-aggressive notes, sad plant, wall clock 4:59, EXIT sign over the door",
            "flat fluorescent light, vending machine glow",
            "steam from the coffee machine, microwave turntable spinning, flickering tube light"),
    "L03": ("Management office", "glass-walled corner office with frosted glass door, big desk, motivational "
            "poster \"TEAMWORK\", \"#1 BOSS\" mug, blinds half closed, KPI chart on the wall",
            "harsh white light with blind-slat shadows",
            "blind shadows sliding slowly, papers stirred by a desk fan"),
    "L04": ("Lobby & elevator", "corporate lobby with steel badge turnstiles, elevator doors, reception desk, "
            "company logo wall, revolving door to the street, EXIT sign above a side door",
            "cold blue-white light inside, warm daylight leaking through the revolving door",
            "revolving door turning, people tapping badges, elevator numbers changing"),
    "L05": ("Office rooftop at night", "rooftop of the office tower, air-conditioning units, wet gravel, low "
            "railing, huge neon city skyline, distant billboards, a glowing green EXIT sign on the stairwell door",
            "deep blue night with pink and teal neon rim light",
            "city lights twinkling, slow drifting clouds, steam from vents, light rain"),
    "L06": ("June's apartment", "tiny studio apartment, kitchen table with an old laptop, stack of unpaid bills, "
            "fairy lights, color-coded sticky notes on the wall, instant noodles, window with rain and a city view, "
            "cat bed",
            "warm low lamp light versus the cold blue glow of the laptop",
            "rain on the window, fairy lights gently blinking, steam from noodles"),
    "L07": ("Night bus", "nearly empty city bus at night, plastic seats, yellow handrails, tired commuters "
            "asleep against windows, ad panels above the windows",
            "sickly yellow interior light, passing streetlights sweeping through",
            "streetlights and neon sliding past the windows, the bus swaying gently"),
    "L08": ("Parking garage", "concrete parking garage, a rented lime-green supercar with a \"RENTAL\" sticker, "
            "ring light on a tripod, puddles, painted pillar numbers",
            "harsh ring light against dim orange sodium lamps",
            "ring light flicker, dripping water, a car passing in the background"),
    "L09": ("Hospital night corridor", "hospital corridor and nurses' station at 3 AM, vending machine, "
            "whiteboard with a shift roster, wheelchairs, double doors, window with night city",
            "cold teal night light with a warm desk lamp at the station",
            "monitor lights blinking, a gurney rolling past, flickering corridor light"),
    "L10": ("Van's loft", "minimal sunny loft, big window, plants, wooden desk with a closed laptop and a "
            "phone face down, record player, white ceramic mug, morning city view",
            "warm golden morning sunlight, soft and calm",
            "dust floating in sunbeams, curtains moving gently, plants swaying"),
    "L11": ("Conference room", "windowless conference room, long table, projector screen showing a pie chart, "
            "speakerphone in the middle, stale donuts, whiteboard with \"SYNERGY\"",
            "dim room lit by the cold projector beam",
            "projector dust in the light beam, ceiling fan, slides changing"),
    "L12": ("City park on a weekday morning", "green park at 10:30 AM on a Tuesday, bench, pond with ducks, "
            "joggers, food cart, office towers far in the background",
            "bright golden sunlight, soft shadows",
            "ducks swimming, leaves falling, people jogging past"),
}

SHOTS = {
    "W": ("Wide establishing shot", "static, very slow drift"),
    "OTS": ("Over-the-shoulder shot", "static"),
    "2S": ("Two-shot", "static"),
    "MS": ("Medium shot", "static"),
    "MCU": ("Medium close-up", "static"),
    "CU": ("Close-up", "slow push-in"),
    "ECU": ("Extreme close-up", "static"),
    "INS": ("Insert detail shot", "static"),
    "CAM": ("Extreme close-up, the character looks directly into the lens, breaking the fourth wall",
            "very slow push-in"),
    "POV": ("Point-of-view shot", "slight handheld sway"),
    "TOP": ("High top-down shot", "static"),
    "LOW": ("Low-angle shot", "static"),
}

TYPE_NAMES = {"A": "Typ A – cutscéna", "B": "Typ B – tutorial level", "C": "Typ C – idle (motivácia)"}
TYPE_RANGES = {"A": (14, 32), "B": (18, 48), "C": (7, 18)}

SEASONS = [
    (1, 26, "S1", "LEVEL 1 – SYSTEM OVERRIDE"),
    (27, 52, "S2", "LEVEL 2 – ASSET FORGING"),
    (53, 78, "S3", "LEVEL 3 – THE SALES ENGINE"),
    (79, 104, "S4", "LEVEL 4 – TRAFFIC GENERATION"),
    (105, 130, "S5", "LEVEL 5 – SCALING & ASCENSION"),
]

HASHTAGS = {
    "A": "#ps2 #storytime #9to5 #corporatehumor #sidehustle #digitalproducts",
    "B": "#ps2 #sidehustle #digitalproducts #onlinebusiness #learnontiktok #9to5",
    "C": "#ps2 #motivation #9to5 #quitmyjob #mindset #digitalproducts",
}

CUE_TXT = {"DROP": "🎵 beat drop", "PING": "🔔 sale ping", "OUT": "🔇 hudba vypadne ~0,4 s",
           "LOOP": "↩ tvrdý strih → loop"}


def season_of(n):
    for a, b, code, name in SEASONS:
        if a <= n <= b:
            return code, name
    raise ValueError(n)


def words(s):
    return len(re.findall(r"[A-Za-z0-9$'’]+", s))


def parse(path):
    eps, cur = [], None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith("//"):
            continue
        if line.startswith("#") and re.match(r"#\d{3} ", line):
            cur = {"num": int(line[1:4]), "title": line[5:].strip(), "scenes": [], "src": path.name}
            eps.append(cur)
        elif line.startswith(">"):
            parts = [p.strip() for p in line[1:].split("|")]
            while len(parts) < 7:
                parts.append("")
            shot, loc, chars, dlg, action, cues, dur = parts[:7]
            if dur and not dur.startswith("@"):
                raise SystemExit(f"{path.name} #{cur['num']}: bad duration field: {line}")
            speaker, text = "", ""
            if dlg and dlg != "—" and dlg != "-":
                if ":" not in dlg:
                    raise SystemExit(f"{path.name} #{cur['num']}: dialogue needs SPEAKER: {line}")
                speaker, text = dlg.split(":", 1)
                speaker, text = speaker.strip(), text.strip()
            cur["scenes"].append(dict(shot=shot, loc=loc, chars=[c for c in chars.split() if c not in ("—","-")], speaker=speaker, text=text,
                                      action=action, cues=[c.strip() for c in cues.split(",") if c.strip()],
                                      dur=float(dur[1:]) if dur else None))
        else:
            k, _, v = line.partition(":")
            cur[k.strip()] = v.strip()
    return eps


def auto_dur(sc):
    if sc["dur"]:
        return sc["dur"]
    w = words(sc["text"])
    if not w:
        return 1.6
    rate = 2.1 if sc["speaker"].startswith("VAN") else 2.8
    return round(min(3.4, max(1.4, 0.8 + w / rate)), 1)


def fmt_t(t):
    return f"{t:.1f}".replace(".", ",")


def srt_t(t):
    ms = int(round(t * 1000))
    return f"00:00:{ms // 1000:02d},{ms % 1000:03d}"


def validate(ep):
    warns = []
    for i, sc in enumerate(ep["scenes"], 1):
        if sc["loc"] not in LOCS:
            warns.append(f"scene {i}: unknown loc {sc['loc']}")
        if sc["shot"] not in SHOTS:
            warns.append(f"scene {i}: unknown shot {sc['shot']}")
        for c in sc["chars"]:
            if c not in CHARS:
                warns.append(f"scene {i}: unknown char {c}")
        sp = sc["speaker"].replace("(VO)", "").strip()
        if sp and sp not in CHARS:
            warns.append(f"scene {i}: unknown speaker {sp}")
        if sp == "VAN":
            if "!" in sc["text"]:
                warns.append(f"scene {i}: VAN uses '!'")
            if words(sc["text"]) > 6 and ep["type"] != "B":
                warns.append(f"scene {i}: VAN line > 6 words")
            if words(sc["text"]) > 9:
                warns.append(f"scene {i}: VAN line > 9 words")
        if words(sc["text"]) > 13:
            warns.append(f"scene {i}: line > 13 words")
    last = [s for s in ep["scenes"] if s["text"]]
    if last and words(last[-1]["text"]) > 4:
        warns.append(f"button > 4 words: {last[-1]['text']}")
    total = sum(auto_dur(s) for s in ep["scenes"])
    lo, hi = TYPE_RANGES[ep["type"]]
    if not lo <= total <= hi:
        warns.append(f"duration {total:.1f}s outside {lo}-{hi}")
    for k in ("emo", "premise", "caption"):
        if k not in ep:
            warns.append(f"missing {k}")
    return warns


def char_line(code):
    name, desc, _ = CHARS[code]
    return f"{name} ({desc})" if desc else name


def scene_prompt(ep, sc, dur):
    name, look, light, motion = LOCS[sc["loc"]]
    shot, cam = SHOTS[sc["shot"]]
    refs = [f"@{c}" for c in sc["chars"] if CHARS[c][1]] + [f"@{sc['loc']}"]
    out = [f"REFERENCES: {', '.join(refs)}",
           f"STYLE: {STYLE}, {light}.",
           f"LOCATION: {name} - {look}.",
           f"SHOT: {shot}."]
    if sc["chars"]:
        out.append("IN FRAME: " + "; ".join(char_line(c) for c in sc["chars"]) + ".")
    if sc["action"]:
        out.append(f"ACTION: {sc['action']}.")
    if sc["text"]:
        sp = sc["speaker"]
        vo = "(VO)" in sp
        code = sp.replace("(VO)", "").strip()
        nm, _, tone = CHARS[code]
        if vo or code == "PA":
            out.append(f"AUDIO: {nm} is heard off-screen ({tone}): \"{sc['text']}\"")
        else:
            out.append(f"DIALOGUE: {nm} says \"{sc['text']}\" ({tone}), accurate lip-sync.")
    else:
        out.append("DIALOGUE: none.")
    if "MGMT" in sc["chars"]:
        out.append("RULE: MANAGEMENT's head must never be visible - crop at the neck.")
    out.append(f"BACKGROUND MOTION: {motion}.")
    out.append(f"CAMERA: {cam}. DURATION: ~{dur:.1f} s.")
    out.append("Keep every character exactly on-model with the reference sheets. No subtitles, no on-screen "
               "text, no watermarks.")
    return "\n".join(out)


def cue_text(cues):
    out = []
    for c in cues:
        if c in CUE_TXT:
            out.append(CUE_TXT[c])
        elif c.startswith("HUD:"):
            out.append(f"🎮 HUD: `{c[4:].strip()}`")
        elif c.startswith("SFX:"):
            out.append(f"🔊 {c[4:].strip()}")
        elif c.startswith("CARD:"):
            out.append(f"🃏 karta: `{c[5:].strip()}`")
        else:
            out.append(c)
    return "<br>".join(out)


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def ep_path(ep):
    code, _ = season_of(ep["num"])
    return f"{code}/{ep['num']:03d}-{slug(ep['title'])}.md"


def render(ep, prev, nxt):
    code, sname = season_of(ep["num"])
    durs = [auto_dur(s) for s in ep["scenes"]]
    total = sum(durs)
    allchars = []
    for s in ep["scenes"]:
        for c in s["chars"]:
            if c not in allchars and CHARS[c][1]:
                allchars.append(c)
    locs = []
    for s in ep["scenes"]:
        if s["loc"] not in locs:
            locs.append(s["loc"])
    L = [f"# #{ep['num']:03d} · {ep['title']}", "",
         f"`{code} · {sname}` · `{TYPE_NAMES[ep['type']]}` · `~{round(total)} s` · `{len(ep['scenes'])} záberov`", ""]
    nav = []
    if prev:
        nav.append(f"[← #{prev['num']:03d}](../{ep_path(prev)})")
    nav.append("[📋 zoznam](../README.md)")
    if nxt:
        nav.append(f"[#{nxt['num']:03d} →](../{ep_path(nxt)})")
    L += [" · ".join(nav), ""]
    L.append(f"> **Premisa:** {ep['premise']}  ")
    L.append(f"> **Emócia diváka:** {ep['emo']}  ")
    if ep.get("edu"):
        L.append(f"> **Čo sa divák naučí:** {ep['edu']}  ")
    if ep.get("clue"):
        L.append(f"> **Indícia / easter egg:** {ep['clue']}  ")
    if ep.get("loop"):
        L.append(f"> **Loop:** {ep['loop']}  ")
    L.append("")
    L.append("**Reference images na nahratie:** " + ", ".join(f"`{c}`" for c in allchars) +
             " · " + ", ".join(f"`{l}` {LOCS[l][0]}" for l in locs))
    L += ["", "## Storyboard", "", "| # | čas | záber | lok. | kto | titulok | strih / zvuk |", "|---|---|---|---|---|---|---|"]
    t = 0.0
    times = []
    for i, (s, d) in enumerate(zip(ep["scenes"], durs), 1):
        times.append((t, t + d))
        who = s["speaker"].replace("(VO)", " (VO)") if s["speaker"] else "—"
        txt = f"„{s['text']}“" if s["text"] else "*(bez repliky)*"
        L.append(f"| {i} | {fmt_t(t)}–{fmt_t(t + d)} | {s['shot']} | {s['loc']} | {who} | {txt} | {cue_text(s['cues'])} |")
        t += d
    if ep.get("cta") == "yes":
        L.append(f"| ⏹ | {fmt_t(t)}–{fmt_t(t + 1.5)} | karta | – | – | `SAVE GAME? → [ EXIT ] link in bio` | end card |")
    L += ["", "## Prompty pre jednotlivé zábery", "",
          "> Ku každému promptu nahraj reference images uvedené v riadku `REFERENCES`.", ""]
    for i, (s, d, (a, b)) in enumerate(zip(ep["scenes"], durs, times), 1):
        L.append(f"### Záber {i} · {fmt_t(a)}–{fmt_t(b)} s · {SHOTS[s['shot']][0].split(',')[0]} · {s['loc']}")
        L += ["", "```text", scene_prompt(ep, s, d), "```", ""]
    L += ["## Titulky (SRT – import do CapCut)", "", "```srt"]
    n = 1
    for s, (a, b) in zip(ep["scenes"], times):
        if s["text"]:
            L += [str(n), f"{srt_t(a)} --> {srt_t(b)}", s["text"], ""]
            n += 1
    if L[-1] == "":
        L.pop()
    L += ["```", "", "## Popis + hashtagy", "", "```text",
          f"{ep['caption']}", "", HASHTAGS[ep["type"]] + " #vanexit", "```", ""]
    return "\n".join(L)


def main():
    eps = []
    for p in sorted((ROOT / "data").glob("*.txt")):
        eps += parse(p)
    eps.sort(key=lambda e: e["num"])
    nums = [e["num"] for e in eps]
    dup = {n for n in nums if nums.count(n) > 1}
    if dup:
        raise SystemExit(f"duplicate episode numbers: {sorted(dup)}")
    total_warn = 0
    out = ROOT / "scripts"
    for i, ep in enumerate(eps):
        w = validate(ep)
        for x in w:
            print(f"#{ep['num']:03d} {ep['title']}: {x}")
        total_warn += len(w)
        prev = eps[i - 1] if i else None
        nxt = eps[i + 1] if i + 1 < len(eps) else None
        p = out / ep_path(ep)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(render(ep, prev, nxt), encoding="utf-8")
    # index
    I = ["# VAN – 130 scenárov", "",
         "Každý scenár má vlastný súbor: storyboard, prompt pre každý záber, titulky (SRT) a popis s hashtagmi.",
         "Reference images: [`../01-character-sheets.md`](../01-character-sheets.md) a "
         "[`../02-location-sheets.md`](../02-location-sheets.md). Postup: [`../README.md`](../README.md).", "",
         "Typy: **A** = cutscéna (virál), **B** = tutorial level (vzdelávanie), **C** = idle (motivácia).", ""]
    counts = {"A": 0, "B": 0, "C": 0}
    for a, b, code, name in SEASONS:
        se = [e for e in eps if a <= e["num"] <= b]
        if not se:
            continue
        I += [f"## {code} · {name}", "", "| # | názov | typ | dĺžka | hook (1. replika) | emócia |", "|---|---|---|---|---|---|"]
        for e in se:
            counts[e["type"]] += 1
            first = next((s["text"] for s in e["scenes"] if s["text"]), "")
            tot = round(sum(auto_dur(s) for s in e["scenes"]))
            I.append(f"| {e['num']:03d} | [{e['title']}]({ep_path(e)}) | {e['type']} | {tot} s | „{first}“ | {e['emo']} |")
        I.append("")
    I.insert(6, f"Spolu **{len(eps)}** videí – A: {counts['A']}, B: {counts['B']}, C: {counts['C']}.\n")
    (out / "README.md").write_text("\n".join(I), encoding="utf-8")
    print(f"rendered {len(eps)} episodes, {total_warn} warnings")


if __name__ == "__main__":
    main()
