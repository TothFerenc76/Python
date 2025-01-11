nyelvek = ['Python', 'C', 'C++', 'Java', 'Python']
web = ['HTML', 'CSS', 'Javascript']

masolat = nyelvek.copy() # masolas

# rendezes
'''
nyelvek.sort()
print(nyelvek)

nyelvek.reverse()
print(nyelvek)
'''
# kereses

print(nyelvek.index('Python')) # az elso elem indexe

#print(nyelvek.index('C#')) # value error, mert nincs a listaban elkerulo megoldas:
if 'C#' in nyelvek:
    print(nyelvek.index('C#'))
 
print(nyelvek.count('Python')) # hanyszor fordul elo a listaban

# bovites

nyelvek.append('C#') # a vegere fuzes
print(nyelvek)

nyelvek.insert(1, 'Java') # beszuras egy indexre
print(nyelvek)

nyelvek.extend(web) # egy masik listavel kibovites
print(nyelvek)


# torles

nyelvek.pop() # utolso elem torlese, ha nincsmegadva ertek
print(nyelvek)
nyelvek.pop(1) # Az elso elem torlodik
print(nyelvek)
nyelvek.remove('Python') #az elso eloforduulast torli
print(nyelvek)
nyelvek.clear()
print(nyelvek)


print(masolat)