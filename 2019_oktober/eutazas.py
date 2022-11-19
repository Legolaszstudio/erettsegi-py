from typing import List


class UtasAdat:
    def __init__(self, megallo: int, datum: str, azonosito: str, tipus: str, ervenyes: str):
        self.megallo = megallo

        self.datum = datum
        self.datum_ev = int(datum[:4])
        self.datum_honap = int(datum[4:6])
        self.datum_nap = int(datum[6:8])
        temp_ido = datum.split("-")[1]
        self.datum_ora = int(temp_ido[:2])
        self.datum_perc = int(temp_ido[2:])

        self.azonosito = azonosito
        self.tipus = tipus
        self.ervenyes = ervenyes
        self.berlet = False
        if self.ervenyes.__len__() == 8:
            self.berlet = True
            self.ervenyes_ev = int(ervenyes[:4])
            self.ervenyes_honap = int(ervenyes[4:6])
            self.ervenyes_nap = int(ervenyes[6:8])


adatok: List[UtasAdat] = []


# 6. feladat
def napokszama(e1: int, h1: int, n1: int, e2: int, h2: int, n2: int) -> int:
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 // 10
    d1 = 365*e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1*306 + 5) // 10 + n1 - 1
    h2 = (h2 + 9) % 12
    e2 = e2 - h2 // 10
    d2 = 365*e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2*306 + 5) // 10 + n2 - 1
    return d2 - d1


def main():
    # 1. feladat
    f = open("./utasadat.txt", "r").readlines()
    for line in f:
        adat_split = line.removesuffix('\n').split(" ")
        adatok.append(
            UtasAdat(
                int(adat_split[0]),
                adat_split[1],
                adat_split[2],
                adat_split[3],
                adat_split[4]
            )
        )

    # 2. feladat
    print("2. feladat")
    print(f"A buszra {len(adatok)} utas akart felszállni.")

    # 3. feladat
    print("3. feladat")
    ervenytelen = 0
    kedvezmenyes = 0
    ingyenes = 0
    for adat in adatok:
        if adat.berlet:
            if (adat.datum_ev > adat.ervenyes_ev) or\
                (adat.datum_ev == adat.ervenyes_ev and adat.datum_honap > adat.ervenyes_honap) or\
                    (adat.datum_ev == adat.ervenyes_ev and adat.datum_honap == adat.ervenyes_honap and adat.datum_nap > adat.ervenyes_nap):
                ervenytelen += 1
            else:
                if adat.tipus == "TAB" or\
                        adat.tipus == "NYB":
                    kedvezmenyes += 1
                elif adat.tipus == "NYP" or\
                    adat.tipus == "RVS" or\
                        adat.tipus == "GYK":
                    ingyenes += 1
        elif adat.ervenyes == "0":
            ervenytelen += 1
        else:
            if adat.tipus == "TAB" or\
                    adat.tipus == "NYB":
                kedvezmenyes += 1
            elif adat.tipus == "NYP" or\
                    adat.tipus == "RVS" or\
            adat.tipus == "GYK":
                ingyenes += 1
    print(f"A buszra {ervenytelen} utas nem szállhatott fel.")

    # 4. feladat
    print("4. feladat")
    felszallok = {}
    for adat in adatok:
        if adat.megallo not in felszallok:
            felszallok[adat.megallo] = 0
        felszallok[adat.megallo] += 1

    legnagyobb = felszallok[adatok[0].megallo]
    for key in felszallok.keys():
        if felszallok[key] > legnagyobb:
            legnagyobb = felszallok[key]
    for key in felszallok.keys():
        if felszallok[key] == legnagyobb:
            print(
                f"A legtöbb utas ({felszallok[key]} fő) a {key}. megállóban próbált felszállni.")
            break

    # 5. feladat
    print("5. feladat")
    print(f"Ingyenesen utazók száma: {ingyenes} fő")
    print(f"A kedvezményesen utazók száma: {kedvezmenyes} fő")

    # 7. feladat
    f = open("figyelmeztetes.txt", "w")
    for adat in adatok:
        if adat.berlet:
            if adat.datum_ev == adat.ervenyes_ev and\
                 adat.datum_honap == adat.ervenyes_honap and\
                    adat.ervenyes_nap >= adat.datum_nap:
                    kulonbseg = adat.ervenyes_nap - adat.datum_nap
                    if kulonbseg <= 3 and kulonbseg >= 0:
                        f.write(f"{adat.azonosito} {adat.ervenyes_ev}-{str(adat.ervenyes_honap).rjust(2, '0')}-{str(adat.ervenyes_nap).rjust(2, '0')}\n")
    f.close()

main()
