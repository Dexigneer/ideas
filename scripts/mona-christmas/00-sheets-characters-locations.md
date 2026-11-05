# 00 – Referenčné hárky: postavy + lokácie

Tieto obrázky vygeneruj **raz** a potom ich prikladaj ako reference images ku každému záberu.
Každý hárok má **tag** (napr. `@MONA`, `LOC-01`), na ktorý sa odvolávajú prompty v scenároch.

> Hlavná hrdinka Mona má vlastný detailný hárok v [`analysis/heroine-mona-character-sheet.md`](../../analysis/heroine-mona-character-sheet.md)
> (prompt 10a). Nižšie je len skrátená verzia pre rýchle kopírovanie.

**Spoločný štýlový základ** (už je zahrnutý v každom prompte nižšie):
`early-2000s PlayStation 2 game cutscene style, slightly low-poly 3D, smooth plastic-like skin shading, stylized hair with visible polygon edges, warm saturated cinematic lighting, 4:3`

---

## A. Postavy

### `@MONA` – hrdinka (3 verzie mikiny = 3 testované slogany)

Vygeneruj 3 varianty, líšia sa len textom na mikine. Do videí daného sloganu prikladaj príslušný variant.

| Variant | Text na mikine (`{SLOGAN}`) |
|---|---|
| `@MONA-A` | `YOU MET ME AT A VERY CHRISTMAS TIME OF THE YEAR` (3 riadky) |
| `@MONA-B` | `SANTA WORKS FOR ME` |
| `@MONA-C` | `OH MY REINDEER!` |

```text
Character reference sheet, early-2000s PlayStation 2 game cutscene style, slightly low-poly 3D model, smooth plastic-like skin shading, stylized hair with visible polygon edges, soft warm cinematic lighting. "Mona", woman in her late 20s, average build, thick copper-ginger hair in a messy updo held by a large cherry-red claw clip, two loose face-framing strands, freckles across the nose, calm heavy-lidded eyes, one eyebrow slightly raised, natural makeup, brick-red lips, small gold hoop earrings. Oversized cream hoodie with "{SLOGAN}" handwritten in cherry red across the chest, loose light-wash jeans, white sneakers. Holding a large clear iced coffee cup with lid and red straw, no logos. Calm knowing half-smile. Front view, 3/4 view, side view, back view, face close-up. Neutral light-gray background, 4:3. Modest, relatable, not sexualized.
```

### `@TASH` – najlepšia kamarátka (hlavná reaktorka)

Hlasná, dramatická, všetko natáča na telefón. Pracuje s Monou v tej istej firme. Miluje Vianoce ešte viac ako Mona, ale *chaoticky*.

```text
Character reference sheet, early-2000s PlayStation 2 game cutscene style, slightly low-poly 3D model, smooth plastic-like skin, warm cinematic lighting. "Tash", woman in her late 20s, deep brown skin, big voluminous dark curly hair, large gold hoop earrings, expressive wide eyes, glossy lips, emerald-green puffer jacket over a mustard sweater, holding a smartphone in a sparkly case. Expressions: shocked mouth open, pointing, screaming with joy. Front, 3/4, side view, face close-up. Neutral light-gray background, 4:3.
```

### `@BEV` – teta Bev (dotieravé otázky)

```text
Character reference sheet, PS2-era 3D cutscene style, slightly low-poly, plastic-like skin, warm lighting. "Aunt Bev", woman in her 60s, short lilac-tinted permed hair, pearl necklace, reading glasses on a chain, loud knitted Christmas sweater with a snowflake pattern, red lipstick slightly over the lip line, judgmental raised eyebrows. Front, 3/4, side view, face close-up. Neutral gray background, 4:3.
```

### `@JOSH` – bývalý / situationship (vždy prehrá)

```text
Character reference sheet, PS2-era 3D cutscene style, slightly low-poly, plastic-like skin, warm lighting. "Josh", man around 30, over-gelled spiky brown hair, overly white smile, too-tight light-blue button-up shirt, puffer vest, chunky silver watch, overconfident smirk. Front, 3/4, side view, face close-up. Neutral gray background, 4:3.
```

