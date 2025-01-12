def teglalapot_novel(a, b):
    a = a * 2
    b = b * 2
    return a, b

a_oldal = 3
b_oldal = 9
#a_oldal, b_oldal = teglalapot_novel(a_oldal, b_oldal)
#print(a_oldal, b_oldal)
#tuple haszalata

ertek = teglalapot_novel(a_oldal, b_oldal)
print(ertek)
print(type(ertek))