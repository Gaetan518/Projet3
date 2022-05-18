def resultat(lettre, compteur, mot):
    """Quand le joueur a trouvé le mot la fonction renvoi win, si le joueur 
    n'a pas trouvé mais est = a 0, elle renvois loose,
    si le joueur n'a pas trouvé mais le compteur n'est pas = a 0 il a encore des essais"""
    win = "Tu as gagné"
    loose = "Tu as perdu"
    if lettre == mot:
        return True
    else:
        compteur == 0
        return False
    if lettre != mot:
        compteur = compteur - 1
        return compteur
            
compteur = 6        
if __name__ == "__main__":
    liste_mot = open("liste_mot.csv") 
    liste_de_mots = list(csv.DictReader(liste_mot, delimiter = ";"))
    mot_a_deviner = mot_hasard(liste_de_mots)
    phrase = "Mot de "+str(len(mot_a_deviner))+" caractères, entrez votre proposition : "
    for i in range(compteur):
        verif_mot(input(phrase), mot_a_deviner)
        resultat(mot_a_deviner,mot_hasard,compteur)
        
