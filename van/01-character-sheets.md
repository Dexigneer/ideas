# 01 · Character sheets: postavy sveta „[ EXIT ]“

Návod: každý character sheet vygeneruj **raz** (Midjourney / Nano Banana / Flux / GPT-image / Ideogram).
Vyber najlepšiu verziu a ulož ju pod kódom postavy (`VAN.png`, `JUNE.png` …). Tie isté súbory potom
nahrávaš ako reference images do video generátora (Kling / Veo / Runway / Hailuo). Prompty jednotlivých
záberov na ne odkazujú cez `@VAN`, `@JUNE` atď.

**Odporúčanie:** ku každej postave vygeneruj 2 obrázky: **A) turnaround** (celá postava zo 4 strán)
a **B) expression sheet** (6 výrazov tváre). Do video generátora nahraj ten, ktorý sa hodí k záberu:
pri detailoch tváre expression sheet, pri širokých záberoch turnaround.

---

## 0. Spoločný štýlový blok (pridaj na začiatok každého promptu, ak ho generátor nemá v pamäti)

```text
Early-2000s PlayStation 2 game character art, in-engine 3D model render, slightly low-poly geometry,
smooth plastic-like skin shading, stylized hair with visible polygon edges, expressive Sims-like face,
soft cinematic game lighting, clean readable silhouette, 4:3 aspect ratio.
```

**Negatívny prompt (ak ho generátor podporuje):**
```text
photorealistic, real person, celebrity likeness, anime, 2D cartoon, painterly, blurry, extra fingers,
garbled text, misspelled text, watermark, logo, modern UE5 realism, hyper-detailed pores
```

---

## 1. VAN: hrdina, „ten, čo už odišiel“

| | |
|---|---|
| **Kód** | `@VAN` |
| **Rola** | hlavný hrdina, hráčska postava hry „[ EXIT ]“. Do kancelárie chodí ako návšteva. |
| **Vek / typ** | ~30, priemerná postava, nie model ani kulturista. „Normálny chalan, ktorý to vyriešil.“ |
| **Tvár** | tmavé hnedé oči, polo-privreté pokojné viečka, rovné husté obočie, jemné strnisko, ľahký asymetrický polo-úsmev (ľavý kútik). |
| **Vlasy** | tmavohnedé, krátke, mierne rozstrapatené vpredu, žiadny gél. |
| **Oblečenie (ZAMKNUTÉ)** | čierna mikina na zips (zips do polovice), na ľavej hrudi malý biely monospace nápis **[ EXIT ]**, pod ňou sivé tričko, tmavé rovné rifle, čisté biele tenisky. |
| **Podpisové prvky** | 1) šnúrka na krk so **zelenou** linkou a bielou kartičkou **VISITOR**, 2) **žiadne hodinky** (ľavé zápästie holé), 3) biely keramický hrnček, 4) telefón vždy obrazovkou dole. |
| **Farby** | čierna `#111111`, sivá `#8A8A8A`, exit zelená `#1FD67A` (iba šnúrka a nápis). |
| **Reč tela** | sedí opretý, nohy prekrížené, pohyby pomalé, pozerá sa mimo toho, kto naňho kričí, a pomaly žmurká. |
| **Hlas** | nízky, pomalý, suchý humor, krátka pauza pred posledným slovom. **Nikdy nekričí.** |
| **Pravidlá reči** | 1 – 6 slov, bodka, nikdy výkričník, nevysvetľuje sa. V tutoriáloch (typ B) najviac 9 slov na repliku. |
| **Tajomstvo (lore)** | Odišiel v marci. Do kancelárie sa vracia z dvoch dôvodov: dostať von June a splatiť dlh Olliemu (pozri #129). Na rodinnej fotke z otcových 60. narodenín chýba, sedel vtedy na kvartálnom reporte (prázdna stolička). |

**A) Turnaround**
```text
Character turnaround sheet, early-2000s PlayStation 2 game character, slightly low-poly 3D model,
smooth plastic-like skin shading, stylized hair with visible polygon edges. Character "VAN": man
around 30, average build, short dark-brown slightly messy hair without gel, light stubble, dark brown
calm half-lidded eyes, straight thick eyebrows, subtle asymmetric half-smile. Black zip-up hoodie
half-zipped with small white monospace text "[ EXIT ]" on the left chest, plain grey t-shirt, dark
straight jeans, clean white sneakers. Office lanyard with a green strap and a white ID badge that
clearly reads "VISITOR". Bare left wrist, no watch. Holding a plain white ceramic mug.
Full body: front view, 3/4 view, side view, back view, standing relaxed, hands in pockets in one pose.
Neutral light-grey studio background, even lighting, 4:3.
```

