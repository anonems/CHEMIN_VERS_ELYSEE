#   importation des parties du jeu

def menu_principale():
    print("")


choice = int(input())

def menu() :
    pv = 100
    print("1. Nouvelle partie")
    if choice == 1 :
        new_game()
    print("2. Partie sauvegardée")
    if choice == 2 :
        load_saved_game()
    print("3. Infos")
    if choice == 3 :
        info()
    print("4. Quitter")
    if choice == 4 :
        quit()

    if choice < 0 or choice > 4 :
        print("Veuillez séléctionner un des numéro afficher")
        menu()
    return choice



def new_game() :
    main_RPG()

def info() :
    print("Ce jeu à été conçu par :")
    print( "Emir : Main")
    print( "Benoit : Combat")
    print("Diego : Inventaire")
    print("Gui : Déplacement ")
    print("Accène : Menu")

def load_saved_game() :
    import time
import progressbar

for i in progressbar.progressbar(range(100)):
    time.sleep(0.02)
    new_game() 

def save_game() :

def quit() :
    if choice == quit :
        print("Vous avez quitté le jeu")
        save_game()
    

menu()