from typing import List
from statistics import mean


class MetJelentes:
    def __init__(self, telepules, ido, szel, homerseklet):
        self.telepules = telepules
        self.ido = ido
        self.szel = szel
        self.homerseklet = homerseklet


adatok: List[MetJelentes] = []


def main():
    # 1. feladat
    f = open("tavirathu13.txt", "r").readlines()
    for line in f:
        sor_adatok = line.removesuffix("\n").split(" ")
        adatok.append(
            MetJelentes(
                sor_adatok[0],
                sor_adatok[1],
                sor_adatok[2],
                int(sor_adatok[3]),
            )
        )

    # 2. feladat
    print("2. feladat")
    user_telepcode = input("Adja meg egy település kódját! Település: ")
    last_dat_from_telep = list(
        filter(lambda x: x.telepules == user_telepcode, adatok))
    last_dat_from_telep = last_dat_from_telep[-1].ido
    print(
        f"Az utolsó mérési adat a megadott településről {last_dat_from_telep[:2]}:{last_dat_from_telep[2:]}-kor érkezett.")

    # 3. feladat
    print("3. feladat")
    leghidegebb_ho = adatok[0].homerseklet
    leghidegebb_bind = None
    legmelegebb_ho = adatok[0].homerseklet
    legmelegebb_bind = None
    for adat in adatok:
        if adat.homerseklet < leghidegebb_ho:
            leghidegebb_bind = adat
            leghidegebb_ho = adat.homerseklet
        if adat.homerseklet > legmelegebb_ho:
            legmelegebb_bind = adat
            legmelegebb_ho = adat.homerseklet
    print(
        f"A legalacsonyabb hőmérséklet: {leghidegebb_bind.telepules} {leghidegebb_bind.ido[:2]}:{leghidegebb_bind.ido[2:]} {leghidegebb_bind.homerseklet} fok.")
    print(
        f"A legmagasabb hőmérséklet: {legmelegebb_bind.telepules} {legmelegebb_bind.ido[:2]}:{legmelegebb_bind.ido[2:]} {legmelegebb_bind.homerseklet} fok.")

    # 4. feladat
    print("4. feladat")
    szelcsendes = []
    for adat in adatok:
        if adat.szel == "00000":
            szelcsendes.append(adat)
    if szelcsendes.__len__() == 0:
        print("Nem volt szélcsend a mérések idején.")
    else:
        for adat in szelcsendes:
            print(f"{adat.telepules} {adat.ido[:2]}:{adat.ido[2:]}")

    # 5. feladat
    print("5. feladat")
    osszes_adat_telepuleskent = {}
    osszes_ho = {}
    kozep_ho = {}
    kozep_ho_orak = {}
    for adat in adatok:
        if adat.telepules not in osszes_ho:
            osszes_ho[adat.telepules] = []
            osszes_adat_telepuleskent[adat.telepules] = []
            kozep_ho_orak[adat.telepules] = [False] * 4
        osszes_adat_telepuleskent[adat.telepules].append(adat)
        osszes_ho[adat.telepules].append(adat.homerseklet)
        if adat.ido.startswith("01") or\
            adat.ido.startswith("07") or\
                adat.ido.startswith("13") or\
                adat.ido.startswith("19"):
            if adat.telepules not in kozep_ho:
                kozep_ho[adat.telepules] = []
            kozep_ho[adat.telepules].append(adat.homerseklet)
        if adat.ido.startswith("01") and kozep_ho_orak[adat.telepules][0] == False:
            kozep_ho_orak[adat.telepules][0] = True
        if adat.ido.startswith("07") and kozep_ho_orak[adat.telepules][1] == False:
            kozep_ho_orak[adat.telepules][1] = True
        if adat.ido.startswith("13") and kozep_ho_orak[adat.telepules][2] == False:
            kozep_ho_orak[adat.telepules][2] = True
        if adat.ido.startswith("19") and kozep_ho_orak[adat.telepules][3] == False:
            kozep_ho_orak[adat.telepules][3] = True

    for key in osszes_ho.keys():
        print(key, end=" ")
        if (kozep_ho_orak[key][0] and kozep_ho_orak[key][1] and kozep_ho_orak[key][2] and kozep_ho_orak[key][3]) == False:
            print("NA;", end=" ")
        else:
            print(f"Középhőmérséklet: {round(mean(kozep_ho[key]))};", end=" ")

        legkisebb = min(osszes_ho[key])
        legnagyobb = max(osszes_ho[key])
        print(f"Hőmérséklet-ingadozás: {legnagyobb - legkisebb}")

    # 6. feladat
    print("6. feladat")
    for key in osszes_adat_telepuleskent.keys():
        f = open(f"./out/{key}.txt", "w")
        f.write(f"{key}\n")
        for adat in osszes_adat_telepuleskent[key]:
            f.write(f"{adat.ido[:2]}:{adat.ido[2:]} {int(adat.szel[3:]) * '#'}\n")
        f.close()
    print("A fájlok elkészültek.")


main()
print()
