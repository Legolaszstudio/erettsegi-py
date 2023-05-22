from typing import List
import sys

class Versenyzo:
    def __init__(self, nev, rajtszam, kategoria, versenyido, tavszazalek) -> None:
        self.nev: str = nev
        self.rajtszam: int = int(rajtszam)
        self.kategoria: str = kategoria
        self.versenyido: str = versenyido
        self.tavszazalek: int = int(tavszazalek)

adatok: List[Versenyzo] = []

f = open("./ub2017egyeni.txt", "r", encoding="utf-8")
f.readline()
for sor in f:
    adatok.append(
        Versenyzo(
            *sor.strip().split(";")
        )
    )
f.close()

print(f"3. feladat: Egyéni indulók: {len(adatok)} fő")

noi_sportolok = list(filter(
    lambda x: x.kategoria == "Noi" and x.tavszazalek == 100,
    adatok
))
print(f"4. feladat: Célba érkező női sportolók: {len(noi_sportolok)} fő")

sportolo_be = input("5. feladat: Kérem a sportoló nevét: ")
keres_result = None
for adat in adatok:
    if adat.nev == sportolo_be:
        keres_result = adat
        break
if keres_result is None:
    print("\tIndult egyéniben a sportoló? Nem")
else:
    print("\tIndult egyéniben a sportoló? Igen")
    print(f"\tTeljesítette a teljes távot? {'Igen' if keres_result.tavszazalek == 100 else 'Nem'}")


def IdoOraban(ido: str):
    ido_split = ido.split(":")
    return int(ido_split[0]) + (int(ido_split[1]) / 60) + (int(ido_split[2]) / 3600)

teljes_tav_ferfi = list(map(
    lambda x: IdoOraban(x.versenyido),
    list(
        filter(
            lambda x: x.kategoria == "Ferfi" and x.tavszazalek == 100,
            adatok
        )
    )
))
print(f"7. feladat: Átlagos idő: {str(sum(teljes_tav_ferfi)/len(teljes_tav_ferfi)).replace('.', ',')} óra")

print("8. feladat: Verseny győztesei")
noi_nyertes = min(adatok, key=lambda x: IdoOraban(x.versenyido) if (x.kategoria == "Noi" and x.tavszazalek == 100) else sys.maxsize)
print(f"\tNők: {noi_nyertes.nev} - {noi_nyertes.versenyido}")

ferfi_nyertes = min(adatok, key=lambda x: IdoOraban(x.versenyido) if (x.kategoria == "Ferfi" and x.tavszazalek == 100) else sys.maxsize)
print(f"\tFérfiak: {ferfi_nyertes.nev} - {ferfi_nyertes.versenyido}")
