# Dubinska provjera registara, rješenja i cjelovite Studije (Koromačno / KOdeCO)
**Datum analize:** 14.10.2026. | **Analitičar:** Qwen (fact-check navigator) | **Metoda:** izravno dohvaćanje s mzozt.gov.hr (python urllib), SHA-256 za svaki dokument, vizualno čitanje skeniranih rješenja (PyMuPDF render + pregled), ekstrakcija teksta cjelovite Studije (pypdf, 801 str.)
**Javni dokument:** DA (ne sadrži imena zaštićenih osoba ni interne reference)

## 1. Registar okolišnih dozvola Holcim Koromačno — PROVJERENO (E-048…E-052)
| Objavljeno | Rješenje od | Postupak | KLASA / URBROJ | SHA-256 (prvih 16) |
|---|---|---|---|---|
| 16.09.2014. | 15.09.2014. | ishođenje OD (objedinjeni uvjeti) | UP/I 351-03/12-02/96 / 517-06-2-2-1-14-46 | ebce44586dfe287c |
| 18.04.2018. | 09.04.2018. | razmatranje uvjeta OD | UP/I 351-03/16-02/135 / 517-06-2-2-1-18-16 | 69598b2d26b5e0a6 |
| 13.12.2021. | 09.12.2021. | izmjena i dopuna uvjeta OD | UP/I-351-02/21-51/04 / 517-05-1-3-1-21-4 | 49e736f7ae5e2b83 |
| 16.05.2024. | 07.05.2024. | izmjena i dopuna uvjeta OD (zahtjev 12.02.2024.) | UP/I 351-02/23-51/9 / 517-05-1-3-1-24-7 | 91b0eb0c70ebcfb9 |
Napomene: (a) rješenje iz 2024. u svojem dispositivu citira sva tri ranija rješenja — lanac je time samopotvrđen; (b) kopija rješenja iz 2014. u dosjeu (OUZO 2014) **hash-identična** novodohvaćenoj; (c) MARA-in sažetak miješa datum objave i datum rješenja — koristiti datum rješenja + KLASA.

## 2. Screening 2021. — službeni početak širenja oporabe otpada (E-046)
Rješenje MGOOR (Uprava za zaštitu prirode) **UP/I-612-07/21-60/63, URBROJ 517-10-2-2-21-2, Zagreb, 29.10.2021.** (zahtjev Holcima zaprimljen **19.10.2021.**): zahvat „Rekonstrukcija postrojenja s ciljem smanjenja emisija ugljičnog dioksida kroz **povećanje energetske oporabe otpada** u tvornici cementa Koromačno" prihvatljiv za ekološku mrežu; valjanost 4 godine (do 29.10.2025.). Str. 2 opisuje: dogradnja **pretkalcinatora**, sustav za izuzimanje klorida (**kloridni bypass**), skladište i transport za doziranje goriva iz otpada; kontrolno gorivo mješavina ugljena i petrol koksa; kapacitet klintera/cementa se ne mijenja. Najbliža POVS HR2001334 Poluotok Ubaš ~1,24 km; Glavna ocjena nije potrebna.
**Značenje:** plan povećane oporabe otpada postoji u službenom dokumentu od 19.10.2021. — prije javnih rasprava o KOdeCO i prije pokusnog rada pretkalcinatora (~listopad 2025. po MO Koromačno).

## 3. PUO kronologija KOdeCO — PROVJERENO (E-053…E-056)
| Datum | Akt | KLASA / URBROJ |
|---|---|---|
| 06.10.2025. | zahtjev Holcima za PUO (opunomoćenik EKONERG) | UP/I-351-03/25-08/46 |
| 30.12.2025. | INFORMACIJA o zahtjevu | isto |
| 10.08.2026. (obj. 14.08.) | INFORMACIJA o upućivanju Studije na javnu raspravu (JR 17.08.–16.09.2026.; uvid: Pula, Raša, Društveni dom Koromačno; javno izlaganje 03.09.2026. 18:30) | 517-04-1-1-26-28 |
| 28.08.2026. (obj. 01.09.) | RJEŠENJE o obustavi postupka (Holcim odustao od zahtjeva istog dana; cl. 46. ZUP; izvršno, bez žalbe, upravni spor 30 dana) | 517-04-1-1-26-30 |
**Cjelovita Studija (801 str., 100.601.525 B, SHA 12c2dc36…) i dalje je objavljena na MZOZT-u unatoč obustavi** — tvrdnja drugih analiza da je „uklonjena sa stranica institucija" je **NETOČNA**.

