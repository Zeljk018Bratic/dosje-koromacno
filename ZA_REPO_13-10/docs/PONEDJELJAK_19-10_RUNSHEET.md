# RUN-SHEET — PONEDJELJAK 19.10.2026. (val slanja) + NOĆNA TRI STVARI

*Svrha: jedno mjesto, bez čitanja 40 dokumenata. Redoslijed je obavezan. Cilj: 90 minuta ukupno.*
*Napravio Qwen 13.10.2026. — sve adrese označene ⚠️ provjeri klik-testom na impressumu prije slanja.*

---

## ⏱️ NOĆAS (max 30 min) — samo tri stvari

### 1. Commit + push — SVE U JEDNOM (10 min)

```powershell
cd PUTANJA-DO-RASPAKIRANOG-PAKETA   # npr. C:\Users\zeljk\Downloads\PAKET_REPO_FINAL_13-10-2026
powershell -ExecutionPolicy Bypass -File .\SVE_U_REPO_13-10.ps1
```

Skripta radi SVE: `git pull` → PAKET v3 u repo → zaštita E-041 → izdvajanje internih dokumenata
izvan repo-a → današnji paket (forenzika, E-042/43/44, list za Vijeće, ovaj run-sheet) → hash-provjera
papirnate kopije sažetka → čišćenje matrice na 44 retka → validacija → `commit` + `push`.
Ako bilo gdje kaže **STOP** → ništa nije pushano; pošalji Qwenu log iz `%LOCALAPPDATA%\dosje-lf-logovi\`.

Na kraju ispiše **HEAD** i **novi root hash za `docs/`** (`git rev-parse HEAD:docs`) — te dvije linije
pošalji Qwenu: ugrađuju se u OLAF točku 5 i EEA notice (trenutno stoji `a3c64477…` @ `bb164ce`,
što je i dalje točno, samo nije najnovije).

> Pravilo: **jedan službeni root hash.** Stari ostaje u evidenciji kao historijski.

### 2. Sweep — LAGANA verzija (15 min), bez `-SlobodanProstor`

```powershell
cd C:\Dokazi_E-2026-10\alati
Set-ExecutionPolicy -Scope Process Bypass -Force
.\proton_sweep.ps1                        # SAMO SCAN — ništa ne briše
notepad .\Proton_Sweep_*\IZVJESTAJ.txt    # pregledaj
.\proton_sweep.ps1 -Cisti -Predmemorija -Potvrdi   # traži UNISTI
```

SSD je KIOXIA BG4 → TRIM je gotovo sigurno uključen → **`-SlobodanProstor` preskoči** (traje satima, ne donosi ništa).
`-Duboko`, `-PovijestKompletno`, `-Indeks` → **preskoči**.

### 3. Preglednik (3 min)

`Ctrl+Shift+Del` → vremenski okvir **sve** → obavezno **Download-Chronik / povijest preuzimanja** + cache.
Ponovi u **svakom profilu** (Chrome, Edge, Firefox) i na mobitelu ako se isto skidalo.

**GOTOVO ZA NOĆAS. Ništa više. Ne otvaraj dosje.**

---

## 📅 PONEDJELJAK 19.10. — VAL (90 min, točno ovim redom)

### KORAK 0 — prije svega (10 min)
- [ ] Provjeri je li stigao odgovor na **ZPPI-04/05/07/08** (rok **16.10.**). Ako jest → arhiviraj, hashiraj, **ne odgovaraj još**.
- [ ] Ako NIJE stigao → zapiši u master: „16.10. istekao, bez odgovora" (to je FAKT, ne zaključak).
- [ ] Otvori `Evidence/Evidence_Matrix.csv` — svaki novi dokument dobiva redak prije nego što se citira.

### KORAK 1 — OLAF V2 (15 min) ⭐ najvažnije
**Datoteka:** `docs/Pravni-akti/2026-10-12_OLAF_THREAD_REPLY_V2_DRAFT.md`
**Status:** tekstu NE TREBA izmjena. Točke 1–5 + 3bis + 3ter su ugrađene i usklađene.
**Kako:**
- [ ] **REPLY na postojeći thread `Ares(2026)9536412`** — NE na no-reply adresu, NE novi mail.
- [ ] Subject ostavi kako je u threadu (`Re: Ares(2026)9536412 — clarifications and procedural status…`).
- [ ] Kopiraj **samo engleski dio** (od „Dear Sir/Madam" do potpisa). **HR NAPOMENE ostaju u repou, ne šalju se.**
- [ ] **Bez AI napomene/disclaimera** — ovo je tvoja izjava s citiranim izvorima.
- [ ] Nakon slanja: PDF poslanog maila + dokaz slanja → `docs/Slanje_Dokaza_19-10-2026/` → SHA-256 → commit.

> ⚠️ **Corrigendum** (`2026-10-12_OLAF_CORRIGENDUM_DRAFT.md`) je **rezerva**: šalje se SAMO ako V2 ne prođe
> ili ako OLAF zatraži zaseban ispravak. Ne šalji oba.

### KORAK 2 — domaći ZPPI val (45 min)

| # | Datoteka | Primatelj | Adresa | Rok odgovora |
|---|---|---|---|---|
| ZPPI-13 | `ZPPI-13/ZAHTJEV_R5_R1_DOZVOLE.md` | Istarska županija, Odjel za održivi razvoj | ⚠️ s impressuma `istra-istria.hr` (službenik za informiranje) · Cc `pristup.informacijama@mzozt.hr` | 15 dana |
| ZPPI-16 | `ZPPI-16/ZAHTJEV_IMI_POVIJESNI_PODACI.md` | IMI Zagreb | ⚠️ s impressuma `imi.hr` | 15 dana |
| ZPPI-17 | `ZPPI-17/ZAHTJEV_HV_NZJZ_PODZEMNE_VODE.md` | Hrvatske vode + NZJZ LSŽ + NZJZ IŽ | ⚠️ **3 odvojena maila** (svaki za svoju nadležnost) | 15 dana |
| ZPPI-18 | `ZPPI-18/ZAHTJEV_SIGURNOSNE_EMITIVNE_ANALIZE.md` | MZOZT (Uprava za PUO i SPVO) · Cc DIRH | `pristup.informacijama@mzozt.hr` · Cc `pisarnica.dirh@dirh.hr` | 15 dana |
| ZPPI-19 | `ZPPI-19/ZAHTJEV_KASTIJUN_SEKUNDAR_UGOVORI.md` | Kaštijun d.o.o. Pula, Premanturska cesta 215 | ⚠️ info-službenik s `kastijun.hr`; ako ga nema → `info@kastijun.hr` + preporučeno pismo | 15 dana |
| ZPPI-20 | `ZPPI-20/ZAHTJEV_MINGO_STRATESKI_PROJEKT_PCI_PMI.md` **← NOVO, večeras dodano** | MINGO, službenik za informiranje · Cc MZOZT | ⚠️ s impressuma `mingo.gov.hr` · Cc `pristup.informacijama@mzozt.hr` | 15 dana |
| ZPPI-04 dop. | `ZPPI-04/DOPUNA_2026-10-13_NOTIFIKACIJE_FAZA1.md` | Carinska uprava / MZOZT (isti kanal kao izvorni) | kao u izvorniku + **urudžbeni broj izvornog** | — |
| ZPPI-05 dop. | `ZPPI-05/DOPUNA_2026-10-13_NEDOSTUPNOST_MJERENJA.md` | MZOZT | `pristup.informacijama@mzozt.hr` | — |

**Pravila za sve:**
- U predmet UVIJEK stavi oznaku (`ZPPI-13 — …`) i, kod dopuna, **urudžbeni broj izvornog zahtjeva**.
- Cc: **samo sebi** (zeljkobratic69@gmail.com + dosje.koromacno@proton.me). Nikome drugome.
- Potpis: ime, adresa, dva maila. **Bez osobnog telefona.**
- Svaki poslan mail → PDF + SHA-256 → `docs/Slanje_Dokaza_19-10-2026/` → **jedan commit na kraju koraka**, ne 8 commitova.

> ZPPI-14 (Gospić videonadzor) i ZPPI-15 (FZOEU natječaj) → **srijeda 21.10.**, ne ponedjeljak. Razlog: FZOEU/CE-ZA-R
> je u aktivnom postupku provjere, neka prođe prvi krug. Ne gubiš ništa.

### KORAK 3 — ostatak domaćeg vala (15 min)

| Što | Datoteka | Kome | Napomena |
|---|---|---|---|
| DIRH — vozila | `Pravni-akti/2026-10-10_HITNA_PRIJAVA_DIRH_EVIDENCIJA_VOZILA.md` | `pisarnica.dirh@dirh.hr` | Upiši **datume snimki** u t. I.1 prije slanja. Rok odgovora 07.11. |
| DORH/USKOK dopuna | `Pravni-akti/2026-10-13_DOPUNA_DORH_USKOK.md` | ODO Pula · Cc USKOK | Predmet = **broj tvoje prijave od 09.10.** Provjeri da je Milinović-isječak označen kao **INDIKACIJA** (t. 2) — ostaje tako. |
| Pravobraniteljica | `Pravni-akti/2026-10-10_DOPIS_PRAVOBRANITELJICI_NEUPOVA.md` | `ombudsman.hr` ⚠️ točna adresa s impressuma | U t. 2 upiši **stvarno stanje na dan slanja** (što je odgovoreno, što nije). Bez „zid šutnje". |
| Status stranke | `Pravni-akti/ZAHTJEV_STATUS_STRANKE_V3_FINAL.md` | tijelo koje vodi postupak | Samo ako je postupak pokrenut; inače čeka. |

### KORAK 4 — zaustavi se ovdje (5 min)
- [ ] Regeneriraj MANIFEST → novi root hash → **OTS pečat** (ako radiš te večeri).
- [ ] Jedan redak u `Stanje_dosjea_na_10.10.2026.md` (addendum 19.10.): što je poslano, kome, urudžbeni brojevi, hashovi.
- [ ] Commit + push.
- [ ] **Kalendar:** 17.10. urgencije (ako ništa) · 21.10. ZPPI-14/15 · 25.10. žalbe Povjereniku · 07.11. DIRH rok.

---

## 🗞️ UTORAK 20.10. — coveri za medije (+24 h, NE prije)

**Datoteka:** `docs/Mediji/2026-10-13_COVER_EMAILS_v3.3.md` (DE + EN, adrese u tablici).

- [ ] U covere **upiši urudžbene brojeve** iz ponedjeljka („zahtjevi zaprimljeni pod brojevima …") — zato je redoslijed bitan.
- [ ] Klik-test svake adrese na impressumu (CORRECTIV, BR Recherche, BIRN, OCCRP).
- [ ] U potpisu **samo** `dosje.koromacno@proton.me` + repo + portal. **Bez osobnog telefona i adrese prebivališta.**
- [ ] **Phantom outleti se ne kontaktiraju i ne imenuju.** Nikad.
- [ ] Ako redakcija pita nešto izvan packa → **ne odgovaraš bez mog read-througha.**

## 🇪🇺 SRIJEDA–ČETVRTAK (21.–22.10.) — EEA + drugo

- [ ] **EEA notice** (`Pravni-akti/2026-10-13_EEA_SECRETARIAT_NOTICE_DRAFT.md`) — šalje se **24–48 h NAKON** OLAF-a i domaćeg vala, ne istovremeno.
      Prije slanja: identificiraj **točnog Programme Operatora** za „Business Development and Innovation Croatia" (eeagrants stranica) i upiši ga u To.
- [ ] ZPPI-14 (Gospić videonadzor), ZPPI-15 (FZOEU).
- [ ] AFCOS / DG REGIO / DG ENV / PETI / Aarhus → **NE šalje se** dok OLAF ne odgovori ili ne odustane od nadležnosti.

---

## 🚫 NE RADI / ODGOĐENO (da ti ne jede dan)

| Stavka | Zašto ne sada | Kada |
|---|---|---|
| TRIJAZA_PLAN.ps1 nad 1440 datoteka u Downloads | Ne donosi dokaznu vrijednost, jede sate | slobodan dan, ne prije 25.10. |
| Sent-mail PDF-ovi od 09.10. (5 hashova) u repo | Nedostatak je **kozmetički** — mailovi su poslani i dokazani | uz commit 19.10., 10 min |
| MO Koromačno grafovi (CDN vraća 403) | Izvor nedostupan; pismo je već arhivirano | kad MO objavi/drugačiji URL |
| ACER PDF lokalni hash | Mišljenje je javno i citirano po broju | kad stigneš, 5 min |
| OJ annex 2026/764 (CO₂ sekcija), redak-po-redak | Nije ništa blokirano time | po potrebi |
| „NETEHNIČKI SAŽETAK STUDIJE…Raša.pdf" (papirnata kopija, izvor zaštićen) | **RIJEŠENO 13.10.** — skripta hashira kopiju; u repo ide samo službena MZOZT kopija, papirnata ostaje izvan repo-a | `SVE_U_REPO_13-10.ps1` |
| Poslovni Proton (§1/§4) + poslovni OneDrive tenant | Nije vezano uz predmet; rizik je korporativni, ne dokazni | odvojeno, 20 min, ne noću |
| Kućice 1/2/3 (zaštićene osobe) | Čeka **njihov** pisani pristanak | po odgovoru |
| Novi alati, nove skripte, novi hash-alati | Dovoljno ih ima | — |
| Petak/akcija na terenu | Odluka o tipu/lokaciji/broju ljudi **nije donesena** → ništa se ne najavljuje pismeno | kad odlučiš, odvojeno |

---

## 🔒 TRI PRAVILA KOJA VAŽE KAD GOD KREĆEŠ PANIKA

1. **Ništa ne ide u spis bez papira ili hasha.** Sumnja = `OTVORENO`, ne činjenica.
2. **Ne pišeš namjeru.** Ne „sabotaža", ne „svjesno", ne „kompenzacija". Pišeš: datum, vrsta dokumenta, tko je što izjavio.
3. **Zaštićene osobe se ne imenuju bez pisanog pristanka.** Kućice ostaju kućice.

---

*Qwen · fact-check navigator · BajteBrothers — 13.10.2026.*
