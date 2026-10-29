import json
import os

SCONTO_OUTFIT = 10

class Outfit:
    def __init__(self, cliente):
        self.cliente = cliente
        self.capi = []

    def aggiungi(self, capo):
        self.capi.append(capo)

    def totale_lordo(self):
        totale = sum(capo.prezzo_finale() for capo in self.capi)
        return round(totale, 2)

    def completo(self):
        categorie = [capo.categoria for capo in self.capi]
        return "top" in categorie and "bottom" in categorie and "scarpe" in categorie

    def sconto(self):
        if self.completo():
            valore_sconto = (self.totale_lordo() * SCONTO_OUTFIT) / 100
            return round(valore_sconto, 2)
        return 0

    def totale(self):
        return round(self.totale_lordo() - self.sconto(), 2)

    def riepilogo(self):
        righe = [f"✨ OUTFIT DI: {self.cliente} ✨", "-" * 20]
        
        for capo in self.capi:
            righe.append(capo.descrizione())
        
        righe.append("-" * 20)
        righe.append(f"Totale lordo: {self.totale_lordo()} €")
        
        if self.sconto() > 0:
            righe.append(f"Sconto outfit completo ({SCONTO_OUTFIT}%): -{self.sconto()} €")
            
        righe.append(f"DA PAGARE: {self.totale()} €")
        return "\n".join(righe)

    def a_dizionario(self):
        return {
            "cliente": self.cliente,
            "capi": [capo.a_dizionario() for capo in self.capi],
            "sconto": self.sconto(),
            "totale": self.totale()
        }

def carica_ordini():
    if os.path.exists("ordini.json"):
        with open("ordini.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salva_ordine(outfit_obj):
    ordini = carica_ordini()
    
    nuovo_ordine = outfit_obj.a_dizionario()
    numero_ordine = len(ordini) + 1
    nuovo_ordine["numero"] = numero_ordine
    
    ordini.append(nuovo_ordine)
    
    with open("ordini.json", "w", encoding="utf-8") as f:
        json.dump(ordini, f, indent=4)
        
    return numero_ordine

def storico_ordini():
    ordini = carica_ordini()
    if not ordini:
        return "📁 Nessun ordine presente nello storico. 📁"
    
    righe = ["\n🗂️  ===== STORICO ORDINI ===== 🗂️"]
    for o in ordini:
        righe.append(f"Ordine #{o['numero']} - Cliente: {o['cliente']} - Totale: {o['totale']} €")
    
    return "\n".join(righe)