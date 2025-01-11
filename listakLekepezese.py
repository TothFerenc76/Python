#listak lekepezese Comprehensive

eredeti = [11, 19, 7 -3]
eredmeny = []

for x in eredeti:
    eredmeny.append(x * 2)

# a jobb megoldas
eredeti = [11, 19, 7 -3]
eredmeny = [x * 2 for x in eredeti]

# csak a pozitivakat duplazzuk
eredeti = [11, 19, 7 -3]
eredmeny = [x * 2 for x in eredeti if x > 0]

# csak a paros szamok negyzetre emelese
eredeti = [10, 19, 7, 12, 6]
negyzet = [x * x for x in eredeti if x % 2 == 0]
print(negyzet)

parosak = [x for x in eredeti if x % 2 == 0]
print(parosak)