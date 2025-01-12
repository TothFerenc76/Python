szamok = [2, 5, 4, 8, 9, 11, 10, 12]

talalat = False
index = 0

while index < len(szamok) and not talalat:
    if szamok[index] % 3 == 0:
        talalat = True
        break
    index += 1

if talalat:
    print('Van', index)
else:
    print('nincs')


talalat = False
index = 0
while not talalat:
    if szamok[index] % 3 == 0:
        talalat = True
    index += 1

if talalat:
    print('Van', index)
else:
    print('nincs')
