cesar = 'Jottem, ' + 'Lattam, ' + 'Gyoztem!'
lista = [1, 2, 3, 4, 5, 6, 7]
print(cesar)

print('Ja' + 'j' * 7)

print(str(7.23), str(8) + 'kg')

r = 10
PI = 3.14
print(f'A kor kerulete: {2 * r * PI:.2f}')

print(lista[1:4])
print(cesar[1:4])

print(lista[:4])
print(cesar[1:])

print(lista[-1])
print(cesar[-1])

print(len(lista))
print(len(cesar))

for elem in lista:
    print(elem)


for karakter in cesar:
    print(karakter)

szamlalo = 0
for karakter in cesar:
    if karakter == 'e':
        szamlalo += 1

print(szamlalo)

if 7 not in lista:
    print('Van!')
else: 
    print('Nincs')

if 'J' in cesar:
    print('Van.')
else:
    print('Nincs')

#kulobseg a lista es a tomb kozt

lista[0] = 17
print(lista)

#cesar[0] = 'L'
print(cesar) #Hiba! A stringek nem valtoztathatok meg!

print(cesar.lower()) # kisbetusit, de csak a kiirasban, ay eredeti nem valtozik
print(cesar)

print(cesar.upper())

print(cesar.count('t')) # megszamoljuk a "t"-t

print(cesar.isupper()) # csak nagybetus-e?

print(cesar.find('a')) # az "a" elso elofordulasa