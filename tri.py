
# utilisation de la liste self.valeur

def triFusion(tab):
    if len(tab) > 1:
        mid = len(tab)//2
 
        G = tab[:mid] # sous-tableau gauche
        D = tab[mid:] # sous-tableau droit
 
        triFusion(G)
        triFusion(D)
 
        # Fusion                               
        i = j = k = 0
 
        while i < len(G) and j < len(D):
            if G[i][0] < D[j][0]:
                tab[k] = G[i]
                i += 1
            else:
                tab[k] = D[j]
                j += 1
            k += 1
 
        while i < len(G):
            tab[k] = G[i]
            i += 1
            k += 1
 
        while j < len(D):
            tab[k] = D[j]
            j += 1
            k += 1
 
