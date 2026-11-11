# Legal soft-edit note 11.11.2026

Applied to Evidence_Matrix_CANON_v2.csv (local LEGAL build SHA-256 `af4306bc36196801e833568c74547a0b4428e99c27017c7f95fb1c93412ed077`):

## E-111
- Status: `TVRDNJA (izvor K / transkript)`
- Opis: jasno "Izvor K navodi", "nije sudski utvrđeno"; imena samo u kontekstu transkripta

## E-126 (Bioinstitut Čakovec)
- Status: `TVRDNJA (izvor K) — NEPROVJERENO`
- Opis: "navodi" / "prema njezinim tvrdnjama" / "ne kao utvrđena činjenica"

## E-127 (Kemis Termoclean / Remondis)
- Status: `TVRDNJA (izvor K) — NEPROVJERENO`
- Opis: "navodno" uz svaku tvrdnju; "Materijal za nadležna tijela (DORH/EPPO), ne kao javna optužba"

## Mojibake
- E-132–E-138: ispravljeno (Gospić, čl., Blasković)

## Restore kanonske matrice
Datoteka na `main` još treba zamjenu punim LEGAL buildom (API limit ~68 KB).

```bash
# iz lokalnog artifakta ili:
git checkout dc111e43728c9dbf89c3bfdbae51725f9530322a -- docs/evidence/Evidence_Matrix_CANON_v2.csv
# zatim primijeni soft-edit + mojibake fix, ili kopiraj Evidence_Matrix_CANON_v2_LEGAL.csv
git add docs/evidence/Evidence_Matrix_CANON_v2.csv
git commit -m "Restore matrix: UTF-8 + legal soft-edit E-111/E-126/E-127"
git push origin main
```

Local SHA-256 LEGAL: `af4306bc36196801e833568c74547a0b4428e99c27017c7f95fb1c93412ed077`
