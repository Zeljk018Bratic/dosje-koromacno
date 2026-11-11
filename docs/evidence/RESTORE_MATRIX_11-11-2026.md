# URGENT — Restore Evidence_Matrix_CANON_v2.csv

**Date:** 11.11.2026

During an automated mojibake fix, the file `docs/evidence/Evidence_Matrix_CANON_v2.csv` on `main` was overwritten with a short placeholder (API payload limit). Full content must be restored.

## Last good blob (with residual mojibake on E-132+ only)

- Commit: `dc111e43728c9dbf89c3bfdbae51725f9530322a`
- Blob SHA: `26b6816558c19b76a413b89ebda598ebb9d67101`

## Restore + fix (local)

```bash
git fetch origin
git checkout dc111e43728c9dbf89c3bfdbae51725f9530322a -- docs/evidence/Evidence_Matrix_CANON_v2.csv

# Fix mojibake (UTF-8 mis-read as Latin-1)
python3 - <<'PY'
from pathlib import Path
p = Path("docs/evidence/Evidence_Matrix_CANON_v2.csv")
t = p.read_text(encoding="utf-8")
rep = {"Ä‡":"ć","Ä\x8d":"č","Ä":"č","Å¾":"ž","Å¡":"š","Ä‘":"đ","ÄŒ":"Č","Ä†":"Ć","Å½":"Ž"}
for a,b in rep.items():
    t = t.replace(a,b)
p.write_text(t if t.startswith("\ufeff") else "\ufeff"+t.lstrip("\ufeff"), encoding="utf-8")
print("fixed", t.count("Gospić"), "Gospić;", "bad left", t.count("GospiÄ"))
PY

git add docs/evidence/Evidence_Matrix_CANON_v2.csv
git commit -m "Restore Evidence_Matrix_CANON_v2.csv + fix mojibake (ćčžšđ)"
git push origin main
```

## Fixed file hash (after mojibake fix)

- SHA-256: `944f33ecdab7d72cc164c05b821a683418197122e8b8f54284a1a03c4c3ffcd4`
- Local artifact (if available): `Evidence_Matrix_CANON_v2_FIXED.csv`

## Note

`MATRIX_ADDENDUM_E132-E138.csv` is intact and already correct UTF-8.
