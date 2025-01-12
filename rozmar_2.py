# Ez nem mukodik, mert egy Int nem kaphat None-t.

"""
szam = None 
while szam > 0:
    szam = int(input('Adj meg egy szamot! '))
print('Program vege!')
"""
# Elegans megoldas
while (szam := int(input('Adj meg egy szamot! '))) > 0: #ha nincs befoglalo zarojel, akkor kiirja, hogy True vagy False
    print(szam)
                  
print('Program vege!')