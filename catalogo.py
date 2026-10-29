import json
import os
import capi

def catalogo_iniziale():
    return [
        {"tipo": "maglietta", "nome": "Basic Tee", "prezzo_base": 15.0, "taglia": "M", "colore": "Bianco", "stampa": ""},
        {"tipo": "maglietta", "nome": "Street Logo", "prezzo_base": 25.0, "taglia": "L", "colore": "Nero", "stampa": "PYTHON-OOP"},
        {"tipo": "felpa", "nome": "Hoodie Urban", "prezzo_base": 45.0, "taglia": "L", "colore": "Grigio", "cappuccio": True},
        {"tipo": "felpa", "nome": "Light Crew", "prezzo_base": 35.0, "taglia": "M", "colore": "Blu", "cappuccio": False},
        {"tipo": "pantalone", "nome": "Cargo Tech", "prezzo_base": 55.0, "taglia": "42", "colore": "Verde", "fit": "cargo"},
        {"tipo": "pantalone", "nome": "Slim Chino", "prezzo_base": 49.0, "taglia": "44", "colore": "Beige", "fit": "slim"},
        {"tipo": "sneakers", "nome": "Cloud Runner", "prezzo_base": 90.0, "numero": 42, "colore": "Bianco", "edizione_limitata": False},
        {"tipo": "sneakers", "nome": "Limited Fire", "prezzo_base": 120.0, "numero": 44, "colore": "Rosso/Nero", "edizione_limitata": True}
    ]

def crea_capo(dati):
    match dati["tipo"]:
        case "maglietta":
            return capi.Maglietta(dati["nome"], dati["prezzo_base"], dati["taglia"], dati["colore"], dati["stampa"])
        case "felpa":
            return capi.Felpa(dati["nome"], dati["prezzo_base"], dati["taglia"], dati["colore"], dati["cappuccio"])
        case "pantalone":
            return capi.Pantalone(dati["nome"], dati["prezzo_base"], dati["taglia"], dati["colore"], dati["fit"])
        case "sneakers":
            return capi.Sneakers(dati["nome"], dati["prezzo_base"], dati["numero"], dati["colore"], dati["edizione_limitata"])
        case _:
            return None

def carica_dati():
    if os.path.exists("catalogo.json"):
        with open("catalogo.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return catalogo_iniziale()

def salva_dati(dati):
    with open("catalogo.json", "w", encoding="utf-8") as f:
        json.dump(dati, f, indent=4)

def carica_catalogo():
    dati = carica_dati()
    salva_dati(dati)
    return [crea_capo(item) for item in dati if crea_capo(item) is not None]

def aggiungi_record(record):
    dati = carica_dati()
    dati.append(record)
    salva_dati(dati)