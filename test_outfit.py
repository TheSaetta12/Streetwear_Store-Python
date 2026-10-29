import capi
import outfit

mio_outfit = outfit.Outfit("Giulio")

tshirt = capi.Maglietta("Street", 19.90, "L", "nero", "SKYLINE")
felpa = capi.Felpa("Urban", 39.90, "M", "grigio", True)

mio_outfit.aggiungi(tshirt)
mio_outfit.aggiungi(felpa)

print("--- RIEPILOGO PARZIALE (senza sconto) ---")
print(mio_outfit.riepilogo())

pantalone = capi.Pantalone("Denim", 49.90, "M", "blu", "slim")
scarpe = capi.Sneakers("Drop-01", 99.90, 43, "nero", True)

mio_outfit.aggiungi(pantalone)
mio_outfit.aggiungi(scarpe)

print("\n--- RIEPILOGO FINALE (con sconto 10%) ---")
print(mio_outfit.riepilogo())