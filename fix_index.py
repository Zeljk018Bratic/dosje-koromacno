import io

# Učitaj čisti HTML
with io.open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pripremi novi gumb
new_button = '  <a class="nav-btn" href="provjereno-mapa.html" target="_blank" style="background-color: #b91c1c; border-color: #fca5a5;">📺 Provjereno: SOA Mapa</a>\n  <a class="nav-btn" href="manifest.html"'

# Ubaci gumb ispred Manifesta
if 'href="manifest.html"' in content:
    content = content.replace('<a class="nav-btn" href="manifest.html"', new_button)
    print("Gumb uspješno dodan!")
else:
    print("Greška: nisam pronašao Manifest gumb.")

# Spremi natrag u čistom UTF-8
with io.open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