## 4. Nalazi iz cjelovite Studije (E-056)
1. **GIO sustav:** primarno doziranje **4 t/h** (glavni gorionik) + **pretkalcinator 15 t/h**; zatvoreno skladište GIO s rampama za kamionske prikolice s pomičnim dnom, automatski kran, zatvoreni tračni transporter do čeličnog tornja pretkalcinatora; kontrola otpada pri prihvatu (interne i vanjske laboratorijske analize).
2. **Dozvola za pokusni rad:** gospodarenje otpadom postupcima **R1 + R13** za neopasni otpad **KB 19 12 10**, KLASA **UP/I-351-04/24-09/7**, URBROJ **517-04-2-1-25-8**, od **14.03.2025.**, važeća do **14.03.2027.** (izdavatelj: Služba za dozvole, prekogranični promet otpadom i informatičku podršku MZOZT).
3. **Količine (tablica u Studiji, 4 godine):** 19 12 10: 20.700,71 / 20.624,87 / 22.097,19 / 20.920,68 t; 19 12 12: 0 / 0 / 0 / 325,99 t; UKUPNO sve šifre: 32.802,96 / 31.649,31 / 30.243,94 / 29.780,28 t.
4. **Mjera 59. (rješenje iz 2006., izmijenjeno):** na dijelu pretkalcinatora koristiti GIO (osnovni KB 19 12 10) po **HRN EN ISO 21640:2021**; mjere 19./20.: usklađivanje klora/žive u GIO uz kapacitete 4 + 15 t/h.
5. **Povijest RDF-a:** rješenje KLASA **UP/I 351-03/06-02/00036**, URBROJ **531-08-3-1-AM/DR-06-6** od **21.09.2006.** — postrojenje za prihvat, doziranje i upuhivanje **RDF-a 4 t/h** u rotacijsku peć (k.č. 521/1 k.o. Skitača); popis ranijih studija: 1985. promjena goriva, 1991. rekonstrukcija, **1997. alternativna goriva (otpadne gume, otpadna ulja)**, **2001. mesno koštano brašno + komunalni mulj**, **2006. RDF iz industrijskog i komunalnog otpada**.
6. **Varijante luke:** V1 = postojeći Vez 2 s lukobranom (~200 m, kut 110°); V2 = nova operativna obala Vez 3 (manje radova u moru, dublji podmorski ispust). Studija uspoređuje obje; odabrano rješenje = V2 (usklađeno s netehničkim sažetkom: Vez 3).
7. **Nulti pogodci u Studiji:** Gospić, SRF, PFAS (isto kao u sažetku). „Sekundar" = isključivo „sekundarno postrojenje/sekundarne sirovine" (nije tvrtka), „Kaštijun" = popis bivših odlagališta Grada Pule (nije ugovor).

## 5. Nesklad sažetak ↔ Studija (E-059) — KLJUČNO ZA JAVNU RASPRAVU
Netehnički sažetak (javni dokument, SHA 431b0d03…): **0 pogodaka** za pretkalcinator, GIO/gorivo iz otpada, KB 19 12, RDF, dozvolu R1/R13. Cjelovita Studija: sve opisano (točke 4.1.–4.5.). **Formulacija za uporabu (bez namjere):** „Javnosti dostupan netehnički sažetak ne opisuje sustav goriva iz otpada ni dozvolu za pokusni rad R1/R13 koje cjelovita Studija navodi; tražimo očitovanje o potpunosti sažetka u smislu cl. 87. ZOZ i Arhuške konvencije."

## 6. Provjera tvrdnji iz medija i civilnog sektora
| Tvrdnja | Izvor | Status |
|---|---|---|
| „148 prekoračenja TOC-a od početka godine, do ~2x od 35 mg/m3" | SDP Istre, priopćenje 15.09.2026. (Hina/N1/Index/HRT) | **TVRDNJA** (atribuirano; poziv na „javno iznesene podatke" bez izvora; službena potvrda ISZZ-a nema) |
| „GVE TOC opća 10 mg/m3, Holcimu dopušteno 35" | SDP / MO; podloga: sažetak str. 43 (10 (35)* + fusnota o internoj ISO dokumentaciji) i Studija (GVE 35 za oba dimnjaka) | **FAKT podloga** / interpretacija „povlastica" = TVRDNJA |
| Zbor mještana 07.10.2026., jednoglasno protiv KOdeCO, zahtjev obustave pretkalcinatora | MO Koromačno (istra24, labin.com, Radio Labin) | **FAKT** (održavanje i zaključci) |
| „Emisije višestruko iznad predviđenih SUO-om" + grafovi SO2/TOC/HCl | MO Koromačno (vlastita analiza) | **TVRDNJA** (grafovi arhivirani, hash; neovisna provjera nema) |
| „Holcim priznao da nema dozvolu za ključni KB otpada iz Gospića; miješanje na neotkrivenoj lokaciji" | MO Koromačno („saznanja"); istra24 ekskluziva (Pazin) | **TVRDNJA/INDIKACIJA** — provjera: inspekcija, EOJN, ZPPI-19 |
| „Dio otpada iz Gospića već dopremljen i spaljen" | MO Koromačno | **TVRDNJA** (mediji o pokusnoj pošiljci = INDIKACIJA; službene potvrde nema) |
| „Podaci s državnih stanica nedostupni od srijede 07.10. ~14:30 do ≥11.10. 11:30" | vlastiti Wayback/uvid | **FAKT opažaj**; zaključak „namjerno gašenje" = **HIPOTEZA** (ne iznositi kao fakt) |
| „Općina Raša mijenja prostorni plan" | Poslovni 03.09.2026. („lokalci idu u promjene prostornog plana") | **INDIKACIJA** (medijska); status postupka = OTVORENO (pitati Općinu) |
| „Projekt vrijedan 350 mil. EUR" | Poslovni / izjave | **TVRDNJA**; službena prezentacija 2024.: **CAPEX 237 mil. EUR** (FAKT) — ne miješati |
| „EU novac 116,9 mil. EUR ostaje; FID 30.06.2027.; pogon 31.05.2030." | Poslovni (izjava Holcima) | **TVRDNJA investitora** (atribuirano); CINEA fichè = FAKT za iznos granta |

