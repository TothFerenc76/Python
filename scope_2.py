# Global (module) scope


def negyzet(a):
    global szam # lehet, de kerulendo!!!
    szam = 10
    print(szam)
    return a ** 2

negyzet(3)
print(f'{szam}')

