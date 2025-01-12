#minden objektum

szam_1 = -350
szam_2 = 500
szamok = [3, 1, 2]
print(f'{szam_1=} | {type(szam_1)} | {id(szam_1)}')
print(f'{szam_2=} | {type(szam_2)} | {id(szam_2)}')
print(f'{szamok=} | {type(szamok)} | {id(szamok)}')

print(szam_1.__abs__())
szamok.sort()
print(szamok)

szam_2 = szam_1 #atadja a referenciat, ezzel a szam_2 megszunik
print(f'{szam_1=} | {type(szam_1)} | {id(szam_1)}')
print(f'{szam_2=} | {type(szam_2)} | {id(szam_2)}')

szam_2 = szam_2 + 1
print(szam_1)
print(szam_2)
print(f'{szam_1=} | {type(szam_1)} | {id(szam_1)}')
print(f'{szam_2=} | {type(szam_2)} | {id(szam_2)}')
