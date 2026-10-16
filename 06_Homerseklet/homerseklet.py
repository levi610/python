
homerseklet = [3, -2, -5, 0, 4, 7, -1, 2, -4, 8]

osszeg = 0
for i in homerseklet:
    osszeg = osszeg + i

atlag = osszeg / len(homerseklet)
print(f"2. feladat: Az átlaghőmérséklet: {atlag:.1f} °C")

min_ertek = homerseklet[0]
min_nap = 1

for i in range(len(homerseklet)):
    if homerseklet[i] < min_ertek:
        min_ertek = homerseklet[i]
        min_nap = i + 1

print(f"3. feladat: A leghidegebb nap: {min_nap}. nap, {min_ertek} °C")

fagynapok = 0
for i in homerseklet:
    if i < 0:
        fagynapok = fagynapok + 1

print(f"4. feladat: {fagynapok} napon volt fagy.")