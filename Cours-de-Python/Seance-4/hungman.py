import random


WordsList = [ 'Vert', 'Chercheur', 'Mercure', 'Corde', 'Plomb', 'Scalpel', 'Tremblement', 'Fibre', 'Bleu', 'Chemin', 'Parcours', 'Enterrement', 'Chapelle']
wrd = random.choice(WordsList).lower()
print('Hungman v1')
def ShowWord(wrd,res):
    done = True
    for x in wrd:
        if x in res:
            print(x,end=' ')
        else:
            print('_',end=' ')
            done = False
    print()
    return done


def StartGame(wrd):
    res = []
    print(f'Essayez de deviner un mot de {len(wrd)} lettres en moins de {len(wrd)} tentatives échouées.')
    tent = len(wrd)
    while not ShowWord(wrd,res):
        rep = input(f' Tentative restant {tent}: ')
        if rep in wrd and rep not in res:
            res.append(rep)
        else:
            tent = tent -1
        if tent < 0:
            return False
    return True

if StartGame(wrd):print('Le joueur J2 a ganer. Bravo')
else:print('Le joueur J2 a perdue.')