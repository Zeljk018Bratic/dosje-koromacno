import pandas as pd

# Sređujemo dnevne prosjeke
df_daily = pd.read_csv("iszz_out/daily_means.csv", sep=';', decimal=',')
df_daily = df_daily.round(2)
df_daily.to_csv("iszz_out/daily_means.csv", index=False, sep=';', decimal=',')
print("daily_means.csv je zaokružen i spremljen.")

# Sređujemo i negativne vrijednosti (za svaki slučaj)
df_neg = pd.read_csv("iszz_out/negative.csv", sep=';', decimal=',')
df_neg = df_neg.round(3) # Ovdje 3 decimale jer su manje vrijednosti
df_neg.to_csv("iszz_out/negative.csv", index=False, sep=';', decimal=',')
print("negative.csv je zaokružen i spremljen.")
