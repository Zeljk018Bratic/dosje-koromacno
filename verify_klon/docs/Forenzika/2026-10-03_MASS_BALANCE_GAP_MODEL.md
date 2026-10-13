
### 1.2. Interpretacija

- **Gap = 0** → dokumentacijski lanac je zatvoren
- **Gap > 0** → postoji neevidentirana masa (zahtijeva objašnjenje)
- **Gap < 0** → postoji višak evidentirane mase (zahtijeva objašnjenje)

**Pozitivan ili negativan Gap sam po sebi nije dokaz nezakonitosti.** On je **indikator** koji zahtijeva daljnju forenzičku obradu.

---

## 2. KATEGORIJE OZNAČAVANJA

Posebno se označavaju pošiljke kod kojih postoji:

### 2.1. Nedostatak zapisa

- pošiljka postoji u carinskom sustavu, ali **nema zapisa u e-ONTO-u**
- pošiljka postoji u e-ONTO-u, ali **nema carinskog zapisa**
- pošiljka postoji u oba sustava, ali **nema zapisa o obradi na lokaciji**

### 2.2. Nesklad podataka

- **KBO se razlikuje** od deklarirane robe
- **masa se razlikuje** između sustava
- **datum se razlikuje** između sustava
- **pošiljatelj ili primatelj se razlikuju** između sustava

### 2.3. Vremenski nesklad

- pošiljka evidentirana u carini **prije** nego u e-ONTO-u (ili obrnuto) s razlikom > 30 dana
- pošiljka evidentirana kao "obrađena" **prije** nego što je uvezena

### 2.4. Dokumentacijski lanac koji se ne može zatvoriti

- nedostaje MRN
- nedostaje CMR
- nedostaje ePL / Prilog VII / notifikacija
- nedostaje potvrda o obradi

---

## 3. PRIMJENA NA KOROMAČNO

### 3.1. Vremenski okvir

- **2014.–2024.** — povijesni carinski tok (prije DIWASS-a)
- **2026.+** — DIWASS tok (Uredba EU 2024/1157)

### 3.2. Obuhvat

Model se primjenjuje na:

- sve pošiljke otpada **uvezene** na lokaciju Koromačno
- sve pošiljke otpada **izvezene** s lokacije Koromačno
- sve pošiljke u **tranzitu** kroz Republiku Hrvatsku

### 3.3. Izvori podataka

- **Carinska uprava** — MRN, deklaracije, CMR
- **MZOZT** — e-ONTO / ISGO evidencija
- **DIRH** — inspekcijski zapisnici
- **Operater** — interna evidencija (ako dostupna)

---

## 4. EPISTEMIČKO OGRANIČENJE

> **Podudaranje same mase nije dovoljno za zaključak o nezakonitosti.**
>
> **Dokazni lanac postaje znatno jači kada se istodobno podudaraju identitet pošiljke, subjekt, datum, masa, oznaka otpada i dokumenti o kretanju.**

---

## 5. IZLAZNI FORMAT

Za svaku pošiljku generira se zapis:

```csv
MRN,pošiljatelj,primatelj,datum,KBO,masa_ulaz,masa_obrada,masa_izlaz,gap,status
