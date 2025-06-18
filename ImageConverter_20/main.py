import os
from PIL import Image

def is_afbeelding(bestand):
    extensies = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp']
    return os.path.splitext(bestand)[1].lower() in extensies

def resize_afbeelding(pad, max_grootte):
    afbeelding = Image.open(pad)
    afbeelding.thumbnail((max_grootte, max_grootte))  # Houdt verhouding
    return afbeelding

def verwerk_afbeeldingen(bronmap, doelmap, max_grootte):
    if not os.path.exists(bronmap):
        print("❌ De opgegeven bronmap bestaat niet.")
        return

    os.makedirs(doelmap, exist_ok=True)

    bestanden = os.listdir(bronmap)
    totaal_bestanden = len(bestanden)
    print(f"📁 Totaal gevonden in bronmap: {totaal_bestanden} bestanden")

    verwerkte = 0
    overgeslagen = 0

    for bestand in bestanden:
        pad = os.path.join(bronmap, bestand)

        if not os.path.isfile(pad):
            continue

        if not is_afbeelding(bestand):
            print(f"⏭️  Geen afbeelding: {bestand} (overgeslagen)")
            overgeslagen += 1
            continue

        try:
            print(f"⚙️  Aanpassen: {bestand}")
            aangepaste_afbeelding = resize_afbeelding(pad, max_grootte)
            uitvoerpad = os.path.join(doelmap, bestand)
            aangepaste_afbeelding.save(uitvoerpad)
            verwerkte += 1
        except Exception as e:
            print(f"❗ Fout bij verwerken van {bestand}: {e}")

    print("\n✅ Verwerking voltooid.")
    print(f"✔️  Aangepaste afbeeldingen: {verwerkte}")
    print(f"❌ Niet-afbeeldingen overgeslagen: {overgeslagen}")

def main():
    print("=== Image Converter ===")
    bronmap = input("Geef het pad naar de bronmap: ").strip()
    doelmap = input("Geef het pad naar de doelmap: ").strip()
    try:
        max_grootte = int(input("Wat is het maximale formaat (bv. 2000)? ").strip())
        if max_grootte < 1 or max_grootte > 2000:
            print("❌ Ongeldige grootte. Moet tussen 1 en 2000 zijn.")
            return
    except ValueError:
        print("❌ Ongeldige invoer voor maximale grootte.")
        return

    verwerk_afbeeldingen(bronmap, doelmap, max_grootte)

if __name__ == "__main__":
    main()
