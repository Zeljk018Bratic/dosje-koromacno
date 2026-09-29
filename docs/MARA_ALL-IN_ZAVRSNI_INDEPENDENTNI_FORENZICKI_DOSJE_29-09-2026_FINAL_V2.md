MARA / OFFF

ZAVRŠNI NEOVISNI FORENZIČKI DOSJE

Labin · Koromačno · Raša · Ubaš | stanje provjere i dokaznog lanca 29. rujna 2026.


| **Svrha dokumenta: neovisno preslagivanje cijelog dostupnog projekta, AI analiza, izvornog koda, SUO dokumentacije, prostorno-planskih akata, lokalnih izjava i aktualnih institucionalnih događaja u jedinstvenu dokaznu strukturu. Ovaj dokument ne presuđuje tko je kriv. On pokazuje što je dokazano, što je tvrdnja, što je indicija, što je hipoteza i što još treba pribaviti.** |
| - |


## **Dokumentarni korpus**

- 7 korisnički dostavljenih Markdown/tekstualnih dokumenata, uključujući četiri AI analize, ALL-IN analizu, riziko-matricu i analizu tokova otpada.

- 1 izvorna SUO studija EKONERG I-03-1212, 801 stranica.

- 2 javna GitHub repozitorija, open-fiscal-forensics i dosje-koromacno.

- 1 dodatni korisnički dostavljeni tekstualni izvor: „KOROMAČNO – Park prirode ili teška industrija“, korišten kao zaseban strateško-povijesni izvor i nije automatski tretiran kao primarni dokaz.

- 1 dostavljeni prijateljev AI chat s prijedlogom neovisne stručne skupine.

| **GLAVNA METODOLOŠKA ODLUKA: AI tekstovi nisu dokazni izvor sami po sebi. Primarni dokument, službeni zapisnik, izvorni kod ili neposredno provjerljiv javni zapis ima prednost pred AI interpretacijom.** |
| - |



# 1. IZVRŠNI SAŽETAK

Nakon ponovnog pregleda cijelog dostupnog korpusa, projekt MARA/OFFF pokazuje tri odvojene vrijednosti. Prva je tehnička, jer daje lokalni alat za reproducibilnu obradu javnih podataka. Druga je dokumentarna, jer GitHub i dosje-koromacno čuvaju kronologiju, dokumente i radne matrice. Treća je istraživačka, jer pokušava povezati proračun, otpad, emisije i prostorne postupke u jedinstveni lanac.

| **NAJVAŽNIJI ZAKLJUČAK: Funkcionalni hardening OFFF-a je velikim dijelom zatvoren. Preostali posao je repository hygiene i dokumentacijska usklađenost, dok za Koromačno i Ubaš najveći otvoreni zadatak ostaje zatvaranje materijalnih tvrdnji primarnim izvorima.** |
| - |


| **Područje** | **Što je danas čvrsto** | **Što još nije dokazano** |
| - | - | - |
| **KOdeCO procedura** | **Holcim je 28.08.2026. odustao od tadašnjeg PUO zahtjeva, a postupak javne rasprave je obustavljen. \[W1\]** | **Da je razlog povlačenja bio prikrivanje, pritisak ili taktička manipulacija.** |
| **PPUO Raša** | **V. izmjene su zaseban prostorno-planski postupak. Javna rasprava o planu je zasebna procedura.** | **Da su izmjene donesene samo radi KOdeCO ili da će sigurno omogućiti novu verziju projekta.** |
| **QRA** | **SUO sadrži numeričke scenarije i zone 50.000/100.000 ppm.** | **Da sama QRA implicira stvarni događaj. Postoji i unutarnja tekstualna/tablearna nedosljednost koju treba razjasniti.** |
| **OFFF hash-chain** | **Aktualni transparency\_reconciler.py implementira SHA-256 lanac i verify\_chain.** | **Da svaki izvorni podatak time postaje istinit. Hash potvrđuje integritet kopije, ne istinitost sadržaja.** |
| **Benford** | **Aktualni forensic\_core.py računa χ² iz opaženih frekvencija.** | **Da prolaz statističkog testa dokazuje urednost ili odsutnost manipulacije.** |
| **Git hygiene** | **.gitignore je uveden.** | **Da su već praćeni .pyc, signatures.db, my\_risk\_oibs.json i privremeni artefakti već uklonjeni iz javnog repozitorija.** |
| **19.013 t / 124 €** | **Tvrdnja postoji u više radnih dokumenata.** | **Nema dovoljnog primarnog carinskog/materijalnog lanca u ovom korpusu da bi tvrdnja bila zatvorena.** |


# **2. METODOLOGIJA: KAKO ČITATI OVAJ DOSJE**

| **Status** | **Značenje** | **Primjer** |
| - | - | - |
| FAKT | Primarni izvor ili izravno provjerljiv zapis postoji. | Sadržaj službenog rješenja Ministarstva. |
| DOKUMENTIRANA TVRDNJA | Postoji dokument koji tvrdi nešto određeno, ali nije neovisno potvrđeno. | Navod o količini određenog toka otpada. |
| INDICIJA | Postoje elementi koji upućuju na pitanje, ali ne zaključuju ga. | Copyright treće tvrtke na endpointu. |
| HIPOTEZA | Objašnjenje koje može biti moguće, ali treba novi dokaz. | Preusmjeravanje regionalnih tokova otpada prema Koromačnom. |
| OTVORENO | Nema dovoljno dokaza za činjeničnu tvrdnju. | 19.013 t talijanskog otpada za 124 €. |


Pravilo za objavu: svaka rečenica koja govori o odgovornosti neke fizičke ili pravne osobe mora biti vezana uz konkretnu radnju, dokument, ovlast i vrijeme. AI interpretacija, medijski naslov ili korelacija nisu zamjena za dokaz.

# **3. ANALIZA SVAKOG AI IZVORA ZASEBNO**

Ovdje AI modeli nisu rangirani. Svaki je promatran kao radni dokument koji je nešto dobro izvukao, ali je istodobno unio i pogreške ili preširoke zaključke.

## **GEMINI**

Koristan dio: Najkorisniji doprinos je prepoznavanje tehničkih rupa u OFFF-u i potreba da se mock hash zamijeni pravim hash-chainom. Također je jasno izdvojio korekciju 6.000 m³ nasuprot 6.000 tona, 19.013 t kao otvorenu tvrdnju i problem statusa oštećenika.

Korekcija: Preuzeo je pojedine tvrdnje kao potvrđene prije dovoljno primarnog provjeravanja. Njegov raniji opis offline arhitekture bio je jači od stvarne implementacije.

## **KIMI**

Koristan dio: Vrlo praktičan compliance prikaz. Dobro je organizirao ScribeHow, ZPPI zahtjeve, zahtjeve za EWC, AMS i neovisno mjerenje.

Korekcija: Previše je puta tretirao “immutable ledger” kao već izveden sustav. Pravno je preširoko opisivao učinak statusa oštećenika i Aarhusa.

## **GROK**

Koristan dio: Najčitljivije je preveo tehničku arhitekturu građanima i jasno opisao delta alarm i Streamlit tijek.

Korekcija: Prebrzo je iz copyrighta izvlačio zaključak o identičnom CityX backendu. Također je korelacije između financija i okoliša previše približio zaključku o nepravilnosti.

## **DEEPSEEK**

Koristan dio: Jasan opis osnovnog rada alata i laka objašnjenja za građane.

Korekcija: Ponavljao je 148, 19.013 t, 124 € i 36 m kao da je dokazni status jednak. Također je dao postotke učinkovitosti koji nemaju metodološku osnovu.

