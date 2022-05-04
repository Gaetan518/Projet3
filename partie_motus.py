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


mot_de_gaetan = mot_hasard
verif_mot(input("Entrez votre proposition: "),mot_de_gaetan) 


def nombre_lettre(mot):
    """Compter le nombre de lettres du mot choisi"""
    return len(mot)

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

    nouv_varia = [0,1,1,0,1]
    for i in range (len(mot)):
        if verif_lettre_bon_place(mot[i], mot2[i]):
            print("bonne place")
        elif verif_lettre_mauvaise_place(mot[i], mot2):
            print("mauvaise place")
        else:
            print("n'existe pas")
            
if __name__ == "__main__":
    liste_mot = open("liste_mot.csv") 
    liste_de_mots = list(csv.DictReader(liste_mot, delimiter = ";"))
    mot_a_deviner = mot_hasard(liste_de_mots)
    verif_mot( ,mot_a_deviner )
    verif_mot(input("Entrez votre proposition: "),mot_de_gaetan)
