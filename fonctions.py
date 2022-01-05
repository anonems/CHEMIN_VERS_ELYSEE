#   permet de faire un choix entre oui et non.
def oui_non():
  print("Choisir oui ou non.")
  urep = input()
  if urep == 'OUI' or urep=='oui':
    return True
  elif urep == 'NON' or urep=='non':
    return False
  while  urep != 'OUI' or urep!='oui' or urep != 'NON' or urep!='non' :
    print('ERREUR ! choisissez oui ou non.')
    urep = input()
    if urep == 'OUI' or urep=='oui':
      return True
    elif urep == 'NON' or urep=='non':
      return False


#   permet de faire un choix entre les chiffres 1 et 2.
def un_deux():
  urep = input()
  if urep == '1' :
    return True
  elif urep == '2' :
    return False
  while  urep != '1' or urep!= '2' :
    print('ERREUR ! choisissez 1 ou 2.')
    urep = input()
    if urep == '1' :
      return True
    elif urep == '2':
      return False

#   permet de faire un choix entre les chiffres 1, 2, 3 ou 4.
def un_quatre():
  urep = input()
  if urep == '1' :
    return 1
  elif urep == '2' :
    return 2
  elif urep == '3' :
    return 3
  elif urep == '4' :
    return 4
  while  urep!='1' or urep!='2' or urep!='3' or urep!='4':
    print('ERREUR ! choisissez 1, 2, 3 ou 4.')
    urep = input()
    if urep == '1' :
      return 1
    elif urep == '2' :
      return 2
    elif urep == '3' :
      return 3
    elif urep == '4' :
      return 4

#   permet de faire un choix entre les chiffres 1, 2, 3, 4 ou 5.
def un_cinq():
  urep = input()
  if urep == '1' :
    return 1
  elif urep == '2' :
    return 2
  elif urep == '3' :
    return 3
  elif urep == '4' :
    return 4
  elif urep == '5' :
    return 5
  while  urep!='1' or urep!='2' or urep!='3' or urep!='4' or urep!='5':
    print('ERREUR ! choisissez 1, 2, 3, 4 ou 5.')
    urep = input()
    if urep == '1' :
      return 1
    elif urep == '2' :
      return 2
    elif urep == '3' :
      return 3
    elif urep == '4' :
      return 4
    elif urep == '5' :
      return 5

#   presentation print rpg.
def presentation_rpg():
  print("___________________________________________________________________________________________")
  print("\n")
  print(
  "#################              ################                 ############################\n"
  "##              ##             ##              ##               ##                        ##\n"
  "##               ##            ##                ##             ##                        ##\n"
  "##                ##           ##                  ##           ##                        ##\n"
  "##                ##           ##                  ##           ##                          \n"
  "##               ##            ##                ##             ##                          \n"
  "##              ##             ##################               ##                          \n"
  "##            ##               ##                               ##                          \n"
  "##          ##                 ##                               ##              ############\n"
  "##        ##                   ##                               ##              ##        ##\n"
  "##          ##                 ##                               ##              ##        ##\n"
  "##            ##               ##                               ##                        ##\n"
  "##              ##             ##                               ##                        ##\n"
  "##                ##           ##                               ############################\n"
  )
  print("\n")
  print("___________________________________________________________________________________________")
  return