## **PRETHODNI CHATGPT MATERIJALI**

Koristan dio: Doprinijeli su velikom 20-poglavnom compliance dokumentu i prepoznali potrebu da se simulacija odvoji od stvarne cenzure.

Korekcija: U ranijim verzijama i sam sam prešao granicu dokazivog u nekoliko formulacija. Ovaj završni dokument to korigira.

## **PRIJATELJEV AI CHAT**

Koristan dio: Najkorisniji novi prijedlog je neovisna stručna skupina sa sedam domena, vlastitim uzorkovanjem, neovisnim mjerenjima i javnim rezultatima.

Korekcija: Broj članova nije zakonska činjenica. Model je organizacijski prijedlog, ne službeno tijelo.

# **4. DODATAK: PRIJATELJEV CHAT I MODEL NEOVISNE STRUČNE SKUPINE**

Dostavljeni prijateljev chat predlaže odvojenu neovisnu stručnu skupinu za Koromačno. Predloženo je sedam područja: cementna tehnologija, kemijska karakterizacija otpada, mjerenje industrijskih emisija, kvaliteta zraka i atmosferska kemija, disperzijsko modeliranje, toksikologija i zdravstveni rizik, epidemiologija i javno zdravstvo. \[F8\]

| **Neovisna skupina ima smisla samo ako dobije pristup primarnim podacima i mogućnost vlastitog uzorkovanja. Skupina koja samo čita podatke operatera stvara drugi ured za pregledavanje papira, ne neovisnu kontrolu.** |
| - |


Konkretne zadaće koje ovaj model može obuhvatiti: kontrola svake pošiljke otpada, neovisno uzorkovanje, kontrolno mjerenje emisija, višetočkasto mjerenje imisija, neovisni model disperzije, zdravstvena procjena na stvarnim mjerenjima i javni strojno čitljiv registar rezultata.

Drugi model je građanski “Evidence Cell”, bez formalnog osnivanja tijela. Tri funkcije mogu se razdvojiti: čuvar izvornika, tehnički validator i dokumentacijski/pravni koordinator. Time građani mogu raditi neovisnu tehničku provjeru i kada službena skupina kasni.

# **5. STVARNI TRENUTNI STANJЕ GITHUB PROJEKTA**

Provjereni su trenutni javno dostupni repozitoriji preko GitHub-a. Oba repozitorija su javna i imaju aktivnu main granu. Git povijest je dokaz razvojnih događaja, ali nije dokaz broja radnih sati.

LIVE provjera je usmjerena na sadržaj aktualne main grane, a ne na jednu stariju commit-poruku. Za dokazni status kôda mjerodavan je sadržaj provjerenih datoteka.

LIVE status napomena: u provjerenom GitHub snapshotu još su vidljivi generirani artefakti poput .pyc, signatures.db, my\_risk\_oibs.json i temp\_dashboard\_chart.png. .gitignore pravila postoje, ali sama pravila ne uklanjaju već praćene datoteke. Ovo je repository-hygiene pitanje, a ne dokaz funkcionalnog kvara jezgre.

| **Stvar u repozitoriju** | **Nalaz nakon zadnjeg MVP polish passa** |
| - | - |
| **transparency\_reconciler.py** | **Aktualni kôd sadrži stvarni SHA-256 hash-chain i verify\_chain koji rekalkulira lanac.** |
| **app.py** | **Aktualni kôd računa SHA-256 nad uploadom, ima označenu simulaciju 15.000 € i prošireni manifest 2.0.0-Hardened.** |
| **forensic\_core.py** | **Benford χ² je korigiran na frekvencije opaženih i očekivanih vrijednosti. Statistika ostaje screening alat.** |
| **ConsensusLedger.sol** | **Pametni ugovor je prisutan. Nema javno potvrđenog produkcijskog deploymenta samo iz koda.** |
| **p2p\_network\_mesh.py** | **P2P mehanizam koristi OFFF\_HMAC\_SECRET iz okruženja i ne pokreće se bez tajne.** |
| **requirements.txt** | **Prisutan je i sadrži runtime biblioteke glavne aplikacije.** |
| **Generirani artefakti** | **U snapshotu su još vidljivi .pyc, signatures.db, my\_risk\_oibs.json i privremena slika. Ovo je cleanup zadatak.** |
| **361-lanac.html** | **Ostaje povijesni/konceptualni sloj i ne miješa se s lokalnom dokaznom matricom Koromačna.** |


# **6. NEOVISNA TEHNIČKA DISekCIJA OFFF-A**

## **6.1 transparency\_reconciler.py**

calculate\_audit\_delta(konto, expected, observed) pretvara očekivani i promatrani iznos u numeričke vrijednosti i vraća delta. To je korisna funkcija, ali sama po sebi ne zna je li “expected” iznos stvarno službeni. Zbog toga svaki expected mora imati izvorni dokument i provenance.

Aktualna verzija transparency\_reconciler.py sada sadrži stvarni SHA-256 lanac: payload se kanonizira, prethodni hash ulazi u izračun, a verify\_chain ponovno računa i uspoređuje svaki blok. Stari mock\_hash nalaz pripada prethodnoj verziji i ne opisuje aktualni kod.

Aktualni kod više ne koristi hardkodirani BLOCKCHAIN\_PRIVATE\_KEY. Vjerodajnice su predviđene kroz environment varijable. Eventualni stvarni ključ koji je nekad bio javno objavljen morao bi se zasebno rotirati.

## **6.2 app.py i simulacija cenzure**

app.py izračunava stvarni SHA-256 nad uploadanom datotekom. To je ispravan način vezivanja lokalne kopije uz hash. U alarmnom dijelu aplikacija stvara df\_alarm kao kopiju podataka. Ako je checkbox aktivan, prvi red sa kontom 3233 ili 3237 smanjuje se za 15.000 €. Aplikacija zatim prikazuje VARIANCE DETECTED i DELTA 15.000 €.

| **To je test alarma. Nije dokaz da je Grad Labin sakrio 15.000 €. U konačnoj javnoj verziji checkbox treba nositi oznaku “SIMULACIJA” na istom mjestu gdje se prikazuje alarm.** |
| - |


Još jedna bitna činjenica: hash koji se prikazuje u tom dijelu app.py jest SHA-256 trenutnog CSV zapisa df\_mock. To nije isto što i verifikacija hash-lanca iz transparency\_reconciler.py.

## **6.3 forensic\_core.py, Benford problem**

BenfordTest.run je u aktualnoj verziji prebačen na frekvencije opaženih i očekivanih znamenki. Time je uklonjen raniji problem skale χ². Rezultat ostaje statistički screening signal i ne dokazuje istinitost izvornog računovodstva.

| **Aktualni Benford status: prethodni 0.0134 bio je iz stare skale. Aktualni kod računa χ² iz opaženih frekvencija. Rezultat treba tumačiti kao statistički indikator, ne kao dokaz potpune odsutnosti manipulacije.** |
| - |


Druga granica je izbor uzorka. Kod zahtijeva najmanje 50 pozitivnih vrijednosti, ali Benford analiza može biti statistički nestabilna na malim uzorcima. Treba koristiti veće i smisleno homogene skupove podataka i izbjegavati miješanje različitih populacija transakcija.

ShannonEntropyTest također nije dokaz manipulacije. Prag 3.0 je programska odluka, a rezultat ovisi o tekstualnom prikazu brojeva, decimalama i načinu normalizacije. Koristan je kao heuristika za dodatni pregled, ne kao presuda.

