# PAKET 14-10-2026 — dubinska provjera registara i cjelovite Studije
**Redoslijed:** (1) PRVO izvrši večerašnji push `SVE_U_REPO_13-10.ps1` (validacijska vrata za 44 reda matrice!). (2) TEK NAKON uspješnog pusha dodaj ovaj paket zasebnim commitom — NE miješati u isti commit jer novi redovi E-045…E-059 mijenjaju broj redova matrice.
**Commit naredbe (nakon što se paket kopira u klon C:\Users\zeljk\dosje-lf):**
```
git add docs/Evidence/E-MATRIX_NOVI_REDOVI_E045-E059.csv docs/Forenzika/2026-10-14_DUBINSKA_PROVJERA_REGISTRI_I_STUDIJA.md docs/Pravni-akti/2026-10-14_OLAF_ADDENDUM_Ares9536412_DRAFT.md docs/Akcija/RASA_VIJECE_14-10-2026_DODATAK.md SHA256_DOKAZI_14-10-2026.txt
git commit -m "Dokazi E-045..E-059: registar OD, screening 2021, PUO akti, cjelovita Studija, dubinska provjera 14-10"
git push
git rev-parse HEAD:docs
```
**VAŽNO — veliki binarni dokazi IZVAN repoa:** PUO_2026-08-14_STUDIJA_cjelovita.pdf (100,6 MB) i ostali PDF-ovi spremaju se lokalno u `C:\Dokazi_E-2026-10\`; u repo idu samo hash i URL (vidi SHA256_DOKAZI_14-10-2026.txt i E-matricu).
**OLAF dodatak:** ne šaljeti prije nego Qwen ugrade novi root hash docs/ i prije potvrde da nema novih Ares poruka u threadu.
**Arhiva čekanja (Željko, iz preglednika):** HTML izvornici N1 (15.09.) i istra24 (zbor) + labin.com — izravno skidanje vraća 403; sačuvati kao PDF/HTML i poslati hash.
