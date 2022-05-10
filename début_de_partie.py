import csv 
liste_mot = open("liste_mot.csv") 
t1 = list(csv.DictReader(liste_mot, delimiter = ";")) 

import random
def mot_hasard(t1):
     """Tire un mot au hasard parmi la liste de mot"""
    mot = random.choice(t1)
    return mot

def nombre_lettre(mot):
    """ Compter le nombre de lettres du mot choisi
        Retourne le nombre à l'utilisateur
        mot = str à deviner
    """
    nb_lettres = 0
    for i in range(len(mot)):
        nb_lettres += 1
        print("Le mot choisi contient",nb_lettres,"lettres")