DataNormalizer odbacuje vrijednosti manje ili jednake nuli. Za pojedine računovodstvene baze negativni iznosi i nule mogu biti legitimni storno ili korektivni zapisi. Takvo odbacivanje treba biti eksplicitno i dokumentirano.

# **7. KAKVA JE ARHITEKTURA KOJA STVARNO POSTOJI**

| **Sloj** | **Implementacija** | **Stvarni status** |
| - | - | - |
| **Ulaz podataka** | **CSV, auto\_adapter, lokalna obrada** | **Operativno. Mrežni API i vanjski izvori moraju se zasebno verificirati.** |
| **Normalizacija** | **auto\_adapter.py, DataNormalizer** | **Operativno. Testovi pokrivaju hrvatski i američki oblik brojeva.** |
| **Reconciliation** | **transparency\_reconciler.py** | **Operativno. Provenance i hash-chain su ojačani u aktualnoj verziji.** |
| **Statistika** | **forensic\_core.py** | **Operativna heuristika. Benford χ² je korigiran, ali ne predstavlja dokaz istinitosti podataka.** |
| **Dokazni hash** | **app.py SHA-256** | **Operativno za konkretnu datoteku.** |
| **Hash-chain ledger** | **append\_hash\_ledger / verify\_chain** | **Implementirano na razini koda i testirano na promjeni payload-a, redoslijedu i brisanju zapisa.** |
| **P2P** | **p2p\_network\_mesh.py** | **Lokalni P2P mehanizam postoji. Ne predstavlja dokaz javnog globalnog validator-mesha.** |
| **Blockchain** | **ConsensusLedger.sol** | **Pametni ugovor postoji. Nema javno verificiranog produkcijskog deploymenta u ovom pregledu.** |
| **IPFS** | **roadmap i README** | **Opis arhitekture postoji. Aktualna produkcijska dostupnost pojedinog endpointa nije ovim dokumentom potvrđena.** |


Zaključak arhitekture nakon zadnjih izmjena: riječ je o local-first građanskom audit MVP-u s operativnim SHA-256 hashiranjem datoteke, implementiranim hash-chainom, testovima integriteta, provenance manifestom i lokalnim P2P mehanizmom. P2P i blockchain sloj treba opisivati kao implementirane/prototipne komponente, a ne kao javno dokazanu globalnu mrežu validatora ili produkcijski blockchain.

# **8. IZVORNA SUO EKONERG I-03-1212, TEHNIČKA PROVJERA**

Dostavljena izvorna SUO studija ima 801 stranicu. Naslov zahvata je dekarbonizacija tvornice cementa u Koromačnu kroz izgradnju sustava za hvatanje ugljikova dioksida, s ciljem proizvodnje ugljično neutralnog cementa. Naručitelj je Holcim Hrvatska d.o.o., a ovlaštenik EKONERG d.o.o. \[F9\]

| **Nalaz iz SUO-a** | **Status** | **Što treba dalje provjeriti** |
| - | - | - |
| Dva spremnika po 3.000 m³, ukupno 6.000 m³ | FAKT | Za javne tekstove koristiti m³, ne t. |
| 16 bar(a), približno -29,4 °C | FAKT | Provjeriti konačni projekt i promjene u novoj verziji. |
| Poglavlje 1.4.5 transport i trajno skladištenje CO₂ izvan opsega zahvata | FAKT | U novoj proceduri provjeriti cjelokupni logistički lanac i pravni tretman prekograničnih učinaka. |
| Transport prema Ravenna CCS, brodovi oko 4.300 m³ | DOKUMENTIRANO U SUO-u | Provjeriti konačne tipove plovila, rutu i mjere sigurnosti. |
| QRA scenariji 50.000 i 100.000 ppm | FAKT O MODELU | Ne izjednačavati s prognozom stvarnog incidenta. |
| Tekstualni opis 100.000 ppm i Tablica 4.20-18 daju različit zaključak o stambenom području | INDIKACIJA KONTRADIKCIJE | Tražiti službeno pojašnjenje autora studije. |
| ALARP klasifikacije u QRA-u | FAKT O STUDIJI | Provjeriti kriterije, ulazne pretpostavke i neovisnu recenziju. |


Kod izvorne SUO studije treba biti posebno oprezan s ranijim tvrdnjama poput “salami slicing”, “greenwashing” ili “namjerno”. Sama činjenica da je određeni element izvan opsega jednog postupka jest dokumentirana. Zaključak da je to učinjeno s namjerom izbjegavanja procjene traži zasebnu pravnu i tehničku analizu cjelokupnog režima.

# **9. TOKOVI OTPADA: KAKO ZATVORITI LANAC**

Dostavljeni materijali ispravno upozoravaju da se različiti tokovi ne smiju automatski spajati. To je jedna od najvažnijih metodoloških lekcija projekta.

| **Tok** | **Status u korpusu** | **Dokument koji nedostaje za zatvaranje lanca** |
| - | - | - |
| Gospić, oko 650 t | FAKT da postoji odluka o zbrinjavanju dijela otpada, ali konkretni EWC i svaki ulaz moraju se zasebno potvrditi. | EWC po pošiljci, vaga, CMR, ulazna analiza, odbijena/prihvaćena šarža, krajnji tok. |
| Gospić, veća opasna frakcija | ODVOJENO OD 650 t | Dokumentacija o točnoj klasifikaciji i odredištu. |
| Italija, povijesni R1 tokovi | DOKUMENTIRANO U DOSJEU ZA POVIJESNE POŠILJKE | Za aktualnu 2026. tvrdnju treba nova dokumentacija. |
| Kaštijun/Pazin → Koromačno | HIPOTEZA | Konkretni podaci o količini, datumu, dobavljaču, prijevozniku i odredištu. |
| 19.013 t + 124 € | OTVORENO | Carinske deklaracije, notifikacije, CMR, fakture, vage i računovodstveni zapis. |


Forenzički lanac treba izgledati ovako: izvor → klasifikacija → masa → prijevoz → ulaz u postrojenje → analiza → procesni zapis → emisije → završna evidencija. Ako jedna karika nedostaje, zapis se vodi kao nepotpun, ne kao dokaz manipulacije.

# **10. STANJE NA TERENU, 29.09.2026.**

| **Događaj** | **Čvrsto potvrđeno** | **Granica izvora** |
| - | - | - |
| 22.09.2026. Gradsko vijeće Labina | Jednoglasno usvojen zaključak: preporuka Vladi da ukine odluku 10.09. o oporabi otpada iz Gospića u Holcimu, kontinuirana mjerenja, hermetički zatvoren transport ako ga bude, poseban fond za neovisna mjerenja. \[W2\] | Iza ovog zaključka nije automatski pravni učinak zabrane rada tvornice. |
| 28.09.2026. Radna skupina | Traži od FZOEU-a, DIRH-a i Holcima dokumente i postavlja rok od pet radnih dana. \[W3\] | Medijski izvještaj prenosi zaključke skupine. Za dokazni paket čuvati službeni zapisnik/zaključak kad bude objavljen. |
| 28.09.2026. MO Koromačno | Objavio “Apsolutno NE” prema KOdeCO i šest zahtjeva vezanih uz otpad, mjerenje i transparentnost. Istodobno izričito navodi da MO nema ovlasti donositi odluke. \[W4\] | To je službeno očitovanje MO-a, ne upravni akt koji sam zaustavlja projekt. |
| 28.09.2026. sastanak Kapelica | Objavljeni izvještaj opisuje prometnu sigurnost, kamere, pješačke prijelaze, nogostup i kružni tok. U tom objavljenom izvještaju KOdeCO nije spomenut. \[W5\] | Izostanak iz objavljenog izvještaja ne dokazuje da se tema nije spomenula izvan izvještaja. |
| Blokade/prosvjedi | Lokalni mediji izvještavaju o blokadama kamiona i kasnijoj blokadi ulaza u tvornicu. \[W6\] | Broj sudionika, trajanje i uzročni učinak na odluke treba vezati uz svaki pojedinačni događaj. |


