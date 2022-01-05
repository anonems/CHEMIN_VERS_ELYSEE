# CHEMIN_VERS_ELYSEE
Nom du projet : " Le chemin vers l'elysée " <br>
Membres du groupe de 5 ainsi que leurs rôles : <br>
                        HAKIRI Emir     -->     Chef de projet & rassemblement des parties, parties deplacament_RPG.py, main_RPG.py <br>
                        LIMACO DIEGO    -->     Gestion de l'inventaire, partie inventaire_RPG.py <br>
                        MUGUET Benoit   -->     Gestion des combats, partie combat_RPG.py <br>
                        ROY Accene      -->     Gestion des menus et de la sauvegarde, partie menu_RPG.py <br>
                        FERNANDES Guy   -->     Assistance et narration (NB : malade au moment du projet) <br>
Lieu : HETIC <br>
Encadrement : JANIN Loïc <br>
Language de programation : Python <br>
Date de rendu limite : 5 janvier 2022 <br>
But du jeu : Le joueur se met dans la peau d'un candidat à la presidentielle, il doit recolté le plus d'élécteurs et combattre les autre candidat pour gagné sa place à l'élysée. <br><br>
Déroulement du jeu : <br>
    Le jeu est en 5 étapes (ou niveaux), chaqu'un de ces niveau est caractériser par un candidat à la présidentielle qui est mis dans un contexte autour duquel sera formé, <br>
    au fur et mesure des interactions du joueur, une situation menant à un combat. <br>
    Les personnages cles sont les suivants, dans l'ordre du jeu : -Hidalgo    -->   La marre de Paris <br>
                                                                  -Zemmour    -->   The hummour <br>
                                                                  -Melanchon  -->   Melonchaud <br>
                                                                  -Le Pen     -->   Pas la peine <br>
                                                                  -Benalla    -->   Alexandre <br><br>
  
Comment gagné le jeu ? : <br>
    Pour gagné le jeu il faut reussir à arriver à la dernière et 5e étape, battre le dernier boss, et tout d'abord avoir recolté plus de 60 élécteurs. <br><br>

Comment se déroule les combats ? : <br>
    Une fois le cambat déclancher le joueur à le choix de combattre ou de quitter le combat, si le joueur combat jusqu'au bout et gagne le combat, <br>
    il repare avec 200 points de vie, 100 élécteurs, et l'arme de son adversaire. <br>
    En revenche si il perd le combat, (c'est à dire qu'il n'a plus de points de vie),  il repare qu'avec 10 élécteurs, puis il passe au niveau suivant (à part le 3e combat, si il le perd il perd le jeu). <br><br>

Qu'en est-il des menus ? : <br>
    dans le jeu nous avons 5 menus différents : <br>
        Le premier menu : <br>
            Le premier menu ne s'affiche qu'une seule fois, au lancement du programme, il permet au joueur de : -Démarrer une nouvelle partie <br>
                                                                                                                -Reprendre à un niveau sauvegarder <br>
                                                                                                                -Lire ce que vous lisez à linstant <br>
                                                                                                                -Quitter le jeu <br><br>
        Le menu principale : <br>
            Le menu principale s'affiche parmis les choix du joystick, une fois selectionner il permet au joueurs de : -Visualiser l'inventaire <br>
                                                                                                                       -Nettoyer la console <br>
                                                                                                                       -Lire ce que vous lisez à l'instant <br>
                                                                                                                       -Quitter & sauvegarder le jeu, si vous choisissez quitter une option de sauvegarde s'affichera <br><br>
        le joystick : <br>
            Le joystick s'affiche à chaque fois que le joueur est appelé à se déplacer, il permet au joueur de : -Avancer <br>
                                                                                                                 -Se diriger à droite <br>
                                                                                                                 -Se diriger à gauche <br>
                                                                                                                 -Faire demis-tour <br>
                                                                                                                 -Afficher le menu principale <br>
            (NB : le joystick à pour but de crée une interraction avec le joueur, de se déplacer d'un niveau à un autre et de crée un systeme de récompense au déplacement avec des objets qui apparaisse lorsque le joueur se déplace et qui peuvent étre ajouter à l'inventaire.) <br> <br>
        Le menu attaque : <br>
            Le menu attaque apparaît lorsque le joueur rentre en mode combat, il permet au joueur de : -Attaquer <br>
                                                                                                       -Afficher l'inventaire <br>
                                                                                                       -Quitter le combat <br>
                                                                                                       -Afficher le menu principale <br><br>
        L'inventaire : <br>
            L'inventaire à cet étape du projet n'ai pas vraiment un menu, il permet seulement de visualiser les objet recoltés pendant les déplacements, et d'afficher le nombre d'élécteurs gagné. <br><br>
            Le vrai but de l'inventaire aurai été de non seulement voir les objet gagné mais en plus de pouvoir les utilisé, mais le temps ne nous à pas permis d'appliquer cette fonctionnalité. <br> <br>
autre chose ? : <br>
  Le fichier fonction.py regroupes les fonctions les plus utilisées dans le programme. <br>
  
