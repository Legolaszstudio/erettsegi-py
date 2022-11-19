from typing import List

class SorozatInfo:
    def __init__(self):
        self.datum: str = ""
        self.cim: str = ""
        self.evad: int = 0
        self.epizod: int = 0
        self.hossz: int = 0
        self.megnezte: bool = False

adatok: List[SorozatInfo] = []


# 6. feladat
def hetnapja(ev: int, ho: int, nap: int) -> str:
    napok = ["v", "h", "k", "sze", "cs", "p", "szo"]
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3:
        ev -= 1
    hetnapja = napok[
        (ev + ev // 4 - ev // 100 + ev // 400 + honapok[ho - 1] + nap) % 7
    ]
    return hetnapja


def main():
    # 1. feladat
    sorok = open("lista.txt", "r").readlines()
    lista_i = -1
    sor_i = 0
    for sornnel in sorok:
        sor = sornnel.rsplit("\n")[0]
        if sor_i % 5 == 0:
            lista_i += 1
            sor_i = 0
            adatok.append(SorozatInfo())
        if sor_i == 0:
            adatok[lista_i].datum = sor
        elif sor_i == 1:
            adatok[lista_i].cim = sor
        elif sor_i == 2:
            adatok[lista_i].evad = int(sor.split("x")[0])
            adatok[lista_i].epizod = int(sor.split("x")[1])
        elif sor_i == 3:
            adatok[lista_i].hossz = int(sor)
        elif sor_i == 4:
            adatok[lista_i].megnezte = (sor == "1")
        sor_i += 1

    # 2. feladat
    date_count = 0
    for adat in adatok:
        if adat.datum != "NI":
            date_count += 1
    print("2. feladat")
    print(
        f"A listában {date_count} db vetítési dátummal rendelkező epizód van.\n")

    # 3. feladat
    view_count = 0
    for adat in adatok:
        if adat.megnezte:
            view_count += 1
    print("3. feladat")
    print(
        f"A listában lévő epizódok {str(round(view_count/len(adatok)*100, 2)).replace('.', ',')}%-át látta.\n")

    # 4. feladat
    nezettseg_sum = 0
    for adat in adatok:
        if adat.megnezte:
            nezettseg_sum += adat.hossz
    nezettseg_nap = nezettseg_sum // (24 * 60)
    nezettseg_sum = nezettseg_sum % (24*60)
    nezettseg_ora = nezettseg_sum // 60
    nezettseg_perc = nezettseg_sum % 60
    print("4. feladat")
    print(
        f"Sorozatnézéssel {nezettseg_nap} napot {nezettseg_ora} órát és {nezettseg_perc} percet töltött.")

    # 5. feladat
    print("\n5. feladat")
    userdate = input("Adjon meg egy dátumot! Dátum=").split('.')
    user_ev = userdate[0]
    user_honap = userdate[1]
    user_nap = userdate[2]

    nem_latta: List[SorozatInfo] = []
    for adat in adatok:
        if adat.datum != "NI":
            splitted = adat.datum.split('.')
            ev = splitted[0]
            honap = splitted[1]
            nap = splitted[2]
            if ev <= user_ev and honap <= user_honap and nap <= user_nap and (adat.megnezte == False):
                nem_latta.append(adat)
    for adat in nem_latta:
        print(f"{adat.evad}x{str(adat.epizod).rjust(2, '0')}\t{adat.cim}")

    # 7. feladat
    print("\n7. feladat")
    user_nap = input("Adja meg a hét egy napját (például cs)! Nap= ")
    already_printed = []
    for adat in adatok:
        if adat.datum != "NI":
            splitted = adat.datum.split('.')
            ev = int(splitted[0])
            honap = int(splitted[1])
            nap = int(splitted[2])
            if hetnapja(ev, honap, nap) == user_nap and (adat.cim not in already_printed):
                already_printed.append(adat.cim)
                print(adat.cim)
    if len(already_printed) == 0:
        print("Az adott napon nem kerül adásba sorozat.")

    # 8. feladat
    f = open("summa.txt", "w")
    film_adat_map = {}
    for adat in adatok:
        if adat.cim not in film_adat_map:
            film_adat_map[adat.cim] = [0,0]
        film_adat_map[adat.cim][0] += adat.hossz
        film_adat_map[adat.cim][1] += 1
    for cim in film_adat_map.keys():
        f.write(f"{cim} {film_adat_map[cim][0]} {film_adat_map[cim][1]}\n")
    f.close()
        


main()
