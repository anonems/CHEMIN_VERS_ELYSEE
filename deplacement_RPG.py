'''
Auteur : Hakiri Emir
Déscription :

'''
#   importation des parties du jeu
from random import randint
from inventaire_RPG import inventaire_ajout_objet,inventaire_ajout_electeurs
from combat_RPG import combat
from menu_RPG import joystick,menu_principale,sauvegarde
from random import randint
from main_RPG import oui_non

#   permet de definir les differents objet à recupérer l'hors du deplacement.
class Objets:
  def __init__(self, nom, tipe,effet):#nom de l'Objet,type de l'objet, seffet : point en plus ou en moins selon le type de l'objet.
    self.nom=nom
    self.tipe=tipe
    self.effet=effet

#   permet de faire un choix entre les chiffres 1 et 2.
def un_deux():
  urep = input()
  if urep == 1 :
    return True
  elif urep == 2 :
    return False
  while  urep != 1 or urep!=2 :
    print('erreur, choisissez 1 ou 2')
    urep = input()
    if urep == 1 :
      return True
    elif urep == 2:
      return False

#   permet de recuperer la commande executer dans le menu, puis l'appliquer au deplacement du joueur.
def deplacement_libre():
  print("La main est à vous, vous pouvez vous déplacer :")
  loc_map=[0,0]   #  liste composé de x : deplacement horizontal et y : deplacement verticale.
  choix=menu_principale()

  #   evolution de la position de du joueur selon la commande joystick dans le menu.
  if choix==1:
    print("Vous vous diriger tout droit...")
    loc_map[1]=(loc_map[1]+5)
  elif choix==2:
    print("Vous vous diriger à droite...")
    loc_map[0]=(loc_map[0]+5)
  elif choix==3:
    print("Vous vous diriger à gauche...")
    loc_map[0]=(loc_map[0]-5)
  elif choix==4:
    print("Vous vous faites demi-tour...")
    loc_map[1]=(loc_map[1]-5)

  #   le joueur souhaite quitter le jeu, on verifie se choix, et on propose la sauvegarde du  niveau du jeu.
  elif choix==5:
    print("vous etes sûr ?")
    if oui_non():
      print("voulez vous sauvegarder le jeu ?")
      if oui_non():
        sauvegarde()
      else :
        return "fin_jeu"

#   cette fonction permet l'apparition d'objet ai hazard sur le chemin du joueur
def objet():
  res_deplacement=deplacement_libre()
  #   definition des objet que le joueur peut trouvé et recupérer sur son chemin.
  marteau=Objets("marteau", "arme",10)
  pv=Objets("Potion de vie", "potion", 5)
  pf=Objets("Potion de force", "potion", 2)
  batb=Objets("Batte de baseboll", "arme", 15)
  pm=Objets("point amercain", "arme", 20)
  gaz=Objets("gaz piqant", "arme", 25)
  electeur=Objets("electeur", "arme", 1)
  #   choix d'un objet au hazard
  l_objets=[marteau,pv,pf,batb,gaz,electeur]
  if (res_deplacement) == ( 1 or 2 or 3 or 4):
    res=l_objets[randint(0,5)]
    print("vous avez trouver l'objet suivant :", res.nom)
    print("voulez-vous le prendre ?")
    if oui_non:
      inventaire_ajout_objet(res) #   ajout de l'objet selectionné dans l'inventaire du joueur
  return res


#   première étape du jeu
def deplacement_un():
  niveau=1
  #   premier deplacement du joueur.
  objet()
  #   contexte générale
  print("Vous êtes rue de Bercy, vous vous diriger vers l'Arena pour assiter au théatre de 'The Humour'")
  #   deuxième déplacement du joueur.
  objet()
  #   mise en situation.
  print("Attention ! une voiture roule à toute vitesse vers vous, le chauffeur vous évite et fini sa course dans une vitrine \n"
        "le chauffeur sort sain et sauf, mais qui est-ce ?\n"
        "la marre de Paris!\n"
        "votre réaction :")
  #   première combat, contre le vigile de Hidalgo.
  print("-1- Insulter") 
  print("-2- Démarer un combat")
  if un_deux:
    print(input())
    print("Hidalgo : Comment ! garde du corp attack !")
    combat(niveau)
  else:
    combat(niveau)


#  deuxième étape du jeu.
def deplacement_deux():
  niveau=2
  print("BRAVO ! vous passez au niveau 2.")
  #   deplacements libre
  objet()
  objet()
  #   contexte
  print("Vous arrivez à l'Arena, pour assiter un sketch selon vos informations, mais ... \n"
        "vous trouverez sur scene un personnage qui vous et famillier, les vannes ne vous plaisent pas ils sont selon vous déplacées.\n"
        "les gens autour de vous ne vous reconaissent pas ils commencent à vous bousculer.\n")
  #   deplacement libre
  objet()
  objet()
  #   mise en situation
  print("La plate-forme est devant vous, vous appercevez un de vos concurrent au micro, 'The humour'...")
  print("c'est à vous, faire un choix :")
  print("1 - monter sur le plate-forme ?")
  print("2 - huer contre 'The humour'")
  if un_deux():
    #   combat contre the humour, repartir avec ses fan si combat gagné.
    combat(niveau)
  else :
    #   combat contre les fan de the humour.
    combat(22)

