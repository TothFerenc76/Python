import random

a = random.randint(0, 10)
b = random.randint(0, 10)

print(f'Itt van ket szam {a} es {b}, milyen miveletet vegezzek veluk?')
valasz = input(f'Add meg a muveleti jelet! ')

if valasz == '+':
    print(f'{a} {valasz} {b} = {a + b}')
elif valasz == '-':
    print(f'{a} {valasz} {b} = {a - b}')
elif valasz == '*':
    print(f'{a} {valasz} {b} = {a * b}')
elif valasz == '/' and b != 0:
    print(f'{a} {valasz} {b} = {a / b}')
else:
    print('?!')