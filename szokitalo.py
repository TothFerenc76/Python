import random

def makeMask(titok, jo):
    result = ''
    for c in titok:
        if c in jo:
            result = result + c
        else:
            result = result + '_'
    return result

def allapotKiiras(titok, jo, rossz):    
    print('Jelenlegi allas: ', makeMask(titok, jo))
    print('Rossz tippek: ', rossz)
    print('-------------------------')

def tippeles(titok, jo, rossz):
    tipp = input('Adj meg egy betut! ')
    if tipp in titok:
        jo.append(tipp)
        return True
    else:
        rossz.append(tipp)
        return False

def main():
    lista = ['Kerek', 'Ablak', 'Tabla', 'Kalap', 'Torta']
    kitalalando = lista[random.randint(0, len(lista) - 1)]
  
    jo_Tippek = []
    rossz_tippek = []

    print('Talald ki melyik 5 betus fonevre gondoltam!')
    while len(jo_Tippek) < 5:
        if tippeles(kitalalando, jo_Tippek, rossz_tippek):
            print('Talalat')
        allapotKiiras(kitalalando, jo_Tippek, rossz_tippek)

    print(kitalalando)
    print(f'Kitalaltad {len(jo_Tippek) + len(rossz_tippek)} lepesbol!')