#   combat pour le troisième niveau.
def event_etape_trois():
  #   definition de quelques citations de melanchon
  l_clache_melonchaud=["Dans ma longue vie politique, je n’ai jamais connu une situation pareille","Tout le monde mange du couscous et des merguez dans ce pays, l'intégration est réussie !","Le Dalaï Lama, vous le trouvez sympathique parce que vous avez lu Tintin au Tibet ?","Ils peuvent toujours nommer Donald à l'Europe ; c'est quand même Picsou qui commande."]
  #   choix du nombre clef
  nb=randint(0,9)
  print("Melonchaud commence !")
  #   deroulement du jeu
  j=0
  for i in range(nb):
    print(l_clache_melonchaud(randint(0,3)))
    print("c'est à vous")
    if input():
      j=j+1
  if j==nb:
    print("vous avez perdu le combat")
  else :
    print("vous avez gagné le combat")

#   troisieme étape du jeu
def deplacement_trois():
    print("BRAVO ! vous passez au niveau 3.")
    niveau = 3
    #   deplacements libre
    objet()
    objet()
    objet()
    #   contexte
    print("Vous êtes arrivez au plateau tv de l'Arena, vous etes confronter au melonchaud...  \n"
          "un nombre de clache est tiré au hazard, vous devrez vous clacher l'un après l'autre,\n"
          "celui qui dit le n-ieme clash perd le combat.\n"
          "c'est parti...")
    #   troisième combat
    event_etape_trois()

      
#   quatrieme etape du jeu
def deplacement_quatre():
  print("BRAVO ! vous passez au niveau 4.")
  #   deplacement libre
  objet()
  objet()
  print("Vous etes sorti de L'arena.")
  #   deplacement libre
  objet()
  objet()
  #   deplacement libre
  #   contexte
  print("vous rentrez au 'Bercy café'")
  #   deplacement libre
  objet()
  print("serveur : qu'est-ce que je vous sert ?")
  print("vous :",input())
  print("serveur : ca marche installez-vous.")
  print("...")
  #   mise en situation
  print("Une femme laisse son sac trainer au sol, le serveur tribuche et renverse votre café.")
  #   debut question:reponse
  print("C'est à vous, faire un choix :")
  print("1- aider le serveur à nettoyer.")
  print("2- ne rien faire.")
  if un_deux():
    print("Une autre concurente ! 'Mme Pas-La-Peine'")
    print("c'est à vous, faire un choix :")
    print("1 - vous : 'Mme, vous devez me payé mon café maintenant.'")
    print("2 - Insulter")
    if un_deux():
      print("Mme Pas-La-Peine : Comment ca ? c'est peut etre moi qui à renversé votre café ?")
      if oui_non():
        print("Mme Pas-La-Peine : vous l'aurez voulu ...")
        #   quatrième combat
        combat(4)
      else :
        print("Mme Pas-La-Peine : revenez à votre place s'il vous plait")
        objet()
        deplacement_cinq()
    else:
      print(input())
      print("Mme Pas-La-Peine : vous l'aurez voulu ...")
      #   quatrième combat
      combat(4)
  else :
    print("serveur : excusez-moi messieur, je vous ramene un second café toute suite.")
    objet()
    #   on passe au niveau suivant sans combat
    deplacement_cinq()

#   cinquième etape du jeu
def deplacement_cinq():
  print("BRAVO ! vous passez au niveau final.")
  #   deplacement libre
  objet()
  objet()
  #   mise en situation
  print("c'est le moment d'aller à l'elysée")
  #   debut question reponse
  print("c'est à vous, faites un choix :")
  print("1- prendre un taxis")
  print("2- prendre les transport en commun")
  if un_deux():
    print("chauffeur : bonjour, vous aller où ?")
    print("vous : rue Faubourg Saint-Honoré, svp")
    print("chauffeur : vous aller à l'élysée")
    print("vous : (faites un choix)")
    if oui_non():
      print("chauffeur : vous travillé au gouvernement ?")  
      print("vous : (faites un choix)")
      if oui_non():
        print("très bien on arrive dans 15 minutes.")
      else :
        print("chauffeur : qu'est ce qui vous ramene la bas alors ?")
        print("c'est à vous, faites un choix :")
        print("1- vous : je suis candidat à l'elysée")
        print("2- vous : je suis fonctionnaire.")
        if un_deux():
          print("chauffeur : vous voulez prendre le pouvoir de force ? J'appel toute suite la police.")
          print("Vous avez perdu !")
        else :
          print("très bien on arrive dans 15 minutes.")
    else :
          print("très bien on arrive dans 15 minutes.")
  else :
    objet()
    objet()
    print("faire un choix :")
    print("1 - prendre le metro.")
    print("2 - prendre le RER.")
    if un_deux():
      print("faire un choix :")
      print("1 - prendre la ligne 6.")
      print("2 - prendre le ligne 14.")
      if un_deux():
        print("tres bien vous arrivez dans 40 minutes.")
      else :
        print("très bien vous arrivez dans 20 minutes.")
    else :
      print("très bien vous arrivez dans 30 minutes.")
    objet()
    objet()
    print("vous êtes devant la porte principale de l'élysée, il y a un une personne.")
    print("Alexandre...")
    print("faire un choix :")
    print("1 - lui demander gentiment de se pousser.")
    print("2 - rentrer par force.")
    if un_deux():
      print("alexandre : que voulez-vous ?")
      print("faire un choix :")
      print("1 - boire un thé avec le président.")
      print("2 - désolé je me suis trompé d'adresse.")
      if un_deux():
        print("alexandre  : vraiment ? venez avec moi, je vais vous servir café au poste")
        print("vous avez perdu.")
      else: 
        print("vous vous moquez de moi?")
        print("faire un choix :")
        print("1 - sorry, I dont speak french.")
        print("2 - Attaquer Alexandre, et rentrer par force.")
        if un_deux():
          print("vous avez perdu")
        else :
          #   cinquième combat
          combat(5)
    else :
      #   cinquième combat
      combat(5)











  return