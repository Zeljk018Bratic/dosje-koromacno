# Koromačno — sažetak dokumenata i primjer teksta za PETI

**Pripremljeno:** 4. studenoga 2026.
**Namjena:** informativna podloga koju zainteresirani mogu provjeriti, prilagoditi i po želji koristiti. Ovo nije podnesena predstavka niti pravno mišljenje.

## Što je izdvojeno iz matrice

U aktualnoj datoteci [Evidence_Matrix_CANON_v2.csv](../../../Evidence_Matrix_CANON_v2.csv) polje `Dokazna_vrijednost` za dolje navedene stavke nije ljestvica važnosti. Zato je ovo praktični izbor relevantnih dokumenata, a ne rangiranje koje je zabilježeno u matrici.

| Zapis | Što dokumentira | Zašto može biti koristan |
|---|---|---|
| **E-054** | MZOZT-ova informacija od 10. 8. 2026., objavljena 14. 8. 2026., o upućivanju Studije na javnu raspravu od 17. 8. do 16. 9. 2026. Javno izlaganje je bilo zakazano za 3. 9. 2026. KLASA **UP/I-351-03/25-08/46**, URBROJ **517-04-1-1-26-28**. | Utvrđuje planirane datume, mjesta uvida i način dostave primjedbi prema službenoj obavijesti. |
| **E-055** | MZOZT-ovo rješenje od 28. 8. 2026. o obustavi postupka procjene utjecaja na okoliš nakon što je nositelj zahvata istog dana odustao od zahtjeva. Objavljeno 1. 9. 2026. KLASA **UP/I-351-03/25-08/46**, URBROJ **517-04-1-1-26-30**. | Daje službeni razlog i datum obustave. Samo po sebi ne utvrđuje nezakonitost postupka ni ishod primjedbi javnosti. |
| **E-056** | EKONERG-ova Studija o utjecaju na okoliš, 801 stranica. U izvodu matrice opisan je planirani sustav alternativnog goriva: do 4 t/h kroz glavni plamenik i do 15 t/h kroz predkalcinator; navedena je i dozvola za pokusni rad za neopasni otpad KB 19 12 10. | Može poslužiti za usporedbu opisa u Studiji s važećim dozvolama i uvjetima. Opis planiranog postrojenja nije dokaz da se ono koristilo ili da su prekršeni uvjeti. |

Dodatni kontekst daje **E-060**: objava Općine Raša o raspravi, obrascima za primjedbe i roku. Matrica bilježi da je obustava 28. 8. prekinula raspravu koja je bila zakazana do 16. 9. te da su primjedbe podnesene do obustave trebale biti objedinjene u izvješću o dotadašnjem tijeku rasprave. To je razlog da se zatraži izvješće i provjeri kako su primjedbe obrađene — ne osnova za tvrdnju da su ignorirane.

### Izvorni dokumenti

- [E-054 — tekst službene informacije o javnoj raspravi](../../evidence/PUO_2026-08-14_INFORMACIJA_JR_text.txt)
- [E-055 — tekst rješenja o obustavi](../../evidence/PUO_2026-09-01_RJESENJE_obustava_text.txt)
- [E-056 — tekstualni izvod Studije](../../evidence/STUDIJA_text.txt)
- [E-060 i ostali zapisi — matrica dokaza](../../../Evidence_Matrix_CANON_v2.csv)

## Institucionalno postupanje i otvorena pitanja

- **E-054, E-055 i E-060** bilježe javno objavljenu proceduru, službenu obustavu nakon odustanka nositelja zahvata te općinsku objavu o tijeku javne rasprave. Iz toga se može tražiti pristup izvješću i evidenciji primjedbi; samo ti zapisi ne dokazuju da ih je tijelo zanemarilo.
- **E-039/E-041** bilježe navod/opažanje da određeni polusatni podaci o emisijama nisu bili javno vidljivi u navedenom razdoblju. U samoj matrici uzrok se ne tvrdi; traže se logovi, izvorni podaci i informacije o kalibraciji.
- **E-073** bilježi prosljeđivanje MZOZT-a DIRH-u. Prosljeđivanje samo po sebi nije dokaz ni ignoriranja ni rješavanja predmeta.

Prema tome, precizno je govoriti o **pitanjima koja treba razjasniti** — dostupnosti dokumentacije, obradi primjedbi i provjerljivosti mjerenja — a ne o dokazanom sustavnom nemaru.

### Podaci mobilne postaje i tehnička provjera (E-121–E-123)

Lokalno dostupan spremljeni 24-satni JSON izvoz za NO navodi 24 satne vrijednosti od 17. do 18. listopada 2026. i sažetak s prosjekom **−1,713 µg/m³**; prikazani raspon je **−2,121 do −0,374 µg/m³**. Zaseban JSON izvoz za NO₂ navodi prosjek **4,37 µg/m³**. To su vrijednosti zabilježene u spremljenim izvozima, a ne neovisna potvrda da su podaci validirani kao koncentracije u zraku, niti sami po sebi utvrđuju uzrok negativnih vrijednosti. Istodobni prikaz NO i NO₂ sam po sebi ne dokazuje da je izračun NOx-a matematički neispravan.

Negativni rezultati opravdavaju zahtjev za tehničkim pojašnjenjem: statusom validacije i naknadnih korekcija, jedinicama i vremenskom zonom, postupkom izračuna NOx-a te zapisima o održavanju i kalibraciji mjerne opreme. Za provjeru treba pribaviti izvorne podatke, metapodatke i objašnjenje nadležnog tijela. Ovi izvozi sami po sebi ne dokazuju kvar opreme, izostanak validacije na serveru ni povredu prava.

