def win(lettre, mot):
    win = "Tu as gagné"
    if lettre == mot:
        return win
    
def lose(lettre, mots):
    lose = "tu as perdue"
    if compteur == 0:
        return lose
    
def retry(lettre, mot):
    if lettre != mots:
        compteur - 1
    
def point(compteur):
    points = 0
    if compteur >= 1:
        points = compteur
