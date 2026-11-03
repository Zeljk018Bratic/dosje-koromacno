# Javna redakcija osobnih podataka

Datum provjere: 3. studenog 2026.

Iz javnih kopija uklonjeni su osobni identifikacijski podaci vlasnika dosjea, kućna adresa, privatni Gmail i vlastoručni potpisi. Namjerno javna službena adresa projekta ostaje dostupna.

## Završne provjere

- Tekstualni sadržaj i metapodaci svih 734 datoteka trenutačnog javnog snapshota provjereni su na poznate osobne identifikatore; nakon redakcije nisu pronađena podudaranja.
- Lokalni Windows OCR provjerio je svih 1.351 stranica PDF-ova sa slikovnim sadržajem te svih 49 samostalnih PNG/JPG slika. Naknadnim OCR-om i vizualnim pregledom ponovno su provjerene sve stranice na kojima su pronađeni osobni podaci.
- OCR je otkrio osobni identifikacijski broj i vlastoručni potpis u dvije duplikatne kopije skeniranog dopisa te kućnu adresu i privatnu e-poštu u arhiviranom rješenju. Sve tri pogođene PDF datoteke redigirane su; naknadna provjera nije pronašla te identifikatore.
- Stranice s tekstualnim slojem provjerene su izdvajanjem teksta. Pronađeni vlastoručni potpisi vizualno su prekriveni u svim trenutačnim kopijama koje ih sadrže.
- SHA-256 manifest odnosi se na javne, redigirane kopije; privatne izvorne kopije i privatni manifest nisu dio repozitorija.

## Opseg i ograničenja

OCR i automatizirano traženje ne mogu potvrditi odsutnost svake moguće osobne informacije niti pouzdano prepoznati svaki rukom pisani podatak. Ovo je dokumentacija konkretne provjere poznatih identifikatora, a ne jamstvo da u repozitoriju nema drugih osobnih podataka.

## Git povijest

Ranije verzije datoteka koje su sadržavale poznate osobne identifikatore uklonjene su iz javne povijesti grane `main`; redigirane trenutačne kopije zadržane su. Povijest je prepisana uz odobrenje vlasnika repozitorija. Korisnicima koji imaju stari klon preporučuje se novo kloniranje.

GitHub je zadržao tri poslužiteljski upravljane reference zatvorenih pull requestova (`refs/pull/1/head`–`refs/pull/3/head`), koje se ne mogu prepisati običnim pushom. Njihovih 63 commita i sadržaj datoteka provjereni su na poznate identifikatore; podudaranja nisu pronađena. Provjera ne obuhvaća rasprave u pull requestovima, forkove ni predmemorirane kopije.
