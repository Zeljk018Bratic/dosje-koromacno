import tkinter as tk
from tkinter import messagebox
import winsound

def upali_alarm(parametar, vrijednost, granica):
    # 1. Zvuk (5 puta zabuči)
    for _ in range(5):
        winsound.Beep(1500, 400)

    # 2. Prozor na ekranu
    root = tk.Tk()
    root.withdraw() # Sakrij pozadinski prozor
    messagebox.showwarning(
        "⚠️ PREKORAČENJE NA MJERNOJ STANICI!",
        f"Parametar: {parametar}\n"
        f"Izmjereno: {vrijednost} µg/m³\n"
        f"Granica: {granica} µg/m³\n\n"
        f"ODMAH PROVJERI PODATKE!"
    )
    root.destroy()

# --- TESTIRANJE ---
if __name__ == "__main__":
    # Ovo je testni poziv, kada budeš spojio sa svojom skriptom, samo zamijeni brojeve
    upali_alarm("NO2", 3825, 200)