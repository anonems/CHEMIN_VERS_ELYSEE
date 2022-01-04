#   permet de faire un choix entre oui et non.
def oui_non():
  print("Choisir oui ou non.")
  urep = input()
  if urep == 'OUI' or urep=='oui':
    return True
  elif urep == 'NON' or urep=='non':
    return False
  while  urep != 'OUI' or urep!='oui' or urep != 'NON' or urep!='non' :
    print('ERREUR ! choisissez oui ou non.')
    urep = input()
    if urep == 'OUI' or urep=='oui':
      return True
    elif urep == 'NON' or urep=='non':
      return False


#   permet de faire un choix entre les chiffres 1 et 2.
def un_deux():
  urep = input()
  if urep == '1' :
    return True
  elif urep == '2' :
    return False
  while  urep != '1' or urep!= '2' :
    print('ERREUR ! choisissez 1 ou 2.')
    urep = input()
    if urep == '1' :
      return True
    elif urep == '2':
      return False

#   permet de faire un choix entre les chiffres 1, 2, 3 ou 4.
def un_quatre():
  urep = input()
  if urep == '1' :
    return 1
  elif urep == '2' :
    return 2
  elif urep == '3' :
    return 3
  elif urep == '4' :
    return 4
  while  urep!='1' or urep!='2' or urep!='3' or urep!='4':
    print('ERREUR ! choisissez 1, 2, 3 ou 4.')
    urep = input()
    if urep == '1' :
      return 1
    elif urep == '2' :
      return 2
    elif urep == '3' :
      return 3
    elif urep == '4' :
      return 4

#   permet de faire un choix entre les chiffres 1, 2, 3, 4 ou 5.
def un_cinq():
  urep = input()
  if urep == '1' :
    return 1
  elif urep == '2' :
    return 2
  elif urep == '3' :
    return 3
  elif urep == '4' :
    return 4
  elif urep == '5' :
    return 5
  while  urep!='1' or urep!='2' or urep!='3' or urep!='4' or urep!='5':
    print('ERREUR ! choisissez 1, 2, 3, 4 ou 5.')
    urep = input()
    if urep == '1' :
      return 1
    elif urep == '2' :
      return 2
    elif urep == '3' :
      return 3
    elif urep == '4' :
      return 4
    elif urep == '5' :
      return 5

#   presentation print rpg.
def presentation_rpg():
  print("___________________________________________________________________________________________")
  print("\n")
  print(
  "#################              ################                 ############################\n"
  "##              ##             ##              ##               ##                        ##\n"
  "##               ##            ##                ##             ##                        ##\n"
  "##                ##           ##                  ##           ##                        ##\n"
  "##                ##           ##                  ##           ##                          \n"
  "##               ##            ##                ##             ##                          \n"
  "##              ##             ##################               ##                          \n"
  "##            ##               ##                               ##                          \n"
  "##          ##                 ##                               ##              ############\n"
  "##        ##                   ##                               ##              ##        ##\n"
  "##          ##                 ##                               ##              ##        ##\n"
  "##            ##               ##                               ##                        ##\n"
  "##              ##             ##                               ##                        ##\n"
  "##                ##           ##                               ############################\n"
  )
  print("\n")
  print("___________________________________________________________________________________________")
  return
