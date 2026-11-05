# VAN × Vantage Strategic Systems: produkčný balík

Všetko na výrobu seriálu **„[ EXIT ]“** (PS2-style cutscény s maskotom VAN) na jednom mieste.

| Súbor | Čo v ňom je |
|---|---|
| [`01-character-sheets.md`](01-character-sheets.md) | 9 postáv: profil, zamknutý vzhľad, hlas, oblúk + prompty na **turnaround** a **expression sheet** |
| [`02-location-sheets.md`](02-location-sheets.md) | 12 lokácií (L01 – L12) + prompty na prázdne „plates“ |
| [`scripts/README.md`](scripts/README.md) | **zoznam 130 videí** (sezóny, hooky, emócie) s odkazmi |
| `scripts/S1 … S5/*.md` | každé video: storyboard, **prompt pre každý záber**, titulky SRT, HUD SRT, popis + hashtagy |
| [`03-marketing-strategy.md`](03-marketing-strategy.md) | TikTok (založenie účtu, publikovanie, hidden gems) + Instagram (carousely × Reels) |
| `data/*.txt`, `tools/render.py` | zdrojové dáta scenárov a generátor. Úpravy rob v `data/`, potom spusti `python3 tools/render.py` |

Pôvodný návrh postavy: [`../analysis/vantage-character-van.md`](../analysis/vantage-character-van.md).

---

## Postup krok za krokom (bez práce navyše)

### 1. Raz na začiatku: reference images
1. Otvor `01-character-sheets.md` a každý prompt **A) Turnaround** a **B) Expression sheet** vlož
   do generátora obrázkov (Midjourney / Nano Banana / GPT-image / Flux).
2. Najlepší výsledok ulož presne pod kódom postavy: `VAN.png`, `VAN-face.png`, `JUNE.png`, `JUNE-face.png`,
   `OLLIE.png`, `MGMT.png`, `REX.png`, `MAE.png`, `NPC.png`, `PIVOT.png`, `KID.png`.
3. To isté s lokáciami z `02-location-sheets.md`: `L01.png` … `L12.png`.
4. Skontroluj texty (**[ EXIT ]**, **VISITOR**, **EMPLOYEE**). Ak sú skomolené, oprav ich v editore obrázkov
   **teraz**, raz a navždy.

> Priečinok s týmito ~23 obrázkami je tvoja „knižnica“. Používaš ich vo všetkých 130 videách.

### 2. Pre každé video
1. Otvor súbor videa (napr. `scripts/S1/001-visitor.md`).
2. Hore je riadok **„Reference images na nahratie“**: zoznam postáv a lokácií pre celé video.
3. Pre každý **Záber 1, 2, 3…**:
   - pozri prvý riadok promptu `REFERENCES: @VAN, @JUNE, @L01` a nahraj presne tieto obrázky
     (`@VAN` = `VAN.png` alebo `VAN-face.png` pri detailoch CU / ECU / CAM),
   - skopíruj **celý blok promptu** (tlačidlo copy v rohu bloku) a vlož ho do video generátora
     (Kling / Veo / Runway / Hailuo / Seedance),
   - nastav dĺžku podľa `DURATION` (zaokrúhli hore na 3 – 5 s, v strihu orežeš) a pomer **4:3**
     (ak generátor 4:3 nemá, generuj 16:9 a orež na 4:3).
4. V strihu (CapCut) poskladaj zábery v poradí, importuj **Titulky SRT** (žlté písmo, čierny obrys)
   a pri type B aj **HUD SRT** (druhá stopa, hore vľavo).
5. Zvuk podľa stĺpca **strih / zvuk** v storyboarde: 🎵 beat drop, 🔔 sale ping, 🔇 výpadok hudby.
6. Popis a hashtagy skopíruj z konca súboru.

### Ak generátor berie menej reference images
Priorita: **1. hovoriaca postava → 2. ďalšie postavy → 3. lokácia.** Lokáciu prompt aj tak podrobne
opisuje, takže pri vynechaní obrázka sa scéna nerozpadne.

### Hlasy a dialóg
Každý prompt obsahuje repliku aj tón hlasu (`DIALOGUE: VAN says "..." (calm, low…)`). Generátory so
zvukom (Veo 3, Kling s audiom) ich nahovoria rovno. Inak repliky nahovor v ElevenLabs. Pre každú postavu
si vyber **jeden hlas a drž ho** (tón je v character sheete) a v CapCut použi lip-sync.

### Zvukové prvky na celú sériu (pripraviť raz)
- **Sale ping:** vlastný krátky zvuk notifikácie (ElevenLabs SFX: *„short bright two-note digital cash
  notification chime, retro game style“*). Nepoužívaj zvuky Shopify / Apple.
- **Hudba:** lo-fi / PS2 menu-chill, bez autorských práv (knižnica TikTok Commercial Music Library alebo
  vlastná z AI generátora s komerčnou licenciou).
- **End card** (videá s `SAVE GAME?`): 1,5 s čierna obrazovka, biely pixel font
  `SAVE GAME? → [ EXIT ] link in bio`. Urob raz ako PNG a vkladaj.

---

## Príbeh v skratke (story bible)

**Svet:** PS2 hra „[ EXIT ]“. Kancelária z roku 2003, hodiny stoja na 4:59, zelená ceduľa EXIT je v každom
zábere. NPC kolegovia sú klony („Dave“). MANAGEMENT nemá tvár.

| Sezóna | Level (modul e-booku) | Oblúk June | Emocionálne vrcholy |
|---|---|---|---|
| S1 · 001–026 | System Override | uväznená v 9-5, nájom, sestra Mae na nočných, „Teach me.“ | #005 zmeškaný hovor, **#022 Ollie prepustený za 4 minúty**, #025 strecha |
| S2 · 027–052 | Asset Forging | mikro-niche (nové nočné sestry), produkt Night Shift OS, impostor syndróm | #030 „Nobody asks“, #039 Vanova prázdna stolička, #050 Mae spala 7 hodín |
| S3 · 053–078 | The Sales Engine | 0 predajov, **prvý ping (#065)**, refund, nájom zaplatený | #055 deň 3: nula, #066 sestra z Ohia, #074 Van a otec |
| S4 · 079–104 | Traffic Generation | 12 zhliadnutí → virál 1,2 M, hejt, Rex kopíruje, Ollie začína | #079 šéfova žena, #090 Mae ju bráni, #095 „It's breakfast“ |
| S5 · 105–130 | Scaling & Ascension | reklamy, rebrík, povýšenie odmietnuté, výpoveď, VISITOR | **#110 Ollieho prvý ping**, #126 cez dvere EXIT (hodiny 5:00), #129 tajomstvo „O.“, #130 loop |

**Dlhé tajomstvá (komentáre a binge):** kto napísal „O.“ na Vanovu kartičku (#012 → #129), prečo sa Van
vracia (#022 → #129), hodiny na 4:59 (#004 → #126), Vanova prázdna stolička (#039 → #074).

**Pravidlá, ktoré platia v každom diele:** hook v 1. sekunde, Van bez výkričníkov a najviac 6 slov (v type B
najviac 9), pravidlo troch, pointa najviac 4 slová, loop. Generátor `tools/render.py` to automaticky kontroluje.

**Disclaimer k číslam:** v dieloch, kde sa spomína príjem (#072, #073, #104), je v popise „results vary“.
Konkrétne sumy sú ilustračné (fikcia). VAN nikdy nesľubuje príjem.
