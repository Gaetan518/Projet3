import csv 
import random

def resultat(mot, lettre):
    compteur = 6
    points = 0
    
    for i in range(6):
        if lettre != mot:
            compteur - 1 #si toute les lettres = mots, joueur gangne sinon -1 au compteur
        else:
            return True
        if compteur > 0:  #si mot trouvé avant que compteur soit = a 0 , point += compteur d'essai restant
                compteur += points
                return points
                
def mot_hasard(t1): 
    mot = random.choice(t1)
    return mot


    verif_mot = mot


mot_de_gaetan = mot_hasard(t1)
mot_a_entré(input("Entrez votre proposition: "),mot_de_gaetan) 


def nombre_lettre(mot):
    nb_lettre = 0
    for lettre in len(mot):
        if lettre in mot:
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
    """Vérifie que mot2 correspond à la variable mot à deviner
    mot: str proposée
    mot2: str à deviner
    """

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
