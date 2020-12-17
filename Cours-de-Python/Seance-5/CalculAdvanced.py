def Calc(op,x,y):
    """ Calcule des deux Valeur"""
    operator_functions = {
    '+': lambda x, y: x + y, 
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y, 
    '/': lambda x, y: x / y,
    '//': lambda x, y: x // y,
    }
    return operator_functions[op](x, y)

# print(Calc('//',10,2))

def yes_or_no(prompt,retries=3,reminder='Essayer Encore'):
    """Yes or No ?"""
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no','nop','nope'):
            return False
        retries = retries -1
        if retries <0:
            raise ValueError('Invalide user response')
        print(reminder)


# yes_or_no('vous voulez quitter ?')
yes_or_no('vous voulez quitter ?',5)
# yes_or_no('vous voulez quitter ?',2,'Try again Please')
# yes_or_no()
