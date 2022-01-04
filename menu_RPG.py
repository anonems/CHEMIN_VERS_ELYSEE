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

#   importation des parties du jeu
from fonctions import un_quatre,oui_non,un_cinq
from inventaire_RPG import inventaire_choix_principal
import os #ceci nous servira pour l'option clear
import sys  #ceci nous servira pour l'interruption du jeu

#   premier menu qui s'affiche au joueur, il ne s'affiche qu'au début du jeu.
def premier_menu():
  print('\033[1m' + "==========LE CHEMIN VERS L'ELYSEE==========" + '\033[0m')
  print(" Choisir 1, 2, 3 ou 4. ")
  print("-1- Nouvelle partie")
  print("-2- Partie sauvegardée")
  print("-3- Infos")
  print("-4- Quitter")
  return un_quatre()

#   le menu principale et en réalité un menu secondaire, qui ne saffiche que sur demande du joueur lorsque le joystick est actionner.
def menu_principale():
  print('\033[1m' + "==========MENU PRINCIPAL==========" + '\033[0m')
  print(" Choisir 1, 2, 3 ou 4. ")
  print("-1- Inventaire")
  print("-2- Clear")
  print("-3- Infos")
  print("-4- Quitter")
  return un_quatre()

#   execution des choix a partir du menu principale
def action_menu_principale(sauver):
  res=menu_principale()
  if res==1:  # affichage de l'inventaire
    inventaire_choix_principal()
  elif res==2:  # nettoyage de la console
    print("voulez-vous nettoyer la console ?")
    if oui_non():
      os.system('cls')  # nettoyage de la console
      action_menu_principale(sauver)
    else:
      action_menu_principale(sauver)
  elif res==3:  # affichage des infos
    print("Vous êtes actuellement au niveau ",sauver)
    print(
      "Nom du projet :  Le chemin vers l\'elysée  \n"
      "Membres du groupe de 4 :                   \n"
      "                       HAKIRI Emir         \n"
      "                       LIMACO DIEGO        \n"
      "                       MUGUET Benoit       \n"
      "                       ROY Accene          \n"
      "                       FERNANDES Guy       \n"
      "Lieu : HETIC                               \n"
      "Encadrement : JANIN Loïc                   \n"
      "Language de programation : Python          \n"
      "Date de rendu limite : 5 janvier 2022        "
    )
  elif res==4:  # quiter le jeu
    print("Voulez-vous vraiment quitter le jeu ?")
    if oui_non():
      print("Voulez-vous sauvegarder le jeu ?")
      if oui_non():
        sauvegarde(sauver)
        print("**************************----------- A BIENTOT ------------*************************")
        sys.exit()  # extinction du jeu
        return
      else :
        print("**************************----------- FIN DU JEU ------------*************************")
        sys.exit()
    else :
      action_menu_principale()
  return res

#   afficher un barre de sauvegarde.
def load_saved_game() :
  print("Sauvegarde en cours, veuillez patienter...")
# barre de chargement
  from time import sleep
  from tqdm import tqdm
  for i in tqdm(range(10)):
    sleep(0.2)

#   fonction de sauvegarde du jeuy.
def sauvegarde(niv):
  load_saved_game()
  import pickle
  
  #Initialisation de la variable de sauvegarde
  niveau_sauvegarde = niv

  #Enregistrement de la variable dans le fichier sous forme de liste
  variables = [niveau_sauvegarde]
  fichierSauvegarde = open("sauvegarde_rpg","wb")
  pickle.dump(variables, fichierSauvegarde)
  fichierSauvegarde.close()
  return

#   affichage du menu joystick.
def joystick():
  print(" ")
  print('\033[1m' + "==========JOYSTICK==========" + '\033[0m')
  print(" Choisir 1, 2, 3, 4 ou 5. ")
  print("-1- AVANCER")
  print("-2- DROITE")
  print("-3- GAUCHE")
  print("-4- DEMIS-TOUR")
  print("-5- Menu principal")
  return un_cinq()

#   menu qui saffiche lors du combat.
def menu_combat():
  print('\033[1m' + "==========ATTAQUE==========" + '\033[0m')
  print(" Choisir 1, 2, 3 ou 4. ")
  print("-1- Vous attaquez")
  print("-2- Inventaire")
  print("-3- Quitter le combat")
  print("-4- Menu principal")
  return un_quatre()


'''
  
premier_menu()
choice = int(input())

def new_game() :
# ajouter le début de la partie
  pass

def load_saved_game() :
# barre de chargement
  from time import sleep
  from tqdm import tqdm
  for i in tqdm(range(10)):
    sleep(0.2)

  import time
  from progressbar import progressbar

  for i in progressbar.progressbar(range(100)):
    time.sleep(0.02)
# ajouter la fonction de savegarde (savegame())

def info() :
  print('\033[1m' + "==========LE CHEMIN VERS L'ELYSEE==========" + '\033[0m')
  print("                            ")
  print("\033[1m" + "Groupe 22" + '\033[0m')
  print("                            ")
  print("---------------")
  print("HAKIRI Emir")
  print("LIMACO Diego")
  print("MUGUET Benoit")
  print("ROY Accene")
  print("YE FERNANDES Guy")
  print("                            ")


def quit() :
    if choice == 4 :
      print("Vous avez quitté le jeu")

if choice < 0 or choice > 4 :
  print("Veuillez séléctionner un des numéro afficher")
if choice == 1 :
  new_game()
if choice == 2 :
  load_saved_game()
if choice == 3 :
  info()
if choice == 4 :
  quit()

def sauvegarde() :
# ajouter la fonction de sauvegarde
  pass
def menu_principale():
  return
  '''
