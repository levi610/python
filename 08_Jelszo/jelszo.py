
jelszo = input("1. feladat: Jelszó: ")


kisbetu = 0
nagybetu = 0
szamjegy = 0
egyeb = 0
hossz = 0

for k in jelszo:
    hossz = hossz + 1
    if "a" <= k <= "z":
        kisbetu = kisbetu + 1
    elif "A" <= k <= "Z":
        nagybetu = nagybetu + 1
    elif "0" <= k <= "9":
        szamjegy = szamjegy + 1
    else:
        egyeb = egyeb + 1

print(f"2. feladat: Kisbetű: {kisbetu}, nagybetű: {nagybetu}, számjegy: {szamjegy}, egyéb: {egyeb}")


elso_szam_hely = 0
i = 0
for k in jelszo:
    i = i + 1
    if "0" <= k <= "9":
        elso_szam_hely = i
        break

if elso_szam_hely > 0:
    print(f"3. feladat: A jelszó hossza: {hossz}, az első számjegy a(z) {elso_szam_hely}. helyen van.")
else:
    print(f"3. feladat: A jelszó hossza: {hossz}, Nincs számjegy a jelszóban.")

if hossz >= 8 and kisbetu > 0 and nagybetu > 0 and szamjegy > 0:
    print("4. feladat: Erős jelszó.")
else:
    print("4. feladat: Gyenge jelszó.")