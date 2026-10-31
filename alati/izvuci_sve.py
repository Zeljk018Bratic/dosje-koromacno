import requests
import json
import csv

# HIER DEINEN GENERIERTEN TOKEN EINTRAGEN
TOKEN = "DEIN_TOKEN_HIER"
REPO = "Zeljk018Bratic/dosje-koromacno"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}

def dohvati_sve_stranice(endpoint):
    url = f"https://github.com{REPO}/{endpoint}"
    rezultati = []
    params = {"per_page": 100, "page": 1}
    
    while True:
        response = requests.get(url, headers=HEADERS, params=params)
        if response.status_code != 200:
            print(f"Greška na {endpoint}: {response.status_code}")
            break
        podaci = response.json()
        
        if isinstance(podaci, dict):
            kljuc = next((k for k in podaci.keys() if isinstance(podaci[k], list)), None)
            if kljuc:
                if not podaci[kljuc]: break
                rezultati.extend(podaci[kljuc])
            else:
                return podaci
        else:
            if not podaci: break
            rezultati.extend(podaci)
            
        params["page"] += 1
    return rezultati

# 1. Izvlačenje kompletnog Actions Timeline-a
print("-> Izvlačim istoriju svih GitHub Actions runs (Stranice 1-26)...")
actions = dohvati_sve_stranice("actions/runs")

# Spremanje u CSV format (za Excel / lagan pregled svih vremena)
with open("timeline_actions.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Run ID", "Naziv", "Status", "Zakljucak", "Pokrenuto (Vreme)", "Zavrseno (Vreme)", "Korisnik"])
    for run in actions:
        writer.writerow([
            run.get("id"), run.get("name"), run.get("status"), 
            run.get("conclusion"), run.get("created_at"), run.get("updated_at"),
            run.get("actor", {}).get("login")
        ])

# 2. Izvlačenje statistike koda i prometa
print("-> Izvlačim statistiku koda i frekvencije...")
statistike = ["stats/commit_activity", "stats/code_frequency", "stats/contributors", "traffic/views"]
for s in statistike:
    ime_fajla = s.replace("/", "_") + ".json"
    res = requests.get(f"https://github.com{REPO}/{s}", headers=HEADERS)
    if res.status_code == 200:
        with open(ime_fajla, "w", encoding="utf-8") as f:
            json.dump(res.json(), f, indent=4)

print("\n[HURRA!] Sve je uspešno izvučeno. Pogledaj kreirane datoteke u folderu!")
