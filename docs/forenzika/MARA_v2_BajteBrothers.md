# MARA v2.0 – Mass Alignment & Reconstruction Analysis
**BajteBrothers Forensic Module**  
**Datum:** 03.10.2026.  
**Fokus:** Prekogranični tok otpada Italija → Hrvatska (Gospić / Tipos Resurs / Bilajska 50) + zasebna grana DZS 2025.

---

## 0. Osnovna pravila MARA v2

### Statusi
| Status | Značenje |
|--------|----------|
| **FAKT** | Neposredno potvrđeno izvornim dokumentom ili službenom statistikom |
| **DOKUMENTIRANA TVRDNJA** | Navedeno u istražnoj dokumentaciji / medijskom prijenosu istrage (Index, USKOK curenja) |
| **INDIKACIJA** | Snažan trag, ali bez potpunog lanca |
| **HIPOTEZA** | Logična pretpostavka koja se još testira |
| **OTVORENO** | Nije dokazano / nema dovoljno podataka |
| **POGREŠNO POSTAVLJENO** | Ranija pretpostavka koja se odbacuje |

### Dva odvojena podatkovna skupa (NE SPAJATI)

| Skup | Razdoblje | Količina | Pošiljki | Izvor | Status |
|------|-----------|----------|----------|-------|--------|
| **A** | 16.05.2022. – 11.04.2024. | 12.338 t | 576 | Istražna dokumentacija (Index / USKOK) | DOKUMENTIRANA TVRDNJA |
| **B** | 2025. | 19.013 t | ? | DZS statistika, CN 3825 90 90, vrijednost 124 € | FAKT (o statističkom zapisu) |

**Pravilo:** Skup A i Skup B se ne spajaju dok se ne pojavi konkretni identifikator koji ih povezuje.

---

## 1. Glavni dokazni lanac (prioritet)

```
Italija 
  → 576 pošiljki 
  → Gospić (Bilajska 50 / Tipos Resurs) 
  → KBO 
  → e-ONTO 
  → Dozvola (kroz vrijeme) 
  → Stvarna obrada / odlaganje 
  → Stanje na lokaciji
```

Zasebna grana:
```
DZS 2025 → 19.013 t → CN 3825 90 90 → 124 € (statistička vrijednost)
```

---

## 2. Ključevi identifikacije pošiljke

### Režim 2022. – 20.05.2026. (stari)
Primarni ključevi (redoslijed prioriteta):
1. Annex VII ID
2. Notification ID / Movement Document ID
3. e-ONTO ID
4. CMR ID
5. Pošiljatelj + Primatelj + KBO + masa + datum
6. MRN **samo ako je generiran**

### Režim od 21.05.2026. (novi)
- DIWASS identifikatori
- Uredba 2024/1157

**Napomena:** MRN **nije** univerzalni ključ za intra-EU promet. Postavljati ga kao takav = POGREŠNO POSTAVLJENO.

---

## 3. SHIPMENT FORENSICS TEMPLATE

Svaka pošiljka se vodi pod ovim poljima:

```
Shipment_ID:                  [interno]
Datum_polaska:                
Datum_ulaska:                 
Pošiljatelj:                  
Adresa_pošiljatelja:          
Primatelj:                    
Adresa_primatelja:            
Odredišno_postrojenje:        
Prijevoznik:                  
Registracija_vozila:          
CMR_ID:                       
Annex_VII_ID:                 
Notification_ID:              
Movement_Document_ID:         
MRN:                          [samo ako postoji]
Intrastat_ref:                [ako postoji]
KBO_EWC:                      
CN_kod:                       
Deklarirani_opis:             
Deklarirana_masa_t:           
Izvagana_masa_t:              
Vrsta_ambalaže:               
Laboratorijska_analiza:       
Stvarni_sastav:               
R_postupak:                   
e-ONTO_ID:                    
Lokacija_ulaza:               
Konačno_odredište:            
Dokaz_oporabe_zbrinjavanja:   
Izvorni_PDF_hash:             
Dokazni_status:               
Napomena:                     
```

**Prvi template za izradu:** jedna konkretna zaustavljena pošiljka na Pasjaku (ima vozilo, prijevoznika, analizu, laboratorij).

---

## 4. Mass Balance Gap – 4 nivoa

| Nivo | Naziv | Usporedba | Status ako postoji nesklad |
|------|-------|-----------|---------------------------|
| 1 | **Transport Gap** | Deklarirana masa ↔ CMR masa ↔ vaga | |
| 2 | **Administrative Gap** | Annex VII / Notification ↔ KBO ↔ e-ONTO | |
| 3 | **Process Gap** | Ulaz ↔ R-postupak (R1/R3/R12/R13…) ↔ proizvod / ostatak | |
| 4 | **Final Destination Gap** | Evidentirani ulaz ↔ stvarno postrojenje ↔ certifikat o oporabi/zbrinjavanju | |

