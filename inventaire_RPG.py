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

def inventaire_ajout_objet():
	return

def inventaire_ajout_electeurs():
	return