# **11. LABINSKI SUSTAV TRANSPARENTNOSTI I CITYX**

Grad Labin na svojoj službenoj stranici objavljuje uslugu transparentnosti proračuna. GitHub dosje i lokalni materijali sadrže OSINT tvrdnju da se na aktivnim endpointima vidi “© 2026 CityX Apps d.o.o.”. U ovoj rundi nisam mogao neovisno dohvatiti production endpoint transparentor.org kroz web alat, pa ta oznaka ostaje INDIKACIJA, ne potvrđena činjenica.

| **Pitanje** | **Dokument koji treba dobiti** |
| - | - |
| Koji softver i verzija danas generiraju javni portal? | Naziv proizvoda, verzija, release date, URL/API base. |
| Tko je ugovorni dobavljač? | Ugovor, aneksi, održavanje, SLA, račun. |
| Koji je source of truth? | Glavna knjiga, data warehouse, portalna baza ili API. |
| Postoji li audit log? | Korisnik, vrijeme, stara vrijednost, nova vrijednost, razlog. |
| Kako se radi javni export? | Opisni postupak i primjer izvornog CSV-a. |
| Kako je dokazana nepromjenjivost? | Originalni hash, datum hashiranja, neovisno sidro. |


| **Tri pitanja za sastanak: 1. Ako današnji portal nije CityX Transparentor, koji točno proizvod, verzija, API i hosting danas generiraju podatke i zašto se na endpointu pojavljuje CityX copyright? 2. Može li Grad pokazati originalni SHA-256 glavne knjige i javnog exporta istog skupa podataka? 3. Postoji li audit log svih izmjena javnih transakcija sa starom i novom vrijednošću?** |
| - |


# **12. PRAVNI I PROCEDURALNI OKVIR, ISPRAVLJENO**

Zakon o prostornom uređenju propisuje da u javnoj raspravi o prijedlogu prostornog plana može sudjelovati svatko. Zakon također određuje sadržaj izvješća o javnoj raspravi i obrazloženje neprihvaćenih primjedbi. \[L1\]

Za ovaj slučaj ključno je odvojiti dva postupka. SUO za KOdeCO bila je jedna procedura, dok V. izmjene PPUO Raša predstavljaju zaseban prostorno-planski postupak. Javna rasprava o SUO-u je obustavljena nakon povlačenja zahtjeva investitora. To ne znači da nova prijava nije moguća. \[W1\]

Zakon o pravu na pristup informacijama propisuje 15 dana za odlučivanje o urednom zahtjevu, uz mogućnost produljenja u zakonom predviđenim situacijama. Protiv rješenja i zbog šutnje postoji žalba Povjereniku za informiranje u skladu s člankom 25. \[L2\]

ZKP čl. 55 uređuje situaciju u kojoj državni odvjetnik utvrdi da nema osnova za progon. Tada se oštećenik obavještava i može pod zakonskim uvjetima sam poduzeti ili nastaviti progon u roku od osam dana od primitka obavijesti. Samoizjašnjavanje osobe u prijavi ne stvara automatski procesni status oštećenika. \[L3\]

Aarhuška konvencija daje važna prava javnosti u okolišnim postupcima, ali nije točno da su svi okolišni podaci bez iznimke pravno nezaštićeni od svakog ograničenja. Za svaki zahtjev treba primijeniti konkretna pravila pristupa informacijama i eventualnih iznimaka.

| **Pravno najčišći put nije “proglasiti projekt nezakonitim”, nego dokumentirati konkretan procesni propust, tražiti konkretan akt, zatražiti pravni lijek koji pripada baš tom aktu i čuvati rokove.** |
| - |


# **13. PUTOVI KOJIMA SE MOŽE OSPORAVATI NOVA FAZA KOdeCO**

Ne postoji jedan gumb kojim građani mogu zaustaviti projekt. Nova faza mora proći više međusobno povezanih procedura. Svaki od njih proizvodi zasebnu mogućnost provjere i pravnog osporavanja, ovisno o konkretnom aktu.

## **A. Prostorni plan**

Pratiti konačni prijedlog V. izmjena PPUO Raša, izvješće o javnoj raspravi, karte, tekstualne odredbe i mišljenje županijskog zavoda. U svakoj primjedbi navesti točan članak, kartu, lokaciju ili nedostajući podatak. \[L1\]

## **B. Nova PUO/SUO**

Tražiti cijelu novu studiju, tehničke podloge, QRA, ulazne podatke, meteorologiju, disperzijski model, scenarij bez zahvata i rezultate neovisne recenzije.

## **C. Okolišna dozvola**

Provjeriti koje EWC kodove, granične vrijednosti i monitoring dopušta važeća okolišna dozvola. Ministarstvo vodi javnu dokumentaciju o Holcimu i njegovim izmjenama. \[W7\]

## **D. Inspekcija**

Za svako prekoračenje vezati datum, vrijednost, mjerno mjesto, GVE, zapisnik inspektora i korektivnu mjeru. Ne oslanjati se samo na graf ili screenshot.

## **E. ZPPI**

Zahtijevati raw AMS, vage, EWC, ulazne analize, inspekcijske spise i ugovore. Svaki zahtjev voditi zasebno i pratiti rokove. \[L2\]

## **F. Upravni lijekovi**

Ako se donese konkretan rješenje ili drugi osporivi akt, vrstu žalbe ili upravnog spora treba vezati uz taj akt i procesni položaj podnositelja. Za odgodni učinak ili privremenu mjeru treba procjenu odvjetnika prema konkretnom postupku.

# **14. HITNI PAKET, ROK OD PET RADNIH DANA**

Radna skupina je 28.09.2026. od FZOEU-a, DIRH-a i Holcima zatražila dokumentaciju te postavila rok od pet radnih dana. \[W3\] To stvara vrlo konkretan forenzički zadatak za građanski dosje.

| **Institucija** | **Traženo** | **MARA obrada nakon primitka** |
| - | - | - |
| FZOEU | Analize otpada iz big-bag vreća i plan sanacije PPK Gospić | Hash svakog dokumenta, EWC/matrica analize, usporedba uzoraka. |
| DIRH | Svi nadzori Holcima 2025. i 2026., posebno nakon pretkalcinatora | Kronologija inspekcija, nalaza, GVE, mjera i izvršenja. |
| Holcim | Interne kemijsko-tehnološke analize otpada, način uporabe, dodatna mjerenja emisija, sirovi kontinuirani podaci, srednjoročni plan | Cross-check sa službenom dozvolom, laboratorijskim analizama i AMS podacima. |
| Imisijska postaja | Rezultati 30-dnevnog mjerenja u Koromačnom čim analitičko izvješće bude dostupno | Vremenska serija, meteorologija, izvori emisija, prostorna usporedba. |


# **15. SCRIBEHOW I RAD GRAĐANINA, OD NULE DO DOKAZA**

Aktualni repozitorij sada sadrži requirements.txt. Dokumentirani instalacijski postupak može se zato vezati uz stvarne runtime ovisnosti, uz napomenu da P2P čvor traži konfiguriranu HMAC tajnu.

| **Windows PowerShell ili CMD  
cd C:\\putanja\\open-fiscal-forensics  
pip install -r requirements.txt  
streamlit run app.py** |
| - |


