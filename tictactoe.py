import random

from essai2 import initialiser_jeu, jouer_partie



#Initialisation du jeu:
print("Bienvenue dans le jeu: Tic Tac Toe ​")
while True:
    try:
        mode_de_jeu = int(input("Choisissez le mode de jeu:\n" \
                                "1- Jouer avec un autre Joueur:\n" \
                                "2- Jouer avec un Robot: "))
        if mode_de_jeu in [1, 2]:
            break
        else:
            print("Veuillez choisir 1 ou 2.")
    except ValueError:
        print("Entrée invalide. Veuillez entrer 1 ou 2.")

if mode_de_jeu == 1:
    print("\n Mode Joueur vs Joueur sélectionné")
    joueur_1 = input("Joueur 01 (X), quel est votre prénom ? ")
    joueur_2 = input("Joueur 02 (O), quel est votre prénom ? ")
    print(f"\nBienvenue {joueur_1} (X) et {joueur_2} (O) ! Le jeu peut commencer.")

elif mode_de_jeu == 2:
    print("\n Mode Joueur vs Robot sélectionné")
    joueur_1 = input("Joueur 01 (X), quel est votre prénom ? ")
    joueur_2 = "Robot IA"
    print(f"\nBienvenue {joueur_1} (X) ! Votre adversaire est le {joueur_2} (O). Le jeu peut commencer.")




#Configuration du tableau de jeu
tableau = ["-","-","-", 
            "-","-","-", 
            "-","-","-"]        
joueur_actuel = "X"
partie_en_cours = True
victoire = False
nombre_de_coups = 0


def afficher_tableau(tableau):

    print("\n")
    print(tableau[0] + " | " + tableau[1] + " | " + tableau[2])
    print("---------") 
    print(tableau[3] + " | " + tableau[4] + " | " + tableau[5])
    print("---------") 
    print(tableau[6] + " | " + tableau[7] + " | " + tableau[8])
    print("\n")





#Partie Jouer avec un autre joueur:
def prendre_input_joueur(tableau, joueur_actuel, nom_joueur):
    while True:
        try:
            position = int(input(f"{nom_joueur} ({joueur_actuel}), choisissez une case (1-9): ")) - 1
            if 0 <= position <= 8:
                if tableau[position] == "-":
                    tableau[position] = joueur_actuel
                    return True
                else:
                    print("Oups, cette case est déja choisie. Veuillez choisir un autre case valide" )
            else:
                print("Entrée invalide. Veuillez entrer un nombre (1 à 9)")

        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre (1 à 9)")




#Partie Robot:
def prendre_input_robot(tableau, joueur_actuel):
    joueur_2 = "Robot IA"
    print(f"{joueur_2} ({joueur_actuel}) joue..")

    coups_possibles= []
    for i, case in enumerate(tableau):
        if case == "-":
            coups_possibles.append(i)

    if coups_possibles:
        position = random.choice(coups_possibles)
        tableau[position] = joueur_actuel
        return True 
    
    return False 



#Vérification de victoire:
def verifier_victoire(tableau):
    global victoire

    lignes = [
        [tableau[0], tableau[1], tableau[2]],
        [tableau[3], tableau[4], tableau[5]],
        [tableau[6], tableau[7], tableau[8]],
    ]

    colonnes = [
        [tableau[0], tableau[3], tableau[6]],
        [tableau[1], tableau[4], tableau[7]],
        [tableau[2], tableau[5], tableau[8]],
    ]

    diagonales = [
        [tableau[0], tableau[4], tableau[8]],
        [tableau[2], tableau[4], tableau[6]],
    ]

    
    def verifier_alignement(alignement):
        return alignement[0] == alignement[1] == alignement[2] and alignement[0] != "-"

    for alignement in lignes + colonnes + diagonales:
        if verifier_alignement(alignement):
            victoire = True
            return True
            
    return False


def changer_joueur(joueur_actuel):
    return "O" if joueur_actuel == "X" else "X"


while partie_en_cours: 
    afficher_tableau(tableau)
    coup_joue = False
    if joueur_actuel == "X":
        coup_joue = prendre_input_joueur(tableau, joueur_actuel, joueur_1)

    elif joueur_actuel == "O":
        if mode_de_jeu == 1:
            coup_joue = prendre_input_joueur(tableau, joueur_actuel, joueur_2)
        elif mode_de_jeu == 2:
            coup_joue = prendre_input_robot(tableau, joueur_actuel)


    if coup_joue:
        nombre_de_coups += 1
        if verifier_victoire(tableau):
            
            afficher_tableau(tableau)
            nom_gagnant = joueur_1 if joueur_actuel == "X" else joueur_2
            
            print(f" Félicitations ! {nom_gagnant} ({joueur_actuel}) a gagné la partie !")
            partie_en_cours = False

        elif nombre_de_coups == 9:
            afficher_tableau(tableau)
            print("Match Nul ! Le tableau est plein, il n'y a pas de gagnant.")
            partie_en_cours = False

        else:
            joueur_actuel = changer_joueur(joueur_actuel)

print("\n--- Fin de la partie ---")



#Relancer la partie
def lancer_jeu():
    print("Bienvenue dans le jeu: Tic Tac Toe​")
    continuer_a_jouer = True
    
    while continuer_a_jouer:
        mode_de_jeu, joueur_1, joueur_2 = initialiser_jeu()

        jouer_partie(mode_de_jeu, joueur_1, joueur_2)
        while True:
            reponse = input("Voulez-vous rejouer ? (oui/non): ").lower()
            if reponse == 'oui':
                break 
            elif reponse == 'non':
                print("Merci d'avoir joué ! Au revoir")
                continuer_a_jouer = False 
                break
            else:
                print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")

lancer_jeu()