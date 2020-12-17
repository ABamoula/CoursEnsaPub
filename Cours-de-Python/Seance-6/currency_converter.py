from py_currency_converter import convert

base_devise = input('Devise de base, ex: USD, EUR,...: ')
to_devise = input('Devise de destination, ex: USD, EUR,...: ')
quant = int(input(f'Quantité á convertir de {base_devise} a {to_devise}: '))
print(convert(base=base_devise,to=[to_devise],amount=quant))