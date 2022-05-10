import csv
""" Import du fichier csv qui contient la liste de mot """
import random
""" Import de la variable random pour tirer un mot au hasard dans la liste """

def resultat(mot, lettre):
    compteur = 6
    points = 0
    
def win(lettre, mot):
    """ Defini si le joueur a placer toute les lettre du mot choisidans la bonne place et 
       que le compteur ne soit pas = 0 , le joueur gagne et retourne un texte """
    win = "Tu as gagné"
    if lettre == mot:
        return win
    

    def lose(lettre, mots):
    """ Defini si le joueur n'a pas placer toutes les lettres du mot dans la bonne place 
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

                
def mot_hasard(t1): 
    mot = random.choice(t1)
    return mot

mot_de_gaetan = mot_hasard(t1)
mot_a_entrer(input("Entrez votre proposition: "),mot_de_gaetan) 


def nombre_lettre(mot):
    nb_lettre = 0
    for lettre in len(mot):
            nb_lettre += 1
            print("Le mot choisi contient",nb_lettre,"lettres.")

def verif_lettre_bon_place(let1, let2):
    if ord(let1) == ord(let2):
        return True

def verif_lettre_mauvaise_place(let1, mot):
    for let2 in mot:
        if ord(let1)==ord(let2):
            return True

def verif_mot(mot,mot2):
    """ Vérifie que mot2 correspond à la variable mot à deviner
        mot: str proposée
        mot2: str à deviner """

    for i in range (len(mot)):
        if verif_lettre_bon_place(mot[i], mot2[i]):
            print("bonne place")
        elif verif_lettre_mauvaise_place(mot[i], mot2):
            print("mauvaise place")
        else:
            print("n'existe pas")
          
        
        verif_mot = mot
        
if __name__ == "__main__":
    liste_mot = open("liste_mot.csv") 
    liste_de_mots = list(csv.DictReader(liste_mot, delimiter = ";"))
    mot_a_deviner = mot_hasard(liste_de_mots)
    verif_mot(verif_mot,mot_a_deviner )
