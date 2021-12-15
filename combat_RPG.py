from random import randint
class Personnage :
    def __init__(self,nom,points_vie,arme,xp,) -> None:
        self.nom = nom
        self.points_vie = points_vie
        self.arme = arme
        self.xp = xp
    

player = Personnage("Benoit",100,"Poing Américain",1)
boss_hidalgo = Personnage("Hidalgo",50,"Arc",2)
boss_melenchon = Personnage("Mélenchon",100,"Batte de baseball",3)
boss_zemmour = Personnage("Zemmour",150,"Gaz lacrymogène",4)
boss_lepen = Personnage("Le Pen",200,"Marteau",5)
boss_macron = Personnage("Macron",300,"Stylo à bille",6)



def ask_action_combat() :
    player_choice = ""
    while player_choice not in ["1","2","3"] :
        print("1 : vous attaquez - 2 : inventaire - 3 : quitter le combat (Vous n'obtiendez ni l'arme de votre adversaire ni son niveau)")
        player_choice = input()
    if player_choice == "1" :
        print("Vous décidez d'attaquer")
    elif player_choice == "2" :
        print("Ouverture de l'inventaire")
    elif player_choice == "3" :
        print("Vous aller quitter le combat")
        




def attaque_player(name,arme) :
    if arme == "Poing Américain" :
        dmg = randint(1,10)
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


# Rue : Hidalgo
# Meeting : Mélenchon
# TV : Zemmour
# Café : Le Pen
# Elysée : Macron

# Les armes et les dégats :
# Poing Américain : 10
# Arc : 5
# Batte de baseball : 10
# Gaz lacrymogène : 15
# Marteau : 20
# Stylo à bille : 30


def combat_description(level) :
    if level == "rue" :
        print("Vous étiez en train de marcher tranquillement dans les rues de Paris ...")
        print("Vous avez beau tourner la tête à gauche et à droite, il y a des travaux partout.")
        print("Vous décidez d'enjamber une barrière quand tout à coup ...")
    if level == "meeting" :
        print("Un imposant batiment se trouve en façe de vous ...")
        print("Vous décidez de rentrer ...")
        print("Après un long couloir sombre, vous apercevez une tribune pleine ainsi qu'un petit homme au loin sur une scène")
        print("Vous vous rapprochez de cette personne, elle vous dévisage et vous saute dessus en un éclair")
    if level == "tv" :
        print("Votre meilleur ami vous a invité à assister à une émission télévisée.")
        print("Plusieurs fois vous lui avez demandé ce que c'était mais il a toujours refusé de vous répondre")
        print("Vous décidez de lui faire confiance et de l'accompagner")
        print("Une fois sur place, vous constatez que vous êtes dans les locaux de Touche Pas à Mon Poste ...")
        print("Vous aimez bien Cyril Hanouna mais lorsque vous decouvrez son invité, vous décidez d'intervenir...")
    if level == "cafe" :
        print("Cela fait maintenant plusieurs heures que vous marchez dans les rues de cette ville que vous ne connaissez pas")
        print("Il fait très chaud et vous avez de plus en plus soif")
        print("Tout à coup vous apercevez un cafe au loin. il semble désert mis à part une personne de dos que vous distinguez à peine")
        print("Vous décidez de vous rapprocher et, une fois au comptoir, après avoir commandé votre pinte, la personne se retourne ...")
    if level == "elysee" :
        print("Félicitations, vous êtes parvenu au plus au niveau de l'Etat (et du jeu), il ne vous reste plus qu'une seule chose à accomplir :")
        print("Vaincre le propriétaire des lieux et ainsi prendre sa place !!!")
        print("Bonne chance")



def combat(nb_rencontre) :
    print("------------------------------------------")
    print("VOUS ENTREZ EN COMBAT")
    print("------------------------------------------")
    if nb_rencontre == 1 :
        adversaire = boss_hidalgo
        combat_description("rue")
    elif nb_rencontre == 2 :
        adversaire = boss_melenchon
        combat_description("meeting")
    elif nb_rencontre == 3 :
        adversaire =boss_zemmour
        combat_description("tv")
    elif nb_rencontre == 4 :
        adversaire = boss_lepen
        combat_description("cafe")
    elif nb_rencontre == 5 :
        adversaire = boss_macron
        combat_description("elysee")
    
    skip_turn = False
    continu = True
    while True and continu :
        if skip_turn :
            print("Vous passez votre tour") 
            skip_turn = False
        else :
            print("")
            print("Vous êtes :",player.nom,"vous êtes équipé d'un(e)",player.arme,"et vous êtes niveau",player.xp)
            print("Vous affrontez :",adversaire.nom,"de niveau",adversaire.xp,"possédant un(e)",adversaire.arme)
            print("")
            while continu == True or player.points_vie > 0 and adversaire.points_vie > 0 :
                print("------------------------------------------")
                ask_action_combat()
                print("------------------------------------------")
                degats_joueur = attaque_player(player.nom,player.arme)
                degats_ennemi = attaque_player(adversaire.nom,adversaire.arme)
                print("")
                player.points_vie = player.points_vie - degats_ennemi
                adversaire.points_vie = adversaire.points_vie - degats_joueur
                if player.points_vie <= 0 :
                    player.points_vie = 0
                    print("Vous avez perdu")
                    print("------------------------------------------")
                    continu = False
                if adversaire.points_vie <= 0 :
                    adversaire.points_vie = 0
                    player.xp = adversaire.xp + 1
                    player.arme = adversaire.arme
                    player.points_vie = player.points_vie + 200
                    print("Vous avez gagné le combat, vous passez niveau",player.xp,"vous gagnez 200 points de vie et vous remportez",player.arme)
                    continu = False
                print("Il vous reste",player.points_vie,"points de vie")
                print("L'ennemi à",adversaire.points_vie,"points de vie")


combat(1)
combat(2)
combat(3)
combat(4)
combat(5)