Tek kada se pojavi nesklad na jednom ili više nivoa → **TOTAL MASS BALANCE GAP**.

---

## 5. Dozvola kroz vrijeme (Tipos Resurs / Bilajska 50)

| Godina / razdoblje | Dozvola | Dopušteni KBO | Dopušteni R-postupci | Maks. količina | Stvarni e-ONTO ulaz | Gap |
|--------------------|---------|---------------|----------------------|----------------|---------------------|-----|
| 2022 | | | | | | |
| 2023 | | | | | | |
| 01.01.–11.10.2024. | | | | | | |
| od 12.10.2024. | Postojeća (R3 7.000 t / R13 50 t za 19 12 04) | 19 12 04 i dr. | R3, R13 | | | |

**Pitanje koje se mora zatvoriti ZPPI-jem:**  
Koje su dozvole vrijedile na Bilajskoj 50 za **svaki dio** razdoblja 16.05.2022. – 11.04.2024. i koje su maksimalne količine i KBO tada bile dopuštene?

---

## 6. Statusna tablica – trenutno stanje

| Nalaz | Status |
|-------|--------|
| 576 pošiljki | DOKUMENTIRANA TVRDNJA |
| 12.338 t | DOKUMENTIRANA TVRDNJA |
| 576 pošiljki završilo u Gospiću | DOKUMENTIRANO (istražna dokumentacija) |
| Talijanske tvrtke navedene u istražnoj dokumentaciji | DOKUMENTIRANA TVRDNJA |
| Sve pošiljke bile pogrešno deklarirane | OTVORENO |
| Sve pošiljke bile opasni otpad | OTVORENO |
| 19.013 t = isti tok kao 576 pošiljki | NIJE DOKAZANO |
| 19.013 t = Koromačno | NIJE DOKAZANO |
| 19.013 t = Tipos Resurs | NIJE DOKAZANO |
| 124 € = stvarna cijena otpada | NIJE DOKAZANO |
| 124 € = DZS statistička vrijednost | FAKT |
| CN 3825 90 90 = automatski „otpad“ | NIJE DOKAZANO |
| e-ONTO može biti ključ za masenu rekonstrukciju | FAKT O FUNKCIJI SUSTAVA |
| MRN kao univerzalni ključ Italija–Hrvatska | POGREŠNO POSTAVLJENO |
| Annex VII / Notification / Movement Document | FAKT (stari režim) |
| DIWASS od 21.05.2026. | FAKT |

---

## 7. Prioritetni ZPPI zahtjevi (revidirani)

### 7.1 Carinska uprava / DIRH
Za svaku relevantnu pošiljku tražim **postojeći identifikator pošiljke** koji je prema tada važećem propisu služio za praćenje (Annex VII, Notification, Movement Document, CMR, e-ONTO ID), uključujući MRN **samo ako je u konkretnom predmetu generiran**.

Prioritet: jedna konkretna zaustavljena pošiljka na Pasjaku (template).

### 7.2 MZOZT – e-ONTO
Izvoz podataka za Tipos Resurs / Bilajska 50 (2022–2024) po mjesecu, po KBO, primljene i predane količine.

### 7.3 Dozvole
Sve dozvole za gospodarenje otpadom koje su vrijedile na lokaciji Bilajska 50 od 16.05.2022. do danas, uključujući kapacitete, KBO i R-postupke.

---

## 8. Sljedeći koraci (operativni)

1. Napraviti prvi popunjeni **Shipment Forensics** zapis za Pasjak pošiljku.
2. Poslati revidirane ZPPI zahtjeve (Carina + MZOZT + dozvole).
3. Popuniti matricu „Dozvola kroz vrijeme“.
4. Bakićeva grana (19.013 t) ostaje zasebna – cilj je probiti agregat do pojedinačnih zapisa bez pretpostavke identiteta.

---

**MARA v2.0** prestaje biti zbirka tvrdnji.  
Postaje **reproducibilni dokazni sustav** koji može uzeti 576 pošiljki i svaku provući kroz dokument → masa → KBO → dozvola → e-ONTO → prijevoz → lokacija → obrada → konačni izlaz.

Ako se nakon toga pojavi 10, 50 ili 200 stvarnih nesklada – imamo mjerljiv rezultat.  
Ako se dokumenti poklapaju – i to je rezultat.