**Napomena o provjeri izvora:** SHA-256 zabilježen u retku E-122 (`7E3F61A081D2356435530BFB74C2D60A85F25B0CEFE09F8B94D087EA982A02BA`) ne podudara se sa SHA-256 lokalno dostupne datoteke [`2026-10-18_API_JSON_NO.json`](../../../2026-10-18_API_JSON_NO.json) (`6610B1C93C753D755908ABAFDEBB36A3AFF4F017567115D00001345D74F820DA`). JSON za E-121 naveden u matrici nije pronađen u ovoj radnoj kopiji. Prije prilaganja ili pozivanja na te hash-vrijednosti treba uskladiti izvorne datoteke i matricu.

## Moguće poveznice s pravom i politikama EU-a

Dokumentacija može biti polazište za pitanja o pristupu informacijama o okolišu i sudjelovanju javnosti, kao i o tome kako se planirane aktivnosti uspoređuju s dozvolama i primjenjivim okolišnim uvjetima. Za PETI se može zatražiti da razmotri koji su propisi EU-a primjenjivi i zatraži pojašnjenja nadležnih tijela. **Ova podloga ne zaključuje da je pravo EU-a prekršeno.**

Korisni prilozi za ta pitanja su obavijest o raspravi, rješenje o obustavi, izvješće o dotadašnjem tijeku rasprave (ako je dostupno), Studija i relevantne dozvole. Za mjerenja treba tražiti izvorne zapise i metapodatke, ne oslanjati se samo na izdvojene ili neprovjerene vrijednosti.

## Pitanja koja se mogu postaviti

1. Gdje je objavljeno izvješće o dotadašnjem tijeku javne rasprave i kako se može dobiti?
2. Koliko je mišljenja, primjedbi i prijedloga zaprimljeno do obustave 28. 8. 2026. i kako su evidentirani?
3. Je li nakon obustave pokrenut novi ili izmijenjeni postupak i gdje su objavljeni odgovarajući akti?
4. Koje su dozvole i uvjeti relevantni za aktivnosti opisane u Studiji i kako se njihova primjena provjerava?

## Primjer teksta za prilagodbu

> Podnositelj/podnositelji mole Europski parlament da razmotri pitanja pristupa informacijama i sudjelovanja javnosti u postupku procjene utjecaja na okoliš koji se odnosi na projekt dekarbonizacije cementare u Koromačnu. Prema zapisima E-054 i E-060, javna rasprava o Studiji bila je zakazana od 17. kolovoza do 16. rujna 2026., s javnim izlaganjem 3. rujna. Rješenjem MZOZT-a od 28. kolovoza 2026. (E-055; KLASA UP/I-351-03/25-08/46, URBROJ 517-04-1-1-26-30) postupak je obustavljen nakon odustanka nositelja zahvata.
>
> Molimo da se razjasni gdje su dostupni izvješće o dotadašnjem tijeku javne rasprave i evidencija primljenih primjedbi te je li pokrenut novi ili izmijenjeni postupak. Također molimo pojašnjenje koje dozvole i uvjeti vrijede za aktivnosti opisane u Studiji i kako se nadzire njihova usklađenost.
>
> Molimo i da nadležna tijela provjere spremljene API izvoze za mobilnu postaju Koromačno navedene u zapisima E-121–E-123: objavljene jedinice, vremenske oznake i vremensku zonu, status validacije i eventualne naknadne korekcije, izračun sažetih vrijednosti za NO/NO₂/NOx te dostupne zapise o održavanju i kalibraciji. Molimo da dostave ili upute na izvorne podatke i metapodatke. Navedeni izvozi bilježe negativne vrijednosti NO i pozitivne vrijednosti NO₂, ali sami po sebi ne utvrđuju uzrok ni povredu propisa.
>
> Ovaj zahtjev proizlazi iz potrebe da javnost može provjeriti službene akte i postupanje. Navedeni dokumenti sami po sebi ne utvrđuju povredu prava EU-a, prekoračenje emisija ili nezakonito postupanje; molimo da se činjenice i primjenjiva pravila provjere na temelju izvorne dokumentacije.

**Prije korištenja:** unesite tko podnosi predstavku, vlastito obrazloženje i konkretan zahtjev. Zadržite samo ono što osobno podržavate i možete potkrijepiti priloženim dokumentima.

## Važno razgraničenje

- Ova podloga **ne tvrdi** da je otpad iz Gospića upućen ili spaljen u Koromačnu. Za takvu tvrdnju bili bi potrebni primarni podaci o pošiljkama, otpremi, vagama, šiframa otpada i primatelju.
- Studija i dozvola opisuju dokumentaciju i dopuštene/planirane aktivnosti; same po sebi ne dokazuju stvarno korištenje otpada ni kršenje propisa.
- Prije korištenja API izvozâ kao priloga uskladite SHA-256 za E-122 i pribavite izvor naveden u E-121; detalji provjere navedeni su u odjeljku o mobilnoj postaji.

## Poveznica za dijeljenje

Javna izravna poveznica na ovu datoteku:
https://github.com/Zeljk018Bratic/dosje-koromacno/blob/main/docs/peticija/PETI/PETI_podloga_Koromacno_HR.md
