import stat_1 as st
import tkinter as tk 
from tkinter import messagebox

noteVal = st.Statistique()

def valuer(): 
    try:
        noteVal.ajout(int(valeurText.get()), int(effectifText.get()))
    except:
        messagebox.showerror("Erreur", "Veiller mettre des informations correct !")

    change1.set(f"{noteVal.getValeur()}")
    change2.set(f"{noteVal.getEffectif()}")

# Creation de la fenetre principale
fenetre = tk.Tk()

# Configuration de la fenetre
fenetre.title("Note")
fenetre.geometry("640x580")
fenetre.minsize(720,400)

# Titre 
titre = tk.Label(fenetre, text = "Note obtenu", pady=10, font=('Calibri', 17, 'bold'))
titre.pack()

# Frame pour element a gauche
# Ajout de valeur avec son effectif
cadre1 = tk.Frame(fenetre)
cadre1.pack()

valeur1 = tk.Frame(cadre1)
valeur1.pack(side = "left")
valeurLabel = tk.Label(valeur1, text="Valeur : ")
valeurLabel.pack(side = "left")
valeurText = tk.Entry(valeur1)
valeurText.pack(side = "right")

effectif1 = tk.Frame(cadre1)
effectif1.pack(side = "left")
effectif1.pack(side = "left")
effectifLabel = tk.Label(effectif1, text="Effectif : ")
effectifLabel.pack(side = "left")
effectifText = tk.Entry(effectif1)
effectifText.pack(side = "right")

envoyerResulthat = tk.Button(cadre1, text="Envoyer", command=valuer)
envoyerResulthat.pack(side = "right")
                                                                                                                                                                    


# ajout de bordur
br = tk.Frame(fenetre, bg = "black", bd=5, width=400)
br.pack()
# Affichage des valeur a droite
tableau = tk.Frame(fenetre)
tableau.pack()
valeur2 = tk.Frame(tableau)
valeur2.pack()

v = tk.Label(valeur2, text="Valeur : ")
v.pack(side="left")
change1 = tk.StringVar()
vAffiche = tk.Label(valeur2, textvariable=change1)
change1.set("None")
vAffiche.pack(side="right")

effectif2 = tk.Frame(tableau)
effectif2.pack()
eff = tk.Label(effectif2, text="Effectif : ")
eff.pack(side="left")
change2 = tk.StringVar()
effAffiche = tk.Label(effectif2, textvariable=change2)
change2.set("None")
effAffiche.pack(side="right")

fenetre.mainloop()
    