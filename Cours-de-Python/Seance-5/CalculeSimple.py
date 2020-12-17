import math

def add(x, y): return x+y
def multi(x, y): return x*y
def divi(x, y):return x/y
def moin(x, y):return x-y
def divEn(x, y):return x//y

def test_egalite_remarquable3(a,b):
    a = float(a)
    b = float(b)
    first = multi(moin(a,b),add(a,b))
    carre = moin(math.pow(2,a),math.pow(2,b))
    print(first,carre)
    assert first == carre ,f'Not Equall {a} and {b}'
    # print('Égale' if first==carre or 'pas égale' )


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
    return None


x = input('x = ')
y = input('y = ')
op = input('op = ')

print(Calcule(op,float(x),float(y)))

# test_egalite_remarquable3(12,192)