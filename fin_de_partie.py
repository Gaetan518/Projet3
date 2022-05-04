def fin_de_partie(lettre):
    win ="Tu as Gagné"
    lose = "Tu as Perdu"
    compteur = 6
    points = 0
    
    for i in range(6):
        if lettre != mot:
            compteur - 1 #si toute les lettres sont égale a mots, joueur gangne sinon deduire 1 de compteur
        else:
            return win
        if compteur == 0: #si compteur d'essai = 0, joueur a perdu
            return lose
        if compteur > 0:  #si mot trouvé avant que compteur soit = a 0 , point += compteur d'aessai restant
                compteur += points
                
