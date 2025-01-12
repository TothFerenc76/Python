diakok = ['Nora', 'Gergo', 'Hanna', 'Tamas', 'Adam']
eletkorok = [17, 16, 18, 18]
'''
for index in range(len(diakok)):
    print(f'{diakok[index]}:{eletkorok[index]}')
'''
#elegansabb
for diak, eletkor in zip(diakok, eletkorok): #osszefesuli parba
    print(f'{diak}, {eletkor}')


print(list(zip(diakok,eletkorok))) #tuple gyartas