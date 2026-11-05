# Mona – vianočná kampaň: scenáre a prompty

Všetko na výrobu videí s hrdinkou **Monou** pre 3 testované slogany.

| Súbor | Čo v ňom je |
|---|---|
| [`00-sheets-characters-locations.md`](./00-sheets-characters-locations.md) | Prompty na **reference images**: postavy (`@MONA`, `@TASH`…), 20 lokácií (`LOC-01`…), hlasy |
| [`A-test-you-met-me.md`](./A-test-you-met-me.md) | 10 kompletných testovacích scenárov – *You met me at a very Christmas time of the year* |
| [`B-test-santa-works-for-me.md`](./B-test-santa-works-for-me.md) | 10 kompletných testovacích scenárov – *Santa works for me* |
| [`C-test-oh-my-reindeer.md`](./C-test-oh-my-reindeer.md) | 10 kompletných testovacích scenárov – *Oh my reindeer!* |
| [`A-bank-90.md`](./A-bank-90.md) | 90 ďalších scenárov – slogan A |
| [`B-bank-90.md`](./B-bank-90.md) | 90 ďalších scenárov – slogan B |
| [`C-bank-90.md`](./C-bank-90.md) | 90 ďalších scenárov – slogan C |
| [`../../analysis/mona-marketing-tiktok-strategy.md`](../../analysis/mona-marketing-tiktok-strategy.md) | Marketingová + TikTok stratégia, merch, plán testu |

---

## 1. Výrobný postup (každé video)

1. **Reference images** (raz): vygeneruj hárky z `00-sheets…` – Mona (variant mikiny podľa sloganu), vedľajšie postavy, lokácie.
2. **Pre každý záber** (S1, S2…): prilož reference uvedené pri zábere (`Refs:`) + skopíruj prompt z bloku.
   - Tagy `@MONA`, `@TASH`, `LOC-01` v prompte nahraď spôsobom, akým tvoj nástroj odkazuje na obrázky
     (napr. Kling *Elements*, Runway *@reference*, Veo *ingredients*, Higgsfield *Soul ID*). Ak nástroj
     tagy nepozná, nechaj ich – opis postavy pomôže aj tak.
   - Ak nástroj robí najprv obrázok a až potom video: použi prompt najprv na keyframe (image), potom ten istý
     prompt na image-to-video.
3. **Hlasy**: repliky zo stĺpca *Replika* do TTS (presety v `00-sheets…`, sekcia C). Ak video model vie
   generovať reč (lip-sync), replika je už v prompte v úvodzovkách.
4. **Strih** podľa šablóny nižšie.
5. **Publikovanie**: popis + hashtagy + pripnutý komentár sú pri každom scenári.

## 2. Šablóna strihu (CapCut) – „herné okno“ 9:16

```
┌──────────────────────┐  1080 × 1920
│   HOOK TEXT (biely,  │  0 – 555 px   ← horný pás: hook text (veľký, 2 riadky max)
│   čierny obrys)      │
├──────────────────────┤
│                      │
│   HERNÉ OKNO 4:3     │  555 – 1365 px (1080 × 810)
│   + žlté titulky     │  ← titulky VNÚTRI okna, dole
│                      │
├──────────────────────┤
│  (malé) MONA · ep.07 │  1365 – 1920 px ← spodok zakrýva UI TikToku, nič dôležité
└──────────────────────┘
```

- **Hook text** v hornom páse = to, čo je v scenári ako *Hook text*. Pozadie pásov čierne (alebo rozmazaný záber).
- **Titulky**: žltá `#FFE94A`, čierny obrys 3 px, bold bezpätkové, dole v hernom okne, CAPS iba na zdôraznenie.
- **Záber = replika**, 1,5 – 2,7 s. Prvá snímka už s replikou, žiadne intro.
- **Hudba** od 0 s, **drop** pri prvej eskalácii, **0,3 – 0,5 s ticho** pred pointou, tvrdý strih na konci.
- **Text na mikine** vždy prekry čistým textom (AI ho skomolí).

### Herné HUD prvky (overlaye v CapCute)

Používajú sa vo formátoch `F2`, `F6`. Urob si ich raz ako šablóny:

| Prvok | Vzhľad |
|---|---|
| **Dialogue wheel** | tmavý polopriehľadný panel vpravo dole, 3 – 4 možnosti biele, vybraná žltá s ▶, zvuk „menu click“ |
| **Skrytá možnosť** | 4. riadok bliká zlatou, objaví sa so zvukom „sparkle“ |
| **Quest / Side quest** | vľavo hore, malý box: „SIDE QUEST: …“ |
| **Achievement** | vyjde zdola: ikona trofeje + „ACHIEVEMENT UNLOCKED – …“ |
| **Loading tip** | čierna obrazovka, dole „TIP: …“ + točiaci sa snehový vločka-loader |
| **Lower third (F5)** | biely pruh: meno postavy + vtipný popis („TASH – best friend, 12 years, tired“) |
| **Chat / dating UI (F8)** | bubliny správ cez herné okno |

## 3. Formáty (aby videá neboli na jedno kopyto)

| Kód | Formát | Prečo funguje |
|---|---|---|
| `F1` | Klasická cutscéna: dráma → zvrat → pointa | osvedčený vzorec 3dMarlon |
| `F2` | Dialogue wheel: herné možnosti, Mona vyberie skrytú | herný vtip, ktorý konkurencia nerobí; ľudia komentujú „ktorú by si vybrala ty“ |
| `F3` | POV: kamera = divák | divák je priamo v scéne s Monou |
| `F4` | Pravidlo troch: 3 situácie, rovnaká reakcia | rytmus, ľahko sa sleduje |
| `F5` | Mockumentary: rozhovory do kamery + zábery | iný rytmus, citovateľné vety |
| `F6` | Quest / achievement HUD | „život ako hra“, ženy zdieľajú („side quest: survive Aunt Bev“) |
| `F7` | Seriál: Part 1 → Part 2 | follow kvôli pokračovaniu |
| `F8` | Tichý / text: chat, dating app, len výrazy | funguje bez zvuku a v každej krajine |
| `F9` | Časová os: dátumy / odpočítavanie | „too early Christmas“ téma, kontrast novembra a decembra |

## 4. Pravidlá Mony (kontrola pri každom videu)

- Mona: 2 – 6 slov, **bez výkričníka**, nikdy nekričí ani sa nevysvetľuje. Vždy s ľadovou kávou.
- Reaktori: CAPS na 1 – 2 slovách, „?!“, kladú otázky za diváka.
- Niekto ju osloví menom. „The Sip“ + pohľad do kamery na konci.
- Férový zvrat: indícia je v obraze skôr (pri každom scenári je uvedená ako *Easter egg*).
- Žiadna žena nie je terčom ponižujúceho vtipu. Žiadne chránené postavy, piesne ani logá.
