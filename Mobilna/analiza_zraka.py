import sqlite3
import csv
import os

# --- POSTAVKE ---
# Vracamo putanju na tvoju originalnu bazu gdje scraper pise!
DB_PATH = r"C:\Users\zeljk\mobilna\zrak.db"
IZLAZNI_CSV = r"C:\Users\zeljk\dosje-koromacno\Mobilna\analiza_anomalija.csv"

def analiziraj_bazu():
    if not os.path.exists(DB_PATH):
        print("Greska: Baza ne postoji na putanji:", DB_PATH)
        return

    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        print("Trazim negativne vrijednosti (anomalije) u bazi...")
        
        # Upit koji vadi samo negativne vrijednosti
        c.execute("""
            SELECT timestamp, parametar, vrijednost 
            FROM mjerenja 
            WHERE vrijednost < 0 
            ORDER BY timestamp DESC
        """)
        anomalije = c.fetchall()

        if not anomalije:
            print("Nema negativnih vrijednosti u bazi. (Jos)")
            conn.close()
            return

        # Spremanje u CSV
        with open(IZLAZNI_CSV, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(["Vrijeme", "Parametar", "Izmjerena vrijednost (ug/m3)"])
            for red in anomalije:
                writer.writerow(red)

        print("Pronadeno", len(anomalije), "negativnih ocitanja!")
        print("Spremljeno u:", IZLAZNI_CSV)
        print("Ovo je tvoj cvrsti dokaz za OLAF/EPPO.")

        conn.close()
    except Exception as e:
        print("Dogodila se greska:", e)

if __name__ == "__main__":
    analiziraj_bazu()