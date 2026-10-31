import json
from pathlib import Path
import pandas as pd

RAW = Path("data/raw_air_data")
OUT = Path("data/mobile_out")
OUT.mkdir(parents=True, exist_ok=True)

rows = []
for f in RAW.glob("*.json"):
    with open(f, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    
    # Uzimamo ime polutanta iz JSON-a ili iz imena fajla
    pol = data.get("pollutant_key", f.stem.split("_")[0]).upper()
    
    # Podaci su u listi "points"
    points = data.get("points", [])
    for item in points:
        rows.append({
            "Source": "Mobilna",
            "Pollutant": pol,
            "Datum": item.get("time") or item.get("date"),
            "Vrijednost": item.get("value")
        })

df = pd.DataFrame(rows)
df.to_csv(OUT / "mobile_raw.csv", index=False)
print(f"Uspješno spremljeno {len(df)} redaka u mobile_raw.csv")
