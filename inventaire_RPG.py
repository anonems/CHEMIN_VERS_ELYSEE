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
from fonctions import un_deux,oui_non

# 	ajout d'objets
l_objet=[]
def inventaire_ajout_objet(objet):
	l_objet.append(objet)
	return l_objet

#	ajout d'electeurs
nb_ele=[0]
def inventaire_ajout_electeurs(nb):
	nb_ele[0]=nb_ele[0]+nb
	return nb_ele[0]

#	la fonction fait le choix principal dans l'inventaire:
def inventaire_choix_principal():
	print('\033[1m' + "==========INVENTAIRE==========" + '\033[0m')
	for i in range(len(l_objet)):
		print(i+1,". ",l_objet[i])
	print("Vous avez",nb_ele[0],"élécteurs.")
	print("Quitter l'inventaire ?")
	while not(oui_non()):
		print("Quitter l'inventaire ?")
	return 

