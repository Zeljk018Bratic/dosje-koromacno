import sqlite3
import pandas as pd
import json
import os
import glob

BASE_DIR = r"C:\Users\zeljk\mobilna"
DB_PATH = os.path.join(BASE_DIR, "zrak.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS sirovi_podaci (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 izvor TEXT,
                 naziv_datoteke TEXT,
                 podaci TEXT
                 )''')
    conn.commit()
    return conn

def spremi_csv(conn, filepath, izvor):
    try:
        # sep=None i engine='python' automatski prepoznaju je li zarez ili točka-zarez
        # on_bad_lines='skip' preskače redove koji su totalno zeznuti
        df = pd.read_csv(filepath, sep=None, engine='python', on_bad_lines='skip')
        for index, row in df.iterrows():
            json_str = row.to_json(force_ascii=False)
            c = conn.cursor()
            c.execute("INSERT INTO sirovi_podaci (izvor, naziv_datoteke, podaci) VALUES (?, ?, ?)", 
                      (izvor, os.path.basename(filepath), json_str))
        conn.commit()
        print(f"✅ Uspješno spremljeno: {os.path.basename(filepath)} ({len(df)} redaka)")
    except Exception as e:
        print(f"❌ Greška kod {os.path.basename(filepath)}: {e}")

def spremi_excel(conn, filepath):
    try:
        # Za XLS koristimo read_excel, ne read_csv
        df = pd.read_excel(filepath)
        for index, row in df.iterrows():
            json_str = row.to_json(force_ascii=False)
            c = conn.cursor()
            c.execute("INSERT INTO sirovi_podaci (izvor, naziv_datoteke, podaci) VALUES (?, ?, ?)", 
                      ("ISZZ_XLS", os.path.basename(filepath), json_str))
        conn.commit()
        print(f"✅ Uspješno spremljeno: {os.path.basename(filepath)} ({len(df)} redaka)")
    except Exception as e:
        print(f"❌ Greška kod {os.path.basename(filepath)}: {e}")

def spremi_json(conn, filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Ako je rječnik (objekt), pretvaramo ga u listu s jednim elementom
        if isinstance(data, dict):
            data = [data]
            
        if isinstance(data, list):
            for item in data:
                json_str = json.dumps(item, ensure_ascii=False)
                c = conn.cursor()
                c.execute("INSERT INTO sirovi_podaci (izvor, naziv_datoteke, podaci) VALUES (?, ?, ?)", 
                          ("JSON_Raw", os.path.basename(filepath), json_str))
            conn.commit()
            print(f"✅ Uspješno spremljeno: {os.path.basename(filepath)} ({len(data)} zapisa)")
        else:
            print(f"⚠️ Preskočeno (nepoznat format): {os.path.basename(filepath)}")
    except Exception as e:
        print(f"❌ Greška kod {os.path.basename(filepath)}: {e}")

def main():
    print("Krećem s izradom baze podataka...")
    conn = init_db()
    
    # 1. CSV datoteke
    csv_files = [
        (os.path.join(BASE_DIR, "data", "mobile_out", "mobile_raw.csv"), "Mobile_Out"),
        (os.path.join(BASE_DIR, "iszz_out", "all_hourly.csv"), "ISZZ_Hourly"),
        (os.path.join(BASE_DIR, "iszz_out", "daily_means.csv"), "ISZZ_Daily"),
        (os.path.join(BASE_DIR, "iszz_vs_mobile_FINAL.csv"), "Usporedba")
    ]
    
    for path, izvor in csv_files:
        if os.path.exists(path):
            spremi_csv(conn, path, izvor)
        else:
            print(f"⚠️ Nema datoteke: {path}")

    # 2. JSON datoteke
    json_folders = [
        os.path.join(BASE_DIR, "data", "raw_air_data", "*.json"),
        os.path.join(BASE_DIR, "monitoring", "data", "raw_air_data", "*.json")
    ]
    
    for pattern in json_folders:
        for filepath in glob.glob(pattern):
            spremi_json(conn, filepath)
            
    # 3. XLS datoteke
    xls_files = glob.glob(os.path.join(BASE_DIR, "iszz_xls", "*.xls"))
    for path in xls_files:
        spremi_excel(conn, path)

    conn.close()
    print("\n🎉 Gotovo! Svi podaci (koji su se dali pročitati) su u bazi 'zrak.db'.")

if __name__ == "__main__":
    main()