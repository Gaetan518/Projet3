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

def nombre_lettre(mot):
    """ Compter le nombre de lettres du mot choisi
        Retourne le nombre à l'utilisateur
        mot = str à deviner """
    nb_lettres = 0
    for i in range(len(mot)):
        nb_lettres += 1
        print("Le mot choisi contient",nb_lettres,"lettres")
