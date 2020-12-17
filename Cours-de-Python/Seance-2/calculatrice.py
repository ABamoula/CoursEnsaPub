
var1=int(input("Saisissez la premiere valeur : "))
var2=int(input("Saisissez la deuxieme valeur : "))
op=input("Saisissez le type d'operation : ")
if op in ["+","-","*","/","//"] :
    if op=="+":
        print(f"le resulat de {var1}{op}{var2}  est :{var1+var2} ")
    if op=="-":
        print(f"le resulat de {var1}{op}{var2}  est :{var1-var2} ")
    if op=="*":
        print(f"le resulat de {var1}{op}{var2}  est :{var1*var2} ")    
    if op=="/":
        print(f"le resulat de {var1}{op}{var2}  est :{var1/var2} ")    
    if op=="//":
        print(f"le resulat de {var1}{op}{var2}  est :{var1//var2} ")            