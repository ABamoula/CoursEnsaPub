nom = input("Merci de saisir votre nom ?\n")
age = input("ton Age ?\n")
agePlus =  -10
try:
    agePlus = int(age) + 10
except ValueError as ve:
    print('Saisir un nombre')
if agePlus > 0:
    print("Bonjour Mr."+nom)
    print("Age : "+age)
    print("après 10 ans votre age sera: : "+ str(agePlus))