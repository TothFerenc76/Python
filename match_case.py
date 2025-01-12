import random

a = random.randint(0, 10)
b = random.randint(0, 10)

print(f'Itt van ket szam {a} es {b}, milyen miveletet vegezzek veluk?')
valasz = input(f'Add meg a muveleti jelet! ')

match valasz:
    case '+':
        print(f'{a} {valasz} {b} = {a + b}')
    case '-':
        print(f'{a} {valasz} {b} = {a - b}')
    case '*':
        print(f'{a} {valasz} {b} = {a * b}') 
    case '/' if b != 0:   
        print(f'{a} {valasz} {b} = {a / b}')  
    case '**' | '%':
        print('Ezt a muveletet nem ismerem!')      
    case other: # case _: ugyanaz
        print('?!')
