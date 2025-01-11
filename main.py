import random, kor
from kor import kerulet as k_kerulet, terulet as k_terulet
from negyzet import kerulet, terulet


print(random.randint(1,10))

print(f'kerulet : {k_kerulet(5):.2f}')
print(f'terulet : {k_terulet(5):.2f}')

print(f'kerulet : {kerulet(5):.2f}')
print(f'terulet : {terulet(5):.2f}')
print(kor.pi)