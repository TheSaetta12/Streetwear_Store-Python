import capi
import outfit
import catalogo
import validazione 

def mostra_catalogo(articoli):
    righe = ["\n----- 📖 CATALOGO DISPONIBILE 📖 -----"]
    
    if capi.Capo.saldi > 0:
        righe.insert(0, f"\n🔥 SALDI ATTIVI: -{capi.Capo.saldi}% SU TUTTO LO STORE! 🔥")
    
    for i, capo in enumerate(articoli, 1):
        righe.append(f"{i}) {capo.descrizione()}")
    return "\n".join(righe)

def main():
    articoli = catalogo.carica_catalogo()
    outfit_attivo = None

    while True:
        print("\n🛹 ===== STREETWEAR STORE ===== 🛹")
        print("📖 1 - Mostra catalogo")
        print("✨ 2 - Nuovo outfit")
        print("➕ 3 - Aggiungi capo all'outfit")
        print("📋 4 - Riepilogo outfit")
        print("🧾 5 - Conferma ordine")
        print("📦 6 - Aggiungi capo al catalogo")
        print("🏷️  7 - Attiva/Disattiva Saldi")
        print("🗂️  8 - Storico ordini")
        print("0 - Esci")

        scelta = input("🕹️  Scegli un'opzione: ")

        match scelta:
            case "1":
                print(mostra_catalogo(articoli))

            case "2":
                nome_cliente = validazione.chiedi_testo("Inserisci il nome del cliente per l'outfit: ")
                outfit_attivo = outfit.Outfit(nome_cliente)
                print(f"✨ Nuovo outfit creato per {nome_cliente}.")

            case "3":
                if not outfit_attivo:
                    print("⚠️  Avviso: Devi prima creare un nuovo outfit (opzione 2)!")
                else:
                    print(mostra_catalogo(articoli))
                    scelta_idx = int(validazione.chiedi_numero("Quale articolo vuoi aggiungere? ", 1, len(articoli)))
                    capo_scelto = articoli[scelta_idx - 1]
                    
                    gia_completo = outfit_attivo.completo()
                    outfit_attivo.aggiungi(capo_scelto)
                    print(f"➕ Aggiunto: {capo_scelto.nome}")
                    
                    if not gia_completo and outfit_attivo.completo():
                        print("🎉 Outfit completo: sconto 10% sbloccato!")

            case "4":
                if not outfit_attivo:
                    print("🤷 Nessun outfit creato.")
                else:
                    print("\n" + outfit_attivo.riepilogo())

            case "5":
                if not outfit_attivo or len(outfit_attivo.capi) == 0:
                    print("⚠️  Avviso: L'outfit è vuoto, non puoi confermare l'ordine!")
                else:
                    print("\n📋 --- RIEPILOGO FINALE --- 📋")
                    print(outfit_attivo.riepilogo())
                    numero_ordine = outfit.salva_ordine(outfit_attivo)
                    print(f"\n✅ Ordine salvato con successo! Numero ordine: #{numero_ordine} 🧾")
                    print(f"\n🙏 Grazie per aver scelto lo Streetwear Store! 🛹")
                    outfit_attivo = None

            case "6":
                print("\n📦 AGGIUNTA NUOVO CAPO")
                print("1-T-shirt, 2-Felpa, 3-Pantalone, 4-Sneakers")
                tipo_scelto = int(validazione.chiedi_numero("Scegli tipo: ", 1, 4))
                
                nome = validazione.chiedi_testo("Nome articolo: ")
                prezzo = validazione.chiedi_numero("Prezzo base: ", 1, 2000)
                colore = validazione.chiedi_testo("Colore: ")
                
                record = {"nome": nome, "prezzo_base": prezzo, "colore": colore}
                
                match tipo_scelto:
                    case 1:
                        record["tipo"] = "maglietta"
                        record["taglia"] = validazione.chiedi_testo("Taglia: ")
                        record["stampa"] = input("Stampa (invio per nessuna): ")
                    case 2:
                        record["tipo"] = "felpa"
                        record["taglia"] = validazione.chiedi_testo("Taglia: ")
                        record["cappuccio"] = input("Con cappuccio? (s/n): ").lower() == 's'
                    case 3:
                        record["tipo"] = "pantalone"
                        record["taglia"] = validazione.chiedi_testo("Taglia: ")
                        record["fit"] = validazione.chiedi_testo("Fit (slim/regular/cargo): ")
                    case 4:
                        record["tipo"] = "sneakers"
                        record["numero"] = int(validazione.chiedi_numero("Numero: ", 30, 50))
                        record["edizione_limitata"] = input("Edizione limitata? (s/n): ").lower() == 's'

                catalogo.aggiungi_record(record)
                articoli.append(catalogo.crea_capo(record))
                print("✅ Articolo aggiunto correttamente al catalogo vivo!")

            case "7":
                if capi.Capo.saldi == 0:
                    capi.Capo.saldi = 20
                    print(f"\n🔥 SALDI -{capi.Capo.saldi}% ATTIVI SU TUTTO LO STORE! 🔥")
                else:
                    capi.Capo.saldi = 0
                    print("\n🛑 SALDI DISATTIVATI. Prezzi tornati al listino standard.")

            case "8":
                print(outfit.storico_ordini())

            case "0":
                print("🙏 Grazie per aver visitato lo Streetwear Store. Alla prossima! 👋")
                break
            
            case _:
                print("❌ Scelta non valida.")

if __name__ == "__main__":
    main()