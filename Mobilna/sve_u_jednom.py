import sqlite3
import requests
import time
import winsound
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# --- POSTAVKE ---
DB_PATH = r"C:\Users\zeljk\mobilna\zrak.db"
LOKACIJA_ID = "b54fb46b-32b6-4d66-af03-2612faae6deb"
LOKACIJA_IME = "Koromačno"
INTERVAL = 3600  # Svakih sat vremena

GRANICE = {
    "NO2": 200.0,
    "SO2": 350.0
}

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS mjerenja (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 timestamp TEXT,
                 lokacija TEXT,
                 parametar TEXT,
                 vrijednost REAL,
                 jedinica TEXT,
                 granica REAL,
                 prekoracenje INTEGER
                 )''')
    conn.commit()
    conn.close()

def upali_alarm(parametar, vrijednost, granica):
    for _ in range(5):
        winsound.Beep(1500, 400)
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning("⚠️ PREKORAČENJE!", f"{parametar}: {vrijednost} µg/m³\nGranica: {granica}")
    root.destroy()

def dohvati_podatke_api():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Provjeravam API...")
    
    plinovi = {"no2": "NO2", "so2": "SO2", "no": "NO", "nox": "NOx"}
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    sada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    for api_oznaka, baza_oznaka in plinovi.items():
        url = f"https://zrak.infomedica.hr/v1/public/locations/{LOKACIJA_ID}/series?pollutant={api_oznaka}&range=24h"
        
        try:
            odgovor = requests.get(url, timeout=10)
            odgovor.raise_for_status()
            podaci = odgovor.json()
            
            # Tražimo točno "points" listu
            if "points" in podaci and len(podaci["points"]) > 0:
                zadnji_zapis = podaci["points"][-1]
                vrijednost = float(zadnji_zapis["value"])
                
                gv = GRANICE.get(baza_oznaka)
                prekoracenje = 0
                
                if gv is not None and vrijednost > gv:
                    prekoracenje = 1
                    print(f"🚨 PREKORAČENJE: {baza_oznaka} = {vrijednost} > {gv}")
                    upali_alarm(baza_oznaka, vrijednost, gv)
                else:
                    print(f"✅ {baza_oznaka}: {vrijednost} µg/m³")
                    
                c.execute("INSERT INTO mjerenja (timestamp, lokacija, parametar, vrijednost, jedinica, granica, prekoracenje) VALUES (?, ?, ?, ?, ?, ?, ?)",
                          (sada, LOKACIJA_IME, baza_oznaka, vrijednost, "µg/m³", gv, prekoracenje))
            else:
                print(f"⚠️ Nema 'points' liste za {baza_oznaka}.")
                
        except Exception as e:
            print(f"❌ Greška za {baza_oznaka}: {e}")
            
    conn.commit()
    conn.close()
    print("💾 Gotovo.")

if __name__ == "__main__":
    init_db()
    print("🚀 Pokrećem API nadzor (Ctrl+C za prekid)...")
    while True:
        dohvati_podatke_api()
        print(f"⏳ Sljedeća provjera za {INTERVAL//60} min...\n")
        time.sleep(INTERVAL)