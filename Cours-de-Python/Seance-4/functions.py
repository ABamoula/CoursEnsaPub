def SayHey(nom):
    """ Say hey in three languages"""
    print(f'Bonjour {nom}')
    print(f'Hello {nom}')
    print(f'Hola {nom}')

def InfiniteParams(*Params):
    for x in Params:
        for y in x:
            print(y)

# SayHey('katima')
# SayHey('Said')
# SayHey('Saalima')

InfiniteParams({'voiture':['BMW','Mercedes'],'Nom':'Karim','Age':43})


