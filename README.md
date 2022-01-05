# CHEMIN_VERS_ELYSEE
Nom du projet : " Le chemin vers l'elysée "
Membres du groupe de 4 ainsi que leurs rôles :
                        HAKIRI Emir     -->     Chef de projet & rassemblement des parties, parties deplacament_RPG.py, main_RPG.py 
                        LIMACO DIEGO    -->     Gestion de l'inventaire, partie inventaire_RPG.py
                        MUGUET Benoit   -->     Gestion des combats, partie combat_RPG.py
                        ROY Accene      -->     Gestion des menus et de la sauvegarde, partie menu_RPG.py
                        FERNANDES Guy   -->     Assistance et narration (NB : malade au moment du projet)
Lieu : HETIC
Encadrement : JANIN Loïc 
Language de programation : Python
Date de rendu limite : 5 janvier 2022
But du jeu : Le joueur se met dans la peau d'un candidat à la presidentielle, il doit recolté le plus d'élécteurs et combattre les autre candidat pour gagné sa place à l'élysée.
Déroulement du jeu :
    Le jeu est en 5 étapes (ou niveaux), chaqu'un de ces niveau est caractériser par un candidat à la présidentielle qui est mis dans un contexte autour duquel sera formé, 
    au fur et mesure des interactions du joueur, une situation menant à un combat.
    Les personnages cles sont les suivants, dans l'ordre du jeu : -Hidalgo    -->   La marre de Paris
                                                                  -Zemmour    -->   The hummour
                                                                  -Melanchon  -->   Melonchaud
                                                                  -Le Pen     -->   Pas la peine
                                                                  -Benalla    -->   Alexandre
  
Comment gagné le jeu ? :
    Pour gagné le jeu il faut reussir à arriver à la dernière et 5e étape, battre le dernier boss, et tout d'abord avoir recolté plus de 60 élécteurs.

Comment se déroule les combats ? :
    Une fois le cambat déclancher le joueur à le choix de combattre ou de quitter le combat, si le joueur combat jusqu'au bout et gagne le combat,
    il repare avec 200 points de vie, 100 élécteurs, et l'arme de son adversaire.
    En revenche si il perd le combat, (c'est à dire qu'il n'a plus de points de vie),  il repare qu'avec 10 élécteurs, puis il passe au niveau suivant (à part le 3e combat, si il le perd il perd le jeu).

Qu'en est-il des menus ? :
    dans le jeu nous avons 5 menus différents :
        Le premier menu :
            Le premier menu ne s'affiche qu'une seule fois, au lancement du programme, il permet au joueur de : -Démarrer une nouvelle partie
                                                                                                                -Reprendre à un niveau sauvegarder
                                                                                                                -Lire ce que vous lisez à linstant
                                                                                                                -Quitter le jeu
        Le menu principale :
            Le menu principale s'affiche parmis les choix du joystick, une fois selectionner il permet au joueurs de : -Visualiser l'inventaire
                                                                                                                       -Nettoyer la console
                                                                                                                       -Lire ce que vous lisez à l'instant
                                                                                                                       -Quitter & sauvegarder le jeu, si vous choisissez quitter une option de sauvegarde s'affichera
        le joystick :
            Le joystick s'affiche à chaque fois que le joueur est appelé à se déplacer, il permet au joueur de : -Avancer
                                                                                                                 -Se diriger à droite
                                                                                                                 -Se diriger à gauche
                                                                                                                 -Faire demis-tour
                                                                                                                 -Afficher le menu principale
            (NB : le joystick à pour but de crée une interraction avec le joueur, de se déplacer d'un niveau à un autre et de crée un systeme de récompense au déplacement avec des objets qui apparaisse lorsque le joueur se déplace et qui peuvent étre ajouter à l'inventaire.)
        
        Le menu attaque :
            Le menu attaque apparaît lorsque le joueur rentre en mode combat, il permet au joueur de : -Attaquer
                                                                                                       -Afficher l'inventaire
                                                                                                       -Quitter le combat
                                                                                                       -Afficher le menu principale
                                                                                                       
        L'inventaire :
            L'inventaire à cet étape du projet n'ai pas vraiment un menu, il permet seulement de visualiser les objet recoltés pendant les déplacements, et d'afficher le nombre d'élécteurs gagné.
            Le vrai but de l'inventaire aurai été de non seulement voir les objet gagné mais en plus de pouvoir les utilisé, mais le temps ne nous à pas permis d'appliquer cette fonctionnalité.
         
 
autre chose ? :
  Le fichier fonction.py regroupes les fonctions les plus utilisées dans le programme.
  
