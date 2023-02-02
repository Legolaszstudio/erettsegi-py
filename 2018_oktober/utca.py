# 2023. február 02.
import random
import string

class Kerites:
    def __init__(self, oldal, szelesseg, szin, hazszam):
        self.oldal = oldal
        self.szelesseg = szelesseg
        self.szin = szin
        self.hazszam = hazszam

    def __str__(self):
        return f"{self.oldal}, {self.szelesseg}, {self.szin}, {self.hazszam}"

    def __repr__(self):
        return self.__str__()


telkek = []

with open("kerites.txt", "r", encoding="utf-8") as f:
    utolso_paros, utolso_paratlan = 2, 1
    for sor in f:
        adatok = sor.strip().split(" ")

        peldany = Kerites(
            int(adatok[0]),
            int(adatok[1]),
            adatok[2],
            utolso_paros if int(adatok[0]) == 0 else utolso_paratlan,
        )
        telkek.append(peldany)
        if peldany.oldal == 0:
            utolso_paros += 2
        else:
            utolso_paratlan += 2

# 2
print(f"2. feladat\nAz eladott telkek száma: {telkek.__len__()}\n")

# 3
utolso_telek = telkek[-1]
# "Igaz" if feltetel == True else "Hamis"
print(f"3. feladat\nA {'páros' if utolso_telek.oldal == 0 else 'páratlan'} oldalon adták el az utolsó telket.")
print(f"Az utolsó telek házszáma: {utolso_telek.hazszam}")

# 4
print("\n4. feladat")
szin = ""
for adat in telkek:
    if adat.oldal == 0 or\
            adat.szin == "#" or\
            adat.szin == ":":
        continue

    if adat.szin != szin:
        szin = adat.szin
    else:
        print(f"A szomszédossal egyezik a kerítés színe: {adat.hazszam}")
        break

# 5
print("\n5. feladat")
haz = int(input("Adjon meg egy házszámot! "))

telek = ""

szinek = list(string.ascii_uppercase) # A - Z
ujszin = ""
for adat in telkek:
    if adat.hazszam == haz:
        telek = adat
        if adat.szin in szinek:
            szinek.remove(adat.szin)
    elif adat.hazszam == haz+2:
        if adat.szin in szinek:
            szinek.remove(adat.szin)
        break
    elif adat.hazszam == haz-2:
        if adat.szin in szinek:
            szinek.remove(adat.szin)

print(f"A kerítés színe / állapota: {telek.szin}")
print(f"Egy lehetséges festési szín: {szinek[random.randint(0,len(szinek)-1)]}")

# 6
with open("utcakep.txt", "w", encoding="utf-8") as f:
    masodik_sor = ""
    for adat in telkek:
        if adat.oldal == 0:
            continue

        hazszam_str = str(adat.hazszam)
        masodik_sor += hazszam_str
        masodik_sor += " " * (adat.szelesseg - len(hazszam_str))
        
        for i in range(adat.szelesseg):
            f.write(adat.szin)

    f.write("\n")
    f.write(masodik_sor)