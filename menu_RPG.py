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

def menu():
  print('\033[1m' + "==========LE CHEMIN VERS L'ELYSEE==========" + '\033[0m')
  print("                                 ")
  print("1. Nouvelle partie")
  print("2. Partie sauvegardée")
  print("3. Infos")
  print("4. Quitter")

menu()
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

def save_game() :
# ajouter la fonction de sauvegarde
  pass
