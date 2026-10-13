# PAKET_REPO_FINAL — 13.10.2026. · SVE DO GITHUB-A U JEDNOJ NAREDBI

**Cilj:** večeras sve najnovije na `github.com/Zeljk018Bratic/dosje-koromacno` (HEAD prije ovoga:
`bb164ce`), a sutra (14.10.) u Raši na Vijeću imati spreman list s pitanjima.

## Korištenje — 3 koraka

1. **Skini** `PAKET_REPO_FINAL_13-10-2026.zip` i raspakiraj bilo gdje (npr. `Downloads`).
2. **Pokreni** (PowerShell):
   ```powershell
   cd C:\Users\zeljk\Downloads\PAKET_REPO_FINAL_13-10-2026
   powershell -ExecutionPolicy Bypass -File .\SVE_U_REPO_13-10.ps1
   ```
3. **Pošalji Qwenu** zadnjih ~15 redaka ispisa (ili cijeli log iz
   `%LOCALAPPDATA%\dosje-lf-logovi\SVE_U_REPO_*.log`):
   - rezultat hash-provjere papirnate kopije (**IDENTICNO / RAZLICITO / PDF-NIJE-NADJEN**),
   - SHA256 matrice + broj redaka,
   - **ROOT HASH docs/** i **HEAD** (zadnje dvije linije).

Skripta **ništa ne briše**: backup matrice, interne datoteke i papirnata kopija idu u
`%LOCALAPPDATA%\dosje-izolacija-INTERNO`. Ako bilo gdje kaže **STOP** — ništa nije pushano,
pošalji log.

## Što skripta radi (redom)

| # | Korak | Zašto |
|---|---|---|
| 0 | `git pull --ff-only` | da commit ide čist, bez konflikta |
| 1 | backup `Evidence_Matrix.csv` izvan repo-a | sigurnost |
| 2 | raspakira **PAKET v3** (122 datoteke) u repo | jer na GitHubu (bb164ce) još NEMA: OLAF V2, EEA, ZPPI-13…20, Mediji 13.10., Uzorkovanje v2, portal-stranice |
| 3 | zaštiti **E-041** | zip-verzija matrice ima samo E-001…E-040; vraća lokalnu matricu, a ako ni ona nema E-041 → postavlja `CLEAN_PREVIEW` (44 retka) |
| 4 | izdvaja **interne datoteke** izvan repo-a | vidi niže |
| 5 | kopira današnji paket u repo | forenzika sažetka, E-042/43/44, hashovi, list za Vijeće, run-sheet |
| 6 | pokreće `NETEH_SAZETAK_PROVJERA.ps1` | hash papirnate kopije vs. službena MZOZT (`431b0d03…`), skidanje službene kopije u `docs/Arhiva/`, dedup matrice + E-042/43/44 |
| 7 | **validacija**: 44+ jedinstvenih redaka, E-041…E-044 prisutni, 1 zaglavlje, 0 duplikata | inače STOP — bez commita |
| 8 | `git add / commit / push` + ispis HEAD i root hash `docs/` | root hash ide u OLAF t.5 i EEA notice (trenutno `a3c64477…` @ bb164ce) |

## Datoteke u ovom paketu

| Datoteka | Kamo ide | Što je |
|---|---|---|
| `SVE_U_REPO_13-10.ps1` | pokreće se lokalno; kopija u `alati/` | glavna skripta |
| `NETEH_SAZETAK_PROVJERA.ps1` | `alati/` | hash + dedup + E-042/43/44 (logovi/backupi izvan repo-a) |
| `docs/Forenzika/2026-10-13_NETEHNICKI_SAZETAK_KODECO_ANALIZA.md` | `docs/Forenzika/` | analiza sažetka studije: 3 crvene linije, 7 nalaza, 15 pitanja, §5 što se NE smije reći |
| `docs/Evidence/E-MATRIX_NOVI_REDOVI_E042-E044.csv` | `docs/Evidence/` | 3 nova retka (sažetak studije, Poslovni 03.09., IstraIN 03.09.) |
| `docs/Evidence/Evidence_Matrix_CLEAN_PREVIEW.csv` | **NIKAMO** — samo fallback ako E-041 nedostaje | 44 retka, referentni izgled matrice |
| `SHA256_NOVI_DOKAZI_13-10-2026.txt` | `docs/Evidence/` | hashovi 5 arhiviranih dokumenata |
| `docs/Akcija/RASA_VIJECE_14-10-2026.md` | `docs/Akcija/` **+ Desktop** | list za sutrašnje Vijeće: TOP 5 naglas, svih 15 pitanja, 3 zabranjene rečenice |
| `docs/PONEDJELJAK_19-10_RUNSHEET.md` | `docs/` | run-sheet za val 19.10. (repo-verzija: bez imena zaštićenih osoba) |
| `PAKET_v3_13-10-2026.zip` | raspakira se u repo (korak 2) | 122 datoteke pripremljene 13.10. ujutro |

## Što skripta IZDVAJA iz repo-a (ne ide na javni GitHub)

1. `docs/Zastita/PAKET_ZA_MATEU_FINAL.md` — u samom dokumentu piše „NE ide u javni repo"
2. `docs/Zastita/OPCIJE_ZASTITA_SLAPP_I_PETAK.md` — označen INTERNO
3. `docs/Uzorkovanje/IZJAVA_PREDLOZAK_MATEA.md` — ime u nazivu datoteke krši kućicu 3
4. `docs/Akcija/2026-10-13_PLAN_JAVNOG_SKUPA_I_SUDJELOVANJA.md` — INTERNO + ime zaštićene osobe
5. papirnata kopija sažetka studije (ako leži u `docs/Arhiva/`) — u repo ide **samo** službena
   MZOZT kopija pod neutralnim nazivom; sve navedeno ostaje sačuvano u
   `%LOCALAPPDATA%\dosje-izolacija-INTERNO` (prebaci u `C:\Dokazi_E-2026-10\Zastita\`).

**Izvan ovog paketa i izvan repo-a (nikad ne commitati):**
`PROTON_OTVRDNJAVANJE_13-10-2026.md`, `TRIJAZA_PLAN.*`, bilo što s recovery frazama/lozinkama.

## Za sutra u Raši (14.10.)

- List je na **Desktopu** (`RASA_VIJECE_14-10-2026.md`) i u repou (`docs/Akcija/`).
- Izvor za sve tvrdnje je **isključivo javna MZOZT kopija** (URL + SHA-256 u zaglavlju lista).
- **Tri rečenice koje se NE smiju izgovoriti** (str. 15/43 dokumenta nas demantiraju) — na vrhu lista.
- Zaštićene osobe se ne spominju ni pod kojim uvjetom.