### `@GREG` – Gregory, kolega „mansplainer“

```text
Character reference sheet, PS2-era 3D cutscene style, slightly low-poly, plastic-like skin, warm lighting. "Gregory", man in his 40s, thinning slicked-back hair, rectangular glasses, beige sweater vest over a white shirt, lanyard with ID badge, holding a tablet, unnecessarily large smartwatch, self-important expression. Front, 3/4, side view, face close-up. Neutral gray background, 4:3.
```

### `@MOM` – Carol, Monina mama

```text
Character reference sheet, PS2-era 3D cutscene style, slightly low-poly, plastic-like skin, warm lighting. "Carol", woman in her late 50s, copper hair streaked with gray in a neat bob (family resemblance to Mona), freckles, cozy burgundy cardigan, apron with holly print, warm but frazzled expression. Front, 3/4, side view, face close-up. Neutral gray background, 4:3.
```

### `@DAD` – Ray, Monin otec

```text
Character reference sheet, PS2-era 3D cutscene style, slightly low-poly, plastic-like skin, warm lighting. "Ray", man in his early 60s, bald with a gray horseshoe of hair, bushy gray mustache, flannel shirt, slippers, TV remote in hand, cheerful clueless expression. Front, 3/4, side view, face close-up. Neutral gray background, 4:3.
```

### `@THEO` – synovec (7 rokov)

```text
Character reference sheet, PS2-era 3D cutscene style, slightly low-poly, stylized cartoonish child proportions, warm lighting. "Theo", 7-year-old boy, messy copper-ginger hair, freckles, missing front tooth, red pajama set with a reindeer print, big curious eyes. Front, 3/4, side view, face close-up. Neutral gray background, 4:3. Wholesome, family-friendly.
```

### `@NANA` – babka June

```text
Character reference sheet, PS2-era 3D cutscene style, slightly low-poly, plastic-like skin, warm lighting. "Nana June", woman in her 80s, fluffy white hair, oversized round glasses, lavender coat, tiny handbag, mischievous smile. Front, 3/4, side view, face close-up. Neutral gray background, 4:3.
```

### `@BRITT` – Brittany, Joshova nová priateľka (neskôr Monina spojenkyňa)

```text
Character reference sheet, PS2-era 3D cutscene style, slightly low-poly, plastic-like skin, warm lighting. "Brittany", woman in her mid-20s, long straight platinum-blonde hair with a pink velvet headband, pastel-pink teddy coat, sparkly nails, bubbly friendly expression. Front, 3/4, side view, face close-up. Neutral gray background, 4:3.
```

### `@SANTA` – Santa „Nick“ (večne prepracovaný zamestnanec)

Generický Santa z folklóru: žiadne logá, žiadna konkrétna filmová ani reklamná podoba.

```text
Character reference sheet, PS2-era 3D cutscene style, slightly low-poly, plastic-like skin, warm lighting. Generic folklore Santa Claus "Nick", heavyset man in his 60s, fluffy white beard, rosy cheeks, classic red suit with white fur trim, black belt, round glasses, visibly tired eyes with dark circles, holding a clipboard. No logos, no brand styling. Front, 3/4, side view, face close-up. Neutral gray background, 4:3.
```

### `@BISCUIT` – Tashin corgi

```text
Character reference sheet, PS2-era 3D cutscene style, slightly low-poly. "Biscuit", a fluffy orange-and-white corgi with a dramatic unimpressed expression, red collar with a tiny bell. Front, side, sitting, close-up. Neutral gray background, 4:3.
```

### Vedľajšie postavy jednorazové (stačí opis v prompte, hárok netreba)

| Tag | Opis do promptu |
|---|---|
| `@ETHAN` | handsome man ~30, short dark hair, navy peacoat, kind but confused face |
| `@PAT` | Mona's boss, woman in her 50s, sharp gray bob, black blazer, reading glasses, no-nonsense |
| `@DIANE` | HR interviewer, woman in her 50s, tight bun, pearl earrings, stern |
| `@LEO` | young barista, 20s, beanie, apron, nervous |
| `@GINA` | hair stylist, 40s, big teased black hair, leopard-print smock, gold chains |
| `@JESS` | new neighbor, woman 20s, glasses, oversized cardigan, moving boxes |
| `@OFFICER` | generic police officer, 40s, mustache, winter uniform jacket (no real agency insignia) |
| `@ELVES` | mall/workshop elves, adults in green elf costumes with pointy hats |

