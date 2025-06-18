import os
import os
import shutil

def genereer_bestandsnamen(mapnaam, output_file='original_filenames.txt'):
    if not os.path.exists(mapnaam):
        print("Map bestaat niet.")
        return

    bestanden = os.listdir(mapnaam)
    bestanden = [f for f in bestanden if os.path.isfile(os.path.join(mapnaam, f))]
    bestanden.sort()

    with open(output_file, 'w') as f:
        for bestand in bestanden:
            f.write(bestand + '\n')
    print(f"{len(bestanden)} bestandsnamen opgeslagen in {output_file}")
    return bestanden

def hernoem_bestanden(mapnaam):
    originele_bestanden = genereer_bestandsnamen(mapnaam)
    if not originele_bestanden:
        return

    for i, oudenaam in enumerate(originele_bestanden, start=1):
        extensie = os.path.splitext(oudenaam)[1]
        nieuwenaam = f"movie_poster_{i:02d}{extensie}"
        os.rename(
            os.path.join(mapnaam, oudenaam),
            os.path.join(mapnaam, nieuwenaam)
        )
    print("Bestanden succesvol hernoemd.")

def herstel_bestandsnamen(mapnaam, input_file='original_filenames.txt'):
    if not os.path.exists(input_file):
        print("Bestand met originele namen niet gevonden.")
        return

    with open(input_file, 'r') as f:
        originele_namen = [regel.strip() for regel in f.readlines()]

    huidige_bestanden = os.listdir(mapnaam)
    huidige_bestanden = sorted([f for f in huidige_bestanden if os.path.isfile(os.path.join(mapnaam, f))])

    if len(huidige_bestanden) != len(originele_namen):
        print("Aantal bestanden komt niet overeen. Kan niet herstellen.")
        return

    for huidig, origineel in zip(huidige_bestanden, originele_namen):
        os.rename(
            os.path.join(mapnaam, huidig),
            os.path.join(mapnaam, origineel)
        )
    print("Bestandsnamen succesvol hersteld.")

def main():
    while True:
        print("\n1. Hernoem en nummer bestanden")
        print("2. Hernoem bestanden naar originele naam")
        print("3. Stop")
        keuze = input("keuze ? ")

        if keuze == "1":
            mapnaam = input("Geef de naam van de map met afbeeldingen (bijv. input): ")
            hernoem_bestanden(mapnaam)
        elif keuze == "2":
            mapnaam = input("Geef de naam van de map met afbeeldingen (bijv. input): ")
            herstel_bestandsnamen(mapnaam)
        elif keuze == "3":
            print("Tot ziens!")
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")

if __name__ == "__main__":
    main()


