import pandas as pd

# 1. ISZZ - dnevni u mjesečne
iszz = pd.read_csv("iszz_out/daily_means.csv")
iszz["Datum"] = pd.to_datetime(iszz["Datum"])
iszz["Mjesec"] = iszz["Datum"].dt.to_period("M").astype(str)
iszz_mj = iszz.groupby(["Pollutant", "Mjesec"])["Vrijednost"].mean().reset_index()
iszz_mj.rename(columns={"Vrijednost": "ISZZ"}, inplace=True)

# 2. Mobilna - u mjesečne
mobile = pd.read_csv("data/mobile_out/mobile_raw.csv")
mobile["Datum"] = pd.to_datetime(mobile["Datum"])
mobile["Mjesec"] = mobile["Datum"].dt.to_period("M").astype(str)
mobile.rename(columns={"Vrijednost": "Mobilna"}, inplace=True)

# 3. ČIŠĆENJE NAZIVA (indeksi u obične brojeve)
replacements = {
    '₂': '2', '₃': '3', '₁': '1', '₅': '5',
    '₀': '0', '₄': '4', '₆': '6', '₇': '7', '₈': '8', '₉': '9',
    'PM2.5': 'PM25'
}

def clean_pol(val):
    val = str(val)
    for k, v in replacements.items():
        val = val.replace(k, v)
    return val.upper()

iszz_mj["Pollutant"] = iszz_mj["Pollutant"].apply(clean_pol)
mobile["Pollutant"] = mobile["Pollutant"].apply(clean_pol)

# 4. Spajamo po parametru i mjesecu
merged = pd.merge(iszz_mj, mobile[["Pollutant", "Mjesec", "Mobilna"]], on=["Pollutant", "Mjesec"], how="outer")
merged["Razlika"] = merged["Mobilna"] - merged["ISZZ"]

merged.to_csv("iszz_vs_mobile.csv", index=False)
print(merged.to_string())
