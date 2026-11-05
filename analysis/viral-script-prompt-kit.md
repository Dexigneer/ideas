# Viral Script Prompt Kit („PS2 cutscéna“ formát)

Praktická nadstavba nad rozborom [`3dmarlon-ps2-virality-breakdown.md`](./3dmarlon-ps2-virality-breakdown.md).
Prompty sú po anglicky, lebo LLM aj video/obrazové modely s nimi fungujú najlepšie (a videá sú
v angličtine). Ak chceš slovenské/české videá, stačí v kroku 1 zmeniť `LANGUAGE`.

Postup: **1) premisa → 2) scenár (master prompt) → 3) kritika a prepis → 4) vizuálne prompty pre
každý záber → 5) strih podľa špecifikácie.**

---

## 1. Master prompt pre scenár (vlož do ChatGPT / Claude ako system alebo prvú správu)

```text
You are a short-form video screenwriter who writes 15–30 second "PS2-style game cutscene" sketches
that go viral on TikTok/Reels/Shorts. You follow the FORMULA below exactly.

FORMULA
- Format: a cutscene from a fictional early-2000s 3D video game. 4:3 frame. Yellow game-style
  subtitles. One line of dialogue = one shot (1.5–2.7 s each). 8–16 lines total. 15–30 s total.
- HERO: always calm, low-reactivity, slightly smug, always one step ahead. Speaks in 2–6 words.
  NEVER uses an exclamation mark. Never explains himself. Never asks for permission. Usually doing
  something casual (eating, drinking, driving) while chaos happens around him.
- REACTORS: loud, expressive, emotional. Use "?!" and put ONE or TWO key words in CAPS per line.
  They ask the questions the viewer is thinking.
- Optional ICON: a recognizable archetype (NOT a copyrighted character by name) whose famous
  "power" or "attitude" fails against the hero.
- Someone must say the HERO's name at least once.

BEAT STRUCTURE (timestamps are targets)
1. HOOK (0–1 s): start mid-conflict. First line is a reaction to something that already happened.
   Must contain "you", a concrete slightly absurd detail, and an accusation / command / riddle.
   First shot is wide or over-the-shoulder with 3+ characters and a visible conflict gesture.
2. STAKES (1–5 s): one line that makes clear what happens if it goes wrong.
3. ESCALATION (5 s – 70 %): 2–4 rounds of pressure, ideally a rule-of-three pattern.
   Hero answers each with a short deadpan line. Music drop on the first escalation.
4. TWIST (70–85 %): hero reveals information he had all along or a detail he noticed that the
   viewer COULD have noticed (plant this clue visually earlier).
5. BUTTON (last 1–1.5 s): ≤4 words. Close-up, ideally looking into the camera. Hard cut, no outro.
6. LOOP: the last shot or last line must connect back to the first (visual rhyme, "again",
   time loop, or the next conflict starting).

ALSO INCLUDE
- One quotable line (could be printed on a T-shirt).
- One visual easter egg / clue that rewards a rewatch.
- An ending that leaves room for comments (unresolved consequence, "wait…", or a reveal people
  will explain to each other).
- If a BRAND/SLOGAN is given: put it visually on the hero's clothing in every shot. Say it out
  loud at most once, only as the button, and only if it lands as a joke.

OUTPUT FORMAT
A) Title (internal) + one-sentence premise.
B) Shot table with columns:
   # | start–end (s) | shot type (wide/OTS/2-shot/MCU/CU/ECU) | who | line (subtitle text exactly,
   with CAPS emphasis) | facial expression + action | background motion | music/SFX cue
C) The visual clue and where it appears.
D) Why the hook stops the scroll (1 sentence) and why people rewatch (1 sentence).
E) 3 alternative button lines.

Write in LANGUAGE: {LANGUAGE}.
```

### Vstup (vyplň a pošli hneď za master promptom)

```text
HERO: {meno, vzhľad (vždy rovnaký), oblečenie s logom/sloganom}
RECURRING CAST: {napr. „Sunday – kučeravá, klamárka, vždy sa červená“; „biela mikina – vždy natáča“}
BRAND / SLOGAN (optional): {„Be the …“}
SETTING: {diner / auto v noci / akvárium-reštaurácia / nočný trh / kancelária…}
TROPE / PREMISE: {pozri sekciu 2}
ICON ARCHETYPE (optional): {napr. „anime villain with a cursed notebook“}
TARGET LENGTH: {15 / 20 / 25 / 30 s}
LANGUAGE: {English}
```

---

## 2. Generátor premís (vzorce, nie kópie)

Každá premisa = **známy trope + malicherná sociálna situácia + hrdina vie niečo navyše**.