## 7. Ispravci netočnosti iz zalijepljenih analiza (obavezno prije citiranja)
1. „Studija uklonjena sa stranica" → **netočno**; Studija je i dalje na MZOZT (hash gore).
2. „Rješenje o obustavi od 1. rujna 2026." → rješenje je **od 28.08.2026.**, objavljeno 01.09.2026.
3. „16.09.2014. izdana prva dozvola" → rješenje **od 15.09.2014.**, objavljeno 16.09.2014.; KLASA UP/I 351-03/12-02/96.
4. „GVE 35 mg/Nm3 odobrena" → precizno: OD GVE TOC = **10 (35)\*** mg/m3 (fusnota: 35 definirano internom ISO dokumentacijom jer TOC potječe iz sirovine); Studija predlaže 35 za oba dimnjaka; EU BAT-AEL za cement = <10 mg/Nm3.
5. „20 godina tihog uvođenja otpada preko okolišnih dozvola" → OD lanac kreće 2014.; povijest alternativnih goriva po Studiji kreće **1997./2001./2006.** — citirati te godine s izvorom.
6. „Zbor građana otkrio planove nove lokacije luke i podmorski ispust" → Zbor je raspravljao o Studiji (koja uključuje Vez 3 i podmorski ispust); „nova lokacija luke" nije usvojena izmjena nego varijanta V2 unutar Studije — ne tvrditi „promjena lokacije bez rasprave": javna rasprava o Studiji **jest** održana (17.08.–16.09.2026.).
7. Cabrunići rješenje (E-047) nema dokazane veze s Holcimom — ne povezivati.

## 8. Zabranjene formulacije (MARA V2)
„sabotaža", „svjesno", „namjerno gašenje podataka", „Holcim prikriva", „pravni manevar" — sve zamijeniti opisom dokumenata i pitanjima. Zaštićene osobe se ne imenuju. Fantomske medije ne kontaktirati.

## 9. Otvoreno (za ZPPI / inspekciju / EOJN)
Izvješće o tijeku javne rasprave (primjedbe 17.08.–16.09.2026.); potvrda ISZZ-a o 148 prekoračenja (pun zapis polusatnih vrijednosti 01.01.–14.10.2026. za stanice Koromačno/Brovinje); ključni brojevi otpada i pošiljatelji zaprimljeni u rujnu/listopadu 2026. (inspekcija/EOJN); status izmjena prostornog plana Općine Raša; arhiva HTML izvornika N1/istra24 (403 na izravno skidanje — sačuvati iz preglednika).


## 10. Obavijest Općine Raša o javnoj raspravi (E-060) — što dokazuje, a što NE
Arhivirano 14.10.2026. (extract stranice; izvorni HTML čuva Željko iz preglednika): rasa.hr obavijest o JR
(17.08.–16.09.2026.), koordinator IŽ, tri fizičke lokacije uvida + tri web stranice, javno izlaganje 03.09.
18:30, primjedbe zaključno 16.09. na IŽ; **Općina je sama pripremila obrazac za primjedbe** (web/print/Word)
uz naputu o vlastoručnom potpisu i potvrdi primitka; cjelovita Studija objavljena i preko Google Drive mape;
sažetak objavljen i na rasa.hr (sadržajno istovjetan MZOZT verziji, normalizirani hash ab5e2dcb…).
**Ispravne pravne formulacije (umjesto „građani nisu imali priliku" i „dokaz političkog dogovora"):**
1. JR je **prekinuta 12. od 30 dana** obustavom postupka (28.08.2026.) — činjenica iz E-055.
2. Primjedbe predane do obustave **ostaju u spisu** i moraju ući u izvješće o javnoj raspravi (E-054/istra24);
   primjedbe koje bi bile predane 29.08.–16.09. **nisu prikupljane** — to je mjerljivi gubitak participacije.
3. Svaka nova ili revidirana Studija zahtijeva **novu javnu raspravu**; do nje projekt nema važeću PUO podlogu.
4. Općina Raša je aktivno **olakšavala** sudjeljenje (obrasci) — tvrdnja „nitko nije omogućio primjedbe" bila bi
   oboriva; koristiti isključivo gornje tri formulacije.
**ZPPI koji iz ovoga proizlazi (već na listi):** izvješće o tijeku javne rasprave (IŽ, odrzivi.razvoj@istra-istria.hr)
s popisom svih primjedbi i odgovorima; potvrda koje su primjedbe zaprimljene 29.08.–16.09. i kako su obrađene.
