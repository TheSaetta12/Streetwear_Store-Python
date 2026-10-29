class Capo:
    totale_creati = 0
    saldi = 0

    def __init__(self, nome, prezzo_base, taglia, colore):
        self.nome = nome
        self.prezzo_base = prezzo_base
        self.taglia = taglia
        self.colore = colore
        self.categoria = "generico"
        Capo.totale_creati += 1

    def applica_saldi(self, prezzo):
        prezzo_scontato = prezzo * (100 - Capo.saldi) / 100
        return round(prezzo_scontato, 2)

    def prezzo_finale(self):
        return self.applica_saldi(self.prezzo_base)

    def descrizione(self):
        return f"{self.nome} ({self.colore}, tg. {self.taglia}) - {self.prezzo_finale()} €"

    def a_dizionario(self):
        return {
            "nome": self.nome,
            "categoria": self.categoria,
            "taglia": self.taglia,
            "colore": self.colore,
            "prezzo": self.prezzo_finale()
        }

class Maglietta(Capo):
    def __init__(self, nome, prezzo_base, taglia, colore, stampa=""):
        super().__init__(nome, prezzo_base, taglia, colore)
        self.categoria = "top"
        self.stampa = stampa

    def prezzo_finale(self):
        prezzo = self.prezzo_base + 5 if self.stampa else self.prezzo_base
        return self.applica_saldi(prezzo)

    def descrizione(self):
        dettaglio = f" con stampa \"{self.stampa}\"" if self.stampa else ""
        return f"T-shirt {self.nome} ({self.colore}, tg. {self.taglia}){dettaglio} - {self.prezzo_finale()} €"

class Felpa(Capo):
    def __init__(self, nome, prezzo_base, taglia, colore, cappuccio=True):
        super().__init__(nome, prezzo_base, taglia, colore)
        self.categoria = "top"
        self.cappuccio = cappuccio

    def prezzo_finale(self):
        prezzo = self.prezzo_base + 8 if self.cappuccio else self.prezzo_base
        return self.applica_saldi(prezzo)

    def descrizione(self):
        dettaglio = " con cappuccio" if self.cappuccio else " senza cappuccio"
        return f"Felpa {self.nome} ({self.colore}, tg. {self.taglia}){dettaglio} - {self.prezzo_finale()} €"

class Pantalone(Capo):
    def __init__(self, nome, prezzo_base, taglia, colore, fit="regular"):
        super().__init__(nome, prezzo_base, taglia, colore)
        self.categoria = "bottom"
        self.fit = fit

    def descrizione(self):
        return f"Pantalone {self.nome} ({self.colore}, tg. {self.taglia}) fit {self.fit} - {self.prezzo_finale()} €"

class Sneakers(Capo):
    def __init__(self, nome, prezzo_base, numero, colore, edizione_limitata=False):
        super().__init__(nome, prezzo_base, str(numero), colore)
        self.categoria = "scarpe"
        self.edizione_limitata = edizione_limitata

    def prezzo_finale(self):
        prezzo = self.prezzo_base * 1.5 if self.edizione_limitata else self.prezzo_base
        return self.applica_saldi(prezzo)

    def descrizione(self):
        dettaglio = " EDIZIONE LIMITATA" if self.edizione_limitata else ""
        return f"Sneakers {self.nome} ({self.colore}, n. {self.taglia}){dettaglio} - {self.prezzo_finale()} €"