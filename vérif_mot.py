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
            
