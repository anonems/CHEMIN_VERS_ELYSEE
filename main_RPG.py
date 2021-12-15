'''
Nom du projet : " Le chemin vers l'elysée "
Membres du groupe de 4 :
                        HAKIRI Emir
                        LIMACO DIEGO
                        MUGUET Benoit
                        ROY Accene
                        YE FERNANDES Guy
Lieu : HETIC
Encadrement : JANIN Loïc 
Language de programation : Python
Date de rendu limite : 5 janvier 2022
'''
#   importation des differentes parties du jeu
#from menu_RPG import menu
#from inventaire_RPG import *
#from combat_RPG import *
from deplacement_RPG import deplacement_un,deplacement_deux,deplacement_trois,deplacement_quatre,deplacement_cinq

#   Fonction de test oui ou non.
def oui_non():
  urep = input()
  if urep == 'OUI' or urep=='oui':
    return True
  elif urep == 'NON' or urep=='non':
    return False
  while  urep != 'OUI' or urep!='oui' or urep != 'NON' or urep!='non' :
    print('erreur, choisissez oui ou non')
    urep = input()
    if urep == 'OUI' or urep=='oui':
      return True
    elif urep == 'NON' or urep=='non':
      return False

#   fonction principale du jeu.
def main_rpg():

  sauvegarde=""  #    permet le retour au niveau sauvgarder
    
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

  print("**************************----------- Début du jeu ------------*************************")
  #   recuperation du nom du joueur.
  print("votre nom ?")
  nom=input()

  #   presentation du jeu.
  print("Cher(e) candidat(e) à l'éléction présidentielle 2022;\n"
      "Dans ce jeu vous devrez tout faire pour arriver à l'élysée,\n"
      "plusieurs étapes avant d'arriver à l'élysée et de jouer le combat finale...\n"
      "Vous trouverez sur votre chemin des obstacles, des combats, des élécteurs...\n"
      "Après chaque combat vous aurez la possibilité d'augmenter vos points de vies selon le stock de potions que vous disposez.\n"
      "Vous pouvez arreter le jeu à tout moment, mais si vous n'avez plus de vie : le jeu est terminé!\n"
      "Le but final est de battre 'Alexandre', le gardien de l'elysée,\n"
      "ce qui vous permetra de passer au decomptage de electeurs que vous aurez acheter ou gagné,\n"
      "Attention ! si vous avez moins de 5 élécteurs vous perdez le jeu.\n"
      "\n")

  #   première interaction avec le joueur, qui n'a aucun effet sur le joueur, met qui permet de ne pas fatigué le joueur avec trop de lecture.
  print("Vous êtes prêt ?")
  if oui_non() :
      print("C'est parti...")
  else :
      print("Tant-pis, c'est parti quand même...")
  ##   Lancement des cinq étape du jeu, une etape n'est abordé que si l'étape précédente est validé.
  if deplacement_un() or sauvegarde == "etape_un": #   première etape du jeu : combat de rue; personnage clef : Hidalgo
      if deplacement_deux() or sauvegarde == "etape_deux": #   deuxième étape du jeu : combat dans un meeting; personnage clef : zemmour
          if deplacement_trois() or sauvegarde == "etape_trois":  #   troisième étape du jeu : combat dans un plateau TV; personnage clef : Mélanchon
              if deplacement_quatre() or sauvegarde == "etape_quatre": #   quatrième étape du jeu : combat dans un café; personnage clef : le pen
                if deplacement_cinq() or sauvegarde == "etape_cinq": #   dernière étape du jeu : combat à l'élysée; personnage clef : benalla
                  #   une fois toutes les étapes validées, fin du jeu.
                  print("BRAVO ! VOUS AVEZ GAGNE")
                  print("**************************----------- FIN DU JEU ------------*************************")
                  return


##################################-------Lancement du jeu-------######################################
main_rpg()