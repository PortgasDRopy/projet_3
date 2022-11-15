from random import randint
def shifumi():
    '''simule une partie de pierre-feuille-ciseaux contre l'ordinateur'''
    score_joueur = 0
    score_ordi = 0
    while score_joueur < 3 and score_ordi < 3:
        joueur = input("pierre = 0, feuille = 1, ciseaux = 2 ")
        while joueur not in ["0","1","2"]:
            joueur = input("Il faut rentrer un nombre compris entre 0 et 2 inclus ")
        ordi = randint(0,2)
        if int(joueur) == ordi:
            print("C'est une égalité")
        elif int(joueur) + 1 % 3 == ordi:
            print("Tu as perdu")
            score_ordi += 1
        else:
            print("Tu as gagné")
            score_joueur += 1
    if score_joueur == 3:  
        print("Tu as gagné la partie, GG!")
    else: 
        print("Tu as perdu la partie, RIP Bozo!")
           
shifumi()