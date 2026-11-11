from pathlib import Path
import pandas as pd

SRC = Path("iszz_xls")
OUT = Path("iszz_out")
OUT.mkdir(parents=True, exist_ok=True)

def load(path):
    df = pd.read_excel(path, header=None)
    hdr = None
    for i, row in df.iterrows():
        if str(row.iloc[0]).strip().lower() == "datum":
            hdr = i
            break
    if hdr is None:
        return None
    data = df.iloc[hdr + 1:].copy()
    data.columns = [str(x).strip() for x in df.iloc[hdr]]
    data = data.dropna(how="all")
    data = data.rename(columns={data.columns[0]: "Datum"})
    return data

def pollutant(path):
    raw = pd.read_excel(path, header=None)
    for v in raw.iloc[:10, 0].dropna().astype(str):
        if "[" in v and "]" in v:
            parts = v.split("[")
            name = parts[0].strip()
            unit = parts[1].split("]")[0].strip()
            return name, unit
    return path.stem, ""

rows = []
for path in sorted(SRC.glob("*.xls*")):
    df = load(path)
    if df is None: continue
    pol, unit = pollutant(path)
    
    # Rješavamo dnevne podatke (koji imaju kolonu Vrijednost)
    if "Vrijednost" in df.columns:
        m = df[["Datum", "Vrijednost"]].copy()
        m["Sat"] = "Dnevno"
    else:
        hours = [c for c in df.columns if c != "Datum"]
        if not hours: continue
        m = df.melt(id_vars=["Datum"], value_vars=hours, var_name="Sat", value_name="TempVrijednost")
        m = m.rename(columns={"TempVrijednost": "Vrijednost"})
        
    m["Pollutant"] = pol
    m["Unit"] = unit
    m["Source"] = path.name
    rows.append(m)

if not rows:
    print("Nema podataka.")
    exit()

df = pd.concat(rows, ignore_index=True)
df["Datum"] = pd.to_datetime(df["Datum"], dayfirst=True, errors="coerce")
# Pretvaramo zareze u točke za decimalne brojeve i uklanjamo greške
df["Vrijednost"] = pd.to_numeric(df["Vrijednost"].astype(str).str.replace(",", "."), errors="coerce")

def clean_sat(x):
    if pd.isna(x): return x
    s = str(x).replace(":00", "")
    return int(s) if s.isdigit() else s
df["Sat"] = df["Sat"].apply(clean_sat)

neg = df[df["Vrijednost"] < 0]
neg.to_csv(OUT / "negative.csv", index=False)

# Računamo rupe samo za satne podatke
hourly = df[df["Sat"] != "Dnevno"]
expected = 24
cov = (
    hourly.groupby(["Pollutant", "Datum"])["Vrijednost"]
      .agg(available="count", missing=lambda s: expected - s.count())
      .reset_index()
)
cov.to_csv(OUT / "missing_hours.csv", index=False)

daily = df.groupby(["Pollutant", "Datum"])["Vrijednost"].mean().reset_index()
daily.to_csv(OUT / "daily_means.csv", index=False)

df.to_csv(OUT / "all_hourly.csv", index=False)

print("Negativnih vrijednosti:", len(neg))
print("Gotovo. Rezultati su u mapi: iszz_out")
