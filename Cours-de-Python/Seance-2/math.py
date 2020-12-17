import math
print('Un chiffre:')
x = int(input())
save = x
cpt =0
while x!= 1:
    x =x //2
    cpt += 1

print(f'{save} = 2**{cpt} ---> {save == math.pow(2,cpt)}')
assert save == math.pow(2,cpt) , f'Faux !'