Aktualni popis ovisnosti pokriva streamlit, pandas, matplotlib, reportlab, requests, web3 i urllib3. hashlib je dio standardne Python biblioteke i ne instalira se zasebno.

Nakon pokretanja građanin učitava izvorni CSV, upisuje metapodatke, pokreće audit, sprema rezultat i SHA-256 te čuva originalnu datoteku. Simulaciju cenzure treba koristiti samo kao test detekcije.

## **15.1 VS CODE, STATUS NAKON MVP POLISH PASSA**

1. SHA-256 hash-chain i verify\_chain: ZATVORENO u aktualnom transparency\_reconciler.py.

2. Benford χ² skala: ZATVORENO u aktualnom forensic\_core.py.

3. Private key i HMAC secret: ZATVORENO na razini izvornog koda. P2P čvor traži OFFF\_HMAC\_SECRET iz okruženja.

4. requirements.txt: ZATVORENO i usklađeno sa stvarnim importima glavne aplikacije.

5. PDF tablice: ZATVORENO. Aktualni pdf\_generator.py koristi Paragraph ćelije i wordWrap="CJK".

6. Testovi integriteta: ZATVORENO za promjenu jednog centa, redoslijed bloka i brisanje zapisa, uz provjere formata brojeva.

7. Provenance manifest: ZATVORENO na razini MVP sheme 2.0.0-Hardened, s proširenim revizorskim poljima.

8. Preostalo iz ovog tehničkog ciklusa: repository hygiene i uklanjanje već praćenih generiranih artefakata.

9. 361-lanac ostaje povijesni/idejni sloj i ne koristi se kao lokalni dokaz Koromačna.

10. Nova izmjena prolazi lokalni test, ručni pregled, commit i provjeru javnog repozitorija.

11. Statistički rezultat nije dokaz kaznene odgovornosti niti potpune vjerodostojnosti izvornog računovodstva.

12. Svaka nova materijalna tvrdnja dobiva dokazni status i primarni izvor.

## **15.2 VS CODE, PREOSTALI REPOSITORY HYGIENE**

Preostali VS Code posao nakon zatvorenog MVP hardeninga je repository hygiene. Ne dirati funkcionalnu jezgru bez konkretnog razloga i testa.

A. Ukloniti već praćene .pyc, signatures.db, my\_risk\_oibs.json i generirane privremene slike iz Git repozitorija, ne samo iz lokalnog direktorija.

B. Provjeriti git history za eventualne stvarne tajne. Ako je stvarni tajni ključ ikada bio commitan, treba ga rotirati i procijeniti potrebu za čišćenjem povijesti.

C. forenzika i Benford više nisu otvorena popravka. Dalje se samo provjerava regresija testovima.

D. P2P sigurnosna promjena je ugrađena. Ostaje samo provjera da je OFFF\_HMAC\_SECRET postavljen u stvarnom okruženju prije pokretanja noda.

E. Reorganizaciju /src /contracts /data /public /archive provesti tek nakon provjere svih importova, relativnih putanja i GitHub Pages linkova.

F. .gitignore pravila postoje, ali već praćeni artefakti moraju se zasebno ukloniti iz Git repozitorija.

G. requirements.txt je sada prisutan i treba ostati sinkroniziran s importima aplikacije.

H. Provenance manifest je proširen na MVP shemu 2.0.0-Hardened. Nove izvore treba puniti stvarnim, a ne fiksnim primjerima.

I. Testovi integriteta su dodani. Nakon novih izmjena treba pokrenuti regresijski paket i ručno pregledati rezultat.

J. VS Code dnevni red ostaje: git status → promjena → lokalni testovi → ručni pregled → commit → push → provjera GitHuba.

# **16. UČINKOVITOST PROJEKTA, BEZ POLITIČKOG BODOVANJA**

Raniji AI dokumenti koriste postotke poput 65/35 ili 85/15. Takvi postoci nemaju empirijsku metodu i ne koriste se u ovom završnom izvještaju. Umjesto toga, učinak se može mjeriti stvarnim ishodima.

| **Mjerilo** | **Što postoji** | **Kako mjeriti dalje** |
| - | - | - |
| Razvojni rad | **Javni Git commit tragovi kroz dva repozitorija** | **Broj kvalitetnih funkcija, testova, source-level corrections i izdanja.** |
| Dokumentacijski rad | Brojni PDF/MD dokumenti, evidence matrix, pravni predlošci | Broj primarnih izvora po tvrdnji i zatvorenih dokaznih karika. |
| Institucionalni odgovor | Gradsko vijeće Labina donijelo jednoglasni zaključak. Radna skupina 28.09. traži podatke i daje rok. \[W2\]\[W3\] | Broj dostavljenih dokumenata, kvaliteta podataka i rokovi odgovora. |
| Javna transparentnost | GitHub i web dosje dostupni javnosti | Broj ažuriranih izvora sa hashom i dokaznim statusom. |
| Terenski pritisak | Dokumentirane blokade i javna okupljanja. \[W6\] | Broj događaja, službeni zapisnici i konkretne institucionalne reakcije. |
| Pravna kvaliteta | ZPPI obrasci, zahtjev za statusom, predložak kaznene prijave | Broj pravilno formuliranih podnesaka i procesnih odgovora. |


Što se može dokazati: inicijativa je proizvela stvarnu količinu softvera, dokumentacije i javne infrastrukture. Što se ne može dokazati samo tim činjenicama: da je upravo inicijativa uzrokovala svaki pojedini odgovor institucija ili svaku odluku investitora.

# **17. LJUDSKI RAD I AI, ŠTO SE STVARNO MOŽE REĆI**

GitHub daje provjerljiv trag razvojnih događaja, ali ne omogućuje zaključivanje o broju radnih sati bez zasebnog vremenskog dnevnika.

Također, nema osnove tvrditi da je AI samostalno proveo terensku istragu. AI modeli su analizirali materijale, a operativni rad, prikupljanje linkova, učitavanje dokumenata, terenska opažanja i GitHub izmjene potječu iz ljudskog projekta. U završnom dosjeu AI treba biti tretiran kao analitički pomoćnik, ne kao svjedok, istražitelj ili izvor primarnih činjenica.

# 18. JEDINSTVENA ALL-IN DOKAZNA MATRICA

Ova matrica je jezgra projekta. Ona razdvaja tvrdnje koje ranije AI analize često spajaju u jednu rečenicu.

