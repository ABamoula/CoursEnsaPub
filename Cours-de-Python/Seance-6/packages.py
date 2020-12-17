from CalculeSimple import add, multi, divEn, divi, moin,pow
from math import pow as pow_math


def Calcule(op, x, y):
    if op == '+':
        return add(x, y)
    elif op == '-':
        return moin(x, y)
    elif op == '/':
        return divi(x, y)
    elif op == '*':
        return multi(x, y)
    elif op == '//':
        return divEn(x, y)
    elif op == '**':
        print(pow_math(x,y))
        return pow(x, y)
    return None


x = input('x = ')
y = input('y = ')
op = input('op = ')


print(Calcule(op, float(x), float(y)))
