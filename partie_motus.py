import csv
""" Import du fichier csv qui contient la liste de mot """
import random
""" Import de la variable random pour tirer un mot au hasard dans la liste """

def win(lettre, mot):
    """ Défini si le joueur a placé toute les lettre du mot choisi dans la bonne place et 
        que le compteur ne soit pas = 0, le joueur gagne et retourne un texte """
    win = "Tu as gagné"
    if lettre == mot:
        return win
    
def loose(lettre, mot):
    """ Défini si le joueur n'a pas placé toutes les lettres du mot dans la bonne place 
        mais que le compteur est = 0, le joueur perd et retourne un texte """
    loose = "Tu as perdu"
    if compteur == 0:
        return loose
    
def retry(lettre, mot):
    """ Si la lettre du mot n'est pas à la bonne place mais que 
        le compteur n'est pas a 0, le joueur a un nouvel essai """
    if lettre != mot:
        compteur - 1

def points(compteur):
    """ Quand le joueur a gagné, des points sont comptabilisés 
        en fonction du nombre d'essais que le joueur a dû utilisé """
    points = 0
    if compteur >= 1:
        points = compteur
         
def mot_hasard(t1):
    """ Tire un mot au hasard dans la liste et défini sa variable """
    string = ""
    mot = random.choice(t1)
    for elem in mot.values():
        string += elem.lower()
    return string

def nombre_lettre(mot):
    """ Défini le nombre de lettres du mot choisi en utilisant une boucle """
    nb_lettre = 0
    for lettre in len(mot):
        nb_lettre += 1
        print("Le mot choisi contient",nb_lettre,"lettres.")

def verif_lettre_bon_place(let1, let2):
    if ord(let1) == ord(let2):
        return True

def verif_lettre_mauvaise_place(let1, mot):
    for let2 in mot:
        if ord(let1) == ord(let2):
            return True

def verif_mot(mot,mot2):
    """ Vérifie que mot2 correspond à la variable mot à deviner
        mot: str proposée
        mot2: str à deviner """

    for i in range (len(mot)):
        if verif_lettre_bon_place(mot[i], mot2[i]):
            print("bonne place :" ,mot[i])
        elif verif_lettre_mauvaise_place(mot[i], mot2):
            print("mauvaise place :" ,mot[i])
        else:
            print("n'existe pas :" ,mot[i])
    
compteur = 6        
if __name__ == "__main__":
    liste_mot = open("liste_mot.csv") 
    liste_de_mots = list(csv.DictReader(liste_mot, delimiter = ";"))
    mot_a_deviner = mot_hasard(liste_de_mots)
    phrase = "Mot de "+str(len(mot_a_deviner))+" caractères, entrez votre proposition : "
    for i in range(compteur):
        verif_mot(input(phrase), mot_a_deviner)
        resultat(mot_a_deviner,mot_hasard,compteur
