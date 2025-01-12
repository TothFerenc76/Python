#Enclosing (nonlocal) scope

def kulso():
    szam = 17

    def belso():
        print(szam)
    belso()

kulso()