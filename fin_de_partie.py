def resultat(mot, lettre):
    compteur = 6            #/!\ se sont des valeurs que nous devront implementer.
    points = 0

def win(lettre, mot):
    """ Defini si le joueur a placer toute les lettre du mot choisidans la bonne place et 
        que le compteur ne soit pas = 0 , le joueur gagne et retourne un texte """
    win = "Tu as gagné"
    if lettre == mot:
        return win
    
def lose(lettre, mots):
    """ Defini si le joueur n'a pas placer toutes les lettre du mot dans la bonne place 
        mais que le compteur est = 0 , le joueur perd et retourne un texte """
    lose = "tu as perdue"
    if compteur == 0:
        return lose
    
def retry(lettre, mot):
    """ Si le lettre du mot ne sont pas toute dans la bonne place mais que 
        le compteur n'est pas a 0, le joueur a un nouvelle essai de deviner """
    if lettre != mots:
        compteur - 1
    
def point(compteur):
    """ Quand le joueur a ganger, des points sont comptabiliser 
        en fonction du nombre d'essai que le joueur a du utiliser """
    points = 0
    if compteur >= 1:
        points = compteur
