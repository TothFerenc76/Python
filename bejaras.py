'''
for szo in szavak:
    print(szo)

for karakter in 'almafa':
    print(karakter)
'''
for index, karakter in enumerate('almafa'):
    print(f'{index}. {karakter}')

for sorszam, karakter in enumerate('almafa', start = 1):
    print(f'{sorszam}. {karakter}')

for _ in range(2, 5, 2): # 2-tol 5-ig 2-tel lepeskozzel ay 5 mar nem tartozik bele
    print(_)

