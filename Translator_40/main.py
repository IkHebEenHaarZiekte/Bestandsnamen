import os
from deep_translator import GoogleTranslator
import pyttsx3

# Vertalen in chunks (max 500 chars per keer)
def vertaal_tekst(tekst, src='en', tgt='nl', chunk_size=500):
    vertaald = ''
    for i in range(0, len(tekst), chunk_size):
        chunk = tekst[i:i+chunk_size]
        vertaald += GoogleTranslator(source=src, target=tgt).translate(chunk)
    return vertaald

def vertaal_map(bronmap, doelmap, src='en', tgt='nl'):
    os.makedirs(doelmap, exist_ok=True)
    bestanden = [f for f in os.listdir(bronmap) if f.lower().endswith('.txt')]

    if not bestanden:
        print("Geen tekstbestanden gevonden in de bronmap.")
        return []

    vertaalde_bestanden = []
    for bestand in bestanden:
        pad = os.path.join(bronmap, bestand)
        with open(pad, 'r', encoding='utf-8') as f:
            tekst = f.read()

        print(f"Vertalen: {bestand}...")
        vertaalde_tekst = vertaal_tekst(tekst, src, tgt)

        uitvoerpad = os.path.join(doelmap, bestand)
        with open(uitvoerpad, 'w', encoding='utf-8') as f:
            f.write(vertaalde_tekst)

        vertaalde_bestanden.append(uitvoerpad)
    return vertaalde_bestanden

def lijst_voorlezen(bestanden):
    if not bestanden:
        print("Geen bestanden om voor te lezen.")
        return

    print("\nVertaalde bestanden:")
    for i, bestand in enumerate(bestanden, 1):
        print(f"{i}. {os.path.basename(bestand)}")

    keuze = input("Kies een bestand om voor te lezen (nummer): ")
    try:
        index = int(keuze) - 1
        if index < 0 or index >= len(bestanden):
            print("Ongeldige keuze.")
            return
    except ValueError:
        print("Ongeldige invoer.")
        return

    pad = bestanden[index]
    with open(pad, 'r', encoding='utf-8') as f:
        tekst = f.read()

    print(f"Bezig met voorlezen: {os.path.basename(pad)}")
    engine = pyttsx3.init()
    engine.say(tekst)
    engine.runAndWait()

def main():
    print("=== Tekstvertaler met voorlezen ===")
    bronmap = input("Pad naar map met teksten (source): ").strip()
    doelmap = input("Pad naar map voor vertaalde teksten (output): ").strip()
    bron_taal = input("Bron taal (bv. en): ").strip() or 'en'
    doel_taal = input("Doeltaal (bv. nl): ").strip() or 'nl'

    vertaalde_bestanden = vertaal_map(bronmap, doelmap, bron_taal, doel_taal)

    if vertaalde_bestanden:
        lijst_voorlezen(vertaalde_bestanden)
    else:
        print("Geen vertaalde bestanden gevonden.")

if __name__ == "__main__":
    main()
