import json
import csv
import os

print("-> Pokrećem lokalnu OFFLINE konverziju podataka...")

ulazni_fajl = "cjeloviti_actions_timeline.json"
izlazni_csv = "timeline_actions.csv"

if not os.path.exists(ulazni_fajl):
    print(f"Greška: Fajl {ulazni_fajl} ne postoji u ovom folderu!")
else:
    with open(ulazni_fajl, "r", encoding="utf-8") as f:
        podaci = json.load(f)
    
    actions = podaci.get("workflow_runs", [])
    
    with open(izlazni_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Run ID", "Naziv Akcije", "Status", "Zaključak", "Pokrenuto (Datum i Vreme)", "Završeno (Datum i Vreme)", "Korisnik (Log-in)"])
        
        for run in actions:
            # Čišćenje formata vremena za Excel (uklanjanje T i Z)
            kreirano = run.get("created_at", "").replace("T", " ").replace("Z", "")
            zavrseno = run.get("updated_at", "").replace("T", " ").replace("Z", "")
            
            writer.writerow([
                run.get("id"), 
                run.get("name"), 
                run.get("status"), 
                run.get("conclusion"), 
                kreirano, 
                zavrseno,
                run.get("actor", {}).get("login")
            ])
            
    print(f"\n[USPEH!] Napravljena je Excel tabela: {izlazni_csv}")
    print("Sada je možeš slobodno otvoriti i filtrirati hronološki.")
