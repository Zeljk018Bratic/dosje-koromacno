import matplotlib.pyplot as plt
import numpy as np

# Točni satni podaci za PM10 na dan 30.09.2026. (od 1:00 do 24:00) izvučeni iz RAW sustava
satni_podaci = [
    10.73, 11.692, 10.405, 9.81, 8.622, 8.502, 8.084, 8.347, 
    8.294, 8.181, 9.186, 9.393, 20.19, 12.827, 10.251, 14.463, 
    33.926, 16.757, 13.659, 12.527, 12.786, 11.344, 10.777, 11.389
]

sati = np.arange(1, 25)
dnevni_prosjek = 12.173  # Službeno iskazana vrijednost za taj dan

# Postavljanje vizualnog stila
fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
ax.set_facecolor('white')
ax.grid(True, linestyle=':', alpha=0.6, color='#cccccc')

# Crtanje stvarnih satnih vrijednosti (RAW DATA)
ax.plot(sati, satni_podaci, color='#d9534f', linewidth=3, marker='o', label='Stvarno satno stanje (RAW DATA)')
ax.fill_between(sati, satni_podaci, color='#d9534f', alpha=0.12)

# Crtanje službenog dnevnog prosjeka
ax.axhline(dnevni_prosjek, color='#0275d8', linestyle='--', linewidth=2.5, 
           label=f'Službeno prikazani dnevni prosjek: {dnevni_prosjek} µg/m³')

# Fiksiran cijeli poziv scatter i annotate funkcija bez grešaka
ax.scatter(17, 33.926, color='black', s=120, zorder=5)
ax.annotate('Maksimalni udar: 33.926 µg/m³\n(Nakon ulaska kamiona pod policijskom pratnjom)', 
            xy=(17, 33.926), xytext=(8, 28),
            arrowprops=dict(facecolor='#333333', shrink=0.1, width=1.5, headwidth=7),
            fontsize=10, weight='bold', bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='gray', alpha=0.9))

# Estetska obrada grafikona
ax.set_title('KOROMAČNO (30.09.2026.) – Kako dnevni prosjek skriva ekološki incident', fontsize=13, pad=15, weight='bold')
ax.set_xlabel('Sat u danu (01:00 - 24:00h)', fontsize=11)
ax.set_ylabel('Koncentracija PM₁₀ čestica (µg/m³)', fontsize=11)
ax.set_xticks(sati)
ax.set_xlim(0.5, 24.5)
ax.set_ylim(0, 40)

ax.legend(loc='upper left', fontsize=10, frameon=True, facecolor='white', edgecolor='none')
plt.tight_layout()

# Spremanje ispravne datoteke na disk
plt.savefig('stvarni_incident_30_09.png', dpi=300)
plt.close()