| **Tvrdnja / pitanje** | **Status** | **Što imamo** | **Što treba** |
| - | - | - | - |
| Holcim je 28.08.2026. odustao od tadašnjeg PUO zahtjeva. | FAKT | Službena obavijest Županije i rješenje Ministarstva. \[W1\] | Sačuvati izvorni akt u evidence vaultu. |
| Nova studija treba biti usklađena s PPUO Raša. | DOKUMENTIRANA TVRDNJA | Holcimova javna komunikacija. | Nova studija i konačni plan. |
| V. PPUO izmjene povezane su s industrijskom zonom i lučkom infrastrukturom. | DOKUMENTIRANO U PLANERSKOM KORPUSU | Službena planerska dokumentacija. | Konačni prijedlog i konačne karte. |
| Projekt ima dva spremnika po 3.000 m³. | FAKT | Izvorni SUO. \[F9\] | Samo provjera nove verzije. |
| Projekt ima 6.000 tona spremnika. | POGREŠNO MJERNO IZRAŽAVANJE | Raniji AI tekstovi. | Koristiti 6.000 m³ dok se masa ne računa iz provjerenih gustoća. |
| Transport CO₂ izvan opsega SUO. | FAKT O DOKUMENTU | Poglavlje 1.4.5. \[F9\] | Pravna ocjena ukupnog lanca. |
| 100.000 ppm ne doseže stanovanje. | KONTRADIKCIJA | Tekstualni dio i Tablica 4.20-18 nisu međusobno usklađeni. | Formalni odgovor autora SUO/QRA. |
| 50.000 ppm scenarij doseže stanovanje. | FAKT O MODELU | QRA tablica/scenarij. | Neovisni peer review ulaza modela. |
| R1 ulazi 29.800-32.800 t/god. | DOKUMENTIRANO U SUO / RADNIM ANALIZAMA | Tablica i analiza. | Potvrda iz evidencije stvarnih ulaza. |
| 19 12 10 dominira s 20.700-22.100 t/god. | DOKUMENTIRANO U RADNIM MATERIJALIMA | SUO/radna analiza. | Provjera po godinama i KBO zapisima. |
| Gospić 650 t je neopasan otpad. | DOKUMENTIRANO | Vladina odluka i lokalni akti. | Točan EWC i originalne analize po šarži. |
| Svi EWC kodovi Gospić su 19 12 04/10/12. | OTVORENO | AI dokumenti navode ih kao moguće kodove. | Službeni EWC kod svake pošiljke. |
| 19.013 t talijanskog otpada ušlo je za 124 €. | OTVORENO | Ponovljena tvrdnja u radnim dokumentima. | Carina, notifikacije, CMR, račun, vaga. |
| Kaštijun/Pazin generiraju tok koji je preusmjeren u Koromačno. | HIPOTEZA | Regionalna vremenska i kapacitetna korelacija. | Primarni transportni i ugovorni podaci. |
| CityX copyright dokazuje isti backend. | INDICIJA | OSINT/screenshot navod. | HTTP, DNS, TLS, API, ugovor, deployment. |
| Grad ima nepromjenjivi hash-ledger. | OTVORENO | Konceptualna dokumentacija. | Prava chain validacija u produkciji. |
| 15.000 € je stvarno skriveno. | SIMULACIJA | UI checkbox scenarij. | Primarni računovodstveni dokaz, ako takav događaj postoji. |
| 148 TOC prekoračenja. | DOKUMENTIRANA TVRDNJA / INDIKACIJA | Lokalni zapisnici i radni dosjei. | RAW AMS, datum, mjerno mjesto, GVE. |
| Emisije su se povećale 10-15x zbog pretkalcinatora. | DOKUMENTIRANA TVRDNJA | Izjave na lokalnim sjednicama. | Sirove usporedive vrijednosti i metodologija. |
| Zdravstveni učinci dr. Mohorovića potvrđuju štetu u Koromačnom. | OTVORENO | Navodi u radnim tekstovima. | Originalne znanstvene publikacije i lokalni epidemiološki podaci. |
| “Greenwashing” je dokazan. | NIJE DOKAZANO | Interpretacija u AI dokumentima. | Dokumentirani marketinški claim + ekspertna analiza, uz pravnu rezervu. |
| Status oštećenika automatski nastaje prijavom. | POGREŠNO | Raniji AI pravni tekstovi. | Primjenjivati ZKP prema konkretnom procesnom položaju. |
| Aarhus znači da okolišni podaci nikad ne smiju imati iznimku. | PREŠIROKO | Raniji AI tekstovi. | Primjena konkretnog ZPPI/okolišnog postupka. |


# 19. KONAČNI NEOVISNI PRIJEDLOZI MARA

## 1. Pretvori MARA-u u dokazni registar, ne u generator optužbi.

Svaki nalaz mora imati izvor, hash, datum, status dokaza i osobu koja ga je provjerila.

## 2. Napravi dvije odvojene baze.

Financijski ledger i environmental ledger trebaju ostati odvojeni, a povezivati se preko datuma, projekta, dobavljača, OIB-a, lokacije, ugovora i drugog provjerljivog ključa.

## 3. Uvedi two-person rule za objavu.

Jedna osoba provjerava dokument, druga provjerava formulaciju zaključka. Tek tada ide javna objava.

## 4. Uspostavi evidence vault.

Originalni PDF/CSV, SHA-256, URL, vrijeme preuzimanja i verzija izvora čuvaju se nepromijenjeni.

## 5. Funkcionalni OFFF hardening je proveden. Prije novih funkcija prioritet je repository hygiene i dokumentacijska sinkronizacija.

Hash-chain, Benford formula, requirements.txt, secrets, testovi i provenance već su funkcionalno obrađeni. Prije novih funkcija prednost sada imaju repository hygiene i sinkronizacija dokumentacije.

## 6. 361-lanac zadrži, ali ga izoliraj.

To je dio povijesti i koncepta projekta. Globalne tvrdnje ne smiju se pojavljivati kao dokaz Koromačna.

## 7. Prioritet prvih pet radnih dana ostaju stvarni dokumenti: FZOEU, DIRH i Holcim podaci koje Radna skupina traži. \[W3\]

Sve ostalo je sekundarno dok ne stignu FZOEU, DIRH i Holcim podaci koje Radna skupina traži. \[W3\]

## 8. Neovisna stručna skupina ima smisla kao kontrolni sloj.

Ali mora imati neovisno uzorkovanje i laboratorijsko mjerenje. Ako nema pristup sirovim podacima, njen učinak je ograničen.

## 9. Građani mogu raditi bez čekanja posebnog odbora.

Open-source alati, ZPPI i javni postupci već daju dovoljno infrastrukture za vlastiti dokazni registar. Službena tijela i građanski alat imaju različite funkcije.

## 10. Pravna komunikacija mora ostati hladna.

Izbaciti privatni život, motive, “oligarhiju”, “ucjenu”, “greenwashing” i “dokazani umišljaj” iz činjeničnog dijela gdje ne postoji primarni dokaz.

# 20. 0-5-30-90 RADNI MODEL

| **Razdoblje** | **Zadatak** | **Izlaz** |
| - | - | - |
| 0-5 radnih dana | Zaprimiti i arhivirati sve odgovore FZOEU, DIRH, Holcim. | Hashirani source package + prva discrepancy tablica. |
| 6-14 dana | Usporediti AMS, vage, EWC, laboratorijske analize i inspekciju. | Kronologija i zatvaranje otvorenih karika. |
| 15-30 dana | Peer review QRA i planerskih promjena. | Neovisne tehničke primjedbe s izvorima. |
| 31-90 dana | Pripremiti dokumentacijski paket za novu PUO/PPUO proceduru i pravne lijekove gdje je primjenjivo. | Versioned dossier 2.0 sa svim primarnim izvorima. |


# 21. REGISTAR IZVORA

