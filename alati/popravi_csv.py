import re

file_path = r"C:\Users\zeljk\dosje-koromacno\docs\evidence\Evidence_Matrix_CANON_v2.csv"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Ovo zamjenjuje ""E- s "\n"E- (dodaje novi red između zapisa)
content = re.sub(r'""(E-\d{3})', r'"\n"\1', content)

# Osigurava da datoteka završava novim redom
if not content.endswith("\n"):
    content += "\n"

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ CSV je popravljen. Svi zapisi su sada u zasebnim redovima.")