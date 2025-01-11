szavak = ['lampa', 'ablak', 'kutya', 'Attila', 'kukta']

for szo in szavak:
    print(szo)
    if szo[0] == 'p':
        print('Van a-val kezdodo szo')
        break
else:
    print('Nincs ilyen szo!')