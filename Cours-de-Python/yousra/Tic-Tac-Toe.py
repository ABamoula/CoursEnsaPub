def afficher_grille(grill):
    for x in grill:
        for n in x:
            print(n, end='|')
        print('')


def mettre_a_jour_grille(grill, op):
    while True:
      lign = input('donner la lign: ')
      Col = input('donner le column :')
      if grill[int(lign) - 1][int(Col) - 1] != '.':
        print('Saisie une autre place:')
      else:
        grill[int(lign) - 1][int(Col) - 1] = op
        break


def verifier_success(grill):
    success = False
    for x in grill:
        for c in x:
            if c == '.':
                success = True
        if len(set([x[0], x[1], x[2]])) == 1 and '.' not in set(
            [x[0], x[1], x[2]]):
            print(str(set([x[0], x[1], x[2]])) + 'a gagner')
            return False
    for y in range(0, 2):
        if len(set([
                grill[0][y], grill[1][y], grill[2][y]
        ])) == 1 and '.' not in set([grill[0][y], grill[1][y], grill[2][y]]):
            print(
                str(set([grill[0][y], grill[1][y], grill[2][y]])) + 'a gagner')
            return False
    if len(set([
            grill[0][0], grill[1][1], grill[2][2]
    ])) == 1 and '.' not in set([grill[0][0], grill[1][1], grill[2][2]]):
        print(str(set([grill[0][0], grill[1][1], grill[2][2]])) + 'a gagner')
        return False
    if len(set([
            grill[0][2], grill[1][1], grill[2][0]
    ])) == 1 and '.' not in set([grill[0][2], grill[1][1], grill[2][0]]):
        print(str(set([grill[0][2], grill[1][1], grill[2][0]])) + 'a gagner')
        return False
    if not success: print('grill plein')
    return success


grill = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
afficher_grille(grill)

while verifier_success(grill):
    print('J1')
    mettre_a_jour_grille(grill, 'X')
    afficher_grille(grill)
    if not verifier_success(grill): break
    print('J2')
    mettre_a_jour_grille(grill, 'O')
    afficher_grille(grill)
