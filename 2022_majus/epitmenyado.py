adosavok = []
telkek = []

class Telek:
    def __init__(self, adoszam, utca, hazszam, adosav, alapterulet):
        self.adoszam = adoszam
        self.utca = utca
        self.hazszam = hazszam
        self.adosav = adosav
        self.alapterulet = alapterulet

def main():
    inputdata = open('utca.txt', 'r').readlines()
    for line in inputdata:
        splits = line.rstrip('\n').split(' ')
        if adosavok.__len__() == 0:
            for sav in splits:
                adosavok.append(int(sav))
        else:
            telkek.append(
                Telek(
                    int(splits[0]),
                    splits[1],
                    splits[2],
                    splits[3],
                    int(splits[4]),
                )
            )
    # 2.feladat
    print(f"2. feladat. A mintában {telkek.__len__()} telek szerepel.")
    # 3 Feladat
    input_ado_szam = int(input("3. feladat. Egy tulajdonos adószáma: "))
    ado_result = list(filter(lambda x: x.adoszam == input_ado_szam, telkek))
    len(ado_result)
    if ado_result.__len__()== 0:
        print("Nem szerepel az adatállományban.")
    else:
        for result in ado_result:
            print(f"{result.utca} utca {result.hazszam}")
    #5. feladat
    # lista = [0] * 3
    # lista = [0 for i in range(3)]
    sav_count = [0,0,0]
    sav_sum = [0,0,0]
    #! Map vagy filter?
    for telek in telkek:
        if telek.adosav == 'A':
            sav_count[0] += 1
            sav_sum[0] += ado(telek)
        elif telek.adosav == 'B':
            sav_count[1] += 1
            sav_sum[1] += ado(telek)
        elif telek.adosav == 'C':
            sav_count[2] += 1
            sav_sum[2] += ado(telek)
    print(f"A sávba {sav_count[0]} telek esik, az adó {sav_sum[0]} Ft.")
    print(f"B sávba {sav_count[1]} telek esik, az adó {sav_sum[1]} Ft.")
    print(f"C sávba {sav_count[2]} telek esik, az adó {sav_sum[2]} Ft.")
    #6. feladat. A több sávba sorolt utcák: 
    print("6. feladat. A több sávba sorolt utcák:")
    utca_sets = [
        set(),
        set(),
        set()
    ]
    dups = set()

    #! Dupla for loop???
    """ for item in telkek:
        dups.append(item.utca) """
  
    for telek in telkek:
        if telek.adosav == 'A':
            utca_sets[0].add(telek.utca)
            if (telek.utca in utca_sets[1]) or (telek.utca in utca_sets[2]):
                dups.add(telek.utca)
        elif telek.adosav == 'B':
            utca_sets[1].add(telek.utca)
            if (telek.utca in utca_sets[0]) or (telek.utca in utca_sets[2]):
                dups.add(telek.utca)
        elif telek.adosav == 'C':
            utca_sets[2].add(telek.utca)
            if (telek.utca in utca_sets[0]) or (telek.utca in utca_sets[1]):
                dups.add(telek.utca)
    dups = list(dups)
    dups.sort()
    print("\n".join(dups))
    #7. feladat
    tulajdonos_dict = {}
    for telek in telkek:
        if telek.adoszam not in tulajdonos_dict:
            tulajdonos_dict[telek.adoszam] = 0
        tulajdonos_dict[telek.adoszam] += ado(telek)
    out = open("fizetendo.txt", "w")
    for adoszam in tulajdonos_dict.keys():
        out.write(f"{adoszam} {tulajdonos_dict[adoszam]}\n")



#4. feladat
def ado(epulet):
    if epulet.adosav == 'A':
        ado = adosavok[0]
    elif epulet.adosav == 'B':
        ado = adosavok[1]
    elif epulet.adosav == 'C':
        ado = adosavok[2]

    ado *= epulet.alapterulet
    if ado < 10000:
        ado = 0

    return ado
    

main()