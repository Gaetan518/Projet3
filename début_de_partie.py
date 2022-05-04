import csv 
liste_mot = open("liste_mot.csv") 
t1 = list(csv.DictReader(liste_mot, delimiter = ";")) 

import random
def mot_hasard(t1): 
    mot = random.choice(t1)
    return mot
mot_hasard(t1)

def nombre_lettre(mot):
    """Compter le nombre de lettres du mot choisi"""
    return len(mot)
