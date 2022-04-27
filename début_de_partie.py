import csv 
liste_mot = open("liste_mot.csv") 
t1 = list(csv.DictReader(liste_mot, delimiter=";")) 

def mot_hasard():
    import random
    hasard = random.choice(t1)