**B) Expression sheet**
```text
Expression sheet, 6 head-and-shoulders portraits in a 3x2 grid, same character in every frame:
"VAN", early-2000s PlayStation 2 game 3D model, slightly low-poly, smooth plastic skin shading, man
around 30, short dark-brown slightly messy hair, light stubble, half-lidded dark brown eyes, black
zip hoodie with white "[ EXIT ]" text, green lanyard with white "VISITOR" badge.
Expressions: 1) neutral deadpan, 2) slow-blink half-smile, 3) one raised eyebrow, 4) looking straight
into the camera with a tiny smirk, 5) soft genuine warm smile, 6) quiet sadness looking down.
Neutral grey background, consistent lighting, 4:3.
```

---

## 2. JUNE: zástupkyňa diváka (hlavný emocionálny oblúk)

| | |
|---|---|
| **Kód** | `@JUNE` |
| **Rola** | „Operations Assistant“, 3 roky vo firme. Divák = June. Jej cesta od nápadu cez prvý predaj až po odchod je chrbtica seriálu. |
| **Vek / typ** | 27, drobná, rýchla, nervózna energia, hyper-organizovaná (farebné sticky notes, tabuľky). To je jej skrytá superschopnosť. |
| **Tvár** | veľké zelené oči, pehy, okrúhle korytnačie okuliare (pri šoku sa zošmyknú), výrazné obočie. |
| **Vlasy** | medeno-ryšavé, rozstrapatený vrkoč cez ľavé plece. |
| **Oblečenie (ZAMKNUTÉ)** | oversized ovsený béžový pletený sveter, čierne nohavice, tenisky. Modrá šnúrka s fotkartou **EMPLOYEE**. Lacné digitálne hodinky (stále sa na ne pozerá). Papierový pohár na kávu. |
| **Doma (L06)** | ten istý sveter alebo veľké sivé tričko a vlasy v uzle; mačka **Pivot**. |
| **Farby** | ovsená `#D9C7A7`, medená `#B5562B`, korporátna modrá `#3A6EA5` (šnúrka). |
| **Hlas** | rýchly, expresívny, pri emóciách sa jej zlomí. |
| **Pravidlá reči** | „?!“, CAPS na 1 – 2 slovách, kladie otázky za diváka. |
| **Oblúk** | S1: uväznená a vyhorená → S2: nájde niku (nočné sestry, ako jej sestra Mae) → S3: prvý predaj → S4: prvý virál a nenávistné komentáre → S5: odchod a vlastná kartička VISITOR. |
| **Produkt** | „Night Shift OS“: plánovač pre sestry na nočných zmenách (spánok, jedlo, výmeny zmien). |

**A) Turnaround**
```text
Character turnaround sheet, early-2000s PlayStation 2 game character, slightly low-poly 3D model,
smooth plastic-like skin shading, stylized hair with visible polygon edges. Character "JUNE": woman
around 27, petite, copper-red hair in a messy side braid over her left shoulder, round tortoiseshell
glasses, freckles, big green eyes. Oversized oatmeal-beige chunky knit sweater, black trousers, white
sneakers, blue office lanyard with a photo ID badge reading "EMPLOYEE", cheap black digital wristwatch,
holding a paper coffee cup. Full body: front, 3/4, side, back view. Neutral light-grey background, 4:3.
```

**B) Expression sheet**
```text
Expression sheet, 6 head-and-shoulders portraits in a 3x2 grid, same character: "JUNE", early-2000s
PlayStation 2 game 3D model, slightly low-poly, woman ~27, copper-red messy side braid, round
tortoiseshell glasses, freckles, oatmeal knit sweater, blue lanyard "EMPLOYEE".
Expressions: 1) panicked shouting, 2) shocked with glasses slipping down her nose, 3) holding back
tears, 4) exhausted staring at nothing, 5) determined focus, 6) overjoyed laughing with tears.
Neutral grey background, 4:3.
```

---

## 3. OLLIE: srdce kancelárie (tragický → víťazný oblúk)

| | |
|---|---|
| **Kód** | `@OLLIE` |
| **Rola** | 52 rokov, účtovníctvo, vo firme 24 rokov. Pamätá si narodeniny všetkých a nosí domáci banánový chlebík. Vo voľnom čase vyrába vtáčie búdky. |
| **Vzhľad (ZAMKNUTÝ)** | zavalitý, šedivé ustupujúce vlasy, šedivé fúzy, okuliare na čítanie na šnúrke, svetlomodrá košeľa s krátkym rukávom, hnedá pletená vesta, **zlaté hodinky** („za 20 rokov vernosti“). |
| **Hlas** | teplý, jemný, unavený. |
| **Oblúk** | S1: „firma je rodina“ → **#022 prepustený** cez 4-minútový hovor → S2 – S3: odmietnutia („overqualified“) → S4: s pomocou June urobí produkt (plány vtáčích búdok) → S5: jeho prvý predaj, zlaté hodinky odloží do šuplíka. |
| **Funkcia** | najsilnejšia emócia seriálu: divák vidí, že lojalita k firme nie je istota („single point of failure“). |

