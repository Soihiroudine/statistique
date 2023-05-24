import tri

class Statistique:
    def __init__(self, val = []):
        self.valeur = val # [valeur, effectif]

    def ajout(self, val, effectif = 1):
        # for ranger in range(len(self.valeur)):
        #     if val == self.valeur[ranger][0]:
        #         self.valeur[ranger][1] += effectif
        #         return [val, effectif]   
        self.valeur.append([val, effectif])
        tri.triFusion(self.valeur)
        return [val, effectif]

    def getValeur(self):
        chaine = ""
        print("Valeur : ", end="")
        for ranger in range(len(self.valeur)):
            if ranger+1 == len(self.valeur):
                chaine += str(self.valeur[ranger][0])
                print(self.valeur[ranger][0])
            else:
                chaine += str(self.valeur[ranger][0])+", "
                print(self.valeur[ranger][0], end=", ")
        return chaine

    def getEffectif(self):
        chaine = ""
        print("Effectif : ", end="")
        for ranger in range(len(self.valeur)):
            if ranger+1 == len(self.valeur):
                chaine += str(self.valeur[ranger][1])
                print(self.valeur[ranger][1])
            else:
                chaine += str(self.valeur[ranger][1])+", "
                print(self.valeur[ranger][1], end=", ")
        return chaine

    def getEffectifDeValeur(self, val):
        sommeEffect = 0
        for i in range(len(self.valeur)):
            if val == self.valeur[i][0]:
                sommeEffect += self.valeur[i][1]
        print(f"La valeur : {val} a {sommeEffect} effectif")
        return sommeEffect

    def effectifTotal(self): # effectif total = N
        somme = 0
        for elt in range(len(self.valeur)):
            somme += self.valeur[elt][1]
        return somme
    
    def frequence(self, effectif): # fréquence = effectif / effectif total
        return effectif / self.effectifTotal()
    
    def frequencePourcent(self, effectif): # frequence en pourcentatge = frequence*100
        return self.frequence(effectif) * 100
    
    def getFrequence(self):
        print("Frequence : ", end="")
        for ranger in range(len(self.valeur)):
            if ranger+1 == len(self.valeur):
                print(round(self.frequence(self.valeur[ranger][1]), 3))
            else:
                print(round(self.frequence(self.valeur[ranger][1]), 3), end=", ")
    
    def getFrequencePourcent(self):
        print("Frequence : ", end="")
        for ranger in range(len(self.valeur)):
            if ranger+1 == len(self.valeur):
                print(round(self.frequencePourcent(self.valeur[ranger][1]), 3))
            else:
                print(round(self.frequencePourcent(self.valeur[ranger][1]), 3), end=", ")

    def moyenne(self): # moyenne = x​1​​+x​2​​+x​3​​+⋯+x​N / N
        somme = 0
        for ranger in range(len(self.valeur)):
            somme += self.valeur[ranger][0]*self.valeur[ranger][1]
        return round(somme / self.effectifTotal(), 3)
    
    def mediane(self): # Mediane = moitité de la liste
        moitier = self.effectifTotal()//2
        compt = 0
        for i in range(len(self.valeur)):
            for j in range(self.valeur[i][1]):
                if compt == moitier:
                    return self.valeur[i][0]
                compt += 1

    def plusGrand(self): # PLus grande valeur
        grand = self.valeur[0][0]
        for elt in range(len(self.valeur)):
            if grand < self.valeur[elt][0]:
                grand = self.valeur[elt][0]
        return grand
    
    def plusPetit(self): # PLus petit valeur
        petit = self.valeur[0][0]
        for elt in range(len(self.valeur)):
            if petit > self.valeur[elt][0]:
                petit = self.valeur[elt][0]
        return petit
    
    def etendu(self): # étendue = plus grand - plus petit
        return self.plusGrand() - self.plusPetit()

# s = Statistique()

# while True:
#     try:
#         val = input("Valeur (ou quitter): ")
#         if val == "q" or val == "quitter":
#             break

#         val = float(val)
#         effectif = input("Effectif : ")
#         effectif = int(effectif)
#     except ValueError:
#         # 1 - choisir un nombre entier
#         print("\n Erreur : veiller saisir un nombre !")
#     else:
#         s.ajout(val, effectif)

# def affiche():
#     print()
#     print("--------------------------------")
#     s.getValeur()
#     s.getEffectif()
#     print()

#     s.getFrequence()
#     s.getFrequencePourcent()
#     print(f"Moyenne : {s.moyenne()}")
#     print(f"Mediane : {s.mediane()}")
#     print()

#     print(f"Plus petit element : {s.plusPetit()}")
#     print(f"Plus grand element : {s.plusGrand()}")
#     print(f"Etendu : {s.etendu()}")
#     print()
#     print("--------------------------------")     


# affiche()