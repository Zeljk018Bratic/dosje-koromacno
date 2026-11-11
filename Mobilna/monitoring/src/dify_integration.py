"""Slanje podataka i pokretanje Dify workflowa za projekt Dosje-Koromačno."""

from __future__ import annotations

import os
import requests

# ZAMIJENI OVAJ TEKST SA SVOJIM STVARNIM DIFY API KLJUČEM (koji počinje s app-):
DIFY_API_KEY = os.environ.get("DIFY_WORKFLOW_API_KEY", "app-OvdjeZalijepiSvojDifyKljuč")

# Točna putanja za izvršavanje Dify workflowa
DIFY_URL = "https://api.dify.ai/v1/workflows/run"


def javi_dify_sustavu(status_poruka: str, tip_podatka: str, putanja_datoteke: str) -> None:
    """Šalje podatke u sustav koristeći isključivo ASCII znakove bez kvačica."""
    headers = {
        "Authorization": "Bearer OK",  # Privremeni fiksni token dok ne povežemo Kun API
        "Content-Type": "application/json"
    }
    
    # Čistimo tekst od kvačica (č, ž, š...) kako requests ne bi bacao 'latin-1' grešku
    sigurna_poruka = status_poruka.replace("č", "c").replace("ć", "c").replace("ž", "z").replace("š", "s").replace("đ", "dj")
    sigurna_putanja = putanja_datoteke.replace("\\", "/") # Windows putanje pretvaramo u standardne mrežne
    
    payload = {
        "inputs": {
            "poruka": sigurna_poruka,
            "tip": tip_podatka,
            "datoteka": sigurna_putanja
        },
        "response_mode": "blocking",
        "user": "zeljko-monitor-sustav"
    }
    
    try:
        # Budući da trenutno Dify URL nije aktivan, ovaj dio će ispisati samo lokalni log
        print(f"[Kun-Log] Priprema obavijesti za {tip_podatka}...")
        # Ako želiš potpuno ugasiti mrežni šum dok ne dobijemo Kun API ključ, 
        # ovdje samo ispisujemo podatke na ekran:
        print(f"[Kun-Sustav] Poruka poslana lokalno: {sigurna_poruka}")
    except Exception as e:
        print(f"[Sustav] Greška: {e}")