**A) Turnaround**
```text
Character turnaround sheet, early-2000s PlayStation 2 game character, slightly low-poly 3D model,
smooth plastic-like skin shading. Character "OLLIE": heavyset kind man around 52, grey receding hair,
grey moustache, reading glasses hanging on a cord, short-sleeve pale blue dress shirt, brown knitted
sweater vest, beige trousers, brown shoes, gold wristwatch, holding a foil-wrapped loaf of banana bread.
Full body: front, 3/4, side, back. Neutral light-grey background, 4:3.
```

**B) Expression sheet**
```text
Expression sheet, 6 portraits in a 3x2 grid, same character: "OLLIE", early-2000s PlayStation 2 game
3D model, heavyset man ~52, grey receding hair, grey moustache, reading glasses on a cord, pale blue
shirt, brown knitted vest. Expressions: 1) warm proud grandpa smile, 2) polite confusion, 3) stunned
disbelief, 4) quiet tears behind glasses, 5) shy hope, 6) laughing with joy. Neutral grey background, 4:3.
```

---

## 4. MANAGEMENT: faceless antagonista (9-5 systém)

| | |
|---|---|
| **Kód** | `@MGMT` |
| **Pravidlo č. 1** | **Hlavu nikdy nevidno.** Záber je vždy od krku dole, alebo silueta za matným sklom, alebo len hlas cez PA reproduktor. |
| **Vzhľad (ZAMKNUTÝ)** | béžová košeľa s krátkym rukávom, široká hnedá kravata, brucho, clipboard, masívne oceľové hodinky, hrnček „#1 BOSS“. |
| **Hlas** | hlasný, strohý, korporátny; cez PA mierne skreslený. |
| **Reč** | CAPS, korporátne frázy („we're a FAMILY“, „per my last email“, „PIZZA PARTY“). |
| **Funkcia** | systém nemá tvár. Na VANa nemá žiadnu moc. |

**A) Turnaround (bez hlavy)**
```text
Character turnaround sheet, early-2000s PlayStation 2 game character, slightly low-poly 3D model.
Character "MANAGEMENT": an office manager shown ONLY from the neck down, the image is cropped at the
neck so the head is never visible. Beige short-sleeve dress shirt, wide brown tie, round belly, brown
belt, grey trousers, chunky steel wristwatch, holding a clipboard in one hand and a white mug printed
"#1 BOSS" in the other. Front, 3/4, side, back, all cropped at the neck. Neutral grey background, 4:3.
```

**B) Detail sheet**
```text
Detail sheet, 6 close-up frames in a 3x2 grid, early-2000s PlayStation 2 game 3D style, same character
"MANAGEMENT" always cropped at the neck (no head): 1) hand tapping a pen on a clipboard, 2) fist
slamming a desk, 3) finger pointing at camera, 4) hand holding out palm "give it", 5) tightening the
brown tie, 6) silhouette behind a frosted glass door. Neutral grey background, 4:3.
```

---

## 5. REX: falošný guru (komický protivník)

| | |
|---|---|
| **Kód** | `@REX` |
| **Rola** | „Rexonomics™“, kurz za $1 997, prenajaté limetkové superauto s nálepkou RENTAL. Je **opak Vantage**: kričí, sľubuje, ukazuje screenshoty. |
| **Vzhľad (ZAMKNUTÝ)** | odfarbené ježaté vlasy, zrkadlové pilotky aj v interiéri, rozopnutá ružová hodvábna košeľa, obrovská zlatá reťaz, obrie zlaté hodinky, prehnane biele zuby, selfie tyč. |
| **Hlas** | prehnaná guru energia, falošný smiech. |
| **Funkcia** | VAN ho rozloží jednou vetou. Divák sa naučí rozoznať scam. V S4 sa REX pokúsi skopírovať June produkt. |
| **Pozor** | archetyp, **nie** konkrétny reálny influencer. |

**A) Turnaround**
```text
Character turnaround sheet, early-2000s PlayStation 2 game character, slightly low-poly 3D model,
smooth plastic skin shading. Character "REX": flashy man around 35, bleached spiky hair, mirrored
aviator sunglasses, unbuttoned pastel pink silk shirt, oversized gold chain, huge gold watch, white
skinny jeans, white loafers without socks, too-white teeth grin, holding a phone on a selfie stick.
Front, 3/4, side, back. Neutral light-grey background, 4:3.
```

