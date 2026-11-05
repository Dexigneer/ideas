# CLAUDE.md – repo `ideas`

Repo na výskum a tvorbu virálnych krátkych videí (TikTok / Reels / Shorts).
Používateľ píše po slovensky – odpovedaj po slovensky.

## Čo je v repe

| Cesta | Obsah |
|---|---|
| `analysis/3dmarlon-ps2-virality-breakdown.md` | Detailný rozbor 5 virálnych „PS2 style“ videí od 3dMarlon: záber po zábere, hook, štruktúra, psychologické mechanizmy, vizuál, zvuk, biznis stratégia, checklist. |
| `analysis/viral-script-prompt-kit.md` | Použiteľné prompty: master prompt na scenár, generátor premís, kritika/prepis, prompty na obrázky a video (PS2 štýl), špecifikácia strihu, ukážkový scenár. |
| `analysis/vantage-character-van.md` | Návrh maskota VAN pre Vantage Strategic Systems: svet hry „[ EXIT ]“, cast, typy videí, ukážková cutscéna, prompty. |
| `van/` | Produkčný balík seriálu VAN „[ EXIT ]“: character sheets, location sheets, **130 scenárov** (`van/scripts/`, prompt pre každý záber, SRT), marketingová stratégia (TikTok + IG). Scenáre sa upravujú v `van/data/*.txt` a generujú cez `python3 van/tools/render.py`. |
| `videos/3dmarlon/` | 5 zdrojových videí od 3dMarlon (+ README s prehľadom). |
| `videos/luca-maxim/` | 5 videí od Luca Maxim (rovnaký PS2 trend; merch „childrenofkhan.com“). Zatiaľ bez samostatného rozboru – stručné porovnanie je v sekcii 8 rozboru 3dMarlon. |

## Ako pracovať

- Pri písaní scenárov, hookov alebo promptov na videá **najprv si prečítaj oba súbory v `analysis/`**
  a riaď sa vzorcom a checklistom odtiaľ (hook v 1. sekunde, pokojný hrdina bez výkričníkov,
  1 replika = 1 záber ~2 s, pravidlo troch, férový zvrat, pointa ≤ 4 slová, loop).
- Nekopíruj chránené postavy ani podoby reálnych celebrít – používaj archetypy alebo vlastné postavy.
- Nové analýzy ukladaj do `analysis/`, nové videá do `videos/<tvorca>/` s krátkym `README.md`.
- Pri analýze videí: snímky cez `ffmpeg` (napr. 2 fps + časové značky do kontaktných hárkov),
  detekcia strihov (`select='gt(scene,0.25)'`), titulky čítaj priamo zo snímok, audio cez
  spektrogram a `ebur128`. Sťahovanie modelov z HuggingFace je v cloud prostredí blokované
  (prepis reči cez whisper nefunguje).
