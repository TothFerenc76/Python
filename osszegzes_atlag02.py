print('Atlag')
print('0-a kilep')
print('---------')

darab = 0 
osszeg = 0

erdemjegy = int(input('Add meg az elso jegyet: '))

while erdemjegy != 0:
    darab += 1
    osszeg = osszeg + erdemjegy
    erdemjegy = int(input('Add meg a kovetkezo jegyet: '))

if darab != 0:
    print('Atlag: ', osszeg / darab)
else:
    print('Nincs adat!')