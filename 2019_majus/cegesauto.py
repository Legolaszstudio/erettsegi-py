from typing import List

class Auto:
    def __init__(self, nap: str, idopont: str, rendszam: str, szemely: str, kmszamlalo: str, behajtas: str):
        self.nap = int(nap)
        self.idopont = idopont
        self.rendszam = rendszam
        self.szemely = szemely
        self.kmszamlalo = int(kmszamlalo)
        self.behajtas = (behajtas == "1")

adatok: List[Auto] = []
def main():
    # 1. feladat
    f = open("autok.txt", "r", encoding="utf-8")
    for sor in f:
        adat = sor.removesuffix('\n').split(' ')
        adatok.append(Auto(adat[0], adat[1], adat[2], adat[3], adat[4], adat[5]))
    f.close()

    # 2. feladat
    print("2. feladat")
    elvitelek = list(filter(lambda x: not x.behajtas, adatok))
    elvitelek = elvitelek[elvitelek.__len__() - 1]
    print(f"{elvitelek.nap}. nap rendszám: {elvitelek.rendszam}")

    # 3. feladat
    print("3. feladat")
    nap_in = int(input("Nap: "))
    napi_adatok = list(filter(lambda x: x.nap == nap_in, adatok))
    for adat in napi_adatok:
        print(f"{adat.idopont} {adat.rendszam} {adat.szemely} {'be' if adat.behajtas else 'ki'}")

    # 4. feladat
    print("4. feladat")
    autok_visszahozatal = {}
    for adat in adatok:
        if adat.rendszam not in autok_visszahozatal:
            autok_visszahozatal[adat.rendszam] = None
        autok_visszahozatal[adat.rendszam] = adat.behajtas
    not_in_count = 0
    for behajtas in autok_visszahozatal.values():
        if not behajtas:
            not_in_count += 1
    print(f"A hónap végén {not_in_count} autót nem hoztak vissza.")

    # 5. feladat
    print("5. feladat")
    autok_tavolsag = {}
    autok_elozo_tavolsag = {}
    for adat in adatok:
        if adat.rendszam not in autok_tavolsag:
            autok_tavolsag[adat.rendszam] = 0
            autok_elozo_tavolsag[adat.rendszam] = adat.kmszamlalo
        else:
            autok_tavolsag[adat.rendszam] += adat.kmszamlalo - autok_elozo_tavolsag[adat.rendszam]
            autok_elozo_tavolsag[adat.rendszam] = adat.kmszamlalo
    for key in sorted(autok_tavolsag):
        print(f"{key} {autok_tavolsag[key]} km")

    # 6. feladat
    print("6. feladat")
    leghoszabb_ut = 0
    leghoszabb_ut_szemely = 0
    kifele_km = {}
    for adat in adatok:
        if not adat.behajtas:
            kifele_km[adat.rendszam] = adat.kmszamlalo
        else:
            tavolsag = adat.kmszamlalo - kifele_km[adat.rendszam]
            if tavolsag > leghoszabb_ut:
                leghoszabb_ut = tavolsag
                leghoszabb_ut_szemely = adat.szemely
    print(f"Leghosszabb út: {leghoszabb_ut} km, személy: {leghoszabb_ut_szemely}")

    # 7. feladat
    print("7. feladat")
    rendszam_input = input("Rendszám: ")
    rendszam_filtered = list(filter(lambda x: x.rendszam == rendszam_input, adatok))
    f = open(f"{rendszam_input}_menetlevel.txt", "w", encoding="utf-8")
    for adat in rendszam_filtered:
        if adat.behajtas:
            f.write(f"{adat.nap}. {adat.idopont}\t{adat.kmszamlalo} km\n")
        else:
            f.write(f"{adat.szemely}\t{adat.nap}. {adat.idopont}\t{adat.kmszamlalo} km\t")
    f.close()
    print("Menetlevél kész.")

main()
print()