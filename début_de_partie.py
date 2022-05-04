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

def nombre_lettre(mot):
    """Compter le nombre de lettres du mot choisi"""
    return len(mot)