---

## B. Lokácie

Prompt na lokáciu generuj **bez postáv** (prázdna scéna). Vznikne čistá referencia prostredia.
Ideálne 2 zábery: široký (establishing) + protiuhol.

| Tag | Lokácia | Pohyb v pozadí (dôležité, aby záber žil) |
|---|---|---|
| `LOC-01` | Monin byt – obývačka (Vianoce už v novembri) | blikajúce svetielka, krb, sneh za oknom |
| `LOC-02` | Rodičovská jedáleň (rodinná večera) | sviečky, para z jedla |
| `LOC-03` | Rodičovská kuchyňa | para z hrncov, rúra svieti |
| `LOC-04` | Kancelária open-space (sviatočná výzdoba) | monitory, kolegovia v pozadí, blikajúca girlanda |
| `LOC-05` | Obchod – vianočná ulička (+ zvyšky Halloweenu) | blikajúce displeje, nakupujúci |
| `LOC-06` | Vianočné trhy v noci | sneh, para z punču, svetlá stánkov |
| `LOC-07` | Bar / sviatočná párty | disco svetlá, tancujúci ľudia, imelo |
| `LOC-08` | Santova zóna v obchodnom centre | rad detí, elfovia, točiaca sa dekorácia |
| `LOC-09` | Auto v noci (interiér + exteriér) | svetlá mesta a sneh za oknami |
| `LOC-10` | Kaviareň – pult | para z kávovaru, ľudia v rade |
| `LOC-11` | Chodba bytovky (dvere susedov, výťah) | blikajúce svetlá na dverách |
| `LOC-12` | Pošta / výdajňa balíkov | rad ľudí, pás s balíkmi |
| `LOC-13` | Monina spálňa v noci | svetlo telefónu, svetielka na okne, sneh |
| `LOC-14` | Vonkajšie klzisko | korčuliari, padajúci sneh |
| `LOC-15` | Kaderníctvo / nechtové štúdio | sušiče, zrkadlá, para |
| `LOC-16` | Letisko – gate pred Vianocami | lietadlá za oknom, tabuľa s odletmi |
| `LOC-17` | Santova dielňa (kancelária na severnom póle) | elfovia pracujú, padajúci sneh za oknom |
| `LOC-18` | „Spovednica“ – mockumentary rozhovor | malý stromček, sviečka |
| `LOC-19` | Školská sála – vianočné vystúpenie | reflektory, deti v kostýmoch |
| `LOC-20` | Tashin byt (maximalistická výzdoba) | stovky svetielok, nafukovacie figúry |

### Prompty lokácií

**LOC-01 – Monin byt, obývačka**
```text
Location reference, early-2000s PlayStation 2 game cutscene style, slightly low-poly 3D environment, warm saturated cinematic lighting, 4:3, no people. Cozy small city apartment living room fully decorated for Christmas: tall decorated tree with warm white lights and red ornaments, garland over a small fireplace with crackling fire, cream sofa with red and plaid pillows, stockings, fairy lights on the window, snow falling outside at night, coffee table with candles and an advent calendar. On a side table a wall calendar showing "NOVEMBER". Wide establishing shot + reverse angle toward the front door.
```

**LOC-02 – Rodičovská jedáleň**
```text
Location reference, PS2-era 3D cutscene style, slightly low-poly, warm candle-lit cinematic lighting, 4:3, no people. Suburban family dining room set for a big family dinner: long wooden table with white tablecloth, roast dishes with rising steam, candles, Christmas crackers at each plate, floral wallpaper, china cabinet, a small tree in the corner, window with snowy garden. Wide shot from the head of the table + reverse angle.
```

**LOC-03 – Rodičovská kuchyňa**
```text
Location reference, PS2-era 3D cutscene style, slightly low-poly, warm lighting, 4:3, no people. Busy suburban kitchen before Christmas: steaming pots, glowing oven with a turkey inside, flour on the counter, cookie trays, holly-print curtains, fridge covered with kids' drawings, sticky notes and a printed "CHRISTMAS SCHEDULE". Wide + counter-level angle.
```

