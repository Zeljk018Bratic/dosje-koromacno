import pandas as pd
import os

# Popis datoteka koje treba srediti
files = [
    "iszz_out/negative.csv",
    "iszz_out/missing_hours.csv",
    "iszz_out/daily_means.csv",
    "data/mobile_out/mobile_raw.csv"
]

for f in files:
    if os.path.exists(f):
        # Učitaj original
        df = pd.read_csv(f)
        # Spremi preko originala, ali s hrvatskim formatom (; i ,)
        df.to_csv(f, index=False, sep=';', decimal=',')
        print(f"Srijeđeno: {f}")
    else:
        print(f"Nema datoteke: {f}")

print("Sve datoteke su spremne za slanje!")
