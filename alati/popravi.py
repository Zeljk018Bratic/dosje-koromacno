import os

file_path = r"C:\Users\zeljk\dosje-koromacno\docs\evidence\Evidence_Matrix_CANON_v2.csv"

replacements = {
    'Ä‡': 'ć', 'ÄŤ': 'č', 'ÄŚ': 'Č', 'Ä†': 'Ć',
    'Ĺˇ': 'š', 'Ĺ ': 'Š', 'Ĺľ': 'ž', 'Ĺ˝': 'Ž',
    'Ä‘': 'đ', 'â†”': '↔', 'â€ž': '„', 'â€ś': '“',
    'â‚¬': '€', 'Â˛': '²'
}

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    for old, new in replacements.items():
        content = content.replace(old, new)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Gotovo! Svi znakovi su popravljeni.")
except Exception as e:
    print(f"❌ Greška: {e}")