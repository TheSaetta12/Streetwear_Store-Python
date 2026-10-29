import capi

capo1 = capi.Capo("Felpa Oversize", 59.99, "L", "Nero")
capo2 = capi.Capo("T-Shirt Basic", 19.505, "M", "Bianco")
capo3 = capi.Capo("Pantaloni Cargo", 45.00, "S", "Verde")

print(capo1.descrizione())
print(capo2.descrizione())
print(capo3.descrizione())

print(f"\nArticoli totali creati nello store: {capi.Capo.totale_creati}")