
# t1 = (10,12,'test',0.5,[1,11,111])

# print(t1[0])
# print(t1[2])
# print(t1[-1])
# print(t1[0:2])

# t1[0] = 23

# print(type(t1[0:2]))

# for x in t1:
#     print(x)
    
# print('length',len(t1))


# C = set()

# B = set([10,10,10,10,20,20,20])
# D = {[1,2],2} TypeError: unhashable type: 'list'
# X = {'1','a','4','d'}
# print(D)
# print(B)
# print(X)


# X = set('abcad')
# Y = set('efga')

# print(X)
# print(Y)

# print(X - Y)
# print(X.difference(Y),'difference')

# print(X | Y)
# print(X.union(Y),'Union')

# print(X & Y)
# print(X.intersection(Y),'intersection')

# X.add('z')
# print(X)
# X.update({'x',3,2})
# print(X)

d2 = {1:'x',2:'3','d':3,'lst':[2,3,2,1,]}
d3 = dict(nom='Kamal',age=23,taille=165)

# print(type(y))
# print(d2.get('parent','said'))
# print(d3)


print(d2)

# print(list(d2.keys()))

# print(list(d2.values()))

# del d2[1]
# print(d2,'del')

# d2.pop(4) KeyError: 4
# d2.pop(2)
# print(d2,'pop')

# print('age' in d3)
# print(len(d3))
d2[12] = ['h','w']
for x,y in d2.items():
    print(x,y)
