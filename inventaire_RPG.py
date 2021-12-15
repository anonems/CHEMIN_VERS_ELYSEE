'''
Auteur : 
Déscription :

'''
#   importation des parties du jeu 

from menu_RPG import *
from combat_RPG import *

#	la function fait le choix principal dans linventaire:
def inventaire_choix_principal():
	print("faire une choix")
	print("1-arme")
	print("2-potion")
	choix = int(input())	
	if choix == 1:
		return True
	elif choix == 2:
		return False
	while choix != 1 and choix != 2:
		print("Erreur!choisir 1 or 2")
		choix = int(input())	
		if choix == 1:
			return True
		elif choix == 2:
			return False
	
def inventaire_choix_secundaire():
	if inventaire_choix_principal():
		print()
	else:
		print()
