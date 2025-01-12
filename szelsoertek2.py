szavak = ['Elemer', 'to', 'ajto', 'roka', 'Aladar', 'pingvin']

legrovidebb = szavak[0]

for szo  in szavak:
    if len(szo) < len(legrovidebb):
        legrovidebb = szo
print(legrovidebb)

print(min(szavak))