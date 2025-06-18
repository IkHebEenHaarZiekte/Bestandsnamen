import os
from PIL import Image
from fpdf import FPDF

def jpgs_naar_pdf(bronmap, uitvoerpad):
    # Haal alle jpg-bestanden op (case-insensitive)
    bestanden = sorted([
        f for f in os.listdir(bronmap)
        if f.lower().endswith(".jpg") and os.path.isfile(os.path.join(bronmap, f))
    ])

    if not bestanden:
        print("❌ Geen JPG-bestanden gevonden in de map.")
        return

    pdf = FPDF(unit="pt")  # pt = punten, handig voor precieze afmetingen

    for bestand in bestanden:
        pad = os.path.join(bronmap, bestand)
        with Image.open(pad) as img:
            breedte, hoogte = img.size
            print(f"➕ Voeg toe: {bestand} ({breedte}x{hoogte})")

            pdf.add_page(format=(breedte, hoogte))
            pdf.image(pad, x=0, y=0, w=breedte, h=hoogte)

    # Maak mappen aan als ze nog niet bestaan
    os.makedirs(os.path.dirname(uitvoerpad), exist_ok=True)

    pdf.output(uitvoerpad)
    print(f"✅ PDF opgeslagen als: {uitvoerpad}")

def main():
    print("=== JPG naar PDF ===")
    bronmap = input("Pad naar map met JPG-bestanden: ").strip()
    uitvoerpad = input("Pad voor uitvoer PDF (bijv. output/bundel.pdf): ").strip()

    if not os.path.isdir(bronmap):
        print("❌ Bronmap bestaat niet.")
        return

    jpgs_naar_pdf(bronmap, uitvoerpad)

if __name__ == "__main__":
    main()