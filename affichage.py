import stat_1 as st
import tkinter as tk 

fenetre = tk.Tk()

fenetre.title("Note")
fenetre.geometry("640x580")
fenetre.minsize(720,400)

titre = tk.Label(fenetre, text = "Note obtenu")
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

effectif = tk.Frame(cadre1)
effectif.pack(side = "left")
effectifLabel = tk.Label(effectif, text="Effectif : ")
effectifLabel.pack(side = "left")
effectifText = tk.Entry(effectif)
effectifText.pack(side = "right")

envoyerResulthat = tk.Button(cadre1, text="Envoyer", command=st.affiche)
envoyerResulthat.pack(side = "right")

# ajput de bordur

bordur = tk.Frame(fenetre, bg = "black", bd=5, width=230).pack()

# Affichage des valeur a droite
tableau = tk.Frame(fenetre)
tableau.pack()

valeur2 = tk.Label(tableau, text="Valeur : ")
valeur2.pack()

v = tk.Label(valeur2, text="Valeur : ")


fenetre.mainloop()

# def afficher():
    