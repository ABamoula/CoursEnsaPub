def ShowGrid(Grid):
    """ Afficher la Grid """
    for x in Grid:
        for y in Grid[x]:
            print((Grid[x][y]).center(5, ' '), '¦', end='')
        print('\n---------------------')


def SubmitValue(row, col, op):
    """ Enregistre la valeur dans la grid return True si Tout semble OK ,False si il yas une valeur deja"""
    if row not in [1, 2, 3]:
        return False
    if col not in [1, 2, 3]:
        return False
    if op not in ['X', 'O']:
        return False
    if Grilled[row][col] != '.':
        return False
    Grilled[row][col] = op
    return True


def CheckWinner(Grid,J1,J2):
    """Vérifiez le gagnant avec les règles de Tic Tac Toe"""

    for x in Grid:
        lign = set(Grid[x].values())
        rows = set(set({Grid[1][x], Grid[2][x], Grid[3][x]}))
        diagonal1 = set(set({Grid[1][1], Grid[2][2], Grid[3][3]}))
        diagonal2 = set(set({Grid[1][3], Grid[2][2], Grid[3][1]}))
        for a in [lign, rows, diagonal1, diagonal2]:
            if len(a) == 1 and '.' not in a:
                if 'X' in a:
                    print(f'***********J1 {J1} Wins***********')
                if 'O' in a:
                    print(f'***********J2 {J2} Wins***********')
                return False
    if CheckFull(Grid):
        print('*********** Grille pleine et personne n\'a gagné ***********')
        return False
    return True


def CheckFull(Grid):
    """Vérifiez si la grille est pleine sans gagnant"""
    place = False
    for x in Grid:
        for y in Grid[x]:
            if Grid[x][y] == '.':
                place = True
    if place:
        return False
    else:
        return True


def mainProgram(Grilled):
    # Get Names
    J1 = input('Nom jouer 1? \n')
    J2 = input('Nom jouer 2? \n')
    # Show the name , operator , Grid
    print(f'Bonjour {J1} et {J2}')
    print(f' {J1} --> X \n {J2} --> O')

    
    ShowGrid(Grilled)

    while CheckWinner(Grilled,J1,J2):
        end = False
        for J in [1, 2]:
            x = input(f' J{J} Lign : ')
            y = input(f' J{J} Colomn : ')
            op = 'X' if J == 1 else 'O'
            while not SubmitValue(int(x), int(y), op):
                print('Value error Try Again')
                x = input(f' J{J} Lign : ')
                y = input(f' J{J} Colomn : ')
            ShowGrid(Grilled)
            if not CheckWinner(Grilled,J1,J2):
                end = True
                break
        if end:
            break
Grilled = {1: {1: '.', 2: '.', 3: '.'}, 2: {
        1: '.', 2: '.', 3: '.'}, 3: {1: '.', 2: '.', 3: '.'}}
mainProgram(Grilled)