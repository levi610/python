
jegyek = [5, 4, 3, 5, 2, 4, 4, 5, 3, 1, 4, 5, 3, 4, 2]


osszeg = 0
for jegy in jegyek:
    osszeg = osszeg + jegy

atlag = osszeg / len(jegyek)
print(f"2. feladat: Az átlag: {atlag:.2f}")
keresett_jegy = int(input("3. feladat: Melyik jegyet keresi? "))
darab = 0
for jegy in jegyek:
    if jegy == keresett_jegy:
        darab = darab + 1

print(f"A(z) {keresett_jegy}-es jegyből {darab} darab van.")

elso_elégtelen_index = 0

for i in range(len(jegyek)):
    if jegyek[i] == 1:
        elso_elégtelen_index = i + 1
        break

if elso_elégtelen_index > 0:
    print(f"4. feladat: Az első elégtelen jegy sorszáma: {elso_elégtelen_index}.")
else:
    print("4. feladat: Nem volt elégtelen jegy.")