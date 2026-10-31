# Mjerne stanice u Koromačnu: Dvije mreže, dvije stvarnosti

**Datum:** 18.10.2026.  
**Status:** JAVNI forenzički sažetak  
**Protokol:** MARA Forensic Team / #BajteBrothers  
**Povezani ID-evi:** E-107, E-108, E-121, E-122, E-123, E-124  

---

## 1. Dvije ključne postaje

### 1.1 Stalna mjerna postaja „Koromačno – Brovinje“ (mreža cementare / NZJZ IŽ)

| Stavka | Podatak |
|--------|--------|
| Upravljanje | Nastavni zavod za javno zdravstvo Istarske županije (NZJZ IŽ) |
| Financiranje / ulaganje | Holcim dobrovoljno uložio (od 2006.) |
| Parametri | SO₂, NO₂, PM2.5, PM10, O₃, CO, H₂S, NH₃ |
| Službeni status | Godišnje izvješće NZJZ IŽ 2025.: zrak **prve kategorije** |
| Anomalija (dosje) | Nerealno niske vrijednosti za industrijsku zonu (npr. NO₂ ≈ 1,82 µg/m³) |

### 1.2 Mobilna imisijska stanica u naselju Koromačno (mreža NZJZ SDŽ)

| Stavka | Podatak |
|--------|--------|
| Upravljanje | Nastavni zavod za javno zdravstvo Splitsko-dalmatinske županije (NZJZ SDŽ) – unajmljena |
| Parametri | SO₂, NO, NOₓ, NO₂ |
| Ključna anomalija | **Fizički nemoguće negativne vrijednosti NO** |
| Vrijednosti | 17.10.2026.: NO = **–2,121 µg/m³** · 18.10.2026. 10:17: NO = **–1,497 µg/m³** |
| API potvrda | JSON izvoz: mean NO ≈ **–1,713 µg/m³** (raspon –0,374 do –2,121); NO₂ mean ≈ 4,37 µg/m³ |

**Zaključak (tehnički):** Masene koncentracije ne mogu biti negativne. Negativni NO + pozitivni NO₂ čine izračun NOx matematički neispravnim. Ukazuje na zero-drift, nekalibriranost ili objavu nevalidiranih podataka.

---

## 2. Nesklad mreža

| Mreža | Prikaz | Problem |
|-------|--------|--------|
| Stacionarna (NZJZ IŽ / cementara) | „Vrlo dobra“ / 1. kategorija | Nerealno niske vrijednosti za aktivnu cementaru |
| Mobilna (NZJZ SDŽ) | Negativni NO | Fizički nemoguće; sumnja na zero-drift / nevalidirane podatke |
| Emisijski AMS (dimnjak) | Dnevni prosjeci „unutar GVE“ | Nedostaju sirovi satni/polusatni TOC (E12 otvoreno) |

**Status:** 🟠 OTVORENO – traži se tehnička verifikacija backend koda, kalibracije, .map datoteka i logova pristupa (ZPPI).

---

## 3. Zagađenje izvan zraka (kontekst lanca)

### Stroncij-90 (Gospić)
- Dokumentirani skok: **24,5 Bq/m² (2023.) → 260 Bq/m² (2025.)** ≈ **+961 %**
- Ozbiljan ekološki i zdravstveni signal; veza s ilegalnim odlaganjem otpada.

### PFAS („vječne kemikalije“)
- Službene analize vode za piće: bez utvrđenog PFAS (prema dostupnim izvorima).
- Neovisne analize / vještačenja: potvrđena prisutnost u **podzemnim vodama** ispod odlagališta u Gospiću (uključujući lokalne bunare) – vidi E-034 (Geotehnički fakultet / USKOK).

---

## 4. Međunarodni kontekst (poveznica)

- **Zero Waste Europe / GAIA webinar** „Beyond Burning“ (15.10.2026.) – Maris Sperac (Maksimir za Zagreb) izravno spomenula hrvatske cementare i carbon capture (KOdeCO) kao infrastrukturu koja može ovisiti o spaljivanju otpada (E-115–E-118).
- Predstavka EP 0474/2023 (Sperac) – zabrana novih spalionica.
- EPPO prijava inicijative Maksimir za Zagreb (Rebro).

---

## 5. Što se traži (ZPPI / inspekcija)

1. Sirovi AMS CSV (satni/polusatni TOC) – E12  
2. Kalibracijski certifikati i logovi mobilne stanice NZJZ SDŽ  
3. Backend / API validacijska pravila (zašto se negativni NO prikazuju)  
4. Usporedba vremenskih serija stacionarna vs mobilna vs dimnjak  
5. Vagarske liste i lab sastav 32 t (Gospić → Pazin → Koromačno)

---

**Napomena:** Dokument je čist, javan, bez referenci na zaštićene izvore.  
**Faza 2 aktivna. Deficiti se zatvaraju.**
