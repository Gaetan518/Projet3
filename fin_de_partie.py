def resultat(mot, lettre):
    compteur = 6
    points = 0
    
    for i in range(6):
        if lettre != mot:
            compteur - 1 #si toute les lettres = mots, joueur gangne sinon -1 au compteur
        else:
            return True
        if compteur > 0:  #si mot trouvé avant que compteur soit = a 0 , point += compteur d'essai restant
                compteur += points
                return points
