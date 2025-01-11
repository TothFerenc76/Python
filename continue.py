szavak = ['lampa', 'ablak', 'kutya', 'Attila', 'kukta']

for szo in szavak:
    if szo[0] == 'a':
        continue
    print(szo)

# tomorebben
for szo in szavak:
    if szo[0] != 'a':
        print(szo)
