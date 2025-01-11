for szam in range(1,10,4):
    print(szam)


tantargyak = ['matek', 'tori', 'bio', 'kemia', 'info']
'''
index = 0
for tantanrgy in tantargyak:
    print(index, tantanrgy)
    index = index + 1


for index in range(len(tantargyak)):
    print(index, tantargyak[index])

'''

for index, tantargy in enumerate(tantargyak):
    print(index, tantargy)