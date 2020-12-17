def greeting(nom):
    """ Say hey in three languages"""
    for greet in ['Bonjour','Hello','Hola']:
        greeting2(nom,greet)


def greeting2(nom,greet):
    print(f'{greet} {nom}')

greeting('karim')