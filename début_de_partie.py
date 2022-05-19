import csv 
import random
liste_mot = open("liste_mot.csv") 
t1 = list(csv.DictReader(liste_mot, delimiter = ";")) 

def mot_hasard(t1):
    """ Défini une variable pour le mot tiré au hasard """
    string = ""
    mot = random.choice(t1)
    for elem in mot.values():
        string += elem.lower()
    return string
