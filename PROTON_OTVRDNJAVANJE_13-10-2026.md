# PROTON — OTVRDNJAVANJE + BRISANJE OBRISANOG
**BajteBrothers / dosje-koromacno · 13.10.2026 · INTERNO (ne ide u javni repo)**

> Ovaj dokument sadrži putanje i opise postavki tvog računa → **ne commitaj ga** u
> `dosje-koromacno`. Ostaje lokalno (npr. `C:\Dokazi_E-2026-10\Zastita\`).

---

## 0. NAJVAŽNIJE, PRIJE SVEGA

Phrase je rotirana **13.10.** (tvoj screenshot: *"Wiederherstellungsphrase — Ein — Zuletzt geändert am 13 Okt."*).
**Stara fraza od 12 riječi time je mrtva.** Tko god je imao onaj PDF, sada drži bezvrijedan papir.

Znači: brisanje diska više **nije krizna operacija nego higijena**. Redoslijed je:

1. **Provjeri čiji je račun bio u tom PDF-u** (vidi §1) — jedino što može biti hitno.
2. Zatvori rupe u oporavku (vidi §3) — da ne izgubiš pristup dok vodiš predmet.
3. Očisti tragove na disku (vidi §5–§6).
4. Provjeri da nije bilo prijave bez tebe (vidi §4).

---

## 1. PITANJE KOJE ODREĐUJE SVE: čiji je bio onaj PDF?

U screenshotu si prijavljen kao **`dosje.koromacno@proton.me`** (projektni račun, 1.96 MB / 500 MB = Free).
`proton-recovery-phrase.pdf` koji je nađen u Downloads / OneDrive **nije nužno** od tog računa.

**Kako provjeriti (2 minute), za SVAKI svoj Proton račun:**

| Korak | Gdje | Što mora pisati |
|---|---|---|
| 1 | `account.proton.me` → prijava | — |
| 2 | Lijevo: **Wiederherstellung** | — |
| 3 | *Erweiterte Wiederherstellungsoptionen* → **Wiederherstellungsphrase** | **"Zuletzt geändert am 13 Okt."** |

- Ako piše **13 Okt.** → taj račun je siguran, stara fraza ne vrijedi. ✔
- Ako piše **stariji datum** → **rotiraj odmah** (klik na phrase → *Zurücksetzen / Neu generieren*),
  zapiši novu na papir, i **ponovno skini Wiederherstellungsdatei** (stara je tada nevažeća).

Isto ponovi za: osobni Proton, bilo koji stariji Proton, i Proton račune koje si otvorio
za projekt (npr. ako postoji i `bajtebrothers@…`). **Jedan po jedan.**

> Napomena: Protonova fraza je **12 riječi** (ne 24). Ako negdje vidiš 12 riječi na papiru/PDF-u — to je to.

---

## 2. ŠTO TVOJ SCREENSHOT VEĆ POKAZUJE (stanje 13.10.)

| Njemački naziv u postavkama | Stanje | Što znači | Ocjena |
|---|---|---|---|
| Wiederherstellungsphrase | **Ein**, promijenjeno 13 Okt. | pokriva **i** reset lozinke **i** dešifriranje podataka | ✔ najjača metoda, rotirana |
| Zurücksetzen im angemeldeten Zustand | **Ein** | reset lozinke iz aktivne sesije (sprječava zaključavanje podataka) | ✔ drži, ali zaključavaj ekran |
| QR-Code-Anmeldung | **Ein** | prijava drugog uređaja skeniranjem QR-a | ⚠ vidi §4 |
| Sicherung der Gerätedaten | **Ein** | šifrirani backup ključeva u **web storageu preglednika** | ✔ ali vidi zamku ispod |
| Wiederherstellungsdatei | **Nicht gespeichert** | datoteka s ključevima za dešifriranje | ✘ **napravi (10 min)** |
| E-Mail-Bestätigung / SMS | **dodano** (ocjena skočila na *"Stark"*) | reset lozinke putem druge e-mail adrese ili broja | ✔ pokriveno — **provjeri čija je ta adresa** (§3.1 pravila) |
| SMS-Verifizierung | nije dodano | reset lozinke putem broja | opcionalno |
| Wiederherstellungskontakt der Daten | nije dodano | pouzdane osobe **potvrđuju** tvoj zahtjev za oporavak podataka | ✘ dodaj 1–2 |
| Notfallkontakt (Emergency Access) | nije dodano | dead-man switch: osoba dobije pristup nakon čekanja | ⚠ **samo na plaćenim planovima** |
| Wiederherstellbarkeit | **"Stark"** ✅ | Protonova ocjena (account safety review) | ✔ **postignuto** — ali vidi §2bis: "Stark" ≠ "sigurno" |

**Zamka kod "Sicherung der Gerätedaten":** ključevi stoje u web storageu **tog** preglednika na **tom** uređaju.
Ako u pregledniku obrišeš "Podatke web-mjesta / Cookies" za `proton.me` → backup je gone.
→ Otvori `account.proton.me` u svom glavnom pregledniku, budi prijavljen, i **nemoj** brisati site data za proton.me.
(Kod brisanja cachea skriptom u §6 to je izuzeto — briše se samo `Cache`/`Code Cache`, ne i `Local Storage`.)

---

## 2bis. "STARK" — ŠTO TO DOKAZUJE, A ŠTO NE

Protonova ocjena **Wiederherstellbarkeit = Stark** dolazi iz alata *account safety review*
(`account.proton.me/safety-review`). Ona mjeri **jednu** stvar:

> *"Ako sutra izgubiš lozinku — možeš li se vratiti unutra I dešifrirati podatke?"*

Po službenoj Protonovoj tablici (`/support/set-account-recovery-methods`) treba ti:

| Korak oporavka | Metoda koja ga pokriva | Kod tebe |
|---|---|---|
| **1. Password reset** | recovery phrase / signed-in reset / **e-mail** / **SMS** | ✔ phrase + signed-in + (e-mail ili SMS) |
| **2. Data recovery** | recovery phrase / device data backup / **recovery file** / **contact-assisted** | ✔ phrase + device data backup (+ možda file/kontakt) |

Recovery phrase pokriva **oba** koraka — zato je "Stark" uopće moguć na Free planu.

### Što "Stark" NE znači (ovo su preostale rupe)

1. **Ne znači da je fraza rotirana.** Ocjena ne gleda datum.
   → §1 ostaje obavezan: *"Zuletzt geändert am 13 Okt."* na **svakom** računu.
2. **Ne znači da imaš recovery file offline.** Ako je "Stark" postignut samo preko
   *Sicherung der Gerätedaten* (device data backup), ključevi stoje u web storageu **jednog**
   preglednika na **jednom** stroju. Jedno brisanje site data / reinstalacija / kvar diska = "Stark" na papiru,
   a podaci zaključani. → §3.2 ostaje **otvoren dok ne skineš datoteku**.
3. **Ne znači da je recovery adresa sigurna.** To je novi mekani trbuh: tko god preuzme tu adresu,
   preuzima reset tvoje lozinke. → §3.1 tablica "NE/DA" vrijedi i sad, plus **2FA na toj adresi**.
4. **Ne znači da je provale nije bilo.** Ocjena gleda postavke, ne sesije/filtere/forward. → §4.
5. **Ne znači da je isto i na drugim računima.** "Stark" je **po računu**.
   Osobni Proton i poslovni tenant **"Interglobe Enterprises (UK)"** se ocjenjuju zasebno. → §1 + §6.1.

### Zaključak u jednoj rečenici
**Krizni dio je zatvoren** (fraza rotirana + ocjena Stark) → ostatak je **higijena**, ne panika:
recovery file offline (§3.2), provjera recovery adrese (§3.1), sesije/filteri (§4),
isti postupak na ostalim računima (§1) i disk/OneDrive (§5–§6).

---

## 3. REDOSLIJED AKCIJA (označi kvačicom)

### 3.1 Recovery e-mail — *E-Mail-Bestätigung → E-Mail-Adresse hinzufügen*  ☐
Proton ti je napisao: *"Datenwiederherstellung benötigt eine Option zur Passwortzurücksetzung (E-Mail oder SMS)"*.
Imaš "Sicherung der Gerätedaten" = **Ein**, dakle **čim dodaš recovery e-mail, pokriveno je oboje**.

**"moj neki e-mail ???" — koju adresu upisati:**

| NE | ZAŠTO |
|---|---|
| drugi vlastiti Proton račun | isti provider = jedna točka pada; tko provali u Proton, ima oboje |
| adresa koja se pojavljuje u prepisci s novinarima, Holcimom, institucijama | protivnik već zna tu adresu → cilja je |
| adresa osoba iz predmeta (Matea, Patrik, Admira, suradnici) | stvaraš vezu koja ih izlaže i koju se može zatražiti na sudu |
| poslovna/adresa tvrtke koju netko drugi administrira | admin ti može resetirati pristup |

| DA | KAKO |
|---|---|
| **neutralna, dosadna adresa** velikog providera, otvorena samo za ovo | koristi se **isključivo** kao Proton recovery |
| jaka jedinstvena lozinka + **2FA na toj adresi** | lozinka ide u tvoj manager/VeraCrypt, nikad u bilješke na disku |
| provjeri **njezine** recovery postavke | inače je to mekani trbuh cijelog lanca |

Za **osobni** račun (koji je ionako u tvoje ime) možeš dodati **i SMS** — dva neovisna puta do reseta.

### 3.2 Wiederherstellungsdatei — *Option hinzufügen → Wiederherstellungsdatei*  ☐
1. Skini datoteku.
2. **Ne ostavljaj je u Downloads / Desktop / OneDrive.** Premjesti u VeraCrypt kontejner.
3. Kopija na USB u sef + ispis (datoteka je šifrirana, pa je ispis bez lozinke bezopasan — ali ipak u sef).
4. **Pravilo:** nakon **svake** promjene lozinke/fraze → skini **novu** datoteku. Stara = otpad.
   (Pošto je fraza rotirana 13.10., sve prijašnje kopije su nevažeće.)

### 3.3 Wiederherstellungskontakt der Daten  ☐
- Osoba **mora već imati Proton račun**; **ne vidi i ne može otvoriti** tvoje podatke — samo potvrđuje tvoj zahtjev.
- Uzmi **1–2 osobe do kojih lako dođeš** (rodbina), a **ne** ljude čija se imena pojavljuju u predmetu:
  ne želiš javno vidljivu vezu `dosje.koromacno ↔ Matea/Patrik` niti da protivnik zna koga pritisnuti.
- Reci im unaprijed da će dobiti mail i da ti se jave — inače zahtjev stoji.

### 3.4 Notfallkontakt / Emergency Access — odluči  ☐
- Dostupno **samo na plaćenim planovima** (ti si Free; Proton nudi *Upgraden für 0,99 €* — vidi ispod).
- **Oboje** morate imati Proton Mail adresu.
- Čekanje: **1, 2, 3, 7, 14 ili 30 dana**; svaki zahtjev ti javlja, možeš ga odbiti.
- Ovo je tvoj **dead-man switch** za dosje: ako tebe nema, osoba ulazi i objavljuje/čuva materijal.
- Preporuka: **30 dana** (dovoljno da stigneš poništiti lažni zahtjev) + osoba koja razumije što treba napraviti
  s repozitorijem i `C:\Dokazi_E-2026-10\`.
- Ako ne platiš: dead-man switch riješi **izvan Protona** (papirnata uputa + VeraCrypt ključ kod druge osobe
  + dogovor o objavi dosjea). Manje elegantno, ali besplatno i ne ovisi o planu.

### 3.5 QR-Code-Anmeldung  ☐
Koristan za prijavu novog uređaja, ali: tko ima pristup tvom **otključanom** uređaju s otvorenom stranicom,
može skenirati i ući. → **Isključi ako ga ne koristiš.** Ako ostaviš: `Win+L` svaki put kad ustaneš,
kratak timeout zaključavanja ekrana, nikad otvoren Proton na tuđem računalu.

### 3.6 2FA  ☐
Proton eksplicitno kaže da 2FA postaviš **prije** metoda oporavka. Provjeri pod
**Sicherheit und Datenschutz** da je 2FA **uključen preko authenticator aplikacije** (ne SMS),
i da imaš **backup kodove** u VeraCryptu/papiru.

---

## 4. PROVJERA DA NIJE BILO PRIJAVE BEZ TEBE (10 min)

- [ ] Proton Account → **Sicherheit und Datenschutz** → aktivne sesije / povijest prijava → odjavi sve što ne prepoznaješ
- [ ] Proton Mail → postavke → **Filter** → nijedan filter ne prosljeđuje na tuđu adresu
- [ ] Proton Mail → postavke → **Weiterleiten und automatisch antworten** → **isključeno** (klasičan trajni nadzor nakon provale)
- [ ] **Identität und E-Mail-Adressen** → nema nepoznatih aliasa
- [ ] **Domainnamen** → prazno
- [ ] Sent / Arhiva → nema poruka koje nisi poslao
- [ ] Proton Sentinel (ako ga imaš na planu) → uključen
- [ ] Recovery phrase → datum = 13 Okt. na **svakom** računu (vidi §1)

---

## 5. DISK: KAKO OBRISATI OBRISANO

### 5.1 Prvo saznaj treba li ti uopće
```powershell
fsutil behavior query DisableDeleteNotify
Get-PhysicalDisk | Select FriendlyName, MediaType, BusType
```
- `DisableDeleteNotify = 0` **i** disk je **SSD** → **TRIM je uključen**: SSD sam nulira obrisane blokove,
  pa je "obrisano" praktički neobnovljivo unutar par minuta. **`cipher /w` ti ne treba** — štedi sate i trošenje diska.
- `= 1` **ili** disk je **HDD** → obavezno pusti `cipher /w` (§5.3).

### 5.2 Ono što si tražio (CMD / PowerShell, jedna linija)
```cmd
cipher /w:C:\
```
> Briše **slobodan prostor** cijelog volumena C: (3 prolaza: nule, random, nule).
> Traje **satima**, treba slobodnog mjesta, prekid je bezopasan.
> Varijanta: `cipher /w:C:\Users\zeljk` → isto briše slobodan prostor volumena na kojem je ta mapa.
> Alternativa (Sysinternals, treba preuzeti s microsoft.com i provjeriti hash): `sdelete -z C:`

Prije toga isključi spavanje: `powercfg /change standby-timeout-ac 0` i stavi laptop na punjač.

### 5.3 Ali prvo — ciljano (brže i pametnije): `proton_sweep.ps1`
Skripta je u workspaceu (`proton_sweep.ps1`). Kopiraj je npr. u `C:\Dokazi_E-2026-10\alati\`.

```powershell
Set-ExecutionPolicy -Scope Process Bypass -Force

# 1) SAMO TRAŽI (nista ne brise) — ovo pusti PRVO
.\proton_sweep.ps1

# 2) pogledaj izvjestaj, pa onda unisti pogotke (skripta trazi da upises UNISTI)
.\proton_sweep.ps1 -Cisti -Potvrdi

# 3) + isprazni Recycle Bin / Temp / Recent / thumbcache / cache preglednika
.\proton_sweep.ps1 -Cisti -Predmemorija -Potvrdi

# 4) ako je HDD ili TRIM=1 (dugo traje)
.\proton_sweep.ps1 -SlobodanProstor -Potvrdi

# opcije: -Duboko (cijeli pogoni)  -Povijest (redovi u History bazi)
#         -PovijestKompletno (cijela History baza)  -Indeks (rebuild Windows Search)
#         -Pogoni C,D  -Izlaz D:\Neko\Mjesto
```

Što skripta radi: traži po **imenu** (uklj. `proton*recovery`, `Wiederherstellungsphrase`,
`seed-phrase`, `proton…backup-keys`), po **sadržaju** tekstualnih datoteka, i **sirovo po bazama
preglednika** (Chrome/Edge `History` = povijest preuzimanja → otkrije je li PDF skinut dvaput i odakle).
Uz to napravi **popis malih PDF-ova** u Downloads/Desktop (`MALI_PDF_POPIS.txt`) — za slučaj da je
datoteka preimenovana; to **ne briše**, samo ispiše.

Zaštite: ne briše ništa bez riječi **UNISTI**; ne dira mape dosjea (`dosje`, `repo_dosje`,
`Forenzika`, `Evidence`, `Pravni-akti`, `Mediji`, `ZPPI`, `MANIFEST-SHA256`, `PAKET_`) — njih samo **prijavi**;
**ne čita i ne sprema sadržaj** nađenih datoteka, samo putanju + SHA-256.

Izlaz: `C:\Dokazi_E-2026-10\Proton_Sweep_<datum_vrijeme>\` → `IZVJESTAJ.txt`, `FUNDLISTE.csv`,
`MALI_PDF_POPIS.txt`, `SWEEP_LOG.txt` + **SHA-256 svakog** na kraju.

> **Ne stavljaš ovo u javni repo.** Izvještaj sadrži putanje tvog profila. Lokalno, u `Zastita/`.

---

## 6. ŠTO SKRIPTA NE HVATA — obavi ručno (15 min)

1. **OneDrive na webu** (oboje: osobni **i** poslovni tenant *"Interglobe Enterprises (UK)"*):
   - [ ] Recycle Bin → isprazni
   - [ ] **Second-stage / Site collection recycle bin** (ako postoji)
   - [ ] Version history te datoteke → obriši sve verzije
   - [ ] Poslovni tenant: **admin vidi sve**. Ako je onaj PDF ikad bio u poslovnom OneDriveu,
         tamo nije pitanje "je li obrisan" nego "tko ima administratorski uvid".
         → Projektni materijal **ne drži** u poslovnom tenantu. To je i OPSEC pravilo za ubuduće.
2. **Preglednik** (`Ctrl+Shift+Del`): obavezno označi **"Download-Chronik"** + cache.
   Provjeri **sve** profile (Chrome, Edge, Firefox) i **mobitel/tablet** ako se isto preuzimalo.
3. **Proton Mail**: ako je PDF ikad poslan kao privitak → fraza je ionako mrtva, ali obriši poruku
   i isprazni **Smeće/Arhivu**.
4. **Papir**: ako si frazu ispisao → stari ispis **uništi** (rezač/spaliti), novi drži u sefu.
5. **Provjera da je stvarno gone** (opcionalno): jedan recovery alat s **službene** stranice
   (npr. Recuva s ccleaner.com), pokrenut u read-only modu na tom folderu, pa ga **deinstaliraj**.
   Hashiraj installer prije pokretanja. Ne skidaj "data recovery" s reklamnih stranica.

---

## 7. ZAPISNIK (za tvoju evidenciju, ne za repo)

> **STATUS 13.10.2026. — ZATVORENO ZA OSOBNI RAČUN.** Potvrđeno: recovery e-mail (drugi mail) + SMS,
> phrase rotirana, recovery-file skinuta, 2FA, „Stark". Preostalo (§2bis): **samo poslovni Proton**
> i **poslovni OneDrive tenant** → odgođeno, vidi `PONEDJELJAK_19-10_RUNSHEET.md` (ne blokira predmet).

```
Datum/vrijeme:            ______________
Racunalo:                 ______________
Proton racun(i):          ______________
Phrase rotirana:          13.10.2026.  (potvrdi datum za SVAKI racun)
Recovery e-mail dodan:    ☑  DRUGI e-mail (potvrdjeno 13.10.2026.)  adresa: ______________ (ne upisuj lozinku!)
Recovery SMS dodan:       ☑  (potvrdjeno 13.10.2026.)  broj: ______________
Wiederherstellbarkeit:    STARK  (potvrdjeno u postavkama)
Wiederherstellungsdatei:  ☑  SKINUTA (potvrdjeno 13.10.2026.)  spremljena u: ______________  hash: ______________
Kontakt za oporavak:      ☐  ime: ________  (nije nitko iz predmeta)
Emergency Access:         ☐  plan: ________  cekanje: ____ dana
2FA (authenticator):      ☐  backup kodovi: ______________
Sesije/filteri/forward:   ☐  provjereno, cisto
proton_sweep.ps1:         ☐  SCAN ☐  CISTI ☐  Predmemorija ☐  SlobodanProstor ☐
Izvjestaj:                C:\Dokazi_E-2026-10\Proton_Sweep_____________\
SHA-256 izvjestaja:       ______________________________________________________
OneDrive (osobni+poslovni): ☐  web recycle bin + verzije ocisceni
Preglednici:              ☐  download-kronika + cache obrisani u svim profilima
```

---

*Pripremio: Qwen (fact-check navigator) za Željka Bratića — BajteBrothers.
Sve tvrdnje o Protonovim postavkama provjerene 13.10.2026. na proton.me/support
(set-account-recovery-methods, device-data-recovery, recovery-file, emergency-access).*