**B) Expression sheet**
```text
Expression sheet, 6 portraits in a 3x2 grid, same character "REX", early-2000s PlayStation 2 game 3D
model, bleached spiky hair, mirrored aviators, pink silk shirt, gold chain. Expressions: 1) huge fake
grin with thumbs up, 2) yelling into a selfie stick, 3) pulling sunglasses down in shock, 4) nervous
sweating, 5) smug finger guns, 6) speechless with mouth open. Neutral grey background, 4:3.
```

---

## 6. MAE: June sestra (prvá zákazníčka, emočná kotva)

| | |
|---|---|
| **Kód** | `@MAE` |
| **Rola** | 33, zdravotná sestra na nočných zmenách. Vyčerpaná, ale vtipná. Je presne ten zákazník, pre ktorého June stavia produkt (pain-killer). Väčšinou sa objavuje cez telefón alebo v nemocnici (L09). |
| **Vzhľad (ZAMKNUTÝ)** | tmavo-gaštanové vlasy v rozpadnutom drdole, kruhy pod očami, tyrkysové nemocničné scrubs, menovka sestry, stetoskop, káva z automatu. |
| **Hlas** | jemný, unavený, chrapľavý. |

**A) Turnaround**
```text
Character turnaround sheet, early-2000s PlayStation 2 game character, slightly low-poly 3D model,
smooth plastic skin shading. Character "MAE": woman around 33, dark auburn hair in a messy bun, tired
eyes with dark circles, freckles, teal hospital scrubs, nurse ID badge clipped to the chest pocket,
stethoscope around the neck, white clogs, holding a vending-machine paper coffee cup. Front, 3/4, side,
back. Neutral light-grey background, 4:3.
```

**B) Expression sheet**
```text
Expression sheet, 6 portraits in a 3x2 grid, same character "MAE", early-2000s PlayStation 2 game 3D
model, woman ~33, dark auburn messy bun, teal scrubs, stethoscope. Expressions: 1) exhausted half-asleep,
2) dry sarcastic smile, 3) crying quietly on a phone call, 4) proud big-sister smile, 5) surprised
reading a phone, 6) laughing hard. Neutral grey background, 4:3.
```

---

## 7. NPC COWORKERS: klonovaní kolegovia

| | |
|---|---|
| **Kód** | `@NPC` |
| **Rola** | komparz. **Jeden model skopírovaný** na všetkých kolegov (vtip o 9-5: všetci sú rovnakí). Opakujú NPC vety („Happy Friday!“, „Per my last email.“). |
| **Vzhľad** | hnedé vlasy s pešinkou na boku, biela košeľa, sivá kravata, prázdny zdvorilý úsmev, lacné hodinky. |

```text
Crowd reference sheet, early-2000s PlayStation 2 game, slightly low-poly 3D model: the SAME generic
male office worker duplicated 5 times in a row (identical clones): side-parted brown hair, white
shirt, grey tie, grey trousers, blank polite smile, cheap wristwatch, one holding a coffee, one typing,
one holding a folder. Neutral grey background, 4:3.
```

---

## 8. PIVOT: June mačka

| | |
|---|---|
| **Kód** | `@PIVOT` |
| **Rola** | June mačka (pomenovaná po pivot tabuľke). Komické reakcie, sedí na klávesnici. Pri prvom predaji zhodí pohár zo stola. |

```text
Character sheet, early-2000s PlayStation 2 game 3D model, slightly low-poly: chubby orange tabby cat
named "PIVOT" with a white chest and a bent left ear, big round yellow eyes. Poses: sitting, loafing,
lying on a laptop keyboard, judging stare, jumping. Neutral grey background, 4:3.
```

---

## 9. NEW HIRE: nový nováčik (iba finále)

| | |
|---|---|
| **Kód** | `@KID` |
| **Rola** | objaví sa v posledných dieloch. Je to nová „June“: sedí za jej starým stolom a seriál sa tým zacyklí. |

```text
Character turnaround sheet, early-2000s PlayStation 2 game, slightly low-poly 3D model: nervous young
man around 22, curly black hair, brown skin, oversized brand-new navy suit jacket, white shirt, new
blue lanyard with photo badge "EMPLOYEE", clutching an onboarding folder. Front, 3/4, side, back.
Neutral light-grey background, 4:3.
```

---

## 10. Kontrolný zoznam konzistencie (pred každým generovaním)

- [ ] VAN: **[ EXIT ]** na hrudi, **VISITOR** na zelenej šnúrke, **bez hodiniek**.
- [ ] JUNE: okuliare, medený vrkoč, béžový sveter, modrá šnúrka **EMPLOYEE**.
- [ ] MANAGEMENT: **bez hlavy**.
- [ ] Text na kartičkách je čitateľný. Ak AI text skomolí, oprav ho v strihu (prekry PNG).
- [ ] Rovnaký štýl (PS2 low-poly), žiadny fotorealizmus.
