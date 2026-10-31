import pandas as pd

df = pd.read_csv("iszz_vs_mobile.csv")
df = df.round(2)

# Sprema s točkom-zarezom i zarezom za decimale (kako hrvatski Excel voli)
df.to_csv("iszz_vs_mobile_FINAL.csv", index=False, sep=';', decimal=',')
print("Gotovo! Napravljena je iszz_vs_mobile_FINAL.csv")
