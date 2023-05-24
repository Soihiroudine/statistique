import csv

bare1 = [
    ['ID', 'Nom', 'Age', 'Taille'] ,
    ['1', 'Walid', '19', '180'],
    ['2', 'Najib', '30', '185'],
    ['3', 'Majda', '27', '175']
    ]

# Ouvrir le fichier csv
with open('data.csv', 'w') as f:

    ecrit = csv.writer(f)
    # Créer un objet csv à partir du fichier
    # obj = csv.reader(f)

    for elt in bare1:
        ecrit.writerow(elt)

with open("data.csv", "r") as file :
    lire = csv.reader(file)

    for ligne in lire:
        print(ligne)