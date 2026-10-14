# docs/DIRH-LKW/ — javna evidencija opažanja vozila (maskirano)

**Namjena foldera:** javni, vremenski slijed građanskih opažanja vozila u lancu prijevoza prema Koromačnu.
**Alat za unos:** `kamion.html` (terenski zapisnik; radi offline, bez servera).
**Naziv:** „DIRH-LKW" (bez dvotočke — dvotočka nije dozvoljena u imenima mapa na Windowsima/GitHubu).

## PRAVILA (obavezna)
1. U ovaj folder ide **SAMO maskirana verzija** zapisnika (`ZAPISNIK-JAVNI-*.md`): registracija maskirana (npr. `CE ***-798`), **bez fotografije**, s SHA-256 hashem originala.
2. **Puni zapisnik** (s pločom, svjedokom i referencom na original) i **originalna fotodatoteka** NE idu u javni repo: idu u Veracrypt arhiv i u prijavu DIRH-u (`docs/Pravni-akti/2026-10-10_HITNA_PRIJAVA_DIRH_EVIDENCIJA_VOZILA.md`).
3. Uz svaki javni zapisnik poželjno je dodati manifest-liniju u `MANIFEST-DIRH-LKW.txt` (`<sha256>  <ime_originala>`) — hash nije osjetljiv podatak, a dokazuje postojanje originala na datum objave.
4. Originalne fotografije se ne uređuju, ne rotiraju i ne brišu s uređaja svjedoka do zaključenja predmeta.

## STRUKTURA
- `ZAPISNIK-JAVNI-E-<datum>-<ID>.md` — po jedno opažanje
- `MANIFEST-DIRH-LKW.txt` — hash linije originala (kumulativno)
- (opcionalno) `README-pregled.md` — kumulativna tablica: datum, lokacija, maskirana ploča, oznaka, hash

## VEZE
- Prijava DIRH-u s punim podacima: `docs/Pravni-akti/2026-10-10_HITNA_PRIJAVA_DIRH_EVIDENCIJA_VOZILA.md`
- Bilješka o pravnom okviru oznake „A" i Uredbe 1013/2006: `docs/Forenzika/2026-10-10_SNIMKA_KAMION_CE_OZNAKA_A.md`
