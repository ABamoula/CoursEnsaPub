l1 = [10,17,25,38,72,12]
l2 = [25,10,13,7,2000]
print(l1)
x = l1.pop()
y = l1.pop(-1)
z = l1.pop(2)
print(l1)
print(f'x = {x} y = {y} z = {z}')

print(l1.count(False))

l1.extend(l2)
print(l1)

l1[2] = 999
print(l1)

l1[1:3] = [11,12,13,14]
print(l1,'# Remplacer [17,999] par [11,12,13,14]')