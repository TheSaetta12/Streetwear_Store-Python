import capi

t_shirt = capi.Maglietta("Street", 19.90, "L", "nero", "SKYLINE")
felpa = capi.Felpa("Urban", 39.90, "M", "grigio", True)
pantalone = capi.Pantalone("Denim", 49.90, "M", "blu", "slim")
scarpe = capi.Sneakers("Drop-01", 99.90, 43, "nero", True)

collezione = [t_shirt, felpa, pantalone, scarpe]

totale_collezione = 0

print("--- COLLEZIONE STREETWEAR STORE ---")

for capo in collezione:
    print(capo.descrizione())
    
    totale_collezione += capo.prezzo_finale()

print("-" * 50)

print(f"VALORE TOTALE COLLEZIONE: {round(totale_collezione, 2)} €")

print(f"Articoli totali disponibili nello store: {capi.Capo.totale_creati}")