def about(): 
  print(
  "Nom du projet :  Le chemin vers l'elysée \n"
  "Membres du groupe de 5 ainsi que leurs rôles :\n"
  "                                             HAKIRI Emir --> Chef de projet & rassemblement des parties, parties deplacament_RPG.py, main_RPG.py\n"
  "                                             LIMACO DIEGO --> Gestion de l'inventaire, partie inventaire_RPG.py\n"
  "                                             MUGUET Benoit --> Gestion des combats, partie combat_RPG.py\n"
  "                                             ROY Accene --> Gestion des menus et de la sauvegarde, partie menu_RPG.py\n"
  "                                             FERNANDES Guy --> Assistance et narration (NB : malade au moment du projet)\n"
  "Lieu : HETIC\n"
  "Encadrement : JANIN Loïc\n"
  "Language de programation : Python\n"
  "Date de rendu limite : 5 janvier 2022\n"
  "But du jeu : Le joueur se met dans la peau d'un candidat à la presidentielle, il doit recolté le plus d'élécteurs et combattre les autre candidat pour gagné sa place à l'élysée.\n"
  "\n"
  "Déroulement du jeu :\n"
  "Le jeu est en 5 étapes (ou niveaux), chaqu'un de ces niveau est caractériser par un candidat à la présidentielle qui est mis dans un contexte autour duquel sera formé,\n"
  "au fur et mesure des interactions du joueur, une situation menant à un combat.\n"
  "Les personnages cles sont les suivants, dans l'ordre du jeu : -Hidalgo --> La marre de Paris\n"
  "                                                              -Zemmour --> The hummour\n"
  "                                                              -Melanchon --> Melonchaud\n"
  "                                                              -Le Pen --> Pas la peine\n"
  "                                                              -Benalla --> Alexandre\n"
  "\n"
  "\n"
  "Comment gagné le jeu ? :\n"
  "Pour gagné le jeu il faut reussir à arriver à la dernière et 5e étape, battre le dernier boss, et tout d'abord avoir recolté plus de 60 élécteurs.\n"
  "\n"
  "\n"
  "Comment se déroule les combats ? :\n"
  "Une fois le cambat déclancher le joueur à le choix de combattre ou de quitter le combat, si le joueur combat jusqu'au bout et gagne le combat,\n"
  "il repare avec 200 points de vie, 100 élécteurs, et l'arme de son adversaire.\n"
  "En revenche si il perd le combat, (c'est à dire qu'il n'a plus de points de vie), il repare qu'avec 10 élécteurs, puis il passe au niveau suivant (à part le 3e combat, si il le perd il perd le jeu).\n"
  "\n"
  "\n"
  "Qu'en est-il des menus ? :\n"
  "dans le jeu nous avons 5 menus différents :\n"
  "Le premier menu :\n"
  "Le premier menu ne s'affiche qu'une seule fois, au lancement du programme, il permet au joueur de : -Démarrer une nouvelle partie\n"
  "                                                                                                    -Reprendre à un niveau sauvegarder\n"
  "                                                                                                    -Lire ce que vous lisez à linstant\n"
  "                                                                                                    -Quitter le jeu\n"
  "\n"
  "Le menu principale :\n"
  "Le menu principale s'affiche parmis les choix du joystick, une fois selectionner il permet au joueurs de : -Visualiser l'inventaire\n"
  "                                                                                                           -Nettoyer la console\n"
  "                                                                                                           -Lire ce que vous lisez à l'instant\n"
  "                                                                                                           -Quitter & sauvegarder le jeu, si vous choisissez quitter une option de sauvegarde s'affichera\n"
  "\n"
  "le joystick :\n"
  "Le joystick s'affiche à chaque fois que le joueur est appelé à se déplacer, il permet au joueur de : -Avancer\n"
  "                                                                                                     -Se diriger à droite\n"
  "                                                                                                     -Se diriger à gauche\n"
  "                                                                                                     -Faire de mis-tour\n"
  "                                                                                                     -Afficher le menu principale\n"
  "(NB : le joystick à pour but de crée une interraction avec le joueur, de se déplacer d'un niveau à un autre et de crée un systeme de récompense au déplacement avec des objets qui apparaisse lorsque le joueur se déplace et qui peuvent étre ajouter à l'inventaire.)\n"
  "\n"
  "Le menu attaque :\n"
  "Le menu attaque apparaît lorsque le joueur rentre en mode combat, il permet au joueur de : -Attaquer\n"
  "                                                                                           -Afficher l'inventaire\n"
  "                                                                                           -Quitter le combat\n"
  "                                                                                           -Afficher le menu principale\n"
  "\n"
  "L'inventaire :\n"
  "L'inventaire à cet étape du projet n'ai pas vraiment un menu, il permet seulement de visualiser les objet recoltés pendant les déplacements, et d'afficher le nombre d'élécteurs gagné.\n"
  "\n"
  "Le vrai but de l'inventaire aurai été de non seulement voir les objet gagné mais en plus de pouvoir les utilisé, mais le temps ne nous à pas permis d'appliquer cette fonctionnalité.\n"
  "\n"
  "autre chose ? :\n"
  "Le fichier fonction.py regroupes les fonctions les plus utilisées dans le programme.\n"
  )
