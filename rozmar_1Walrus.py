szo = None # A while vizsgalathoz kell, hogy letezen a valtozo, ezert semmi erteket kap.
while szo != '':
    szo = input('Adj meg szavakat! Ha kilepnel, csak ENTER-t uss! ')

print('Program vege')

# Elegansabb megoldas a walrus operator
while (szo := input('Adj meg szavakat! Ha kilepnel, csak ENTER-t uss! ') != ''):
    print(szo)
print('Program vege')