**LOC-04 – Kancelária**
```text
Location reference, PS2-era 3D cutscene style, slightly low-poly, cool office light mixed with warm fairy lights, 4:3, no people. Open-space office decorated for the holidays: rows of desks with monitors, tinsel on cubicle walls, a sad small office tree, a whiteboard reading "HOLIDAY PARTY – PLANNING", a glass meeting room, a water cooler, snowy city skyline through big windows. Wide + desk-level angle.
```

**LOC-05 – Obchod, vianočná ulička**
```text
Location reference, PS2-era 3D cutscene style, slightly low-poly, bright store lighting with colorful displays, 4:3, no people. Big-box store aisle in early November: one side fully stocked with Christmas trees, ornaments, inflatable snowmen and a giant animatronic reindeer, the other side a clearance bin of leftover Halloween pumpkins and skeletons with "70% OFF" signs, shopping carts, hanging banner "HOLIDAY SEASON IS HERE". Wide aisle shot + end-cap angle.
```

**LOC-06 – Vianočné trhy**
```text
Location reference, PS2-era 3D cutscene style, slightly low-poly, warm golden string lights against a dark blue night sky, 4:3, no people. European-style Christmas market in a town square: wooden stalls with glowing roofs, steaming mulled wine pots, gingerbread hearts, a carousel in the background, big decorated tree, gentle snowfall, cobblestones, a life-size reindeer statue made of lights. Wide + stall-level angle.
```

**LOC-07 – Bar / sviatočná párty**
```text
Location reference, PS2-era 3D cutscene style, slightly low-poly, moody pink and teal neon mixed with warm string lights, 4:3, no people. Trendy bar hosting a holiday party: neon sign "SLEIGH BAR", bar counter with cocktails, disco ball, dance floor, mistletoe hanging from the ceiling, tinsel curtain backdrop for photos, velvet booths. Wide + bar-counter angle.
```

**LOC-08 – Santova zóna v obchodnom centre**
```text
Location reference, PS2-era 3D cutscene style, slightly low-poly, bright festive mall lighting, 4:3, no people. Shopping mall Santa photo area: big red velvet throne, fake snow, candy-cane fence, wooden sleigh prop, giant presents, queue ropes, rotating snowflake decorations, mall storefronts and escalators in the background. Wide + throne angle.
```

**LOC-09 – Auto v noci**
```text
Location reference, PS2-era 3D cutscene style, slightly low-poly, night lighting, 4:3, no people. Interior of a small hatchback car at night: front seats, dashboard glow, a tiny Christmas tree air freshener, iced coffee in the cup holder, snowy city street with blurred Christmas lights through the windshield and side windows. Also an exterior shot of the same car on a snowy roadside at night. Driver-side angle + passenger angle + exterior.
```

**LOC-10 – Kaviareň**
```text
Location reference, PS2-era 3D cutscene style, slightly low-poly, warm cozy lighting, 4:3, no people. Small independent coffee shop: counter with espresso machine releasing steam, chalkboard menu, pastry display, plain white cups (no logos), a "HOLIDAY MENU – COMING SOON" sign, rainy-snowy window, plants. Wide from the queue + behind-the-counter angle.
```

**LOC-11 – Chodba bytovky**
```text
Location reference, PS2-era 3D cutscene style, slightly low-poly, warm hallway lighting, 4:3, no people. Apartment building hallway: two facing apartment doors, one heavily decorated with a wreath, lights and a "SANTA STOP HERE" doormat, the other plain; an elevator with sliding doors at the end, moving boxes stacked, radiator, potted plant. Wide down the hallway + doorway angle.
```

**LOC-12 – Pošta / výdajňa balíkov**
```text
Location reference, PS2-era 3D cutscene style, slightly low-poly, flat fluorescent light, 4:3, no people. Busy post office in December: long counter with glass partitions, stacks of parcels, conveyor belt with boxes, queue line stanchions, a "LAST DAY FOR CHRISTMAS DELIVERY" sign, sad tinsel on the counter. Wide from the queue + counter angle.
```

