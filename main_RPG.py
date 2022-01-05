'''
Nom du projet : " Le chemin vers l'elysée "
Membres du groupe de 4 :
                        HAKIRI Emir
                        LIMACO DIEGO
                        MUGUET Benoit
                        ROY Accene
                        FERNANDES Guy
Lieu : HETIC
Encadrement : JANIN Loïc 
Language de programation : Python
Date de rendu limite : 5 janvier 2022
'''

#   importation des differentes parties du jeu
from deplacement_RPG import deplacement_un,deplacement_deux,deplacement_trois,deplacement_quatre,deplacement_cinq
from menu_RPG import premier_menu
from fonctions import oui_non,presentation_rpg,about
from inventaire_RPG import inventaire_ajout_electeurs
presentation_rpg()
#   fonction principale du jeu.
#   recuperation du nom du joueur.
print("votre nom ?")
nom_joueur=input()
nom=[nom_joueur]

print("Bonjour",nom_joueur)
print("Tes vacances se sont bien passé ?")
if oui_non():
  print("Tant-mieux.")
  print("...")
else:
  print("Tant-pis")
  print("...")
def main_rpg():
  first=premier_menu()
  sauvegarde=0  #    permet le retour au niveau sauvgarder

  #le cas où le joueur demande de commencer une nouvelle partie.
  if first == 1: 
    print("**************************----------- Début du jeu ------------*************************")
    #   presentation du jeu.
    print("Cher(e) candidat(e) à l'éléction présidentielle 2022;\n"
        "Dans ce jeu vous devrez tout faire pour être president.,\n"
        "plusieurs étapes avant d'arriver à l'élysée et de jouer le combat finale...\n"
        "Vous trouverez sur votre chemin des obstacles, des combats, des élécteurs...\n"
        "Après chaque combat vous aurez la possibilité d'augmenter vos points de vies selon le stock de potions que vous disposez.\n"
        "Vous pouvez arreter le jeu à tout moment, mais si vous n'avez plus de vie : le jeu est terminé!\n"
        "Le but final est de battre 'Alexandre', le gardien de l'elysée,\n"
        "ce qui vous permetra de passer au decomptage de electeurs que vous aurez pu ramasser sur votre chemin,\n"
        "Attention ! si vous avez moins de 60 élécteurs vous perdez le jeu.\n"
        "\n")

    #   première interaction avec le joueur, qui n'a aucun effet sur le joueur, met qui permet de ne pas fatigué le joueur avec trop de lecture.
    print("Vous êtes prêt ?")
    if oui_non() :
        print("C'est parti...")
    else :
        print("Tant-pis, c'est parti quand même...")

    ##   Lancement des cinq étape du jeu, une etape n'est abordé que si l'étape précédente est validé.
    if deplacement_un() : #   première etape du jeu : combat de rue; personnage clef : Hidalgo
      if deplacement_deux() : #   deuxième étape du jeu : combat dans un meeting; personnage clef : zemmour
        if deplacement_trois() :  #   troisième étape du jeu : combat dans un plateau TV; personnage clef : Mélanchon
          if deplacement_quatre() : #   quatrième étape du jeu : combat dans un café; personnage clef : le pen
            if deplacement_cinq() : #   dernière étape du jeu : combat à l'élysée; personnage clef : benalla
              if inventaire_ajout_electeurs(0)>60:
              #   une fois toutes les étapes validées, fin du jeu.
                print("BRAVO ! VOUS AVEZ GAGNE")
              else :
                print("DOMAGE ! Vous avez perdu.")
              print("**************************----------- FIN DU JEU ------------*************************")
              return

  #   le cas où le joueur souhaite continuer depuis une sauvegarde précédente.
  elif first == 2:
    import pickle 
    import os.path
    fichierini = "sauvegarde_rpg"
    #Ouverture du fichier si il existe et récupération de la liste
    if os.path.isfile(fichierini):
        fichierSauvegarde = open(fichierini,"rb")
        variables = pickle.load(fichierSauvegarde)
        fichierSauvegarde.close()
        #récupération des données dans les variables
        sauvegarde = variables[0]
        ##   Lancement des cinq étape du jeu, une etape n'est abordé que si l'étape précédente est validé.
        if deplacement_un() or sauvegarde == 1: #   première etape du jeu : combat de rue; personnage clef : Hidalgo
          print("Vous reprenez au niveau 1.")
          if deplacement_deux() or sauvegarde == 2: #   deuxième étape du jeu : combat dans un meeting; personnage clef : zemmour
            print("Vous reprenez au niveau 2.")
            if deplacement_trois() or sauvegarde == 3:  #   troisième étape du jeu : combat dans un plateau TV; personnage clef : Mélanchon
              print("Vous reprenez au niveau 3.")
              if deplacement_quatre() or sauvegarde == 4: #   quatrième étape du jeu : combat dans un café; personnage clef : le pen
                print("Vous reprenez au niveau 4.")
                if deplacement_cinq() or sauvegarde == 5: #   dernière étape du jeu : combat à l'élysée; personnage clef : benalla
                  print("Vous reprenez au niveau 5.")
                  #   une fois toutes les étapes validées, fin du jeu.
                  if inventaire_ajout_electeurs(0)>60:
                  #   une fois toutes les étapes validées, fin du jeu.
                    print("BRAVO ! VOUS AVEZ GAGNE")
                  else :
                    print("DOMAGE ! Vous avez perdu.")
                  print("**************************----------- FIN DU JEU ------------*************************")
                  return

    else:
        #Le fichier n'existe pas
        print("Aucun element de sauvegarde trouvé.")
        main_rpg()

  #   le cas où le joueur souhaite afficher les infos relatives au jeu.
  elif first == 3:
    about()
    main_rpg()
  #   le cas où le joueur souhaite quiter le jeu avant de le commencer.
  elif first == 4:
    print("au revoir.")
    return

##################################-------Lancement du jeu-------######################################
main_rpg()
