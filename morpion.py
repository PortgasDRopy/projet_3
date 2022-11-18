from operator import xor
jeu = {}

def aligne(case):
    '''Renvoie True si l'un des deux joueurs à gagner, False sinon'''
    ligne = 0
    colonne = 0
    diagonale = 0
    for coordonnees in jeu.keys():
        if coordonnees != case:
            if coordonnees[1] == case[1]:
                if jeu[coordonnees] == jeu[case]:
                    colonne +=1
            if coordonnees[4] == case[4]:
                if jeu[coordonnees] == jeu[case]:
                    ligne += 1
            if not xor(case[1] == '1', case[4] == '1'):
                if not xor(coordonnees[1] == '1', coordonnees[4] == '1') and coordonnees[1] != case[1] and coordonnees[4] != case[4]:
                    if jeu[coordonnees] == jeu[case]:
                        diagonale += 1
    if ligne == 2 or colonne == 2 or diagonale == 2:
        return True
    return False

def morpion():
    '''Simule une partie de morpion entre deux joueurs'''
    victoire = False
    egalite = False
    tour = -1
    for x in range(3):
        for y in range(3):
            jeu[str((x, y))] = " "
    while not victoire and not egalite:
        tour += 1
        if tour % 2 == 0:
            j1 = input("Choisis un duo de coordonnées (x, y) : ")
            while j1 not in jeu.keys() or jeu[j1] != " ":
                j1 = input("Choisis un duo de coordonnées (x, y) valide STP. ")
            jeu[j1] = "O"
            victoire = aligne(j1)
            print(" ", jeu["(0, 2)"], "|", jeu["(1, 2)"], '|', jeu["(2, 2)"], "\n", "-----------", "\n", "", jeu["(0, 1)"], "|", jeu["(1, 1)"], "|", jeu["(2, 1)"], "\n", "-----------", "\n", "", jeu["(0, 0)"], "|", jeu["(1, 0)"], "|", jeu["(2, 0)"])
        else:
            j2 = input("Choisis un duo de coordonnées (x, y) : ")
            while j2 not in jeu.keys() or jeu[j2] != " ":
                j2 = input("Choisis un duo de coordonnées (x, y) valide STP.")
            jeu[j2] = "X"
            victoire = aligne(j2)
            print(" ", jeu["(0, 2)"], "|", jeu["(1, 2)"], '|', jeu["(2, 2)"], "\n", "-----------", "\n", "", jeu["(0, 1)"], "|", jeu["(1, 1)"], "|", jeu["(2, 1)"], "\n", "-----------", "\n", "", jeu["(0, 0)"], "|", jeu["(1, 0)"], "|", jeu["(2, 0)"])
        if tour == 8:
            print("C'est une égalité ! Domaj")
            egalite = True
    if victoire :
        if tour % 2 == 0:
            print("Bravo J1 tu as gagné ! Sale BG")
        else:
            print("Bravo J2 tu as gangé ! Gigachad")

morpion()

        


    

