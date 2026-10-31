# POTPUNO PROVJERENA SKRIPTA ZA POPRAVAK KVAČICA
file_path = r"C:\Users\zeljk\dosje-koromacno\docs\evidence\Evidence_Matrix_CANON_v2.csv"

zamjene = {
    'Ä‡': 'ć', 'Ä': 'č', 'Ä‘': 'đ', 'Å¡': 'š', 'Å¾': 'ž',
    'Ä†': 'Ć', 'ÄŚ': 'Č', 'Ä': 'Đ', 'Å ': 'Š', 'Å½': 'Ž',
    'OkoliÅ¡na': 'Okolišna',
    'PoÄetno': 'Početno',
    'rjeÅ¡enje': 'rješenje',
    'zaÅ¡tite': 'zaštite',
    'okoliÅ¡a': 'okoliša',
    'postojeÄ‡e': 'postojeće',
    'KoromaÄno': 'Koromačno',
    'sluÅ¾bena': 'službena',
    'OpÄ‡ina': 'Općina',
    'RaÅ¡a': 'Raša',
    'podruÄja': 'područja',
    'duÅ¾nosti': 'dužnosti',
    'sadrÅ¾i': 'sadrži',
    'tvornice': 'tvornice',
    'cementa': 'cementa'
}

print("Citam datoteku...")
try:
    # Otvaramo datoteku i čitamo. Ako naiđe na čudne znakove, neće pući.
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        tekst = f.read()

    print("Popravljam kvacice...")
    for stari, novi in zamjene.items():
        tekst = tekst.replace(stari, novi)

    # Spremamo natrag u čisti UTF-8 bez BOM-a
    with open(file_path, "w", encoding="utf-8", newline="") as f:
        f.write(tekst)
    
    print("✅ SVE JE POPRAVLJENO! Kvačice su vraćene.")
except Exception as e:
    print(f"❌ Došlo je do greške: {e}")