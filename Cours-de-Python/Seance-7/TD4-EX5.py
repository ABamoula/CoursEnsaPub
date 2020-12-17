import random

def GenInt():
    return chr(random.randint(48,57))

def GenUpper():
    return chr(random.randint(65,90))

def passgen(length,with_digits=True,with_uppercase=True):
    random_int = ''
    random_upper = ''
    generated_pass = ''
    for x in range(0,length):
        if with_digits: random_int =  GenInt()
        if with_uppercase: random_upper = GenUpper()
        random_lower = chr(random.randint(97,122))
        pick = random.randint(1,3)
        if pick == 1 :
            if with_digits: generated_pass += random_int
            else: generated_pass +=random_lower
        if pick == 2 :
            if with_uppercase: generated_pass += random_upper
            else: generated_pass +=random_lower
        if pick == 3 :
            generated_pass +=random_lower
    return generated_pass

for x in range(0,10):
    print(passgen(15,with_digits=True,with_uppercase=True))