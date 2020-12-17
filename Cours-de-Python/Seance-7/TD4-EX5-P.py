import random
from string import ascii_lowercase
from string import ascii_uppercase
def GenInt():return random.randint(0,9)
def GenUpper():return random.choice(ascii_uppercase)
def passgen(length,with_digits=True,with_uppercase=True):
    random_int = ''
    random_upper = ''
    generated_pass = ''
    for x in range(0,length):
        if with_digits: random_int =  str(GenInt())
        
        if with_uppercase: random_upper = GenUpper()
        
        random_lower = random.choice(list(ascii_lowercase))
        
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
    print(passgen(10,with_digits=True,with_uppercase=True))