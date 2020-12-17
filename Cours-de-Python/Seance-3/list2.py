l1 = [25,10,13,7,2000]
l1.sort()
print(l1,"Ordered") # nums triée

l2 = ["William","Kamal","Eric","Kevin","Joe"] 
l2.sort()
print(l2) # Ordre Alphabitic

l1.append(999)
print(l1,"Added 999")

l1.reverse()
print(l1,"Revesed") # reversed

l1.remove(999)
print(l1,"sans la valeur 999") # Print l1 sans la valeur 999

i = l1.index(25)
print(i,"indice de 25")

l1.pop(i)
print(l1,"Removes value 25 with index")