**LOC-13 – Monina spálňa v noci**
```text
Location reference, PS2-era 3D cutscene style, slightly low-poly, dark blue night with warm fairy-light accents, 4:3, no people. Cozy bedroom at night: bed with a cream duvet and a plaid blanket, fairy lights around the window, snow falling outside, nightstand with an iced coffee cup and a phone glowing, digital clock showing 3:07 AM. Wide + bed-level angle.
```

**LOC-14 – Klzisko**
```text
Location reference, PS2-era 3D cutscene style, slightly low-poly, evening blue hour with warm string lights, 4:3, no people. Outdoor public ice rink in a city square: big decorated tree in the middle, string lights overhead, rental skates booth, hot chocolate stand, falling snow. Wide + ice-level angle.
```

**LOC-15 – Kaderníctvo / nechtové štúdio**
```text
Location reference, PS2-era 3D cutscene style, slightly low-poly, bright warm lighting, 4:3, no people. Glam hair and nail salon decorated for Christmas: salon chairs facing big mirrors with bulbs, hood dryers, manicure station with polish bottles, pink and gold tinsel, a small pink Christmas tree, hairspray mist in the air. Wide + mirror angle.
```

**LOC-16 – Letisko**
```text
Location reference, PS2-era 3D cutscene style, slightly low-poly, cool daylight through big windows, 4:3, no people. Airport departure gate before Christmas: rows of seats, departures board with several "DELAYED" flights, a plane visible on snowy tarmac, sad small tree with tinsel, charging station, gate desk. Wide + seat-level angle.
```

**LOC-17 – Santova dielňa**
```text
Location reference, PS2-era 3D cutscene style, slightly low-poly, warm lamp light, 4:3, no people. Cozy folklore Christmas workshop office: wooden workbenches with toys, conveyor belt with wrapped gifts, huge wall calendar counting down to December 24, a giant scroll "NICE LIST", a whiteboard with an org chart, snow falling outside arched windows. Generic, no brands. Wide + desk angle.
```

**LOC-18 – Spovednica (mockumentary)**
```text
Location reference, PS2-era 3D cutscene style, slightly low-poly, soft documentary-style key light, 4:3, no people. Simple interview setup: a single armchair in front of a softly blurred living-room background, tiny Christmas tree with lights, a candle, bookshelf. Framed medium shot like a documentary confessional interview.
```

**LOC-19 – Školská sála**
```text
Location reference, PS2-era 3D cutscene style, slightly low-poly, stage spotlights, 4:3, no people. Elementary school auditorium: small stage with red curtains, cardboard nativity-style backdrop with stars, rows of folding chairs, paper snowflakes, parents' phones would be held up here. Wide from the audience + stage angle.
```

**LOC-20 – Tashin byt**
```text
Location reference, PS2-era 3D cutscene style, slightly low-poly, overwhelming multicolor lighting, 4:3, no people. Small apartment with absurdly maximalist Christmas decorations: hundreds of multicolor lights, three trees, inflatable snowman, singing animatronic tree, tinsel everywhere, garlands on every surface, a giant deflated reindeer inflatable on the floor. Wide + doorway angle.
```

---

## C. Hlasy (AI TTS) – ulož si ich ako presety

| Postava | Popis hlasu |
|---|---|
| Mona | female, low alto, late 20s, slow and dry, slightly amused, never shouting, small pause before the last word |
| Tash | female, late 20s, high energy, fast, dramatic, cracks into shrieks on CAPS words |
| Aunt Bev | female, 60s, nasal, theatrical, judgmental, loud |
| Josh | male, 30, smug, salesy, overconfident, voice cracks when losing |
| Gregory | male, 40s, nasal, pedantic, slow-talking "well actually" tone |
| Carol (mama) | female, late 50s, warm, frazzled, fast |
| Ray (otec) | male, 60s, jolly, booming, clueless |
| Theo | child, 7, curious, slight lisp |
| Nana June | female, 80s, sweet but sly |
| Brittany | female, mid-20s, bubbly, upspeak |
| Santa Nick | male, 60s, deep, exhausted, sighing |
