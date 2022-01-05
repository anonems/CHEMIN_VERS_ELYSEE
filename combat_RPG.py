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

from random import randint
from menu_RPG import menu_combat,action_menu_principale
from inventaire_RPG import inventaire_ajout_objet, inventaire_choix_principal,inventaire_ajout_electeurs

#     class permettant la creation de personnages
class Personnage :
    def __init__(self,nom,points_vie,arme,xp,) -> None:
        self.nom = nom
        self.points_vie = points_vie
        self.arme = arme
        self.xp = xp   

#       creation de personnages clef dans le jeu
player = Personnage("Player",100,"Poing Américain",1)
boss_hidalgo = Personnage("Hidalgo",50,"Arc",2)
boss_melenchon = Personnage("Mélenchon",100,"Batte de baseball",3)
boss_zemmour = Personnage("Zemmour",150,"Gaz lacrymogène",4)
boss_lepen = Personnage("Le Pen",200,"Marteau",5)
boss_macron = Personnage("Macron",300,"Stylo à bille",6)

#       les actions possible dans le combat
def ask_action_combat(nb_rencontre) :
    choix_menu_combat=menu_combat()
    if choix_menu_combat == 1 :
        print("Vous décidez d'attaquer...")
        return choix_menu_combat
    elif choix_menu_combat == 2 :
        print("Ouverture de l'inventaire...")
        inventaire_choix_principal()
        return choix_menu_combat
    elif choix_menu_combat == 3 :
        print("Vous aller quitter le combat...")
        return choix_menu_combat
    elif choix_menu_combat == 4:
        action_menu_principale(nb_rencontre)
        return choix_menu_combat

#       fonction permettant au joueur et a l'adversaire l'utilisation d'une arme
def attaque_player(name,arme) :
    if arme == "Poing Américain" :
        dmg = randint(1,10) #   variable au qui possede un valeur aleatoire qui correspond au dommage causer par l'arme
        print(name,"attaque avec un(e)",arme,"et fait :",dmg,"points de dégats")
        return dmg
    elif arme == "Arc" :
        dmg = randint(1,15)
        print(name,"attaque avec un(e)",arme,"et fait :",dmg,"points de dégats")
        return dmg
    elif arme == "Batte de baseball" :
        dmg = randint(1,20)
        print(name,"attaque avec un(e)",arme,"et fait :",dmg,"points de dégats")
        return dmg
    elif arme == "Gaz lacrymogène" :
        dmg = randint(1,20)
        print(name,"attaque avec un(e)",arme,"et fait :",dmg,"points de dégats")
        return dmg
    elif arme == "Marteau" :
        dmg = randint(1,30)
        print(name,"attaque avec un(e)",arme,"et fait :",dmg,"points de dégats")
        return dmg
    elif arme == "Stylo à bille" :
        dmg = randint(1,40)
        print(name,"attaque avec un(e)",arme,"et fait :",dmg,"points de dégats")
        return dmg

#       fonction principale de combat.
def combat(nb_rencontre) :
    print("------------------------------------------")
    print("VOUS ENTREZ EN COMBAT")
    print("------------------------------------------")

    #   attribution de l'adversaire de combat selon le niveau du jeu
    if nb_rencontre == 1 :
        adversaire = boss_hidalgo
    elif nb_rencontre == 2 :
        adversaire = boss_melenchon
    elif nb_rencontre == 3 :
        adversaire =boss_zemmour
    elif nb_rencontre == 4 :
        adversaire = boss_lepen
    elif nb_rencontre == 5 :
        adversaire = boss_macron

    continu = True
    #   informations sur l'etat du joueur et de son adversaire
    print("")
    print("Vous :",player.nom,"vous êtes équipé d'un(e)",player.arme,"et vous êtes niveau",player.xp)
    print("Vous affrontez :",adversaire.nom,"de niveau",adversaire.xp,"possédant un(e)",adversaire.arme)
    print("")
        #   boucle principale du jeu

    while continu :
        print("------------------------------------------")
        choix_action_combat=ask_action_combat(nb_rencontre)
        print("------------------------------------------")
        if choix_action_combat == 1: 
            degats_joueur = attaque_player(player.nom,player.arme)
            degats_ennemi = attaque_player(adversaire.nom,adversaire.arme)
            print("")
            player.points_vie = player.points_vie - degats_ennemi
            adversaire.points_vie = adversaire.points_vie - degats_joueur
            if player.points_vie <= 0 :
                player.points_vie = 0
                continu=False
                inventaire_ajout_electeurs(10)
                print("Vous avez perdu")
                print("------------------------------------------")
                continu = False
                return True
            elif adversaire.points_vie <= 0 :
                adversaire.points_vie = 0
                player.xp = adversaire.xp + 1
                player.arme = adversaire.arme
                player.points_vie = player.points_vie + 200
                inventaire_ajout_objet(adversaire.arme)
                inventaire_ajout_electeurs(100)
                print("Vous avez gagné le combat, vous passez niveau",player.xp-1,"vous gagnez 200 points de vie et vous remportez",player.arme)
                continu = False
                return True
            print("Il vous reste",player.points_vie,"points de vie")
            print("L'ennemi à",adversaire.points_vie,"points de vie")

        elif choix_action_combat==3:
            return True
            