| **ID** | **Izvor** | **Status u ovom dokumentu** |
| - | - | - |
| F1 | DeepSeek AI: “Kako nadzirati proračun i okoliš: MARA, OFF i borba protiv KOdeCO Net Zero”. | AI radni materijal, sekundarni izvor. |
| F2 | Grok AI: “Izvješće građanima Labina: Arhitektura OFFF / MARA…”. | AI radni materijal, sekundarni izvor. |
| F3 | KIMI AI: “Izvještaj o usklađenosti i mobilizacijski dokument”. | AI radni materijal, sekundarni izvor. |
| F4 | MARA “Forenzička disekcija SUO Lipanj 2026, I-03-1212, EKONERG za Holcim”. | Radna analiza izvornog SUO-a. |
| F5 | Strateški Riziko-Matrix: Koromačno & Raša. | Radna hipotezna matrica. |
| F6 | Spajanje tokova materijala: Kaštijun, Pazin i Holcim. | Radna analiza tokova. |
| F7 | Akcija Češalj, strateška forenzička analiza i unakrsno povezivanje. | Korisnički zadatak i radni korpus, s nedokazanim tvrdnjama izdvojenim. |
| F8 | Prijateljev AI chat “Nakon ALL IN dokumenta…”. | Sekundarni prijedlog neovisne stručne skupine. |
| F9 | SUO Dekarbonizacija tvornice cementa u Koromačnu, EKONERG I-03-1212, Lipanj 2026., 801 stranica. | Primarni tehnički izvor. |
| G1 | https://github.com/Zeljk018Bratic/open-fiscal-forensics | Primarni izvor za stanje koda i Git povijest. |
| G2 | https://github.com/Zeljk018Bratic/dosje-koromacno | Primarni izvor za javni dosje i dokumente. |
| W1 | Istarska županija, obustava javne rasprave o SUO, 02.09.2026. | Primarni službeni proceduralni izvor. https://zdrava-sana.istra-istria.hr/hr/clanci/istarska-zupanija-novosti/18075/obavijest-o-obustavi-postupka-javne-rasprave-o-studiji-utjecaja-na-okolis-za-zahvat-dekarbonizacije-tvornice-cementa-u-koromacnu-kroz-izgradnju-sustava-za-hvatanje-ugljikovog-dioksida-s-ciljem-proizvodnje-ugljicno-neutralnog-cementa-opcina-rasa-istarska-z/ |
| W2 | Gradsko vijeće Labina, zaključak 22.09.2026., zaštita zdravlja i okoliša. | Sekundarni medijski prijenos uz službenu gradsku objavu sjednice. https://5portal.hr/vijesti\_detalj.php?id=60413 |
| W3 | Glas Istre, zaključak Radne skupine 28.09.2026., pet radnih dana. | Aktualni medijski izvor s konkretnim sadržajem zahtjeva. https://www.glasistre.hr/istra/2026/09/28/zakljucak-radne-skupine-za-pracenje-kvalitete-zraka-u-okolici-tvornice-u-koromacnu-nadlezne-institu-1086231 |
| W4 | Mjesni odbor Koromačno, očitovanje 28.09.2026. | Aktualno lokalno očitovanje. https://5portal.hr/vijesti\_detalj.php?id=60481 |
| W5 | Sastanak gradonačelnika i MO Kapelica 28.09.2026. | Aktualni lokalni medijski izvještaj. https://labinstina.info/vijesti/129716-raspravljalo-se-o-pjesackim-prijelazima-i-novom-kruznom-toku-ni-rijeci-o-nedavnoj-blokadi-ceste |
| W6 | Izvještaji o blokadi ulaza u Holcim 28.09.2026. | Aktualni lokalni medijski izvor. https://labinstina.info/vijesti/129679-raste-napetost-u-koromacnu-prosvjednici-blokirali-tvornicu-zatvorit-cemo-spalionicu-borit-cemo-se-do-gole-koze |
| W7 | MZOZT, Holcim Hrvatska d.o.o., okolišne dozvole. | Primarni službeni izvor. https://mzozt.gov.hr/o-ministarstvu-1065/djelokrug/uprava-za-procjenu-utjecaja-na-okolis-i-odrzivo-gospodarenje-otpadom-1271/okolisna-dozvola/okolisne-dozvole/holcim-hrvatska-d-o-o-koromacno/7234 |
| L1 | Zakon o prostornom uređenju, NN 155/2025. | Primarni pravni izvor. https://narodne-novine.nn.hr/clanci/sluzbeni/full/2025\_12\_155\_2315.html |
| L2 | Zakon o pravu na pristup informacijama, NN 25/2013 s izmjenama. | Primarni pravni izvor. https://narodne-novine.nn.hr/clanci/sluzbeni/2013\_02\_25\_403.html |
| L3 | Zakon o kaznenom postupku, pročišćeni tekst, čl. 55. | Primarni pravni izvor za citirani mehanizam čl. 55. https://narodne-novine.nn.hr/clanci/sluzbeni/2011\_10\_121\_2386.html |
| **F22** | **Korisnički dostavljeni tekst: „KOROMAČNO – Park prirode ili teška industrija“ (29.09.2026.)** | **Sekundarni/strateški izvor. Povijesni, prostorni i komunikacijski sloj. Materijalne tvrdnje zatvoriti primarnim izvorima prije pravne uporabe.** |


# 22. JAVNE POVEZNICE ZA NASTAVAK REVIZIJE

