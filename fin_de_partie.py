def resultat(mot, lettre):
    compteur = 6
    points = 0
    
    for i in range(6):
        if lettre != mot:
            compteur - 1 #si toutes les lettres = mots, joueur gagne sinon -1 au compteur
        else:
            return True
        if compteur > 0:  #si mot trouvé avant que compteur = 0 , point += compteur d'essai restant
                compteur += points
                return points
