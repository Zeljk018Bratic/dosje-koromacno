# Javna redakcija osobnih podataka

Datum provjere: 3. studenog 2026.

Iz javnih kopija uklonjeni su osobni identifikacijski podaci vlasnika dosjea, kućna adresa, privatni Gmail i vlastoručni potpisi. Namjerno javna službena adresa projekta ostaje dostupna.

## Završne provjere

- Tekstualni sadržaj i metapodaci svih 734 datoteka trenutačnog javnog snapshota provjereni su na poznate osobne identifikatore; nakon redakcije nisu pronađena podudaranja.
- Lokalni Windows OCR provjerio je 749 slabo tekstualnih stranica PDF-ova te svih 49 samostalnih PNG/JPG slika. Nakon redakcije nije bilo podudaranja s poznatim identifikatorima.
- Stranice s tekstualnim slojem provjerene su izdvajanjem teksta. Dva pronađena vlastoručna potpisa vizualno su prekrivena u svim trenutačnim kopijama koje ih sadrže.
- SHA-256 manifest odnosi se na javne, redigirane kopije; privatne izvorne kopije i privatni manifest nisu dio repozitorija.

## Opseg i ograničenja

OCR nije primijenjen na svih 1.351 stranica PDF-ova koje sadrže slike; stranice s dovoljnim tekstualnim slojem provjerene su izdvajanjem teksta. OCR i automatizirano traženje ne mogu potvrditi odsutnost svake moguće osobne informacije niti pouzdano prepoznati svaki rukom pisani podatak. Ovo je dokumentacija konkretne provjere poznatih identifikatora, a ne jamstvo da u repozitoriju nema drugih osobnih podataka.

## Git povijest

Ranije verzije datoteka koje su sadržavale poznate osobne identifikatore uklonjene su iz javne povijesti grane `main`; redigirane trenutačne kopije zadržane su. Povijest je prepisana uz odobrenje vlasnika repozitorija. Korisnicima koji imaju stari klon preporučuje se novo kloniranje.