OFFF GitHub: [https://github.com/Zeljk018Bratic/open-fiscal-forensics](https://github.com/Zeljk018Bratic/open-fiscal-forensics)

Koromačno dosje GitHub: [https://github.com/Zeljk018Bratic/dosje-koromacno](https://github.com/Zeljk018Bratic/dosje-koromacno)

Interaktivni dosje: [https://zeljk018bratic.github.io/dosje-koromacno/](https://zeljk018bratic.github.io/dosje-koromacno/)

Transparentor, korisnički naveden endpoint: [https://transparentor.org](https://transparentor.org)

Transparentor API dokumentacija, korisnički naveden URL: [https://transparentor.orgapi-dokumentacija](https://transparentor.orgapi-dokumentacija)

Zatraži API ključ, korisnički naveden URL: [https://transparentor.orgzatrazi-api-kljuc](https://transparentor.orgzatrazi-api-kljuc)

Napomena o Google Docs/Drive poveznicama: one su dostavljene kao linkovi, ali sadržaj tih linkova nije bio pouzdano dohvatljiv kroz dostupni konektor u ovoj provjeri. Zato nisu korištene kao potvrđeni primarni izvori. Ako se kasnije pribave njihove datoteke, treba ih uvesti kao zasebne verzije u evidence vault, bez zamjene za već potvrđene primarne izvore.

# **23. STRATEŠKI DODATAK: KOROMAČNO 1922–2045 I PITANJE UBAŠA**

**Novi korisnički dostavljeni tekst „KOROMAČNO – Park prirode ili teška industrija“ uvodi povijesno-prostorni sloj koji u ranijem ALL-IN-u nije bio dovoljno razvijen. Povezuje industrijsku povijest Koromačna, promjene vlasništva, sadašnji KOdeCO kontekst i pitanje buduće namjene prostora. Zbog razine izvornosti, materijalne tvrdnje iz tog teksta ovdje se vode kao zaseban izvor i ne pretvaraju se automatski u činjenice.**

## **23.1 Povijesna linija cementare**

**Dostavljeni tekst navodi početak izgradnje 1922. godine, početak rada 1926., razvoj proizvodnje tijekom 1928.–1931., radničko naselje Valmazzinghi, modernizaciju 1971. i uključivanje u SOUR Istarske tvornice cementa i hidratiziranog vapna 1980. godine. Ovaj dio treba voditi kao povijesni korpus koji se potvrđuje arhivskim i industrijsko-povijesnim izvorima. Povijesna činjenica da je industrija postojala ne rješava današnji pravni i okolišni status budućih zahvata.**

## **23.2 Privatizacija i vlasnički lanac**

**Novi tekst navodi više konkretnih podataka iz privatizacije početkom 1990-ih: procjenu od 55 milijuna DEM, dokapitalizaciju od 108,43 milijuna DEM, transakciju dionica Hrvatskog mirovinskog osiguranja u iznosu 8.551.805 DEM, ulogu Jakše Barbića i njegovu kasniju funkciju u nadzornom odboru Holcima. Ovi navodi imaju visoku dokaznu vrijednost samo ako se svaki broj i svaka funkcija vežu uz konkretan privatizacijski elaborat, odluku, prospekt, vlasnički registar, godišnje izvješće, zapisnik ili drugi primarni dokument. Ne smije se iz same vremenske ili poslovne povezanosti izvlačiti zaključak o protupravnosti ili sukobu interesa.**

## **23.3 KOdeCO Net Zero kao sadašnji sloj**

**Dostavljeni tekst ponovno ističe vrijednost projekta KOdeCO Net Zero, potporu iz EU Inovacijskog fonda i cilj hvatanja i trajnog skladištenja CO₂. U ovom dosjeu primarni tehnički okvir ostaje izvorna SUO EKONERG I-03-1212, zajedno s njezinim parametrima, QRA scenarijima, transportom i prostorno-planskim postupcima. Novi tekst zato dopunjuje postojeći tehnički korpus, a ne zamjenjuje ga.**

## **23.4 Ubaš: prostorna zaštita kao zasebno pitanje**

**Novi tekst otvara pitanje Ubaša kao prirodnog i prostornog prostora koji bi mogao biti predmet snažnijeg režima zaštite, uključujući raspravu o mogućnosti proglašenja Parka prirode. Za neovisni dosje treba prvo utvrditi današnji službeni režim zaštite, granice, planske oznake, vlasničko-katastarski status i stručne podloge o prirodnim vrijednostima. Tek nakon toga može se procijeniti pravni učinak bilo kojeg novog režima zaštite na postojeće i buduće zahvate.**

**Za ovaj predmet treba razdvojiti četiri mape dokaza: službeni registar zaštite prirode, prostorni planovi, katastarsko-vlasnička dokumentacija i stručne podloge o bioraznolikosti, krajobrazu i geologiji. Sama oznaka Natura 2000 ili prijedlog Parka prirode ne treba se koristiti kao zamjena za provjeru konkretnih granica i konkretnih pravnih učinaka.**

## **23.5 Dokazna matrica novog izvora**

| **Tema** | **Status** | **Što trenutno imamo** | **Što treba zatvoriti** |
| - | - | - | - |
| **Početak gradnje 1922. / rad 1926.** | **DOKUMENTIRANA TVRDNJA** | **Novi tekst iznosi kronologiju S.P.E.M.A.** | **Arhivski/industrijski primarni izvor** |
| **Proizvodnja 1928.–1931.** | **DOKUMENTIRANA TVRDNJA** | **Navedene količine i broj radnika** | **Izvorni industrijski izvještaj ili arhivski zapis** |
| **Valmazzinghi i industrijsko naselje** | **DOKUMENTIRANA TVRDNJA** | **Opis radničkog naselja uz tvornicu** | **Povijesni plan, katastar ili arhivska dokumentacija** |
| **Fašistički almanah 1936.** | **DOKUMENTIRANA TVRDNJA** | **Navedena publikacija „Le Opere del Regime in Istria“** | **Digitalni/originalni primjerak publikacije** |
| **Modernizacija 1971. i SOUR 1980.** | **DOKUMENTIRANA TVRDNJA** | **Navodi o modernizaciji i organizacijskom uključenju** | **Industrijska kronika, odluke i organizacijski akti** |
| **Procjena 55 mil. DEM** | **OTVORENO** | **Brojka iz novog korisničkog teksta** | **Privatizacijski elaborat i odluka o procjeni** |
| **Dokapitalizacija 108,43 mil. DEM** | **OTVORENO** | **Brojka iz novog korisničkog teksta** | **Dionice, dokapitalizacijski ugovori i financijski trag** |
| **Transakcija 8.551.805 DEM** | **OTVORENO** | **Navod o dionicama Hrvatskog mirovinskog osiguranja** | **Izvorni vlasnički/financijski dokument** |
| **Barbić i funkcije u Holcimu** | **DOKUMENTIRANA TVRDNJA / OTVORENO PO SEGMENTIMA** | **Navodi o funkciji i korporativnim ulogama** | **Godišnja izvješća, registri i odluke NO** |
| **KOdeCO 116,9 mil. € / 237 mil. €** | **DOKUMENTIRANO U PROJEKTNOM KORPUSU** | **SUO + postojeći projektni materijali** | **Za javni navod vezati točan primarni dokument** |
| **Ubaš i sadašnji režim zaštite** | **OTVORENO ZA DODATNU PROVJERU** | **Novi tekst navodi Natura 2000 i šumski režim** | **Službeni registar, karte, PPUO, katastar i stručne podloge** |
| **Mogući budući Park prirode Ubaš** | **HIPOTEZA / JAVNO-POLITIČKI PRIJEDLOG** | **Novi tekst otvara mogućnost rasprave** | **Studija vrijednosti, granice, pravni model i javna procedura** |
| **Predviđanja o budućem razvoju prostora** | **HIPOTEZA** | **Novi tekst spominje više mogućih scenarija** | **Odvojene scenarijske studije i službeni planski akti** |

## **23.6 Što ovaj dodatak mijenja u ALL-IN dokaznoj logici**

**Ovaj novi sloj ne dokazuje sam po sebi nezakonitost privatizacije, kaznenu odgovornost bilo koje osobe, buduće produženje eksploatacije niti uzročnu vezu između povijesnih vlasničkih odluka i današnjeg KOdeCO projekta. Njegova vrijednost je u vremenskoj osi: industrijska povijest → vlasničke promjene → današnji okolišni i prostorni postupci → buduće pitanje namjene prostora.**

**Za javnu komunikaciju naslov „Park prirode ili teška industrija“ može služiti kao pitanje o budućem modelu prostora. Za pravni i forenzički dio precizniji oblik je: „Koji službeni režim zaštite, prostorni plan i dokazivi kriteriji trebaju odrediti buduću namjenu područja Ubaša i Koromačna?“**

# 24. ZAVRŠNI NEOVISNI ZAKLJUČAK

Projekt MARA/OFFF ima stvarnu vrijednost kao građanska infrastruktura za prikupljanje, normalizaciju, dokumentiranje i uspoređivanje javnih podataka. Nakon zadnjeg tehničkog ciklusa jezgra ima snažniji integritetni sloj: SHA-256 hashiranje datoteke, stvarni hash-chain, korigirani Benfordov izračun, testove integriteta, prošireni provenance manifest i sigurnosnu provjeru konfigurirane P2P tajne.

Najvažniji rezultat ove revizije nije nova politička interpretacija. To je razdvajanje četiri razine koje se moraju čitati odvojeno: tehnička funkcionalnost alata, vjerodostojnost izvora, pravni proces i javna komunikacija. Dodatak o povijesti Koromačna i Ubašu pokazuje da se i povijesni, vlasnički i prostorni navodi moraju voditi istim dokaznim standardom.

| **Ako želite ozbiljan dosje koji Grad, inspekcija, Ministarstvo ili DORH ne mogu lako odbaciti kao “internetsku priču”, standard treba biti jednostavan: manje velikih riječi, više originalnih dokumenata, hashova, vremenskih oznaka, sirovih podataka, neovisnih mjerenja i precizno formuliranih pitanja.** |
| - |


Ovaj završni dokument ne daje politički poredak kandidata, institucija, prosvjeda ili razvojnih modela. Daje dokazni okvir. Za svaki sporni navod konačni standard ostaje isti: izvor → identitet dokumenta → datum → hash → sadržaj → procesna važnost → neovisna provjera. Tamo gdje karika nedostaje, status ostaje OTVORENO.

**VERZIJA DOKUMENTA: V2 · 29.09.2026. · aktualiziran OFFF status + dodan strateško-povijesni blok Koromačno/Ubaš.**
