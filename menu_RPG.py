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
from fonctions import un_quatre,oui_non,un_cinq
from inventaire_RPG import inventaire

def premier_menu():
  print('\033[1m' + "==========LE CHEMIN VERS L'ELYSEE==========" + '\033[0m')
  print(" Choisir 1, 2, 3 ou 4. ")
  print("-1- Nouvelle partie")
  print("-2- Partie sauvegardée")
  print("-3- Infos")
  print("-4- Quitter")
  return un_quatre()

def menu_principale():
  print('\033[1m' + "==========MENU PRINCIPALE==========" + '\033[0m')
  print(" Choisir 1, 2, 3 ou 4. ")
  print("-1- Inventaire")
  print("-2- Clear")
  print("-3- Infos")
  print("-4- Quitter")
  return un_quatre()

def action_menu_principale(sauver):
  res=menu_principale()
  if res==1:
    inventaire()
  elif res==2:
    print("voulez-vous nettoyer la console ?")
  elif res==3:
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
  elif res==4:
    print("Voulez-vous vraiment quitter le jeu ?")
    if oui_non():
      print("Voulez-vous sauvegarder le jeu ?")
      if oui_non():
        sauvegarde(sauver)
        print("A bientot...")
        return
      else :
        print("Fin du jeu.")
        return 
  return res

def sauvegarde(niv):
  import pickle
  #Enregistrer mes variables sous forme d'une liste dans un fichier
  #Initialisation des variables
  niveau_sauvegarde = niv

  #Enregistrement des variables dans le fichier
  variables = [niveau_sauvegarde]
  fichierSauvegarde = open("sauvegarde_rpg","wb")
  pickle.dump(variables, fichierSauvegarde)
  fichierSauvegarde.close()
  return


def joystick():
  print(" ")
  print('\033[1m' + "==========JOYSTICK==========" + '\033[0m')
  print(" Choisir 1, 2, 3 ou 4. ")
  print("-1- HAUT")
  print("-2- DROITE")
  print("-3- GAUCHE")
  print("-4- DEMIS-TOUR")
  print("-5- Menu principale")
  return un_cinq()

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