| # | Vzorec | Príklad premisy |
|---|---|---|
| 1 | Nadprirodzená moc zlyhá na hrdinovi | prekliatá kniha / hypnóza / čítanie myšlienok nefunguje na hrdinu |
| 2 | Hrdina je v časovej slučke dlhšie než ostatní | „Y'all? An hour. Me? Eight months.“ |
| 3 | Verejný trapas iného „alfa“ typu, hrdina má kľúčovú informáciu | zamietnutá karta, odtiahnuté auto, zrušená rezervácia |
| 4 | Ultimátum / hádanka „ktorá z nás?“ | hrdina vyrieši logickou pascou |
| 5 | Obvinenie, ktoré sa otočí na žalobcu | „You said HE kissed you!“ |
| 6 | Identické postavy (dvojčatá, klony, rovnaké kostýmy) | „Which one of us is real?“ |
| 7 | Výsluch / policajná miestnosť, kde hrdina vypočúva policajta | role reversal |
| 8 | Hrdina je skrytý vlastník / šéf / kontakt | „I'm your emergency contact.“ / „I own the restaurant.“ |
| 9 | Pozorovanie detailu (Sherlock mini) | rúž v zrkadle, mačka naopak, červené líca |
| 10 | Absurdná eskalácia v troch krokoch | karta 1 declined → karta 2 declined → „this one's a gym membership“ |
| 11 | Postava robí to, čo by robil divák | „Nah, I gotta film this.“ |
| 12 | Falošné riešenie a potom „wrong X“ | „He caught it!“ → „Wrong wok.“ |
| 13 | Zloduch sa zosype, hrdina pokračuje v jedle | kontrast energie |
| 14 | Pokračovanie minulého dielu z iného miesta | diner → auto (tá istá lož) |
| 15 | Hrdina odmietne pravidlá hry | „I don't have to pick.“ |

**Prompt na premisy:**
```text
Using the FORMULA above, generate 15 premises for HERO {…} in SETTINGS {…}.
For each: hook line (≤10 words), stakes line, twist (what the hero knows), button (≤4 words),
the visual clue, and a loop idea. Rank them by scroll-stopping power and rewatch potential.
Avoid copyrighted character names; use archetypes.
```

---

## 3. Prompt na kritiku a prepis (vždy spusti po prvej verzii)

```text
Score this script 1–10 on each criterion and rewrite it to reach ≥9 everywhere:
1. Hook: does line 1 start mid-conflict, include "you", a concrete absurd detail, and is it
   understandable with sound OFF?
2. Stakes clear by 5 s?
3. Pace: every line ≤ ~2.7 s spoken; no line over 12 words; hero lines ≤ 6 words, no "!"?
4. Contrast: reactors loud (CAPS / ?!) vs hero deadpan?
5. Rule of three present?
6. Twist: surprising yet fair (clue planted visually earlier)?
7. Button: ≤4 words, lands in the last 1.5 s, no outro?
8. Loop: does the ending connect to the start?
9. Rewatch trigger (easter egg / clue)?
10. Comment trigger (unresolved / debatable / lore)?
11. Quotable line?
12. Brand: visible on hero every shot, not preachy?
Then output the improved shot table only.
```

---

## 4. Vizuálne prompty

### 4a. Character sheet (urob raz a používaj ako referenciu, aby postava bola vždy rovnaká)

```text
Character reference sheet, early-2000s PlayStation 2 game cutscene style, slightly low-poly 3D model,
smooth plastic-like skin shading, stylized hair with visible polygon edges, expressive large eyes,
soft cinematic lighting. Character: {HERO description: hair, skin, face, outfit with "{SLOGAN}"
printed clearly on the chest, accessories}. Front view, 3/4 view, side view, close-up face with
neutral smug half-smile. Neutral gray background, 4:3.
```

### 4b. Keyframe pre každý záber (obrázok)

```text
PS2-era video game cutscene still, 4:3 aspect ratio, 3D rendered, slightly low-poly characters,
warm saturated cinematic lighting, {SETTING with moving background elements: fire / aquarium
with sharks / neon city / steam}, {SHOT TYPE: wide / over-the-shoulder / medium close-up / extreme
close-up}, {WHO is in frame and their positions}, {EXPRESSION + GESTURE: arms crossed, pointing,
hands over mouth, blushing cheeks, deadpan half-smile}, {HERO consistent with reference},
"{SLOGAN}" legible on hoodie. No text overlays, no subtitles.
```

### 4c. Pohyb (image-to-video, 2 – 3 s klip)

