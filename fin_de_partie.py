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
                
                
        
import csv 
liste_mot = open("liste_mot.csv") 
t1 = list(csv.DictReader(liste_mot, delimiter = ";")) 

import random
def mot_hasard(t1): 
    mot = random.choice(t1)
    return mot
mot_hasard(t1)

def nombre_lettre(mot):
    nb_lettre = 0
    for lettre in len(mot):
        if lettre in mot:
            nb_lettre += 1
            print("Le mot choisi contient",nb_lettre,"lettres.")
nombre_lettre(mot)
