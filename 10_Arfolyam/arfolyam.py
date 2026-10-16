
arfolyam = [320, 335, 331, 340, 352, 347, 360, 358, 341, 345, 362, 370]


emelkedett = 0
csokkent = 0
max_eses = 0
max_eses_nap = 0

van_elozo = False
elozo = 0
nap = 0

for ar in arfolyam:
    nap = nap + 1
    if van_elozo:
        if ar > elozo:
            emelkedett = emelkedett + 1
        elif ar < elozo:
            csokkent = csokkent + 1
            eses = elozo - ar
            if eses > max_eses:
                max_eses = eses
                max_eses_nap = nap
    else:
        van_elozo = True
    elozo = ar

print(f"2. feladat: Emelkedett: {emelkedett} napon, csökkent: {csokkent} napon.")
print(f"3. feladat: A legnagyobb esés: {max_eses} Ft a(z) {max_eses_nap}. napon.")


kuszob = float(input("4. feladat: Küszöb (Ft): "))

elso_nap = 0
nap = 0
for ar in arfolyam:
    nap = nap + 1
    if ar > kuszob:
        elso_nap = nap
        break

if elso_nap > 0:
    print(f"Az első nap, amikor az árfolyam meghaladta a küszöböt: {elso_nap}.")
else:
    print("Az árfolyam nem haladta meg a küszöböt.")