```text
{CHARACTER} says the line "{LINE}" with {EMOTION}, subtle lip-sync, small natural head motion,
{one micro-action: sips drink through straw / turns head slowly / points with pen / covers mouth},
background keeps moving ({fire flickers / sharks swim / neon lights pass}), camera {static |
slow push-in | slight handheld}. Duration {2–3} s. Keep the PS2 cutscene look, no style drift.
```

### 4d. Hlasy (AI TTS)

- **Hrdina:** nízky, pomalý, mierne pobavený hlas, žiadna snaha, krátke pauzy pred poslednou slabikou.
- **Reaktori:** vyššie, rýchlo, emotívne, prehnaná intonácia na CAPS slovách.
- **Ikona/zloduch:** teatrálny, smiech „ha ha ha…“, zrútenie do kriku.

---

## 5. Špecifikácia strihu (CapCut / Premiere)

| Prvok | Nastavenie |
|---|---|
| Rozlíšenie | 4:3 (napr. 1440×1080 alebo 768×576) |
| Titulky | žltá (#FFE94A ± ), čierny obrys 2 – 3 px, bezpätkové bold, dole na stred, 1 – 2 riadky, bez animácie |
| Dôraz | CAPS na 1 – 2 slovách v replike reaktorov |
| Strih | na každú repliku; záber 1,5 – 2,7 s; reakčné zábery môžu prísť počas repliky |
| Prvá snímka | už s titulkom a s hovoriacou postavou (žiadny čierny úvod) |
| Hudba | súvislá vrstva od 0 s; jemnejší nástup, **drop na prvej eskalácii** (2 – 6 s); **0,3 – 0,5 s výpadok** tesne pred pointou |
| Hlasitosť | cieľ ~ −10 až −12 LUFS, hlasy nad hudbou |
| Koniec | ≤ 1,5 s po pointe, tvrdý strih, žiadna end-card (okrem stratégie s URL ako Luca Maxim) |

---

## 6. Ukážkový scenár (originálny, podľa formulky)

**Premisa:** Nočná práčovňa. Tri kamarátky obvinia hrdinu, že im ukradol mikinu. Hrdina vie,
že zlodejka je jedna z nich, pretože mikina je ešte teplá zo sušičky, ktorú má na sebe… ona.

| # | Čas | Záber | Kto | Titulok | Akcia / výraz | Pozadie / zvuk |
|---|---|---|---|---|---|---|
| 1 | 0,0 – 1,8 | wide | Mia | „You took my hoodie. From the DRYER.“ | ukazuje prstom, ostatné majú prekrížené ruky | bubny sušičiek sa točia, hudba potichu |
| 2 | 1,8 – 3,4 | MCU | HERO | „Which dryer?“ | skladá ponožky, nepozrie sa | |
| 3 | 3,4 – 5,6 | 2-shot | Zoe | „Give it back or we're telling EVERYONE.“ | | **beat drop** |
| 4 | 5,6 – 7,2 | CU | HERO | „Number seven.“ | dvíha obočie | |
| 5 | 7,2 – 9,2 | wide | Mia | „There IS no number seven?!“ | otáča sa: sušičky 1, 2, 3, 4, 5, 6 | (clue: v pozadí stojí Luna pri stroji s ručne napísaným „7“) |
| 6 | 9,2 – 10,8 | MCU | HERO | „Ask Luna.“ | srká kávu z automatu | |
| 7 | 10,8 – 12,6 | CU | Luna | „Why would I— it's not even WARM!“ | prsty na rukáve (mikina pod bundou) | |
| 8 | 12,6 – 14,2 | MCU | HERO | „Never said warm.“ | malý úsmev | |
| 9 | 14,2 – 16,0 | wide | Mia + Zoe | „LUNA?!“ | Luna si zapne bundu až po bradu | hudba vypadne na 0,4 s |
| 10 | 16,0 – 17,2 | ECU, do kamery | HERO | „Number seven.“ | žmurkne | hard cut → loop na „You took my hoodie“ |

*Easter egg:* „7“ napísané fixkou na sušičke za Lunou v zábere 1 aj 5. *Komentáre:* „kto si všimol
sedmičku?“ *Citovateľná veta:* „Never said warm.“

---

## 7. Rýchly checklist pred publikovaním

- [ ] Prvá veta sa dá pochopiť bez zvuku do 1 s?
- [ ] Hrdina nemá ani jeden výkričník?
- [ ] Je tam pravidlo troch?
- [ ] Je zvrat férový (indícia bola v obraze)?
- [ ] Pointa ≤ 4 slová a končí ≤ 1,5 s pred koncom?
- [ ] Koniec sa zacyklí na začiatok?
- [ ] Logo/slogan je čitateľné (žiadny AI skomolený text)?
- [ ] Žiadne mená chránených postáv ani podoby reálnych celebrít?
