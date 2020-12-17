from random import randint
l1 = [21,33,12.2,8.2,90.6,]
l2 = [False,True,'Rose', 'black']

print(l1 , len(l1)) # L1
print(l2, len(l2)) # L2
#EX 1
l2[0],l2[1] = l2[1],l2[0]
print(l2)
l2[0],l2[1] = 'vrai','faux'
print(l2)
#Ex 6
l3 =[]
for z in range(0,17): 
    l3.append(randint(0,9))
print(l3)
l3.sort()
print(l3)
# # Ex 7 
# n3,n6,n9 = 0,0,0 #initialize incides

# if l3.count(6): #if 6 exist
#     n6 = l3.index(6)
#     print(f'6 => {l3.count(6)}fois premier indice {n6}')

# if l3.count(3): #if 3 exist
#     n3 = l3.index(3)
#     print(f'3 => {l3.count(3)}fois premier indice {n3}')

# if l3.count(9): #if 9 exist
#     n9 = l3.index(9)
#     print(f'9 => {l3.count(9)}fois premier indice {n9}')

for x in [3,6,9]:
    if x in l3:
        print(f'{x} => {l3.count(x)}fois premier indice: {l3.index(x)}')

#Ex 8
print('#Ex 8')
print(l3)
for x in range(0,6):
    l3.append(10)
print(l3)
print('#Ex 9')
for x in range(0,3):
    l3.pop(0)
print(l3)
#Ex 9
print('#Ex 9')
for x in [l1,l2,l3]:
    print(x)
    x.reverse()
    print(x)
#EX 10

print('#Ex 10')
mil = len(l3)//2 # devision entier

x = l3[0]+ l3[-1]

l3.insert(mil,x)

print(x,'indice',mil,l3)

print(len(l3))


