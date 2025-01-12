def fugg(a, b, c=100):#default parameter nincs szokoz
    """
    Ide kell beirni, hogy mit csinal
    """
    return (a + b) * c

#nev szerinti hivatkozas
print(fugg(c=1, b=2, a=1000))

#valtozo szamu parameter
def fugg2(x, *args):#a csillag kell!
    return

print(fugg2(1,12, 11,7, 17))