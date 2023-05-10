# Afficher valeur de statistique

# Valeur 
# effectif



class Statistique:
    def __init__(self):
        self.valeur = []
        self.effectif = []

    def ajout(self, val, effectif = 1):
        for ranger in range(len(self.valeur)):
            if val == self.valeur[ranger]:
                self.effectif[ranger] += effectif
                return [val, effectif]
        self.valeur.append(val)
        self.effectif.append(effectif)
        return [val, effectif]
    
    def triFusion(self, T, debut, fin):
        if debut > fin:
            return 0
        # Trouvez le point milieu pour diviser le tableau en deux moitiés
        milieu = (debut+fin)/2
     
        # Appelez triFusion pour la première moitié du tableau:
        self.triFusion(T, debut, milieu)
 
        # Appelez triFusion pour la deuxième moitié du tableau:
        self.triFusion(T, milieu+1, fin)
 
        # Fusionnez les deux moitiés triées
        self.fusion(T, debut, fin, milieu)

    def getValeur(self):
        print("Valeur : ", end="")
        for ranger in range(len(self.valeur)):
            if ranger+1 == len(self.valeur):
                print(self.valeur[ranger])
            else:
                print(self.valeur[ranger], end=", ")

    def getEffectif(self):
        print("Effectif : ", end="")
        for ranger in range(len(self.effectif)):
            if ranger+1 == len(self.effectif):
                print(self.effectif[ranger])
            else:
                print(self.effectif[ranger], end=", ")

    def getEffectifDeValeur(self, val):
        sommeEffect = 0
        for i in range(len(self.valeur)):
            if val == self.valeur[i]:
                sommeEffect += self.effectif[i]
        print(f"La valeur : {val} a {sommeEffect} effectif")
        return sommeEffect

    def effectifTotal(self): # effectif total = N
        somme = 0
        for elt in self.effectif:
            somme += elt
        return somme
    
    def frequence(self, effectif): # fréquence = effectif / effectif total
        return effectif / self.effectifTotal()
    
    def frequencePourcent(self, effectif): # frequence en pourcentatge = frequence*100
        return self.frequence(effectif) * 100
    
    def getFrequence(self):
        print("Frequence : ", end="")
        for ranger in range(len(self.effectif)):
            if ranger+1 == len(self.effectif):
                print(round(self.frequence(self.effectif[ranger]), 3))
            else:
                print(round(self.frequence(self.effectif[ranger]), 3), end=", ")
    
    def getFrequencePourcent(self):
        print("Frequence : ", end="")
        for ranger in range(len(self.effectif)):
            if ranger+1 == len(self.effectif):
                print(round(self.frequencePourcent(self.effectif[ranger]), 3))
            else:
                print(round(self.frequencePourcent(self.effectif[ranger]), 3), end=", ")

    def moyenne(self): # moyenne = x​1​​+x​2​​+x​3​​+⋯+x​N / N
        somme = 0
        for ranger in range(len(self.valeur)):
            somme += self.valeur[ranger]*self.effectif[ranger]
        return round(somme / self.effectifTotal(), 3)
    
    def mediane(self): # Mediane = moitité de la liste
        moitier = self.effectifTotal()//2
        compt = 0
        for i in range(len(self.valeur)):
            for j in range(self.effectif[i]):
                if compt == moitier:
                    return self.valeur[i]
                compt += 1

    
    def plusGrand(self): # PLus grande valeur
        grand = self.valeur[0]
        for elt in self.valeur:
            if grand < elt:
                grand = elt
        return grand
    
    def plusPetit(self): # PLus petit valeur
        petit = self.valeur[0]
        for elt in self.valeur:
            if petit > elt:
                petit = elt
        return petit
    
    def etendu(self): # étendue = plus grand - plus petit
        return self.plusGrand() - self.plusPetit()

s = Statistique()

while True:
    try:
        val = input("Valeur (ou quitter): ")
        if val == "q" or val == "quitter":
            break

        val = float(val)
        effectif = input("Effectif : ")
        effectif = int(effectif)
    except ValueError:
        # 1 - choisir un nombre entier
        print("\n Erreur : veiller saisir un nombre !")
    else:
        s.ajout(val, effectif)

print()
print("--------------------------------")
s.getValeur()
s.getEffectif()
print()

s.getFrequence()
s.getFrequencePourcent()
print(f"Moyenne : {s.moyenne()}")
print(f"Mediane : {s.mediane()}")
print()

print(f"Plus petit element : {s.plusPetit()}")
print(f"Plus grand element : {s.plusGrand()}")
print(f"Etendu : {s.etendu()}")
print()
print("--------------------------------")     