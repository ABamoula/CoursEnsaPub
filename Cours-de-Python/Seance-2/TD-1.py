import math

b = False
while not b:
    try:
        R = float(input('Saisir le rayon: '))
        unite = input('unite: ')
        if unite in ['cm','m']:
            b = True
    except ValueError as e:
        print('Erreur de saisie')
if unite == 'm':
    surface = math.pi * math.pow(R*100,2)
else:
    surface = math.pi * R*R
print(f'pour le rayon {R}{unite} la surface est {surface} cm²')