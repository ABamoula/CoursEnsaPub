import random
# hello
def afficher(choix,utilisateur):
    m = len(choix)
    for x in choix:
        if x in utilisateur:
            print(x,end=' ')
        else:
            print('-',end=' ')
    print()

def verification(choix,lettres):
    if lettres in choix:
        return True
    else:
        return False

def gagner(choix, utilisateur):
    for y in choix:
        if y not in utilisateur:
            return False
    return True


words = [ 'Vert', 'Chercheur', 'Mercure', 'Corde', 'Plomb', 'Scalpel', 'Tremblement', 'Fibre', 'Bleu', 'Chemin', 'Parcours', 'Enterrement', 'Chapelle']
utilisateur = []
choix = random.choice(words).lower()
m = len(choix)

print('Hangman v1')
print(f'Essayez de deviner un mot de {m} lettres en moins de {m} tentatives.')

afficher(choix,utilisateur)
tentatives = 1
while True:
    lettres = input(f'Tentative {tentatives} : ')
    if verification(choix,lettres):
        if lettres not in utilisateur:
            utilisateur.append(lettres)
    else:
        tentatives = tentatives +1 # tentative += 1
    afficher(choix,utilisateur)
    if tentatives > m:
        print('Le joueur J2 a perdu.')
        break
    if gagner(choix,utilisateur):
        print('Le joueur J2 a Gangner.')
        break